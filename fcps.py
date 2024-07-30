import os.path
from time import sleep
import datetime
from os import system,remove,rmdir,listdir,path,mkdir
from shutil import copy
current_year = datetime.datetime.now().year
import cryptography.fernet
from tkinter import messagebox
import tkinter as tk
from PIL import Image,ImageTk
key = cryptography.fernet.Fernet.generate_key()
x = cryptography.fernet.Fernet
#calling remove function from os module
gui = tk.Tk()
gui.title("FCP file creator")
gui.geometry('300x300')
gui.resizable(False, False)
try:
    imagepath = Image.open('./FCPlogo.png')
    image = ImageTk.PhotoImage(imagepath)
    gui.iconphoto(False, image)
except FileNotFoundError:
    pass
tk.Label(gui,text='*enter the filepath of the FCPSF').pack()
filepath = tk.StringVar()
entry = tk.Entry(gui,width=42,textvariable=filepath).pack()
tk.Label(gui,text='*enter the files list which would be contained in FCPSF').pack()
filelist = tk.StringVar()
entry = tk.Entry(gui,width=42,textvariable=filelist).pack()
def exitto(cool=True):
    gui.destroy()
    if cool == True:
        messagebox.showinfo(title="good news",message=r"the creation process has been 100% completed")
    else:
        pass
    exit()
def ask():
    ask = tk.messagebox.askyesno(title="Confirm Deletion", message="""can the FCPDA delete the output folder if the app
    made this folder allow to it to delete the folder but if you made this folder you should know that you must to change it's name because
    names for folders(output,build,DSA) would make problems to the system""")
    if ask:
        try:
            rmdir('./output')
        except (FileNotFoundError,OSError):
            for k in range(len(listdir('./output'))):
                try:
                    remove(f'./output/{listdir("./output")[k]}')
                except PermissionError:
                    pass
            rmdir('./output')
    exitto(False)
