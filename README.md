# 🤖 ALTEN Automation 🤖
This project is designed with Python, behave and Selenium. Follow the steps below to configure and run the project from scratch.

<br/>

## 📋 Requirements
Ensure you have the following programs and tools installed on your computer:

- [Git](https://git-scm.com/downloads): To clone the repository.
- [Python 3](https://www.python.org/downloads/): For project automation. Version `^3.10.9`.
- **pip (Only on macOS)**:
    ```bash
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    ```

<br/>

## 📦 Installation

1.  Open your terminal and clone the repository:
    ```bash
    git clone https://github.com/briansalashache/alten_automation.git
    cd alten_automation
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    ```
    - Windows
        ```bash
        .venv\Scripts\activate
        ```
    - Linux/macOS
        ```bash
        source .venv/bin/activate
        ```
    

3. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

<br/>

## 📁 Project structure
The repository is organized as follows:

    alten_automation/
    │
    ├── .venv/              # Python virtual environment directory
    │
    ├── features/           # Directory containing the BDD test specification files
    │   ├── pages/          # Directory containing classes for interacting with web pages using Selenium
    │   │   ├── base_page.py
    │   │   ├── contact_form_page.py
    │   │   └── ...
    │   ├── steps/          # Directory containing step definitions for BDD tests
    │   │   ├── contact_form.py
    │   │   └── ...
    │   ├── utilities/      # Directory containing files with useful functions for different aspects of the project
    │   │   ├── logging_config.py
    │   │   ├── report_utils.py
    │   │   └── ...
    │   ├── contact_form.feature
    │   ├── environment.py
    │   └── ...
    │
    ├── reports/    # Directory containing reports generated for each test (.log and .csv files and screenshots)
    │   └── ...    
    │
    ├── .gitignore          # File specifying the files and directories ignored by Git
    ├── Dockerfile          # File to build the Docker image
    ├── README.md           # Project documentation
    └── requirements.txt    # File specifying the project dependencies

<br/>

## ✅ Run tests

You can run the tests with the following command:
```bash
behave
```

You can also run the tests in a docker container:
1. First make sure you have **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** installed
2. Open Docker Desktop.
3. Run these commands:
    ```bash
    docker build . -t alten_automation:latest
    docker run -v .\\features:/features alten_automation:latest
    ```

<br/>

## 📄 Official documentation
For more detailed information, see the official documentation:
* **[Python](https://docs.python.org/3/)**
* **[Selenium](https://selenium-python.readthedocs.io/)**
* **[behave](https://behave.readthedocs.io/en/latest/)**
