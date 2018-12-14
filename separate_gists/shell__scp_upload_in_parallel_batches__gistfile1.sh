

##################################################################################################
# description:  shell: scp upload in parallel batches
# raw_url:      https://gist.githubusercontent.com/mrkafk/3389ef792d855ee38ea9/raw/4703c6b9968530145533ab5dc40e2c26d8e51b34/gistfile1.sh
# filename:     gistfile1.sh


FLIST=file_paths_list.txt

COUNTER=0
PIDS=()

cat ${FLIST} | while read F; do
                COUNTER=$((COUNTER + 1))
                echo COUNTER $COUNTER
                sleep 1
                scp ${F} root@host:/data/tmp &
                PID=$!
                echo Adding PID $PID
                PIDS+=($PID)
                if [ $COUNTER -lt 20 ]; then
                        continue
                fi
                # wait for uploads batch to complete
                for PID in ${PIDS[@]}; do
                        echo waiting for PID $PID
                        wait $PID
                done
                # reset PIDS array
                PIDS=()
                COUNTER=0
done


                