#!/bin/bash

# The following script will export all accounts to an import script.
# this script should be run as zimbra user
# target for ZCS 8, single server deployment
# last update 2014-04-04
# ognjen.miletic@gmail.com
# original at http://www.3open.org/d/zimbra/export_accounts

# customize these to your needs
# work folder must be writable by zimbra
work_folder=/tmp
import_script=${work_folder}/accounts-import.sh
brojac=0
# reset files:
echo "Criando arquivo vazio ${import_script}";
echo  '' > ${import_script}
echo "Exportando lista de usuarios...";
# get all account to $accounts
accounts=`zmprov -l gaa | egrep -v 'admin|wiki|galsync|spam|ham|virus|stimpson'`;
echo "Quase...";
echo "Criando script de importação...";
# loop for each account
for account in ${accounts}; do
  echo "${brojac}: exportando conta ${account} ..."
  dn=`zmprov -l ga ${account} displayName | grep displayName | sed 's/displayName: //'`;
  up=`zmprov -l ga ${account} userPassword | grep userPassword | sed 's/userPassword: //'`;
  
  # generate import script
  echo "Adicionando no script para importar..."
  echo "echo 'Importando ${account}'" >> ${import_script} 
  echo "zmprov ca ${account} ${up} displayName '${dn}'" >> ${import_script}
  echo "zmprov ma ${account} userPassword '${up}'" >> ${import_script}
  # add blank line separator
  echo '' >>  ${import_script}
  let brojac=brojac+1    
done

echo "Exportacao concluida.";
echo "Script de importacao está no caminho ${import_script}";
echo "Copie para um novo servidor e execute";
