#!/usr/bin/env python
# -*- coding: utf-8 -*-
### BEGIN INIT INFO
# Provides:             daemon-python
# Required-Start:       $network
# Required-Stop:        $network
# Default-Start:        3 4 5
# Default-Stop:         0 1 2
# Short-Description:    Daemon Python
### END INIT INFO

import os, time
import sys

def createDaemon():

	if len(sys.argv) > 1:
		if sys.argv[1] == "start":
			start()

		elif sys.argv[1] == "stop":
			stop()

		elif sys.argv[1] == "restart":
			stop()
			time.sleep(1)
			start()
		else:
			print "Usage: daemon-python.py {start|stop|restart}"
	else:
		print "Usage: daemon-python.py {start|stop|restart}"



def doTask():

	while True:

		try:
			os.system('MeuSoftware.py')
	 	except:
			print "Problemas hein..."

def pidfork(pid):

	file = open('/var/run/MeuSoftware.pid', "w+")
	file.flush()

	print >> file, str(pid)

	file.close()

	os.system('for i in `ps aux|grep MeuSoftware|grep -v grep|awk \'{print $2}\'`;do echo $i >> /var/run/MeuSoftware.pid;done')

def start():

	pid = os.fork()

	try:
		if pid > 0:

			pidfork(pid)
			print "Starting the MeuSoftware with PID: %s" % pid
			os._exit(0)

	except OSError, error:

		print 'Unable to fork. Error: %d (%s)' % (error.errno, error.strerror)
		os._exit(1)

	doTask()

def stop():

	try:
		file = open('/var/run/MeuSoftware.pid')

		pid = file.read().split('\n')
		print "Stopping the MeuSoftware"
		pipe = os.popen('ps aux|grep -v grep|grep bot|wc -l')
		output = int(pipe.read())

		if output > 0:
			for pids in pid:
				if pids is not "":
					pids = int(pids)
					os.kill(pids, 9)
			file.flush()
			file.close()

	except OSError, e:
		if e.errno == 3:
			print "Nao esta rodando"

if __name__ == '__main__':
	# Create the Daemon
	createDaemon()
