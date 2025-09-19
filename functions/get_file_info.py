import os
from google.genai import types
from .get_file_content import schema_get_file_content
from .run_python_file import schema_run_python_file
from .write_file import schema_write_file

def get_files_info(working_directory, directory='.'):
    abs_working_dir = os.path.abspath(working_directory) # Get absolute path of working directory
    target_dir = os.path.abspath(os.path.join(working_directory, directory))

    
    # Checking if info asked about (files/dirs) in working dir
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    # Checking if dir is dir
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        output_lines = []  # List to store info about each file/dir
        directory_list = os.listdir(target_dir)  # Get all items in the directory

        # For each item in the directory, gather its absolute path, check if it's
        # a directory, get its size, and format the info for output
        for i in directory_list:
            items = os.path.join(target_dir, i)
            dir_or_no = os.path.isdir(items)
            size = os.path.getsize(items)
            
            output_lines.append(f"- {i}: file_size={size} bytes, is_dir={dir_or_no}\n")
        
        # Return all info as a single string
        return "".join(output_lines)

    except:
        return "Error: Unable to retrieve directory contents"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)   