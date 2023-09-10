import sys

def main():
    print("Hello World!")
    args = sys.argv

    print(args[1])
    # print(args[2])
    if args[1] == '-h':
        print("-h in Hello World!")
    elif args[1] == '-m':
        meibo()

class Person:
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
    
    def print_height(self):
        print(self.name+"さん"+"の"+"身長"+"は"+str(self.height)+"(cm)"+"です。")
    
    def print_weight(self):
        print(self.name+"さん"+"の"+"体重"+"は"+str(self.weight)+"(kg)"+"です。")
    
    def print_footsize(self):
        print(self.name+"さん"+"の"+"足のサイズ"+"は"+str(self.footsize)+"です。")
    
    def print_profession(self):
        print(self.name+"さん"+"の"+"職業"+"は"+str(self.profession)+"です。")

    def print_working_history(self):
        print(self.name+"さん"+"の"+"職歴"+"は"+str(self.working_history)+"です。")
    
    def is_public(self):
        if self.publishing_settings == "公開":
            return True
        else:
            return False

def meibo():
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
    all_print(meibo)

    # file close
    f.close()

def all_print(persons: Person):
    for person in persons:
        # print(person)
        if person.is_public() == False:
            continue
        # person.properties()
        person.print_height()
        person.print_weight()
        person.print_footsize()
        person.print_profession()
        person.print_working_history()


if __name__ == "__main__":
    main()