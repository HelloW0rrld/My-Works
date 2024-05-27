import customtkinter as ctk
from PIL import Image
import time
storageDir = r"C:\Users\MUSTAPHA\Desktop\Python Projects\Login window\Do Not CLick!!!!!!!!\WHY!!!!\AGain!!!!!!!\bRO!!\11.11.19\11.11.18\11.11.11\11.11.16\keys.txt"

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()

    usernameEntry.delete(0, ctk.END)
    passwordEntry.delete(0, ctk.END)

    with open(storageDir, "r") as file:
        content=file.readlines()
    usernamefound = any(username in str(line) for line in content)
    if usernamefound:
        for line in content:
            if username in line:
                username, checkedPass = line.split("@", 1)
                if checkedPass == password:
                    usernameEntry.configure(border_color="green", placeholder_text="...")
                    passwordEntry.configure(border_color="green", placeholder_text="...")
                    access()
                else:
                    usernameEntry.configure(border_color="gray", placeholder_text="")
                    passwordEntry.configure(border_color="red", placeholder_text="Invalid Password")
            else:
                usernameEntry.configure(border_color="red", placeholder_text="")
                passwordEntry.configure(border_color="gray", placeholder_text="Password...")
    time.sleep(1)

def signUp():
    print("Signing Up...")

root = ctk.CTk()
root.title("WI-FI")
root.minsize(450, 350)
root.maxsize(450, 350)

background = ctk.CTkFrame(master=root, fg_color="#474044")
background.pack(expand=True, fill=ctk.BOTH, padx=10, pady=10)
background.grid_rowconfigure(0, weight=1)
background.grid_rowconfigure(1, weight=1)
background.grid_rowconfigure(2, weight=0)
background.grid_rowconfigure(3, weight=1)
background.grid_columnconfigure(0, weight=1)

logo = ctk.CTkImage(dark_image=Image.open(r"C:\Users\MUSTAPHA\Desktop\Python Projects\Login window\Icons\black_wifi_icon2.png"), size=(150, 150))
logoLabel = ctk.CTkLabel(background, image=logo, text="")
logoLabel.grid(row=0, column=0, padx=10, pady=10)

usernameEntry = ctk.CTkEntry(master=background, height=20, width=200, placeholder_text="Username...", border_color="black", fg_color="#293132")
usernameEntry.grid(row=1, column=0, padx=0, pady=0)

passwordEntry = ctk.CTkEntry(master=background, height=20, width=200, show="x", placeholder_text="Password...", border_color="black", fg_color="#293132")
passwordEntry.grid(row=2, column=0, padx=0, pady=0)

rememberMe = ctk.CTkCheckBox(master=background, text=" Remember Me", width=200, hover_color="#547AA5", fg_color="#55BBFF")
rememberMe.grid(row=3, column=0, padx=70)
rememberMe.deselect()

submit = ctk.CTkButton(master=background, height=20, width=140, text="Submit", text_color="white", font=("", 14), fg_color="#293132", hover=True, hover_color="#1E3839", border_width=2, corner_radius=2, border_color="black", command=login)
submit.grid(row=1, column=1, padx=(20, 30))

signup = ctk.CTkButton(master=background, height=20, width=140, text="Sign-Up", text_color="white", font=("", 14), fg_color="#3B1B1B", hover=True, hover_color="#1E3839", border_width=2, corner_radius=2, border_color="black", command=signUp)
signup.grid(row=2, column=1, padx=(20, 30))

def access():
    print("working")
root.mainloop()
