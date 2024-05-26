@echo off
SET VENV_DIR=venv

:: Check if virtual environment directory exists
IF NOT EXIST %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
) ELSE (
    echo Virtual environment already exists.
)

echo Activating virtual environment...
CALL %VENV_DIR%\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Starting the game...
python main_game.py

echo Deactivating virtual environment...
CALL deactivate

echo Done.
pause
