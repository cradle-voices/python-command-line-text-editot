import sys
# we are trying to get the value from the command line 
def handle_list(command, lines):
   
    # start = int(command[1])
    # end   = start + 10
    command_line = command.split()
    start        = one_to_zero(int(command_line[1]))
    end          = start + 10
    # adding some sanity 
    if start < 0:
        start = 0
    if end > len(lines):
        end = len(lines)
    # print(lines[int(origin):])
    # loop throug it 
    for i in range(start, end):
        print(f"{i}: {lines[i]}", end="")

def handle_edit(command, lines):
    command_line        = command.split()
    line_number         = one_to_zero(int(command_line[1]))
    if line_number < 0 or line_number > len(lines):
        print("no such line ")
        return 
    lines[line_number] = input()+"\n"


def handle_apend(command, lines):
    command_line        = command.split()
    line_number         = one_to_zero(int(command_line[1]))
    if line_number < 0 or line_number > len(lines):
        return 
    new_line = input()
    lines.insert(line_number,new_line+"\n")

def handle_write(command, lines, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)



def handle_delete(command, lines):
    # get the line numbr to delete 
    command_line = command.split()
    line_number         = one_to_zero(int(command_line[1]))
    # check if the line number exists in our list 
    if line_number < 0 or line_number > len(lines):
        print("no such line ")
        return 
    # delete the line 
    lines.pop(line_number)

def one_to_zero(number):
    """ converts a number from a 1-based index to 0-bases index"""
    return number -1 

def user_input(lines):
    """ this function keep on acceptign the user input from the termina """
    done  = False
    while not done:
        command = input("> ").strip()

        if command[0] == 'q':
            done = True
        elif command[0] =='l':
            handle_list(command, lines)
        elif command[0] =='d':
            handle_delete(command, lines)
        elif command[0] =='e':
            handle_edit(command, lines)
        elif command[0] =='a':
            handle_apend(command, lines)
        elif command[0] =='w':
            handle_write(command, lines, filename)
        elif command == '':
            continue
        else: 
            print("unkown command ")
def read_file(filename):
    """ this function reads a file and converts the items into a list """
    # initialize a empty list 
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)

    return lines

if len(sys.argv) ==2:
    filename = sys.argv[1]
    
elif len(sys.argv) == 1: #no file name given just the script invoked 
    filename = None
else:
    print("usage tr.py [filename]", file=sys.stderr)
    sys.exit

if filename is not None:
    lines    = read_file(filename)
    user_input(lines)
else:
    lines  = []
# print(lines)