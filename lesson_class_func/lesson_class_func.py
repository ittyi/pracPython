import sys

def main():
    print("Hello World!")
    args = sys.argv

    print(args[0])
    print(args[1])
    print(args[2])
    if args[1] == '-h':
        print("-h in Hello World!")
    
    meibo()

class Person:
    def __init__(self, record):                  # コンストラクタ
        self.name = record[0]
        self.height = record[1]
        self.weight = record[2]
        self.footsize = record[3]
        self.profession = record[4]
        self.working_history = record[5]
        self.publishing_settings = record[6]
    
    def properties(self):
        print("name:", self.name)
        print("height:", self.height)
        print("weight:", self.weight)
        print("footsize:", self.footsize)
        print("profession:", self.profession)
        print("working_history:", self.working_history)
        print("publishing_settings:", self.publishing_settings)


def meibo():
    print("in meibo()")
    path = './meibo.txt'

    f = open(path)

    print(type(f))
    # <class '_io.TextIOWrapper'>
    s = f.read()
    # print(type(s))
    # print(s)
    meibo_list = s.split('\n')
    # print(meibo_list)
    for record in meibo_list:
        if record == '':
            continue
        print(record)
        tmp = record.split()
        print(tmp)
        Person(tmp).properties()


    f.close()

        
if __name__ == "__main__":
    main()