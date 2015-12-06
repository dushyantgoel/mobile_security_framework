import subprocess

f=open('input.txt')
filename = f.read().split('.')[0]

bashcommand="echo '"+filename+"' > ../../cmd.txt"
print bashcommand
output = subprocess.check_output(['bash','-c', bashcommand])

bashcommand="cp ../../../uploads/"+filename+".apk ../../"+filename+".zip"
print bashcommand
output = subprocess.check_output(['bash','-c', bashcommand])

bashcommand="unzip ../../"+filename+".zip -d ../../"+filename
print bashcommand
output = subprocess.check_output(['bash','-c', bashcommand])

bashcommand="cp ../../../uploads/"+filename+".apk ../../../uploads/"+filename+".zip"
print bashcommand
output = subprocess.check_output(['bash','-c', bashcommand])

bashcommand="unzip ../../../uploads/"+filename+".zip -d ../../../uploads/"+filename
print bashcommand
output = subprocess.check_output(['bash','-c', bashcommand])


bashcommand="cp ../../"+filename+"/classes.dex ."
output = subprocess.check_output(['bash','-c', bashcommand])
print bashcommand

bashcommand="./d2j-dex2jar.sh classes.dex"
output = subprocess.check_output(['bash','-c', bashcommand])
print bashcommand

bashcommand="java -jar ./jd-cmd/jd-cli/target/jd-cli.jar ./classes-dex2jar.jar -od ../../original_"+filename+" -oc"
output = subprocess.check_output(['bash','-c', bashcommand])
print bashcommand

bashcommand="rm -rf ../../"+filename+".zip"
output = subprocess.check_output(['bash','-c', bashcommand])
print bashcommand

bashcommand="rm ./classes.dex ./classes-dex2jar.jar"
output = subprocess.check_output(['bash','-c', bashcommand])
print bashcommand
