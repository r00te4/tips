import os
import sys
from shutil import copy
def hostbak ():
	hostbak_path= 'C:\\WINDOWS\\system32\\drivers\\etc\\hosts.bak'
	host_path='C:\\WINDOWS\\system32\\drivers\\etc\\hosts'
	copy(host_path,hostbak_path)
	print "Hosts File BackupED!"
def getRights ():
	os.system('cacls c:\windows\system32\drivers\etc\hosts /grant Everyone:F')
	print "Get the Rights"
def hostattach(hostlist):
	host_path='C:\\WINDOWS\\system32\\drivers\\etc\\hosts'
	host_file=open(host_path,'a+')	
	

	try:

	    host_file.writelines(hostlist)
	    print "New Hosts AttachED!"

	finally:

	    host_file.close()
	
if __name__ == "__main__":
    hostlist = ["127.0.0.1 www.google.com"]
    getRights()
    hostbak()
    hostattach(hostlist)

