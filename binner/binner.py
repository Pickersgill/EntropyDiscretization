import numpy as np
import sys

# The data source, a list of integers classed based on there values, 1 is in the class of "1" etc...
data = [x[:-1] for x in open(sys.argv[1])]

# The cutoff point for recursion. Once entropy < 2 stop splitting
CUTOFF = 2

# Eponymous split function
def split(data, split_ind):
    return data[:split_ind], data[split_ind:]

# Returns entropy of given data portion
def entropy_of(Di):
    classes = set(Di)
    ent = 0

    for k in classes:
        pk = (1 /len(Di)) * Di.count(k)
        ent += pk * np.log2(pk)

    return -ent

# calculates information gain of given split based on entropy of un-split data portion
def information_gain_of(D, Di1, Di2):
    total_ent = entropy_of(D)

    # normalize entropy of splits:
    norm_ent_Di1 = (len(Di1) / len(D)) * entropy_of(Di1)
    norm_ent_Di2 = (len(Di2) / len(D)) * entropy_of(Di2)

    return total_ent - (norm_ent_Di1 + norm_ent_Di2)

# recursive function splitting data into bins based on maximal information gain
def find_bins(D):

    # check whether to stop recurring
    if entropy_of(D) <= CUTOFF:
        return [D]

    highest_gain = None
    highest_gain_ind = None
    
    # find highest gain
    for i in range(1, len(D)):
        split1, split2 = split(D, i)
        inf_gain = information_gain_of(D, split1, split2)
        if highest_gain == None or inf_gain > highest_gain:
            highest_gain = inf_gain
            highest_gain_ind = i

    # recur
    D1, D2 = split(D, highest_gain_ind)
    return find_bins(D1) + find_bins(D2)

# entry point function
def binnify(D):
    bins = find_bins(D)
    print("Created %d bins" % len(bins))
    print("Here is the binned dataset...")

    for b in bins:
        print(str(b), end=" | ")
    print()
    
binnify(data)

