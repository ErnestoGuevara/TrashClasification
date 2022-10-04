# TrashClasification
## Project Description
In Mexican culture, separating garbage is not common but it is essential for all to live in a better environment and even in a better world. Daily in Mexico City, 12,843 tons of waste are generated; this equates on average to 1.5 kg per person per day. But much of this garbage is recyclable or reusable and is not separated. Not separating the garbage is something that can affect us since we will live in a more polluted environment. 
## Solution
The solution that is proposed is to make a smart garbage can that can be used by anyone already in a home, in a school or in an office and can place any bottle piece by piece so that it can be detected and then shall detect what type of garbage is with the detection system. The next step would be that the trash movement system shall accommodate the garbage where it should go and then the user feedback system shall give information to the user to learn more about why it is good to separate the garbage and some information about the type of garbage that is being thrown away.
## How to run 
First of all you have to clone the project: 
```
git clone (link)
```
Then you have to download the imgTransform folder from: https://drive.google.com/drive/folders/1Quzi-nfAZaTQA4JxVl7mEAshsHSJtAEK?usp=sharing 

You have to place this folder in the root directory. In this folder you will see that it has the classes of grabage that we are using, so you can add any image that you want in its respective folder.

Then once you alredy add all the images you want to use for the dataset, you have to run the next code:
```
python3 code/imageTransformer.py
```
This code will sort and set the data set that the CNN will be use.

For the last to run the main code for the cnn using pytorch you have to run:
```
python3 code/classification.py
```
This will generate a model. This model you can use it to start to identify with another images the garbage using the next code:
```
python3 code/classification.py --image (name of image) --model (name of model)
```

## Credits
We take the base of the project: https://github.com/YaelBenShalom/Objects-Recognition-and-Classification

