def avg(marks):
    #will stop bc mark1 is an empty list
    assert len(marks) != 0
    return sum(marks)/len(marks)




a = 1

#will give AssertionError, because a == 1  and program will stop here
#assert a == 0

#will pass and no error
assert a == 1

mark1 = []
print("Average of mark1:",avg(mark1))




