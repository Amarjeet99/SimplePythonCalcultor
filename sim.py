print(' enter your choice : '.center(50,'*'))
print(' Press  1 for add  : '.center(50,'*'))
print(' Press  2 for sub  : '.center(50,'*'))
print(' Press  3 for mul  : '.center(50,'*'))
print(' Press  4 for div  : '.center(50,'*'))
print(' Input quit for exit  : '.center(50,'*'))

ch=''

while ch!='quit':
	ch=input('enter your choice : ')
	if ch=='1':
		a=int(input('enter 1st no : '))
		b=int(input('enter 2st no : '))
		sum=a+b
		print(sum)
	elif ch=='2':
		a=int(input('enter 1st no : '))
		b=int(input('enter 2st no : '))
		sub=a-b
		print(sub)
	elif ch=='3':
		a=int(input('enter 1st no : '))
		b=int(input('enter 2st no : '))
		mul=a*b
		print(mul)
	elif ch=='4':
		a=int(input('enter 1st no : '))
		b=int(input('enter 2st no : '))
		div=a/b
		print(div)

