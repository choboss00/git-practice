def fizzbuzz(num):
    for i in range(1, num+1):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(f'{i}')

if __name__=='__main__':
    fizzbuzz(15)
