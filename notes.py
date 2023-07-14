import PySimpleGUI as sg
from pathlib import Path

smileys = [
    "happy", [":)", "XD", ":D", "<3"],
    "sad", [":(", "T_T"],
    "other", [":3"]
]
smiley_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ["File", ["Open", "Save", "---", "Exit"]],
    ["Tools", ["Word Count"]],
    ["Add", smileys],
    ["Help", "Exit"]
]

sg.theme("GrayGrayGray")
layout = [
    [sg.Menu(menu_layout)], 
    [sg.Text("Untitled", key = "-DOCNAME-")],
    [sg.Multiline(no_scrollbar = True, size = (75, 25), key = "-TEXTBOX-")]
]

window = sg.Window("Text Editor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Exit':
        sg.WIN_CLOSED
        break
    if event == 'Open':
        file_path = sg.popup_get_file('open', no_window = True)
        if file_path:
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text())
            window['-DOCNAME-'].update(file_path.split('/')[-1])
            
    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window = True, save_as = True)
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])
        
    if event == "Word Count":
        full_text = values["-TEXTBOX-"]
        clean_text = full_text.replace("\n", " ").split(" ")
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f"words {word_count}\ncharacters: {char_count}")
        
    if event in smiley_events:
        current_text = values['-TEXTBOX-']
        new_text = current_text + ' ' + event
        window['-TEXTBOX-'].update(new_text)
        
window.close()
