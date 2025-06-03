@echo off
echo Running tests with Pytest (with retry logic)...
pytest --env qa --browser chrome --alluredir=allure-results --reruns 2 --reruns-delay 2

echo.
echo Generating Allure report...
allure generate allure-results --clean -o allure-report

echo.
echo Opening Allure report in browser...
start allure-report\index.html
