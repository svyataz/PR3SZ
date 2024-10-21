import pandas as pd


class inspection :
    def __init__(self):
        self.__ans = None
        self.__s = None
        self.__answers = []
        self.__ddb = pd.read_csv("C:/Users/svyat/Desktop/тестирование/PR3SZ/main.csv")
    
    def ddb_setter(self, newdb):
        self.__ddb = newdb

    def ddb_getter(self):
        return  self.__ddb
    
    def ans_setter(self, newans):
        self.__ans = newans

    def ans_getter(self):
        return  self.__ans
    
    def s_setter(self, news):
        self.__s = news

    def s_getter(self):
        return  self.__s
    
    def ansInput(self):
        self.__s = self.__ddb.head(1).transpose().loc[self.__ddb.iloc[0] == 1].index[0]
        print("do you have", self.__s[self.__s.find('_') + 1:], "?(y/n):", end="")
        self.__ans = input()
    
    def ans_check(self):
        if not(self.__ans == 'y' or self.__ans == 'n'):
            print("incorrect answer")
            return True
        elif self.__ans == 'y':
            self.__ddb = self.__ddb[self.__ddb[self.__s] == 1]
        else:
            self.__ddb = self.__ddb[self.__ddb[self.__s] == 0]
        return False
    
    def loop(self):
            self.ansInput()
            if(self.ans_check()): 
                self.startInspection()
                return None
            self.__ddb = self.__ddb.drop(self.__s, axis=1)
            self.__answers.append(self.__ans)

    def answer(self):
        if not('y' in self.__answers):
            return "You are healthy"
        return "Diagnosis:" + self.__ddb.iloc[0]['label'][self.__s.find('_') + 1:]

    def startInspection (self):
        while (len(self.__ddb.columns) > 1 and len(self.__ddb) > 1):
            self.loop()
        return self.answer()

'''game_inst = inspection()
print(game_inst.startInspection())'''