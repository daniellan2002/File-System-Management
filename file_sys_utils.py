#Tianyi Lan 01/2021
import os
from pathlib import Path
from pathlib import PurePath
import shutil
import time



'''Part A Functions'''
def partA_run(files_considered:list):
    '''
        Runs the first part of the program to search for
        files under Consideration
    '''
    print('''
    Please type "R" for recursive search;

    or

    "D" for directory search, folowed by your preferred directory URL: \n''')

    #Takes Input
    user_input = input()

    #Validates Input
    valid = valid_input(user_input)
    while not valid:
        print('ERROR')
        user_input = input()

        valid = valid_input(user_input)
    #Parse Input
    directory_path = user_input.split(' ', 1)

    #Process Input to 'D' or 'R' Commands

    try:
        if directory_path[0] == 'D':
            files_considered.extend(directory_files(Path(directory_path[1])))
            print_d_files(directory_path[1])

        elif directory_path[0] == 'R':
            files_considered.extend(all_files(Path(directory_path[1])))
            print_all_files(directory_path[1])

    except OSError:
        pass
#------------------------------------------Main Run
def valid_input(user: str) -> bool:
    '''
        Return True if input is in the right format
        and the path is valid
        Else return False
    '''

    directory_path = user.split(' ', 1)

    commands = {'D':1, 'R':1}
    if not directory_path:
        #print('Empty')
        return False
    elif len(directory_path) == 1:
        return False
    elif directory_path[0] not in commands:
        #print('Letter Error')
        return False
    elif not os.path.isdir(directory_path[1]):
        #print('Not a directory')
        return False
    elif not os.path.exists(directory_path[1]):
        #print('Directory not exist')
        return False

    return True
#------------------------------------------Validates
def directory_files(directory_path: str):
    '''
        Given input MUST be a directory
        Used to find all files under one directory
        input: str (Path)
        output:list (files for consideration)
    '''
    files = []
    for elem in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path,elem)):
            files.append(os.path.join(directory_path,elem))

    return files
#------------------------------------------Directory
def all_files(directory_path: str):
    '''Returns all files given by Input'''

    files = []
    for elem in os.listdir(directory_path):
        if os.path.isdir(os.path.join(directory_path, elem)):
            files = files + all_files(os.path.join(directory_path, elem))
        else:
            files.append(os.path.join(directory_path, elem))
    return files
#------------------------------------------Recursive
def print_all_files(directory_path:str):
    '''
        Print all files under consideration by printing
        files from original directory first, and files
        from all other subdirectories
    '''

    files = []
    directories = []

    full_paths = os.listdir(directory_path)

    for elem in sorted(full_paths):
        if os.path.isdir(os.path.join(directory_path, elem)):
            directories.append(os.path.join(directory_path, elem))
        else:
            files.append(os.path.join(directory_path, elem))

    for n in sorted(files):
        print(n)

    for n in directories:
        print_all_files(n)
#------------------------------------------Print Recursive
def print_d_files(directory_path):
    '''
        Print only files from a directory specified
    '''
    files = []

    for elem in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path,elem)):
            files.append(os.path.join(directory_path,elem))
    for file in sorted(files):
        print(file)
#------------------------------------------Print Directory



'''Part B Functions'''

