# blank dictionary
b = {}
x = {}

a = [1,1,1,2,2,2,4,4,0,0,-1]
N = 11
a.sort()
c = 1
i = 0

while i < N:
    #print("i",i)
    for j in range(i+1, N):
        if a[i] == a[j]:
            c += 1
            #print(c)
        else:
            break

    #print("j",j)

    # inserting value in dictionary b -->> key: element  (a[i]) and value  count of element
    # we can exchange value as per our operations need
    b[a[i]] = c
    x[c] = a[i]

    # putting value of j in i
    i = i + j

    #print("c",c)
    #default value of c
    c = 1

# print dictionary b having elements as key and count as corresponding values
print(b)

# print max key value
print(max(b))

#print max key's of value
print(b[max(b)])

print(x)
print(max(x))
print(x[max(x)])

