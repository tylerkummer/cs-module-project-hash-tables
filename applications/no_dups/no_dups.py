from collections import Counter


def no_dups(s):
    # Your code here
    word_list = s.split(" ")

    for i in range(0, len(word_list)):
        word_list[i] = "".join(word_list[i])

    count = Counter(word_list)

    word_list = " ".join(count.keys())
    return(word_list)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
