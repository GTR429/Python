import random

def khoitao():
    digits = set()
    while len(digits) < 4:
        digits.add(random.randint(0, 9))
    return list(digits)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


unique_digits = khoitao()
tries=0
a,b,c,d = unique_digits
true_t=0
n=input('Nhập số: ')
while (not is_number(n)) or len(n)!=4 or n[0]==n[1] or n[0]==n[2] or n[0]==n[3] or n[1]==n[2] or n[1]==n[3] or n[2]==n[3]:
    n=input('Nhập lại số có 4 chữ số: ')
#kiểm tra
while true_t!=4:
    tries+=1
    true_t=0 
    true_w=0
    while (not is_number(n)) or len(n)!=4 or n[0]==n[1] or n[0]==n[2] or n[0]==n[3] or n[1]==n[2] or n[1]==n[3] or n[2]==n[3]:
        n=input('Nhập lại số có 4 chữ số: ')
    if n[0]==str(a): 
        true_t+=1
    else:
        if n[0]==str(b): 
            true_w+=1
        if n[0]==str(c): 
            true_w+=1
        if n[0]==str(d): 
            true_w+=1
   
    if n[1]==str(b): 
        true_t+=1
    else:
        if n[1]==str(a): 
            true_w+=1
        if n[1]==str(c): 
            true_w+=1
        if n[1]==str(d): 
            true_w+=1

    if n[2]==str(c): 
        true_t+=1
    else:
        if n[2]==str(b): 
            true_w+=1
        if n[2]==str(a): 
            true_w+=1
        if n[2]==str(d): 
            true_w+=1

    if n[3]==str(d): 
        true_t+=1
    else:
        if n[3]==str(b): 
            true_w+=1
        if n[3]==str(c): 
            true_w+=1
        if n[3]==str(a): 
            true_w+=1
    
    print(true_t)
    print(true_w)
    if true_t!=4: 
        n=input('Nhập lại số: ')
    else:
        print('You win!')
        print('About '+str(tries)+' tries')
