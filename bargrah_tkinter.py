from tkinter import *
import plotly.graph_objects as go

window = Tk()

window.title("Kilowatt hours cost calculator")

window.geometry('400x100')

lbl = Label(window, text="Input kW Hours")

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)


def grapher(num):
    arr = []

    # 0 off
    allon = num * .0831

    # 20 off
    off = num * .2
    on = num * .8
    off = off * .0155
    on = on * .0831
    off = off + on  # this will be the total bar for 20/80 split

    # 40 off
    offfourty = num * .4
    onfourty = num * .6
    offfourty = offfourty * .0155
    onfourty = onfourty * .0831
    offfourty = offfourty + onfourty

    # 60 off
    offsix = num * .6
    onsix = num * .4
    offsix = offsix * .0155
    onsix = onsix * .0831
    offsix = offsix + onsix

    # 80 off
    offe = num * .8
    one = num * .2
    offe = offe * .0155
    one = one * .0831
    offe = offe + one

    # 100 off
    alloff = num
    alloff = alloff * .0155

    arr.append(allon)
    arr.append(off)
    arr.append(offfourty)
    arr.append(offsix)
    arr.append(offe)
    arr.append(alloff)

    # ----From this point is June-August calculations----#
    aarr = []

    # 0 off
    oallon = num * .2197

    # 20 off
    ooff = num * .2
    oon = num * .8
    ooff = ooff * .0155
    oon = oon * .2197
    ooff = ooff + oon  # this will be the total bar for 20/80 split

    # 40 off
    oofffourty = num * .4
    oonfourty = num * .6
    oofffourty = oofffourty * .0155
    oonfourty = oonfourty * .2197
    oofffourty = oofffourty + oonfourty

    # 60 off
    ooffsix = num * .6
    oonsix = num * .4
    ooffsix = ooffsix * .0155
    oonsix = oonsix * .2197
    ooffsix = ooffsix + oonsix

    # 80 off
    ooffe = num * .8
    oone = num * .2
    ooffe = ooffe * .0155
    oone = oone * .2197
    ooffe = ooffe + oone

    # 100 off
    oalloff = num
    oalloff = oalloff * .0155

    aarr.append(oallon)
    aarr.append(ooff)
    aarr.append(oofffourty)
    aarr.append(ooffsix)
    aarr.append(ooffe)
    aarr.append(oalloff)

    percent_vals = [0, 20, 40, 60, 80, 100]

    fig = go.Figure(data=[go.Bar(name='June through August', y=aarr, x=percent_vals, marker_color='maroon',
                                 hovertext=['0% Offpeak', '20% off vs 80% on', '40% off vs 60% on', '60% off vs 40% on',
                                            '80% off vs 20% on', '100% off']),
                          go.Bar(name='September through May', y=arr, x=percent_vals,
                                 hovertext=['0% Offpeak', '20% off vs 80% on', '40% off vs 60% on', '60% off vs 40% on',
                                            '80% off vs 20% on', '100% off'])])

    fig.update_layout(
        title_text="Cost of Kilowatt Hours Based on Onpeak vs Offpeak Percentage June-August vs Sept-May",
        xaxis=dict(title='Percentage used during Offpeak'),
        yaxis=dict(title='Cost in Dollars ($)'))
    fig.show()


def clicked():  # for off months
    grapher(int(txt.get()))

    # print (int(txt.get()) + 5)

    # res = "Welcome to " + txt.get()

    # lbl.configure(text= res)


btn = Button(window, text="Calculate costs Summer vs September-May", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()