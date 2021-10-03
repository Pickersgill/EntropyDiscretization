# EntropyDiscretization
Discretization of data set based on minimizing entropy.

# Usage

Give the source dataset in plaintext format where each row (line) is a comma seperated list of the attributes.
It is assumed that the final entry on each line is the label. E.g:

```rubiks_cube 4 4 2```

This row shows a data object with attributes (rubiks_cub, 4, 4) and label 2.

If you want to change or re-generate the source data it may be helpful to use:
```dataset/gen_nums.py```

Run the program with:
```
python3 run.py dataset/my_data_set
```

After running the program will show 2 graphs, one showing total entropy for the dataset and another showing
the "normalized" entropy, total entropy divided by number of bins.

Change the BIN_AMOUNT constant in ```binner/binner.py``` to determine how many bins will be created.

# Observations

- Setting BIN_AMOUNT equal to the number of data objects will always result in total entropy 0 as each bin
    will be entirely pure containing only 1 item.

- Total entropy tends to increase until approaching n/2 bins (where n is number of data objects) and 
    approaching 0.

- Normalized entropy tends to decrease after each iteration (which I imagine is the desired effect).






