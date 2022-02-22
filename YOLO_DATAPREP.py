import os
import shutil 

directories=("/home/priyanshu-vaaan/Downloads/VIDS Data annotation","/home/priyanshu-vaaan/Downloads/VIDS Data annotation/VIDS/DATAZIP/DATA5","/home/priyanshu-vaaan/Downloads/VIDS Data annotation/VIDS/DATAZIP/DATA6","/home/priyanshu-vaaan/Downloads/VIDS Data annotation/VIDS/DATAZIP/DATA7","/home/priyanshu-vaaan/Downloads/VIDS Data annotation/VIDS/DATAZIP/DATA8")
save_data=("/home/priyanshu-vaaan/EBIN_TRAINING/VIDS_DATA_NEW/")
count=12136

for directory in directories:
    for filename in os.listdir(directory):
        os.chdir(directory)
        if filename.endswith(".jpg"):
            file=filename.split(".")[0]
            os.rename("{}.jpg".format(file),"{}.jpg".format(count))
            os.rename("{}.txt".format(file),"{}.txt".format(count))        
            shutil.copyfile("{}.jpg".format(count),(os.path.join(save_data,"{}.jpg".format(count))))
            shutil.copyfile("{}.txt".format(count),(os.path.join(save_data,"{}.txt".format(count))))
            count+=1



