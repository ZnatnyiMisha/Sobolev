from tkinter import *
import requests
def parser(nazvanie):
    lm=Label(root)
    lm.destroy()
    request=requests.get(url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing').json()
    for i in request['data']['cryptoCurrencyList']:
        if nazvanie == i.get('name'):
            nazv=i['name']
            cena=i['quotes'][0]['price']
            lm=Label(root,text=f'Название: {nazv}\n' \
                   f'Цена: {round(cena,2)}$', bg='#F28165', font=('MV Boli', 14, 'bold'))
            lm.place(x=110,y=5)


root=Tk()
root.title('Парсер COINMARKETCAP'
root.resizable(height=False,width=False)
root.geometry('400x400')
root['bg']='#C7EECA'
s=StringVar()
m=Entry(root,textvariable=s,bg='#8A4A3A', font=('MV Boli', 12, 'bold'))
m.place(x=85,y=100)
h=Button(root,text='Начать!', bg='#AA43E4',font=('MV Boli', 14,'bold'), command=lambda: parser(s.get()))
h.place(x=157, y=250)
root.mainloop()