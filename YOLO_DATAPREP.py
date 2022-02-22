import os
import shutil 

directories=(" "," "," ")   #List your directories
save_data=("")              #Location where you want to save your data
count=0                #use a non pre-existing max count 

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