def partB_run(files_considered:list, interesting_files:list):
    '''
        Runs the second part of the program to search for
        files that are interesting
    '''

    print('''
    To further select your files, here are the options:

    Type the capitalized letter:

        "A" if you want to select all the files;


        "N" followed by a space and the name of the file if you wish to
        search the file by name;


        "E" followed by a dot or space and the name of the extension
        (E.py or E py)


        "T" followed by a string of texts you are looking for in a text file;
        (T hello or T Good Morning)


        "<" followed by the size of the file in bytes for any file that's less
        than the given size;


        ">" followed by the size of the file in bytes for any file that's greater
        than the given size;

    \n
    ''')
        
    user_input_B = input()

    valid = valid_input_B(user_input_B)

    while not valid:
        print('ERROR')

        user_input_B = input()

        valid = valid_input_B(user_input_B)

    directory_path = user_input_B.split(' ', 1)

    if directory_path[0] == 'A':
        interesting_files.extend(all_interesting_files(files_considered))
        print_A(interesting_files)

    elif directory_path[0] == 'N':
        interesting_files.extend(files_by_name(files_considered,directory_path[1]))
        print_A(interesting_files)

    elif directory_path[0] == 'E':
        interesting_files.extend(files_by_ext(files_considered,directory_path[1]))
        print_A(interesting_files)

    elif directory_path[0] == 'T':
        interesting_files.extend(files_by_text(files_considered,directory_path[1]))
        print_A(interesting_files)

    elif directory_path[0] == '<':
        interesting_files.extend(less_than(files_considered,directory_path[1]))
        print_A(interesting_files)

    elif directory_path[0] == '>':
        interesting_files.extend(greater_than(files_considered,directory_path[1]))
        print_A(interesting_files)

#------------------------------------------Main Run
def all_interesting_files(files_considered:list):
    '''
        Return all files in the files considered list
    '''
    return files_considered
#------------------------------------------All Files
def valid_input_B(user:str) -> bool:
    '''
        Checks whether the input is valid for part B
    '''
    if not user:
        return False

    allowed = {'T':1, 'N':1, 'E':1}
    if user.count(' ') > 1 and user[0] not in allowed: #Check if space counts as input
        return False

    directory_path = user.split(' ', 1)

    commands = {'N':1, 'E':1, 'T':1, '<':1, '>':1, 'A':1}

    if not directory_path:
        return False

    if len(directory_path) == 1:
        if user[0] != 'A':
            return False
        else:
            return True
    elif len(directory_path) == 2:
        if directory_path[0] not in commands:
            return False
        elif not directory_path[1]:
            return False
        elif directory_path[0] == 'A':
            return False
        elif directory_path[0] == 'E':
            if '.' in directory_path[1] and directory_path[1].count('.') > 1:
                return False
            elif '.' in directory_path[1] and directory_path[1].index('.') != 0:
                return False
            else:
                return True
        elif directory_path[0] == '<' and not directory_path[1].isdigit():
            return False
        elif directory_path[0] == '>' and not directory_path[1].isdigit():
            return False
        else:
            return True

    return False
#------------------------------------------Validates
def print_A(files:list):

    '''
        The print function for files, prints each file
        in order sorted by levels and ordinal values
    '''
    sorted_files = []


    counter = set()

    for file in (files):
        p = PurePath(file)
        counter.add(len(p.parts))

    counter = list(counter)
    counter = sorted(counter)

    for count in counter:

        storage = []

        for file in files:
            p = PurePath(file)
            if len(p.parts) == count:
                storage.append(file)

        sorted_files.append(storage)

    for group in sorted_files:
        for file in sorted(group):
            print(file)
#------------------------------------------Print Files
def files_by_name(storage_files:list, name:str) -> list:
    '''
        Return files that matches the name given in the Input
        from the files considered list
    '''

    files = []

    for file in storage_files:
        if os.path.basename(file) == name:
            files.append(file)

    return files
#------------------------------------------Name Search
def files_by_ext(storage_files:list, ext:str) -> list:
    '''
        Takes a list of file paths, name of extension
        Return a list with files extensions matching the
        extension given in input
    '''

    files = []

    for file in storage_files:
        filename, file_extension = os.path.splitext(file)

        file_extension = file_extension.strip('.')
        ext = ext.strip('.')

        if file_extension == ext:
            files.append(file)

    return files
#------------------------------------------Extension Search
def files_by_text(storage_files: list, text:str) -> list:
    '''
        Takes list of files for consideration and a text query
        Return a list of files that contain the text query
    '''

    files = []

    for file in storage_files:

        f = None
        try:

            f = open(Path(file),'r', encoding = 'utf-8')
            lines = f.read()
        except OSError:
            continue
        except ValueError:
            continue
        else:
            if text in lines:
                files.append(file)
        finally:
            if f != None:
                f.close()
    return files
