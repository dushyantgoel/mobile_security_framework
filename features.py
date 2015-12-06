import subprocess

bashcommand="cat full_java_sourcecode.txt | grep -E -o 'http://.*' > Features/hardcoded_urls.txt  "
output = subprocess.check_output(['bash','-c', bashcommand])

bashcommand="cat Features/hardcoded_urls.txt | wc -l "
output = subprocess.check_output(['bash','-c', bashcommand])

#print "There are "+output.strip('\n')+" no of Hardcoded URL instances. They are as follows: \n"

bashcommand="cat Features/hardcoded_urls.txt"
#print bashcommand
output = subprocess.check_output(['bash','-c', bashcommand])
#print output

bashcommand="cat full_java_sourcecode.txt | grep -E -e '.*javax\.crypto.*' -e '.*sun\.misc.*' -e '.*java\.security.*' -e '.*crypto.*' > Features/encryption.txt"
#print bashcommand
output = subprocess.check_output(['bash','-c', bashcommand])
#print output

bashcommand="cat Features/encryption.txt | wc -l "
output = subprocess.check_output(['bash','-c', bashcommand])

if output > 0:
#	print "Encryption Libraries are present. The details are as follows:\n"
	bashcommand="cat Features/encryption.txt"
	output = subprocess.check_output(['bash','-c', bashcommand])
#	print output

else:
	print "No encryption libraries provided.\n"

