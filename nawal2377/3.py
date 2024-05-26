user=input('enter username: ')
l=[]
count=0
q=open('questions.csv','r')
res=open('answers.csv','w')
for i in q:
    l1=i.rstrip().split(',')
    l.append(l1)
for i in l:
    print(i[0])
    ans=input()
    if ans==i[1]:
        count+=1
        print('correct')
    else:
        print('incorrect')
print(user)
print('true answers is ',count,'from 20')
res.write(user+','+ str(count))
q.close()
res.close()

