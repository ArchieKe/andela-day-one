def prime(count):
    prime = []
    if count > 1:
        for i in range(1,count,1):
	        for x in range(2,i):
	            if i % x == 0:
	  	            break
	            else:
	                prime.append(i)

    return prime
print(prime(100))


def fibonacci(number):
    fnum=0
    snum=1
    
    seq=[]
    for i in range(number):
        if i <= 1:
            next_num=i
        else:
            next_num=fnum+snum
            fnum=snum
            snum=next_num
        seq.append(next_num)
	return seq
