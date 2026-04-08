@echo off
cd /d "%~dp0"
git add -A
git commit -m "update %date% %time%"
git -c credential.helper= -c http.extraHeader="Authorization: Basic YmFzaWxhaWExMjM6Z2hwX1Q0WVk3TEFiY2VaYVc3TlFTVHJ2VG9kTzhMU21NNzBZNXR4WQ==" push origin master
echo.
echo Done! Files uploaded to GitHub.
pause
