# Python-WorkingWith-VirtualEnvs

Make sure you are working in a venv (Virtual Environment) before installing dependencies for this project.

Create the required venv with the following commands:
```
python3 -m venv .venv
source .venv/bin/activate
```

Then install dependencies by running the installDepsScript file.

> If working from vscode make sure you have selected the right interpreter (the one in the venv) with the command:\
Python: Select Interpreter\
Launch it by doing: Ctrl+Shift+P and typing the mentioned command.

## Matplotlib dependencies
For matplotlib to render in linux you need:
```bash
sudo apt install python3.8-venv
sudo apt install python3-tk
sudo apt install qt5-qmake
```

and get the dependencies for the project with:
```bash
pip install --upgrade pip
pip install matplotlib
pip install pyqt5
pip install pandas
```
or just get them from the current requirements.txt file with:
```bash
pip install -r requirements.txt
```