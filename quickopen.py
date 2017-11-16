import webbrowser

# #webbrowser.get('firefox').open_new_tab('http://www.google.com')
# websites = open("websites.txt","r")
# #print websites.readline()
# for line in websites.readlines():
# 	webbrowser.get('firefox').open_new_tab(line)
# task = raw_input()

websites={}

def addGroup(groupName):
	websites[groupName] = []

def addToGroup(groupName,link):
	websites[groupName].append(link)

def open(groupName):
	for site in websites[groupName]:
		webbrowser.get('firefox').open_new_tab(site)


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
		open(group)
	elif(command == "end"):
		break

