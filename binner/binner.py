import numpy as np
from binner import graph
import sys

Graph = graph.Graph

# The data source, a list of integers classed based on there values, 1 is in the class of "1" etc...
data = [tuple(x[:-1].split(", ")) for x in open(sys.argv[1])]

entropy_series = []
norm_entropy_series = []

# The cutoff point for recursion. Once entropy < 2 stop splitting
CUTOFF = 2
BIN_AMOUNT = 200

# Eponymous split function
def split(data, split_ind):
    return data[:split_ind], data[split_ind:]

# Returns entropy of given data portion
def entropy_of(Di):
    class_list = [x[-1] for x in Di]
    class_space = set(class_list)
    ent = 0

    for k in class_space:
        pk = (1 /len(class_list)) * class_list.count(k)
        ent += pk * np.log2(pk)

    return -ent

# calculates information gain of given split based on entropy of un-split data portion
def information_gain_of(D, Di1, Di2):
    total_ent = entropy_of(D)

    # normalize entropy of splits:
    norm_ent_Di1 = (len(Di1) / len(D)) * entropy_of(Di1)
    norm_ent_Di2 = (len(Di2) / len(D)) * entropy_of(Di2)

    return total_ent - (norm_ent_Di1 + norm_ent_Di2)

def replace(array, ind, replacement):
    return array[:ind] + replacement + array[ind + 1:]

def highest_gain_of(Di):
    highest_gain = None
    highest_gain_ind = None
    
    # find highest gain
    for i in range(1, len(Di)):
        split1, split2 = split(Di, i)
        inf_gain = information_gain_of(Di, split1, split2)
        if highest_gain == None or inf_gain > highest_gain:
            highest_gain = inf_gain
            highest_gain_ind = i

    return highest_gain_ind

# find bins by splitting the bin with the highest entropy until you have a specified number of bins
def find_bins_using_split_highest_entropy(D, graph=None):
    bins = [D]
    
    while len(bins) <= BIN_AMOUNT:
        highest_ent = None
        worst_bin_ind = None

        for i in range(len(bins)):
            b = bins[i]
            ent = entropy_of(b)
            if highest_ent == None or ent > highest_ent:
                highest_ent = ent
                worst_bin_ind = i
    
        worst_bin = bins[worst_bin_ind]
        split1, split2 = split(worst_bin, highest_gain_of(worst_bin))
        bins = replace(bins, worst_bin_ind, [split1, split2])
    
        if graph:
            graph.add_to_series(sum(map(entropy_of, bins)))

    return bins
    
# recursive function splitting data into bins based on maximal information gain until a cutoff entropy level
# is reached
def find_bins_using_entropy_cutoff(D):

    # check whether to stop recurring
    if entropy_of(D) <= CUTOFF:
        return [D]

    highest_gain_ind = highest_gain_of(D)

    # recur
    D1, D2 = split(D, highest_gain_ind)
    return find_bins_using_entropy_cutoff(D1) + find_bins_using_entropy_cutoff(D2)

# entry point function
def binnify(D):
    # bins = find_bins_using_entropy_cutoff(D)
    graph = Graph()
    bins = find_bins_using_split_highest_entropy(D, graph)
    graph.show()
    
    
binnify(data)

