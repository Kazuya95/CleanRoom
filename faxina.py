import os

PATH = './'
# File extensions that will be organized
EXTENSIONS = {
    "EXECUTABLES": ['.exe', '.msi', '.jar', '.apk'],
    "IMAGES": ['.jpeg', '.jpg', '.tiff', '.gif', '.bmp',
               '.png', '.PNG', '.bpg', '.svg', '.heif', '.psd'],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm",
               ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": ['.txt', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods',
                  '.odt', '.xps', '.dotx', '.docm', '.dox', '.xls', '.xlsx', '.ppt', '.pptx'],
    "PDFS": ['.pdf'],
    "COMPRESSED": ['.rar', '.zip', '.7z', '.bzip2',
                   '.gzip', '.tar', '.wim', '.xz', ],
    "SCRIPTS": ['.ahk', '.js', '.json']
    }

# listagem de arquivos
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

def cleanner():
    allUserFiles = getFilesList(PATH)
    printAllUserFiles(allUserFiles)
    for fileName in allUserFiles:
        userFileExtension = extractFileExtension(fileName)

        for fileType, extensionsList in EXTENSIONS.items():
            for extension in extensionsList:
                if userFileExtension == extension:
                    organizer(fileName, fileType.capitalize())

    print('\nYour files are now organized! =) \n')
    return


if __name__ == "__main__":
    cleanner()
