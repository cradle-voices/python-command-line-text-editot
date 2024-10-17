# python-command-line-text-editot
Python command line text editor showing how to interact with files 

# Command Line Text Editor

This Python script provides a simple command-line interface for manipulating text files. Users can list, edit, append, delete, and save text lines from a file. 

## Requirements

- Python 3.x

## Usage

To run the script, use the following syntax in the terminal:

```bash
python editor.py [filename]
```

- `[filename]`: (Optional) The name of the file to be read and edited. If no file is provided, the script starts with an empty list of lines.

## Commands

Once the script is running, you can use the following commands to manipulate the text:

- **l [start]**: List 10 lines starting from the line number `[start]`.
- **e [line_number]**: Edit the line at `[line_number]`.
- **a [line_number]**: Append a new line after the specified `[line_number]`.
- **d [line_number]**: Delete the line at `[line_number]`.
- **w**: Write all changes back to the file.
- **q**: Quit the program.

## Example

```bash
> python tr.py example.txt
> l 1
0: First line
1: Second line
2: Third line
> e 2
> This is the updated third line.
> w
```

This command will edit the third line in `example.txt` and save the changes to the file.

## Notes

- Line numbers are based on 1-based indexing when using commands but are internally converted to 0-based indexing in the script.
- If you try to delete or edit a line that doesn't exist, the script will inform you that there is no such line.
