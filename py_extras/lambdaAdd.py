add = lambda x,y : x + y

print(add(2, 3))


print(list(map(lambda x: x*2, [1,2,3,4])))


dict_a = [{'name':'python', 'points':10}, {'name':'java','points': 8}]


print(list(map(lambda x: x['name'], dict_a)))

print(list(map(lambda x: x['points']*10, dict_a)))

print(list(map(lambda x: x['name'] == "python", dict_a)))