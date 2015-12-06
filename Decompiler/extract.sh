cd original*
find . -type f -exec mv {} . \;
find . -type d -exec rm -rf {} \;

cat * > ../../full_java_sourcecode.txt
cd ..
