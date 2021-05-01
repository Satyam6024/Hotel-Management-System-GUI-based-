from tkinter import*
from PIL import Image, ImageTk
from customer import Customer_Window



class Hotel_Management_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1920x1080+0+0")



        # --------Header Image-------
        img1 = Image.open(r"S:\projects\GUI based Hotel Management System Using Database in MySQL\Images\header1.jpg")
        img1 = img1.resize((1920,140),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbling = Label(self.root, image=self.photoimg1, relief=RIDGE)
        lbling.place(x=0, y=0, width=1920, height=140)



        # ---------Main Frame-----------
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=140, width=1920, height=908)



        # -----------Navigation Menu-------------
        lbl_menu = Label(main_frame, text="Menu", font=("times new roman", 20, "bold"), bg="lightblue", fg="white", bd=1, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)



        # ---------Button Frame-----------
        btn_frame = Frame(main_frame, bd=0, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=230, height=180)

        customer_btn = Button(btn_frame, text="Customer", command=self.customer_details, width=22, font=("times new roman", 14, "bold"), bg="lightblue", fg="white", bd=0, cursor="hand2")
        customer_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="Room", width=22, font=("times new roman", 14, "bold"), bg="lightblue", fg="white", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="Details", width=22, font=("times new roman", 14, "bold"), bg="lightblue", fg="white", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="Report", width=22, font=("times new roman", 14, "bold"), bg="lightblue", fg="white", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LogOut", width=22, font=("times new roman", 14, "bold"), bg="lightblue", fg="white", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)



        # ---------Main Body Image-----------
        img3 = Image.open(r"S:\projects\GUI based Hotel Management System Using Database in MySQL\Images\body1.jpg")
        img3 = img3.resize((1670,900),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbling1 = Label(main_frame, image=self.photoimg3, bd=0, relief=RIDGE)
        lbling1.place(x=235, y=0, width=1670, height=900)



        # -----------Navigation Images--------
        img4 = Image.open(r"S:\projects\GUI based Hotel Management System Using Database in MySQL\Images\restaurant.jpg")
        img4 = img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbling2 = Label(main_frame, image=self.photoimg4, bd=0, relief=RIDGE)
        lbling2.place(x=0, y=225, width=230, height=210)



        img5 = Image.open(r"S:\projects\GUI based Hotel Management System Using Database in MySQL\Images\swimimgpool.jpg")
        img5 = img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbling3 = Label(main_frame, image=self.photoimg5, bd=0, relief=RIDGE)
        lbling3.place(x=0, y=440, width=230, height=190)



        img6 = Image.open(r"S:\projects\GUI based Hotel Management System Using Database in MySQL\Images\room.jpg")
        img6 = img6.resize((230,190),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lbling4 = Label(main_frame, image=self.photoimg6, bd=0, relief=RIDGE)
        lbling4.place(x=0, y=635, width=230, height=190)




    def customer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_Window(self.new_window)
        



if __name__ == "__main__":
    root = Tk()
    obj = Hotel_Management_System(root)
    root.mainloop()