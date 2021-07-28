

                                #"""This Program is for creating IDE for Python"""


#Imports Library first

from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

#Initialize Tkinter

compiler = Tk()
compiler.title('Addypy IDE')
file_path = ''

# Defining Function For File Path

def set_file_path(path):
    global file_path
    file_path = path

#Defining Function to Open File

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

# Defining Function For save as option

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open (path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

# Defining Function for rn Command Menu
def run():
    if file_path =='':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

menu_bar = Menu(compiler)

# Defining Commands for Menu Buttons (File Menu)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command (label='Save', command=save_as)
file_menu.add_command (label='Save As', command=save_as)
file_menu.add_command (label='Exit', command=exit)
menu_bar.add_cascade (label='File', menu=file_menu)

# Defining Commands for Menu Buttons (Run Menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade (label='Run', menu=run_bar)

# Closing Body of Tkinter

compiler.config(menu = menu_bar)
editor = Text()
editor.pack()
code_output = Text(height=10)
code_output.pack()
compiler.mainloop()