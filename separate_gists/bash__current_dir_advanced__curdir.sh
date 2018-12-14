

##################################################################################################
# description:  bash: current dir advanced
# raw_url:      https://gist.githubusercontent.com/mrkafk/aa07a5fd683dea6b661f/raw/44edd370bc0f6501ce848f7fa76a3128a65e1d8c/curdir.sh
# filename:     curdir.sh


#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPTDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"


                