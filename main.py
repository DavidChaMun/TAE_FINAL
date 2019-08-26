import tkinter as tk
root = tk.Tk()
# Code to add widgets will go here...

#Neuronal Network = 0
#Random Forest = 1
#Vectorial Support = 2
selected_model = tk.IntVar()
select_model_msg = tk.StringVar()
select_model_msg.set("None")
preddicted_value = tk.StringVar()
preddicted_value.set("0")

catego_questions_frames = []
numeric_questions_frames = []

catego_columns = ['education', 'workclass', 'marital_status', 'ocupation', 'ethnicity', 'gender', 'native_country']
numeric_cols = ['age', 'fnlwgt', 'capital_gain', 'capital_loss', 'hours_per_week']

survey_frame = tk.Frame(root)
model_frame = tk.Frame(root)
help_frame = tk.Frame(root)

help_frame.grid(row=0,column=0)
survey_frame.grid(row=1,column=0)
model_frame.grid(row=2, column=0)

title_label = tk.Label(help_frame, width=15, text="Model Survey!")
title_label.grid(row=0, column=0)

# Generates the question labels for the categorical features
survey_row_index = 0
survey_col_index = 0

for m in catego_columns:
    catego_questions_frames.append({
        'frame': None,
        'label': None,
        'entry': None,
        'entry_var': tk.StringVar()
    })

    catego_questions_frames[-1]['frame'] = tk.Frame(survey_frame)
    catego_questions_frames[-1]['frame'].grid(row=survey_row_index,column=survey_col_index)
    survey_row_index += 1

    catego_questions_frames[-1]['label'] = tk.Label(master=catego_questions_frames[-1]['frame'], text=m, width=13,  anchor='w')
    catego_questions_frames[-1]['label'].grid(row=0, column=0)

    catego_questions_frames[-1]['entry'] = tk.Entry(master=catego_questions_frames[-1]['frame'], 
        textvariable=catego_questions_frames[-1]['entry_var'], width=30)
    catego_questions_frames[-1]['entry'].grid(row=0, column=1)


# Generates the question labels for the numerical features 
survey_row_index = 0
survey_col_index = 1

for m in numeric_cols:
    numeric_questions_frames.append({
        'frame': None,
        'label': None,
        'entry': None,
        'entry_var': tk.DoubleVar()
    })


    numeric_questions_frames[-1]['frame'] = tk.Frame(survey_frame)
    numeric_questions_frames[-1]['frame'].grid(row=survey_row_index,column=survey_col_index)
    survey_row_index += 1

    numeric_questions_frames[-1]['label'] = tk.Label(master=numeric_questions_frames[-1]['frame'], text=m, width=12, anchor='w', padx=15)
    numeric_questions_frames[-1]['label'].grid(row=0, column=0)

    numeric_questions_frames[-1]['entry'] = tk.Entry(master=numeric_questions_frames[-1]['frame'], 
        textvariable=numeric_questions_frames[-1]['entry_var'], width=20)
    numeric_questions_frames[-1]['entry'].grid(row=0, column=1)

# -----
def predict():
    print("Trying to predict")
    preddicted_value.set(str(int(preddicted_value.get())+1))

    mod = selected_model.get()

    if (mod == 0):
        print("Selected Neuronal Networks")
    elif (mod == 1):
        print("Selected Random Forest")
    elif (mod == 2):
        print("Selected Support-Vector Machine")

    x_num_vals = [{'label': e['label'].cget("text"), 'val':e['entry_var'].get()} for e in numeric_questions_frames]
    x_cat_vals = [{'label': e['label'].cget("text"), 'val':e['entry_var'].get()} for e in catego_questions_frames]

    print(x_cat_vals)


# -----
def select_model():

    mod = selected_model.get()
    msg = ""

    if (mod == 0):
        print("Selected Neuronal Networks")
        msg = "Neuronal Networks"
    elif (mod == 1):
        print("Selected Random Forest")
        msg = "Random Forest"
    elif (mod == 2):
        print("Selected Support-Vector Machine")
        msg = "Support-Vector Machine"

    select_model_msg.set("Predicting with " + msg  + ": ")

model_select_frame = tk.Frame(model_frame)
model_select_frame.grid(row=0, column=0)

neural_model_s = tk.Radiobutton(master=model_select_frame, text="Neuronal Network", var=selected_model, value=0, anchor='w',
    command=select_model, justify=tk.LEFT, width=30)
neural_model_s.grid(row=0, column=0 )

forest_model = tk.Radiobutton(master=model_select_frame, text="Random Forest", var=selected_model, value=1, anchor='w',
    command=select_model, justify=tk.LEFT, width=30)
forest_model.grid(row=1, column=0 )

vector_model = tk.Radiobutton(master=model_select_frame, text="Support-Vector Machine", var=selected_model, value=2, anchor='w',
    command=select_model, justify=tk.LEFT, width=30)
vector_model.grid(row=2, column=0 )

predict_buttom = tk.Button(master=model_frame, text="Predict", command=predict)
predict_buttom.grid(row=0, column=1  )

result_frame = tk.Frame(model_frame)
result_frame.grid(row=0, column=2)

model_selected_msg_label = tk.Label(master=result_frame, textvariable=select_model_msg)
model_selected_msg_label.grid(row=0, column=0, sticky = tk.N+tk.S+tk.E+tk.W)

preddicted_value_label = tk.Label(master=result_frame, textvariable=preddicted_value)
preddicted_value_label.grid(row=1, column=0, sticky = tk.N+tk.S+tk.E+tk.W)
root.mainloop()

