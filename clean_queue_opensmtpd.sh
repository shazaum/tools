#!/bin/sh
# version 1.0

#Limpar queue...
domains='gmail.com.br
lokelokicom.com
wsync.com.br
homail.com
hotmail.co
homail.com
hormail.com
htomail.com
hotail.com
hotamil.com
hotmaic.com
hotmaiil.com
hotsail.com
hptmail.com
hotamil.com
hotamail.com
hotmaill.com
hotmial.com
homtail.com
homail.com
hormail.com
hotmal.com
hortmail.com
HOTMAL.COM
hotmaail.com
ihotmail.com
25hotmail.com
91hotmail.com
outlok.com
outloock.com
xxx.com
xsmile.com.br
gmail.com.br
gmav.com
gamail.com
gmaiil.com
gmial.com
igmail.com
nikashopp.com.br
bool.com.br
mkxt.com
naotem.com
n.com
publiccloud.com.br
embratelcloud.com.br
producoesvsrevolucao.com.br
autlook.com
www-data
yahool.com.br
yhaoo.com.br
yahho.com
teste.com
teste.com.br
bo.com.br
'

#esta opcao pode ser um pouco lenta

for domainlist in $domains
	do

		queue=`smtpctl show queue|grep pending|grep $domainlist |cut -d"|" -f1`
		echo "Emails restantes para limpar: $count"
		echo "Removendo $domainlist"
		for queuelistID in $queue
			do
				smtpctl remove $queuelistID
			done
	done

queueNoDomain=`smtpctl show queue||grep -E "(No MX found for domain|4\.2\.1|Network error on destination MXs|Temporary failure in MX lookup|Bad response: non-printable character in reply|User unknown in local recipient table|User doesn't exist)" |cut -d"|" -f1`

for queuelistID in $queueNoDomain
	do
		count=`smtpctl show queue|grep pending|wc -l`
		echo "Emails restantes para limpar: $count"
		smtpctl remove $queuelistID
	done
