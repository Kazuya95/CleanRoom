'''
Fase 1: Geral
( ) organizacao por tempo de modificacao
( ) gerar relatorio do que foi transferido
( ) Exibicao na propria GUI
'''

import os
from tkinter import *
from tkinter.filedialog import *
import json

def getFilesList(path):
    return os.listdir(path)

def printAllUserFiles(allFilesArray):
    print('List of files and folders found:\n')
    for i in range(len(allFilesArray)):
        print('{}'.format(allFilesArray[i]))


def createDestinyFolder(fileFolder):
    if not os.path.exists(fileFolder):
        print('Making directories')
        os.makedirs(fileFolder)
    else:
        pass

def moveFileToDestinyFolder(fileName, destinyFolderName):
    try:
        os.rename(os.path.join('./', fileName),
                  os.path.join(destinyFolderName, fileName))
    except:
        pass

def organizer(fileName, destinyFolderName):
    createDestinyFolder(destinyFolderName)
    moveFileToDestinyFolder(fileName, destinyFolderName)
    print('The file {} is moved.'.format(fileName))

def extractFileExtension(fileName):
    return str(fileName[fileName.rfind('.'):])

def choiced_folder():
    whatFolder = askdirectory()
    os.chdir(whatFolder)
    return os.getcwd()

def jason_read(name):
    with open(name) as f:
        data_listofdict = json.load(f)
        return data_listofdict

def cleanner():
    EXTENSIONS = jason_read('C:/Users/Johnny/Desktop/conteiner/programacao/py/py3/faxina/extension.json')
    address = choiced_folder()
    allUserFiles = getFilesList(address)
    printAllUserFiles(allUserFiles)
    for fileName in allUserFiles:
        userFileExtension = extractFileExtension(fileName)
        for fileType, extensionsList in EXTENSIONS.items():
            for extension in extensionsList:
                if userFileExtension == extension:
                    organizer(fileName, fileType.capitalize())

    print('\nYour files are organized!\n')
    

def manager():
    clean=Tk()
    clean.title('CleanRoom v0.0')
    clean.geometry('400x400')

    visor_frame = LabelFrame(clean,text= 'See the outputs here')
    visor_frame.grid(row=0,column=0)
    screen = Label(visor_frame,text='',width=20,height=10)
    screen.grid(row=0,column=0)

    ask_frame = LabelFrame(clean,text= 'Choice the path')
    ask_frame.grid(row=1,column=0)
    do_it = Button(ask_frame,text='Cleanroom',command=cleanner)
    do_it.grid(row=0,column=0)

    clean.mainloop()

if __name__ == "__main__":
    manager()
