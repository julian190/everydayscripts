import os 
import shutil
# file extenstions 
extdic = {
        'Document':['.csv','.dat','.db','.log','.mdb','.sav','.sql','.tar','.xml','.pdf'],
        'Photos':['.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg'],
        'Audio':['.aif','.cda','.mid','.mp3','.mpa','.ogg','.wav','.wma','.wpl'],
        'Archive':['.7z','.arj','.deb','.pkg','.rar','.rpm','.targz','.z','.zip']
}
stat_files ={}
# get current folder where the script is there 
current_path = os.path.dirname(os.path.realpath(__file__))

def movefile(file,ext):
    targetpath = current_path+'/' #move the files to the folder named as the dic key
    for x , y in extdic.items():
        
        for extensions in y: # looking inside extenstions in the dictunary
            if ext in extensions:
                if not os.path.exists(targetpath+x): # if the directory not exists it will create one 
                    os.mkdir(targetpath+x)
                    shutil.move(current_path+'/'+file,targetpath+x) # move the files to the created directory
                    stat_files[x] = stat_files.get(x,0)+1
                    print('file ', file, 'moved to',targetpath,x) # Just for Debug :)
                if(os.path.exists(targetpath+x+'/'+filename)):  # If the file exists in the directory will print that file is there 
                    print('file found' , file , 'and wont copy')
                else:
                    shutil.move(current_path+'/'+file,targetpath+x) # if the directory exists and the file is not there then it will copy
                    stat_files[x] = stat_files.get(x,0)+1
                    print('file ', file, 'moved to',targetpath,x)
    
                

                #
                #print(file,targetpath+x)
                
#loop in the director and get the extenstion then move it
files = [f for f in os.listdir(current_path) if os.path.isfile(f)]
for filename in files:
    ext = os.path.splitext(filename)[1]
    movefile(filename,ext)
    print('total moved files ',stat_files)




