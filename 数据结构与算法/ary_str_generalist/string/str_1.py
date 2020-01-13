# s = str('hello')
# print(s.split('e'))
# print(s.count('l'))
# print(s.title())
# print(s.encode('gbk'))
# print('/'.join(s))
# print(s.replace('l', 'tt', 1))
# print(s.capitalize())
# print(s.center(10, '*'))
# print(s.find('o'))
# print(s.strip('e'))
# print('---------')
# print(s.expandtabs(6))
# print(s.lstrip('ppp'))
# print(s.partition('l'))
# print(s.rindex('l'))
#
# s = 'abc12d12ef12gh'
# print(s.replace('12', '34'))
# print(s.find('12'))


def sub_str(string, start, len_):
    if start > len(string) or start < 0 or len_ < 1 or len_ >= len(string):
        print('你看不见吧<>')
    else:
        if start + len_ >= len(string):
            sub = string[start:]
        else:
            i = 0
            sub = ''
            while i < len_:
                sub += string[start]
                i += 1
                start += 1
        return sub


def find_str(string, example):
    i = j = 0
    while i < len(string) and j < len(example):
        if string[i] == example[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == len(example):
        return i - j
    else:
        return False


def max_sub(string1, string2):
    i = k = 0
    n1, n2 = len(string1), len(string2)
    max_, ad = 0, 0

    while i < n1:
        j = 0
        while j < n2:
            if string1[i] == string2[j]:
                k = 1
                while i+k < n1 and j+k < n2:
                    if string1[i+k] == string2[j+k]:
                        k += 1
                    else:
                        break
                if k > max_:
                    ad = i
                    max_ = k
                j += k
            else:
                j += 1
        i += 1

    i, j, res = ad, 0, ''
    while j < max_:
        res += string1[i]
        i += 1
        j += 1
    print(res)


def digit_str(string):
    len_ = i = start = 0
    while i < len(string):
        x = string[i]
        if '0' <= x <= '9':
            count = 0
            ad = i
            while '0' <= x <= '9':
                count += 1
                i += 1
                x = string[i]
            if count > len_:
                len_ = count
                start = ad
        else:
            i += 1
    print(string[start:start+len_], len_, start, sep='****')


# print(sub_str('string', 6, 4))
# print(find_str('string', 'tr'))
# max_sub('hello world.', 'this is a world, how old')

# string = 'abc12345ed126ss123456789ts'
# digit_str(string)

# print(repr('b'))


def center_sym(string):
    i, j = 0, len(string)-1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


# print(center_sym('abba'))

def rear_range_str(string):
    i, j = 0, 1
    res1 = ''
    while i < len(string):
        res1 = string[i] + res1
        i += 2
    res2 = ''
    while j < len(string):
        res2 = res2 + string[j]
        j += 2
    return res2 + res1


# print(rear_range_str('ABCDEFGHIJKL'))


def pattern(string, matching, start):
    n1, n2 = len(string), len(matching)
    if n1-n2-start < 0:
        print('参数不符合要求')
        return -1
    i, j, s = start, 0, 0
    while i < n1 and j < n2:
        if string[i] == matching[j]:
            i += 1
            j += 1
        elif matching[j] == '*':
            i += 1
            j += 1
        else:
            i = i-j+1
            s = i
            j = 0
    if j >= n2:
        return s
    print('匹配失败')
    return -1


# print(pattern('hello python', '*p', 0))


print('i' in 'pin')
