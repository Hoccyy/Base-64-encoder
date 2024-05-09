@echo off

rem Activate the virtual environment (if needed)
if not exist venv\Scripts\activate.bat (
    python -m venv venv
)

rem Run the Python script
venv\Scripts\activate
python main.py

rem Pause to see output (optional)
pause

rem Deactivate the virtual environment
deactivate
