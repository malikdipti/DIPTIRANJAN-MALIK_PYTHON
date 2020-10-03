# importing os module   
import os 
path = os.getcwd() 
  
  
print("Directory entry name and their inode number")  
with os.scandir(path) as itr: 
    for entry in itr : 
        # Exclude the entry name 
        # starting with '.'   
        if not entry.name.startswith('.') : 
            # print entry name 
            # and entry's inode() number  
            print(entry.name, " :", entry.inode()) 
