import sys

def print_meibo(settingList: list):
    print("in meibo()")

    # file open&input part
    path = './meibo.txt'
    f = open(path)
    s = f.read()

    # Input processing part
    meibo_list = s.split('\n')
    meibo = []
    for record in meibo_list:
        if record == '':
            continue
        tmp = record.split()
        meibo.append(Person(tmp))

    # output part
    print(str(len(meibo))+"人の名簿を受け取りました。")
    all_print(meibo, settingList)

    # file close
    f.close()

class Person:
    HEIGHT = "身長"
    WEIGHT = "体重"
    FOOTSIZE = "足のサイズ"
    BMI = "BMI"
    PROFESSION = "職業"
    WORKING_HISTORY = "職歴"
    LIST_OF_SETTINGS = [HEIGHT, WEIGHT, FOOTSIZE, BMI, PROFESSION, WORKING_HISTORY]

    def __init__(self, record): # コンストラクタ
        self.name = record[0]
        self.height = int(record[1])
        self.weight = int(record[2])
        self.footsize = record[3]
        self.profession = record[4]
        self.working_history = record[5]
        self.publishing_settings = str(record[6])
    
    def properties(self):
        print("name:", self.name)
        print("height:", self.height)
        print("weight:", self.weight)
        print("footsize:", self.footsize)
        print("profession:", self.profession)
        print("working_history:", self.working_history)
        print("publishing_settings:", self.publishing_settings)
    
    def print_height(self, flag: bool):
        if flag == False:
            return
        print(self.name+"さん"+"の"+"身長"+"は"+str(self.height)+"(cm)"+"です。")
    
    def print_weight(self, flag: bool):
        if flag == False:
            return
        print(self.name+"さん"+"の"+"体重"+"は"+str(self.weight)+"(kg)"+"です。")
    
    def print_footsize(self, flag: bool):
        if flag == False:
            return
        print(self.name+"さん"+"の"+"足のサイズ"+"は"+str(self.footsize)+"です。")
    
    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def print_bmi(self, flag: bool):
        if flag == False:
            return
        print(self.name+"さん"+"の"+"BMI"+"は"+str(self.bmi())+"(kg/m2)"+"です。")
    
    def print_profession(self, flag: bool):
        if flag == False:
            return
        print(self.name+"さん"+"の"+"職業"+"は"+str(self.profession)+"です。")

    def print_working_history(self, flag: bool):
        if flag == False:
            return
        print(self.name+"さん"+"の"+"職歴"+"は"+str(self.working_history)+"です。")
    
    def is_public(self):
        if self.publishing_settings == "公開":
            return True
        else:
            return False

def all_print(persons: Person, settingList: list):
    # print("in all_print()")
    t = create_dict(settingList, Person.LIST_OF_SETTINGS)
    for person in persons:
        if person.is_public() == False:
            continue

        person.print_height(t[person.HEIGHT])
        person.print_weight(t[person.WEIGHT])
        person.print_footsize(t[person.FOOTSIZE])
        person.print_bmi(t[person.BMI])
        person.print_profession(t[person.PROFESSION])
        person.print_working_history(t[person.WORKING_HISTORY])

def create_dict(settingList: list, LIST_OF_SETTINGS: list[str]):
    # print("in create_dict()")
    dict = {}
    index = 0
    for setting in LIST_OF_SETTINGS:
        if setting in settingList:
            dict[setting] = True
        elif setting not in settingList:
            dict[setting] = False
        else:
            print("setting error")
            sys.exit()
        index += 1
    
    # print("dict:", dict)
    return dict