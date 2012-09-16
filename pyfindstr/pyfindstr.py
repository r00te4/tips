import os,sys,fileinput,string
def find_str(fname,seek):
	res_list=[]
	for line in fileinput.input(fname):
		if line.find(seek)!=-1:
			res='FilePath===>'+fname+'========LineNumber===>'+(str)(fileinput.lineno())+'\r\n'
			res_list.append(res)
	return res_list

def  walk_dir(dir,fileinfo,topdown=True,seek='mcl'):
	str_results=[]
	res_file=open(fileinfo,'w')
	for root,dirs,files  in os.walk(dir,topdown):	
		for name in files:
			filename=os.path.join(name)
			filepath=os.path.join(root,name)
			str_result=find_str(filepath,seek)
			str_results.append(' '.join(str_result))
	print str_results
	str_results='\n' .join(str_results)
	res_file.write(str_results)

#walk_dir('./','res.txt')
def main():
	inputdir=raw_input('Enter The Path You Are LookingUp:')
	resdir=raw_input('Enter Your Result File name:')
	walk_dir(inputdir,resdir)

if __name__=='__main__':
	main()


