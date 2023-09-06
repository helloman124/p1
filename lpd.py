ascii_value=65
number_of_rows=5
for i in range(number_of_rows):
    for j in range((2*i+1)):
          print(chr(ascii_value),end="")
          ascii_value+=1
    print()
