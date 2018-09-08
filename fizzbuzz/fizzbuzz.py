def fizzbuzz(a,b):
    if type(a)==list and type(b)==list:
        total=len(a)+len(b)
        if total%3==0 and total%5==0:
            # print(total)
            return('fizzbuzz')
        elif total%3==0:
            # print(total)
            return ('fizz')
        elif total%5==0:
            # print(total)
            return('buzz')
        else:
            return total
    else:
        return('Invalid input')

