b=[ ]
while True:
	a=input()
	if a=='stop':
		break
	a=int(a)
	b.append(a)
print(b)
f=0
for i in range(1,len(b)+1):
		f=f+i
print(f)

	
	