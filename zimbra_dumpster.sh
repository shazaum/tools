#!/bin/bash
#
# Na falta de espaço, sempre é bom limpar....
# Uma alternativa para nao apagar tudo, é selecionar um periodo... (Esse processo é mais demorado.)

# In lack of space, it is always good to clean ...
# An alternative to not delete everything, is to select a period ... (This process is more time consuming.)
#
#for i in `zmprov -l gaa`
#do
#	echo "Erase dumpster - $i"
#	IDstrash=`zmmailbox -z -m $i s --dumpster -t message -l 100 "in:trash before:-20days"|grep mess|awk '{print $2}'`
#	for ids in $IDstrash
#	do
#		zmmailbox -z -m $i emptyDumpster
#	done
#done


Log=/var/log/clean-trashs-mail.log

for i in `zmprov -l gaa`
do
	#echo "Erase dumpster - $i" >> $Log
	echo "Erase dumpster - $i"
	zmmailbox -z -m $i emptyDumpster
done