#!/usr/bin/python
#
#   Author: Shazaum (Renato dos Santos)
#   Mail:   shazaum@gmail.com
#
# The example is specific to Active Directory

ldapserver="IP_SERVER"          #ldap server
port="389"                      #ldap port (389 default)
ldapbind="YOUR_USER"
ldappassword="YOUR_PASS"

#base="dc=company,dc=com"
base="OU=Perfis Gerenciados,DC=company,DC=com"
scope = ldap.SCOPE_SUBTREE

#--------------------------------------------------------------------------------------------------
import ldap, string, os, time, sys 

def my_search(l, keyword):


    #filter = "cn=" + "*" + keyword + "*" #caso queria filtrar por parte de nome
    filter = "ObjectCategory=user"
    retrieve_attributes = None
    count = 0
    result_set = []
    timeout = 0
    email = []
    try:
            result_id = l.search(base, scope, filter, retrieve_attributes)
            
            while 1:

                  result_type, result_data = l.result(result_id, timeout)
                                    
                  if (result_data == []):
                      break
                  else:
                      if result_type == ldap.RES_SEARCH_ENTRY:
                            result_set.append(result_data)
            if len(result_set) == 0:
              print "Null"
              return 
            for i in range(len(result_set)):
                for entry in result_set[i]:                 
                    try:
                        name = entry[1]['cn'][0]
                        user = entry[1]['sAMAccountName'][0]
                        if 'mail' in entry[1]:
                            email = entry[1]['mail'][0]
                        else:
                            email = "Null"
                        count = count + 1
                        print "---"
                        print "%d.\nName: %s\nUser: %s\nE-mail: %s" % (count, name, user, email)
                    except:
                        pass
    except ldap.LDAPError, error_message:
        print "Error :"
        print error_message
try:
    l=ldap.open(ldapserver)
    l.simple_bind_s(ldapbind,ldappassword)

    keyword="Paulo"
    
    print "Procurando..\n"
    my_search(l, keyword)

except ldap.LDAPError, error_message:
    print error_message
    print "Problemas para conectar. %s " % error_message