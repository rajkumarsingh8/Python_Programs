import os


file_dir = r"C:\Users\kumar\Downloads\Python_VS_Code\Assignment_1_BasicPythonConcepts\Assignment_4_FilesExceptionsAndErrors\sample.txt"
try:
    with open(file_dir,'rt') as fh:
        lines = fh.readlines()
        print("Reading the file content:")
        line_num = 1
        for line in lines:
            print(f"Line {line_num}: {line.strip('\n')}")
            line_num += 1
except FileNotFoundError:
    file_name = os.path.basename(file_dir)
    print(f"Error: The file {file_name} was not found.")