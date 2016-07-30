import glob
import os

#This function creates the new folder and gathers all the files to call move on each of them.
#Extension: the extension of the files to be moved. eg JPG. 
#newFolder: the name of the folder the files will be moved to. eg videos. 
#path: the current path to the files eg /Users/Gary/Pictures/
def moveFiles(extension, newFolder, path):
  #get location of all files in directory with extension
  filesLocation = os.path.join(path,("*." + extension))
  #read in all the matching file paths
  filenames = glob.glob(filesLocation)
  
  #Check if the folder to move the files to exists, if not create it.
  if not os.path.exists(path + newFolder):
     os.makedirs(os.path.join(path, newFolder))
  
  #for each file, move the file to the new folder.
  for file in filenames:
    move(file, newFolder)
    
#This function moves a file to the new location.
#file: the file to be moved
#newFolder: the name of the folder the file should be moved to.
def move(file, newFolder):
  #get the length of the file name without the path.
  fileNameLength = (len(file) - file.rindex("/") - 1)
  #get the name of the file from the path
  fileName = file[-fileNameLength:]
  #remove the file name from the path of the file.
  filePath = file[:-fileNameLength]
  #the new path for the file
  newFilePath = os.path.join(filePath,newFolder, fileName)
  
  #if the file already exists in the new folder, change the file name. Else move the file
  if os.path.exists(newFilePath):
    print "Error! File: " + fileName + " already exists!" 
    #retrieve a new file name from the user
    fileName = raw_input("Enter a new name for the file:")
    #rename the file to the inputted file name.
    os.rename(file, filePath + fileName)
    #move the renamed file.
    move(filePath + fileName, newFolder)
  else:
    #move the file to the new location.
    os.rename(file, newFilePath)
    print fileName + " moved to " + newFilePath
  