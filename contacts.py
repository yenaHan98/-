# Object = 기능(function) + 속성(Property, Attribute, Feature) => 파라미터( AI 파트 )

class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):
        print(f'이름 : {self.name}, 전화번호:{self.phone}, 이메일:{self.email}, 주소:{self.addr}')


    @staticmethod
    def set_contact():
        name = input('이름')
        phone = input('번호')
        email = input('이메일')
        addr = input('주소')
        contact = Contact(name, phone, email, addr)
        return contact

    @staticmethod
    def get_contact(clist):
        for i in clist:
            i.print_info()

    @staticmethod
    def del_contact(clist, name):
        for i , t in enumerate(clist):
            if t.name == name:
                del clist[i]


    @staticmethod
    def print_menu():
        print('1 연락처입력')
        print('2 연락처출력')   
        print('3 연락처삭제')
        print('4 종료')
        menu = input('메뉴선택 :')
        return menu

    @staticmethod
    def run():
        clist = []
        while 1:
            menu = Contact.print_menu()
            if menu == '1':
                t = Contact.set_contact()
                clist.append(t)

            if menu == '2':
                Contact.get_contact(clist)
                

            if menu == '3':
                name = input('삭제할 이름')
                Contact.del_contact(clist, name)

            elif menu == '4':
                break

if __name__ == '__main__':
    Contact.run()
    

"""
결론 : 객체지향은 속성이 존재해야 한다.
그리고 속성을 정의하는 곳은 __init__(속성파라미터)이다.
self는 객체내부의 속성에 접근하는 키워드
속성은 은닉화때문에 반드시 self. 로만 접근할 수 있다.
이는 보안의 기본이다.
"""