
@echo off
cd /d "%~dp0"

echo Installing packaging tools...
python -m pip install streamlit pandas seaborn matplotlib pyinstaller

if errorlevel 1 goto error

echo.
echo Building CO2 Explorer...
python -m PyInstaller --noconfirm --clean --onedir --name "CO2 Explorer" --collect-all streamlit --collect-all pandas --collect-all matplotlib --collect-all seaborn --add-data "app.py;." --add-data "annual-co2-emissions-per-country.csv;." --add-data "co-emissions-per-capita.csv;." --add-data "gdp-worldbank-constant-usd.csv;." --add-data "land-area-km.csv;." --add-data "population-with-un-projections.csv;." launcher.py

if errorlevel 1 goto error

echo.
echo BUILD COMPLETE!
echo Your application is in dist\CO2 Explorer\
pause
exit /b 0

:error
echo.
echo BUILD FAILED. Check the error messages above.
pause
exit /b 1
