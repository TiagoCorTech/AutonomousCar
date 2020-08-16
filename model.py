import csv
#import cv2
import numpy as np
from scipy import ndimage


lines = []
with open('recData/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)
        
images = []
measurements = []
for line in lines :
    for i in range(3):
        
        if i == 0 :
            correction = 0
        elif i == 1:
            corection = 0.075
        else :
            correction = -0.075
        #Normal Images 
        image = ndimage.imread(line[i])
        measurement = float(line[3]) + correction
        images.append(image)
        measurements.append(measurement)
        
        #Flipped Images
        image_flipped = np.fliplr(image)
        measurement_flipped = -measurement
        images.append(image_flipped)
        measurements.append(measurement_flipped)
        
        
        
X_train = np.array(images)
Y_train = np.array(measurements)


from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, AveragePooling2D, Cropping2D, Dropout
from keras.layers.convolutional import Conv2D

model = Sequential()
model.add(Cropping2D(cropping=((50,20), (0,0)), input_shape=(160,320,3)))
model.add(Lambda(lambda x: x/255.0 - 0.5))
model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu'))
model.add(AveragePooling2D())
model.add(Dropout(0.3))
model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu'))
model.add(AveragePooling2D())
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(units=120, activation='relu'))
model.add(Dense(units=84, activation='relu'))
model.add(Dense(1))


model.compile(loss='mse',optimizer='adam')
model.fit(X_train, Y_train, validation_split = 0.2, shuffle=True, epochs=3)

model.save('model.h5')
exit()



