def reverseWords():
    while True:
        nr = str(input())
        int_list = [int(i) for i in nr if i.isdigit()]
        if len(int_list) >= 1:
            print('error, rewrite!')
        else:
            reverse = nr[::-1]
            return reverse
        if nr == '':
            break


pr = reverseWords()
print(pr)







