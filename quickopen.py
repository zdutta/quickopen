import webbrowser

#webbrowser.get('firefox').open_new_tab('http://www.google.com')
websites = open("websites.txt","r")
#print websites.readline()
for line in websites.readlines():
	webbrowser.get('firefox').open_new_tab(line)
task = raw_input()

