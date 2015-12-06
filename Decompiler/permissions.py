import sys
import subprocess


def permissions(manifest):
	bashcommand = "cat "+manifest+" | grep -E -o '\"android.permission.*'"
	output = subprocess.check_output(['bash','-c',bashcommand])
	output = output.split('\n')
	#for i in range(len(output)-1):
	#	temp = output[i].split()
	#	output[i] = temp[1]
	#	output[i] = output[i][:-3]
	#	output[i] = output[i][14:]
	return output


filename = sys.argv[1]
x =  permissions(filename)
for i in range(len(x)-1):
	print x[i]

