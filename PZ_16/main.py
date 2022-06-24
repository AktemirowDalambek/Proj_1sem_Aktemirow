import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='green', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="img/add.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить товар', command=self.open_dialog, bg='green', bd=0, fg='white',
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.edit_img = tk.PhotoImage(file="img/edit.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='green',
                                    bd=0, fg='white', compound=tk.TOP, image=self.edit_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="img/delete.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='green',
                               bd=0, fg='white', compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="img/search.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='green',
                               bd=0, fg='white', compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="img/update.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='green',
                                bd=0, fg='white', compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(
            'number', 'code', 'naimenovanie', 'naimenovaniemgz', 'zayavki', 'kol', 'edizm', 'optcost'), height=15,
                                 show='headings')

        self.tree.column('number', width=20, anchor=tk.CENTER)
        self.tree.column('code', width=100, anchor=tk.CENTER)
        self.tree.column('naimenovanie', width=100, anchor=tk.CENTER)
        self.tree.column('naimenovaniemgz', width=100, anchor=tk.CENTER)
        self.tree.column('zayavki', width=100, anchor=tk.CENTER)
        self.tree.column('kol', width=120, anchor=tk.CENTER)
        self.tree.column('edizm', width=100, anchor=tk.CENTER)
        self.tree.column('optcost', width=100, anchor=tk.CENTER)

        self.tree.heading('number', text='#')
        self.tree.heading('code', text='Код товара')
        self.tree.heading('naimenovanie', text='Товар')
        self.tree.heading('naimenovaniemgz', text='Магазин')
        self.tree.heading('zayavki', text='Заявки магазина')
        self.tree.heading('kol', text='Кол-во товара')
        self.tree.heading('edizm', text='Ед. измерения')
        self.tree.heading('optcost', text='Опт. цена')

        self.tree.pack()

    def records(self, number, code, naimenovanie, naimenovaniemgz, zayavki, kol, edizm, optcost):
        self.db.insert_data(number, code, naimenovanie, naimenovaniemgz, zayavki, kol, edizm, optcost)
        self.view_records()

    def update_record(self, number, code, naimenovanie, naimenovaniemgz, zayavki, kol, edizm, optcost):
        self.db.cur.execute(
            """UPDATE users SET number=?, code=?, naimenovanie=?, naimenovaniemgz=?, zayavki=?, kol=?, edizm=?, optcost=? WHERE number=?""",
            (number, code, naimenovanie, naimenovaniemgz, zayavki, kol, edizm, optcost, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE number=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, naimenovaniemgz):
        naimenovaniemgz = (naimenovaniemgz,)
        self.db.cur.execute("""SELECT * FROM users WHERE naimenovaniemgz=?""", naimenovaniemgz)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x250+400+300')
        self.resizable(False, False)

        label_number = tk.Label(self, text='#')
        label_number.place(x=50, y=1)
        self.number = ttk.Entry(self)
        self.number.place(x=170, y=1)

        label_code = tk.Label(self, text='Код товара')
        label_code.place(x=50, y=25)
        self.code = ttk.Entry(self)
        self.code.place(x=170, y=25)

        label_naimenovanie = tk.Label(self, text='Товар')
        label_naimenovanie.place(x=50, y=50)
        self.naimenovanie = ttk.Entry(self)
        self.naimenovanie.place(x=170, y=50)

        label_naimenovaniemgz = tk.Label(self, text='Магазин')
        label_naimenovaniemgz.place(x=50, y=75)
        self.entry_naimenovaniemgz = ttk.Combobox(self, values=[u'Пятерочка', u'Магнит', u'Перекресток',u'Читай-Город', u'Wallmart',
                                                u'Gucci', u'Hoff', u'Ikea', u'DNS'])
        self.entry_naimenovaniemgz.place(x=170, y=75)


        label_zayavki = tk.Label(self, text='Заявки магазина')
        label_zayavki.place(x=50, y=100)
        self.zayavki = ttk.Entry(self)
        self.zayavki.place(x=170, y=100)

        label_kol = tk.Label(self, text='Кол-во товара')
        label_kol.place(x=50, y=125)
        self.entry_kol = ttk.Entry(self)
        self.entry_kol.place(x=170, y=125)

        label_edizm = tk.Label(self, text='Ед. измерения')
        label_edizm.place(x=50, y=150)
        self.entry_edizm = ttk.Combobox(self, values=[u'Килограмм', u'Литров', u'Метров', u'Штук'])
        self.entry_edizm.place(x=170, y=150)

        label_optcost = tk.Label(self, text='Опт. цена')
        label_optcost.place(x=50, y=175)
        self.optcost = ttk.Entry(self)
        self.optcost.place(x=170, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=200)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=200)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.number.get(),
                                                                       self.code.get(),
                                                                       self.naimenovanie.get(),
                                                                       self.entry_naimenovaniemgz.get(),
                                                                       self.zayavki.get(),
                                                                       self.entry_kol.get(),
                                                                       self.entry_edizm.get(),
                                                                       self.optcost.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=200)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.number.get(),
                                                                          self.code.get(),
                                                                          self.naimenovanie.get(),
                                                                          self.entry_naimenovaniemgz.get(),
                                                                          self.zayavki.get(),
                                                                          self.entry_kol.get(),
                                                                          self.entry_edizm.get(),
                                                                          self.optcost.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        self.code_search = ttk.Combobox(self,
                                        values=[u'Пятерочка', u'Магнит', u'Перекресток',u'Читай-Город', u'Wallmart',
                                                u'Gucci', u'Hoff', u'Ikea', u'DNS'])
        self.code_search.place(x=60, y=20, width=200)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=70, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.code_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('OptovayaBaza.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                number INTEGER,
                code TEXT, 
                naimenovanie TEXT NOT NULL,
                naimenovaniemgz TEXT,
                zayavki INTEGER,
                kol INTEGER,
                edizm TEXT,
                optcost INTEGER
                )""")

    def insert_data(self, number, code, naimenovanie, naimenovaniemgz, zayavki, kol, edizm, optcost):
        self.cur.execute(
            """INSERT INTO users(number, code, naimenovanie, naimenovaniemgz, zayavki, kol, edizm, optcost) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (number, code, naimenovanie, naimenovaniemgz, zayavki, kol, edizm, optcost))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Oптовая База")
    root.geometry("1000x450+300+200")
    root.resizable(False, False)
    root.mainloop()