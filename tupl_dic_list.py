name = input("Enter file:")
time_stamp = list()
strng_lst = list()
sent = " "
a_lst = list()
dict_lst = list()
time_dict = dict()
c = list()
#if len(name) > 1 : name = "mbox-short.txt":
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith('From'):
                continue
    words = line.split()
    time_stamp = words[5:6]
    for i in time_stamp:
        strng_lst.append(i)             
for ll in range(len(strng_lst)):
    sent = sent + " " + strng_lst[ll] 
hrs_lst = sent.split()
for h in hrs_lst:
    h_lst = h.split(':')
    a_lst.append(h_lst)
for i in a_lst:
    dict_lst.append(i[0])
for i in dict_lst:
    time_dict[i] = time_dict.get(i,0)+1
for k,v in time_dict.items():
    c.append((k,v))
c = sorted(c)
for k,v in c:
    print(k,v)
            