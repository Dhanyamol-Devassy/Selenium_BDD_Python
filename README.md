# Selenium BDD Python Framework
This repository provides a framework for Selenium BDD (Behavior-Driven Development) testing using Python. It integrates with **Behave** for writing BDD-style tests and **Allure** for generating interactive reports. This setup also includes CI/CD integration via **GitHub Actions**.

Used https://automationexercise.com/ for sample testcases. 
![image](https://github.com/user-attachments/assets/ee7992c8-1fb4-4f10-af9f-3594b17fa26e)
## Cloning the Repository
1. Open your terminal.
2. Clone the repository:
   git clone https://github.com/Dhanyamol-Devassy/Selenium_BDD_Python.git
3. Navigate into the repository directory
   cd Selenium_BDD_Python
## Setting Up the Virtual Environment
It’s recommended to use a virtual environment for Python projects.
1.	Create a virtual environment:
python -m venv venv
2.	Activate the virtual environment:
On Windows: venv\Scripts\activate
On MacOS/Linux:: source venv/bin/activate
## Installing Dependencies
After activating the virtual environment, install the required dependencies using:
pip install -r requirements.txt
##Running Tests Locally
1.	To run the tests, use the following command:
behave
2.	The command will execute all .feature files located in the features/ directory and the corresponding Python step definitions.
## Generating Allure Reports
1.	To generate the Allure report, run the following command:
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results features

This will generate a folder named allure-results in the reports directory containing the necessary files to view the Allure report
## Viewing Allure Reports Locally
Once the tests have executed and the results are generated, you can view the Allure report by running:
Allure serve reports/allure-results.

This will start a local server and open the Allure report in your default web browser. You can view details such as test results, logs, and failure screenshots.
## GitHub Actions Workflow
CI/CD Integration
This repository includes a GitHub Actions workflow for Continuous Integration (CI) and Continuous Deployment (CD). The workflow is defined in: .github/workflows/ run_behave_tests.yml. It will automatically run on every push or pull request, executing the tests and generating Allure reports.

## Viewing Allure Reports from GitHub Actions
After running the tests through GitHub Actions:
1.	Go to the Actions tab in your GitHub repository.
2.	Select the latest workflow run.
3.	Scroll down to the Artifacts section and download Allure reports and screenshots.
4.	Open the index.html file from the Allure report to view the results. Can also be viewed at https://dhanyamol-devassy.github.io/Selenium_BDD_Python/index.html

![image](https://github.com/user-attachments/assets/b1eed6ce-c40a-4167-a190-b8111f23cb91)
![image](https://github.com/user-attachments/assets/e4a8add8-8f27-489f-977f-cbed8c6449c8)
![image](https://github.com/user-attachments/assets/b19aec8e-fbb3-42f6-83ca-9e286e540518)


     







