import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np
import os
with open('img_list', 'r') as f:
    lines = f.readlines()
for line in lines:
    img_id=line.strip().split()[0]
    img_gt=os.path.join('%s%s' %('/Users/ccmac/compare_preds/groundtruth/',img_id))
    #img_hyy=os.path.join('%s%s' %('/Users/ccmac/compare_preds/result_2/hyy_det/',img_id))
    #img_zdb=os.path.join('%s%s' %('/Users/ccmac/compare_preds/result_2/zdb_det/',img_id))
    img_cc=os.path.join('%s%s' %('/Users/ccmac/compare_preds/result_3/cc_det/',img_id))
    np_gt=mpimg.imread(img_gt)
    np_cc=mpimg.imread(img_cc)
    
    plt.figure(figsize=(15,8))

    plt.subplot(211)
    plt.imshow(np_gt) 
    plt.title("gt")
    plt.axis('off') 

    plt.subplot(212)
    plt.imshow(np_cc) 
    plt.title("cc")
    plt.axis('off') 
    
    plt.savefig('combine_3/%s' %img_id)
    plt.clf()
    #plt.close('all')
