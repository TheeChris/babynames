'''
  Calculating the uniqueness and average age of my children
    This is just a fun script to analyze the Social Security Administration's
    baby names and actuarial life tables datasets.
    The accompanying blog post is at: 
    http://echrislynch.com/2018/05/10/fun-with-baby-names/
'''

# Load Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a list of years from 1880 to 2016
years = [i for i in range(1880, 2017)]

# Initialize an empty list to become the babynames dataframe
babynames = []

# Generate the babyname csv file names to be imported
for each in years:
    file_name = "datasets/babynames/yob%s.txt" % each

    columns = ['Name', 'Sex', 'Count']
    
    # read each csv file into a dataframe
    babyname_df = pd.read_csv(file_name, sep=',', header=0, names=columns)
    
    # insert a column for the year
    babyname_df.insert(0, 'Year', each)
    
    # append each year's dataframe to the babynames list
    babynames.append(babyname_df)

# convert the babynames list into a dataframe
babynames = pd.concat(babynames, axis=0)
print(babynames.head())

# Create functions to generate name-based dataframes and plots
def get_info(name, sex):
    '''
    This function takes a name and sex and generates a dataframe 
    with that specific information from the babynames dataframe
    '''
    name_data = babynames[(babynames['Name'] == name) & (babynames['Sex'] == sex)]
    return name_data

def plot_trends(names, sex, color, scale='linear', title=None, style='seaborn-white'):
    '''
    This function takes a name and sex and creates a plot showing
    the number of births for that name from 1880 to 2016
    '''
    for idx in range(len(names)):
        info = get_info(names[idx], sex[idx])
        axes = plt.plot(info['Year'], info['Count']/1000, label=names[idx], alpha=0.8, c=color[idx])
        plt.title(title)
    plt.legend(loc='best')
    plt.xlabel('year')
    plt.ylabel('count (thousands)')
    plt.yscale(scale)
    plt.style.use(style)
    plt.axis([1880,2016,0,12])
    return axes

# Add columns to dataframe: 'Total Births by Year' and 'Total by Year and Sex'
babynames['Total by Year and Sex'] = 0
babynames['Total Births by Year'] = 0

for year in years:
    babynames.loc[babynames.Year == year, 'Total Births by Year'] = babynames[(babynames.Year == year)]['Count'].sum()  
    babynames.loc[(babynames.Year == year) &  (babynames.Sex == 'F'), 'Total by Year and Sex'] = babynames[(babynames.Year == year) & (babynames.Sex == 'F')]['Count'].sum()
    babynames.loc[(babynames.Year == year) & (babynames.Sex == 'M'), 'Total by Year and Sex'] = babynames[(babynames.Year == year) & (babynames.Sex == 'M')]['Count'].sum()
    
# Add columns to dataframe: 'Percent of Total' and 'Percent by Sex'
babynames['Pct of Total'] = (babynames['Count'] / babynames['Total Births by Year']) * 100
babynames['Pct by Sex'] = (babynames['Count'] / babynames['Total by Year and Sex']) * 100

# Create dataframes for Maya and Henry
maya = get_info('Maya','F')
henry = get_info('Henry', 'M')

# Plot trends for Maya and Henry
kids = ['Maya','Henry']
plot_trends(kids, ['F','M'], ['blue', 'red'], title='The Popularity of Henry & Maya')
plt.show()

# Top 5 female names in 2014
top5_2014 = babynames[(babynames['Sex'] == 'F') & (babynames['Year'] == 2014)]
top5_2014 = np.array(top5_2014.iloc[:5,1]).tolist()
print('The Top 5 Female Names of 2014:', top5_2014)

# Create dataframes for each name in Top 5
olivia = get_info('Olivia','F')
sophia = get_info('Sophia','F')
isabella = get_info('Isabella','F')
ava = get_info('Ava','F')
mia = get_info('Mia','F')

# Plot number of Mayas against Top 5 
_top = plt.plot(maya['Year'], maya['Count'])
_top = plt.plot(olivia['Year'], olivia['Count'])
_top = plt.plot(sophia['Year'], sophia['Count'])
_top = plt.plot(isabella['Year'], isabella['Count'])
_top = plt.plot(ava['Year'], ava['Count'])
_top = plt.plot(mia['Year'], mia['Count'])
_top = plt.legend(['Maya','Olivia', 'Sophia', 'Isabella', 'Ava', 'Mia'])
_top = plt.xlabel('Year')
_top = plt.ylabel('Number of Births')
_top = plt.title('Maya vs 2014 Top 5 Names')
_top = plt.xlim(1980,2016)

plt.show()

# Combine 2014 names into one dataframe for easier reading
top5_2014_merged = olivia.append([sophia, isabella, ava, mia, maya])

print(top5_2014_merged[top5_2014_merged['Year'] == 2014])

# Create a dataframe from male actuarial data
life_table_male = pd.read_csv('datasets/babynames/LifeTables_M_2017.csv', skiprows=4)

# Extract subset relevant to those alive in 2016
lifetables_male_2016 = life_table_male.loc[life_table_male['Year'] + life_table_male['x'] == 2016]

# Plot the mortality distribution: year vs. l(x)
lifetables_male_2016.plot('Year', 'l(x)')

# Merge Henry dataframe with relevant actuarial data
henry_alive = henry.merge(lifetables_male_2016, on='Year')

# Create a column of the estimated number of living Henrys from each year
henry_alive['n_alive'] = henry_alive['l(x)']*henry_alive['Count']/(10**5)

# Generate a plot of the number of living Henrys at each age
_h = plt.plot(henry_alive.x, henry_alive.n_alive)
_h = plt.title('Living Henrys by Age')
_h = plt.xlabel('Age')
_h = plt.ylabel('Number of Living Henrys')
_h = plt.axis([2,115,0,9500])
plt.show()

# Create a column of the product of age and number alive
henry_alive['rel_age'] = henry_alive.x * henry_alive.n_alive

# From weighted age, calculate the average age
avg_age = henry_alive.rel_age.sum() / henry_alive.n_alive.sum()
print('The average age of Henry is', '%.2f' % avg_age)

