taskkill /f /t /im ip_offerer.exe
pyinstaller -F ip_offerer.py --noconsole
move dist\ip_offerer.exe ip_offerer.exe
