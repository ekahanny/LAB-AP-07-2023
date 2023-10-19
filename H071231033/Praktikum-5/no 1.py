def mix_strings(s1, s2):
    s3 = ''
    len_s1 = len(s1)
    len_s2 = len(s2)
    for x in range(max(len_s1, len_s2)):
        if x < len_s1:
            s3 += s1[x]
        if x < len_s2:
            s2 = s2[::-1]
            s3 += s2[x]
    return s3

s1 = 'Abc'
s2 = '123'
print(mix_strings(s1, s2))
