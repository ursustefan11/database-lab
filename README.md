# Data Engineering Project: database-lab
## Project Summary

This project is a showcase of data engineering skills using Python, SQL Server, and SSIS. It demonstrates how to generate fake and random data for different scenarios, how to design and implement an OLTP and an OLAP database, how to tune and optimize performance of SQL Server, and how to create an ETL pipeline using SSIS. The project can be used as a template or a reference for similar projects or as a learning resource for data engineering concepts and techniques, as the initial reason for creating this project was for experimenting.

## Project Overview

The project consists of three main components:

- A Python script that uses the Faker library and Multithreading to generate fake data for various tables in the OLTP database.
- A SQL Server database that hosts the OLTP and OLAP databases. The OLTP database has a normalized schema with multiple tables and relationships. The OLAP database has a denormalized, star schema with a few fact tables and multiple dimension tables.
- An SSIS package that implements an ETL pipeline to move data from the OLTP to the OLAP database. The package uses data flow tasks, control flow tasks, and variables to perform various transformations and validations on the data.

## How to Run the Project

### To run the project, you will need the following:

- Python 3.8 or higher
- SQL Server 2019 or higher
- SSIS 2019 or higher
- The necessary packages (you can find each package in "Python/main.py" at the top of the script and install using `pip install {package}` or `python -m pip install {package}`)

### The steps to run the project are as follows:

1. Clone or download this repository to your local machine.
2. Open the SQL Server Management Studio and create a new database. Run the scripts from the `SQL/Create Tables`, `SQL/Create Roles` and `SQL/Database Tuning` folder to create the tables and relationships and indexes for the OLTP and OLAP databases.
3. Open the Python script from the "Python/main.py" folder. Modify the parameters at the top of the script to specify the number of records, The thread number will be automatically updated based on the available logical processors on your machine. Run the script to populate the OLTP database with fake and random data.
4. Open the Visual Studio and create a new SSIS project. Add the package "ETL.dtsx" from the main folder to the project. Configure the connection managers to point to your SQL Server instance and the "OLTP" and "OLAP" databases.
5. Run the SSIS package "ETL.dtsx" to execute the ETL pipeline. You can monitor the progress and results of each task in the package.
6. You can now query and analyze the data in both databases using SQL queries or any BI tool of your choice.

### Contact
If you have any questions or need further assistance, I encourage you to reach out to me on LinkedIn. The most effective way to truly understand something is to teach others, so don't hesitate to contact me.
