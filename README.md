Currency Data Scraper and SQL Importer
This script scrapes historical currency exchange data from a given URL, processes it into a structured format, and uploads it to a specified SQL Server database table. It is designed to automate the extraction and storage of currency data for later analysis or reporting.

Key Features
Data Extraction: Fetches historical exchange rate data from the specified API endpoint.
Data Processing: Converts JSON data to a pandas DataFrame and formats the timestamp into a date format. The data is then grouped by date to retain only the maximum values for each day.
Database Upload: Inserts processed data into a SQL Server table, devise_marroc, replacing existing data if the table already exists.
Prerequisites
Python Packages: Ensure the following packages are installed:
requests for HTTP requests.
pandas for data handling.
SQLAlchemy and pyodbc for database connection and operations.
Database Configuration: Update the following variables with your SQL Server details:
server_name
database
username
password
The script uses an ODBC connection string to connect to SQL Server. Make sure ODBC Driver 17 for SQL Server is installed and configured.
Usage
Call the function scrape_data(url) with the appropriate API endpoint.
Example: scrape_data('https://wise.com/rates/history+live?source=MAD&target=TND&length=5&resolution=daily&unit=year')
The script will automatically fetch, process, and upload the data to your SQL Server.
