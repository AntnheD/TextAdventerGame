@echo off
echo Creating virtual environment if it does not exist...
if not exist textadventureenv (
    python -m venv textadventureenv
)

echo Activating virtual environment...
call textadventureenv\Scripts\activate

echo Checking necessary Python packages...

REM List of required Python packages
set packages=pygame colorama

REM Check if each package is installed
for %%i in (%packages%) do (
    pip show %%i >nul 2>&1
    if errorlevel 1 (
        echo Installing %%i...
        pip install %%i
    ) else (
        echo %%i is already installed.
    )
)

echo Ensuring sounds directory exists...
if not exist sounds (
    mkdir sounds
)

echo Checking necessary sound files...
if not exist sounds\game_over_sound.wav (
    echo Error: sounds\game_over_sound.wav is missing.
    exit /b 1
)

REM Additional checks for other sound files can be added here...

echo Compiling Python files...
python -m compileall .

echo Starting the game...
python main_game.py
