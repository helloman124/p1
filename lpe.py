strings=eval(input("enter the list\n"))
count=0
for x in strings:
    if len(x)>=2 and x[0]==x[-1]:
        count+=1
print("string 1st and last charecter are same is:",count)
