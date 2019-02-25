rd /s /q build
mkdir build
copy antivirus6.py build
copy curemod.py build
copy scanmod.py build
copy virus.kmd build
cd build
pyinstaller -F antivirus6.py