from __future__ import with_statement
import contextlib
import sys
import time

from pyke import knowledge_engine
from pyke import krb_traceback, goal
import sys
import PySimpleGUI as sg

engine = knowledge_engine.engine(__file__)
fc_goal = goal.compile('symptoms.diagnosis($diagnosis)')

def Diagnosis_rules():
    engine.reset()

    engine.activate('FC_diagnosis_rules')

    print("doing proof")
    print()
    count = 0

    try:
        with fc_goal.prove(engine) as gen:
            for vars, plan in gen:
                count = count + 1
                if count == 1:
                    print("Your diagnosis is: %s" % (vars['diagnosis']))
                else:
                    print("Another disease detected -> %s" % (vars['diagnosis']))

    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    # counter to check if a diagnosis was reached through rules otherwise it remains 0 and prints the following
    if count == 0:
        print("Test Inconclusive: medical exams needed to make a definitive diagnosis")
    if count > 1:
        print()
        print("More than one disease is detected according to the given symptoms, medical")
        print("examinations needed to confirm a diagnosis")
    print()
    print("done")


# Diagnosis_rules()

light_gray = "#FAFAFA"
maroon = "#800000"

sg.theme("LightGrey1")
layout = [
    [sg.Text("", key="-HEADER-")],
    [sg.Column([
        [sg.Frame(
            "", 
            layout=[
                [sg.Text(
                    "  Hello! I'm",
                    font=("Poppins", 10)), 
                 sg.Text(
                    "Heartwise", 
                    font=("Poppins", 10, "bold"),
                    pad=(10,10)), 
                 sg.Text(
                    "- your Elderly Heart Health Assistant!  ",
                    font=("Helvetica", 10)
                )]
            ], 
            key="-INTRO-", 
            pad=(15,0), 
            background_color=light_gray,
            border_width=2,
        )],
        [sg.Frame(
            "", 
            layout=[
                [sg.Text(
                    " Let's Start! ", 
                    font=("Poppins", 10), 
                    pad=(10,10)
                )]
            ], 
            key="-START-", 
            pad=(15,10), 
            border_width=2,
            background_color=light_gray,
        )],
        [sg.Frame(
            "Question 1", 
            layout=[
                [sg.Text(
                    "Do you experience shortness of breath?", 
                    pad=(8,8)
                )],
                [sg.Button(
                    "  Yes, I have  ",
                    pad=(10,10)), 
                 sg.Button(
                    "  Nope  ",
                    pad=(0,10),
                    button_color=('white', maroon)
                )]
            ], 
            key="-Q1-", 
            pad=(15, 5), 
            background_color=light_gray,
            border_width=2,
        )],
        [sg.Text("", size=(1, 12))],
        [sg.Frame(
            "Input", 
            layout=[
                [sg.InputText(
                    "Type your response here...",
                    pad=(10, 10),  
                    background_color=light_gray,
                    border_width=0,
                    font=("Helvetica", 9),
                    size=(60, 1)
                )],
                [sg.Button(
                    "  Send  ",
                    pad=(10)
                )]
            ], 
            key="-INPUT-", 
            pad=(15, 5), 
            background_color=light_gray,
            border_width=2,
        )],
        [sg.Text("", key="-FOOTER-", size=(1, 10))],
    ], vertical_scroll_only=True)]
]

window = sg.Window("Heartwise", layout, finalize=True, size=(450, 600))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()