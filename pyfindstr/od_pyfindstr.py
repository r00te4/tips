import os,sys,fileinput
def listyourdir(level,path):
	for i in os.listdir(path):
		print ' *' *(level+1) +i
		if os.path.isdir(path+'\\'+i):
			listyourdir(level+4,path+'\\'+i)

rootpath=os.path.abspath('.')
print rootpath

#listyourdir(4,rootpath)


def ftw(root=os.getcwd(),patterns='*'):
	pattern_list=patterns.split(';')
	for (path,dirs,files) in os.walk(root):
		for name in files:
			fullname=os.path.join(path,name)
			for pattern in pattern_list:
				if fnmatch.fnmatch(name,pattern):
					yield fullname
#print " a new method"
#ftw()
def find_str(fname,seek):
	res_list=[]
	for line in fileinput.input(fname):
		if line.find(seek)!=-1:
			#print fileinput.lineno(),fname
			res='FilePath===>'+fname+'========LineNumber===>'+(str)(fileinput.lineno())
			res_list.append(res)
	#print res_list
	print res_list

def  walk_dir(dir,fileinfo,topdown=True,seek='mcl'):
	for root,dirs,files  in os.walk(dir,topdown):
		for name in files:
			#print(os.path.join(name))
			#fileinfo.write(os.path.join(root,name)+'\n')
			filename=os.path.join(name)
			print filename
			filepath=os.path.join(root,name)
			find_str(filepath,seek)
			#file=open(filepath,"r")
			#print file.readline()
		#for name in dirs:
			#print (os.path.join(name))
			#fileinfo.write(' * ' + os.path.join(root,name) + '\n')
fileinfo=open('list.txt','w')
walk_dir('./',fileinfo)
filedata=open('aa.txt','r')
def o_find_str(data):
	seek='mcl'
	for line in fileinput.input(data):
		if line.find(seek) !=-1:
			print fileinput.lineno()
	#print data.read()
	
	#return seek in data.read()
	#data=data.readlines()
	# you can find line_no with out fileinput
	"""
	line_no=1
	for line in data:
		print line
		if not line.find(seek)==-1:
			print line_no
		line_no +=1
	"""


#res=find_str('aa.txt','mcl')
#res=find_str(filedata)
#print res
	