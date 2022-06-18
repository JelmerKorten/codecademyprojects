# %% [markdown]
# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# %% [markdown]
# ## Step 1. Import Python Modules

# %% [markdown]
# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# %%
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# %% [markdown]
# ## Step 2 Prep The Data

# %% [markdown]
# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# %%
df = pd.read_csv('all_data.csv')
df.head()

# %% [markdown]
# ## Step 3 Examine The Data

# %% [markdown]
# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# %% [markdown]
# What six countries are represented in the data?

# %%
countries = df['Country'].unique()
print(countries)

# %% [markdown]
# What years are represented in the data?

# %%
years = df['Year'].unique()
print(years)

# %% [markdown]
# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# %% [markdown]
# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# %%
df.rename(columns={'Life expectancy at birth (years)':'LEABY'},inplace=True)
df.head()

# %% [markdown]
# Run `df.head()` again to check your new column name worked.

# %%
#check

# %% [markdown]
# ---

# %% [markdown]
# ## Step 5 Bar Charts To Compare Average

# %% [markdown]
# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# %%
chile = df[df.Country == 'Chile']
maxgdpchile = max(chile.GDP)
zim = df[df.Country == 'Zimbabwe']

# %%
chilezim = chile.append(zim, ignore_index=True)

# %%
chilezim.head()

# %%
plt.figure(figsize=(15,8))
sns.set_palette('pastel')
sns.set_style('whitegrid')
ax = sns.barplot(data=df,x='Country',y='GDP')
plt.show()

# %%

plt.figure(figsize=(15,8))
ax = sns.barplot(data=chilezim,x='Country',y='GDP')
plt.show()


# %%
ax = sns.barplot(data=zim,x='Country',y='GDP')
plt.show()

# %% [markdown]
# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# %%
plt.figure(figsize=(15,5))
sns.barplot(data=df,x='Country',y='LEABY')
plt.show()


# %% [markdown]
# What do you notice about the two bar charts? Do they look similar?

# %%
#the bar charts look somewhat similar
#however on the LEABY one zimbabwe is more visible as the difference in yvalue is not as big
#something to note as well is that LEABY in chile is actually relatively high compared to their gdp

# %% [markdown]
# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# %% [markdown]
# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# %%
fig = plt.subplots(figsize=(15, 10))
sns.violinplot(data=df,x='Country',y='LEABY')
plt.title('LEABY per Country',fontsize=20)
plt.savefig('1-violin_lifeexp.png')
plt.show()

# %% [markdown]
# What do you notice about this distribution? Which country's life expactancy has changed the most?

# %% [markdown]
#  Most are stable but Zim's has changed quite a bit as we can see by the violin plot being very spread out
#  there is not really a certain point where it stayed for a longer while

# %% [markdown]
# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# %%
f, ax = plt.subplots(figsize=(10, 15)) 
ax = sns.barplot(data=df,x='Country',y='GDP',hue='Year')
plt.xticks(rotation=60)
plt.ylabel('GDP in Trillion USD')
plt.show()

# %%
#giving chile and zim its own charts to get information for this data

f, ax = plt.subplots(figsize=(10, 10)) 
ax = sns.barplot(data=chilezim,x='Country',y='GDP',hue='Year')
plt.xticks(rotation=60)
plt.ylabel('GDP in 10 Billions USD')
plt.show()

# %%
#giving  zim its own charts to get information for this data

f, ax = plt.subplots(figsize=(10, 10)) 
ax = sns.barplot(data=zim,x='Country',y='GDP',hue='Year')
plt.xticks(rotation=60)
plt.ylabel('GDP in Billion USD')
plt.show()

# %%
fig = plt.figure(figsize=(15,15))
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.suptitle('GDP per country',x=.4,y=.9,fontsize=20)

ax1 = plt.subplot2grid((3,3),(0,0),colspan=2)
ax1 = sns.barplot(data=df,x='Country',y='GDP',hue='Year',palette='pastel')
plt.xticks(rotation=15)
plt.ylabel('GDP in 10 Trillion USD')
ax1.legend(bbox_to_anchor=(1.05, 1))
ax1.set_xlabel(None)

ax2 = plt.subplot2grid((3,3),(1,0),colspan=1,rowspan=1)
ax2 = sns.barplot(data=chilezim,x='Country',y='GDP',hue='Year',palette='pastel')
plt.xticks(rotation=15)
plt.ylabel('GDP in 100 Billions USD')
ax2.legend().remove()
ax2.set_xlabel(None)

