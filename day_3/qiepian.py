L= ['name','age','old',1,3,4,4,5,55,66,6,6,7,7,7,7,8,]

print(L[1])
# slice 切片操作 L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。 	
print(L[0:2])
#第一个索引为0 可以省略
print(L[:2])

#取出倒数第一个元素
print(L[-1])
# 切片 取出倒数第一个元素
print(L[-1:])
# 从倒数第三个开始 取到最后一个 不包括最后一个
print(L[-3:-1])
