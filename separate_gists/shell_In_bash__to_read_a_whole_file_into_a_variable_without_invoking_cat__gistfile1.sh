

##################################################################################################
# description:  shell In bash, to read a whole file into a variable without invoking cat
# raw_url:      https://gist.githubusercontent.com/mrkafk/b12e8ff749d8dc04cf19/raw/9ef76a61c5a3fa0b85756559d932425b70c8ba52/gistfile1.sh
# filename:     gistfile1.sh


#!/bin/bash
value=$(<config.txt)
echo "$value"



