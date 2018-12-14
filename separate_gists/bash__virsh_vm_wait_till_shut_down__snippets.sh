

##################################################################################################
# description:  bash: virsh vm_wait_till_shut_down
# raw_url:      https://gist.githubusercontent.com/mrkafk/c9703a731d369bba9a15f2075ab58f45/raw/e13339a93b57e7955da886ef05d31851b689085d/snippets.sh
# filename:     snippets.sh


function vm_wait_till_shut_down () {
  for i in {1..600}; do
    STATE=$(virsh domstate "$1")
    if [ "$STATE" != "running" ]; then
      sleep 1
      return 0
    fi
    sleep 1
  done
  return 1
}


                