exponent=lambda number, index:number**index

nums=[1,2,3,4,5,6]
res = map(exponent,nums,range(0,len(nums)))
print(list(res))

