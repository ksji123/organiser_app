import os
import shutil
import tkinter
from tkinter import Button, Entry, Frame, Label, Listbox, OptionMenu, StringVar, filedialog
from tkinter.constants import BOTTOM, END, TOP
import time

def organiser_app_window():
    mainscreen = tkinter.Tk()
    mainscreen.title("organize it")
    global scvalue, file_path, result, options
    def copy_files_as_extention(main_folders):
        try:
            main_folder = f"{main_folders}"
            main_folder = main_folder.replace("\\","\\\\")
            subfolders = [main_folder]
            my_folders = [] 
            exts = []
            for folder in subfolders:
                subfolders.remove(folder)
                my_folders.append(folder)
                files = os.listdir(folder)
                for file in files:
                    if not os.path.isdir(os.path.join(folder,file)):
                        ext = file.split('.')[-1]
                        exts.append(ext)
                    else:
                        subfolder = os.path.join(folder,file)
                        subfolders.append(subfolder)
            for ex in exts:
                if not os.path.isdir(os.path.join(main_folder,"types of file")):
                    os.mkdir(os.path.join(main_folder,"types of file"))
                if not os.path.isdir(os.path.join(os.path.join(main_folder,"types of file"),ex)):
                    os.mkdir(os.path.join(os.path.join(main_folder,"types of file"),ex))
            for folder in my_folders:
                my_folders.remove(folder)
                files = os.listdir(folder)
                for file in files:
                    if not os.path.isdir(os.path.join(folder,F"{file}")):
                        ext = file.split('.')[-1]
                        try:
                            folder = folder.replace("\\","/")
                            main_folder = main_folder.replace("\\", "/")
                            shutil.copy(f"{folder}/{file}",f"{main_folder}/types of file/{ext}/{file}")
                            results.insert(END,f"{file} copied successfully")
                        except shutil.SameFileError:
                            results.insert(END,f"{file} already exist")
                        except PermissionError:
                            results.insert(END,f"coping file {file} permission denied")
                        except Exception as e:
                            results.insert(END,f"ERROR! unable to copy")
                        mainscreen.update()
                    else:
                        subfolder = os.path.join(folder,file)
                        my_folders.append(subfolder)
            process.set("process has been done.\n you can exit the app now")
            process_completed.update()
        except Exception as e:
            process.set("failed! check folder is selected")
        
    def move_files_as_extention(main_folders):
        try:
            main_folder = f"{main_folders}"
            main_folder = main_folder.replace("\\","\\\\")
            subfolders = [main_folder]
            my_folders = [] 
            exts = []
            for folder in subfolders:
                subfolders.remove(folder)
                my_folders.append(folder)
                files = os.listdir(folder)
                for file in files:
                    if not os.path.isdir(os.path.join(folder,file)):
                        ext = file.split('.')[-1]
                        exts.append(ext)
                    else:
                        subfolder = os.path.join(folder,file)
                        subfolders.append(subfolder)
            for ex in exts:
                if not os.path.isdir(os.path.join(main_folder,"types of file")):
                    os.mkdir(os.path.join(main_folder,"types of file"))
                if not os.path.isdir(os.path.join(os.path.join(main_folder,"types of file"),ex)):
                    os.mkdir(os.path.join(os.path.join(main_folder,"types of file"),ex))
            for folder in my_folders:
                my_folders.remove(folder)
                files = os.listdir(folder)
                for file in files:
                    if not os.path.isdir(os.path.join(folder,F"{file}")):
                        ext = file.split('.')[-1]
                        try:
                            folder = folder.replace("\\","/")
                            main_folder = main_folder.replace("\\", "/")
                            shutil.move(f"{folder}/{file}",f"{main_folder}/types of file/{ext}/{file}")
                            results.insert(END,f"{file} moved successfully")
                            del file
                        except shutil.SameFileError:
                            results.insert(END,f"{file} already exist")
                        except PermissionError:
                            results.insert(END,f"moving file {file} permission denied")
                        except Exception as e:
                            results.insert(END,f"ERROR! unable to move")
                        mainscreen.update()
                    else:
                        subfolder = os.path.join(folder,file)
                        my_folders.append(subfolder)
            process.set("process has been done.\n you can exit the app now")
            process_completed.update()
        except Exception as e:
            process.set("failed! check folder is selected")
    options = ["all files"]
    def open_file():
        file_path = filedialog.askdirectory(title='select file')
        file_path = file_path.replace("/", "\\")
        scvalue.set(file_path)
        folder_path.set(file_path)
        view_bar.update()
        b2.update()
        b3.update()
        b4.update()
        try:
            main_folder = f"{file_path}"
            main_folder = main_folder.replace("\\","\\\\")
            subfolders = [main_folder]
            exts = []
            opt_ext = []
            for folder in subfolders:
                subfolders.remove(folder)
                files = os.listdir(folder)
                for file in files:
                    if not os.path.isdir(os.path.join(folder,file)):
                        ext = file.split('.')[-1]
                        exts.append(ext)
                    else:
                        subfolder = os.path.join(folder,file)
                        subfolders.append(subfolder)
            for i in exts:
                if i not in opt_ext:
                    opt_ext.append(i)
            mainscreen.update()
            process.set("folder has been selected")
            process_completed.update()
        except Exception as e:
            process.set("failed! check folder is selected")

    def create_shortcut_file(main_folders):
        try:
            main_folder = f"{main_folders}"
            main_folder = main_folder.replace("\\","\\\\")
            subfolders = [main_folder]
            my_folders = [] 
            exts = []
            for folder in subfolders:
                subfolders.remove(folder)
                my_folders.append(folder)
                files = os.listdir(folder)
                for file in files:
                    if not os.path.isdir(os.path.join(folder,file)):
                        ext = file.split('.')[-1]
                        exts.append(ext)
                    else:
                        subfolder = os.path.join(folder,file)
                        subfolders.append(subfolder)
            for ex in exts:
                if not os.path.isdir(os.path.join(main_folder,"types of shortcut file")):
                    os.mkdir(os.path.join(main_folder,"types of shortcut file"))
                if not os.path.isdir(os.path.join(os.path.join(main_folder,"types of shortcut file"),ex)):
                    os.mkdir(os.path.join(os.path.join(main_folder,"types of shortcut file"),ex))
            for folder in my_folders:
                my_folders.remove(folder)
                files = os.listdir(folder)
                for file in files:
                    if not os.path.isdir(os.path.join(folder,F"{file}")):
                        ext = file.split('.')[-1]
                        try:
                            os.symlink(f"{folder}\\{file}",f"{main_folder}\\types of shortcut file\\{ext}\\shortcut_{file}")
                            results.insert(END,f"{file} shortcut created successfully")
                        except Exception as e:
                            results.insert(END,f"ERROR! unable to make shortcut or run as administrator")
                        mainscreen.update()
                    else:
                        subfolder = os.path.join(folder,file)
                        my_folders.append(subfolder)
            process.set("process has been done.\n you can exit the app now")
            process_completed.update()
        except Exception as e:
            process.set("failed! check folder is selected\n or run as administrator")


    note = Label(mainscreen, text="💐welcome! to the app 🎇🎉💐\n\n steps:\n\n 1. select folder by clicking select folder button\n 2. click copy or move button to copy or move\n 3. look the bottom bars to check results and processes\n NOTE: I RECOMEND YOU TO USE COPY METHOD 😁" ,font="algerian 14 italic")
    note.pack(side=TOP)

    folder_path = StringVar()
    scvalue = StringVar()
    view_bar = Entry(mainscreen, text=scvalue,state="readonly",border="10",width="100")
    view_bar.pack()

    def folder_open():
        os.startfile(folder_path.get())




    f1 = Frame(mainscreen)
    b1 = Button(f1, text="select folder",fg="black", command=open_file, border="10",font="algerian 12 bold")
    b1.grid(row=0, columnspan=2)

    b4 = Button(f1, text="open folder",command=folder_open, border="10", justify="center",font="algerian 12 bold", bg="aqua")
    b4.grid(row=1,columnspan=2)

    b2 = Button(f1, text="copy and arrange\n folder", bg="green",fg="white", command=lambda:copy_files_as_extention(folder_path.get()), border="10", justify="center",font="algerian 12 bold")
    b2.grid(row=2, column=0)

    b3 = Button(f1, text="move and arrange\n folder", bg="red",fg="white", command=lambda:move_files_as_extention(folder_path.get()), border="10", justify="center",font="algerian 12 bold")
    b3.grid(row=2, column=1)

    b3 = Button(f1, text="create shortcut\n and arrange\n folder",padx="100", bg="orange",fg="white", command=lambda:create_shortcut_file(folder_path.get()), border="10", justify="center",font="algerian 12 bold")
    b3.grid(row=3, columnspan=2)

    f1.pack()

    f2 = Frame(mainscreen)

    result = StringVar()
    res = Label(f2, text="processes:",font="algerian 15 bold")
    res.grid(row=0, column=0)

    results = Listbox(f2,border="8",width="80",height="20", justify="left",fg="red",font="algerian 8 bold")
    results.grid(row=0, column=1)
    
    pros = Label(f2, text="result:",font="algerian 15 bold")
    pros.grid(row=1, column=0)

    process = StringVar()
    process_completed = Entry(f2, text=process,border="10",width="40", justify="left",fg="green" ,font="algerian 16 bold")
    process_completed.grid(row=1, column=1)


    f2.pack(side=BOTTOM)

    mainscreen.mainloop()


if __name__ == "__main__":
    organiser_app_window()