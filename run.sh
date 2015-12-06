mkdir Features
cd Decompiler
bash run.sh
rm -rf original*
cd ..
python features.py 
mv certfile.txt hardcoded_certs.txt strings.json appsize.txt hashes.txt Features/
firefox abc.html
 
