num = input(str('vui long nhap 2 nguyen: '))
x = num.split()
a = int(x[0])
b = int(x[1])
print('so nguyen bat dau la:',a)
print('so nguyen ket thuc la:',b)
while b < a:
    num = input('vui long nhap lai so ket thuoc lon hon so bat dau: ')
    x = num.split()
    a = int(x[0])
    b = int(x[1])
    print('so nguyen bat dau la:',a)
    print('so nguyen ket thuc la:',b)
else:
    for i in range(a,b+1):
        if i%3 == 0 and i%5 == 0 :
            print('Fizz Buzz')
        elif i % 3 == 0:
                print('Fizz')
        elif i % 5 == 0:
                print('Buzz')
        else:
            print(i) 
