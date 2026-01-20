# while
cnt=0
while cnt<5:
    print(cnt) #vertical printing
    cnt+=1



cnt=0
while cnt<5:
    print(cnt,end=" ") # horizontal printing
    cnt+=1


cnt=0
res=[]
while cnt<5:
    res.append(cnt) # [0, 1, 2, 3, 4]
    cnt+=1

print(res)

cnt = 0
result = []

while cnt < 5:
    result.append(str(cnt))
    cnt += 1

print(" ".join(result)) # 0 1 2 3 4


# In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.

count = 0
while count < 5:
    print(count,end=' ')
    count = count + 1
else:
    print('\nloop ends with a count of ',count)



#break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break


#continue
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1