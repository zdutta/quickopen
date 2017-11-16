import webbrowser
import sys
# #webbrowser.get('firefox').open_new_tab('http://www.google.com')
# websites = open("websites.txt","r")
# #print websites.readline()
# for line in websites.readlines():
# 	webbrowser.get('firefox').open_new_tab(line)
# task = raw_input()


websites={}

def addGroup(groupName):
	# websites[groupName] = []
	file = open("websites/{}.txt".format(groupName),"w+")
	file.close()

def addToGroup(groupName,link):
	 # websites[groupName].append(link)
	 file = open("websites/{}.txt".format(groupName),"w")
	 file.write(link)
	 file.close()

def openGroup(groupName):
	 # for site in websites[groupName]:
	 # 	webbrowser.get('firefox').open_new_tab(site)
	 file = open("websites/{}.txt".format(groupName),"r")
	 
	 for line in file.readlines():
	 	webbrowser.get('firefox').open_new_tab(line)
	 file.close()




while(1):
	command = raw_input()
	if(command[0:9] == "add group"):
		addGroup(command[10:])
	elif(command[0:6] == "add to"):
		group = command[7:]
		newLink = raw_input()
		addToGroup(group,newLink)
	elif(command[0:4] == "open"):
		group = command[5:]
		openGroup(group)
	elif(command == "end"):
		break
	else:
		print "Invalid command"

