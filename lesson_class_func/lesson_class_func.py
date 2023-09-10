import sys
import hello
import meibo

def main():
    print("main start")
    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 lesson_class_func.py -h or -m")
        sys.exit()
    
    argsList = []
    if len(args) > 2:
        print("len(args)")
        for i in range(2, len(args)):
            print(args[i])
            argsList.append(args[i])
    
    print(argsList)

    # mode select
    if args[1] == '-h':
        hello.print_hello()
    elif args[1] == '-m':
        meibo.print_meibo(argsList)

if __name__ == "__main__":
    main()