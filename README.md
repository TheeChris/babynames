# Calculating the uniqueness and average age of my children

This is just a playful analysis of my kids' names using data from the Social Security Administration (SSA). In particular, I was curious about the fact that before my daughter, I only ever knew of two women named Maya: Angelou and Rudolph. We named our daughter after the former, believing it to be a beautiful and seemingly unique name, and Maya Angelou was a great poet and activist who had died shortly before our daughter's birth. (Side note: it also allowed me to tie in my love for astronomy: the "oldest sister" in the Pleiades star cluster is named Maia). However, when we moved to California a few of years ago, we started meeting several girls between the ages of 2 to 12 named Maya. Is the name more popular than we realized? Or is this a case of frequency illusion? With regards to our son, Henry, we assumed that the average age of Henry's has to be around 80, but again, we seem to be meeting more and more kids named Henry. So what is the average age of Henrys? Let's see what we can find out.

## 1.0 Load Libraries and Data

We will use a few libraries for reading data (io, zipfile, urllib), data manipulation (pandas, numpy), and visualization (matplotlib, plotly).

We will be pulling in data from the [SSA's baby names dataset](https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data). This is a zip file containing data on names, birth counts, and sex broken down into individual files for each year. We will extract the files and append them to a dataframe for easy manipulation. Here is a random sample of the dataframe.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4627</th>
      <td>1935</td>
      <td>Madell</td>
      <td>F</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9682</th>
      <td>2002</td>
      <td>Dhamar</td>
      <td>F</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3920</th>
      <td>1971</td>
      <td>Starlet</td>
      <td>F</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1053</th>
      <td>1885</td>
      <td>Arlena</td>
      <td>F</td>
      <td>5</td>
    </tr>
    <tr>
      <th>14155</th>
      <td>2004</td>
      <td>Zharick</td>
      <td>F</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3021</th>
      <td>1920</td>
      <td>Macil</td>
      <td>F</td>
      <td>11</td>
    </tr>
    <tr>
      <th>6260</th>
      <td>1953</td>
      <td>Min</td>
      <td>F</td>
      <td>5</td>
    </tr>
    <tr>
      <th>8378</th>
      <td>1939</td>
      <td>Ronell</td>
      <td>M</td>
      <td>6</td>
    </tr>
    <tr>
      <th>27398</th>
      <td>2001</td>
      <td>Cashawn</td>
      <td>M</td>
      <td>6</td>
    </tr>
    <tr>
      <th>22416</th>
      <td>2015</td>
      <td>Syler</td>
      <td>M</td>
      <td>34</td>
    </tr>
  </tbody>
</table>



## 2.0 The Popularity of Maya

Let's start by plotting the number of babies named Maya or Henry dating back to 1880.



<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~echris/4.embed" height="600px" width="100%"></iframe>

Regarding the name Maya, the first thing that stands out is that it doesn't appear in the SSA data until around 1940. The name is found in lots of cultures, so I'm curious if the introduction of the name into the US was the result of post-World War II migration.  Unfortunately, that will remain speculation with this current data set, but maybe something to look into in the future.  There has definitely been a steady increase in girls named Maya since the mid-1980s, with a peak just before my daughter was born. This peak, however, is nothing compared to the numbers we are getting from the name Henry. It seems like Henry is making a very strong comeback and nearing its peak in the early 20th century.  Looks like we are going to have a lot of Henrys over the age of 75 and under the age of 10.

So far it seems like Maya is a relatively unique name.  To get a better idea of how unique, let's plot Maya against the top 5 most popular girl's name for 2014. I will create dataframes for each of the top 5 names so that we can pull the birth count numbers over time. Then we can plot the data compared to the name Maya.  Interestingly enough, if you plot all of the birth counts of these names over the years, you will see that they were all relatively unpopular until the mid-80's and 90's when they all began to climb rapidly. For this reason, I started the data off at 1980 so that we can get a better look.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~echris/16.embed" height="600px" width="100%"></iframe>

We can see from the plot that the name Maya was only about 1/5th as popular as the name Olivia.  However, it does not give us a very robust idea of the name popularity. We could really dive in and start calculating the number of Maya's projected to be living between the ages of 2 and 14, and from that determine the percentage of 2- to 14-year-olds named Maya, but let's just look at one last calculation to get a better idea of the popularity of the names in 2014.

|     Name | Pct_of_Total | Pct_by_Sex |
| -------: | :----------: | :--------: |
|   Olivia |   0.538474   |  1.12439   |
|   Sophia |   0.506015   |  1.05662   |
| Isabella |   0.464386   |  0.969691  |
|      Ava |   0.426839   |  0.891289  |
|      Mia |   0.367472   |  0.767322  |
|     Maya |   0.10739    |  0.224243  |

Maya was ranked 73rd in 2014 birth names. Although none of the top five accounted for more that 1.12% of female names in 2014, Maya come in at the 73rd most popular name and accounts for on 0.22% of females born that year (5 times less than the most popular name). It can be argued that Maya is a unique name, but so are all of the other names. I will have to assume that my hearing the name Maya more frequently is simply the result of the frequency illusion bias. A better question might be: is it more unique to give your daughter a name that doesn't end in 'a'?

## 2.1 The Age of Henry

Now to figure out the average age of Henrys. First, we need to pull in data from the [SSA's Actuarial Life Tables](https://www.ssa.gov/oact/STATS/table4c6.html). You can see the head of the table and definitions of features below.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>x</th>
      <th>q(x)</th>
      <th>l(x)</th>
      <th>d(x)</th>
      <th>L(x)</th>
      <th>T(x)</th>
      <th>e(x)</th>
      <th>D(x)</th>
      <th>M(x)</th>
      <th>A(x)</th>
      <th>N(x)</th>
      <th>a(x)</th>
      <th>12a(x)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1900</td>
      <td>0</td>
      <td>0.145957</td>
      <td>100000</td>
      <td>14596</td>
      <td>90026</td>
      <td>4640595</td>
      <td>46.41</td>
      <td>100000</td>
      <td>39810</td>
      <td>0.3981</td>
      <td>2289435</td>
      <td>22.8943</td>
      <td>269.23</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1900</td>
      <td>1</td>
      <td>0.038140</td>
      <td>85404</td>
      <td>3257</td>
      <td>83776</td>
      <td>4550569</td>
      <td>53.28</td>
      <td>83159</td>
      <td>25598</td>
      <td>0.3078</td>
      <td>2189435</td>
      <td>26.3283</td>
      <td>310.44</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1900</td>
      <td>2</td>
      <td>0.019577</td>
      <td>82147</td>
      <td>1608</td>
      <td>81343</td>
      <td>4466793</td>
      <td>54.38</td>
      <td>77884</td>
      <td>22510</td>
      <td>0.2890</td>
      <td>2106276</td>
      <td>27.0436</td>
      <td>319.02</td>
    </tr>
  </tbody>
</table>

### Defining Actuarial Table Features

|    Column     | Description                                                  |
| :-----------: | ------------------------------------------------------------ |
|       x       | The age of the person.                                       |
| q<sub>x</sub> | The probability that a person exact age x will die within one year. |
| l<sub>x</sub> | The number of persons surviving to exact age x (in 100,000s). |
| d<sub>x</sub> | The number of deaths between exact ages x and x+1.           |
| L<sub>x</sub> | The number of person-years lived between exact ages x and x+1. |
| T<sub>x</sub> | The number of person-years lived after exact age x.          |
| e<sub>x</sub> | The average number of years of life remaining at exact age x. |

The rest of the table contains actuarial calculations that you can get more information about in the SSA's [Definitions of Life Tables Functions](https://www.ssa.gov/oact/HistEst/PerLifeTables/LifeTableDefinitions.pdf) document, but we won't be using those for now.

Next, I am going to merge the life table data with Henry's dataframe to calculate the estimated number of living Henry's for each year. Below is a plot of the estimated number of living Henrys by age.  

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~echris/8.embed" height="600px" width="100%"></iframe>



We can see that although there is a large grouping of Henrys aged 50-70, they are dwarfed by the number of Henrys that have been born in the past 10 years.  This should have a noticeable effect by dragging the average under the age of 50.  

We calculate the average age of Henry as 37.1. I guess Henrys could say they are getting younger every day (statistically speaking, of course). This is an important reminder that an average is not always a good statistic. After all, we have over twice as many 62-year-old Henrys and five times as many 2-year-old Henrys. We can get a better sense of how death plays a roll in this moving average by comparing the births by year to the estimated number of living.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~echris/10.embed" height="600px" width="100%"></iframe>

## 3.0 Conclusion

It appears that I was wrong on both accounts: there are not an inordinate number of Mayas being born and the average age of Henry is not even close to 80. The name Maya only accounted for 0.22% of females born in 2014. However, the name has unarguably gained popularity in the last 30 years. The average age of Henry is only 37, but the guess of 80 was not completely off-base. The peak year for Henrys was 1921, which means there are plenty of Henrys born 80 or more years ago.

## 4.0 Bonus Material

I fell into a bit of a rabbit hole while looking at the babynames and actuarial data, so here are some additional insights that I found. First, lets look at the peak years for Henry and Maya.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~echris/20.embed" height="600px" width="100%"></iframe>

It will be interesting to see if Henry can reach its 1920s peak or if it will continue to level off and drop. It looked like Maya was going to start climbing above Henry in popularity, but the name really started dropping off since its peak in 2006.

Next, let's add data for my wife (Raina) and I.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~echris/12.embed" height="600px" width="100%"></iframe>

Wow. I often joke about there being so many Chris's that we need to number off, but look at Mt. Chris up there! It towers over the other names so much that we lose all visual information about Raina and most of it from Maya. Let's compare the name popularities on a logarithmic scale to get a better sense of how their popularity has changed over time.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~echris/18.embed" height="600px" width="100%"></iframe

After converting to a logarithmic scale we can better see the change in name popularity over time.  We see that although Raina still remains a relatively obscure name, Maya appears much closer to Henry and Chris.  It is fascinating to me that both Raina ***and*** Maya don't seem to appear in the US until World War II. Regardless, one thing is clear, my wife takes the crown on most unique name in our house.

While looking at the data, I noticed some babies named Unknown showed up. Just out of curiosity, let's see if there are any trends in the number of people who were too tired to give their baby a name.  Anybody who has gone labor knows what I'm talking about.  I was exhausted and all I had to do was support the real work that my wife was doing. Honestly, I'm surprised we don't see any "Who Cares" on the list.

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~echris/14.embed" height="600px" width="100%"></iframe>

It looks like there was a bit of an issue with naming babies in the 1950s?  Did parents get tired of having to name all of their Baby Boomer kids? If anyone knows an Unknown, let me know. I really want to know how things turned out.  