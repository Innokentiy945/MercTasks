**How to run tests**

**Pre-Conditions:**
1) install python3
2) pip install pytest/selenium
3) pip install allure-pytest
4) download & install webdriver to C:/

**Run tests:**
`python -m pytest TaskTwo/Tests/Tests.py --alluredir=TaskTwo/Results `

**Generate report:**
`allure generate --clean -o TaskTwo/Reports TaskTwo/Results`