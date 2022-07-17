# def body_mass_index(mass, height):
#     bmi = mass / (height * height)
#     if 18.5 < bmi < 25:
#         print("Оптимальная масса")
#     if bmi < 18.5:
#         print("Недостаточная масса")
#     if bmi > 25:
#         print("Избыточная масса")
#     return bmi
# #
# #
# print(body_mass_index(mass=int(input()), height=float(input())))

# def count_smth(a):
#     length = len(a)
#     main = length * 60
#     rubble = main // 100
#     kopeika = main % 100
#     print(f'{rubble} р. {kopeika} коп.')
#
#
# count_smth(a=str(input()))

# def count_word(a):
#     splitting = a.split()
#     return len(splitting)
#
# print(count_word(a=str(input())))


# def astrology(a):
#     years = {
#         0: 'Обезьяна', 1: 'Петух', 2: 'Собака', 3: 'Свинья', 4: 'Крыса', 5: 'Бык',
#         6: 'Тигр', 7: 'Заяц', 8: 'Дракон', 9: 'Змея', 10: 'Лошадь', 11: 'Овца'
#             }
#     main = a % 12
#     for key,values in years.items():
#         if main == key:
#             print(values)
#
# astrology(a=int(input()))

# def reverse(a):
#     if len(a) == 6:
#        sliced = a[0] + a[-5:][::-1]
#     else:
#         sliced = a[::-1]
#     return sliced
#
# print(int(reverse(a=str(input()))))

# print(f'{int(input()):,}')

# def joseph(n,k):
#     return 1 if n == 1 else (joseph(n - 1, k) + k - 1) % n + 1
#
# print(joseph(n=int(input()), k=int(input())))

# number = int(input())
# first, second, third, fourth = 0, 0, 0, 0
#
# for _ in range(number):
#     x, y = map(int, input().split())
#     first += x > 0 and y > 0
#     second += x < 0 and y > 0
#     third += x < 0 and y < 0
#     fourth += x > 0 and y < 0
#
# print(f"Первая четверть: {first}")
# print(f"Вторая четверть: {second}")
# print(f"Третья четверть: {third}")
# print(f"Четвертая четверть: {fourth}")


# def counting(a):
#     count = 0
#     b = a.split()
#     b = [int(i) for i in b]
#     for j in range(0, len(b) -1):
#         if b[j] < b[j+1]:
#             count+=1
#     return count
#
# print(counting(a=str(input())))

#
# def back_front(a):
#     b = a.split()
#     b = [int(i) for i in b]
#     c = [b[-1]] + b[:-1]
#     print([b[-1]])
#     return c
#
#
# sliced = back_front(a=str(input()))
# for i in sliced:
#     print(i, end=' ')]


# class Solution():
#     def countOdds(self, low: int, high: int) -> int:
#         count = 0
#         for i in range(low, high+1):
#             if i % 2 !=0:
#                 count += 1
#
#         return count
#
#
# s = Solution()
# lenght = s.countOdds(low=int(input()), high=int(input()))
# print(lenght)

# en = [list(int(i)) for i in input().split() for i in range(int(input()))]



# def task1(array):
#     dictionary = {}
#     splitted = [int(i) for i in array]
#     for i,j in enumerate(splitted):
#         if j < 1:
#             dictionary[i] = j
#     first_elem = next(iter(dictionary))
#     return first_elem
#
# print("Index of first element: ", task1(array=str(input())))





# import wikipedia
# import requests
# from bs4 import BeautifulSoup as bs
#
#
# r = requests.get("https://ru.wikipedia.org/w/index.php?"
#                  "title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F"
#                  ":%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5"
#                  "_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83")
# print(r.status_code)
#
# soup = bs(r.text, "html.parser")
# data = soup.find("div", class_='mw-category-group')
#
#
# print(data)
#     # get_title = i.split('=')
#
#     # print(get_title)



from datetime import datetime
list1 = []
a = {'data': {'lesson': [1594663200, 1594666800],
         'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
         'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
 'answer': 0
}
for i in a['data'].values():
    list1.append(i)

#transforming data for pupils and tutors
def transform_data(list, sec_time):
    for k in list:
        var = datetime.utcfromtimestamp(k)
        var_to_int = int(var.strftime('%S'))
        sec_time = sec_time + var_to_int
    return sec_time

pupils_tr = transform_data(list1[1], 0)
print("pupils", pupils_tr)
tutors_tr = transform_data(list1[2], 0)
print("tutors", tutors_tr)

total_sec = pupils_tr + tutors_tr
a['answer'] = total_sec + 3600
print(a)



if __name__ == '__main__':
   for i, test in enumerate(a):
       test_answer = transform_data(a['data'], 0)
       assert test_answer == a['answer'], f'Error on test case {i}, got {test_answer}, expected {a["answer"]}'



