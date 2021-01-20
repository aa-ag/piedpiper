###--- IMPORTS --###
from zipfile import ZipFile
import settings


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
    zip_object = ZipFile('zip_file.zip', 'w')

    # add each file in path to zip file
    zip_object.write('.gitignore')
    zip_object.write('README.md')
    zip_object.write('settings.py')
    zip_object.write('zip.py')

    # close zip File
    zip_object.close()


###--- DRIVER CODE ---##
if __name__ == "__main__":
    zip_all_files_in_path()
