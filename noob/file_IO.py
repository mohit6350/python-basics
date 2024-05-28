import os

path = "C:\\Users\\Khare\\Desktop\\python_stuff"
'''
try:
    os.mkdir(path)
    print("created successfully.")
except FileExistsError:
    print("Directory already created.")
except OSError as error:
    print(error)    
'''
print("Scanning for data....")    
path = "F:\\"

dir_count = 0
file_count = 0

for root,dirs,files in os.walk(path):
    
    for dir in dirs:
        print(f"Directory: {dir}")
        dir_count = dir_count + 1
        for file in files:
            file_count = file_count + 1
            print(f"file : {file}")
            
print(f"Total dir: {dir_count}")
print(f"Total files: {file_count}")
