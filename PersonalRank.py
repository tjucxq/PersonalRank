#coding=utf-8

def PersonalRank(G, alpha, root, max_step):
    rank = dict()
    rank = {x:0 for x in G.keys()}
    rank[root] = 1
    #start iteration
    for k in range(max_step):
        tmp = {x:0 for x in G.keys()}

