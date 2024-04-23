from __future__ import with_statement
import contextlib
import sys
import time

from pyke import knowledge_engine
from pyke import krb_traceback, goal
import sys
# import PySimpleGUI as sg

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
#GUI code done but weren't able to link it with the knowledge base files !
# sg.theme("dark grey 10")
# layout=[
#     [
#         [
#             sg.Text("Do you experience shortness of breath?")
#         ],
#         [
#             sg.Button("Yes")
#         ],
#         [
#             sg.Button("No")
#         ],
# [
#             sg.Text("Do you experience fatigue?")
#         ],
#         [
#             sg.Button("Yes")
#         ],
#         [
#             sg.Button("No")
#         ],
# [
#             sg.Text("Do you experience chest pain?")
#         ],
#         [
#             sg.Button("Yes")
#         ],
#         [
#             sg.Button("No")
#         ],
# [
#             sg.Text("Do feel fluttering in your chest?")
#         ],
#         [
#             sg.Button("Yes")
#         ],
#         [
#             sg.Button("No")
#         ],
# [
#             sg.Text("Is your heart beat slower than normal?")
#         ],
#         [
#             sg.Button("Yes")
#         ],
#         [
#             sg.Button("No")
#         ]
#     ]
# ]
#Create a window
# window = sg.Window ("Expert Heart Deasieases System", layout, size=(300, 300))
# while True:
#     event, values = window.read()
#     print(event)
#     if event == sg.WIN_CLOSED:
#         break

# window.close()
# exit()