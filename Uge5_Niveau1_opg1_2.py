# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:20:08 2024

@author: KOM
"""

app = "C:/Users/KOM/Desktop/Opgaver/app_log.txt"
new = "C:/Users/KOM/Desktop/Opgaver/new_log.txt"

with open(app, "r", encoding="utf-8") as app, open(new, 'w') as new:
    for line in app:
        if "ERROR" not in line and "WARNING" not in line:
            new.write(line)