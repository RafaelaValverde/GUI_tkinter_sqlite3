import tkinter as tk
from tkinter import messagebox
from db_alunos import Database

db = Database('alunos.db')


def add_item():
    if nome_txt.get() == '' or endereco_txt.get() == '' or curso_txt.get() == '' or rg_txt.get() == '' or ra_txt.get() == '':
        messagebox.showerror('Campos Obrigatórios',
                             'Por favor, preencha todos os campos')
        return
    db.insert(nome_txt.get(), endereco_txt.get(),
              curso_txt.get(), rg_txt.get(), ra_txt.get())
    messagebox.showinfo('Confirmação', 'Aluno cadastrado com sucesso!')
    clear_text()


def clear_text():
    nome_txt.delete(0, 'end')
    endereco_txt.delete(0, 'end')
    curso_txt.delete(0, 'end')
    ra_txt.delete(0, 'end')
    rg_txt.delete(0, 'end')


root = tk.Tk()

root.title('CADASTRO DE ALUNOS')
root.geometry('645x270')
root.configure(background='#dde')

nome_label = tk.Label(
    root, text='Nome Completo:', background='#dde', foreground='#009', anchor='w')
nome_label.place(x=30, y=20, width=200, height=30)

nome_txt = tk.Entry(root)
nome_txt.place(x=30, y=48, width=270, height=30)
nome_txt.focus()

endereco_label = tk.Label(
    root, text='Endereço:', background='#dde', foreground='#009', anchor='w')
endereco_label.place(x=30, y=90, width=200, height=30)

endereco_txt = tk.Entry(root)
endereco_txt.place(x=30, y=118, width=270, height=30)

curso_label = tk.Label(
    root, text='Curso:', background='#dde', foreground='#009', anchor='w')
curso_label.place(x=330, y=20, width=200, height=30)

curso_txt = tk.Entry(root)
curso_txt.place(x=330, y=48, width=280, height=30)

rg_label = tk.Label(
    root, text='RG:', background='#dde', foreground='#009', anchor='w')
rg_label.place(x=330, y=90, width=200, height=30)

rg_txt = tk.Entry(root)
rg_txt.place(x=330, y=118, width=130, height=30)

ra_label = tk.Label(
    root, text='RA:', background='#dde', foreground='#009', anchor='w')
ra_label.place(x=480, y=90, width=200, height=30)

ra_txt = tk.Entry(root)
ra_txt.place(x=480, y=118, width=130, height=30)

# Botões
add_btn = tk.Button(root, text='Cadastrar Aluno', command=add_item)
add_btn.place(x=30, y=180, width=150, height=30)

clear_btn = tk.Button(root, text='Limpar Campos', command=clear_text)
clear_btn.place(x=330, y=180, width=150, height=30)

# Start program
root.mainloop()
