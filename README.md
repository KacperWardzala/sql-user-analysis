# SQL Project - User Sessions and Purchases Analysis

This project is an analysis of user data, specifically focusing on user sessions and purchase behavior. The data is stored in a PostgreSQL database, and the project includes SQL queries for analysis and Python scripts for visualization.

## Project Structure

sql_project/ 
├── data/ 

│ ├── users_data.csv # CSV file containing user data 

│ ├── sessions_data.csv # CSV file containing session data 

│ └── purchases_data.csv # CSV file containing purchase data 

├── sql/ 

│ ├── schema.sql # Database schema definitions 

│ └── analysis_queries.sql # Analytical SQL queries 

├── scripts/ 

│ ├── load_data.py # Script to load CSV data into PostgreSQL 

│ └── visualize_data.py # Script to generate visualizations from the data 

├── README.md # Project documentation



## Requirements

Before running the project, make sure you have the following dependencies installed:

- Python 3.7+
- PostgreSQL
- Required Python packages (can be installed via `requirements.txt`)

### Python Packages:
- `pandas`
- `matplotlib`
- `sqlalchemy`
- `psycopg2`
- `python-dotenv`

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```
Database Setup
PostgreSQL Database: This project assumes that you have a PostgreSQL database set up. You can change the database connection details in the .env file.

Creating the Database Schema: The schema.sql file contains the necessary SQL to create the users, sessions, and purchases tables. You can run the SQL script to set up the schema in your PostgreSQL database.

```bash
psql -U your_user -d your_database -f sql/schema.sql
```
Loading the Data: The data in the data/ folder needs to be loaded into the PostgreSQL database. You can use the load_data.py script to load the data from the CSV files into the database.

```bash
python scripts/load_data.py
```
## SQL Queries
The analysis_queries.sql file contains various SQL queries to analyze the data, such as:

- Number of sessions per user

- Average purchase amount per user

- Number of purchases per day

- User distribution by country

You can run these queries in PostgreSQL to get insights from the data.

## Data Visualization
The visualize_data.py script generates visualizations using the data from the database. The following plots are created:

1. Sessions per User: A bar chart showing the number of sessions for each user.

2. Average Purchase Amount per User: A bar chart showing the average purchase amount for each user.

3. Purchases per Day: A bar chart showing the number of purchases made each day.

4. User Distribution by Country: A bar chart showing the number of users per country.

To generate the visualizations, run the following command:

```bash
python scripts/visualize_data.py
```
The plots will be saved in the plots/ directory.
