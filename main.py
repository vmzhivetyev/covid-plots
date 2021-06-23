# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

import plotly.graph_objects as go
#
# fig = go.Figure()
#
# for country in df['location']:
#     df1 = df[df['location'] == country]
#
#     fig.add_trace(go.Scatter(
#         df1,
#         x='date', y='total_cases', name=country
#     ))


def plot(df, country, population):
    df = df[df['location'] == country]
    # df = df[df['date'] == '2020-10-04']

    vac_key = 'people_fully_vaccinated'

    df[[vac_key, 'new_deaths', 'hosp_patients', 'new_cases']] /= population

    df = df[[vac_key, 'new_deaths', 'hosp_patients', 'new_cases', 'date', 'location']]
    df.dropna(subset=['new_cases'], inplace=True)
    df = df[df['new_cases'] != 0.0]

    print(df.values)

    fig = px.line(df, x='date', y='new_cases', title='COVID', color="location", hover_data=[], log_y=True)

    fig.add_scatter(x=df['date'], y=df[vac_key], mode='lines', name='Fully Vaccinated', connectgaps=True)
    fig.add_scatter(x=df['date'], y=df['new_deaths'], mode='lines', name='Deaths', connectgaps=True)
    fig.add_scatter(x=df['date'], y=df['hosp_patients'], mode='lines', name='Hospitalized', connectgaps=True)

    fig.show()


plot(df, 'Israel', population=9e4)
plot(df, 'United States', population=328e4)
plot(df, 'India', population=1.3 * 1e7)
plot(df, 'Indonesia', population=270e4)
plot(df, 'Argentina', population=45e4)
plot(df, 'Pakistan', population=216e4)
