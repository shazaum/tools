#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import os, time
import requests
import urllib2
import sys
import logging

config = ConfigParser.ConfigParser()
config.read('/root/status.conf')

#Exemplos
apacheuser = config.get('server', 'apacheuser')
apachepassword = config.get('server', 'apachepassword')
token = config.get('server', 'token')
cachetserver = config.get('server', 'cachetserver')

pidfile = config.get('server', 'pidfile')
logfile = config.get('server', 'logfile')

sections = config.sections()

logging.basicConfig(filename=logfile,level=logging.INFO)

def createDaemon():

	if sys.argv[1] == "start":
		start()

	elif sys.argv[1] == "stop":
		stop()

	elif sys.argv[1] == "restart":
		stop()
		time.sleep(1)
		start()
	else:
		print "Options:"
		print "\tstart\n\tstop\n\trestart"


def doTask():

	while True:

		for context in config.sections():

			if context != "server":

				clientID = config.get(context, 'id')
				clientURL = config.get(context, 'url')

				url = "http://status.domain.com.br/api/v1/components/" + clientID
				headers = {'content-type' : 'application/json;', 'X-Cachet-Token' : token}

				#operacional
				op = '{\"status\":\"1\"}'

				#Problemas de performance
				pf = '{\"status\":\"2\"}'

				#Indisponibilidade parcial
				ip = '{\"status\":\"3\"}'

				#Indisponibilidade total
				it = '{\"status\":\"4\"}'
			
				logging.info(time.ctime())

				time.sleep(1)

				try:
					clientCode = urllib2.urlopen(clientURL)
					clientCodeReturn = str(clientCode.getcode())

					if clientCodeReturn == "200":
						
						logging.info(" LOG HERE " + context + ": " + clientCodeReturn)
					 	r = requests.put(url, headers=headers, data=op, auth=(apacheuser, apachepassword))
					else:
					 	logging.warning(" LOG HERE " + context + " error with code: " + clientCodeReturn)
					 	r = requests.put(url, headers=headers, data=it, auth=(apacheuser, apachepassword))

			 	except urllib2.HTTPError, e:
					logging.error('HTTPError = ' + str(e.code) + ' ' + clientURL)
					r = requests.put(url, headers=headers, data=it, auth=(apacheuser, apachepassword))
				except urllib2.URLError, e:
					logging.error('URLError = ' + str(e.reason) + ' ' + clientURL)
					r = requests.put(url, headers=headers, data=it, auth=(apacheuser, apachepassword))
				except httplib.HTTPException, e:
					logging.error('HTTPException = ' + clientURL)
					r = requests.put(url, headers=headers, data=it, auth=(apacheuser, apachepassword))

def pidfork(pid):

	file = open('/var/run/status.pid', "w+")
	file.flush()

	print >> file, str(pid)

	file.close()

def start():

	pid = os.fork()

	try:

		if pid > 0:

			pidfork(pid)
			print "Startng the monitor with PID: %s" % pid
			os._exit(0)

	except OSError, error:

		print 'Unable to fork. Error: %d (%s)' % (error.errno, error.strerror)
		os._exit(1)

	doTask()
  
def stop():

	file = open('/var/run/status.pid')

	pid = int(file.read().strip())
	print "Stopping the monitor"
	os.kill(pid, 9)


	file.flush()
	file.close()

if __name__ == '__main__':
	# Create the Daemon
	createDaemon()