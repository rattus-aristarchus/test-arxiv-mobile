# A SAMPLE TEST BASE FOR THE [ARXIV EXPLORER](https://github.com/GarrettBeatty/arXiv-eXplorer) APP

ArXiv is a website that has been allowing free access to scientific articles in certain fields since the beginning of 1990s. ArXiv eXplorer is an Android app for the site which you can download [here](https://f-droid.org/en/packages/com.gbeatty.arxiv/). 

![The arxiv mobile app](/resources/images/arxiv_mobile_0.png) ![The arxiv mobile app](/resources/images/arxiv_mobile_1.png) ![The arxiv mobile app](/resources/images/arxiv_mobile_2.png) ![The arxiv mobile app](/resources/images/arxiv_mobile_3.png)

In a nutshell:

![XKCD on the subject](/resources/images/arxiv_xkcd.png)

## Covered functionality:

- The first page of the mobile app
- Basic search

A [separate project](https://github.com/rattus-aristarchus/test-arxiv) hosts tests for the arXiv site itself.

## Tech stack:
<img src="resources/icons/python.svg" height="40" width="40" /><img src="resources/icons/selenium.png" height="40" width="40" /><img src="resources/icons/selene.png" height="40" width="40" /><img src="resources/icons/pytest.svg" height="40" width="40" /><img src="resources/icons/allure_Report.svg" height="40" width="40" /><img src="resources/icons/allure_EE.svg" height="40" width="40" /><img src="resources/icons/jenkins.svg" height="40" width="40" /><img src="resources/icons/jira.svg" height="40" width="40" /><img src="resources/icons/browserstack.png" height="40" width="40" /><img src="resources/icons/github.png" height="40" width="40" /><img src="resources/icons/pycharm.png" height="40" width="40" />

## Local execution

To run the tests locally, do the following:

- clone the remote repository `https://github.com/rattus-aristarchus/test_arxiv_mobile.git`
- create an `.env` file with environment variables. The file should contain the following variables:
```
BROWSERSTACK_LOGIN=your login for browserstack 
BROWSERSTACK_PASSWORD=your password for browserstack
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

There is a [Jenkins](https://jenkins.autotests.cloud/job/007-niknal-arxiv-mobile/) project that can execute tests stored in this repository. To run the tests:
- open the project
- click "Build Now"

![Run in Jenkins](resources/images/jenkins_run.png)

### Allure Report

The Jenkins project is integrated with Allure Report. Once the job has run, it creates a link to the report:

![Allure Report](resources/images/allure_report.png)

The "Suites" tab has a detailed representation of how each test was executed, with steps, attachments, etc.

![Allure Report](resources/images/allure_report_tree.png)


### Allure Testops

The Jenkins project is also integrated with an [Allure Testops project](https://allure.autotests.cloud/project/3848/dashboards), which stores test results for all previous launches of the project. Why would we need that? 

- to have manual and automated test cases in the same interface, showing their collective coverage of features:
![Manual and automated test cases in Allure Testops](resources/images/allure_testops_manual_and_automated.png)

- to have defects that help categorize and quickly sort test failures:
![Allure Testops dashboard](resources/images/allure_testops_defects.png)

- to have aggregated statistics on test runs:
![Allure Testops dashboard](resources/images/allure_testops_dashboard.png)

### Jira

The Allure Testops project is integrated with Jira. Issues are linked to test cases in Testops.

![Jira](resources/images/jira.png)