ax3 = plt.subplot2grid((3,3),(1,1),colspan=1,rowspan=1)
ax3 = sns.barplot(data=zim,x='Country',y='GDP',hue='Year',palette='pastel')
plt.xticks(rotation=15)
plt.ylabel('GDP in 10 Billion USD')
ax3.legend().remove()
ax3.set_xlabel(None)

plt.savefig('11-gdp_per_country.png',bbox_inches='tight')
plt.show()

# %% [markdown]
# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# %%
f, ax = plt.subplots(figsize=(10, 9))
#sns.color_palette('powderblue',16)
ax = sns.barplot(data=df,x='Country',y='LEABY',hue='Year',palette='pastel')
plt.xticks(rotation=60)
plt.ylim(40,85)
plt.ylabel('Life Expectancy at birth')
plt.title('Life Expectancy per Country per Year',fontsize=20)
plt.savefig('12-leaby_country.png')
plt.show()

# %%
f, ax = plt.subplots(figsize=(10, 9)) 
ax = sns.barplot(data=zim,x='Country',y='LEABY',hue='Year')
plt.xticks(rotation=60)
plt.ylim(40,65)
plt.ylabel('Life Expectancy at birth')
plt.show()

# %%
#multiplot leaby


# %% [markdown]
# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# %% [markdown]
# First impressions:
# countries bars changes the most: Life expectancy for zim goes up strongly
# What year athe biggest changes? for zim the turningpoint was 2006-2007
# which country has had the least change in gdp? mexico/chile
# how do countries compare? some go steep, others go flat...
# relationship between gdp and life? looks like there is a correlation however chile sort of contradicts that.
# We can expect to see life expectancy to go up, especially in third world countries due to arrival and better access to health care. GDP went up in booming and rising countries, espeically china is good example as the produce a lot of different products which helps them raise the gdp
# 

# %% [markdown]
# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# %% [markdown]
# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# %% [markdown]
# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# %%
# Uncomment the code below and fill in the blanks
g = sns.FacetGrid(data=df, col='Year', hue='Country', col_wrap=4, height=2)
g.map(plt.scatter,'GDP','LEABY', edgecolor="w").add_legend()
plt.suptitle('LEABY vs GDP /year /country',fontsize=20)
plt.subplots_adjust(top=0.90)
plt.savefig('2-scatter_gpd_lifexp.png')

# %% [markdown]
# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# %% [markdown]
# which country moves the most along gdp xaxis? china/maybe usa
# which country moves most along yaxis? zim
# is this surprising? zim is one of the poorer countries so not crazy their life expectancy moves up
# as discussed above china is expected to grow with their presence in the world production market
# do I think this is easy to read? no, there are too many graphs. however you can see some scales yes.

# %% [markdown]
# ## Step 9. Line Plots for Life Expectancy

# %% [markdown]
# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# %%
# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"


# Uncomment the code below and fill in the blanks
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3.map(sns.lineplot, "Year", "LEABY").add_legend()
plt.suptitle('LEABY /year /country',fontsize=20)
plt.subplots_adjust(top=0.90)
plt.savefig('4-facet_lifexp_country.png')

# %% [markdown]
# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

# %% [markdown]
# zimbabe changes most, followed by china
# zims turnaround was 2005/2006 the rest is quite steady of time
# least change is in mexico by the looks of it
# looks this way because we're reaching a high life expectency. and still zim stands for healthcare increase, both being more in the country available and ppl being able to afford it with increase of gdp 

# %% [markdown]
# ## Step 10. Line Plots for GDP

# %% [markdown]
# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# %%
g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3.map(sns.lineplot, "Year", "GDP").add_legend()
plt.suptitle('GBP /year /country',fontsize=20)
plt.subplots_adjust(top=0.90)
plt.savefig('3-facet_gdp_country.png')

# %% [markdown]
# Which countries have the highest and lowest GDP?

# %%
#lowest gdp is zim
#highest gdp is america

# %% [markdown]
# Which countries have the highest and lowest life expectancy?

# %%
#lowest life expenctancy is zim as well
#highest is germany/chile

# %% [markdown]
# ## Step 11 Researching Data Context 

# %% [markdown]
# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# %%
#how come the zim line changed so much?
#they got better access to health care and they had a cleanup of shanty towns after the US used their name in a bad way


# %% [markdown]
# ## Step 12 Create Blog Post

# %% [markdown]
# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??


