# PYSIDE6 Minimal template

## Development Environment
- Code Editor: VS Code
- Python: python v3.12.x
- Cmake 
- MinGW Make

## Create virtual environmnet
```bash
python -m venv .venv
```

## Activate virtial environment
```bash
source .venv/Script/activat
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Opening Qt Desighner
```bash
.venv\Scripts\pyside6-designer.exe
```

## Steps to build 
1. Create build folder and open terminal in that folder.
1. Cmake build
```bash
cmake .. -G "MSYS Makefiles"
```
1. Make build
```bash
make
```
1. Run application

Ater successfull build the executable will generated as `run\bin\app.exe`. you can run this by double click on that or by cmd by following command
```bash
.\run\bin\app.exe
```
