import os
import glob
import sys
#target_folder = 'C:/Users/DBLab/Downloads/deathinthefamily'
target_folder = sys.argv[1]
fileList = glob.glob(target_folder+'/*.jpg')
formatTarget = '0'+str(len(str(bin(int(len(fileList)))))) +'b'
for f in fileList:
    filename = f.replace(target_folder, '').replace('\\', '')
    nameOnly = filename.split('.')[0]
    ext = filename.split('.')[1]
    nameOnly = format(int(nameOnly), formatTarget)
    
    result = nameOnly+'.'+ext
    print(filename + ' >> '+result)
    os.rename(target_folder+'/'+filename, target_folder+'/'+result)