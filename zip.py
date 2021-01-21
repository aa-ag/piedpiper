###--- IMPORTS --###
from zipfile import ZipFile
import settings
import os
from os.path import basename

###--- GLOBAL VARIABLES ---###
path = settings.PATH


###--- FUNCTIONS ---###
def zip_all_files_in_path():
    '''
     creates zip file using `ZipFile` object,
     then writes each file in the path to it
    '''
    global path

    # create zip file
    with ZipFile('zip_file.zip', 'w') as zf:
        # Iterate over all the files in directory
        for folders, subfolders, filenames in os.walk(path):
            for filename in filenames:
                # create complete filepath of file in directory
                file_path = os.path.join(folders, filename)
                # add file to zip
                zf.write(file_path, basename(file_path))

    # close zip file
    zf.close()


###--- DRIVER CODE ---##
if __name__ == "__main__":
    zip_all_files_in_path()
