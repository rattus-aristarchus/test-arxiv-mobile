# A SAMPLE TEST BASE FOR THE [ARXIV MOBILE](https://f-droid.org/ru/packages/com.commonsware.android.arXiv/) APP

ArXiv is a website that has been allowing free access to scientific articles in certain fields since the beginning of 1990s. 

![Arxiv main page](/resources/images/arxiv.png)

In a nutshell:

![XKCD on the subject](/resources/images/arxiv_xkcd.png)

## Covered functionality:

- The first page of the mobile app
- Basic search

## Tech stack:
<img src="resources/icons/python.svg" height="40" width="40" />
<img src="resources/icons/selenium.png" height="40" width="40" />
<img src="resources/icons/selene.png" height="40" width="40" />
<img src="resources/icons/pytest.svg" height="40" width="40" />
<img src="resources/icons/allure_Report.svg" height="40" width="40" />
<img src="resources/icons/allure_EE.svg" height="40" width="40" />
<img src="resources/icons/jenkins.svg" height="40" width="40" />
<img src="resources/icons/jira.svg" height="40" width="40" />
<img src="resources/icons/browserstack.png" height="40" width="40" />
<img src="resources/icons/github.png" height="40" width="40" />
<img src="resources/icons/pycharm.png" height="40" width="40" />

## Local execution

To run the tests locally, do the following:

- clone the remote repository `https://github.com/rattus-aristarchus/test_arxiv.git`
- create an `.env` file with environment variables. The file should contain the following variables:
```
BROWSERSTACK_LOGIN=логин для browserstack (для запуска мобильных тестов)
BROWSERSTACK_PASSWORD=пароль для browserstack
```
- execute the following commands in the root folder of the project:
```sh
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry update
pytest tests
```


##  Remote execution

There is a [Selenoid](https://selenoid.autotests.cloud/#/) server with a [Jenkins](https://jenkins.autotests.cloud/job/mlankin_arxiv_tests/) project that can execute tests stored in this repository. To run the tests:
- open the project
- click "Build with Parameters"
- choose the build parameters (or just use default values)
- click "Build"

![Run in Jenkins](resources/images/jenkins_run.png)

### Allure Report

The Jenkins project is integrated with Allure Report. Once the job has run, it creates a link to the report:

![Allure Report](resources/images/allure_report.png)

The "Suites" tab has a detailed representation of how each test was executed, with steps, attachments, etc.

![Allure Report](resources/images/allure_report_tree.png)


### Отчеты в Allure Testops

The Jenkins project is also integrated with an [Allure Testops project](https://allure.autotests.cloud/project/3759/dashboards), which stores test results for all previous launches of the project. Why would we need that? 

- to have manual and automated test cases in the same interface, showing their collective coverage of features:
![Manual and automated test cases in Allure Testops](resources/images/allure_testops_manual_and_automated.png)

- to have defects that help categorize and quickly sort test failures:
![Allure Testops dashboard](resources/images/allure_testops_defects.png)

- to have aggregated statistics on test runs:
![Allure Testops dashboard](resources/images/allure_testops_dashboard.png)

### Jira

The Allure Testops project is integrated with Jira. Separate issues have been created for each detected bug (see [here](https://jira.autotests.cloud/browse/HOMEWORK-948) and [here](https://jira.autotests.cloud/browse/HOMEWORK-963)). Each issue is linked to an Allure Testops test case, and vice versa.

![Jira](resources/images/jira.png)