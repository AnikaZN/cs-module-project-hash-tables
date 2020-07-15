def no_dups(s):
    # Your code here
    string = []
    words = s.split()
    for word in words:
        if word not in string:
            string.append(word)
        else:
            pass
            
    return " ".join(string)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
