list_tupples=[(1234,'john',23000,23),
              (1235,'amanda',30000,27),
              (1236,'jack',25000,24),
              (1237,'jim',28000,29),
              (1238,'raj',29000,30),
              (1239,'rakesh',33000,33),
              (1240,'anna',43000,45),
              (1241,'raju',53000,35),
              (1242,'emma',50000,49)]
print(list_tupples)
sum=0
for *others,salary,age in list_tupples:
    sum=sum+salary
    avg=sum/len(list_tupples)
print(sum,avg)

