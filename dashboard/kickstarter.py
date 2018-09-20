#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://github.com/flavianh/dashboards-frameworks-comparison
"""

import os
import random
import string
import pandas as pd
import os
import datetime
from itertools import product

from bokeh.core.properties import value
from bokeh.events import Reset
from bokeh.events import SelectionGeometry
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
from bokeh.models.widgets import CheckboxButtonGroup
from bokeh.models.widgets import Div
from bokeh.plotting import figure
from bokeh.plotting import curdoc

import pandas as pd
from datetime import datetime
from collections import namedtuple


# Create Dummy Data
def rand_str(length):
    return "".join([random.choice(string.ascii_letters) for _ in range(length)])

ts_lower = int(datetime(2007, 1, 1).timestamp())
ts_upper = int(datetime(2018, 1, 1).timestamp())

def rand_year():
    return datetime.utcfromtimestamp(random.randint(ts_lower, ts_upper))

columns = ("name", "year", "USD", "category", "state")
categories = "art,food,game".split(",")
states = "successful,pending,failed,canceled".split(",")

n_project = 1000
df = list()
for _ in range(n_project):
    name = rand_str(32)
    year = rand_year()
    USD = random.randint(10000, 500000)
    category = random.choice(categories)
    state = random.choice(states)
    project = (name, year, USD, category, state)

    df.append(project)

df = pd.DataFrame(df, columns=columns)

#
colors = "#35f245,#d2a400,#ff1f1f".split(",")

sources_year_vs_usd = {
    state: ColumnDataSource(
        dict(
            x=list(),
            y=list(),
            name=list(),
            state=list(),
        )
    )
    for state in states
}


def update_source(selected_categories):
    sub_df = df[df.category.isin(selected_categories)]
    for state in states:
        tmp_df = sub_df[sub_df.state == state]
        data = dict(
            x=tmp_df.year,
            y=tmp_df.USD,
            name=tmp_df.name,
            state=[state, ] * tmp_df.shape[0]
        )
        sources_year_vs_usd[state].data = data


def filter_categories(indexes):
    if len(indexes):
        selected_categories = [categories[ind] for ind in indexes]
    else:
        selected_categories = categories
    update_source(selected_categories)


update_source(categories)

select = CheckboxButtonGroup(labels=categories)
select.on_click(filter_categories)

hover_year_with_usd = HoverTool(
    tooltips=[
        ("name", "@name"),
    ]
)

p_year_with_usd = figure(
    plot_height=200,
    tools=[hover_year_with_usd, "box_select", "reset"]
)

for state, color in zip(states, colors):
    p_year_with_usd.circle(
        x='x',
        y='y',
        line_color='white',
        fill_color=color,
        alpha=0.7,
        size=15,
        legend=state,
        source=sources_year_vs_usd[state]
    )


p_year_with_usd.xaxis.axis_label = "Date"
p_year_with_usd.yaxis.axis_label = "USD pledged"
# See http://bokeh.pydata.org/en/latest/docs/reference/models/formatters.html for all formatters
p_year_with_usd.xaxis.formatter = DatetimeTickFormatter()
p_year_with_usd.yaxis.formatter = NumeralTickFormatter(format="$0,0")
p_year_with_usd.legend.click_policy = 'hide'
p_year_with_usd.legend.location = "top_left"

p_year_with_usd.on_event(Reset, lambda _: update_source(categories))
# p_year_with_usd.on_event(SelectionGeometry, update_on_usd_vs_date_selection)

title = Div(text='<h1 style="text-align: center">Kickstarter Dashboard</h1>')
layout = column(title, select, p_year_with_usd, sizing_mode='scale_width')

curdoc().add_root(layout)

