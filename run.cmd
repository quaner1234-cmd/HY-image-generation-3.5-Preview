@echo off
REM 极薄包装: 只负责切到仓库目录并调用 gen.py, 参数原样透传。
REM 核心生图逻辑全部在 gen.py, 本文件不含任何凭据。
setlocal
pushd "%~dp0"
python gen.py %*
set "RC=%ERRORLEVEL%"
popd
exit /b %RC%
