immutable_var=( 'a', 'b', 1, 2)
print(immutable_var)
#immutable_var['a']=m
#изменения невозможны, так как кортеж не поддерживает изменения элементов
mutable_list=([3, 4], ['h', 't'])
mutable_list[0][0]=6
mutable_list[0][1]=7
mutable_list[1][0]='r'
mutable_list[1][1]='x'
print(mutable_list)