string = input("Enter A String \n")

l = []

l = string.split(" ")

d = {}

for i in range(len(l)):
      key = l[i]
      d.update({key:l[i][0]})

print(d)



