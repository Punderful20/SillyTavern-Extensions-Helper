import tkinter as tk
import subprocess

window = tk.Tk()
window.title('SillyTavern Extension Helper')
window.geometry('512x256')

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()

selectedModules = ''

def print_selection():
    global selectedModules
    selectedModules = ''
    if (var1.get() == 1):
        #label.config(text='Module: Classify enabled.')
        selectedModules += 'classify, '
    if (var2.get() == 1):
        selectedModules += 'summarize, '
    if (var3.get() == 1):
        selectedModules += 'caption, '
    if (var4.get() == 1):
        selectedModules += 'keywords, '
    if (var5.get() == 1):
        selectedModules += 'prompt, '
    if (selectedModules == ''):
        label.config(text='No modules selected.')
    else:
        label.config(text='Modules selected: ' + selectedModules)
    

def run_tavern_extras():
    subprocess.Popen(['python', 'server.py', '--enable-modules=' + selectedModules])

def save_config():
    with open('helper_config.txt', 'w') as f:
        f.write(f"Selected modules: {selectedModules}")
        f.close()

def load_config():
    try:
        f = open('helper_config.txt', 'r')
        tempString = f.read()
        selectedModules = f.read()
        var1.set(int('classify' in tempString))
        var2.set(int('summarize' in tempString))
        var3.set(int('caption' in tempString))
        var4.set(int('keywords' in tempString))
        var5.set(int('prompt' in tempString))
        print_selection()
    except:
        print('File does not exist.')

load_config()

label = tk.Label(window, bg='white', width=100, text='No modules selected.')
label.pack()

c1 = tk.Checkbutton(window, text='Module: Classify', variable=var1, onvalue=1, offvalue=0, command=print_selection)    
c1.pack()
c2 = tk.Checkbutton(window, text='Module: Summarize', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='Module: Caption', variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='Module: Keywords', variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack()
c5 = tk.Checkbutton(window, text='Module: Prompt', variable=var5, onvalue=1, offvalue=0, command=print_selection)
c5.pack()

b1 = tk.Button(window, text='Run Tavern-extras with selected modules', command=run_tavern_extras)
b1.pack()
b2 = tk.Button(window, text='Save config', command=save_config)
b2.pack()
b3 = tk.Button(window, text='Load config', command=load_config)
b3.pack()

window.mainloop()