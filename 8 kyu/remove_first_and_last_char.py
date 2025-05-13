def slice(str):
    if len(str) < 3:
        return str
    str = str[1:len(str)-1]
    print(str)
    return str


slice('hello')