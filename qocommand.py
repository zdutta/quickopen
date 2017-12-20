#commandline tool implementation
import webbrowser
import sys
import os
import argparse

def addGroup(groupName):
	file = open("websites/{}.txt".format(groupName),"w+")
	file.close()

def addToGroup(groupName,link):
	 file = open("websites/{}.txt".format(groupName),"w")
	 file.write(link)
	 file.close()

def openGroup(groupName):
	 file = open("websites/{}.txt".format(groupName),"r")
	 
	 for line in file.readlines():
	 	webbrowser.get('firefox').open_new_tab(line)
	 file.close()

def removeGroup(groupName):
	os.remove(("websites/{}.txt").format(groupName))

def main():
	parser = argparse.ArgumentParser(description='Process requests to create groups and add links')
	parser.add_argument( '-ag',action='store_true', help='The group you would like to add')
	parser.add_argument('-atg', action='store_true', help='The link you would like to add to the specified group')
	parser.add_argument('-og', action='store_true', help='The group you would like to open')
	parser.add_argument('-rg', action='store_true', help='The group you would like to remove')
	parser.add_argument('args', nargs=argparse.REMAINDER)
	args = parser.parse_args()
	if args.ag:
		addGroup(args.args[0])
		print 'adding ' + args.args[0]
	elif args.atg:
		addToGroup(args.args[0],args.args[1])
		print "adding " + args.args[1] + " to " + args.args[0]
 	elif args.og:
		openGroup(args.args[0])
		print "opening " + args.args[0]
	elif args.rg:
		removeGroup(args.args[0])
		print "removing " + args.args[0]

if __name__ == '__main__':
	main()