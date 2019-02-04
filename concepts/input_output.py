#it will map input values to n and q using map function
n, q = map(int, input().split())
print({} is n and {} is q.format(n,q))
print(n,q)



#it will put and map input elements to a list
x = list(map(int, input().split()))
print(x)
print({} is a list first value.format(x[0]))



#default input will be a string, here take input --> 2 3 4
l = input()
#can split string with any character, in this exp, it will split with " " --> ['2','3','4']
l = l.split(" ")
# this will print list l having characters --> ['2','3','4']
print(l)  



# it will convert the input to int, NOTE: input should be number only, without space
m = int(input())
