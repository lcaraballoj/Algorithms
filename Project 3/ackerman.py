def ackerman(m, n):
    if m == 0:
        return n + 1
    elif (m > 0 and n == 0):
        return ackerman(m-1, 1)
    elif (m> 0 and n>0):
        return ackerman(m-1, ackerman(m, n-1))

def main():
    m = int(input("Enter a value for m\n"))
    n = int(input("Enter a value for n "))

    print("Ackerman Alogrithm answer: ", ackerman(m, n))

main()
