cd src/dex2jar-2.0
bash get_input.sh
python extract.py 2>../../error.log
cd ../..
bash extract.sh
bash cert_check.sh
python permissions.py Manifest.xml > ../Features/manifest_permissions.txt
python app_info.py Manifest.xml > ../Features/App_info.txt
python remove_folder.py