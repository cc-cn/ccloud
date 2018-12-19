import cPickle as pickle  
f = open('voc_2007_trainval_gt_roidb.pkl')  
info = pickle.load(f)  
print info[:10]