class filecontainer():
    #the class start
    def __init__(self):
        #just make this function for the "self" of the class
        pass#pass it because it does nothing
    #no goal __inti__ function
    def find_between(self,code:str,first_word:str, second_word:str, occurrence:int):
        #this function is an important in-system function found in a lot of wedu programs
        #-----------------------------------------------------------------------
        #THE OCCURRENCE VAR IS THE SAME AS SAYING 'THE OCCURRENCE PARAMETER'
        #-----------------------------------------------------------------------
        lines = code.strip().split("\n")
        #takes the main code and strip it and split \n
        first_line_number = None
        second_line_number = None
        count = 0
        """it's important to set it 0 for this line(*1) which will increase it by 1
        with each circle of a loop"""
        for i, line in enumerate(lines):#i*0.5 is the same i in the line
            #a for loop which will the value of i and line vars. by enumerate the lines var.
            if first_word in line:
                #if the first_word var. is found in line var increase the count var.
                count += 1#*1 the line
                if count == occurrence:
                    """if the count var. has the same value as the occurrence var set
                    first_line_number as the same value as i"""
                    first_line_number = i#set first_line_number as the same value as i
            if second_word in line and count == occurrence:
                """if the second_word var. is found in line var and count var. 
                has the same value as the occurrence var set second_line_number 
                as the same value as i"""
                second_line_number = i#set second_line_number as the same value as i
                break
                #break the loop if the case for this if statement applyed after it's operations are completed
        if first_line_number is not None and second_line_number is not None:
            """if these two doesn't have the value of None(they are having the same value 
            as i*0.5) that means (first and second word vars. must be found in line 
            and the count var has the same vaule as the occurrence var)"""
            words_between = []#setting the words_between var as a plank list
            for i in range(first_line_number + 1, second_line_number):
                #a loop that it's range starts at(first_line_number + 1, second_line_number)
                line = lines[i].strip()
                """the line var which is mostly a part from the lines var
                and the part is special part identified from others by having the same
                index as the value of i var. and after all of that it's all striped out"""
                words_between.append(lines[i])
                #this will add lines[i] to the word_between var. which is a list
            return words_between#this will return the word_between var
        else:#if first or second line_number is or both None
            return []  # If either first_word or second_word is not found in the file or occurrence is not found
    def list_to_string(self,lst):
        #the same as the find_between function it will turn a list to a string
        string = '\n'.join(lst)
        #this var. the list after it's converted to a list
        #----------------------------------------------------------
        """this is info about the return functiob but I can't but it after it because the
        return line is the last line of any function that contains it"""
        #----------------------------------------------------------
        """this function will return the value of the string var. and it will
        replace \n with \\n inside(r'') as part to solve the PSRP"""
        #----------------------------------------------------------
        return string.replace(r'\\n',r'\n')
    def FCmaker(self,file_path:str,filespatho_list:list):
        if file_path != f'{file_path[:-3]}.py':
            messagebox.showerror(title="bad news", message=r"""an error because of filepath has no fileformat or it's not the .py file format
note:you must write the file name like this: 'name.py' no folder at the back or front of it and you must to write the .py file format""")
            exitto(False)
        try:
            mkdir('./output')
        except FileExistsError:
            messagebox.showinfo(title="bad news you might get an error",message=r"""an error happened because you have folder with the name output
which the system automatically creates it so if it exists already that would cases an error now the system would ignore that for you but if there is any
thing in that folder had the same name as any of the automatically generated temp files and etc... you would get an error""")
        """this function will put data into any fc file
        parameters:
        file_path:str :the fc file path with file format off course
        filespatholist:list : the files that you want to put in the fc file"""
        #-----------------------------------------------------
        self.filepath = file_path
        #setting the file_path parameter to self.filepath
        self.fileslist = filespatho_list
        #setting the filespatho_list parameter to self.fileslist
        copy('./FCPlogo.png', './output/FCPlogo.png')
        #-----------------------------------------------------
        """setting the parameter as vars. to make them easier and better for both inside and
        outside this function"""
        #-----------------------------------------------------
        self.i = 0
        """this is the first value for the self.i which is 0 and it will get higher by 1 
        each time it's being used in the and _extracted_from_FCmaker_9 it's important 
        because it's used as indentifier for each chank"""
        #------------------------------------------------------
        try:
            self.delfile = open(f'./output/{self.filepath}', 'w')
            self.delfile.write('')
            self.delfile.close()#clear all data of the file in self.filepath
            self.base = open(f'./output/{self.filepath}','w')
            self.base.write(f"""import cryptography.fernet
import tkinter as tk
import os
from tkinter import messagebox
from PIL import Image,ImageTk
gui = tk.Tk()
gui.title("FCP file opener")
gui.geometry('300x300')
gui.resizable(False, False)
try:
    imagepath = Image.open('./FCPlogo.png')
    image = ImageTk.PhotoImage(imagepath)
    gui.iconphoto(False, image)
except FileNotFoundError:
    pass
tk.Label(gui,width=23,height=14,background='light grey').place(x=0,y=0)
tk.Label(gui,text='file path: {self.filepath[:-3]}.exe',background='light grey').place(x=0,y=0)
tk.Label(gui,text='number of files: {len(self.fileslist)}',background='light grey').place(x=0,y=30)
tk.Label(gui,text='FCP file version: 2.0 BETA',background='light grey').place(x=0,y=60)
tk.Label(gui,text="THE HEAVY DRAGON EDITION",background='light grey').place(x=0,y=90)
tk.Label(gui,text="FCP program mark type: -ODS",background='light grey').place(x=0,y=120)
tk.Label(gui,text="COPYRIGHT {current_year} WEDU",background='light grey').place(x=0,y=150)
tk.Label(gui,text="All RIGHTS RESERVED",background='light grey').place(x=0,y=180)
tk.Label(gui,text='Enter the password').place(x=180,y=0)
PASSWORD = tk.StringVar()
entry = tk.Entry(gui,width=21,textvariable=PASSWORD).place(x=168,y=20)
def exito(case=True):
   gui.destroy()
   if case == True:
      messagebox.showinfo(title="good news",message=r"the extracting process has been 100% completed")
   else:
      pass
   exit()
def openfile(PASSWORD):\n""")
            self.base.close()
            for i2 in range(len(self.fileslist)):
                #a loop that it's length is how many items in the self.fileslist var.
                self._extracted_from_FCmaker_9(i2, self.fileslist)#calling the _extracted_from_FCmaker_9
            self.base2 = open(f'./output/{self.filepath}','a')
            print(f"""   ORG_PASSWORD = {key}
   if PASSWORD == ORG_PASSWORD:
      try:
         os.mkdir('./extracted_data')
      except FileExistsError:
         messagebox.showerror(title="bad news",message='''so this error happened because of the system wanted to make a folder with the name
extracted_data but a folder with the same name existed before the system would try make to the extracted_data folder''')
         aska = tk.messagebox.showinfo(title="you should do something", message='''can the you delete the extracted_Data folder if the app
made this folder delete the folder but if you made this folder you should know that you must to change it's name because
names for folders(extracted_data,output,build,..._build,dist,DSA) would make problems to the FCP topic apps because these apps
would make folders with the same as these name to store or do operations and things like that but when they exist already the system would be in problem''')
         exito(False)
   else:
      messagebox.showerror(title="wrong password",message='''you wrote a wrong password so you can't extract 
the data expect if you wrote a correct password''')
      exito(False)
""",file=self.base2)
            self.base2.close()
            self.base3 = open(f'./output/{self.filepath}','a')
            for i3 in range(len(self.fileslist)):
                print(f"""   FREE{i3 + 1} = cryptography.fernet.Fernet(PASSWORD).decrypt(cryptography.fernet.Fernet(ORG_PASSWORD).encrypt(d{i3 + 1}[3:-2]))
   FREEPATH{i3 + 1} = str(cryptography.fernet.Fernet(PASSWORD).decrypt(cryptography.fernet.Fernet(ORG_PASSWORD).encrypt(p{i3 + 1}[1:-1])),'utf-8')
   open(f'./extracted_data/""" + '{FREEPATH' + f'{i3 + 1}' + "}'" + """,'x').close()
   w""" + f"""{i3 + 1} = open(f'./extracted_data/""" + '{FREEPATH' + f'{i3 + 1}' + "}'" + """,'wb')
   w""" + f"""{i3 + 1}.write(FREE""" + f'''{i3 + 1}''' + """)
   w""" + f"""{i3 + 1}.close()""", file=self.base3)
            print("""   exito()
def openfiles():
   print(bytes(PASSWORD.get()[2:-1],'utf-8'))
   openfile((bytes(PASSWORD.get()[2:-1],'utf-8')))
button = tk.Button(gui,text='send',command=openfiles).place(x=213,y=42)
gui.mainloop()""", file=self.base3)
            self.base3.close()
        except (PermissionError,AttributeError,OSError):
            messagebox.showerror(title="bad news", message=r"an error because of wrong info or it's just Permission denied")
            ask()
        system(f'cd ./output/ & pyinstaller --noconsole {self.filepath}')
        #try:
        while (0==0):
            if os.path.exists(f'./output/dist/{self.filepath[:-3]}'):
                system(f'''powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c cd {path.dirname(path.abspath(__file__))}/output/ & MOVE build {self.filepath[:-3]}_build & MOVE dist DSA'"''')
                while (0==0):
                    if os.path.exists(f'./output/DSA/{self.filepath[:-3]}'):
                        try:
                            copy('./output/FCPlogo.png', f'./output/DSA/{self.filepath[:-3]}/FCPlogo.png')
                            open(f'./output/{file_path[:-3]}_password.txt','x').close()
                            passfile = open(f'./output/{file_path[:-3]}_password.txt', 'w')
                            passfile.write(f'{key}')
                            passfile.close()
                        except FileExistsError:
                            ask()
                        remove(f"./output/{self.filepath}")
                        remove('./output/FCPlogo.png')
                        break
                    else:
                        sleep(10)
                break
            else:
                sleep(5)
        """
        except (FileNotFoundError,PermissionError):
            messagebox.showerror(title="bad news",message="an error happened because you wrote a name of folder before the file name\n or a Permisstion error but it's mostly because you wrote folder name you must to write filename with .py extension nothing more or less")
            exitto(False)
        """
        messagebox.showinfo(title="the password it's found in...",message=f"we sent it in a text file called\n'./output/{file_path[:-3]}_password.txt'")
        exitto()
    def _extracted_from_FCmaker_9(self, i2, fileslist):
        self.i += 1
        '''important var. that gives the number for each chank to make it diffrent from the
        other chanks in the chank-base'''
        try:
            self.makefilechank = f"""   d{self.i} = b'''"{open(fileslist[i2],'rb').read()}"'''\n"""
        except FileNotFoundError:
            messagebox.showerror(title="bad news",message=r"an error happened because one of the files in the filelist wasn't found")
            remove(f'./output/{self.filepath}')
            ask()
            exitto(False)
        #this is the part that makes the place for files data(data chank)
        self.makepathchank = f"""   p{self.i} = b'''"{fileslist[i2]}"'''\n"""
        #this is the part that makes the place for files paths(path chank)
        #--------------------------------------------------------
        self.writingfile = open(f'output/{self.filepath}','a')
        #start I/O operations for the fc file with the append mode
        print(self.makefilechank, file=self.writingfile)#writing the data chank in the fc file
        print(self.makepathchank, file=self.writingfile)#writing the path chank in the fc file
        #writing both chanks into the fc file
        self.writingfile.close()#close all file operations
FC = filecontainer()
def do_it():
    print(filepath.get())
    temp1 = filelist.get()
    thelist = []
    for i in range(len(temp1.split(','))):
        thelist.append(temp1.split(',')[i])
    print(thelist)
    FC.FCmaker(filepath.get(),thelist)
tk.Button(gui,text='create',command=do_it,background='blue',foreground='yellow',borderwidth='4',font=("Arial", 10, "bold"),width=10).pack(pady=5)
tk.Label(gui,width=50,height=100,background='light gray').place(x=0,y=120)
tk.Label(gui,text='FCP file creator version: 2.0 BETA',background='light gray').place(x=0,y=130)
tk.Label(gui,text="THE HEAVY DRAGON EDITION",background='light gray').place(x=0,y=160)
tk.Label(gui,text="FCPFC mark type: -ODS",background='light gray').place(x=0,y=190)
tk.Label(gui,text=f"COPYRIGHT {current_year} WEDU",background='light gray').place(x=0,y=220)
tk.Label(gui,text="All RIGHTS RESERVED",background='light gray').place(x=0,y=250)
gui.mainloop()