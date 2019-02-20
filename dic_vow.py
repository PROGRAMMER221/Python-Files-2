k = int(input("How Many Key You Want To Get \n"))

d = {}

for i in range(k):
      key = input("Enter A Key Value \n")
      l = []
      for i in key:
            if  i in "aeiouAEIOU":
                  l.append(i)
      d.update({key:l})

print(d)

