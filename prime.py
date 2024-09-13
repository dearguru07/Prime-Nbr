# def Prime(n):
#     tem=True
#     er=n//2
#     for i in range(1,er+1):
#         if n%i==0:
#             tem=False
#     if tem==True:
#         print('prime number')        
#     else:
#         print('not a prime')    
# n=int(input('Enter a number'))        
# Prime(n)



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input('Enter a number: '))
if is_prime(n):
    print('Prime number')
else:
    print('Not a prime number')