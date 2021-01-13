#JAN 11: PROJECT NO.01 - DOWNLOADS FILE ORGANISER
# This project basically automatically places each file to a folder based on either its filetype
# or a specific code I use when naming my files - in this case I use "DS_", "CS_", "MATH_" 
# to put any file with a name starting with that code into a corresponding folder. 
# This way, if I don't want a file to be organised by its filetype I can use one of the codes instead.
#
# This has taught me the use of dictionaries and introduced me to some basic python libraries and syntax
# Also taught me how to have a python script run remotely in the background.
# Possible extension would be to implement comprehension for the dictionary. It might be something I might do in the next project.
# Another extension would be to create the folders automatically so 
# that others can run the script without having to create each folder in the directory themselves.

import os

FOLDER_PATH = 'C:\\Users\\abhin\\Downloads'

folder_dict = {
	"IMAGES": ["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg",
			"heif", "psd"],
	"VIDEOS": ["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng",
			"qt", "mpg", "mpeg", "3gp","mkv"],
	"DOCUMENTS": ["doc", "pptx", "pdf", "docx", "doc", "xla","csv"],
	"AUDIO": ["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3",
			"msv", "ogg", "oga", "raw", "vox", "wav", "wma"],
	"PLAINTEXT": ["txt", "in", "out"],
    "EBOOKS": ["mobi", "epub"],
    "RAR": ["zip"],
	"PYTHON": ["py"],
	"XML": ["xml"],
	"EXE": ["exe"],
    "DATA": ["DS_"],
    "COSC": ["CS_"],
    "MATH": ["MATH_"],
}

folders = list(folder_dict.keys())
frmtList = list(folder_dict.values())

def returnFldrName(myFrmt):
    i = 0
    for frmt in frmtList:
        if myFrmt in frmt:
            return folders[i] 
        i += 1
    return "OTHER"

def listDir(dir, ext, fldr):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        if fileName.find(ext, 0) != -1:
            os.replace(dir + "\\" + fileName, dir + "\\" + fldr + "\\" +  fileName)
        elif fileName.find("." + ext) != -1:
            os.replace(dir + "\\" + fileName, dir + "\\" + fldr + "\\" +  fileName)


def returnDirFrmtList():
    dirFrmtList = set()
    fileNames = os.listdir(FOLDER_PATH)
    subjectKeyList = ["DS_", "CS_", "MATH_"]
    for fileName in fileNames:
        for subject in subjectKeyList:
            if subject in fileName:
                dirFrmtList.add(subject)
        if fileName.rfind(".") != -1:
            dirFrmtList.add(fileName[fileName.rfind(".")+1: len(fileName)])
    return(dirFrmtList)


def main():
    dirFrmtList = returnDirFrmtList()
    for Frmt in dirFrmtList:
        print(Frmt, returnFldrName(Frmt))
        listDir(FOLDER_PATH, Frmt, returnFldrName(Frmt))

main()
