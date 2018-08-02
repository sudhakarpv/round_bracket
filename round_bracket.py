# round_bracket
def main():
    pass
    n=input()
    list_1=list(n)
    k=list_1.count('(')
    j=list_1.count(')')
    if(k==j):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
