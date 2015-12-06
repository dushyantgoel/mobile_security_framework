import sys
import subprocess

def package_name(manifest):
	bashcommand = "cat "+manifest+" | grep -E -o 'package.*'"
	output = subprocess.check_output(['bash','-c',bashcommand])
	output = output[:-3]
	output = output[9:]
	return output

def main_activity(manifest):
	bashcommand = "cat "+manifest+ " | grep -E -o 'version.*'"
	output = subprocess.check_output(['bash','-c',bashcommand])[:-3]
	output = output.split()
	return output

def main():
	filename = sys.argv[1]
	print package_name(filename)
	print main_activity(filename)

main()
