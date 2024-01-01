#! /bin/sh
for i in 1 2 3
do
  echo "Command: scp /temp/meatricbeat-7.4.2-amd64.deb student@k8s$i:/tmp/metricbeat-7.4.2-amd64.deb"
  scp /tmp/metricbeat-7.4.2-amd64.deb student@k8s$i:/tmp/metricbeat-7.4.2-amd64.deb
done
