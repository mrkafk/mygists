

##################################################################################################
# description:  shell, bash: dir of executing script
# raw_url:      https://gist.githubusercontent.com/mrkafk/86f17dbdba71966637b7/raw/27226e36d1be8a2768b5d1d57102a47e7b499fc1/gistfile1.sh
# filename:     gistfile1.sh


CURD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$CURD"


                