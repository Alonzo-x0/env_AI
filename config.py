import os

INPUT_DATASET = 'datasets/original'

BASE_PATH = 'datasets/idc'

#creates and organizes paths
TRAIN_PATH = os.path.sep.join([BASE_PATH, 'training'])
VAL_PATH = os.path.sep.join([BASE_PATH, 'validation'])
TEST_PATH = os.path.sep.join([BASE_PATH, 'testing'])


#percent of data to use
TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1