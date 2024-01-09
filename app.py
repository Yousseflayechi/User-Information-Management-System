from tkinter import *
from tkinter import ttk
import tkcalendar
import psycopg2 as pg2

class App:
    def __init__(self):
        root = Tk()
        root.title("APPLICATION")

        # Database Connection
        conn = pg2.connect(database='__', user='___', password='___')
        cur = conn.cursor()

        # Create a table if it doesn't exist
        cur.execute("CREATE TABLE IF NOT EXISTS user_info (id SERIAL PRIMARY KEY, "
                    "first_name VARCHAR(50), last_name VARCHAR(50), "
                    "gender VARCHAR(10), age INT, nationality VARCHAR(50), "
                    "born_date DATE, phone_number VARCHAR(15), email VARCHAR(50), "
                    "country VARCHAR(50), city VARCHAR(50), zipcode VARCHAR(10))")
        conn.commit()

        frame = Frame(root)
        frame.pack()

        label_frame = LabelFrame(frame, text='User Infos')
        label_frame.grid(row=0, column=0, padx=10, pady=10)

        # Labels for User Infos
        Label(label_frame, text='ID').grid(row=0, column=0)
        Label(label_frame, text='First Name').grid(row=0, column=1)
        Label(label_frame, text='Last Name').grid(row=0, column=2)
        Label(label_frame, text='Gender').grid(row=0, column=3)
        Label(label_frame, text='Age').grid(row=0, column=4)
        Label(label_frame, text='Nationality').grid(row=0, column=5)
        Label(label_frame, text='Born date').grid(row=2, column=0)

        # Entry widgets for User Infos
        id_entry = Entry(label_frame)
        first_name_entry = Entry(label_frame)
        last_name_entry = Entry(label_frame)
        gender_CB = ttk.Combobox(label_frame, values=['Men', 'Women', 'Other'])
        age_entry = Entry(label_frame)
        nat_entry = Entry(label_frame)
        birthday_date = tkcalendar.DateEntry(label_frame)

        id_entry.grid(row=1, column=0)
        first_name_entry.grid(row=1, column=1)
        last_name_entry.grid(row=1, column=2)
        gender_CB.grid(row=1, column=3)
        age_entry.grid(row=1, column=4)
        nat_entry.grid(row=1, column=5)
        birthday_date.grid(row=2, column=1)

        for w in label_frame.winfo_children():
            w.grid_configure(padx=10, pady=10)

        # Another Infos Frame
        frame2 = Frame(root)
        frame2.pack()

        label_frame2 = LabelFrame(frame2, text='Another Infos')
        label_frame2.grid(row=0, column=0, padx=10, pady=10)

        # Labels for Another Infos
        Label(label_frame2, text='Phone number').grid(row=0, column=0)
        Label(label_frame2, text='Email').grid(row=0, column=1)
        Label(label_frame2, text='Country').grid(row=2, column=0)
        Label(label_frame2, text='City').grid(row=2, column=1)
        Label(label_frame2, text='Zipcode').grid(row=2, column=2)

        # Entry widgets for Another Infos
        email_entry = Entry(label_frame2)
        phone_entry = Entry(label_frame2)
        country_entry = Entry(label_frame2)
        city_entry = Entry(label_frame2)
        zipcode_entry = Entry(label_frame2)

        email_entry.grid(row=1, column=0)
        phone_entry.grid(row=1, column=1)
        country_entry.grid(row=3, column=0)
        city_entry.grid(row=3, column=1)
        zipcode_entry.grid(row=3, column=2)

        for w in label_frame2.winfo_children():
            w.grid_configure(padx=10, pady=10)

        # Save Button
        save_button = Button(root, text="Save", command=lambda: self.save_data(
            id_entry.get(), first_name_entry.get(), last_name_entry.get(),
            gender_CB.get(), age_entry.get(), nat_entry.get(),
            birthday_date.get(), phone_entry.get(), email_entry.get(),
            country_entry.get(), city_entry.get(), zipcode_entry.get(),
            conn, cur))
        save_button.pack()

        root.mainloop()

    def save_data(self, id_val, first_name, last_name, gender, age, nationality,
                  born_date, phone_number, email, country, city, zipcode, conn, cur):
        try:
            query = "INSERT INTO user_info (id, first_name, last_name, gender, age, nationality, " \
                    "born_date, phone_number, email, country, city, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (id_val, first_name, last_name, gender, age, nationality, born_date,
                      phone_number, email, country, city, zipcode)
            cur.execute(query, values)
            conn.commit()
            print("Data saved successfully!")
        except Exception as e:
            print(f"Error: {e}")

App()
