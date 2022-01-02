def reversestr(s):
    if s=="":
        return s
    else:
        return reversestr(s[1:])+s[0]

print(reversestr("Hello"))
