#Primary Folder = /var/www aka the live folder
#Secondary Folder = /var/backup aka backup folder
#This script compares two two folder(Primary folder and secondary folder)
#if the contents of primary folder are different from that secondary folder
#the contents of secondary folder are copied to the primary folder

#!/bin/bash
#START
diff /var/backup /var/www > diff.txt #Checks the difference between two folders
if [ diff.txt ] #Checks if the diff.txt is empty or not
then
	rm -f diff.txt 
	rm -rf /var/www #removes the primary folder
	cp -r --copy-contents /var/backup/www /var #Copies the seonday folder to the primary
else
	rm -f diff.txt
fi
#END