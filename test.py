sbpm = 60
ebpm = 200
diff = ebpm - sbpm

diff = (ebpm-sbpm)/20

for x in range(21):
    #print(ebpm-sbpm)
    #print(sbpm + diff*x)
    print(60_000/sbpm, 60_000/ebpm)
    print(60_000/(sbpm+diff*x))