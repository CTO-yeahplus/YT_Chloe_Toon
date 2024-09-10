timing = []
caption = []
cap_dict = {}

f = open("/Users/eugeneko/Documents/dev/YT_Chloe_caption/captions_timing.txt", 'r')
lines = f.readlines()
for line in lines:
    timing.append(line)
    print(line)
f.close()

f = open("/Users/eugeneko/Documents/dev/YT_Chloe_caption/cap_new.txt", 'r')
cap_lines = f.readlines()
for line in cap_lines:
    caption.append(line.strip())
    #print(line)
f.close()

#print (len(timing), len(caption))

for i,item in enumerate(timing):
    try:
        if i < 2 :
            cap_dict[item]=caption[i]
        else:
            cap_dict[item]=caption[i-1]

    except:
        pass

f=open("/Users/eugeneko/Documents/dev/YT_Chloe_caption/cap_done.txt", 'w')

for k in cap_dict.keys():
    f.write(k)
    f.write(cap_dict[k])
    f.write('\n\n')
    print (k,cap_dict[k])
f.close()
