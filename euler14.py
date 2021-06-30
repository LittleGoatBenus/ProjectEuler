
temp = 0
long = 0
running = True
seqlen = 0

for i in range(13, 100):

    while running:
        if (i % 2) == 0:
            i = i/2
        else:
            i = (i*3)+1

        if i == 1:
            running = False

        seqlen += 1

    sequencelen = seqlen+1

    if sequencelen > long:
        print(sequencelen)
        long = sequencelen
    else:
        print(long)
