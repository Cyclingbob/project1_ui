import os
import keyboard
import time

path = "//des.grplnk.net/home/nabil.hakkeem/Desktop/Nabil Hakkeem - documents/pyhtoin/UI for backend/dxfs"
dir_list = (os.listdir(path))
display_length = 10
global current_object_list, pointer
current_object_list = []
pointer = 0

class Scroll:
    def __init__(self, text, display_length):
        self.text = text
        self.pointer_index = 0
        self.pointer_start = 0
        self.pointer_end = display_length

    def scrollText(self):
        if self.pointer_index>(len(self.text)-self.pointer_end):
            self.pointer_start = 0
            self.pointer_index = 0
        printed_text  = self.text[self.pointer_start+self.pointer_index:self.pointer_end+self.pointer_index]
        return printed_text

def button1():
    global current_object_list, pointer
    print('buttton 1')
    pointer+=1
    current_object_list.clear()

def button2():
    print('button 2')
    selected=dir_list[pointer]
    confirm = input(f'Print? {text1:.10} \nYes(1)     No(Enter)\n')
    if confirm == '1':
        print('Selected file: ',text1)
    else:
        print('File unselected')

button1key = 'ctrl+y'
button2key = 'ctrl+u'

keyboard.add_hotkey(button1key, button1)
keyboard.add_hotkey(button2key, button2)

while 1:
    if pointer==len(dir_list):
        pointer = 0
    text1 = dir_list[pointer]
    if len(text1)>display_length:
        if len(current_object_list) == 0:
            current_text = Scroll(text1, display_length)
            current_object_list.append(current_text)
            current_pointer = pointer
        
        text = current_text.scrollText()
        current_text.pointer_index+=1
    else:
        text = text1
    print(text)
    print('Select(1)    Next(Enter)')
        #print(pointer)
    time.sleep(0.2)
    #if selected, goes through checks to make sure pointer remains in the same place and it is a file
'''
    if lmao=='1':
        selected=dir_list[pointer]
        confirm = input(f'Print? {text1} \nYes(1)     No(Enter)\n')
        if confirm == '1':
            print('Selected file: ',text1)
        else:
            print('File unselected')
    elif lmao=='2':
        break
    elif lmao =='3':
        current_text.pointer_index+=1
    else:
        pointer+=1
        current_object_list.clear()
'''

keyboard.wait('esc')
