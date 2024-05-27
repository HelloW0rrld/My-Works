import customtkinter as ctk

class Logic:
    @staticmethod
    def percentage():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, "% ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def pie():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, "π ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def c():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.delete(1.0, ctk.END)
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def factorial():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, "! ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def square():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, "² ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def square_root():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, " sqrt(")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def divide():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, " / ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def multiply():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, " * ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def minus():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, " - ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def plus():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, " + ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def negate():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, " +/- ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def insert_number(number):
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, str(number))
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def insert_dot():
        questionHolder.configure(state=ctk.NORMAL)
        questionHolder.insert(ctk.END, " . ")
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def delete():
        questionHolder.configure(state=ctk.NORMAL)
        content = questionHolder.get(1.0, ctk.END).strip()
        content = content[: -1]
        questionHolder.delete(1.0, ctk.END)
        questionHolder.insert(ctk.END, content)
        questionHolder.configure(state=ctk.DISABLED)

    @staticmethod
    def calculate():
        content = questionHolder.get(1.0, ctk.END).strip()

        # Initialize variables to hold the current number and the result
        current_number = 0
        result = 0

        # Initialize variables to track the current operation and whether we are parsing a number
        current_operation = '+'
        parsing_number = False

        # Iterate over each character in the content
        for char in content:
            # Check if the character is a digit
            if char.isdigit():
                # If we are parsing a number, concatenate the digit to the current number
                current_number = current_number * 10 + int(char)
                parsing_number = True
            elif char in ['+', '-', '*', '/']:
                # If the character is an arithmetic operation, and we have parsed a number
                if parsing_number:
                    # Perform the current operation and update the result
                    if current_operation == '+':
                        result += current_number
                    elif current_operation == '-':
                        result -= current_number
                    elif current_operation == '*':
                        result *= current_number
                    elif current_operation == '/':
                        result /= current_number
                    # Reset the current number and parsing flag
                    current_number = 0
                    parsing_number = False

                # Update the current operation
                current_operation = char

        # Perform the last operation with the last number if there's one
        if parsing_number:
            if current_operation == '+':
                result += current_number
            elif current_operation == '-':
                result -= current_number
            elif current_operation == '*':
                result *= current_number
            elif current_operation == '/':
                result /= current_number

        # Print the final result
        print("Result:", result)
        ansHolder.configure(state=ctk.NORMAL)
        ansHolder.delete(1.0, ctk.END)
        ansHolder.insert(ctk.END, round(result))
        ansHolder.configure(state=ctk.DISABLED)
        questionHolder.yview_moveto(2)

root = ctk.CTk()
root.minsize(320, 500)
root.maxsize(320, 500)
root.title("Calculator")
ctk.set_default_color_theme("blue")

ansFrame = ctk.CTkTextbox(master=root, height=50)
ansFrame.pack(padx=10, pady=(10, 10), fill=ctk.BOTH, side=ctk.TOP, expand=True)
ansFrame.grid_rowconfigure(0, weight=1)
ansFrame.grid_columnconfigure(0, weight=1)
ansFrame.grid_columnconfigure(1, weight=1)

ansHolder = ctk.CTkTextbox(master=ansFrame, height=20, width=500, font=("Arial fb", 60, "bold"))
ansHolder.grid(row=0, column=0, padx=20, pady=30, sticky="nsew")
ansHolder.configure(state=ctk.DISABLED)

questionHolder = ctk.CTkTextbox(master=ansFrame, height=20, width=100, font=("Arial fb", 20))
questionHolder.grid(row=0, column=1, padx=10, pady=30, sticky="ew")
questionHolder.configure(state=ctk.DISABLED)


buttonHolder = ctk.CTkFrame(master=root, height=1000)
buttonHolder.pack(padx=10, pady=(0, 10), fill=ctk.BOTH, side=ctk.BOTTOM, expand=True)
buttonHolder.grid_rowconfigure(0, weight=1)
buttonHolder.grid_columnconfigure(0, weight=1)
buttonHolder.grid_rowconfigure(1, weight=1)
buttonHolder.grid_columnconfigure(1, weight=1)
buttonHolder.grid_rowconfigure(2, weight=1)
buttonHolder.grid_columnconfigure(2, weight=1)
buttonHolder.grid_rowconfigure(3, weight=1)
buttonHolder.grid_columnconfigure(3, weight=1)
buttonHolder.grid_rowconfigure(4, weight=1)
buttonHolder.grid_rowconfigure(5, weight=1)

# Row 1
button00 = ctk.CTkButton(master=buttonHolder, height=50, text="%", command=Logic.percentage)
button00.grid(padx=(10, 0), pady=(10, 0), row=0, column=0, sticky="nsew")
button00.configure(fg_color="#2F4F4F")

button01 = ctk.CTkButton(master=buttonHolder, height=50, text="π", command=Logic.pie)
button01.grid(padx=2, pady=(10, 0), row=0, column=1, sticky="nsew")
button01.configure(fg_color="#2F4F4F")

button02 = ctk.CTkButton(master=buttonHolder, height=50, text="C", command=Logic.c)
button02.grid(padx=(0, 0), pady=(10, 0), row=0, column=2, sticky="nsew")
button02.configure(fg_color="#2F4F4F")

