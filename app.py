from tkinter import *
from tkinter import ttk
import tkcalendar
import psycopg2 as pg2
import tksheet
from tkinter import messagebox

class App:
    def __init__(self):
        root = Tk()
        root.title("APPLICATION")
        root.geometry("700x800")

        # Database Connection
        conn = pg2.connect(database='user_info', user='postgres', password='YOURPASSWORD')
        cur = conn.cursor()

        # Create a table if it doesn't exist
        cur.execute("CREATE TABLE IF NOT EXISTS user_info (id SERIAL PRIMARY KEY, "
                    "first_name VARCHAR(50), last_name VARCHAR(50), "
                    "gender VARCHAR(10), age INT, nationality VARCHAR(50), "
                    "born_date DATE, phone_number VARCHAR(15), email VARCHAR(50), "
                    "country VARCHAR(50), city VARCHAR(50), zipcode VARCHAR(50))")
        conn.commit()

        frame = Frame(root)
        frame.pack()

        label_frame = LabelFrame(frame, text='User Infos')
        label_frame.grid(row=0, column=0, padx=10, pady=10)

        Label(label_frame, text='ID').grid(row=0, column=0)
        Label(label_frame, text='First Name').grid(row=0, column=1)
        Label(label_frame, text='Last Name').grid(row=0, column=2)
        Label(label_frame, text='Gender').grid(row=0, column=3)
        Label(label_frame, text='Age').grid(row=0, column=4)
        Label(label_frame, text='Nationality').grid(row=0, column=5)
        Label(label_frame, text='Born date').grid(row=2, column=0)

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

        Label(label_frame2, text='Phone number').grid(row=0, column=0)
        Label(label_frame2, text='Email').grid(row=0, column=1)
        Label(label_frame2, text='Country').grid(row=2, column=0)
        Label(label_frame2, text='City').grid(row=2, column=1)
        Label(label_frame2, text='Zipcode').grid(row=2, column=2)

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

        frame3 = Frame(root)
        frame3.pack()

        label_frame3 = LabelFrame(frame3, text='View and Update User Infos')
        label_frame3.grid(row=0, column=0, padx=10, pady=10)

        id_label = Label(label_frame3, text="Enter Id")
        id_label.grid(row=1, column=1)

        id_entry2_delete = Entry(label_frame3)
        id_entry2_delete.grid(row=1, column=2)

        deleteButton = Button(root, text="delete", command=lambda: self.delete_data(id_entry2_delete.get(), cur, conn))
        deleteButton.pack()

        frame4 = Frame(root)
        frame4.pack()
        label_frame4 = LabelFrame(frame4, text='Show Data')
        label_frame4.grid(row=0, column=0, padx=10, pady=30)

        showButton = Button(label_frame4, text="Show Data", command=lambda: self.show(cur, conn))
        showButton.pack()

        root.mainloop()

    def save_data(self, id_val, first_name, last_name, gender, age, nationality,
                  born_date, email, phone_number, country, city, zipcode, conn, cur):
        try:
            query = "INSERT INTO user_info (id, first_name, last_name, gender, age, nationality, " \
                    "born_date, email, phone_number, country, city, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (id_val, first_name, last_name, gender, age, nationality, born_date,
                      email, phone_number, country, city, zipcode)
            cur.execute(query, values)
            conn.commit()
            messagebox.showinfo("showinfo", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("showinfo", f"Error:{e}.")

    def delete_data(self, user_id, cur, conn):
        try:
            if user_id:
                query = "DELETE FROM user_info WHERE id = %s"
                values = (user_id,)
                cur.execute(query, values)
                conn.commit()
                messagebox.showinfo("showinfo", f"User with ID {user_id} has been deleted.")

            else:
                messagebox.showinfo("showinfo", f"User ID not provided..")

        except Exception as e:
            messagebox.showerror("showinfo", f"Error:{e}.")



    def show(self, cur, conn):
        new_window = Toplevel()
        new_window.title("Data")

        try:
            cur.execute("SELECT * FROM user_info")
            rows = cur.fetchall()
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")

        # Create a tksheet widget
        sheet = tksheet.Sheet(new_window)
        sheet.grid(sticky="nsew")

        # Set the headers
        headers = ["id", "first_name", "last_name", "gender", "age", "nationality",
                   "born_date", "phone_number", "email", "country", "city", "zipcode"]
        sheet.headers(headers)

        # Populate the data
        sheet.set_sheet_data(rows)

        # Enable sheet bindings
        sheet.enable_bindings(("single_select",
                               "row_select",
                               "column_width_resize",
                               "arrowkeys",
                               "right_click_popup_menu",
                               "rc_select",
                               "rc_insert_row",
                               "rc_delete_row",
                               "copy",
                               "cut",
                               "paste",
                               "delete",
                               "undo",
                               "edit_cell"))

App()
