# Workshop -001: Data engineer
By **Natalia López Gallego**


## Overview

This project involves efficient data management and advanced visualization techniques. Starting with a CSV file containing candidate data from selection processes, an application was developed to migrate this data into a relational database. Detailed analysis was performed on the database-stored data, and various insightful chart visualizations were generated.

Technologies utilized in this project include:

-   **Python**: For data handling and analysis.
    
-   **Jupyter Notebook**: For interactive data analysis and visualization.
    
-   **MySQL**: For database management.

## Table of Contents

 - [Install](https://github.com/ntlg72/etl-ws-1?tab=readme-ov-file#install)
	 - [Python libraries](https://github.com/ntlg72/etl-ws-1?tab=readme-ov-file#python-libraries)
	 - [Installing WSL 2 and Docker on Ubuntu (WSL 2)](https://github.com/ntlg72/etl-ws-1?tab=readme-ov-file#installing-wsl-2-and-docker-on-ubuntu-wsl-2)
	 - [Setting Up MySQL Database with Docker](https://github.com/ntlg72/etl-ws-1?tab=readme-ov-file#setting-up-mysql-database-with-docker)
 - [Usage](https://github.com/ntlg72/etl-ws-1?tab=readme-ov-file#usage)
 - Documentation

## Install

### Python libraries

1. **Open a command prompt or terminal window**:
   - To access your command prompt or terminal window, search for "cmd" or "Terminal" in your system's search bar and open it.

2. **Navigate to the project directory**:
   - Change directory to where your project is located:
     ```bash
     cd path/to/your/project
     ```

3. **Create and activate a virtual environment**:
   - In the project directory, run the following commands:
     ```bash
     python -m venv venv
     ```
     ```bash
     source venv/bin/activate  # For Mac and Linux
     ```
     ```bash
     venv\Scripts\activate  # For Windows
     ```

4. **Install the required dependencies**:
   - Make sure you have a `requirements.txt` file in your project directory that lists all your dependencies. Then, run:
     ```bash
     pip install -r requirements.txt
     ```

5. **Install additional packages**:
   - To install SQLAlchemy, run:
     ```bash
     pip install SQLAlchemy
     ```
   - To install the MySQL driver, run:
     ```bash
     pip install mysql-connector-python
     ```
   - To install python-dotenv, run:
	     ```bash
	     pip install python-dotenv
	     ```
       
6. **Run the application**:
   - Start your application by running the following command:
     ```bash
     python app.py
     ```

7. **Deactivate the virtual environment**:
   - When you're done, you can deactivate the virtual environment by running:
     ```bash
     deactivate
     ```


### Installing WSL 2 and Docker on Ubuntu (WSL 2)


1. **Enable WSL 2:**
   - Open PowerShell as Administrator and run:
     ```powershell
     wsl --install
     ```
   - Set WSL 2 as the default version:
     ```powershell
     wsl --set-default-version 2
     ```

2. **Install Ubuntu:**
   - Run the following command in PowerShell:
     ```powershell
     wsl.exe --install -d Ubuntu-24.04
     ```
   - Launch Ubuntu from the Start menu and complete the installation by creating a new user account.

3. **Turn on Docker Desktop WSL 2:**

   **Important:** Uninstall any previous versions of Docker Engine and CLI installed through Linux distributions.

   - Download and install the latest Docker Desktop for Windows.
   - Follow the installation instructions and enable WSL 2 when prompted.
   - Start Docker Desktop.
   - Navigate to **Settings** > **General** and select **Use WSL 2 based engine**.
   - Click **Apply & Restart**.
   - 
4.  **Confirm Docker Installation:**  
- Open a WSL distribution (e.g., Ubuntu) and display the version and build number by entering:

	```bash
     docker --version
     ```
     - Test that your installation works correctly by running a simple built-in Docker image:
     ```bash
     docker run hello-world
     ```
     
Now Docker commands work from Windows using the new WSL 2 engine.


### Setting Up MySQL Database with Docker

1. **Pull MySQL Image:**
   - Open your terminal and run the following command to pull the MySQL image:
     ```bash
     docker pull mysql
     ```

2. **Run MySQL Container:**
   - Run the MySQL container and create a new database named `ws_001`:
     ```bash
     docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=your_password -e MYSQL_DATABASE=ws_001 -p 3307:3306  -d mysql
     ```

Where `mysql` is the name you want to assign to your container, and `your_password` is the password to be set for the MySQL root user.

3. **Access MySQL Container:**
   - Access the MySQL container's shell:
     ```bash
     docker exec -it mysql-container mysql -u root -p 
     ```

4. **Create the `candidates` Table:**
   - Once inside the MySQL shell, switch to the `ws_001` database:
     ```sql
     USE ws_001;
     ```
   - Create the `candidates` table:
     ```sql
     CREATE TABLE candidates (
         first_name VARCHAR(50),
         last_name VARCHAR(50),
         email VARCHAR(100),
         country VARCHAR(50),
         application_date DATE,
         yoe INT,
         seniority VARCHAR(50),
         technology VARCHAR(50),
         code_challenge_score INT,
         technical_interview VARCHAR(50)
     );
     ```



## Usage



## Documentation
