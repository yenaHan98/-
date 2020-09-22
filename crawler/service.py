import sys
sys.path.insert(0, r'C:\Users\yenaHan\SbaProjects')

from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, shutil
from pandas import DataFrame

class Service:
    def __init__(self):
        self.soup = None
        self.len_mytarget = None
        self.mytarget = None
        self.myfolder =None
        self.weekday_dict= None
        self.list = None

    def bugs_music(self):
        pass
    def naver_movie(self):
        pass
    def get_url(self,url):
        myparser = 'html.parser' 
        response = urlopen(url)
        self.soup = BeautifulSoup(response, myparser)
        return type(self.soup)

    def create_folder_weekend(self,folderName):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}
        self.weekday_dict=weekday_dict
        
        myfolder = './'+folderName +'/' 
        self.myfolder = myfolder
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)

    @staticmethod
    def saveFile(myfolder, mysrc:str , myweekday:str, mytitle :str,weekday_dict):

        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
       
        myfile = open(filename, mode='wb')  
        myfile.write(image_file.read())  
        myfile.close()
    def setting_target(self,tag,class_attrs):
        self.mytarget = self.soup.find_all(tag, attrs={'class': class_attrs})
        self.len_mytarget=  len(self.mytarget)
        print("타겟의 길이:",self.len_mytarget)
    #
    def loop_fun(self,replace_str,mycolumns,filename):

        self.mylist = []  

        for abcd in self.mytarget:
            myhref = abcd.find('a').attrs['href']
            print('myhref:', myhref)
            print('_' * 30)
            myhref = myhref.replace( replace_str , '')
            result = myhref.split('&')
            print('myhref:',myhref)
            print('_'*30)
            print('result:',result)
            print('_'*30)
            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]
            print('mytitleid:',mytitleid)
            print('_' * 30)
            print("myweekday:",myweekday)
            print('_' * 30)
            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')
            print(mytitle)

            mysrc = imgtag.attrs['src']
            myfolder=self.myfolder
            weekday_dict=self.weekday_dict
            Service.saveFile(myfolder,mysrc, myweekday, mytitle,weekday_dict)

            sublist = []
            sublist.append(mytitleid)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)
            self.mylist.append(sublist)
        mylist=self.mylist
        Service.saveImagesCsv(mycolumns,mylist,filename)

    @staticmethod
    def saveImagesCsv(mycolumns,mylist,filename):
        myframe = DataFrame(mylist, columns=mycolumns)

        myframe.to_csv(filename, encoding='utf-8', index=False)
        print(filename + '파일로 저장됨')

        print('finished')