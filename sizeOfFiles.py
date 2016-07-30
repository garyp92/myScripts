import os, glob

#This function gets every sub directory of dir and pases each directory to the function to get total size of the files in that directory
#dir: the root directory in which to start the search.
def getSizeAllSubDirs(dir):
  for path, dirs, files in os.walk(dir):
    #get the size of the files in the current directory.
    getTotalSizeFiles(path)
    #for each subdirectory, recurse to search all child directories.
    for dirName in dirs:
      getNestedDirectory(os.path.join(path,dirName))

#This function gets the total size in MB of the files in a directory.
#dir: the directory which the files to count are located.
def getTotalSizeFiles(dir):
  #get all the files in dir.
  fileNames = glob.glob(os.path.join(dir,"*.*"))
  totalBytes = 0
  totalMB = 0.0
  #open a log txt file for appending
  dataFile = open("sizeInfo.txt", "a")
  
  #for each file in the directory get the size and increase the totalSize accordingly
  for file in fileNames:
    fileSize = os.path.getsize(file)
    totalBytes += fileSize

  #Convert size from bytes to MB
  totalMB = totalBytes/1000000
  #Append data to the end of the log file.
  s = "Size of files in directory %s = %f MB" % (dir, totalMB)
  dataFile.write(s + "\n")