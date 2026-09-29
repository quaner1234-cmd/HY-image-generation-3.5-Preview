// 本地 OCR — 用 macOS Vision 框架客观验证生成图里的文字是否渲染正确。
//
// 关键设计: usesLanguageCorrection = false
//   开启纠错时 OCR 会用语言模型"猜"出正确拼写, 会把渲染失败的乱码修正成
//   看起来正确的结果 —— 那正好会掩盖生图模型真实的文字渲染缺陷。
//   关闭后输出的是图上真实存在的字形, 才能作为判据。
//
// 用途: Hy Image Challenge Track 1 (Type & Layout) 的成败取决于文字是否正确,
//       主模型无读图能力, 本工具提供可重复的客观验证。
//
// 用法: ./ocr image.png [more.png ...]
// 输出: 每行 "置信度<TAB>识别文本"

import Foundation
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count > 1 else {
    FileHandle.standardError.write("usage: ocr <image> [image ...]\n".data(using: .utf8)!)
    exit(1)
}

for path in args.dropFirst() {
    let url = URL(fileURLWithPath: path)
    guard let image = NSImage(contentsOf: url),
          let cg = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        print("=== \(path) ===\nLOAD_FAIL")
        continue
    }

    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = false          // 见文件头说明
    request.recognitionLanguages = ["zh-Hans", "en-US"]

    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    do {
        try handler.perform([request])
    } catch {
        print("=== \(path) ===\nERROR \(error)")
        continue
    }

    print("=== \(path) ===")
    guard let observations = request.results, !observations.isEmpty else {
        print("(no text detected)")
        continue
    }
    for observation in observations {
        if let best = observation.topCandidates(1).first {
            print(String(format: "%.2f\t%@", best.confidence, best.string))
        }
    }
}
