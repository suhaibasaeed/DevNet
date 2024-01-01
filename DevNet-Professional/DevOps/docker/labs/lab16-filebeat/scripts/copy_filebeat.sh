#! /bin/sh
for i in 1 2 3
do
  echo "Command: scp /temp/filebeat-7.4.2-amd64.deb student@k8s$i:/tmp/filebeat-7.4.2-amd64.deb"
  scp /tmp/filebeat-7.4.2-amd64.deb student@k8s$i:/tmp/filebeat-7.4.2-amd64.deb
done
