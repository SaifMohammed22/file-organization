import os
import shutil

#Declaring the folder path that contains all the files 
file_directory = "C:/Users/saifm/Desktop/demo"
#Making the wanted directories
notebook_directory = "C:/Users/saifm/Desktop/demo/JupyterNotebook files"
os.makedirs(notebook_directory)
#----------------------------------------------------------------
data_directory = "C:/Users/saifm/Desktop/demo/CSV & Exel files"
os.makedirs(data_directory)
#----------------------------------------------------------------
python_directory = "C:/Users/saifm/Desktop/demo/Python files"
os.makedirs(python_directory)
#----------------------------------------------------------------
text_directory = "C:/Users/saifm/Desktop/demo/Text files"
os.makedirs(text_directory)
#----------------------------------------------------------------
other_directory = "C:/Users/saifm/Desktop/demo/Other files"
os.makedirs(other_directory)

#Looping through each file in our directory
for file_name in os.listdir(file_directory):
    file_path = os.path.join(file_directory, file_name)

    #Checking if the file is a file or a directory
    if os.path.isfile(file_path):
        #Get the file extension
        file_extensions = os.path.splitext(file_name)[1]

        if file_extensions == ".ipynb":
            try:
                shutil.move(file_path, notebook_directory)
                print(f"Notebook moved successfully to {notebook_directory}")
                print("*" * 30)
            except Exception as e:
                print(f"Error: {e}")
                print("*" * 30)


        elif file_extensions in ['.csv', '.xlsx'] :
            try:
                shutil.move(file_path, data_directory)
                print(f"CSV file moved successfully to {data_directory}")
                print("*" * 30)
            except Exception as e:
                print(f"Error: {e}")
                print("*" * 30)

        elif file_extensions == ".py":
            try:
                shutil.move(file_path, python_directory)
                print(f"Python file moved successfully to {python_directory}")
                print("*" * 30)
            except Exception as e:
                print(f"Error: {e}")
                print("*" * 30)

        elif file_extensions == ".txt":
            try:
                shutil.move(file_path, text_directory)
                print(f"Text file moved successfully to {text_directory}")
                print("*" * 30)
            except Exception as e:
                print(f"Error: {e}")
                print("*" * 30)
        else:
            try:
                shutil.move(file_path, other_directory)
                print(f"Other file moved successfully to {other_directory}")
                print("*" * 30)
            except Exception as e:
                print(f"Error: {e}")
                print("*" * 30)

    

