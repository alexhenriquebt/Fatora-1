#Algoritmo com interface para fatorar polinômios
from sympy.abc import x
from sympy import factor, sympify, pretty
from tkinter import *

def fatorar_exibir():
    try:
        entrada_texto = entrada.get()
        polinomio = sympify(entrada_texto)
        fatorado = factor(polinomio)
        resultado = f'''
        Expressão: {entrada_texto}
        Interpretado: {polinomio}
        Expressão fatorada: {fatorado}
        '''
        resultado_fatoracao.config(text=resultado)
    except Exception as e:
        resultado_fatoracao.config(text='erro ao fatorar! Verifique se digitou o polinômio corretamente')

janela = Tk()
janela.title('Fatora-1(fatorador de polinômios)')
janela.geometry('400x350')
janela.resizable(False, False)


texto_orientacao = Label(janela, text='Digite o polinômio para ser fatorado (ex.: x**2 + 5*1/2 - 1): ')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

entrada = Entry(janela, width=20)
entrada.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="executar", command=fatorar_exibir)
botao.grid(column=0, row=2, padx=10, pady=10)

resultado_fatoracao = Label(janela, text='Resultado aparecerá aqui!')
resultado_fatoracao.grid(column=0, row=3, padx=5, pady=5)


janela.mainloop()