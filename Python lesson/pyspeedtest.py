# import speedtest
#
# def test():
#     s = speedtest.Speedtest()
#     s.get_servers()
#     s.get_best_server()
#     s.download()
#     s.upload()
#     res = s.results.dict()
#     return res["download"], res["upload"], res["ping"],
# def main():
#     for i in range(1):
#         d, u, p =test()
#         print('Test #{}'.format(i+1))
#         print('Download: {:.2f} Mb/s'.format(d / 1024/1024))
#         print('Upload: {:.2f} MB/s\n'.format(u / 1024/1024))
#         print('Ping: {}\n'.format(p))
# lst = []
# import time
# lst.append(time.time())
# if __name__ == '__main__':
#     main()
# lst.append(time.time())
# print(lst[1]-lst[0])

#
# import pyspeedtest
#
# st = pyspeedtest.SpeedTest()
#
# print(st.download())

# for num in range(0,10):
#     if num <= 7:
#         print(num)
#     else:
#         break

# i = 0
# while i < 20:
#     if i < 15:
#         break
#     else:
#         print(i)
#         i += 1

# for num in range(0,5):
#     if num == 3:
#         print('Пропускаем 3')
#         continue
#
#     else:
#         print(num)

# for num in range(19):
#     if num == 15:
#         print('Акаары')
#         continue
#     else:
#         print(num)
#
# i = 0
# while i < 10:
#     i +=1
#     if i ==3:
#         print('Засссал на три')
#         continue
#     if i ==5:
#         print('Зассал на пять')
#     if i == 8:
#         print('Восемь мне не обойти')
#     else:
#         print(i)

# i = 4
# while i < 10:
#     i +=1
#     if i == 6:
#         print('6 мне не обойти')
#         continue
#     else:
#         print(i)


# for i in range(10):
#     if i == 4:
#         print('Четыре нам пофигу')
#         continue
#     else:
#         print(i)

# for i in range(10):
#     if i > 4:
#         pass
#     else:
#         print('Вывод на экран от 1 до 4:', i)

# while True:
#     pass

# list = {'milk': '', 'bread': 'v', 'pie': '', 'cherry': 'v,', 'cucumber': 'v', 'cheese': '', 'cream': ''}
# for k, v in list.items():
#     if v == 'v':
#         continue
#     print(k)

#
# l = {'bmw': '1', 'toyota': '2,', 'mersedes': '3', 'audi': '4'}
# for k, v in l.items():
#     print(k, v)

# list = 'Break and Continue operators'
# for i in range(0, len(list)):
#     if list[i] == 'x':
#         print(list[i])
#         break
#     print(list[i], end = '')

# word = 'выап вапв'
# for i in range(0, len(word)):
#     if word[i] == 'а':
#         print(word[i])
#         break
#     print(word[i], end = '')

# list = 'My mom and dad are the best)'
# for i in range(0, len(list)):
#     if list[i] == 'a':
#         print(list[i])
#         break
#     if i>0 and (i+1)%3 == 0:
#         continue
#     print(list[i], end = '')

# list = ['snow', 'rain', 'wind', 'sun', 'clouds']
# for i in list:
#     if len(i) < 3:
#         continue
#     print(i, end = ' ')
# print()
#
# word = ['sdaf', 'cad', 'tbgh', 'bn']
# for x in word:
#     if len(x) < 2:
#         continue
#     print(x, end=' ')
# print()

# name = input('name: ')
# password = input('password: ')
#
# while True:
#     if len(password)<8:
#         print('Too short password')
#     elif name in password:
#         print('Psw contains name')
#     else:
#         print('Password was set!')
#         break
#     password = input('Password: ')

# list = ['3sdf', 'sadf', 1, '1' ]
# for i in list:
#     if i == '1':
#         print('Все хорошо')
#     else:
#         pass

# for i in 'Hello world':
#     if i == "e":
#         print('Буква "Е" в строке есть')
#     else:
#         print('Буквы "а" в строке нет')
#
# for n in range(2,10):
#     for x in range(2,n):
#         if n%x ==0:
#             print(n, 'equals' , x, '* ', n//x)
#             break
#         else:
#             print(n, 'is a prime number')

car = {'bmw', 'toyota', 'mersedes', 'audi', 'Ud'}
for i in car:
    if len(i) < 3:
        print('yes')
else:
    print('No')