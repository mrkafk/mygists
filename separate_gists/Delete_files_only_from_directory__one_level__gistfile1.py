

##################################################################################################
# description:  Delete files only from directory, one level
# raw_url:      https://gist.githubusercontent.com/mrkafk/f533e7c8a91d423e31dbcffff52fbeab/raw/0c3831c82ebaa6d279d9409342a4d977370bedf2/gistfile1.py
# filename:     gistfile1.py


import os
import shutil

def purge_files_in_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


