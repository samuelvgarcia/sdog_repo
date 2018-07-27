#Basic scripting in Python

#Modules to import
import os  #low level stuff like listdir, change dir, rename file, get the path / directory 
import shutil as sh #high level shell commands like copyfile
import subprocess as spr #for running shell commands
import sys  #argv (getting shell arguments), and exit for leaving script execution
import inspect


# def we_are_frozen():
#     # All of the modules are built-in to the interpreter, e.g., by py2exe
#     return hasattr(sys, "frozen")

# def module_path():
#     encoding = sys.getfilesystemencoding()
#     if we_are_frozen():
#         return os.path.dirname(unicode(sys.executable, encoding))
#     return os.path.dirname(unicode(__file__, encoding))

# import basic_scripting
# my_path = basic_scripting.module_path()

from inspect import getsourcefile
from os.path import abspath, dirname

#Get current directory of this file
# cwd1 = os.path.abspath( __file__ )
# cwd = os.path.dirname( cwd1 )
cwd = dirname( abspath(getsourcefile(lambda:0)) )
# cwd = dirname(cwd1)
# Note: this won't work if we are running the file 
# from an interactive environment like ipython or idle

# Another option some people do is:
# f_path = os.path.abspath( __file__ )
# cwd = os.path.dirname( f_path ) #just the directory which contains this file
# However: This can work in an interactive environment
# if the python script calls a second script
# and that second script uses the abspath method
# but at that point, we already know where we are

# print( cwd1 )
# print( cwd )
##

print("\nThis python script is located at:")
print(cwd + '\n')

#DEBUG
# cwd = os.getcwd()
# print(__file__)
# f_path = os.path.abspath(__file__) #full path of this python file
# f_path = inspect.getsourcefile(lambda _: none)
# print(f_path)

#Change working directory
my_path = "/Users/sdog/Documents/Python_Scripts/test_files"
os.chdir( my_path ) #makes "path" the current directory 

#List all files in path 
my_str = os.listdir( my_path )
quot = '\"' #(for printing quotation mark)
print( "List of all files in " + quot + my_path + quot + " :\n")  
print( my_str )
print()

x = 77.1
s = "x = " + str(x)
print( s + '\n' )

#Create file
fname1 = "file1.txt"
tmp = open( fname1, 'w' )
tmp.write( "this is a test file\n")
tmp.close()

#Copy file
fname2 = "file2.txt"
sh.copyfile( fname1, fname2 )

#Remove files:
os.remove( fname1 )

#Create directory
my_path2 = my_path + "/tmp_folder"
if not (os.path.exists( my_path2 ) ):
    os.makedirs( my_path2 ) 
    print( "directory created" )

#Move file
sh.copyfile( fname2, my_path2 + "/" + fname2 ) #copies file to new directory
os.remove( fname2 ) #then removes the old file


#Shell arguments
sys.argv #list of all arguments in shell
#this is usefull when getting shell inputs into python scripts
#for example if in the shell we typed in:
#python my_script.py input.txt output.txt
#then sys.argv() -> ["my_script.py", "input.txt", "output.txt"]
print( sys.argv[0] )


#Run Shell commands from within Python
#i.e. run a python script from within a python script
#Also demonstrating try/except block
tmp_path = my_path + "/../"  #try commenting this out to get error

try:
    spr.run( ["python",  tmp_path + "hello.py"] )

except:
    print( "error, check code\n")
    sys.exit()

print( "We got through try/except block")
tmp = spr.run( ["ls", "-l"] )

#if on Windows
"""
spr.run( ["dir"], shell=1 )

"""

# my_str = os.path.abspath(__file__)
# print(my_str)
# my_str2 = os.path.dirname( my_str )
# print(my_str2)








