#!/usr/bin/env python
# coding: utf-8

# In[1]:


# EPL data set
# Import the Libraries
# Load Dataset
# Creat 2 new columns
# Total Goals
# Penalty Goals
# Penalty Attempts
# Pie chart for penalties missed vs scored
# Unique positions
# Total FW players
# Total MF players
# players from different nations
# Most players from which countries
# Clubs with max players in their squad
# Club with min players in their squad
# players based on age group
# Total under 20 players in each club
# Total under 40 players in each club
# Under 20 players in Brighton,Southampton,ManU
# Under 40 players in ManU,West Bromwich Albion
# Average age of players in each club
# Total assists from each club
# Total Goals from each club
# Top 20 assists
# Top 20 Goals
# Top 20 Assists per match
# Top 20 Goals per match
# Pie chart Goals with assist & Goals without assist
# Top 20 players with most yellow cards
# Top 20 players with most red cards


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


EPL_df = pd.read_csv('C:\\Users\\Jadhav\\Downloads\\EPL_20_21.csv')
EPL_df.head()


# In[3]:


EPL_df.info()


# In[4]:


EPL_df.describe()


# In[5]:


EPL_df.isna().sum()


# In[6]:


EPL_df['MinsPerMatch'] = (EPL_df['Mins']/EPL_df['Matches']).astype(int)
EPL_df['GoalsPerMatch'] = (EPL_df['Goals']/EPL_df['Matches']).astype(float)
EPL_df.head()


# In[7]:


Total_Goals = EPL_df['Goals'].sum()
print(Total_Goals)


# In[8]:


Total_PenaltyGoals = EPL_df['Penalty_Goals'].sum()
print(Total_PenaltyGoals)


# In[9]:


Total_PenaltyAttempts = EPL_df['Penalty_Attempted'].sum()
print(Total_PenaltyAttempts)


# In[10]:


plt.figure(figsize=(19,8))
pl_not_scored = EPL_df['Penalty_Attempted'].sum() - Total_PenaltyGoals
data = [pl_not_scored, Total_PenaltyGoals]
labels = ['Penalties missed','Penalties Scored']
color = sns.color_palette('husl')
plt.pie(data, labels = labels, colors = color, autopct = '%.0f%%')
plt.show()


# In[11]:


EPL_df['Position'].unique()


# In[12]:


EPL_df[EPL_df['Position'] == 'FW']


# In[13]:


EPL_df[EPL_df['Position'] == 'MF']


# In[14]:


np.size((EPL_df['Nationality'].unique()))


# In[15]:


nationality = EPL_df.groupby('Nationality').size().sort_values(ascending = False)
nationality.head(10).plot(kind = 'bar',figsize=(19,8),color = sns.color_palette("magma"))


# In[16]:


EPL_df['Club'].value_counts().nlargest(10).plot(kind = 'bar',figsize = (16,8),color=sns.color_palette("viridis"))


# In[17]:


EPL_df['Club'].value_counts().nsmallest(10).plot(kind = 'bar',figsize = (16,8),color=sns.color_palette("viridis"))


# In[18]:


Under25 = EPL_df[EPL_df['Age'] <= 25]
age25_30 = EPL_df[(EPL_df['Age'] > 25) & (EPL_df['Age'] <= 30)]
age30_35 = EPL_df[(EPL_df['Age'] > 30) & (EPL_df['Age'] <= 35)]
Above35 = EPL_df[EPL_df['Age']>35]


# In[19]:


x = np.array([Under25['Name'].count(),age25_30['Name'].count(),age30_35['Name'].count(),Above35['Name'].count()])
mylabels = ["<=25",">25 & <=30", ">30 & <=35", ">35"]
plt.title('Total players with Age Groups',fontsize = 50,)
plt.pie(x, labels = mylabels, autopct="%.1f%%")
plt.show()


# In[20]:


players_under_20 = EPL_df[EPL_df['Age'] < 20]
players_under_20['Club'].value_counts().plot(kind = 'bar', color = sns.color_palette("cubehelix"))


