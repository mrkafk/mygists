#!/bin/bash -i -x

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPTDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

cd "$SCRIPTDIR"

. ve/bin/activate

./get_my_gists.py

date
git add .
git commit -m "gists on `date`"
export HOME=/Users/mark
PKEY=~/.ssh/id_rsa_gh git push

