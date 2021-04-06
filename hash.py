#Jonathan Gill Sarah Osbourne
#03/25/21
#refrences programiz.com/python-programming/methods/list/remove
#geeksforgeeks.org/python-os-listdir-method/
#tutorialspoint.com/python/os_walk.html
#geeksforgeeks.org/sha-in-python/

import os
import hashlib
        
def vet(dirlist): #vets list for uneeded directories
    dirlist.remove('dev')
    dirlist.remove('proc')
    dirlist.remove('run')
    dirlist.remove('sys')
    dirlist.remove('tmp')
    return dirlist

def gettree(list2):#gets tree
    pathinfo = [ ]
    for i in list2:
        for root,dirs,files in os.walk(i,topdown= True):
            for name in files:
                x = (os.path.join(root,name))
                pathinfo.append(x)


    return pathinfo
            
        

def gettimea(pathinfo): #gets time accessed
    timeaccessed = []
    for i in pathinfo:
        x= os.stat(i)
        atime = x[7]
        timeaccessed.append(atime)



    return timeaccessed

def gettimem(pathinfo): #gets time modified
    timemodified = []
    for i in pathinfo:
        x= os.stat(i)
        atime = x[8]
        timemodified.append(atime)



    return timemodified 

def hashme(filetree): #makes a hashlist
    hashlist = []
    for i in filetree:
        ihash = hashlib.sha256(i.encode())
        ihash2 = ihash.hexdigest()
        hashlist.append(ihash2)

    return hashlist


########################################################################


list1 = os.listdir('/')  #gets paths

data = open("hashdata.txt",'w+') #gets data

rtest = data.read()  #gets test sample

rdata = rtest.split(' ') #gets hash comparison from hashfile

list2 = vet(list1) # vets paths

filetree = gettree(list2) #makes tree from vetted path

timea = gettimea(filetree) #gets time accessed

timem = gettimem(filetree) #gets time modified

data2 = hashme(filetree) #gets new hashes from paths

counter = 0

#tests for data manipulation and list file path/info

if rtest =='' :

    for i in filetree:
        print(" The name and path of the file is" + " " + str(i)) 
        print( " It was last accessed at time " + " " + str(timea[counter]))
        print ( " It was last modified at time " + " " + str(timem[counter]))
        print(" ")
        counter+= 1
        

if rtest != '':

    for i in filetree:

        print(" The name and path of the file is" + " " + str(i)) 
        print( " It was last accessed at time " + " " + str(timea[counter]))
        print ( " It was last modified at time " + " " + str(timem[counter]))
        if data2[counter] != rdata[counter]:
            print(" This file has been modified since previous hashing")
        print(" ")
        counter +=1
        



for i in data2:
    data.write(i)
    data.write(' ')

data.close()








