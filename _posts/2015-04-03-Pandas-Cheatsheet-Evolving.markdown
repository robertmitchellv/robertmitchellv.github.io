---
layout: post
title:  "My Pandas Cheatsheet&#8212;always evolving"
date:   2015-04-03 8:30:00
comments: true
categories:
---
### As I learn more this page will be updated

The goal of this post has two aims; one, to keep me from googling pandas questions
that I've forgotten already.  I feel like Sisyphus!  So, here
are :

### Make matplotlib.pyplot look better with no effort:
{% highlight python linenos %}
import matplotlib.pyplot as plt
plt.style.use('ggplot')
%matplotlib inline
{% endhighlight %}

### Delete column
{% highlight python linenos %}
del df['colName']
{% endhighlight %}

### Rename columns
{% highlight python linenos %}
df.columns = ['col1', 'col2', 'col3'] # this does not reindex columns
{% endhighlight %}

### Copy column
{% highlight python linenos %}
df['newCol'] = df['oldCol'] # where newCol is the copy
{% endhighlight %}

### Reindex columns
{% highlight python linenos %}
cols = ['col1', 'col2', 'col3', 'col4'] # list of how you'd like it
df = df.reindex(columns=cols)
{% endhighlight %}

### Show unique values
{% highlight python linenos %}
df[df['colName'].unique()]
{% endhighlight %}

### Delete row
{% highlight python linenos %}
df = df.drop(2)  # where two is the df's index
df = df.drop('rowName')  # if you reindexed
{% endhighlight %}

### Remove characters before a specific character
{% highlight python linenos %}
df['colName'] = df['colName'].apply(lambda x: x.split('-')[-1]) # char = -
{% endhighlight %}

### Remove characters after a specific character
{% highlight python linenos %}
df['colName'] = df['colName'].apply(lambda x: x.split('-')[0]) # char = -
{% endhighlight %}

### Remove characters, e.g., commas from data
{% highlight python linenos %}
df['colName'] = df['colName'].str.replace(',', '')
{% endhighlight %}

### Convert datatypes, e.g., object to float
{% highlight python linenos %}
df[['col4', 'col5', 'col10']] = df[['col4', 'col5', col10]].astype(float)
{% endhighlight %}

### Convert NaN values to zeros (or anything else)
{% highlight python linenos %}
df = df.fillna(0) # remember that this returns a new object!
{% endhighlight %}

### Replace string values with numeric representations
{% highlight python linenos %}
dictionary = {'value1': 1, 'value2': 2, 'Value3': 3}
df.replace({'colName': dictionary})
{% endhighlight %}

### Project data based on a value range from a column
{% highlight python linenos %}
df[df.colWithNumbers <= 360] # shows me values less than or equal to 360
df[df['colWithStrings'].str.contains("word")] # shows me values with 'word' in them
{% endhighlight %}

### Project data based on two values (use and or pipe symbol to denote relationship)
{% highlight python linenos %}
df[(df['colWithString'].str.contains("word")) & (df.colWithNumber <= 5)] # and
df[(df['colWithString'].str.contains("firstWord")) | (df['colWithString'].str.contains("secondWord"))] # or
{% endhighlight %}

### Groupby as variable
{% highlight python linenos %}
groupedby = df.groupby(df.colName) # or:
groupedby = df.groupby(df.colName).add_suffix('/Mean') # add column suffixes
{% endhighlight %}

### Use groupedby variable and find the mean for your values
{% highlight python linenos %}
groupedbyMean = groupedby.mean()
{% endhighlight %}
