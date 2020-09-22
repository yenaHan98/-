from titanic.entity import Entity
import numpy as np
import pandas as pd
'''
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
'''

class Service:
    def __init__(self):
        self.entity = Entity()

    def new_model(self, payload) -> object:
        this = self.entity
        this.context = './data'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


    @staticmethod
    def create_train(self, this):
        return this.train.drop('Servived', axis=1) # train은 답이 제거된 데이터셋

    # self 없이 create_label 기능 만들기
    # self 없이 차원축소하기 위해 drop_feature 만들기

    @staticmethod
    def create_label(this):
        return this.train['Servived']

    @staticmethod
    def drop_feature(this):
        pass