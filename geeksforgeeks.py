def upper_case():
    
    S = input('Enter a word with mixed capitalization')

    for i in S:
        if i in S.isupper():
            i.lower()
            print(i)