@echo off
set PYTHONPATH=.
pytest tests/ --env qa --browser chrome --alluredir=allure-results
allure generate allure-results --clean -o allure-report
start allure-report\index.html
