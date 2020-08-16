# **Behavioral Cloning** 

## Writeup Template

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

All the files are included

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

- I based my architecture from the LeNet model. 

#### 2. Attempts to reduce overfitting in the model

The model contains dropout layers in order to reduce overfitting (model.py lines 51 and 54). 

I used flipped images in order to generalize better the data. 

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 61).

#### 4. Appropriate training data

I used different data to train the model: 

- 1 Lap of center driving. 
- 1 Lap of "Accidents" where the car were off the road. 
- After running simulations, I spotted difficult places where I collected more data specifically to improve results. 
- I used the 3 images with correction in order to help the model avoid sides. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

First, I was following the model that I was watching on the videos. Then, I started to finde for more advance and roubust architectures like the ones we used with LeNet. 

There, I saw good results. So I tried improving data with splitting methods and augmented data with the 3 images with correction. 

Finally, I add dropouts after the pooling in order to generalize the model.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 46-58) consisted of a convolution neural network with the following layers and layer sizes ...

#### 3. Creation of the Training Set & Training Process

First, I collected 1 lap of center-drive data. Then, I collected data simulating errors of the driver. 

Then I Run de simulator to see what happened. Ther, I spotted a few dificult places for the network, so I collected much more data only on those places. 

After that, I saw a good behavior. So, I used splitting methods and the other 2 camera positions to get more input data.

There, I saw thata the validation loos was not improving with epochs, so I decided to increase droping rates. 

And voilá... The car was working right and safely. 
