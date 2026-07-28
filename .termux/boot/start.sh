#!/data/data/com.termux/files/usr/bin/bash

bash /data/data/com.termux/files/home/scripts/stop.sh
sleep 2
termux-wake-lock
runsvdir ~/sv &
