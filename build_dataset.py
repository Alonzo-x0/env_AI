import config
import imgTool
import random, shutil, os
from datetime import datetime
startTime = datetime.now()


#checks INPUT_DATASET path tree for any images
originalPaths = list(imgTool.list_images(config.INPUT_DATASET))

#seed randomizes based on the input and system time
#shuffle shuffles the list provided
random.seed(7)
random.shuffle(originalPaths)


#index multiplies the length of the tree by the TRAIN_SPLIT defined in config, in this case
#80% percent
index=int(len(originalPaths)*config.TRAIN_SPLIT)

#takes the multiplied percentage length from earlier to 
#create a list based off previous percent
trainPaths  = originalPaths[:index]
testPaths = originalPaths[index:]

index = int(len(trainPaths)*config.VAL_SPLIT)
valPaths = trainPaths[:index]

trainPaths = trainPaths[index:]

#organized in 3s to be used later in next for loop
datasets = [('training', trainPaths, config.TRAIN_PATH),
			('validation', valPaths, config.VAL_PATH),
			('testing', testPaths, config.TEST_PATH)]


for (setType, originalPaths, basePath) in datasets:
	print(f'Building {setType} set')

	if not os.path.exists(basePath):
		print(f'Building directory {config.BASE_PATH}')
		#looks for directory base path from config
		#makes it if not found
		os.makedirs(basePath)

	for path in originalPaths:
		file = path.split(os.path.sep)[-1]
		#splits list to get last element, an img file
		#ex: ['datasets/original', '12878', '0', '12878_idx5_x2151_y2951_class0.png']
		label = file[-5:-4]
		#done to get the 0 or 1 at the end of img ex:class0.png

		#basepath is training, label is 1 or 0
		#creates datasets/idc\training\0
		labelPath = os.path.sep.join([basePath, label])
		if not os.path.exists(labelPath):
			print(f'Building directory {labelPath}')
			os.makedirs(labelPath)

		newPath = os.path.sep.join([labelPath, file])
		#output is datasets/idc\training\0\10253_idx5_x601_y851_class0.png where
		#the img is file, and to the left is labelPath
		#print(path, newPath)
		shutil.copy2(path, newPath)
print('done')
print(datetime.now()-startTime)