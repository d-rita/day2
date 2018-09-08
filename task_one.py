def countVowels(string):
    vowels=['a','e','i','o','u']
    word_vowels=[]
    vowels_count=0
    for i in string:
        if i in vowels:
            word_vowels.append(i)
            vowels_count+=1
    x = set(word_vowels)
    x="".join(x)
    return(x, vowels_count-len(x))
    


        


