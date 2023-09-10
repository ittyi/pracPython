import sys
import hello
import meibo
import general_purpose

def main():
    print("main start")
    args = sys.argv
    count_length = general_purpose.ft_len(args)

    if count_length < 2:
        print("Usage: python3 lesson_class_func.py -h or -m")
        sys.exit()
    
    argsList = []
    if count_length > 2:
        print("len(args)")
        for i in range(2, count_length):
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