# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:50:53 2020

@author: josep
"""
from pyvis.network import Network
from networkx.algorithms import community
import networkx as nx
import pandas as pd
import itertools

colors = pd.read_csv("L:\\Github Repos\\playground\\Graph\\sciencesNodes.csv")
print(colors.loc[colors['node'] == 'supernatural', 'color'].values[0])

def getColor(id):
    print(colors.loc[colors['node'] == id, 'color'].values[0])
    return colors.loc[colors['node'] == id, 'color'].values[0]

got_net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", heading=("Top Community"))

# set the physics layout of the network
#got_net.barnes_hut()
got_data = pd.read_csv("L:\\Github Repos\\playground\\Graph\\sciences.csv")

sources = got_data['from']
targets = got_data['to']
weights = got_data['weight']

edge_data = zip(sources, targets, weights)
# edge_data2 = zip(sources, targets)
# edge_data3 = zip(sources, targets)

# G =nx.from_pandas_edgelist(got_data,'from','to')
# print(G.number_of_nodes())

# topComm = None
# comp = nx.algorithms.community.centrality.girvan_newman(G)

# topComm = None
# comp = nx.algorithms.community.centrality.girvan_newman(G)
 
# sample code for using the girvan_newman calc
# k = 3
# for i in range(k):
#     print(i)
#     # keep getting the next set of communities
#     # at the ith split
#     kthLevel = next(comp)
# counts = {}
# for e in edge_data2:
#     counts[e[0]] = 0
#     counts[e[1]] = 0
 
# for e in edge_data3:
#     counts[e[0]] = counts[e[0]] + 1
#     counts[e[1]] = counts[e[1]] + 1

# numConnections = sorted(counts.values(), reverse=True)

# sumCount = 0
# for con in numConnections:
#     if con<5:
#         sumCount += 1

# print(sumCount)

for e in edge_data:
    src = str(e[0])
    dst = str(e[1])
    edg = e[2]
    got_net.add_node(dst, dst, title=dst, color=getColor(dst))
    got_net.add_node(src, src, title=src, color=getColor(src))
    got_net.add_edge(dst, src, value=edg)
    # if((counts[e[0]] > 200) or (counts[e[1]] > 200)):
    #     # only the top 13 nodes have over 200 connections
    #     got_net.add_edge(src, dst, value=1)

        

    # flag = True
    # for i in range(k+1):
    #     for j in range(k+1):
    #         if(i == j):
    #             continue
            
    #         if(src in kthLevel[i] and dst in kthLevel[j]):
    #             flag = False
            
    #         if(not flag):
    #             break
 
    #     if(not flag):
    #         break
 
 
    # if(flag):
    #     #print("FOUND")
    #     got_net.add_edge(src, dst, value=1)
 
neighbor_map = got_net.get_adj_list()
 
# add neighbor data to node hover data
for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])
 
    
got_net.show_buttons(filter_=['physics'])
got_net.show("alpha_testes.html")
