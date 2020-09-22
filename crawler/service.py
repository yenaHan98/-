import sys
sys.path.insert(0, 'C:/SBAProject')

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
    # 이 메소드는 url을 받아서 soup 속성을 초기화한다.
    def get_url(self,url):
        myparser = 'html.parser' # html.parser : 간단한 HTML과 XHTML 구문 분석기. 표준 라이브러리
        response = urlopen(url)
        self.soup = BeautifulSoup(response, myparser)
        return type(self.soup)

    # 이 메소드는 folderName을 가진 이름의 파일을 현재 폴더 하위에 생성한다.
    def create_folder_weekend(self,folderName):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}
        self.weekday_dict=weekday_dict
        # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
        
        myfolder = './'+folderName +'/' # 유닉스 기반은 '/'이 구분자
        self.myfolder = myfolder
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)

    # mysrc 이미지파일의 url myweekday는 요일정 mytitle에 이미지 제목이 들어간다.
    @staticmethod
    def saveFile(myfolder, mysrc:str , myweekday:str, mytitle :str,weekday_dict):

        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
        # print(mysrc)
        # print(filename)

        myfile = open(filename, mode='wb')  # wb : write binary
        myfile.write(image_file.read())  # 바이트 형태로 저장
        myfile.close()
        # soup의 태그와 속성을 이용해 target을 정하고 타겟의 길이를 프린트한다.
    def setting_target(self,tag,class_attrs):
        self.mytarget = self.soup.find_all(tag, attrs={'class': class_attrs})
        self.len_mytarget=  len(self.mytarget)
        print("타겟의 길이:",self.len_mytarget)
    #
    def loop_fun(self,replace_str,mycolumns,filename):

        self.mylist = []  # 데이터를 저장할 리스트

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
            # print(mysrc)
            myfolder=self.myfolder
            weekday_dict=self.weekday_dict
            Service.saveFile(myfolder,mysrc, myweekday, mytitle,weekday_dict)

            # break

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