import sys
import general_purpose

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

    print(str(count_public(meibo))+"人の名簿を受け取りました。")
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

    HONORIFIC_TITLE = "さん"
    SUFFIX = "です。"

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

    def template_print(self, selected_item: str, item_value: str, unit: str):
        print(self.name+self.HONORIFIC_TITLE+"の"+selected_item+"は"+item_value+unit+self.SUFFIX)

    def print_height(self, flag: bool):
        if flag == False:
            return
        self.template_print(self.HEIGHT, str(self.height), "(cm)")
    
    def print_weight(self, flag: bool):
        if flag == False:
            return
        self.template_print(self.WEIGHT, str(self.weight), "(kg)")
    
    def print_footsize(self, flag: bool):
        if flag == False:
            return
        self.template_print(self.FOOTSIZE, str(self.footsize), "(cm)")
    
    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

    def print_bmi(self, flag: bool):
        if flag == False:
            return
        self.template_print(self.BMI, str(self.bmi()), "(kg/m2)")
    
    def print_profession(self, flag: bool):
        if flag == False:
            return
        self.template_print(self.PROFESSION, str(self.profession), "")

    def print_working_history(self, flag: bool):
        if flag == False:
            return
        self.template_print(self.WORKING_HISTORY, str(self.working_history), "年")
    
    def is_public(self):
        if self.publishing_settings == "公開":
            return True
        else:
            return False

def count_public(persons: Person):
    count = 0
    for person in persons:
        if person.is_public() == True:
            count += 1
    return count

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
        print()

def create_dict(settingList: list, LIST_OF_SETTINGS: list[str]):
    # print("in create_dict()")
    dict = {}
    index = 0
    flg_more_than_once_in_settingList = False
    for setting in LIST_OF_SETTINGS:
        if setting in settingList:
            dict[setting] = True
            flg_more_than_once_in_settingList = True
        elif setting not in settingList:
            dict[setting] = False
        else:
            print("setting error")
            sys.exit()
        index += 1
    
    print("dict:", dict)
    if flg_more_than_once_in_settingList == False:
        return {'身長': True, '体重': True, '足のサイズ': True, 'BMI': True, '職業': True, '職歴': True}
    return dict