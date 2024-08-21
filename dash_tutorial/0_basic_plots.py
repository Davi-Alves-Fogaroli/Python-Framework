import plotly.express as px
import pandas as pd

#NORMAL PLOT
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()


# #PLOT WHIT 2 COLUNS WITH DIFFERENT COLORS
# df = px.data.gapminder().query("continent=='Oceania'")
# fig = px.line(df, x="year", y="lifeExp", title="Compar life expectancy, Australia and New Zealand", color="country")    
# fig.show()


# #ORDER IN LINE CHARTS
# # if you dont order your data, the lines moving 'backwards' across the chart
# df = pd.DataFrame(dict(
#     x = [1,3,2,4],
#     y = [1,2,3,4]
# ))

# fig_1 = px.line(df, x='x', y='y', title="Unsorted Imput")
# fig_1.show()

# df = df.sort_values(by='x')
# fig_2 = px.line(df, x='x', y='y', title="Sorted Imput")
# fig_2.show()


#CONNECTED SCATTERPLOTS
# in connected scatterplots two graph are plot side by side

# df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
# fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
# fig.update_traces(textposition="bottom right")
# fig.show()


#MARKER ON LINE && SYMBOL ARGUMENT
# just increment circle on the line, to represent the data

# df = px.data.gapminder().query("continent == 'Oceania'")
# fig = px.line(df, x='year', y='lifeExp', color='country', markers=True, symbol="country")
# fig.show()


#LINE PLOTS ON DATE AXES
# .......https://plotly.com/python/line-charts/

# import plotly.express as px

# df = px.data.stocks()
# fig = px.line(df, x='date', y="GOOG")
# fig.show()