# In[21]:


players_under_40 = EPL_df[EPL_df['Age'] < 40]
players_under_40['Club'].value_counts().plot(kind = 'bar', color = sns.color_palette("magma"))


# In[22]:


players_under_20[players_under_20['Club'] == 'Brighton']


# In[23]:


players_under_20[players_under_20['Club'] == 'Southampton']


# In[24]:


players_under_20[players_under_20['Club'] == 'Manchester United']


# In[25]:


players_under_40[players_under_40['Club'] == 'Manchester United']


# In[26]:


players_under_40[players_under_40['Club'] == 'West Bromwich Albion']


# In[27]:


plt.figure(figsize=(20, 10))
sns.boxplot(x = 'Club', y='Age', data = EPL_df)
plt.xticks(rotation = 100)


# In[28]:


num_player = EPL_df.groupby('Club').size()
data = (EPL_df.groupby('Club')['Age'].sum())/ num_player
data.sort_values(ascending = False)


# In[29]:


Assits_by_clubs = pd.DataFrame(EPL_df.groupby('Club', as_index=False)['Assists'].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax = sns.barplot(x='Club',y='Assists',data=Assits_by_clubs.sort_values(by="Assists"),palette='Set1')
ax.set_xlabel("Club",fontsize=40)
ax.set_ylabel("Assists",fontsize=30)
plt.xticks(rotation=80)
plt.rcParams["figure.figsize"] = (20,8)
plt.title('Graph of Clubs vs Total Assists',fontsize = 40)


# In[30]:


Goals_by_clubs = pd.DataFrame(EPL_df.groupby('Club', as_index=False)['Goals'].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax = sns.barplot(x='Club',y='Goals',data=Goals_by_clubs.sort_values(by='Goals'),palette='icefire')
ax.set_xlabel("Club",fontsize=40)
ax.set_ylabel("Goals",fontsize=30)
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"] = (20,8)
plt.title('Plot of Clubs vs Total Goals',fontsize = 40)


# In[31]:


top_20_assists = EPL_df[['Name','Club','Assists','Matches']].nlargest(n=20, columns = 'Assists')
top_20_assists


# In[32]:


top_20_goals = EPL_df[['Name','Club','Goals','Matches']].nlargest(n=20, columns = 'Goals')
top_20_goals


# In[33]:


top_20_goals_per_match = EPL_df[['Name','GoalsPerMatch','Matches','Goals']].nlargest(n=20, columns = 'GoalsPerMatch')
top_20_goals_per_match


# In[34]:


top_20_assists_per_match = EPL_df[['Name','Matches','Assists']].nlargest(n=20, columns = 'Assists')
top_20_assists_per_match


# In[35]:


plt.figure(figsize=(20,10))
assists = EPL_df['Assists'].sum()
data = [Total_Goals - assists, assists]
labels = ['Goals without assists','Goals with assists']
color = sns.color_palette('Set1')
plt.pie(data, labels = labels, colors = color, autopct = '%.0f%%')
plt.show()               


# In[36]:


epl_yellow=EPL_df.sort_values(by='Yellow_Cards', ascending=False)[:20]
plt.figure(figsize=(20,6))
plt.title("Players with most yellow cards")
c=sns.barplot(x=epl_yellow['Name'], y=epl_yellow['Yellow_Cards'], label='players', color='yellow')
plt.ylabel('Number of Yellow Cards')
c.set_xticklabels(c.get_xticklabels(),rotation=60)
c


# In[37]:


epl_red=EPL_df.sort_values(by='Red_Cards', ascending=False)[:20]
plt.figure(figsize=(20,6))
plt.title("Players with most red cards")
c=sns.barplot(x=epl_red['Name'], y=epl_red['Red_Cards'], label='players', color='Red')
plt.ylabel('Number of Red Cards')
c.set_xticklabels(c.get_xticklabels(),rotation=60)
c


# In[ ]:




