from file_sys_utils import *




def main_run():
    '''
        Runs all three parts of the program,
        partA_run
        partB_run
        partC_run
    '''
    interesting_files = []
    files_considered = []

    #Finds All Files for Consideration
    partA_run(files_considered)
    #Searches Files that are Interesting
    partB_run(files_considered, interesting_files)
    #Takes Actions on the Interesting Files
    partC_run(interesting_files)



if __name__ == '__main__':
    main_run()
