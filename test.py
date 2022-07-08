# def body_mass_index(mass, height):
#     bmi = mass / (height * height)
#     if 18.5 < bmi < 25:
#         print("Оптимальная масса")
#     if bmi < 18.5:
#         print("Недостаточная масса")
#     if bmi > 25:
#         print("Избыточная масса")
#     return bmi
#
#
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




en = [list(int(i)) for i in input().split() for i in range(int(input()))]

















