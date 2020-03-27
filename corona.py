from tkinter import *
from tkinter import messagebox
import COVID19Py
import pandas as pd
def fight_corona(conf_list):
    d = pd.DataFrame.from_dict(conf_list)
    d = pd.concat([d, d['coordinates'].apply(pd.Series),d['latest'].apply(pd.Series)], axis=1)
    d.drop(columns= ['coordinates', 'latest'], inplace= True)
    return d
def confirmed_wrld():
    conf_list = covid19.getLocations(rank_by='confirmed')
    df = fight_corona(conf_list)
    df.to_excel('confirmed.xlsx')
    messagebox.showinfo('Saved','The list is saved in confirmed.txt file in the same folder if you dont have confirmed.txt file create one in the same directory and redo this action')

def recovered_wrld():
    recovered_lst = covid19.getLocations(rank_by='recovered')
    df = fight_corona(conf_list)
    df.to_excel('recovered.xlsx')
    messagebox.showinfo('Saved',"The list is saved in recovered.txt file in the same folder if you dont have recovered.txt file create one in the same directory and redo this action")

def deaths_wrld():
    dth_lst = covid19.getLocations(rank_by='deaths')
    df = fight_corona(conf_list)
    df.to_excel('deaths.xlsx')
    messagebox.showinfo('Saved',"The list is saved in deaths.txt file in the same folder if you dont have deaths.txt file create one in the same directory and redo this action")
covid19 = COVID19Py.COVID19(data_source="csbs")
root = Tk()
root.geometry("500x500")
root.title("CoronaVirus Locator")
confirmed_BTN = Button(text="confirmed in the whole world", command = confirmed_wrld)
confirmed_BTN.pack()
recovered_BTN = Button(text="recovered in the whole world", command = recovered_wrld)
recovered_BTN.pack()
deaths_BTN = Button(text="deaths in the whole world", command = deaths_wrld)
deaths_BTN.pack()
root.mainloop()
