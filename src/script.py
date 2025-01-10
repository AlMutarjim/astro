import os

def read_and_format_text_files(root_dir, script_filename):
    """
    Reads all text files in a directory recursively (excluding the script itself) 
    and formats their contents for output.

    Args:
        root_dir: The root directory to search.
        script_filename: The name of the script file to exclude.

    Returns:
        A formatted string containing the contents of all text files.
    """

    output = ""
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == script_filename:
                continue  # Skip the script file itself

            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Format the output
                relative_path = os.path.relpath(filepath, root_dir)
                output += f"/{relative_path}:\n"  # Use relative path from root
                output += "```\n"
                output += content + "\n"
                output += "```\n\n"
            except UnicodeDecodeError:
                print(f"Skipping non-text file (likely binary): {filepath}")
            except Exception as e:
                print(f"Error processing file {filepath}: {e}")

    return output

if __name__ == "__main__":
    script_filename = "script.py"  # Or get the actual script name using os.path.basename(__file__)
    output_string = read_and_format_text_files("C:/Users/Siddiq/Documents/Gitlab/astrotest/tutorial/src/", script_filename)
    print(output_string)