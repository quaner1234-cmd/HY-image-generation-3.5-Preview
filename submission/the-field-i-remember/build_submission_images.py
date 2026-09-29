import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
BG = "#f3f0e9"
INK = "#252728"
MUTED = "#66717b"
LINE = "#9ba7b1"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    font_dir = Path(os.environ["WINDIR"]) / "Fonts" if "WINDIR" in os.environ else None
    filenames = [
        "segoeuib.ttf" if bold else "segoeui.ttf",
        "arialbd.ttf" if bold else "arial.ttf",
    ]
    names = [font_dir / name for name in filenames] if font_dir else []
    for name in names:
        if name.exists():
            return ImageFont.truetype(str(name), size=size)
    return ImageFont.load_default()


def contain(image: Image.Image, width: int, height: int) -> Image.Image:
    copy = image.copy()
    copy.thumbnail((width, height), Image.Resampling.LANCZOS)
    return copy


def centered(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str,
             used_font: ImageFont.ImageFont, fill: str, spacing: int = 8) -> None:
    draw.multiline_text(xy, text, font=used_font, fill=fill, anchor="mm",
                        align="center", spacing=spacing)


def build_before_after() -> None:
    source = Image.open(ROOT / "source-photo.jpg").convert("RGB")
    final = Image.open(ROOT / "final.png").convert("RGB")
    canvas = Image.new("RGB", (2040, 1460), BG)
    draw = ImageDraw.Draw(canvas)
    label_font = font(28, bold=True)

    for image, x, label in (
        (source, 40, "ORIGINAL PHOTO"),
        (final, 1040, "FINAL — HY IMAGE 3.5"),
    ):
        fitted = contain(image, 960, 1280)
        px = x + (960 - fitted.width) // 2
        py = 100 + (1280 - fitted.height) // 2
        canvas.paste(fitted, (px, py))
        centered(draw, (x + 480, 1410), label, label_font, INK)

    canvas.save(ROOT / "before-after.png", format="PNG", optimize=True)


def rounded_box(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int],
                title: str, subtitle: str | None = None) -> None:
    draw.rounded_rectangle(box, radius=22, fill="#fbfaf7", outline=LINE, width=3)
    cx = (box[0] + box[2]) // 2
    cy = (box[1] + box[3]) // 2
    if subtitle:
        centered(draw, (cx, cy - 18), title, font(34, bold=True), INK)
        centered(draw, (cx, cy + 40), subtitle, font(25), MUTED, spacing=6)
    else:
        centered(draw, (cx, cy), title, font(34, bold=True), INK)


def arrow(draw: ImageDraw.ImageDraw, x: int, y1: int, y2: int) -> None:
    draw.line((x, y1, x, y2 - 14), fill=MUTED, width=4)
    draw.polygon([(x - 10, y2 - 20), (x + 10, y2 - 20), (x, y2)], fill=MUTED)


def build_workflow() -> None:
    canvas = Image.new("RGB", (1600, 1500), BG)
    draw = ImageDraw.Draw(canvas)
    centered(draw, (800, 95), "THE FIELD I REMEMBER", font(42, bold=True), INK)
    centered(draw, (800, 145), "WORKFLOW", font(24, bold=True), MUTED)

    boxes = [
        (250, 220, 1350, 410),
        (250, 535, 1350, 725),
        (250, 850, 1350, 1080),
        (250, 1205, 1350, 1395),
    ]
    rounded_box(draw, boxes[0], "My hometown photograph")
    rounded_box(draw, boxes[1], "Visual-language exploration")
    rounded_box(
        draw,
        boxes[2],
        "Hy Image 3.5 Preview on GMI Cloud",
        "Reference-guided generation / editing",
    )
    rounded_box(draw, boxes[3], "The Field I Remember")
    arrow(draw, 800, boxes[0][3], boxes[1][1])
    arrow(draw, 800, boxes[1][3], boxes[2][1])
    arrow(draw, 800, boxes[2][3], boxes[3][1])
    canvas.save(ROOT / "workflow.png", format="PNG", optimize=True)


if __name__ == "__main__":
    build_before_after()
    build_workflow()
