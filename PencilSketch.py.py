#!/usr/bin/env python
# coding: utf-8

# In[24]:


#importing libraries
import cv2
import matplotlib.pyplot as plt


# In[25]:


img=cv2.imread("anu.jpg")
RGB_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.axis(False)
plt.show()


# In[26]:


#conveted to grey scale
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#inverted the image
invert_img=cv2.bitwise_not(grey_img)
#blured image
blur_img=cv2.GaussianBlur(invert_img,(111,111),0)
#invert blured image
invblur_img=cv2.bitwise_not(blur_img)


# In[27]:


sketch_img=cv2.divide(grey_img,invblur_img,scale=150)


# In[28]:


plt.figure(figsize=(14,8))
plt.subplot(1,2,1)
plt.title('Original image',size=18)
plt.imshow(RGB_img)
plt.axis('off')
plt.subplot(1,2,2)
plt.title('Sketch',size=18)
rgb_sketch=cv2.cvtColor(sketch_img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.show()

