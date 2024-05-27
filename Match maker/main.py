import customtkinter as ctk
import random as r
import time

def submit():
    global steps
    firstnameText = firstname.get(1.0, ctk.END).strip()
    secondnameText = secondname.get(1.0, ctk.END).strip()

    if len(firstnameText) != 0 and len(secondnameText):
        firstname.delete("1.0", ctk.END)
        secondname.delete("1.0", ctk.END)

        secondname.configure(state=ctk.DISABLED)
        firstname.configure(state=ctk.DISABLED)
        matchbutton.configure(state=ctk.DISABLED)

        randomNo = r.randrange(1, 101)
        randomNoCapped = randomNo/100
        currentValue = matchprogress.get()
        total_duration = 2
        steps = int(total_duration / 0.01)
        increment = abs(randomNoCapped - currentValue) / steps

        for _ in range(steps):
            if currentValue < randomNoCapped:
                currentValue += increment
                matchprogress.set(min(currentValue, randomNoCapped))
                matchprogress.configure(progress_color="#729B79")
            else:
                currentValue -= increment
                matchprogress.set(max(currentValue, randomNoCapped))
                matchprogress.configure(progress_color="#A72F2F")
            root.update_idletasks()
            root.update()
            time.sleep(0.01)
            matchbutton.configure(text="%")
            label0.configure(text="<><><><><><>" + str(randomNo) + "%" + "<><><><><><>")
            label1.configure(text="<><><><><><>❦<><><><><><>")
        if randomNoCapped == 1:
            firstname.configure(state=ctk.NORMAL)
            matchbutton.configure(text="💐")
            label0.configure(text="<><><><><><>🥀<><><><><><>")
            label1.configure(text="<><><><><><>🥀<><><><><><>")
            firstname.configure(state=ctk.DISABLED)

        matchprogress.configure(progress_color="#B366A1")
        firstname.configure(state=ctk.NORMAL)
        secondname.configure(state=ctk.NORMAL)
        matchbutton.configure(state=ctk.NORMAL)

root = ctk.CTk()
root.minsize(300, 500)
root.maxsize(400, 600)
root.title("Match???")
ctk.set_default_color_theme("green")

holder = ctk.CTkFrame(master=root, fg_color="#0E1116")
holder.pack(padx=10, pady=10, expand=True, fill=ctk.BOTH)
holder.grid_rowconfigure(0, weight=0)
holder.grid_rowconfigure(1, weight=0)
holder.grid_rowconfigure(2, weight=1)
holder.grid_rowconfigure(3, weight=1)
holder.grid_columnconfigure(0, weight=1)
holder.grid_columnconfigure(1, weight=1)
holder.grid_columnconfigure(2, weight=1)

matchprogress = ctk.CTkProgressBar(master=holder, height=70, fg_color="#CEDFD9", border_width=2, border_color="#5F5449", progress_color="#9E7B9B", orientation="horizontal", corner_radius=0)
matchprogress.grid(row=2, columnspan=3, padx=20, pady=0, sticky="ew")
matchprogress.set(0)

matchbutton = ctk.CTkButton(master=holder, height=60, width=180, text="%", text_color="black", fg_color="#5F5449", font=("Arial fb", 30, "bold"), border_width=0, border_color="black", hover_color="#729B79", anchor="center", command=submit, corner_radius=50)
matchbutton.grid(row=3, column=1, padx=20, pady=0)

firstname = ctk.CTkTextbox(master=holder, height=50, fg_color="gray", font=("Arial fb", 16), border_width=2, border_color="black", corner_radius=20)
firstname.grid(row=3, column=0, padx=(20, 0), pady=0, sticky="ew")

secondname = ctk.CTkTextbox(master=holder, height=50, fg_color="gray", font=("Arial fb", 16), border_width=2, border_color="black", corner_radius=20)
secondname.grid(row=3, column=2, padx=(0, 20), pady=0, sticky="ew")

label0 = ctk.CTkLabel(master=holder, text_color="#5F5449", text="<><><><><><>❦<><><><><><>", height=50, width=50, font=("arial fb", 50, "bold"))
label0.grid(row=0, columnspan=3, padx=20, pady=(20, 0))

label1 = ctk.CTkLabel(master=holder, text_color="#5F5449", text="<><><><><><>❦<><><><><><>", height=50, width=50, font=("arial fb", 50, "bold"))
label1.grid(row=4, columnspan=3, padx=20, pady=(20, 20))

root.mainloop()