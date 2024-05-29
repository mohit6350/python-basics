import os
import psutil

drives = psutil.disk_partitions(all=True)
drive_info = []

def get_files(drive_mountpoint):
    dir_count = 0
    file_count = 0
    drive_path = drive_mountpoint
    output_lines = []
    
    for root, folders, files in os.walk(drive_path):
        for folder in folders:
            folder_path = os.path.join(root, folder)
            output_lines.append(f"Folder: {folder_path}")
            dir_count += 1
            
        for file in files:
            file_path = os.path.join(root, file)
            output_lines.append(f"File: {file_path}")
            file_count += 1
    
    output_lines.append(f"Total folders: {dir_count}")
    output_lines.append(f"Total files: {file_count}")
    
    return output_lines

def get_drives_data():
    for drive in drives:
        drive_dict = {
            "device" : drive.device,
            "mountpoint": drive.mountpoint
        }
        usage = psutil.disk_usage(drive.mountpoint)
        drive_dict["total_size"] = int((((usage.total/1024)/1024)/1024))
        drive_dict["free_size"] = int((((usage.free/1024)/1024)/1024))  # Fixed typo (1204 -> 1024)
        drive_info.append(drive_dict)
    return drive_info

if __name__ == "__main__":
    
    # Get drive data and write to file
    infos = get_drives_data()
    with open("D://mohit//data_collected.txt", "w", encoding="utf-8") as file:
        for info in infos:
            file.write(str(info) + "\n")
            print(info)

    # Get files data and write to the same file
    DRIVES_NAME = ["D://","E://"]
    for drive in DRIVES_NAME:
        files_data = get_files(drive)
        with open("D://mohit//data_collected.txt", "a", encoding="utf-8") as file:
            for line in files_data:
                file.write(line + "\n")
                print(line)
