from sys import argv
with open(argv[len(argv)-1]) as fp : 
    entrada = list(map(int, fp.read().splitlines()))
    print(sum([((entrada[1:] + [0])[i] - entrada[i]) > 0 for i in range(len(entrada))]))
    