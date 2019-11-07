from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import SeparableConv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K
#import tensorflow.keras.backend as K


'''Daftpunker1'''

class CancerCore:
	@staticmethod
	def build(width, height, depth, classes):
		model = Sequential()
		#initializes models
		shape=(height, width, depth)
		channelDim = -1
		#shape of image
		#WxH of pic, RGB channel (3), number of classes is 1 or 0 from pics (2)

		if K.image_data_format() == 'channels_first':
			shape = (depth, height, width)
			channelDim = 1
		
		print(len(shape))
		#32 = number of output filters in conv, input_shape = 3D tensor
		#padding = same to add 0 padding aka padding input == output
		model.add(SeparableConv2D(32, (3, 3), padding = 'same', input_shape = shape))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis = channelDim))
		model.add(MaxPooling2D(pool_size=(2, 2)))
		model.add(Dropout(0.25))

		model.add(SeparableConv2D(64, (3, 3), padding = 'same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis = channelDim))
		model.add(SeparableConv2D(64, (3, 3), padding = 'same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis = channelDim))
		model.add(MaxPooling2D(pool_size = (2, 2)))
		model.add(Dropout(0.25))

		model.add(SeparableConv2D(128, (3, 3), padding = 'same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis = channelDim))
		model.add(SeparableConv2D(128, (3, 3), padding = 'same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis = channelDim))
		model.add(SeparableConv2D(128, (3, 3), padding = 'same'))
		model.add(Activation('relu'))
		model.add(BatchNormalization(axis = channelDim))
		model.add(MaxPooling2D(pool_size = (2, 2)))
		model.add(Dropout(0.25))

		model.add(Flatten())
		model.add(Dense(256))
		model.add(Activation('relu'))
		model.add(BatchNormalization())
		model.add(Dropout(0.5))

		model.add(Dense(classes))
		model.add(Activation('softmax'))

		return model


