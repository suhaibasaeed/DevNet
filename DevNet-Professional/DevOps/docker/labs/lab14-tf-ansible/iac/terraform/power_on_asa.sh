#!/bin/sh
vmname="asa1"
vmid=$(vim-cmd vmsvc/getallvms | grep "$vmname" | awk '{print $1}')
stat1=$(vim-cmd vmsvc/power.getstate "$vmid" | grep "off")
if [ "$stat1" == "Powered off" ]
then
 vim-cmd vmsvc/power.on "$vmid"
fi
