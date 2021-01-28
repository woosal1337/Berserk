
from os import listdir
from os import path as osPath
from sys import path as sysPath
from inspect import getfile,currentframe
from shutil import rmtree


# to find the previous directory as many as the given number
def parentPath(parentCount):
    currentDir = osPath.dirname(osPath.abspath(getfile(currentframe())))
    for parent in range(parentCount):
        parentDir = osPath.dirname(currentDir)
        currentDir = parentDir
    return currentDir


# to import the previous directory as many as the given number
def importParent(parentCount):
    try:
        currentDir = osPath.dirname(osPath.abspath(getfile(currentframe())))
        for parent in range(parentCount):
            parentDir = osPath.dirname(currentDir)
            currentDir = parentDir
        sysPath.insert(1, currentDir)
        return True
    except:
        return False


# to remove directory
def removeDir(dir_name):
    try:
        rmtree(dir_name)
        return True
    except:
        return False


# finding a file from any given directory
def findFile(pathOfFile, fileName):
    files = listdir(pathOfFile)
    for file in files:
        if file == fileName:
            return fr"{pathOfFile}\{file}"
    else:
        return False


# scanning of given directory
def scanDir(pathOfFile):
    files = listdir(pathOfFile)
    fullPathFileList = []
    for file in files:
        fileName = r"{0}\{1}".format(pathOfFile,file)
        fullPathFileList.append(fileName)
    return fullPathFileList
