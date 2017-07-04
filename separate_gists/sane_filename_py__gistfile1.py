

##################################################################################################
# description:  sane filename py
# raw_url:      https://gist.githubusercontent.com/mrkafk/18e8edf66578aee8e659c6c18511d3f5/raw/d543b6a3e17620198a2b2fa0d197a89aaf699b9e/gistfile1.py
# filename:     gistfile1.py


filename_chars = string.ascii_letters + string.digits + '_.'

def sane_filename(fname):
    return ''.join([c if c in filename_chars else '_' for c in fname])



