
#import necessary libraries
from decimal import Decimal 
  
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 
    #end if
#end function

#take inputs for prime factors & text
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
no = int(input('Enter the value of text = ')) 

#calc n & t (t = O(n) above)
n = p*q 
t = (p-1)*(q-1) 
  

for e in range(2,t): 
    if gcd(e,t)== 1: 
        break
    #end if
#next e
  
  
for i in range(1,10): 
    x = 1 + i*t 
    if x % e == 0: 
        d = int(x/e) 
        break
    #end if
#next i

#calc cipher text
ctt = Decimal(0) 
ctt = pow(no,e) 
ct = ctt % n 
  
#decryption
dtt = Decimal(0) 
dtt = pow(ct,d) 
dt = dtt % n 
  
#print values to screen
print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt)) 