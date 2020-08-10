name = input("Enter file:")
# name and count will be key and val of dict
count = dict()
max_count = 0

#"mbox-short.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    list_line = line.split()
    sender_name = list_line[1]
    count[sender_name] = count.get(sender_name,0)+1
#print(count)
max_sender = None

max_count = None
for sndr,cont in count.items():
    if max_count is None or cont > max_count:
        max_sender = sndr
        max_count = cont
        
print(max_sender,max_count)