from tkinter import *# библиотека предназначенная для создания окна приложения
import requests # библиотека предназначенная для сбора информации со страниц интернета
def parser(nazvanie):
    """Функция сбора информации с сайта или же просто парсер"""
    lm=Label(root) # переменная созданная для того чтобы метка удалялась при запуске парсинга
    lm.destroy() # удаление метки после нажатия кнопки
    request=requests.get(url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing').json()
    for i in request['data']['cryptoCurrencyList']: # перебор json словаря
        if nazvanie == i.get('name'): # проверка и сравнение введеного значение с названием криптовалюты
            nazv=i['name'] # переменная с названием криптовалюты
            cena=i['quotes'][0]['price'] # переменная с ценой
            lm=Label(root,text=f'Название: {nazv}\n' \
                   f'Цена: {round(cena,2)}$', bg='#F28165', font=('MV Boli', 14, 'bold')) # метка с ценой и названием введеной валюты
            lm.place(x=110,y=5)#расположение метки

"""Данная часть предназначена для создания окна приложения"""
root=Tk()# предназанчена для создания и работы окна
root.title('Парсер COINMARKETCAP') # название программы
root.resizable(height=False,width=False) # нельзя менять размеры окна приложения
root.geometry('400x400') # установленные размеры приложения
root.iconphoto(True, PhotoImage(file='icon.png'))# предназначена для установления значка приложения
root['bg']='#C7EECA' # цвет окна приложения
s=StringVar() # переменная со значением из поля ввода
m=Entry(root,textvariable=s,bg='#8A4A3A', font=('MV Boli', 12, 'bold')) # поле ввода
m.place(x=85,y=100)#расположение поля ввода
h=Button(root,text='Начать!', bg='#AA43E4',font=('MV Boli', 14,'bold'), command=lambda: parser(s.get())) #кнопка с функцией парсинга
h.place(x=157, y=250)#расположение кнопки
root.mainloop()# предназанчена для создания и работы окна