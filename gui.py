#User Interface code - Version 1 - Object

import tkinter as tk

class CarStatusGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Car Status")

        self.car_turn1_var = tk.BooleanVar()
        self.car_turn2_var = tk.BooleanVar()
        self.object_in_lane1_var = tk.BooleanVar()
        self.object_in_lane2_var = tk.BooleanVar()
        self.object_in_lane3_var = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        # create labels with row=0
        car_turn1_label = tk.Label(self.window, text="Car at Turn 1:")
        car_turn1_label.grid(row=0, column=0)
        car_turn2_label = tk.Label(self.window, text="Car at Turn 2:")
        car_turn2_label.grid(row=1, column=0)
        object_in_lane1_label = tk.Label(self.window, text="Object in Lane 1:")
        object_in_lane1_label.grid(row=2, column=0)
        object_in_lane2_label = tk.Label(self.window, text="Object in Lane 2:")
        object_in_lane2_label.grid(row=3, column=0)
        object_in_lane3_label = tk.Label(self.window, text="Object in Lane 3:")
        object_in_lane3_label.grid(row=4, column=0)

        # create checkboxes aligned with labels
        car_turn1_checkbox = tk.Checkbutton(self.window, variable=self.car_turn1_var, state="disabled")
        car_turn1_checkbox.grid(row=0, column=1)
        car_turn2_checkbox = tk.Checkbutton(self.window, variable=self.car_turn2_var, state="disabled")
        car_turn2_checkbox.grid(row=1, column=1)
        object_in_lane1_checkbox = tk.Checkbutton(self.window, variable=self.object_in_lane1_var, state="disabled")
        object_in_lane1_checkbox.grid(row=2, column=1)
        object_in_lane2_checkbox = tk.Checkbutton(self.window, variable=self.object_in_lane2_var, state="disabled")
        object_in_lane2_checkbox.grid(row=3, column=1)
        object_in_lane3_checkbox = tk.Checkbutton(self.window, variable=self.object_in_lane3_var, state="disabled")
        object_in_lane3_checkbox.grid(row=4, column=1)

    def update_values(self, car_turn1, car_turn2, object_in_lane1, object_in_lane2, object_in_lane3):
        self.car_turn1_var.set(car_turn1)
        self.car_turn2_var.set(car_turn2)
        self.object_in_lane1_var.set(object_in_lane1)
        self.object_in_lane2_var.set(object_in_lane2)
        self.object_in_lane3_var.set(object_in_lane3)

        # update the GUI to reflect the new values
        self.window.update()

    def run(self):
        self.window.mainloop()


