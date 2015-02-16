# import operator
# import functools
# functools.reduce(operator.mul, [1,2,3,4,5,6], 1)

def is_prime(N):
    if N == 2:
        return True
    elif N % 2 == 0:
        return False
    #TODO:- A more efficient method would be range till square root
    for current in range(3,int(N/2)+1,2):
        if N % current == 0:
            return False
    return True

def gen_prime():
    count = 2
    while True:
        if is_prime(count):
            yield count
        count += 1

def get_facts(N,factors):
    # import pdb; pdb.set_trace()
    for x in gen_prime():
        if N % x == 0:
            factors.append(x)
            # get_facts(N/x,factors)
        elif not is_prime(N / x):
            get_facts(N/x,factors)
        else:
            break

def main():
    N = int(input("Enter the number to factorize"))
    factors = []
    factors = get_facts(N)
    print term

if __name__ == '__main__':
    main()