button03 = ctk.CTkButton(master=buttonHolder, height=50, text="Del", command=Logic.delete)
button03.grid(padx=(2, 10), pady=(10, 0), row=0, column=3, sticky="nsew")
button03.configure(fg_color="#2F4F4F")

# Row 2
button10 = ctk.CTkButton(master=buttonHolder, height=50, text="!", command=Logic.factorial)
button10.grid(padx=(10, 0), pady=2, row=1, column=0, sticky="nsew")
button10.configure(fg_color="#2F4F4F")

button11 = ctk.CTkButton(master=buttonHolder, height=50, text="x²", command=Logic.square)
button11.grid(padx=2, pady=2, row=1, column=1, sticky="nsew")
button11.configure(fg_color="#2F4F4F")

button12 = ctk.CTkButton(master=buttonHolder, height=50, text="√x", command=Logic.square_root)
button12.grid(padx=(0, 0), pady=2, row=1, column=2, sticky="nsew")
button12.configure(fg_color="#2F4F4F")

button13 = ctk.CTkButton(master=buttonHolder, height=50, text="÷", command=Logic.divide)
button13.grid(padx=(2, 10), pady=2, row=1, column=3, sticky="nsew")
button13.configure(fg_color="#2F4F4F")

# Row 3
button20 = ctk.CTkButton(master=buttonHolder, height=50, text="7", command=lambda: Logic.insert_number(7))
button20.grid(padx=(10, 0), pady=0, row=2, column=0, sticky="nsew")
button20.configure(fg_color="#2F4F4F")

button21 = ctk.CTkButton(master=buttonHolder, height=50, text="8", command=lambda: Logic.insert_number(8))
button21.grid(padx=2, pady=0, row=2, column=1, sticky="nsew")
button21.configure(fg_color="#2F4F4F")

button22 = ctk.CTkButton(master=buttonHolder, height=50, text="9", command=lambda: Logic.insert_number(9))
button22.grid(padx=(0, 0), pady=0, row=2, column=2, sticky="nsew")
button22.configure(fg_color="#2F4F4F")

button23 = ctk.CTkButton(master=buttonHolder, height=50, text="✕", command=Logic.multiply)
button23.grid(padx=(2, 10), pady=0, row=2, column=3, sticky="nsew")
button23.configure(fg_color="#2F4F4F")

# Row 4
button30 = ctk.CTkButton(master=buttonHolder, height=50, text="4", command=lambda: Logic.insert_number(4))
button30.grid(padx=(10, 0), pady=2, row=3, column=0, sticky="nsew")
button30.configure(fg_color="#2F4F4F")

button31 = ctk.CTkButton(master=buttonHolder, height=50, text="5", command=lambda: Logic.insert_number(5))
button31.grid(padx=2, pady=2, row=3, column=1, sticky="nsew")
button31.configure(fg_color="#2F4F4F")

button32 = ctk.CTkButton(master=buttonHolder, height=50, text="6", command=lambda: Logic.insert_number(6))
button32.grid(padx=(0, 0), pady=2, row=3, column=2, sticky="nsew")
button32.configure(fg_color="#2F4F4F")

button33 = ctk.CTkButton(master=buttonHolder, height=50, text="—", command=Logic.minus)
button33.grid(padx=(2, 10), pady=2, row=3, column=3, sticky="nsew")
button33.configure(fg_color="#2F4F4F")

# Row 5
button40 = ctk.CTkButton(master=buttonHolder, height=50, text="1", command=lambda: Logic.insert_number(1))
button40.grid(padx=(10, 0), pady=0, row=4, column=0, sticky="nsew")
button40.configure(fg_color="#2F4F4F")

button41 = ctk.CTkButton(master=buttonHolder, height=50, text="2", command=lambda: Logic.insert_number(2))
button41.grid(padx=2, pady=0, row=4, column=1, sticky="nsew")
button41.configure(fg_color="#2F4F4F")

button42 = ctk.CTkButton(master=buttonHolder, height=50, text="3", command=lambda: Logic.insert_number(3))
button42.grid(padx=(0, 0), pady=0, row=4, column=2, sticky="nsew")
button42.configure(fg_color="#2F4F4F")

button43 = ctk.CTkButton(master=buttonHolder, height=50, text="+", command=Logic.plus)
button43.grid(padx=(2, 10), pady=0, row=4, column=3, sticky="nsew")
button43.configure(fg_color="#2F4F4F")

# Row 6
button50 = ctk.CTkButton(master=buttonHolder, height=50, text="+/−", command=Logic.negate)
button50.grid(padx=(10, 0), pady=(2, 10), row=5, column=0, sticky="nsew")
button50.configure(fg_color="#2F4F4F")

button51 = ctk.CTkButton(master=buttonHolder, height=50, text="0", command=lambda: Logic.insert_number(0))
button51.grid(padx=2, pady=(2, 10), row=5, column=1, sticky="nsew")
button51.configure(fg_color="#2F4F4F")

button52 = ctk.CTkButton(master=buttonHolder, height=50, text="•", command=Logic.insert_dot)
button52.grid(padx=(0, 0), pady=(2, 10), row=5, column=2, sticky="nsew")
button52.configure(fg_color="#2F4F4F")

button53 = ctk.CTkButton(master=buttonHolder, height=50, text="=", command=Logic.calculate)
button53.grid(padx=(2, 10), pady=(2, 10), row=5, column=3, sticky="nsew")
button53.configure(fg_color="#273F3F")

root.mainloop()
