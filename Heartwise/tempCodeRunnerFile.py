layout=[
    [
        [
            sg.Text("Do you experience shortness of breath?")
        ],
        [
            sg.Button("Yes")
        ],
        [
            sg.Button("No")
        ],
[
            sg.Text("Do you experience fatigue?")
        ],
        [
            sg.Button("Yes")
        ],
        [
            sg.Button("No")
        ],
[
            sg.Text("Do you experience chest pain?")
        ],
        [
            sg.Button("Yes")
        ],
        [
            sg.Button("No")
        ],
[
            sg.Text("Do feel fluttering in your chest?")
        ],
        [
            sg.Button("Yes")
        ],
        [
            sg.Button("No")
        ],
[
            sg.Text("Is your heart beat slower than normal?")
        ],
        [
            sg.Button("Yes")
        ],
        [
            sg.Button("No")
        ]
    ]
]
#Create a window
window = sg.Window ("Expert Heart Deasieases System", layout, size=(100, 100))
while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break

window.close()
exit()