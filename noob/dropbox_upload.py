import dropbox

def upload_to_dropbox(file_path, access_token):
    dbx = dropbox.Dropbox(access_token)
    for entry in dbx.files_list_folder('').entries:
        print(entry.name)
        
    try:
        dbx = dropbox.Dropbox(access_token)

        with open(file_path, "rb") as f:
            file_data = f.read()

        file_name = '/' + file_path.split('/')[-1]

        dbx.files_upload(file_data, file_name)
        print(f"File '{file_name}' uploaded successfully.")
    except dropbox.exceptions.ApiError as err:
        print(f"Failed to upload file: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ACCESS_TOKEN = ''
    FILE_PATH = 'C://Users//Khare//Desktop//nf//2.png'

    upload_to_dropbox(FILE_PATH, ACCESS_TOKEN)
