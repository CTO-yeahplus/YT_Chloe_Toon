timing = []
caption = []
cap_dict = {}

f = open("/Users/eugeneko/Documents/dev/YT_Chloe_Toon/TOON_cap/TOON_timing.sbv", 'r')
lines = f.readlines()
for line in lines:
    timing.append(line.strip())
    #print(line)
f.close()

f = open("/Users/eugeneko/Documents/dev/YT_Chloe_Toon/TOON_cap/TOON_cap_new.txt", 'r')
cap_lines = f.readlines()
for line in cap_lines:
    if line:
        caption.append(line.strip())
    #print(line)
f.close()
print ('CAPTION\n\n',caption,'\n\n')

#print (len(timing), len(caption))
for i,item in enumerate(timing):
    print(i, item)
    if item:
        cap_dict[item]=caption[i]

f=open("/Users/eugeneko/Documents/dev/YT_Chloe_Toon/TOON_cap/TOON_cap_done.txt", 'w')

print(cap_dict)
for k in cap_dict.keys():
    f.write(k)
    f.write('\n')
    f.write(cap_dict[k])
    f.write('\n\n')

f.close()


