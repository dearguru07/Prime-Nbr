def Prime(n):
    tem=True
    er=n//2
    for i in range(1,er+1):
        if n%i==0:
            tem=False
    if tem==True:
        print('prime number')        
    else:
        print('not a prime')    
n=int(input('Enter a number'))        
Prime(n)