#------------------------------------------Text Search
def less_than(storage_files:list, threshhold:int) -> list:
    '''
        Takes a list of interesting files, and an integer as threshold
        Return a list of files whose size in bytes are smaller than threshold
    '''

    files = []

    for file in storage_files:
        if os.path.getsize(Path(file)) < int(threshhold):
            files.append(file)

    return files

    '''
    Need to check for FileNotFound error IF user deletes file during program
    '''
#------------------------------------------Size Search: Less
def greater_than(storage_files: list, threshold:int) -> list:
    '''
        Takes a list of interesting files, and an integer as threshold
        Return a list of files whose size in bytes are greater than threshold
    '''

    files = []

    for file in storage_files:
        if os.path.getsize(Path(file)) > int(threshold):
            files.append(file)

    return files

    '''
    Need to check for FileNotFound error IF user deletes file during program
    '''
#------------------------------------------Size Search: Greater




'''Part C Functions'''

def partC_run(interesting_files:list):

    '''
        Runs the third part of the program to take actions
        on the files that are interesting
    '''

    print('''
    Finally, type:

        "T", if you have selected a text file and wishes to print out its first line.

        (WARNING: If you have not selected any text file, the program will terminate)

        "D", if you wish to duplicate the files you have selected with an
        extension name ".dup";

        \n
        ''')
    
    user_input_C = input()

    valid = valid_input_C(user_input_C)

    while not valid:
        print("ERROR")

        user_input_C = input()

        valid = valid_input_C(user_input_C)

    if user_input_C == 'F':
        first_line(interesting_files)
    elif user_input_C == 'D':
        duplicate_file(interesting_files)
    elif user_input_C == 'T':
        change_time(interesting_files)
#------------------------------------------Main Run
def valid_input_C(user:str):
    '''
        Checks whether input is valid for part C
    '''

    if len(user) != 1:
        return False
    commands = {'F':1, 'D':1, 'T':1}

    if user not in commands:
        return False

    return True
#------------------------------------------Validates
def sort_C(files:list) -> list:
    '''
        Sorts the files in the list by depth
        and by lexicographic ordering
    '''

    sorted_files = []
    final_files = []

    counter = set()

    for file in (files):
        p = PurePath(file)
        counter.add(len(p.parts))

    counter = list(counter)
    counter = sorted(counter)

    for count in counter:

        storage = []

        for file in files:
            p = PurePath(file)
            if len(p.parts) == count:
                storage.append(file)

        sorted_files.append(storage)

    for group in sorted_files:
        for file in sorted(group):
            final_files.append(file)
    return final_files
#------------------------------------------Sorts the List
def first_line(files:list):
    '''
        Takes a list of files and print
        first line of text from the file it's a text file

        Else print NOT TEXT
    '''

    files = sort_C(files)

    for file in (files):

        f = None
        try:

            f = open(Path(file),'r', encoding = 'utf-8')
            lines = f.readlines()
        except OSError:
            print('NOT TEXT')
            continue
        except ValueError:
            print('NOT TEXT')
            continue
        else:
            if lines:
                print(lines[0].replace('\n', ''))
        finally:
            if f != None:
                f.close()
#------------------------------------------Print First Line
def duplicate_file(files:list):
    '''
        Make a duplicate copy of each file
        in the given list of files

        Stores the duplicate file in the same directory
        where the original resides

        appends ".dup" to the end of the file
    '''

    for file in files:

        dst = file + '.dup'
        try:
            shutil.copy(file, dst)
        except OSError:
            continue
#------------------------------------------Duplicate
def change_time(files:list):
    '''
        Take a list of files and modify the
        timestamp to the current date / time
    '''

    for file in files:
        # print(file)
        # print('Before change', time.ctime(os.path.getmtime(file)))
        try:
            os.utime(file, None)
        except OSError:
            #print("CANNOT BE OPENED")
            continue
#------------------------------------------Change Timestamp








