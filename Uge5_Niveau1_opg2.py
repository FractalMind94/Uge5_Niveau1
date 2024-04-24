# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:13:45 2024

@author: KOM
"""
# define path for known file 
source_path="Desktop/Opgaver/Uge5_niveau1/source_data.csv" #relative file path
#define new path for new file
new_source_path="Desktop/Opgaver/Uge5_niveau1/new_source_data.csv" #relative file path

try:
    # Define path for file and read
    with open(source_path,"r", encoding="utf-8") as source:  
        # write new file in defined directory
            with open(new_source_path, 'w') as new:
                for line in source:
                    new.write(line)

# If error print error and error type
except FileNotFoundError as e:
    print()
    print("Directory or File does not exist, Errortype=", repr(e))
    print()
except NameError as d:
    print()
    print("Name Does Not Exist, Errortype=", repr(d))
    print()
except PermissionError as g:
    print()
    print("File is Protected, Errortype=", repr(g))
    print()
else:
     print()
     print("Your file has been saved in folder as:", new_source_path )
     print()
    
        