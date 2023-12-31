#!/bin/sh
vmname="asa1"
vmid=$(vim-cmd vmsvc/getallvms | grep "$vmname" | awk '{print $1}')
stat1=$(vim-cmd vmsvc/power.getstate "$vmid" | grep "on")
if [ "$stat1" == "Powered on" ]
then
 vim-cmd vmsvc/power.off "$vmid"
fi
