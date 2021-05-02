from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector


class Customer_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1670x850+240+175")


        # --------------Variables for Database-------------------
        self.variable_ref = StringVar()
        x = random.randint(1000,9999)
        self.variable_ref.set(str(x))

        self.variable_customer_name = StringVar()
        self.variable_father_name = StringVar()
        self.variable_gender = StringVar()
        self.variable_dob = StringVar()
        self.variable_address = StringVar()
        self.variable_pincode = StringVar()
        self.variable_nationality = StringVar()
        self.variable_mobileNo = StringVar()
        self.variable_email = StringVar()
        self.variable_idProof = StringVar()
        self.variable_idNo = StringVar()



        # ------------Title----------
        lbl_title = Label(self.root, text="Add Customer's Details", font=("times new roman", 18, "bold"), bg="lightblue", fg="white")
        lbl_title.place(x=0, y=0, width=1670, height=50)


        # -------------Label Frame-------------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer's Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y= 50, width=500, height=550)


        # -----------Labels and Entries------------
        # Customer's reference
        customer_reference = Label(labelframeleft, text="Customer's Ref.", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_reference.grid(row=0, column=0, sticky=W)

        entry_reference = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_ref)
        entry_reference.grid(row=0, column=1)


        # Customer's Name
        customer_name = Label(labelframeleft, text="Customer's Name: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_name.grid(row=1, column=0, sticky=W)

        entry_customer_name = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_customer_name)
        entry_customer_name.grid(row=1, column=1)

 
        # Customer's father name
        customer_father_name = Label(labelframeleft, text="Father's Name: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_father_name.grid(row=2, column=0, sticky=W)

        entry_father_name = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_father_name)
        entry_father_name.grid(row=2, column=1)


        # Customer's gender combobox
        customer_gender = Label(labelframeleft, text="Gender: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_gender.grid(row=3, column=0, sticky=W)

        combobox_gender = ttk.Combobox(labelframeleft, font=("arial", 12), width=33, state="readonly", textvariable=self.variable_gender)
        combobox_gender["value"] = ("Male", "Female", "Others")
        combobox_gender.current(0)
        combobox_gender.grid(row=3, column=1)


        # Customer's Date of Birth
        customer_dob = Label(labelframeleft, text="Date of Birth: ", font=("arial", 12, "bold"), padx=0, pady=6)
        customer_dob.grid(row=4, column=0, sticky=W)

        combobox_date = ttk.Combobox(labelframeleft, font=("arial", 12), width=5, state="readonly", textvariable=self.variable_dob)
        combobox_date["value"] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", 
                                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", 
                                "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        combobox_date.current(0)
        combobox_date.place(x=155, y=145, width=50, height=25)


        combobox_months = ttk.Combobox(labelframeleft, font=("arial", 12), width=10, state="readonly")
        combobox_months["value"] = ("January", "February", "March", "April", "May", "June", 
                                    "July", "August", "September", "October", "November", "December")
        combobox_months.current(0)
        combobox_months.place(x=230, y=145, width=130, height=25)


        combobox_year = ttk.Combobox(labelframeleft, font=("arial", 12), width=10, state="readonly")
        combobox_year["value"] = ("1901", "1902", "1903", "1904", "1905", "1906", "1907", "1908", "1909", "1910", 
                                "1911", "1912", "1913", "1914", "1915", "1916", "1917", "1918", "1919", "1920", 
                                "1921", "1922", "1923", "1924", "1925", "1926", "1927", "1928", "1929", "1930", 
                                "1931", "1932", "1933", "1934", "1935", "1936", "1937", "1938", "1939", "1940", 
                                "1941", "1942", "1943", "1944", "1945", "1946", "1947", "1948", "1949", "1950", 
                                "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960", 
                                "1961", "1962", "1963", "1964", "1965", "1966", "1967", "1968", "1969", "1970", 
                                "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", 
                                "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", 
                                "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", 
                                "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", 
                                "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", 
                                "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030")
        combobox_year.current(99)
        combobox_year.place(x=385, y=145, width=90, height=25)

        
        # Customer's address
        customer_address = Label(labelframeleft, text="Address: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_address.grid(row=5, column=0, sticky=W)

        entry_address = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_address)
        entry_address.grid(row=5, column=1)


        # Customer's pincode
        customer_pincode = Label(labelframeleft, text="Pin Code: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_pincode.grid(row=6, column=0, sticky=W)

        entry_pincode = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_pincode)
        entry_pincode.grid(row=6, column=1)


        # Customer's nationality
        customer_nationality = Label(labelframeleft, text="Nationality: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_nationality.grid(row=7, column=0, sticky=W)

        entry_nationality = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_nationality)
        entry_nationality.grid(row=7, column=1)


        # Customer's mobile number
        customer_mobile_number = Label(labelframeleft, text="Mobile No.: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_mobile_number.grid(row=8, column=0, sticky=W)

        entry_mobile_number = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_mobileNo)
        entry_mobile_number.grid(row=8, column=1)


        # Customer's email
        customer_email = Label(labelframeleft, text="Email Id.: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_email.grid(row=9, column=0, sticky=W)

        entry_email = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_email)
        entry_email.grid(row=9, column=1)


        # Customer's id proof combobox
        customer_id_proof = Label(labelframeleft, text="Id. Proof: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_id_proof.grid(row=10, column=0, sticky=W)

        combobox_id_proof = ttk.Combobox(labelframeleft, font=("arial", 12), width=33, state="readonly", textvariable=self.variable_idProof)
        combobox_id_proof["value"] = ("Passport", "Aadhaar Card", "Voter Id.", "Driving Lisence", "Others")
        combobox_id_proof.current(0)
        combobox_id_proof.grid(row=10, column=1)


        # Customer's id_number
        customer_id_number = Label(labelframeleft, text="Id. Number: ", font=("arial", 12, "bold"), padx=2, pady=6)
        customer_id_number.grid(row=11, column=0, sticky=W)

        entry_id_number = ttk.Entry(labelframeleft, width=35, font=("arial", 13), textvariable=self.variable_idNo)
        entry_id_number.grid(row=11, column=1)



        # -------------Add, Update, Delete, and Reset Button------------
        btn_frame = Frame(labelframeleft, relief=RIDGE)
        btn_frame.place(x=0, y=450, width=490, height=40)

        btn_add = Button(btn_frame, text="Add", font=("arial", 14, "bold"), bg="green", fg="white", width=9, cursor="hand2")
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", font=("arial", 14, "bold"), bg="blue", fg="white", width=9, cursor="hand2")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", font=("arial", 14, "bold"), bg="red", fg="white", width=9, cursor="hand2")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", font=("arial", 14, "bold"), bg= "white", fg="blue", width=9, cursor="hand2")
        btn_reset.grid(row=0, column=3, padx=1)




        # --------------Search System----------------
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer's Data", font=("arial", 12, "bold"), padx=2)
        table_frame.place(x=520, y=50, width=900, height=550 )

        searchBy = Label(table_frame, font=("arial", 12, "bold"), text="Search By: ", bg="red", fg="white")
        searchBy.grid(row=0, column=0, sticky=W, padx=4)


        combobox_searchBy = ttk.Combobox(table_frame, font=("arial", 12), width=20, state="readonly")
        combobox_searchBy["value"] = ("Reference No.", "Customer's Name", "Mobile No.")
        combobox_searchBy.current(0)
        combobox_searchBy.grid(row=0, column=1, padx=4)
        
        searchBox = ttk.Entry(table_frame, width=35, font=("arial", 12))
        searchBox.grid(row=0, column=2, padx=4)

        btn_search = Button(table_frame, text="Search", font=("arial", 12, "bold"), bg="green", fg="white", width=9, cursor="hand2")
        btn_search.grid(row=0, column=3, padx=4)

        btn_showAll = Button(table_frame, text="Show All", font=("arial", 12, "bold"), bg="white", fg="blue", width=9, cursor="hand2")
        btn_showAll.grid(row=0, column=4)



        # --------------Data Table-------------
        data_table=Frame(table_frame, bd=2, relief=RIDGE)
        data_table.place(x=0, y=50, width=880, height=340)

        scroll_x = ttk.Scrollbar(data_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table, orient=VERTICAL)

        self.customer_data_table = ttk.Treeview(data_table, column=("reference", "name", "father's_Name", "gender", "dob", "address", "pincode", "nationality", 
                                                                     "mobileNo", "email", "idproof", "idno"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.customer_data_table.xview)
        scroll_y.config(command=self.customer_data_table.yview)


        self.customer_data_table.heading("reference", text="Reference. No.")
        self.customer_data_table.heading("name", text="Customer's Name.")
        self.customer_data_table.heading("father's_Name", text="Father's Name")
        self.customer_data_table.heading("gender", text="Gender")
        self.customer_data_table.heading("dob", text="Date of Birth")
        self.customer_data_table.heading("address", text="Address")
        self.customer_data_table.heading("pincode", text="Pin Code")
        self.customer_data_table.heading("nationality", text="Nationality")
        self.customer_data_table.heading("mobileNo", text="Mobile No.")
        self.customer_data_table.heading("email", text="Email Id")
        self.customer_data_table.heading("idproof", text="Id Proof")
        self.customer_data_table.heading("idno", text="Id No.")

        self.customer_data_table["show"] = "headings"

        self.customer_data_table.column
        self.customer_data_table.column("reference", width=120)
        self.customer_data_table.column("name", width=120)
        self.customer_data_table.column("father's_Name", width=120)
        self.customer_data_table.column("gender", width=120)
        self.customer_data_table.column("dob", width=120)
        self.customer_data_table.column("address", width=120)
        self.customer_data_table.column("pincode", width=120)
        self.customer_data_table.column("nationality", width=120)
        self.customer_data_table.column("mobileNo", width=120)
        self.customer_data_table.column("email", width=120)
        self.customer_data_table.column("idproof", width=120)
        self.customer_data_table.column("idno", width=120)

        self.customer_data_table.pack(fill=BOTH, expand=1)


    # def add_data(self):











if __name__ == "__main__":
    root = Tk()
    obj = Customer_Window(root)
    root.mainloop()