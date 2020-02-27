#!/usr/bin/env python
# coding: utf-8

# The main goal of this project is to apply concepts learned through the DataQuest missions.
# The dataset in use was scraped from eBay Kleinanzeigen (a classifieds section of the German eBay website.)

# In[1]:


import numpy as np
import pandas as pd

autos = pd.read_csv('autos.csv', encoding = 'Latin-1')


# In[2]:


autos


# In[3]:


autos.info()
autos.head()


# It is already possible to see that there are some informations missing (fueltype, model and vehicletype) on some rows.

# Lets start by cleaning columns:

# In[4]:


autos.columns


# In[12]:


autos.rename(columns = {'yearOfRegistration' : 'registration_year', 'monthOfRegistration' : 'registration_month', 'notRepairedDamage':'unrepaired_damage', 'dateCreated':'ad_created', 'offerType':'offer_type', 'vehicleType':'vehicle_type', 'powerPS':'power_ps', 'fuelType':'fuel_type', 'nrOfPictures':'nr_of_pictures', 'postalCode':'postal_code', 'lastSeen':'last_seen', 'dateCrawled':'date_crawled'}, inplace = True)


# In[13]:


autos.columns


# In[14]:


autos.head()


# Changed column names in order to adapt it to good practices.

# In[32]:


autos.describe(include='all')


# Columns with mostly one value: nr_of_pictures
# Needs more investigation: seller, unrepaired_damage
# Numeric data stored as text: price, odometer, 

# In[29]:


autos['seller'].value_counts()


# In[30]:


autos['nr_of_pictures'].value_counts()


# In[31]:


autos['unrepaired_damage'].value_counts()


# In[33]:


autos['offer_type'].value_counts()


# In[34]:


autos['abtest'].value_counts()


# In[35]:


autos['registration_year'].value_counts()


# There are some impossible values for registration_year. 
# 'offer_type' has 49999 instances of Angebot and 1 of Gesuch.
# 'seller' has 49999 instances of Privat and 1 of Gewerblich
# nr_of_pictures is always 0
# Numeric data stored as text: price, odometer
# 
# Lets change price and odometer to numeric:

# In[47]:


autos['price'] = autos['price'].str.replace('$','').str.replace(',','')
autos['price'] = autos['price'].astype(float)


# In[48]:


autos['price']


# In[55]:


autos['odometer'] = autos['odometer'].str.replace('km','').str.replace(',','')
autos['odometer'] = autos['odometer'].astype(float)


# In[56]:


autos['odometer']


# In[57]:


autos.rename(columns={"odometer":"odometer_km"}, inplace = True)


# In[58]:


autos


# In[ ]:




