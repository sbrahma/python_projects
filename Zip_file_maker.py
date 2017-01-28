"""
Project: Create Zip File Maker
Author: S.Brahma
Date: 28/1/2017
Problem: The user enters various files from different directories and the program zips them up into a zip file. 
Optional: Apply actual compression to the files. Start with Huffman Algorithm. import os, datetime
"""
source_dir = ['/Users/Sam/python'] # please change it accordingly
upload_time = datetime.datetime.now().strftime("%Y-%m-%d")

folder = os.path.join('/Users/Sam/python/backup', upload_time ) # please change it accordingly
filename = folder + '.zip'
zip_command = "zip -qr '%s' %s"	%(folder, ' '.join(source_dir))

# run zip command
if os.system(zip_command) == 0:
	print " the file %s is successfully zipped" %filename
else:
	print "Backup failed."	
	




# Another version discussed in the book "A byte of Python"

# import os
# import time
# # 1. The files and directories to be backed up are specified in a list.
# source = ['/Users/Sam/python']
# 
# # 2.The backup must be stored in a main backup directory
# target_dir ='/Users/Sam/python/backup'# Remember to change this to what you will be using
# 
# # 3. The files are backed up into a zip file.
# # 4. The name of the zip archive is the current date and time
# target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 
# # 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
# zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
# 
# # Run the backup
# if os.system(zip_command) == 0:
# 	print 'Successful backup to', target
# else:
# 	print 'Backup FAILED'