def reverseWords(nr):
        for i in nr:
            if i.isdigit():
                return False
            else:
                return nr[::-1]


pr = reverseWords(nr=str(input()))
print(pr)






