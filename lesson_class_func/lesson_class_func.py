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

def meibo():
    print("in meibo()")
    path = './meibo.txt'

    f = open(path)

    print(type(f))
    # <class '_io.TextIOWrapper'>
    s = f.read()
    print(type(s))
    print(s)
    meibo_list = s.split('\n')
    print(meibo_list)
    for record in meibo_list:
        if record == '':
            continue
        print(record)


    f.close()

        
if __name__ == "__main__":
    main()