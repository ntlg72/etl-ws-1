Installation
================

This section explains why certain Python libraries and technologies are used in this project, and provides step-by-step instructions for setting up the project. Python must be installed previusly as well as an integrated development environment (IDE).

.. contents::
   :local:

Python virtual enviroment & dependencies
----------------------------------------

Virtual environments are essential for modern Python development, providing isolated spaces for each project to manage dependencies and avoid conflicts.  By creating a dedicated virtual environment, projects gain their own set of installed packages, separate from the system's Python installation and other projects, preventing version clashes and namespace pollution.  This isolation enables reproducible builds, as a requirements.txt file can capture the exact dependency configuration for easy recreation on other machines, ensuring consistent project behavior.  Furthermore, virtual environments simplify project setup and deployment by providing a clean, predictable environment and facilitating the replication of dependencies in target environments.   The following steps guide you through setting up a virtual environment and installing necessary dependencies to ensure a consistent and isolated project environment.

Implementation
""""""""""""""

1. In the project directory, the following command is used to create the virtual enviroment called "venv" in the IDE:

``py -m venv <environment_name>``

2. The activation and deactivation of the enviroment is done as follows with de **CMD** terminal:

``activate``

The "(venv)" indicates that the enviroment is activated.

.. image:: https://i.postimg.cc/T1dCsPsH/Captura-de-pantalla-2025-02-22-172014.png

To deactive use the command ``deactivate``.The absence of the "(venv)" indicates that the enviroment is deactivated.

3. The project directory contains a "requirements.txt" file in that lists all the dependencies needed. To install them, the ``pip install -r requirements.txt`` is run while the enviroment is activated. With the command pip list we can check that the dependencies have been installed.

.. image:: https://i.postimg.cc/15gp36Dr/Captura-de-pantalla-2025-02-22-174350.png


Installing WSL 2 and Docker for MySQL Deployment
------------------------------------------------

WSL 2 (Windows Subsystem for Linux 2) provides a lightweight, virtualized Linux environment that integrates seamlessly with Windows, enabling developers to run Linux-based tools and applications with improved performance and compatibility. Using a Dockerized MySQL image within WSL 2 allows for consistent, isolated, and portable development environments, which can be easily managed and shared. This approach ensures that the database setup is consistent across different development machines and avoids potential conflicts with other local services or applications.

- A Dockerized MySQL image is preferred over a local installation because it offers better isolation (preventing dependency conflicts), simplified management (easy start/stop/remove), environment consistency (reducing deployment issues), and streamlined updates/maintenance (easy version control and rollback).  
- WSL 2  is used in this case because it provides a Linux kernel running within Windows, enabling Docker Desktop to efficiently run Linux containers (like the MySQL image) using a lightweight virtual machine.


Enabling WSL 2
""""""""""""""

1. Open PowerShell as Administrator.
2. Run: ``wsl --install``
3. Set WSL 2 as the default version: ``wsl --set-default-version 2``

Installing Ubuntu
"""""""""""""""""

1. Run the following command in PowerShell: ``wsl.exe --install -d Ubuntu-24.04``
2. Launch Ubuntu from the Start menu and complete the installation by creating a new user account.

Turning on Docker Desktop WSL 2
"""""""""""""""""""""""""""""""

**Important:** Uninstall any previous versions of Docker Engine and CLI installed through Linux distributions.

1. Download and install the latest `Docker Desktop for Windows <https://www.docker.com/products/docker-desktop>`_.
2. Follow the installation instructions and enable WSL 2 when prompted.
3. Start Docker Desktop.
4. Navigate to Settings > General and select "Use WSL 2 based engine".
5. Click "Apply & Restart".

Confirming Docker Installation
""""""""""""""""""""""""""""""

1. Open a WSL distribution (Ubuntu-24.04).
2. Display the version and build number by entering: ``docker --version``

.. image:: https://i.postimg.cc/sXkZBHYP/Captura-de-pantalla-2025-02-22-180409.png

3. Test the installation by running a simple built-in Docker image: ``docker run hello-world``

.. image:: https://i.postimg.cc/NFR2R8D3/Captura-de-pantalla-2025-02-22-180614.png

Now Docker commands work from Windows using the new WSL 2 engine.

