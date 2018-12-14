#!/usr/bin/env python3

import requests
import codecs
import string

from config import USERNAME, API_TOKEN


import os
pyfile_top_dir = os.path.dirname(os.path.abspath(__file__))


filename_chars = string.ascii_letters + string.digits + '_.'

def sane_filename(fname):
    return ''.join([c if c in filename_chars else '_' for c in fname])


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


def get_user_pub_gists(username):
    req = requests.get('https://api.github.com/users/{}/gists'.format(username))
    gists = req.json()
    purge_files_in_folder(os.sep.join([pyfile_top_dir, 'separate_gists']))
    fcnt = 0
    with codecs.open('public_gists.txt', mode='wb', encoding='utf-8', errors='replace') as fo:
        for g in gists:
            description = g['description']
            files = g['files']
            for f in files.values():
                fname = f['filename']
                raw_url = f['raw_url']
                cnt = requests.get(raw_url)
                print('fname', fname, 'raw_url', raw_url)
                s = '''

##################################################################################################
# description:  {}
# raw_url:      {}
# filename:     {}


{}

                '''.format(description, raw_url, fname, cnt.text)
                fo.write(s)
                sep_gist = sane_filename(description) + '__' + fname
                p = os.sep.join([pyfile_top_dir, 'separate_gists', sep_gist])
                with codecs.open(p, mode='wb', encoding='utf-8', errors='replace') as sgfo:
                    sgfo.write(s)
                    fcnt += 1
                # from IPython import embed
                # embed()
        print(f'Wrote {fcnt} gists files')


def flow():
    '''Mission Control.'''
    get_user_pub_gists(USERNAME)


if __name__ == '__main__':
    flow()
