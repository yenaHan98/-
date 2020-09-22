import sys
sys.path.insert(0, r'C:\Users\yenaHan\SbaProjects')

from crawler.entity import Entity

from crawler.service import Service


# 내부에서는 모듈의 객체를 인스턴스화해야 한다.
# 대문자는 클래스
# 소문자는 인스턴스= (객체)
# 라운드 브레이스가 있는 클래스는 생성자이다.
# 결론.. 객체지향(OOP)에서는 속성과 기능을 호출하는 구조로 
# 두가지 방식이 있는데
# (스태틱)클래스 객체
# (다이나믹) 인스턴스 객체

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