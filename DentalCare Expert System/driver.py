import tkinter as tk
from tkinter import ttk
from tkinter import font
from pyke import knowledge_engine, krb_traceback
import shutil
import os

# Path of the directory to be removed
dir_path = r'C:\Users\Acer\Desktop\PyKE ES\pyke_project_Dental_Clinic\clinic_dentist_project_code\compiled_krb'

# Ensure the directory exists before trying to remove it
if os.path.exists(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"The directory {dir_path} and all its contents have been removed successfully.")
    except OSError as e:
        print(f"Error: {e.strerror}")
else:
    print(f"The directory {dir_path} does not exist.")


# Initialize the knowledge engine
engine = knowledge_engine.engine(__file__)

# Function to handle gum issues
def periodontal_diseases():
    engine.reset()
    engine.activate('rules')
    try:
        gingivitis_found = False
        # Prove the goal related to gum issues
        with engine.prove_goal('rules.periodontal($bring)') as gen:
            for vars, _ in gen:
                if vars['bring'] == "Gingivitis" and not gingivitis_found:
                    gingivitis_found = True
                    # Display information about Gingivitis
                    display_result("Gingivitis Information:\n\nGingivitis is a mild form of gum disease. You can usually reverse it with:\n- Daily brushing and flossing.\n- Regular cleaning by a Dentist or Dental Hygienist.\n- You must go to the doctor if it isn't stop bleeding.\nUntreated Gingivitis can lead to Periodontitis like Leukemia which is a type of blood cancer.\n\n")
    except Exception as e:
        print("An error occurred:", e)
    if not gingivitis_found:
        display_result("No Periodontal detected.\n\n")

# Function to handle dental abscess
def dental_abscess():
    engine.reset()
    engine.activate('rules')
    try:
        # Prove the goal related to dental abscess
        with engine.prove_goal('rules.dental_abscess($bring)') as gen:
            advice = [vars['bring'] for vars, _ in gen]
            display_result("Dental Abscess Advice:\n" + "\n".join(advice) + "\n\n")
    except Exception as e:
        krb_traceback.print_exc()
        
# Function to handle dental_cavity_caries
def dental_cavity_caries():
    engine.reset()
    engine.activate('rules')
    try:
        # Prove the goal related to dental_cavity_caries
        with engine.prove_goal('rules.dental_cavity($bring)') as gen:
            advice = [vars['bring'] for vars, _ in gen]
            display_result("Dental Cavity Teeth Advice:\n" + "\n".join(advice) + "\n\n")
    except Exception:
        krb_traceback.print_exc()

# Function to handle tooth discoloration
def discoloration_teeth():
    engine.reset()
    engine.activate('rules')
    try:
        # Prove the goal related to tooth discoloration
        with engine.prove_goal('rules.discoloration($bring)') as gen:
            advice = [vars['bring'] for vars, _ in gen]
            display_result("Discoloration Teeth Advice:\n" + "\n".join(advice) + "\n\n")
    except Exception:
        krb_traceback.print_exc()
        
# Function to handle tooth discoloration
def pre_Implantitis():
    engine.reset()
    engine.activate('rules')
    try:
        # Prove the goal related to tooth discoloration
        with engine.prove_goal('rules.pre_implantitis($bring)') as gen:
            advice = [vars['bring'] for vars, _ in gen]
            display_result("PreImplantitis Advice:\n" + "\n".join(advice) + "\n\n")
    except Exception:
        krb_traceback.print_exc()

# Function to handle selection of dental condition
def on_condition_selected():
    result_text.delete('1.0', tk.END)
    numper_disease = int(selected_disease.get())
    if numper_disease == 1:
        periodontal_diseases()
    elif numper_disease == 2:
        dental_abscess()
    elif numper_disease == 3:
        dental_cavity_caries()
    elif numper_disease == 4:
        discoloration_teeth()
    elif numper_disease == 5:
        pre_Implantitis()
        

