# SauceDemo Automation Tests - Playwright (Python)

Author: Mohana Priya Ravikumar (https://github.com/R-Mohana-Priya/SauceDemo-Playwright-Python-Tests)

Follow these steps in your terminal or command prompt:

# 1. Navigate to your project folder

	cd C:\Users\YourUsername\source\repos\saucedemo_tests

# 2. Create and activate a virtual environment (venv)

	python -m venv venv
	
	venv\Scripts\activate.bat

# 3. Upgrade pip

	python -m pip install --upgrade pip

# 4. Install dependencies

	pip install pytest pytest-html pytest-xdist playwright

	python -m playwright install

# 5. Verify installations

	pytest --version

	python -m playwright --version

# 6. Run tests and generate HTML report

	pytest --html=report.html --self-contained-html

# 7. We can find the pytest HTML report in the path along with screenshots embedded to the report

	C:/Users/YourUsername/source/repos/saucedemo_tests/report.html

# 7. (Optional) Run tests in parallel using 5 workers
	
	pytest -n 5 --html=report.html --self-contained-html
