ch = list(map(int,file.split(" ")))
for i in range(max(ch)+1):
     counts.append(ch.count(ch[i]))
print('kol-vo ',i,'?????:',ch.count(ch[i]))
print('kol-vo ',i,'rav:',ch.count(ch[i]))
print ('chasto:',counts.index(max(counts)))
print ('redko:',counts.index(min(counts)))
print ('razlichnie:',(101-counts.count(0)))