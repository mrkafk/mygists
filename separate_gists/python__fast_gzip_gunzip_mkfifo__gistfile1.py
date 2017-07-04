

##################################################################################################
# description:  python: fast gzip gunzip mkfifo
# raw_url:      https://gist.githubusercontent.com/mrkafk/3c6eab5ca112e45d0781/raw/19079da75b8a50bc60225db2b2ab656c443c10db/gistfile1.py
# filename:     gistfile1.py



#http://www.code-corner.de/?p=153

    import os
    import subprocess

    tmp_fifo = "tmp_fifo"

    os.mkfifo(tmp_fifo)

    p = subprocess.Popen("gzip --stdout -d traj.pdb.gz > %s" % tmp_fifo, shell=True)
    f = io.open(tmp_fifo, "r")

    while True:
        line = f.readline()
        if not line: break

    f.close()
    p.wait()

    os.remove(tmp_fifo)


