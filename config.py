import os


fLocation = input('Manually input directory or hit space for default dataset directory: ')

if fLocation == ' ':
	INPUT_DATASET = 'datasets/original'

else:
	INPUT_DATASET = fLocation	

print(INPUT_DATASET)
BASE_PATH = 'datasets/idc'

#creates and organizes paths
TRAIN_PATH = os.path.sep.join([BASE_PATH, 'training'])
VAL_PATH = os.path.sep.join([BASE_PATH, 'validation'])
TEST_PATH = os.path.sep.join([BASE_PATH, 'testing'])

#TODO
#Ask for user input from terminal line for location to datasets


#percent of data to use
TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1