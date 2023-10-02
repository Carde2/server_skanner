#Imports
import PySimpleGUI as sg
import socket


# Add your new theme colors and settings
tvomel = {'BACKGROUND': '#1C1C1C',
        'TEXT': '#ffffff',
        'INPUT': '#FFFAFA',
        'TEXT_INPUT': '#000000',
        'SCROLL': '#c7e78b',
        'BUTTON': ('#464544', '#FFFAFA'),
        'PROGRESS': ('#01826B', '#D0D0D0'),
        'BORDER': 2,
        'SLIDER_DEPTH': 0,
        'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('Tvomel', tvomel)


sg.theme('Tvomel')

#Window layout
layout = [
        [sg.Text('0.0.0.0 or example.com')],
        [sg.InputText('')],
        [sg.Text('What is this?', size=(15, 1)), sg.InputCombo(('DOMEN', 'IP'), size=(10, 3))],
        [sg.Text('From which port to which port to scan?', size=(30, 1)), sg.InputText('', size=(6, 1)), sg.Text('to', size=(4, 1)), sg.InputText('', size=(6, 1))],
        [sg.Submit('OK')]
          ]


#Window Name
window = sg.Window('Port scanner by @tvomel', layout)    


#Window logic
event, values = window.read()  
window.close()

#skan logic






