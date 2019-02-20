d = {}

string = input("Enter A String\n")

l = []

l = string.split(" ")

for i in range(len(l)):
      d.update({l[i]:l[i][0]})

print(d)
