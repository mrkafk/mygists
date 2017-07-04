

##################################################################################################
# description:  bash: current dir advanced
# raw_url:      https://gist.githubusercontent.com/mrkafk/aa07a5fd683dea6b661f/raw/4dea6148bdd714ae98095d10b2219c0d2bf17fd4/curdir.sh
# filename:     curdir.sh



# based on http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPTDIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"


