
""" ------------ task1 ----------------"""
def task1(array):
    dictionary = {}
    splitted = [int(i) for i in array]
    for i,j in enumerate(splitted):
        if j < 1:
            dictionary[i] = j
    first_elem = next(iter(dictionary))
    return first_elem

print("Index of first element: ", task1(array=str(input())))




""" ------------ task3 ----------------"""


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
