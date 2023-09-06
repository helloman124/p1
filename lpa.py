def letterchanges(st):
    index=0
    new_word=""
    alphabet="abcdefghijklmnopqrstuvwxyza"
    for i in st.lower():
        if i.islower():
            index=alphabet.index(i) + 1
            new_word+=alphabet[index]
        else:
            new_word+=index
    return new_word
print(letterchanges(input("enter 4 charecters:")))
