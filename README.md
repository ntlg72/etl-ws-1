
# Workshop -001: Data engineer
By **Natalia López Gallego**

## Overview

This project involves efficient data management and advanced visualization techniques. Starting with a CSV file containing candidate data from selection processes, an application was developed to migrate this data into a relational database. Detailed analysis was performed on the database-stored data, and various insightful chart visualizations were generated.

Technologies utilized in this project include:

-   **Python**: For data handling and analysis.
    
-   **Jupyter Notebook**: For interactive data analysis and visualization.
    
-   **MySQL**: For database management.


## Table of Contents

- [Installation](#installation)
	- [Python Virtual Environment & Dependencies](#python-virtual-environment--dependencies)
		 - [Implementation](#implementation)
	- [Installing WSL 2 and Docker for MySQL Deployment](#installing-wsl-2-and-docker-for-mysql-deployment)
		 - [Enabling WSL 2](#enabling-wsl-2)
		 - [Installing Ubuntu](#installing-ubuntu)
  - [Turning on Docker Desktop WSL 2](#turning-on-docker-desktop-wsl-2)
	- [Confirming Docker Installation](#confirming-docker-installation)
- [Usage](#usage)
- [License](#license)


## Prerequisites  

Before you begin, ensure you have met the following requirements:
- **Operating System:** Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11
-  **Python:** 3.13 
-  **Dependencies:** WSL 2.

## Installation

Follow these steps to install **etl-ws-1**: 

1.  Clone the repository:

	```bash
    cd git clone https://github.com/ntlg72/etl-ws-1.git
    ```
2. Navigate to the project directory:
    ```bash
    cd etl-ws-1
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Python Virtual Environment & Dependencies

Virtual environments are essential for modern Python development, providing isolated spaces for each project to manage dependencies and avoid conflicts. By creating a dedicated virtual environment, projects gain their own set of installed packages, separate from the system's Python installation and other projects, preventing version clashes and namespace pollution. This isolation enables reproducible builds and simplifies project setup and deployment.

### Implementation

1. In the project directory, use the following command to create the virtual environment:
    ```bash
    py -m venv <environment_name>
    ```
2. The invocation of the activation script is platform-specific (`_<venv>_` must be replaced by the path to the directory containing the virtual environment):

```markdown
| Platform | Shell      | Command to activate virtual enviroment |  
|----------|------------|----------------------------------------
| Windows  | cmd.exe    | C:\> <venv>\Scripts\activate.bat       |     
|          | PowerShell | PS C:\> <venv>\Scripts\Activate.ps1    |    
```

3. The project directory contains a `requirements.txt` file listing all necessary dependencies. To install them, wihile the virtual enviroment is activated, run:
    ```bash
    pip install -r requirements.txt
    ```
   You can check the installed dependencies using:
    ```bash
    pip list
    ```

## Installing WSL 2 and Docker for MySQL Deployment

WSL 2 (Windows Subsystem for Linux 2) provides a lightweight, virtualized Linux environment that integrates seamlessly with Windows, enabling developers to run Linux-based tools and applications with improved performance and compatibility. Using a Dockerized MySQL image within WSL 2 allows for consistent, isolated, and portable development environments.

### Enabling WSL 2

1. Open PowerShell as Administrator.
2. Run:
    ```bash
    wsl --install
    ```
3. Set WSL 2 as the default version:
    ```bash
    wsl --set-default-version 2
    ```

### Installing Ubuntu

1. Run the following command in PowerShell:
    ```bash
    wsl.exe --install -d Ubuntu-24.04
    ```
2. Launch Ubuntu from the Start menu and complete the installation by creating a new user account.

### Turning on Docker Desktop WSL 2

Important: Uninstall any previous versions of Docker Engine and CLI installed through Linux distributions.

1. Download and install the latest Docker Desktop for Windows.
2. Follow the installation instructions and enable WSL 2 when prompted.
3. Start Docker Desktop.
4. Navigate to **Settings > General** and select **Use WSL 2 based engine**.
5. Click **Apply & Restart**.

### Confirming Docker Installation

1. Open a WSL distribution (Ubuntu-24.04).
2. Display the version and build number by entering:
    ```bash
    docker --version
    ```
3. Test the installation by running a simple built-in Docker image:
    ```bash
    docker run hello-world
    ```
## Usage 


## License

This project is licensed under the [MIT License](LICENSE).

> Written with [StackEdit](https://stackedit.io/).
