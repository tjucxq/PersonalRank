#coding=utf-8

def PersonalRank(G, alpha, root, max_step):
    rank = dict()
    rank = {x:0 for x in G.keys()}
    rank[root] = 1
    #start iteration
    for k in range(max_step):
        tmp = {x:0 for x in G.keys()}
        #get node i and i's out edges set ri
        for i, ri in G.items():
            #get node i's edges and its weight
            for j, wij in ri.items():
                tmp[j] += alpha * rank[i] / (1.0*len(ri))

        tmp[root] += (1 - alpha)
        rank = tmp

        print 'iter: ' + str(k) + "\t",
        for key, value in rank.items():
            print "%s:%.3f, \t"%(key, value),
        print

    return rank

if __name__ == "__main__":
    G = {'A' : {'a':1, 'c':1},
         'B' : {'a':1, 'b':1, 'c':1, 'd':1},
         'C' : {'c':1, 'd':1},
         'a' : {'A':1, 'B':1},
         'b' : {'B':1},
         'c' : {'A':1, 'B':1, 'C':1},
         'd' : {'B':1, 'C':1}}
    PersonalRank(G, 0.85, 'A', 100)