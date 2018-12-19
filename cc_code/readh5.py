import os
import h5py

with h5py.File('/home/chencheng/data/base_35000/0098380.h5','r') as f:
    print(f.keys())
    print(f['person_upper'])

print(0)
