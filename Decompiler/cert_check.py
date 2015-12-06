import subprocess
import hashlib

f = open('cmd.txt')
inp = '../uploads/'+f.read().strip('\n')

print 'cd '+inp
print "find . -type f | egrep -e 'cer' -e 'pem' -e 'cert' -e 'crt' -e 'pub' -e 'key' -e 'pfx' -e 'p12' > ../../hardcoded_certs.txt"
print 'cd ../../Decompiler/'
print 'java -jar CertPrint.jar '+inp+'/META-INF/CERT.RSA > ../certfile.txt'
print 'java -jar strings_from_apk.jar '+inp+'.apk '+inp+'/'
print 'mv '+inp+'/strings.json ../'
print 'du -k '+inp+'.apk | cut -f1 > ../appsize.txt'

#print "[INFO] Generating Hashes"
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
BLOCKSIZE = 65536
afile = open(inp+'.apk','rb')
buf = afile.read(BLOCKSIZE)
while len(buf) > 0:
    sha1.update(buf)
    sha256.update(buf)
    buf = afile.read(BLOCKSIZE)
sha1val = sha1.hexdigest()
sha256val=sha256.hexdigest()
#print 'rm hashes.txt'
print 'echo '+sha1val+' >> hashes.txt'
print 'echo '+sha256val+' >> hashes.txt'
print 'mv hashes.txt ../'

print 'java -jar AXMLPrinter2.jar '+inp+'/AndroidManifest.xml > Manifest.xml' 