def reverseWords(nr):
        while True:
            if nr.isdigit():
                return False
            else:
                return nr[::-1]

pr = reverseWords(nr=str(input()))
print(pr)






