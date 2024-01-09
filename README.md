# User-Information-Management-System

Overview
This Python script implements a simple user information management system using the Tkinter GUI toolkit. It allows users to input and save personal information, such as name, gender, age, contact details, and more. The application stores the data in a PostgreSQL database.

Prerequisites
Before running the script, ensure you have the following installed:

Python 3
Tkinter library
ttk from Tkinter
tkcalendar library
psycopg2 library
PostgreSQL database (with appropriate credentials)
How to Use
Database Configuration:

Update the database connection details (database name, username, and password) in the pg2.connect() statement within the script.
Table Creation:

The script creates a table named user_info in the PostgreSQL database to store user information. If the table doesn't exist, it will be created automatically.
Run the Script:

Execute the script, and a GUI window will appear with fields to input user information.
Input User Information:

Enter the required details in the respective fields.
The 'Born date' field includes a date picker using the tkcalendar library.
Save Data:

Click the "Save" button to store the entered data in the PostgreSQL database.
Database Schema
The script defines a table named user_info with the following columns:

id (Serial): Unique identifier for each user.
first_name (VARCHAR): First name of the user.
last_name (VARCHAR): Last name of the user.
gender (VARCHAR): Gender of the user (Men, Women, Other).
age (INT): Age of the user.
nationality (VARCHAR): Nationality of the user.
born_date (DATE): Date of birth of the user.
phone_number (VARCHAR): Phone number of the user.
email (VARCHAR): Email address of the user.
country (VARCHAR): Country of residence of the user.
city (VARCHAR): City of residence of the user.
zipcode (VARCHAR): Zipcode of the user's location.
Data Saving
The entered user information is saved to the PostgreSQL database when the "Save" button is clicked. A simple error handling mechanism is in place to catch and print any exceptions that may occur during the data-saving process.

Feel free to customize the script according to your specific requirements.
