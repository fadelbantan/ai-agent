import os, subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:    
        result = subprocess.run(args=["python3", abs_file_path] + args, timeout=30, capture_output=True, cwd=working_directory)
        
        final_output = ""
        decoded_stdout = result.stdout.decode('utf-8').strip()
        decoded_stderr = result.stderr.decode('utf-8').strip()
        
        if decoded_stdout: # This checks if the string is not empty
            final_output += f"STDOUT: {decoded_stdout}"
        if decoded_stderr:
            if final_output: # If stdout was added, add a newline first
                final_output += "\n"
            final_output += f"STDERR: {decoded_stderr}"

        if result.returncode != 0:
            if final_output: # If stdout or stderr was added, add a newline first
                final_output += "\n"
            final_output += f"Process exited with code {result.returncode}"
        if not final_output: # If after all that, final_output is still empty
            return "No output produced."
        return final_output
    except Exception as e:
        return f"Error: executing Python file: {e}"
