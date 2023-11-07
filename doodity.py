import os
from pydub import AudioSegment
from pydub.utils import mediainfo
from alive_progress import alive_bar; import time
import time

UserInput = ""

def loadingbar(file_size_mb):
    # Use file size in MB as the total
    with alive_bar(file_size_mb) as bar:  
        for _ in range(int(file_size_mb)):
            # Simulate loading for each MB
            time.sleep(0.1)  
            bar()  

files_db = {}

def UploadPage():
    file_path = input("Please enter the path of your .wav or .mp3 file to upload: ")
    upload_result = upload_file(file_path)
    if upload_result is not None:
        # Unpack and return the result if it is not None
        return upload_result
    # If upload_result is None, return a tuple with two None values
    return (None, None)



def Submitted(file_size_mb):
    loadingbar(file_size_mb)
    print("Submitted! In later implementation this will use my partner's microservice to upload the file to a different python file and start analyzing the DB's!")


def UploadHistory():
    print('Upload history will be displayed here. it will utilize microservice')
    
def is_valid_file(filename):
    return filename.lower().endswith(('.wav', '.mp3'))

def loading_bar():
    print('hi')
    


def upload_file(file_path):
    if os.path.exists(file_path) and is_valid_file(file_path):
        file_size_bytes = os.path.getsize(file_path)
        file_size_mb = int(file_size_bytes / (1024 * 1024))
        print(f"File '{file_path}' has been successfully uploaded. \nSize: {file_size_mb:.2f} MB")
        
        # Add the file to the files_db dictionary with a None value for the dB level
        filename = os.path.basename(file_path)
        files_db[filename] = None
        
        return input("Enter S to submit, F to upload a different file, or M to go back to the main Menu: ").upper(), file_size_mb
    else:
        print("Invalid file. Please make sure the file exists and is a .wav or .mp3 file.")
        UploadPage()
    return None

def UploadHistory():
    print('Upload history:')
    print('| Filename | Average dB |')
    print('|----------|------------|')
    for filename, db_level in files_db.items():
        db_display = db_level if db_level is not None else "Pending"
        print(f'| {filename: <8} | {db_display: <10} |')


header = """\
|=======================================================================================|
|            Welcome to Doodity - the Decible Analyzer For Your Favorite Files          |
|              Press U to upload a file, H to view upload history, Q to quit            |
|=======================================================================================|
"""



def main():
    print(header)
    while True:
        UserInput = input("Please enter your choice (U/H/Q): ").upper()
        if UserInput == "U":
            UserInput, file_size_mb = UploadPage()  
            if UserInput == "S" and file_size_mb is not None:
                # Pass the file size to the Submitted function only if file_size_mb is not None
                Submitted(file_size_mb)  
            elif UserInput == "F":
                print("You pressed F")
                # Reset UserInput to continue the loop
                UserInput = ''
                UploadPage()
            elif UserInput == "M":
                print("Returning to main menu...")
                # Do nothing, the loop will continue
        elif UserInput == "H":
            UploadHistory()
        elif UserInput == "Q":
            print("Have a good day!")
            break
        else:
            print("Invalid input, please try again.")



if __name__ == "__main__":
    main()
