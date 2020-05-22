import ndjson
import json
import numpy as np

INPUT_FILE='data/full_simplified_cat.ndjson'

with open(INPUT_FILE) as f:
    reader = ndjson.reader(f)
    line_number=0

    for line in reader:
        line_number += 1
        nparray= np.array(line['drawing'])
        print(nparray)
#         np.savetxt("converted/cat-{}".format(line_number),)

