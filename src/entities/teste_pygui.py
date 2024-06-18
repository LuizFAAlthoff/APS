import PySimpleGUI as sg

layout = [[sg.Text('Hello from PySimpleGUI')], [sg.Button('OK')]]

window = sg.Window('Demo Window', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'OK':
        break

window.close()
