#Главная ветка
#6.1
string_6_1 = "Hello World!"
print(string_6_1[0])
print(string_6_1[-1])
print(string_6_1[6:11])

#6.2
string_6_2 = str(input("Введите строку: "))
if len(string_6_2)%2 == 0:
    print(string_6_2.upper())
else:
    print(string_6_2.lower())

#6.3
string_6_3 = str(input("Введите строку: "))
chars_6_3 = "aeiouAEIOU"
cnt_6_3 = 0
for i in string_6_3:
    if i in chars_6_3:
        cnt_6_3 += 1
print("Количество гласных букв в строке:", cnt_6_3)

#6.4
string_6_4 = str(input("Введите строку: "))
result_6_4 = ""
for i in range(len(string_6_4)):
    if i == 0 or string_6_4[i] != string_6_4[i-1]:
        result_6_4 += string_6_4[i]
print(result_6_4)

#6.5
string_6_5_1 = str(input("Введите первое слово: "))
string_6_5_2 = str(input("Введите второе слово: "))
answer_6_5 = False
if sorted(string_6_5_1.lower()) == sorted(string_6_5_2.lower()):
    answer_6_5 = True
print(answer_6_5)