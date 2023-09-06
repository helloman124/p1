def length(string):
    if string==" ":
     return 0
    else:
     return 1+len(string[1:])

def minn(A,n):
   if(n==1):
      return A[0]
   return min(A[n-1],minn(A,n-1))
    
def strrev(l):
   if l=="":
      return ""
   else:
      return l[-1]+strrev(l[:-1])
    
ch=int(input("enter ch: "))
if ch==1:
    string=input("enter str: ")
    print("str len is ",len(string))
elif ch==2:
    A=eval(input("enter the list:")) 
    n=len(A)  
    print("smallest stringis",minn(A,n))
elif ch==3:
   l=str(input("enter a string"))
   print("reverse of a string:",end="")
   print(strrev(l))
