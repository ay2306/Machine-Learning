import numpy as np
import pandas as pd
# import PyQt5
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn import svm
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# # matplotlib.inline

labelled_images = pd.read_csv('train.csv')
images = labelled_images.iloc[0:,1:]
labels = labelled_images.iloc[0:,:1]
train_images, test_images, train_labels, test_labels = train_test_split(images,labels,random_state=0)
i = 1
test_images[test_images>0]=1
train_images[train_images>0]=1
img = train_images.iloc[i].values
img = img.reshape((28,28))
#print(img)
#plt.plot([1,2])
plt.imshow(img,cmap='binary')
#plt.hist(train_images.iloc[i])
#print(train_labels.values.ravel())
clf = svm.SVC()
clf.fit(train_images,train_labels.values.ravel())
clf.score(test_images,test_labels)

test_data = pd.read_csv('test.csv')
#print(test_data[1:5000])
#test_data_images = test_data.iloc[0:5000]
test_data[test_data>0]=1
result = clf.predict(test_data)
i = 1
img = test_data.iloc[i].values
img = img.reshape((28,28))
plt.imshow(img,cmap='binary')
print(result[i])
i += 1
df = pd.DataFrame(result)
df.index.name = 'ImageId'
df.index += 1
df.columns = ['Label']
df.to_csv('results.csv',header=True)