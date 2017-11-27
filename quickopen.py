import webbrowser
import sys
import os
# #webbrowser.get('firefox').open_new_tab('http://www.google.com')
# websites = open("websites.txt","r")
# #print websites.readline()
# for line in websites.readlines():
# 	webbrowser.get('firefox').open_new_tab(line)
# task = raw_input()


websites={} #dictionary

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

def removeGroup(groupName):
	os.remove(("websites/{}.txt").format(groupName))


while(1):
	print "Enter a command:"
	command = raw_input()
	if(command[0:9] == "add group"):
		addGroup(command[10:])
		print command[10:] + " added"
	elif(command[0:6] == "add to"):
		group = command[7:]
		print "Enter link to add to " + group
		newLink = raw_input()
		addToGroup(group,newLink)
		print newLink + " added to " + group
	elif(command[0:4] == "open"):
		group = command[5:]
		openGroup(group)
		print group + " opened"
	elif( command[:12] == "remove group"):
		group = command[13:]
		removeGroup(group)
		print group + " removed"
	elif(command == "end"):
		print "application ended"
		break
	else:
		print "Invalid command"

