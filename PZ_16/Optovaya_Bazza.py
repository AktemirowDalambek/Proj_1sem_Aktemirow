from tkinter import ttk
import tkinter as tk

class Optovaya_Bazza(tk.Toplevel):

 """Класс для дочернего окна"""

 def __init__(self, root, app):
     super().__init__(root)
     self.init_Optovaya_Bazza()
     self.view = app

 def init_Optovaya_Bazza(self):
     self.title('Добавить игрока')
     self.geometry('400x220+400+300')
     self.resizable(False, False)

     label_description = tk.Label(self, text='Номер')
     label_description.place(x=50, y=25)
     self.entry_description = ttk.Entry(self)
     self.entry_description.place(x=110, y=25)

     label_name = tk.Label(self, text='Имя')
     label_name.place(x=50, y=50)
     self.entry_name = ttk.Entry(self)
     self.entry_name.place(x=110, y=50)

     label_sex = tk.Label(self, text='Пол')
     label_sex.place(x=50, y=75)
     self.combobox = ttk.Combobox(self, values=[u'Мужской', u'Женский'])
     self.combobox.current(0)

     self.combobox.place(x=110, y=75)
     label_old = tk.Label(self, text='Возраст')
     label_old.place(x=50, y=100)
     self.entry_old = ttk.Entry(self)

     label_score = tk.Label(self, text='Результат')
     label_score.place(x=50, y=125)

     self.entry_score = ttk.Entry(self)
     self.entry_score.place(x=110, y=125)

     self.entry_old.place(x=110, y=100)
     btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
     btn_cancel.place(x=300, y=170)
     self.btn_ok = ttk.Button(self, text='Добавить')

     self.btn_ok.place(x=220, y=170)
     self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                    self.entry_name.get(),
                                                                    self.combobox.get(),
                                                                    self.entry_old.get(),
                                                                    self.entry_score.get()))

     self.grab_set()
     self.focus_set()