import xmltodict
import h5py
import numpy as np


def parseXML(xml_f):
	with open(xml_f, 'r') as f:
		d = xmltodict.parse(f.read())
		anno = d['annotation']
		width = anno['size']['width']
		height = anno['size']['height']
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
	return m, width, height


def xml2h5(xmls, dst):
	with open(xmls, 'r') as f:
		try:
			while True:
				line = f.next().strip()
				filename = line.split('/')[-1]
				newpath = "{}/{}".format(dst, filename.strip("xml") + "h5")
				m, _, _ = parseXML(line)
				with h5py.File(newpath, 'w') as h5:
					for label, bbs in m.items():
						h5.create_dataset(label, data=np.array(bbs, dtype=np.int32))
		except StopIteration:
			pass


if __name__ == '__main__':
	import sys
	import os

	if len(sys.argv) == 1:
		print "python .. xmls dst"
		sys.exit(0)

	xmls = sys.argv[1]
	dst = sys.argv[2]

	if os.path.exists(dst):
		print "dst exists!"
		sys.exit(0)
	os.mkdir(dst)

	xml2h5(xmls, dst)
