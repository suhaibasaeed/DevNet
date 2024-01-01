#! /bin/sh
for i in 1 2 3 4
do
  echo "Command: sshpass -p "badpass"  ssh notauser@k8s1"
  sshpass -p "badpass" ssh notauser@k8s1
  echo "Command: sshpass -p "badpass"  ssh notauser@k8s2"
  sshpass -p "badpass" ssh notauser@k8s2
  echo "Command: sshpass -p "badpass"  ssh notauser@k8s3"
  sshpass -p "badpass" ssh notauser@k8s3
done
