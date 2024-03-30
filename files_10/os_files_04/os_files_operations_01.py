import os
import shutil
from send2trash import send2trash

print('-----------------os_files_operations------------')
print('-------------------os.listdir---------------')
file_list = os.listdir('C:\\MY_FILES')
print(file_list)

print('-------------------create new dir--------------')
if not os.path.exists('C:\\MY_FILES\\new_folder'):
    os.makedirs('C:\\MY_FILES\\new_folder')

print('-------------copy file from location----------')
source_file = 'C:\\MY_FILES\\people.csv'
dest_file = 'C:\\MY_FILES\\new_folder\\people3.csv'
#shutil.copyfile(source_file,dest_file)

print('-------------rename a file----------')
old_name = 'C:\\MY_FILES\\new_folder\\people3.csv'
new_name = 'C:\\MY_FILES\\new_folder\\people_new.csv'
#os.rename(old_name,new_name)


print('-------------move(cut) directory to another dest----------')
source_file2 = 'C:\\MY_FILES\\people_cairo.csv'
dest_file2 = 'C:\\MY_FILES\\new_folder\\people_cairo.csv'
#shutil.move(source_file2,dest_file2)

print('-------------------delete file--------------')
file_to_delete = 'C:\\MY_FILES\\new_folder\\people_new.csv'
#send2trash(file_to_delete)   # move to recycle bin
os.remove(file_to_delete)    # delete permanently without recycle bin
