import sys
sys.path.insert(0, r'C:\Users\yenaHan\SbaProjects')

from crawler.entity import Entity

from crawler.service import Service


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
if __name__=='__main__':
    mycolumns = ['타이틀 번호', '요일', '제목', '링크']
    filename = 'cartoon.csv'
    url= 'https://comic.naver.com/webtoon/weekday.nhn'
    new_folder_name='newfile'
    tag='div'
    attrs='thumb'
    replace_str='/webtoon/list.nhn?'
    api = Controller()
    service= Service()
    service.get_url(url)
    service.create_folder_weekend(new_folder_name)
    service.setting_target(tag, attrs)
    service.loop_fun(replace_str,mycolumns,filename)