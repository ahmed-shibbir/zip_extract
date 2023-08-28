
# Import modules including function(s) defined in the functions.py file
import PySimpleGUI as sg
from functions import extract_archive

# Define the variables for the layout of the window
label1 = sg.Text("Select archive")
file = sg.Input()
file_browse = sg.FileBrowse("Choose", key='file')

label2 = sg.Text("Select dest folder")
folder = sg.Input()
folder_browse = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
exit_button = sg.Button("Exit")
msg = sg.Text()

# Create the layout for the window
window = sg.Window("Archive Extractor",
          [[label1,file,file_browse],
           [label2, folder, folder_browse],
           [extract_button, exit_button, msg]])

# Activate the window with a while loop and complete the file
# extraction process

while True:
    event, values = window.read()

    WIN_CLOSED = sg.WINDOW_CLOSED
    if event in (WIN_CLOSED, 'Exit'):
        break

    try:
        filepath = values['file']
        dest_dir = values['folder']
        extract_archive(filepath=filepath, dest_dir=dest_dir)
        msg.update('Files extracted successfully!')

    except FileNotFoundError:
        sg.popup("File not found. Please provide a valid filepath.")
    except Exception as e:
        sg.popup(f"An error occurred: {str(e)}")


window.close()