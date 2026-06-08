str='abaabbaaabbbaaaabbbb'
result = []
for i in range(1, 5):
    s = 'a' * i + 'b' * i
    result.append(s)
print(result)

list=['7', '$', '5', '9','.', '1']
ans=[]
for i in list:
    if i.isdigit():
        ans.append(i)
ans.sort()
j=0
for i in range(len(list)):
    if list[i].isdigit():
        list[i] = ans[j]
        j+=1
print(list)