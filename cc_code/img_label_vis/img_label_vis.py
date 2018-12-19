import numpy as np
import h5py as h5
import copy
import xmltodict
import cv2
import sys
import os

_classes=['person_upper', 'person_head']
_class_to_ind={'person_upper':0, 'person_head':1}

#_class_to_ind = dict(zip(self._classes, xrange(self.num_classes)))

def load_gt(label_path):
		
	bbs_all = np.zeros((0, 4), dtype=np.float32)
	gt_classes = np.zeros((0), dtype=np.float32)
	label_path = label_path.strip()
	if label_path.endswith(".h5"):
		with h5.File(label_path, 'r') as f:
			for cls in f.keys():
				if cls not in _classes:
					continue
				bbs = f[cls][...]
				if bbs.size == 0:
					continue
				bbs[:, 2] = bbs[:, 0] + bbs[:, 2] - 1
				bbs[:, 3] = bbs[:, 1] + bbs[:, 3] - 1
				bbs_all = np.vstack((bbs_all, bbs))
				gt_classes = np.hstack(
					(gt_classes, np.ones(len(bbs)) * _class_to_ind[cls]))
	if label_path.endswith(".txt"):
                with open(label_path, 'r') as f:
			boxes=f.readlines()
                        for box in boxes:
				box=box.strip().split()
				if len(box)<5:
                                        continue
				box=np.array([int(box[0]), int(box[1]),int(box[2]),int(box[3]),int(box[4]),float(box[5])])
                                bbs = box[1:5]
                                bbs[2] = bbs[0] + bbs[2] - 1
                                bbs[3] = bbs[1] + bbs[3] - 1
				bbs=bbs.reshape(1,-1)
                                bbs_all = np.vstack((bbs_all, bbs))
                                gt_classes = np.hstack((gt_classes, box[0]%2))

	if label_path.endswith(".xml"):
                with open(label_path, 'r') as f:
                        d = xmltodict.parse(f.read())
                        anno = d['annotation']
                        objs = anno['object']
                        m = {}
                        if not isinstance(objs, list):
                                objs = [objs]
                        for obj in objs:
                                label = obj['name']
                                box = obj['bndbox']
                                x1 = box['xmin']
                                y1 = box['ymin']
                                x2 = box['xmax']
                                y2 = box['ymax']
                                bb = [x1, y1, x2, y2]
                                bb = [int(x) for x in bb]
                                if m.has_key(label):            
                                        m[label].append(bb)
                                else:
                                        m[label] = [bb]
                        for cls in m.keys():
                                if cls not in _classes:
                                        continue
                                bbs = np.array(m[cls])
                                if bbs.size == 0:
                                        continue
                                bbs_all = np.vstack((bbs_all, bbs))
                                gt_classes = np.hstack(
                                        (gt_classes, np.ones(len(bbs)) * _class_to_ind[cls]))



	assert len(bbs_all) == len(gt_classes), "bbs, gt_classes len differ!"
	return bbs_all, gt_classes


def vis_detections(im, gt_classes, bbs_all):
	window = "gt"
	cv2.namedWindow(window)
	im = im.copy()
	num = len(gt_classes)
	class_color = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

	for i in xrange(num):
		bbox = bbs_all[i, :]
		bbox = [int(x) for x in bbox]
		color = class_color[int(gt_classes[i])]
		cv2.rectangle(im, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
		info = ""
		cv2.putText(im, info, (bbox[0], bbox[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
	cv2.imshow(window, im)
	key = cv2.waitKey()
        if key == 27 or key== -1:
                sys.exit(0)





if len(sys.argv)!=2:
	print('tips : python img_label_vis img_label_path')
	exit()
img_label=sys.argv[1]
with open(img_label, 'r') as f:
	lines = f.readlines()

for line in lines:
	img = line.strip().split()[0]
	label = line.strip().split()[1]
	im = cv2.imread(img)

	bbs_all, gt_classes=load_gt(label)

	vis_detections(im, gt_classes, bbs_all)
