#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import quandl


# In[7]:


# Quandl API Key
quandl.ApiConfig.api_key = 'q5w1saUdGvM48KkZzjHX'


# In[11]:


# Define the financial metrics
metrics = ["EPS", "Free Cash Flow", 
           "Return on Equity", "Return on Invested Capital", 
           "Current Ratio", "Debt to Equity"]


# In[13]:


# Download the data for all stocks in the Sharadar SF1 dataset
data = quandl.get_table("SHARADAR/SF1", dimension="MRY")


# In[24]:


print(data.columns.tolist())


# In[22]:


print(data.columns)


# In[25]:


# Screen the stocks based on Phil Town's style
screener = data[(data["eps"] > 0) & 
                (data["fcf"] > 0) & 
                (data["roe"] > 0) & 
                (data["roic"] > 0) & 
                (data["currentratio"] > 1) & 
                (data["de"] < 1)]


# In[26]:


# Print all the results
print(screener)


# In[27]:


# Print top 10 Results
print(screener.head(10))


# In[28]:


# Display in Table format
from IPython.display import display
display(screener)


# In[31]:


# Create Bar Graph Showing EPS Values

import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(x='ticker', y='eps', data=screener)
plt.show()


# In[32]:


# Create scatter plot of Return on Equity and Return on Invested Capital
import plotly.express as px
fig = px.scatter(screener, x='roe', y='roic', color='ticker')
fig.show()


# In[ ]:




