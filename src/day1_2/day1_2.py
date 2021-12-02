from sys import argv
with open(argv[len(argv)-1]) as fp : 
    entrada = list(map(int, fp.read().splitlines()))
    dif = [(entrada[i]+entrada[i+1]+entrada[i+2]) for i in range(len(entrada)) if i+2 < len(entrada)]
    print(sum([((dif[1:] + [0])[i] - dif[i]) > 0 for i in range(len(dif))]))
