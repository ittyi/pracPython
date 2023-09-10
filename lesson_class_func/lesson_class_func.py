import sys
import hello
import meibo

def main():
    print("main start")
    args = sys.argv

    print(args[1])
    # print(args[2])
    if args[1] == '-h':
        hello.print_hello()
    elif args[1] == '-m':
        meibo.print_meibo()

if __name__ == "__main__":
    main()