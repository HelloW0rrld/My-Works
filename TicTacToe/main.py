import customtkinter as ctk
import random

idle_button_color = "#69482E"
hover_button_color = "white"
selected_button_color = "red"
button_grid = [["empty", "empty", "empty"], ["empty", "empty", "empty"], ["empty", "empty", "empty"]]
choices_left = []

def main():
    start_button.destroy()
    start_bg.destroy()

    game_bg = ctk.CTkFrame(master=root, fg_color="#291D12")
    game_bg.pack(fill=ctk.BOTH, expand=True)
    game_bg.rowconfigure(0, weight=1)
    game_bg.rowconfigure(1, weight=1)
    game_bg.columnconfigure(0, weight=1)

    #score & menu block
    menuscore_frame = ctk.CTkFrame(master=game_bg, fg_color="gray", corner_radius=0, height=80)
    menuscore_frame.grid(padx=0, pady=0, sticky="ew")

    #choices block
    choices_frame = ctk.CTkFrame(master=game_bg, fg_color="gray", corner_radius=10, border_width=2, border_color="#2C2C2C")
    choices_frame.grid(padx=15, pady=15, sticky="nsew")
    choices_frame.rowconfigure(0, weight=1)
    choices_frame.rowconfigure(1, weight=1)
    choices_frame.rowconfigure(2, weight=1)
    choices_frame.columnconfigure(0, weight=1)
    choices_frame.columnconfigure(1, weight=1)
    choices_frame.columnconfigure(2, weight=1)

    #row1
    button00 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(0))
    button00.grid(row=0, column=0, sticky="ns", padx=0, pady=10)
    button01 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(1))
    button01.grid(row=0, column=1, sticky="ns", padx=0, pady=10)
    button02 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(2))
    button02.grid(row=0, column=2, sticky="ns", padx=0, pady=10)

    #row2
    button10 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(3))
    button10.grid(row=1, column=0, sticky="ns", padx=0, pady=10)
    button11 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(4))
    button11.grid(row=1, column=1, sticky="ns", padx=0, pady=10)
    button12 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(5))
    button12.grid(row=1, column=2, sticky="ns", padx=0, pady=10)

    #row3
    button20 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(6))
    button20.grid(row=2, column=0, sticky="ns", padx=0, pady=10)
    button21 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(7))
    button21.grid(row=2, column=1, sticky="ns", padx=0, pady=10)
    button22 = ctk.CTkButton(master=choices_frame, text="", height=100, width=100, fg_color=idle_button_color,
                             hover_color=hover_button_color, border_width=2, border_color="#2C2C2C", command=lambda: userButtonClicked(8))
    button22.grid(row=2, column=2, sticky="ns", padx=0, pady=10)

    button_names = {
        0: button00,
        1: button01,
        2: button02,
        3: button10,
        4: button11,
        5: button12,
        6: button20,
        7: button21,
        8: button22
    }

    def userButtonClicked(buttonID):
        name = button_names.get(buttonID, None)
        if name is not None:
            button_grid[buttonID // 3][buttonID % 3] = "filled"
            name.configure(fg_color=selected_button_color, text="X", font=("arial fb", 60), state=ctk.DISABLED)
            ai(button_names)
        else:
            print(f"Invalid buttonID: {buttonID}")

    def ai(button_names):
        choices_left.clear()
        for row_index, row in enumerate(button_grid):
            for col_index, space in enumerate(row):
                if space == "empty":
                    choices_left.append((row_index, col_index))
        if not choices_left:
            pass
        else:
            random_choice = random.choice(choices_left)
            buttonID = random_choice[0] * 3 + random_choice[1]
            aiButtonClicked(buttonID, button_names)
            button_grid[buttonID // 3][buttonID % 3] = "filled"

def aiButtonClicked(buttonID, button_names):
    button_name = button_names.get(buttonID, None)
    if button_name is not None:
        button_name.configure(fg_color="black", text="O", font=("arial fb", 60), state=ctk.DISABLED)
        choices_left.clear()
    else:
        pass

root = ctk.CTk()
root.title("Tic Tac Toe")
root.minsize(400, 400)
root.maxsize(400, 400)

start_bg = ctk.CTkFrame(master=root, fg_color="#BD895F")
start_bg.pack(fill=ctk.BOTH, expand=True)
start_button = ctk.CTkButton(master=start_bg, fg_color="#69482E", height=50, width=150,
                             border_width=2, border_color="#2C2C2C", text="START", font=("Bodoni", 20, "bold"), hover_color="#B39379", command=main)
start_button.pack()
start_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
root.mainloop()