# Function to display result
def display_result(result):
    result_window = tk.Toplevel()
    result_window.title("Result")
    result_window.geometry("700x200")

    result_label = tk.Label(result_window, text=result, font=("Helvetica", 12), anchor="w", justify="left")
    result_label.pack(fill="both", padx=20, pady=20)
    
# Function to submit name and age
def submit_name_age():
    name = name_var.get()
    age = age_var.get()
    greeting_label.config(text=f"Hi {name}, you are {age} years old!", font=font_3)
    submit_button.pack_forget()
    tk.Label(root, text="Now, let's talk about your dental concerns.", font=font_4).place(relx=0.5, rely=0.55, anchor='n')
    tk.Label(root, text="Which dental issue are you experiencing?", font=font_4).place(relx=0.5, rely=0.60, anchor='n')
    global selected_disease
    selected_disease = tk.StringVar(root, "1")
    tk.Radiobutton(root, text="Periodontal Disease", variable=selected_disease, value="1", font=font_4).place(relx=0.4, rely=0.65, anchor='n')
    tk.Radiobutton(root, text="Dental Abscess", variable=selected_disease, value="2", font=font_4).place(relx=0.38, rely=0.70, anchor='n')
    tk.Radiobutton(root, text="Teeth Cavity/Caries", variable=selected_disease, value="3", font=font_4).place(relx=0.4, rely=0.75, anchor='n')
    tk.Radiobutton(root, text="Discoloration Teeth", variable=selected_disease, value="4", font=font_4).place(relx=0.4, rely=0.80, anchor='n')
    tk.Radiobutton(root, text="Pre-Implantitis", variable=selected_disease, value="5", font=font_4).place(relx=0.37, rely=0.85, anchor='n')
    submit_button_2 = tk.Button(root, text="Proceed", command=on_condition_selected)
    submit_button_2.place(relx=0.5, rely=0.91, anchor='n')

# Initialize the Tkinter GUI
root = tk.Tk()
root.title("DentalCare Expert System")
root.geometry("600x700")

font_1 = font.Font(family="Helvetica", size=17)
font_2 = font.Font(family="Helvetica", size=17, weight="bold", slant="italic")
font_3 = font.Font(family="Helvetica", size=11, slant="italic")
font_4 = font.Font(family="Helvetica", size=11)

label_welcome = tk.Label(root, text="Welcome to ", font=font_1)
label_welcome.place(relx=0.5, rely=0.1, anchor='n')

label_dentalcare = tk.Label(root, text="DentalCare Expert System", font=font_2)
label_dentalcare.place(relx=0.5, rely=0.15, anchor='n')

tk.Label(root, text="I'm Dr. Mamaronsing, your virtual dentist assistant.", font=font_3).place(relx=0.5, rely=0.20, anchor='n')

tk.Label(root, text="May I have your name, please?", font=font_4).place(relx=0.5, rely=0.26, anchor='n')
name_var = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name_var, style='Rounded.TEntry', width=28)
name_entry.place(relx=0.5, rely=0.3, anchor='n')

tk.Label(root, text="How about your age?", font=font_4).place(relx=0.5, rely=0.37, anchor='n')
age_var = tk.StringVar()
age_entry = ttk.Entry(root, textvariable=age_var, style='Rounded.TEntry', width=28)
age_entry.place(relx=0.5, rely=0.4, anchor='n')

submit_button = tk.Button(root, text="Submit Name & Age", command=submit_name_age)
submit_button.place(relx=0.5, rely=0.45, anchor='n')

greeting_label = tk.Label(root, text="")
greeting_label.place(relx=0.5, rely=0.5, anchor='n')

result_label = tk.Label(root, text="Results:")
result_text = tk.Text(root, height=15)

style = ttk.Style()
style.configure('Rounded.TEntry', borderwidth=1, relief="solid", bordercolor="black", padding=5, 
                focusthickness=3, focuscolor="#4C4C4C", background="#FFFFFF", font=font_4, borderradius=67)

root.mainloop()
