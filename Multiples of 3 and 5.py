
#BASIC METHOD ONE
'''This solution isn't bad but isn't good either '''

multiples =[]
for i in range(1000):
    if (i%3 ==0 or i%5==0 ):
        multiples.append(i)
print(sum(multiples))

#MORE EFFICIENT METHOD
'''This method is more efficient because we compute the sum od the arithmetic sequene for all the multiples of 3,5,15 without iterating through anything at all.'''
def arithm_sum(n):
    #arithmetic sequence
    return n*(n+1)/2

def aritthm_seq(limit):
    threes = 3*arithm_sum(n//3)
    fives = 5 * arithm_sum(n // 5)
    fifteens = 15 * arithm_sum(n // 5)
    return threes+fives-fifteens
