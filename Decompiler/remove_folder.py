import subprocess

f= open('cmd.txt').read().strip('\n')
bashcommand='rm -rf '+f
print bashcommand
output = subprocess.check_output(['bash','-c', bashcommand])
