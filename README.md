# Gill-Osborne
Lab8 Code and README.txt file 
Summary: 


Our code walks through the files on a file system. The result of our code prints out the file names and their paths. We have provided a list of specified files directories that our code will ignore (i.e. /dev, /proc, etc.). These file directories are ignored as they are considered unhashable. For part 1, we utilized the python libraries os.listdir and os.walk to help us organize the file system’s information. The library os.listdir takes the input of a file path and returns the entry names in the directory in a list format. Os.listdir allows us to see what files are in what directories. Once we know what files are in what directories, we can utilize os.walk to file trees. Os.walk generates the file names in a directory tree by ‘walking’ to different file (nodes). This library allows us to go through the entire file system and return their paths to the user. Os.walk will skip over the files that we have deemed unhashable. 


For part 2, we utilized the hashlib python library. Hashlib generates a SHA2 hash for files that are moving through the file system. Based upon the information that we gathered in Part I, we are able to apply hashes to each file in the file tree. 


For part 3, we stored the file and hash information by writing it to a file. The out file contains the filename with its full path, the hash of the file, and the date/time it was observed. 


Finally, our code is able to run and update the hash information associated with the file, show any new files within the file system, show what files have been modified, and print out a summary of this information into a file.
