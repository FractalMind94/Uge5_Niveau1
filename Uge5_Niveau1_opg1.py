# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:40:08 2024

@author: KOM
"""
# define path for known file
app_path = "C:/Users/KOM/Desktop/Opgaver/app_log.txt" #absolute file path for known file
#define new path for new file
new_path = "C:/Users/KOM/Desktop/Opgaver/new_log.txt" #absolute file path for new file

# open .txt and store it in data list
with open(app_path, "r", encoding="utf-8") as app:
    #removing given parameters and store them in a list
    data=[line for line in app.readlines() if "ERROR" not in line and "WARNING" not in line]

# write new file 
with open(new_path, 'w') as new:
    for line in data:
        new.write(line)
        

        
