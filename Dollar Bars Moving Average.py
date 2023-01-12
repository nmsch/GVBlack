#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf


# In[3]:


# Define the stock symbol
symbol = "SPY"


# In[16]:


# Download the historical data
data = yf.download(symbol, start="2018-01-01", end="2023-01-12")


# In[17]:


# Calculate the dollar volume
data["dollar_volume"] = data["Close"] * data["Volume"]


# In[18]:


# Define the threshold for dollar bars
threshold = 100000000


# In[19]:


# Create the dollar bars
dollar_bars = data[data["dollar_volume"] >= threshold]


# In[20]:


# Print the dollar bars
print(dollar_bars)


# In[21]:


import matplotlib.pyplot as plt


# In[22]:


# Plot the dollar volume
plt.plot(dollar_bars["dollar_volume"])

# Add labels and title to the graph
plt.xlabel("Date")
plt.ylabel("Dollar Volume")
plt.title("Dollar Bars for " + symbol)

# Show the graph
plt.show()


# In[23]:


import matplotlib.pyplot as plt

# Define the window size for the moving average
window = 100

# Calculate the moving average
dollar_bars["moving_average"] = dollar_bars["dollar_volume"].rolling(window=window).mean()

# Plot the dollar volume
plt.plot(dollar_bars["dollar_volume"], label="Dollar Volume")

# Plot the moving average
plt.plot(dollar_bars["moving_average"], label="Moving Average", linestyle='dashed')

# Add labels and title to the graph
plt.xlabel("Date")
plt.ylabel("Dollar Volume")
plt.title("Dollar Bars for " + symbol)

# Add legend
plt.legend()

# Show the graph
plt.show()


# In[36]:


# Get the stock information of a specific stock
ticker = "DIS"
stock = yf.Ticker(ticker)


# In[37]:


# Get the live stock data
info = stock.info


# In[38]:


# Print the live stock data
print(info)


# In[ ]:




