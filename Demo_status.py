import socket
from contextlib import closing
import subprocess

def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print("Port is open")
        else:
            print("Port is not open")

def simulator_status():
	process = subprocess.Popen("ssh -i ~/.ssh/demo.pem creditcard-1.field.hortonworks.com ps -aux | grep Simulator",
	 shell = True, stdout=subprocess.PIPE, stderr= subprocess.STDOUT)
	output,stderr = process.communicate()
	status = process.poll()
	print(output)
	if len(output) > 3:
		print("Simulator is running -- If no demo is scheduled exit shutdown procedure")
	else:
		print("Simulator is not running.")

def river_status():
	host_0 		= 'river0.field.hortonworks.com'
	host_8 	= 'river8.field.hortonworks.com'
	ambari_port 	= 8080
	registry_port 	= 7788
	superset_port 	= 9088
	nifi_port 		= 9090
	print("Checking River Ambari Port")
	check_socket(host_0, ambari_port)
	print("Checking River Registry Port")
	check_socket(host_0, registry_port)
	print("Checking River Superset Port")
	check_socket(host_8, superset_port)
	print("Checking River Nifi Port")
	check_socket(host_8, nifi_port)

def creditcard_status():
	host_1 = 'creditcard-1.field.hortonworks.com'
	host_2 = 'creditcard-2.field.hortonworks.com'
	nifi_port 		= 9090
	registry_port 	= 7788
	ui_port 		= 8098
	# add functionality to see if simulator script is running
	# check for running process /root/CreditCardTransactionSimulator with ps -aux | grep
	print("Checking CC NiFi Port")
	check_socket(host_1, nifi_port)
	print("Checking CC Registry Port")
	check_socket(host_1, registry_port)
	print("Checking UI Port")
	check_socket(host_1, ui_port)

def lake_status():
	host_1 = 'lake1.field.hortonworks.com'
	host_9 = 'lake9.field.hortonworks.com'
	host_4 = 'lake4.field.hortonworks.com'
	host_8 = 'lake8.field.hortonworks.com'
	ambari_port		= 8080
	nifi_port 		= 9090
	registry_port 	= 7788
	superset_port	= 9088
	print("Checking Lake Ambari Status")
	check_socket(host_1, ambari_port)
	print("Checking Lake NiFi Status")
	check_socket(host_9, nifi_port)
	print("Checking Lake Registry Status")
	check_socket(host_8, registry_port)
	print("Checking Lake Superset Port")
	check_socket(host_4, superset_port)

def nifi_twitter_status():
	host_1 = 'twitterdemo7.field.hortonworks.com'
	banana_port = 8983
	nifi_port = 8080
	print("Checking Nifi Twitter Banana Status")
	check_socket(host_1, banana_port)
	print("Checking Nifi Twitter Nifi Status")
	check_socket(host_1, nifi_port)

if __name__ == "__main__":
	river_status()
	creditcard_status()
	lake_status()
	nifi_twitter_status()
	simulator_status()
