# Introduction
- This project selenium-ketangpai is main to build a basic framework demo of web automation testing.
- This project is aimed at automation test engineers and test development engineers
- The tested site is: https://v4.ketangpai.com/
#### Testcases included:
1. Login （smoke test && exception test)
1. AddClass (smoke test)
1. Attendance (smoke test)

  In total of 9 testcases
  
#### Framework or Pattern included
- Selenium
- Pytest
- PageObject


  
#### Requirements
- pip install -r requirements.txt
- you will also need to install Chromedriver



---



# How To Run?
#### you have 2 methods to run this project
1. terminal

```
pytest -s -v --alluredir=allure-report-files
```
2. run .py

```
__init__.py
```

if you require a report , please run the following code in your termial as well

```
allure serve allure-report-files
```


