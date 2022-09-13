# Print 1 to n using backtracking


def printNum(n):
    if n < 1:
        return
    printNum(n-1)
    print(n)

def main():
    n = int(input("enter number"))
    printNum(n)

main()