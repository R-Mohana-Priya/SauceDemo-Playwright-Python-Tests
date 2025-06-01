# SauceDemo Automation Tests - Playwright (Python)

**Author:** Mohana Priya Ravikumar  
**GitHub Repository:** [SauceDemo-Playwright-Python-Tests](https://github.com/R-Mohana-Priya/SauceDemo-Playwright-Python-Tests)

This project contains automated end-to-end tests for [SauceDemo](https://www.saucedemo.com/) using [Playwright](https://playwright.dev/python/) and [Pytest](https://docs.pytest.org/).

---

### 1. Clone the repository
git clone https://github.com/R-Mohana-Priya/SauceDemo-Playwright-Python-Tests.git

### 2. Navigate into the project test folder
cd SauceDemo-Playwright-Python-Tests/saucedemo_tests

### 3. Create a virtual environment
python -m venv venv

### 4. Activate the virtual environment (Windows)
venv\Scripts\activate.bat

### (If you're on macOS/Linux, use this instead)
ource venv/bin/activate

### 5. Upgrade pip
python -m pip install --upgrade pip

### 6. Install required Python packages and Playwright browser drivers
pip install pytest pytest-html pytest-xdist playwright
python -m playwright install

(Optional) Verify installations
pytest --version
python -m playwright --version

### 7. Run the tests with an HTML report
pytest --html=report.html --self-contained-html

(Optional) Run tests in parallel with 5 workers and generate the report
pytest -n 5 --html=report.html --self-contained-html


