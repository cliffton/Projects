#Fibonacci Series 
#TODO:- Limits and this seems cooler
"""
    if N == 1:
        return [1, 0]
    else:
        terms = fib(N - 1)
        terms = [terms[0] + terms[1], terms[0]]
        return terms

"""


def fibo(percision):
    count = 1
    first_term = 0
    second_term = 1
    if count <= 1:
        next = count
    while count < percision:
        next = first_term + second_term
        first_term =  second_term
        second_term = next
        count +=1
    return next


def main():
    term = fibo(int(input(
        "Enter the number terms to calculate: ")))

    print term

if __name__ == '__main__':
    main()