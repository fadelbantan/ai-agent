import os

def get_files_info(working_directory, directory='.'):
    abs_working_dir = os.path.abspath(working_directory) # Get absolute path of working directory
    full_path = os.path.join(abs_working_dir, directory) # Join working dir and target dir
    abs_full_path = os.path.abspath(full_path) # Get absolute path of target dir
    
    # Checking if info asked about (files/dirs) in working dir
    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    # Checking if dir is dir
    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'
    
    output_lines = []  # List to store info about each file/dir
    try:
        directory_list = os.listdir(abs_full_path)  # Get all items in the directory

        # For each item in the directory, gather its absolute path, check if it's
        # a directory, get its size, and format the info for output
        for i in directory_list:
            items = os.path.join(abs_full_path, i)
            dir_or_no = os.path.isdir(items)
            size = os.path.getsize(items)
            
            output_lines.append(f"- {i}: file_size={size} bytes, is_dir={dir_or_no}\n")
        
        # Return all info as a single string
        return "".join(output_lines)

    except:
        return "Error: Unable to retrieve directory contents"
