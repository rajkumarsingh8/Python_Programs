import os

file_dir = r"C:\Users\kumar\Downloads\Python_VS_Code\Assignment_1_BasicPythonConcepts\Assignment_4_FilesExceptionsAndErrors\output.txt"
file_name = os.path.basename(file_dir)

# Step 1: Write initial content (overwrites if file exists)
with open(file_dir, "wt") as fh:
    write_content = input("Enter text to write to the file: ")
    fh.write(write_content + "\n")
    print(f"Data successfully writen to {file_name}.")


# Step 2: append new content (preserves existing data)
with open(file_dir, "at") as fh:
    append_content = input("Enter addition text to append: ")
    fh.write(append_content + "\n")
    print("Data successfully appended.")


# Step 3: read the final content of the file
with open(file_dir, "rt") as fh:
    final_content = fh.read()
    print(f"Final content of {file_name}:")
    print(final_content)
