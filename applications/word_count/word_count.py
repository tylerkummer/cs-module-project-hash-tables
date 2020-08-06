def word_count(s):
    # Your code here
    count = {}
    word_list = s.lower().split()

    for word in word_list:
        word_strip = word.strip('" : ; , . - + = / \ | [ ] { } ( ) * ^ &')

        if word_strip == '':
            return {}
        elif word_strip in count:
            count[word_strip] += 1
        else:
            count[word_strip] = 1

    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
