## User-Information-Management-System

# Overview
This Python script implements a simple user information management system using the Tkinter GUI toolkit. It allows users to input and save personal information, such as name, gender, age, contact details, and more. The application stores the data in a PostgreSQL database.

# Features
- Input and store user information in a PostgreSQL database.
- Two frames for different categories of user information.
- Save button to store entered data in the database.
- User Information Entry:
ID
First Name
Last Name
Gender
Age
Nationality
Born date

- Additional Information:

Phone Number
Email
Country
City
Zipcode
Save Button:

- View and Update:
Allows users to enter the ID of a user to delete their information.

- Delete Button:

Deletes user information based on the provided ID.

- Show Data:

Displays all stored user information in a separate window using a tksheet (Tkinter spreadsheet) widget.

# Troubleshooting
- Database Connection Issues:
If you encounter issues connecting to the PostgreSQL database, ensure that the database server is running, and the provided credentials are correct.

- Dependency Installation:
Make sure you have installed all the required dependencies using the specified versions.

# Prerequisites
Before running the script, ensure you have the following installed:

- Python 3.x
- Tkinter library
- ttk (themed widgets) library
- tkcalendar library
- psycopg2 library
- PostgreSQL Database




# Setup
1. Install the required libraries:
   ```bash
   pip install tk tkcalendar psycopg2
   
2 Create a PostgreSQL database with the following structure:

CREATE TABLE IF NOT EXISTS user_info (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    age INT,
    nationality VARCHAR(50),
    born_date DATE,
    phone_number VARCHAR(15),
    email VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(50),
    zipcode VARCHAR(10)
);

3 Update the database connection details in the code (database, user, password in the pg2.connect call).

4 Run the application 

# Usage
Fill in the user information in the respective entry fields.
Click the "Save" button to store the data in the PostgreSQL database.

# Contributors
Youssef Layechi
