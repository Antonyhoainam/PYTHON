def demnguyenam(s):
    dem = 0
    b = False
    for i in range(len(s)):
        if s[i]== 'u'or s[i] == 'e' or s[i] == 'o' or s[i]=='a' or s[i]=='i':
            dem = dem + 1
            if dem >= 3:
                return s
s = "Ah meta descriptions… the last bastion of traditional marketing! The only cross-over point between marketing and search engine optimisation! The knife edge between beautiful branding and an online suicide note!"
chuoi = s.split()
c = []
c = list(filter(lambda x: demnguyenam(x),chuoi))
print(c)