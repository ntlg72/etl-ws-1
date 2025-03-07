

# Workshop -001: Data engineer
By **Natalia López Gallego**

## Overview

This project involves efficient data management and advanced visualization techniques. Starting with a CSV file containing candidate data from selection processes, an application was developed to migrate this data into a relational database. Detailed analysis was performed on the database-stored data, and various insightful chart visualizations were generated.

Technologies utilized in this project include:

-  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54): For data handling and analysis.
    
-    
   ![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white): For interactive data analysis and visualization.
-   ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white): For database management.


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
	- [Python Virtual Environment & Dependencies](#python-virtual-environment--dependencies)
		 - [Implementation](#implementation)
	- [Installing WSL 2 and Docker for PostgreSQL Deployment](#installing-wsl-2-and-docker-for-postgresql-deployment)
		 - [Enabling WSL 2](#enabling-wsl-2)
		 - [Installing Ubuntu](#installing-ubuntu)
  - [Turning on Docker Desktop WSL 2](#turning-on-docker-desktop-wsl-2)
	- [Confirming Docker Installation](#confirming-docker-installation)
  - [Setting Up PostgreSQL Database with Docker](#setting-up-postgresql-database-with-docker)
- [Usage](#usage)
- [Documentation](#documentation)


## Prerequisites  

Before you begin, ensure you have met the following requirements:
- [![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white)](#) Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11
-    [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#): 3.12.9
- [![Visual Studio Code](https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white)](#) or your prefered Python IDE.

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

## Installing WSL 2 and Docker for PostgreSQL Deployment

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

## Redash setup

Redash is an open-source data collaboration platform that enables you to connect to any data source, visualize data and share it.

### Cloning the Repository

We are going to self-host Redash using the official setup script. For this, you need to clone the Redash repository in your *WSL 2 Ubuntu 24.04* machine.

```bash
	git clone https://github.com/getredash/setup.git etl-ws-  	1/redash
	cd etl-ws-1/redash
 ```

This will clone the repository into a directory named `redash` (already existent inside this project’s directory) and change into that directory.


### Installation

When running the Redash setup script (`setup.sh`), you might encounter the following error:

``./setup.sh: 187: pwgen: not found``

This error indicates that the `pwgen` utility is missing. To fix this, install `pwgen` on your system.

Run:

``` bash
sudo apt update && sudo apt install -y pwgen
```

After installing `pwgen`, re-run the setup script in the `pwgen` directory:

``` bash
./setup.sh
```

### Mail Configuration (optional)

To enable Redash to send emails (e.g., for alerts or password resets), you must configure your SMTP settings. Depending on your installation method, these environment variables might reside in a `.env` file (e.g., `/opt/redash/.env`).

Add the following environment variables, replacing the placeholder values with your actual SMTP server details:

```bash 
REDASH_MAIL_SERVER=your_smtp_server_address
REDASH_MAIL_PORT=your_smtp_port
REDASH_MAIL_USE_TLS=true_or_false
REDASH_MAIL_USE_SSL=true_or_false
REDASH_MAIL_USERNAME=your_smtp_username
REDASH_MAIL_PASSWORD=your_smtp_password
REDASH_MAIL_DEFAULT_SENDER=your_default_sender_email
```

**Important:**

-   Set `REDASH_MAIL_USE_TLS` to `true` if your SMTP server requires TLS.
    
-   Set `REDASH_MAIL_USE_SSL` to `true` if your SMTP server requires SSL.
    
-   Do not set both TLS and SSL to `true` simultaneously.
    

After updating your mail configuration, restart your Redash services to apply the changes (`docker-compose up -d`, running `docker-compose restart` won’t be enough as it won’t read changes to env file). To test email configuration, you can run `docker-compose run --rm server manage send_test_mail`.

## Usage 

### Running a PostgreSQL Instance with Docker Compose

We will use a single container for our PostgreSQL instance with Docker Compose. In your command line or terminal of your WSL2 machine, navigate to this project's directory, and into the `postgresql` directory.

```bash
cd etl-ws-1/postgresql
```
<<<<<<< HEAD
Now you are going to update the existent `docker-compose.yml`. You must change the default MySQL credentials to suit your needs. Locate the database service section in your Docker Compose file and update the following environment variables with your own credentials:

- **MYSQL_USER:** The username to connect to your database.

- **MYSQL_PASSWORD:** The password for the specified user.

- **MYSQL_ROOT_PASSWORD:** The password for the root user.

Now you can start the container. Run `docker-compose up` (this might take a while on the first run because Docker needs to pull the containers). You should now have a MySQL instance running.

To access the MySQL container’s shell:

`docker exec -it mysql-db-1 mysql -u <user> -p <user_password> `

### Setting up a .env file for MySQL Credentials in WSL2 Ubuntu 24.04
=======
Now you are going to update the existent `docker-compose.yml`. You must change the default PostgreSQL credentials to suit your needs. Locate the database service section in your Docker Compose file and update the following environment variables with your own credentials:

The file works in the following way:

1.  **Database Initialization**:
    
    -   When the container starts, PostgreSQL reads the username and password from the secrets files (`postgres_user.txt`  and  `postgres_password.txt`).
        
    -   It creates a database named  `ws_001`  using the provided credentials.
    
2.  **Data Persistence**:
    
    -   The database data is stored in the local directory  `./my_db`  on the host machine, ensuring it persists across container restarts or deletions.
        
3.  **Accessing the Database**:
    
    -   External applications can connect to the database using  `localhost:5433`  (or the host's IP address) with the credentials specified in the secrets files.

### **Steps to Use:**

1.  Create the secrets files in the `postgresql` directory:
    
    -   `postgres_user.txt`: Add the database username (e.g.,  `admin`).
        
    -   `postgres_password.txt`: Add the database password (e.g.,  `password123`).

2. Create the volume directory in the  `postgresql` directory :

	  ```bash
	 mkdir my_db
	```

	##### **Example Directory Structure:**
	├── docker-compose.yml
	├── postgres_user.txt
	├── postgres_password.txt
	└── my_db/
        
3.  Run the Docker Compose file:
    
	  ```bash
	 docker-compose up -d
	```
   
4.  Access the PostgreSQL command-line client:
	```yaml
	docker exec -it pg psql -U <your_user> -d ws_001 -p 5433
	```
### Setting up a .env file for PostgreSQL Credentials in WSL2 Ubuntu 24.04
>>>>>>> 5eeae01 (readme updated)

A `.env` file is needed to store your MySQL credentials securely, including the WSL2 IP address and the password  set up.

**1. Locate the project directory:**

Navigate to the directory where this repository has been cloned This is where you'll create the `.env` file. In the terminal it can be be done trhought the following commands:
```
    cd /path/to/cloned/repository/directory
```
**2. Create the .env file:**

In the project directory, create a new file named `.env` (no file extension). You can do this from the command line:
```
touch .env
```

Or using a text editor.

**3. Add your PostgreSQL credentials to the .env file:**

Open the `.env` file with a text editor and add the following lines, replacing the placeholders with your actual values:

```
	PG_USER=your_postgres_user
    PG_PASSWORD=your_postgres_user_password
    PG_HOST=your_wsl2_ip_address
    PG_PORT=5433
    PG_DATABASE=ws_001
```
-   **`PG_USER`:** Your PostgreSQL username.
-   **`PG_PASSWORD`:** The password you set for your PostgreSQL user.
-   **`PG_HOST`:** This is _crucial_. You need the IP address of your WSL2 instance. See step 4 below to find this.
-   **`PG_DATABASE`:** The PostgreSQL database created with the docker compose file.
-   **`PG_PORT`:** The port MySQL is listening on port 5433 according to our docker compose file.

**4. Find your WSL2 IP Address:**

There are several ways to find the IP address of your WSL2 instance:

-   **From WSL:** Open your WSL2 terminal and run:
    
    Bash
    
    ```
    ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1

    ```
    
-   **From Windows (PowerShell):** Open PowerShell as administrator and run:
    
    PowerShell
    
    ```
    wsl hostname -I
    ```
    
-   **From Windows (Command Prompt):** Open command prompt and run:
    
    ```
    wsl hostname -I
    ```
    

The output will be the IP address of your WSL2 instance. Use this IP address for `MYSQL_HOST` in your `.env` file.

**5. Secure the .env file:**

The `.env` file contains sensitive information. It's _extremely important_ to prevent it from being accidentally committed to version control (like Git). Add `.env` to your `.gitignore` file:

```
.env
```

This will tell Git to ignore the `.env` file.

## Using Redash

### Login to Redash

Once the setup is complete and the Redash services are running, you can access the Redash web interface using your browser. By default, the Redash instance will be available at:

http://localhost:5000/

Open this URL in your web browser to start using Redash.

### Connect to a Data Source

Before you can write queries, you need to connect Redash to a data source. Navigate to the 'Settings' and add your data source (select "PostgreSQL") with the appropriate credentials.

![Connect to a Data Source](https://redash.io/assets/images/docs/gitbook/add-data-source.gif)

### How to create a dashboard

A dashboard is composed of widgets, which can be any visualization created from the query source page. The dashboard is created by clicking on the “New Dashboard” button on the homepage, assigning it a name, and then clicking on the “save” button.

You can also, at any time, create a dashboard by clicking on the dropdown menu on the fixed navbar.

After this, you will have an empty page with the dashboard name. The next steps will explain how to create the widgets to fill the dashboard.

### Create query

Redash comes with an interface to write and run queries on the platform.

Just click on the “New Query” button, type a name for your query (otherwise, it will be considered a draft), copy and paste the query inside the text area, and click on the “save” button.

![Create query](https://redash.io/assets/images/docs/gifs/dashboards/dashboards.gif)

### Create visualizations for the query

All saved queries by default have a ‘Table’ visualization created. You can create more visualizations after the query runs for the first time.

The options are:

- Chart
- Cohort
- Counter
- Map
- And more.

Click on the “+ New Visualization” button, select the visualization type, set a name and options for the visualization, and then click “save”.

Type the name of the query to see the visualizations available for the query.

Choose the visualization, optionally set the widget’s size (Regular or Double), and click the “Add to Dashboard” button.

![Create visualizations for the query](https://redash.io/assets/images/docs/gifs/visualization/new_viz.gif)


## Documentation 
Documentation for this project was made using [![Read the Docs](https://img.shields.io/badge/Read%20the%20Docs-8CA1AF?logo=readthedocs&logoColor=fff)](#).


> Written with [StackEdit](https://stackedit.io/).