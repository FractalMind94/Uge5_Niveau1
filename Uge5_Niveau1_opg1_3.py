# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:36:35 2024

@author: KOM
"""

#open .txt file
with open("C:/Users/KOM/Desktop/Opgaver/app_log.txt", "r", encoding="utf-8") as app:
   

# write new file without the given parameters
    with open("C:/Users/KOM/Desktop/Opgaver/new_log.txt", 'w') as new:
        for line in app:
            if "ERROR" not in line and "WARNING" not in line:
                new.write(line)