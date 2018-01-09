from numpy import *

from os import listdir,linesep
from os.path import isfile,isdir,getsize,join


'''
Class for calculating the average of measurement data
'''
class AverageCalculator:

    '''
    Construtor providing the directory path where the measurement data can be found.
    It is possible to add another separator for the points and values. Default is a whitespace character
    '''
    def __init__(self,directory_path,separator=" "):
        self.directory_path=directory_path
        self.separator=separator

    '''
    Returns the average of the measurement data in the form of two vectors.
    The first vector contains the measurement points and the second vector the measurement data.
    Empty files are not included in the average just as files which dont have the same number of lines the first file.
    '''
    def GetResult(self):
        files=self.GetDirectoryContents()

        points=self.GetMeasurementPoints(files[0])
        values=zeros(points.shape)

        n_files=len(files)
        for file in files:
            isEmptyFile=getsize(join(self.directory_path,file)) == 0

            if not isEmptyFile:
                file_value=self.GetMeasurementValue(file)

                isSameDimension=file_value.shape == values.shape
                if isSameDimension:
                    values+=file_value
            else:
                n_files-=1

        if n_files > 0:
            values/=n_files
        else:
            values=array([],dtype=float)
            
        return points,values

    '''
    Returns the contents of the directory as a list of files names
    If you want to use a filter (eg. only *.txt files), this is where you should implement it.
    '''
    def GetDirectoryContents(self):
        return listdir(self.directory_path)

    '''
    Reads the location of the measurement points.
    It's assumed they are found in the first column of the file.
    '''
    def GetMeasurementPoints(self,file):
        points=[]
        with open(join(self.directory_path,file)) as f:
            flag=True
            for line in f:
                if flag:
                    flag=False
                    continue
                points+=[line.split(self.separator)[0]]

        return array(points,dtype=float)
    

    '''
    Reads the value of the measurement points.
    It's assumed they are found in the second column of the file.
    '''
    def GetMeasurementValue(self,file):
        values=[]
        with open(join(self.directory_path,file)) as f:
            flag=True
            for line in f:
                if flag:
                    flag=False
                    continue
                values+=[line.replace(linesep,'').split(self.separator)[1]]

        return array(values,dtype=float)
    
calculator=AverageCalculator(DEIN_PFAD,separator="\t")
f=open("/Users/Nora/Desktop/andi_ist_cool.txt","w+")
for i in range(x.shape[0]):
    f.write("%f\t%f\n"%(x[i],y[i]))
f.close()
