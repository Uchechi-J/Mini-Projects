import tkinter as tk
from tkinter import ttk
from tkinter import *


def BMR():
    body_weight = int(weight_entry_box.get())
    body_weight_unit = weight_option_box.get()
    if body_weight_unit == 'Pounds':
        body_weight /= 2.2
    basal_metabolic_rate = int(body_weight) * 20
    # print(Basal_Metabolic_Rate) #Function test
    return basal_metabolic_rate


def TEF():
    thermic_effect_of_feeding = BMR() * 0.1
    # print(Thermic_Effect_of_Feeding) # Function test
    return thermic_effect_of_feeding


def EEE():
    activity = activity_option_box.get()
    if activity == "Lightly active":
        exercise_energy_expenditure = int(250)
    elif activity == "Moderately active":
        exercise_energy_expenditure = int(325)
    elif activity == "Very active":
        exercise_energy_expenditure = int(425)
    else:
        exercise_energy_expenditure = int(500)
    # print(Exercise_Energy_Expenditure) # Function test
    return exercise_energy_expenditure


def NEAT():
    activity = activity_option_box.get()
    if activity == "Lightly active":
        nonexercise_activity_thermogenesis = 250
    elif activity == "Moderately active":
        nonexercise_activity_thermogenesis = 250
    elif activity == "Very active":
        nonexercise_activity_thermogenesis = 500
    else:
        nonexercise_activity_thermogenesis = 500
    # print(NonExercise_Activity_Thermogenesis) # Function test
    return nonexercise_activity_thermogenesis


def TDEE():
    target_daily_calorie_intake = BMR() + TEF() + EEE() + NEAT()
    gender = sex_option_box.get()
    if gender == "Male":
        target_daily_calorie_intake += 100
    else:
        target_daily_calorie_intake -= 100
    # print(target_daily_calorie_intake) # function test
    output_value.config(text=str(target_daily_calorie_intake) + " calories")


window = tk.Tk()

# window creation
window.geometry("323x380")
window.title("GARMIN Calorie Calculator")
window.configure(background="#0DCEDA")

# frame creation
frame = tk.Frame(window, padx=10, pady=15)
frame.configure(background= "#6EF3D6")
frame.pack()

# input frame creation
input_frame = tk.Frame(frame,padx=20, pady=20, relief=GROOVE)
input_frame.configure(background="#6EF3D6")
input_frame.pack()

# age field
age_label = tk.Label(input_frame, text="Age:",width=10)
age_label.grid(row=0, column=0)
age_label.configure(background="#000000", foreground='#FFFFFF' )
age_spinbox = tk.Spinbox(input_frame, from_=12, to=112, width=20)
age_spinbox.grid(row=0, column=1, columnspan=2)

# sex field
sex_label = tk.Label(input_frame, text="SEX:", width=10)
sex_label.grid(row=1, column=0)
sex_label.configure(background="#000000", foreground='#FFFFFF')
sex_option_box = ttk.Combobox(input_frame, width=20, values=["Female", "Male"])
sex_option_box.grid(row=1, column=1, columnspan=2)

# weight field
weight_label = tk.Label(input_frame, text="Weight:", width=10)
weight_label.grid(row=2, column=0)
weight_label.configure(background="#000000", foreground='#FFFFFF')
weight_entry_box = tk.Entry(input_frame, width=8)
weight_entry_box.grid(row=2, column=1)
weight_option_box = ttk.Combobox(input_frame, width=8,  values=["Pounds", "Kilograms"])
weight_option_box.grid(row=2, column=2)

# goal field
goal_label = tk.Label(input_frame, text="Goal:", width=10)
goal_label.grid(row=3, column=0)
goal_label.configure(background="#000000", foreground='#FFFFFF')
goal_option_box = ttk.Combobox(input_frame, width=20, values=["Fat Loss", "Maintenance", "Muscle Gain"])
goal_option_box.grid(row=3, column=1, columnspan=2)

# activity field
activity_label = tk.Label(input_frame, text="Activity Level:")
activity_label.grid(row=4, column=0)
activity_label.configure(background="#000000", foreground='#FFFFFF')
activity_option_box = ttk.Combobox(input_frame, width=20,
                                   values=["Lightly active", "Moderately active", "Very active", "Extra active"])
activity_option_box.grid(row=4, column=1, columnspan=2)

# calculate button
calculate_button = tk.Button(input_frame, text="Calculate", relief=RAISED, command=TDEE)
calculate_button.grid(row=5, column=0, sticky="news")
calculate_button.configure(background="#FFFFFF", foreground='#000000')

for widget in input_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# output frame creation
output_frame = tk.Frame(frame, padx=20, pady=20)
output_frame.configure(background="#6EF3D6")
output_frame.pack()

# Output field
output_label = tk.Label(output_frame, text="Target Daily Caloric Intake",)
output_label.grid(row=0, column=0, columnspan=3)
output_label.configure(background="#000000", foreground='#FFFFFF')
output_value = tk.Label(output_frame, width=15, height=2, relief=RIDGE)
output_value.grid(row=1, column=0, columnspan=3)



for widget in output_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


window.mainloop()
