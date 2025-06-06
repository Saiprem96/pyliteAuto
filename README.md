# 🧪 PyLite Auto Framework

A powerful and scalable Python-based Selenium automation framework with:

- ✅ PyTest + Selenium WebDriver
- ✅ Page Object Model (POM)
- ✅ Configurable via YAML
- ✅ Data-driven testing via Excel/CSV
- ✅ Allure Reports
- ✅ Retry logic for flaky tests
- ✅ CLI arguments for browser/environment

---

## 📁 Folder Structure

```
pyliteAuto/
├── config/              # YAML configs (env, browser, URL)
├── data/                # Test data (CSV / Excel)
├── drivers/             # WebDriver executables (chromedriver, etc.)
├── logs/                # Execution logs
├── pages/               # Page Object Model classes
├── reports/             # Custom reports (if any)
├── tests/               # All test cases
├── utils/               # Reusable utilities (config reader, logger, Excel reader)
├── allure-results/      # Raw Allure test output
├── allure-report/       # Final HTML report
├── conftest.py          # Global fixtures
├── run_tests.bat        # One-click test + report script
├── requirements.txt     # All dependencies
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Project

```bash
git clone https://github.com/your-username/pyliteAuto.git
cd pyliteAuto
```

### ✅ 2. Create Virtual Environment & Install Packages

```bash
pip install -r requirements.txt
```

### ✅ 3. Install Allure CLI (One-time)

#### For Windows using Scoop:

```bash
scoop install allure
```

✅ Make sure Java is installed and `allure --version` works in terminal.

---

## 🧪 Run Tests

### 🔹 Basic Test Run

```bash
pytest --env qa --browser chrome
```

### 🔹 Run with Allure Reporting

```bash
pytest --env qa --browser chrome --alluredir=allure-results
allure generate allure-results --clean -o allure-report
start allure-report\index.html
```

### 🔹 Or Use the .bat File

```bash
run_tests.bat
```

✅ This script runs tests, generates Allure report, and opens it automatically.

---

## 🔁 Retry Logic for Flaky Tests

Add to any test:

```python
@pytest.mark.flaky(reruns=2, reruns_delay=1)
```

Or apply globally from CLI:

```bash
pytest --reruns 2 --reruns-delay 1
```

---

## 📊 Allure Report Screenshot (Example)

![Allure Report](./sample-report.png)

---

## 📦 Technologies Used

- Python 3.x
- Selenium WebDriver
- PyTest
- Allure Reporting
- openpyxl (Excel support)
- PyYAML
- Logging module

---

## 👤 Author

**Saiprem Namburi**  
> Automation + Manual QA | API + UI Testing | PyTest + Selenium + Excel  
> 📫 saiprem@example.com *(update with your real email)*

---

## 📄 License

This project is licensed under the MIT License.
## 🌍 Live Allure Report

👉 [Click here to view the latest Allure Report](https://your-netlify-url.netlify.app)
#   P y t h o n _ s e l e n i u m _ p r o j e c t  
 