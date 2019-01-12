import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('PEGI_Ratings_20170907.csv')
sns.set()

df['year'] = df.release.str.slice(0, 4)

# Graph by year
graph_df = df[['year', 'rating']].groupby('year', as_index=False).agg('mean')

p = sns.relplot(data = graph_df, x="year", y="rating", kind="line", color="#391E29")
p.set_ylabels("PEGI rating")
p.set_xlabels("Year of release")
p.set(ylim=(0, 11))
plt.title("Average PEGI rating by year")

fig = plt.gcf()
fig.set_size_inches(12, 4)
fig.savefig('plot_year.png', dpi=100, bbox_inches='tight')

# Graph by genre
graph_df = df[['genre', 'rating']].groupby('genre', as_index=False).agg('mean')

p = sns.catplot(data = graph_df, x="rating", y="genre", kind="bar", color="#36554B")
p.set_xlabels("PEGI rating")
p.set_ylabels("Game genre")
p.set(xlim=(0, 13))
plt.title("Average PEGI rating by game genre (1999-2017)")

fig = plt.gcf()
fig.set_size_inches(12, 5)
fig.savefig('plot_genre.png', dpi=100, bbox_inches='tight')

# Graph by platform
graph_df = df[['platform', 'rating']].groupby('platform', as_index=False).agg('mean')

p = sns.catplot(data = graph_df, x="rating", y="platform", kind="bar", color="#853C43")
p.set_xlabels("PEGI rating")
p.set_ylabels("")
p.set(xlim=(0, 13))
plt.title("Average PEGI rating by game platform (1999-2017)")

fig = plt.gcf()
fig.set_size_inches(12, 12)
fig.savefig('plot_platform.png', dpi=100, bbox_inches='tight')

