import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'    
    
    try:
        if not os.path.exists(abs_file_path):
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
            with open(abs_file_path, "w") as f:
                f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        Exception("Error: Cannot create file.")

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write files, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    )
)