from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

def inc_dec(Close, Open):
    if Close > Open:
        value = "Increase"
    elif Close < Open:
        value = "Decrease"
    else:
        value = "Equal"
    return value

start = datetime.datetime(2015,11,1)
end = datetime.datetime(2016,3,10)

df = data.DataReader(name="GOOG", data_source="google",start=start, end=end)

p = figure(x_axis_type = 'datetime', width=1000, height = 300, responsive = True)

p.title.text = "Google: %s - %s" %(str(start), str(end))
#p.grid.grid_line_alpha = 0.3

df["Status"] = [inc_dec(Close, Open) for Close, Open in zip(df.Close, df.Open)]

df["Middle"] = (df.Open + df.Close) / 2

df["Height"] = abs(df.Close - df.Open)

Hours_12 = 12 * 60 * 60 * 1000

p.segment(df.index, df.High, df.index, df.Low, color = "Black")

p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
       Hours_12, df.Height[df.Status == "Increase"], fill_color = "#CCFFFF", line_color = "black")

p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
       Hours_12, df.Height[df.Status == "Decrease"], fill_color = "#FF3333", line_color = "black")

output_file("StockGraph.html")

show(p)
