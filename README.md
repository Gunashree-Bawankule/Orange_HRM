# Orange_HRM
# Automation test engineering with Playwright sync
==============
## Scope

The first scope of this code is to automate and test the Demo Website


## Setup virtual environment

When project is created  in Pycharm, it would prompt user to setup a virtual environment.
Please select Poetry Environment and check checkbox install packages from pyproject.toml

Recommended **Python interpreter** version : **3.12.3**

Please keep in mind that Poetry needs to be installed on your system.

In case Poetry is missing please install through pip.

Please refer [Poetry Documentation](https://python-poetry.org/docs/)

##  To install dependencies:

In case all dependencies are not installed in your virtual environment. Please install it as below:

`poetry install`

Run playwright install to download browser binaries:

`playwright install`

## Please change below details in .env file for test execution :

    HEADLESS = headless browser True/False

    WINDOW_SIZE = Expected browser window size

Things to keep in mind while defining tags.
1. Tags should exist in the feature file.
2. Tags to include should be COMMA seperated e.g. "@login"
3. Tags to exclude should be SPACE seperated and should be prepended with a TILDE (~) symbol. e.g. "~@fail ~@pass"
4. The combination of to include and exclude tags should be SPACE seperated. e.g. "@login,~@fail ~@pass"


## [Sync Automation of Application locally]

1. by using Playwright setup on your linux machine
2. In sync playwright use behave BDD
3. create the requirement.txt file and update it

- #### features
    All the feature files and step definition file (python implementation of BDD steps)
    as well as the behave supporting files such as environment.py are maintained in this directory.

    1. **Feature files** : _gherkin language feature files are stored in application feature specific directory structure_
    2. **Steps**: _All the step definition files are stored in the Steps directory_
    3. **environment.py** : _This is backbone of the behave BDD framework.
       All the hook implementations are maintained in this file._
    4. **assertion** :
      _All assertions based on assertions needed for tests are defined here._

  2.  **User_flow** :
  Any future complex functionality implementation should be included in this directory.

    - login.py : _Application user and login/logout functions are managed here_
    - navigation.py : _All menu driven navigations are managed here_


- #### reports
  The allure report generates files on test execution and stores in this directory.
  Contents of this directory should not be checked in to the remote repository.
  Please follow [this commands](Allure report installation : Install allure framework from https://github.com/allure-framework/allure2/releases and add its path till bin to environment variables 
- 1) poetry add allure_behave 
- 2)behave -f allure_behave.formatter:AllureFormatter -o reports/ features
- 3)allure serve reports/)   [to set up allure report and access it.]

- #### screenshot
   All the screenshot recorded by the Playwright tool are stores in the reports directory. Contents of this directory should never be committed to git.
- #### video
    All the video recorded by the Playwright tool are stores in the video directory. Contents of this directory should never be committed to git.

**At project root directory below files are placed**

- .env : _All the environment variable are defined here_
- .flake8 : _Flake8 linter configuration details_
- .gitignore : _all file and folder which git should ignore are listed here_
- .pre-commit-config.yaml : Pre-commit hook configuration is maintained here.
Please refer to [this webpage](https://pre-commit.com/) for setting up pre-commit for your local setup_
- .reformat-gherkin.yaml : _BDD .feature formatting configuration is maintained here._
- poetry.lock : _Automatically generated/updated when poetry dependencies are added/updated/removed from pyproject.toml file. PLEASE DO NOT EDIT THIS FILE MANUALLY_
- pyproject.toml : _Poetry dependency management file. It is very important to maintain this file regularly. Only required dependencies should be added here._

 
- #### github Action
- use the proper git commands and push the codes on the git repository.
   

