#!/usr/bin/env python
# coding: utf-8

# In[21]:


df = pd.read_csv("C:/Users/karth/OneDrive/Desktop/dataset - netflix1.csv")


# In[22]:


print(df)


# In[23]:


df.head(10)


# In[26]:


df.isnull().sum()


# In[27]:


df.dropna()


# In[43]:


import pandas as pd
from scipy import stats
data = df['release_year']

# Calculate Z-scores for each data point
z_scores = stats.zscore(data)

# Define a threshold for identifying outliers
threshold = 1

# Filter out the outliers
cleaned_df = df[abs(z_scores) <= threshold]

# Save the cleaned DataFrame to a new CSV file
cleaned_df.to_csv('cleaned_data.csv', index=False)


# In[44]:


cleaned_data=pd.read_csv("cleaned_data.csv")


# In[45]:


cleaned_data


# In[ ]:





# In[ ]:




