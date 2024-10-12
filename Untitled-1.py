import pandas as pd


class inspection :
    def __init__(self):
        self.__ddb = pd.read_csv("C:/Users/svyat/Desktop/тестирование/PR3SZ/main.csv")
    
    def startInspection (self):
        while(len(self.__ddb.columns) > 1 and len(self.__ddb) > 1):
            self.__s = self.__ddb.head(1).transpose().loc[self.__ddb.iloc[0] == 1].index[0]
            print("do you have", self.__s[self.__s.find('_') + 1:], "?(y/n):", end="")
            ans = input()
            if not(ans == 'y' or ans == 'n'):
                print("incorrect answer")
                continue
            elif ans == 'y':
                self.__ddb = self.__ddb[self.__ddb[self.__s] == 1]
                if(self.__ddb.columns[-2] == self.__s):
                    print("diagnosis:", self.__ddb.iloc[0]['label'][self.__s.find('_') + 1:])
            else:
                self.__ddb = self.__ddb[self.__ddb[self.__s] == 0]
            self.__ddb = self.__ddb.drop(self.__s, axis=1)
            print(self.__ddb)
        print("diagnosis:", self.__ddb.iloc[0]['label'][self.__s.find('_') + 1:])
game_inst = inspection()
game_inst.startInspection()