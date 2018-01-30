fp=open("macrolib.asm","r")

fp1=fp.readlines()
mac_array=[]
mac=[]
macdef=[]

mac_name=[]
mac_para=[]
macstart_index=[]
macend_index=[]

def check_macro(i,m1):
	macro_len=len(m1)
	m=[]
	for j in range(i,len(m1)):
		if('%endmacro' in m1[j]):
			m.append(m1[j])
			macdef.append(m)
		
			if(int(j)==int(macro_len-1)):			
				break			
			else:
				check_macro((j+1),mac)
			break	
		else:	
			m.append(m1[j])
	return macdef
	
for i in range(len(fp1)):
		fp1[i]=fp1[i].replace('\t','')
		fp1[i]=fp1[i].replace('\n','')
		mac_array.append(fp1[i])

for i in range(len(mac_array)):
	if('section' in mac_array[i]):	
		break
	else:
		if(mac_array[i] != ''):
			mac.append(mac_array[i])
mlen1=len(mac)
print "\n"+str(mac)

macdef=check_macro(0,mac)

print "\n"+str(macdef)

for i in range(len(macdef)):
	a=[]
	b=[]
	a=macdef[i]
	if('%macro' in a[0]):		
		b=a[0].split()
		macstart_index.append(mac.index(a[0]))

	mac_name.append(b[1])
	mac_para.append(b[2])

for i in range(len(mac)):
	if('%endmacro' in mac[i]):		
		macend_index.append(i)

#-----------------------------------------------MNT MDT WTRITE----------------------------------------------------------------------------------

f1=open("mnt.txt","w")
f2=open("mdt.txt","w")

print "\nMNT:-"

for i in range(0,len(mac_name)):
	f1.write("\n***********Macro Name Table*************")
	f1.write("\n MacroName\tMacroPara\tStartindex\tEndindex\n\n")
	f1.write("\n"+str(mac_name[i])+"\t\t"+str(mac_para[i])+"\t\t"+str(macstart_index[i])+"\t\t"+str(macend_index[i]))

print "\nMDT:-"

md=[]
macdd=[]
start=0
end=0

for i in range(0,len(macstart_index)):
	 md.append(mac[(macstart_index[i]+1):macend_index[i]])

for i in range(0,len(md)):
	macdd=md[i]
	start=macstart_index[i]
	end=macend_index[i]

	f2.write( "\n")

	for i in range(0,len(macdd)):
		if(i==0):
			f2.write("\------------Macro Defination Table------------")
			f2.write("\nMacrodefination\tStartindex\tEndindex\n\n")
			f2.write(macdd[i]+"\t"+str(start)+"\t\t"+str(end)+"\n")
		else:
			f2.write(macdd[i]+"\n")	 	

