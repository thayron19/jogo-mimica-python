import random
import tkinter
import keyboard


# ---------------------------------------------------------------------------------------------------------------------
def sorteia():

    global cancel

    tempo_texto['foreground'] = '#1bbf3e'
    palavra_texto['foreground'] = '#1bbf3e'

    if len(lista) != 0:
        num_sorte = random.randint(0, len(lista) - 1)

        palavra_texto['text'] = lista[num_sorte]

        del lista[num_sorte]

        if len(lista) == 1:
            jogo_texto['text'] = f'{len(lista)} verbo restante'
        elif len(lista) == 0:
            jogo_texto['text'] = 'Último verbo!'
        else:
            jogo_texto['text'] = f'{len(lista)} verbos restantes'

        if cancel != '':
            janela.after_cancel(cancel)

        cronometro(91)

    else:
        palavra_texto['text'] = 'Fim do jogo'
        tempo_texto['text'] = ''
        jogo_texto['text'] = ''
        janela.after_cancel(cancel)
        jogo_btn.destroy()


# ---------------------------------------------------------------------------------------------------------------------
def cronometro(sec):

    global cancel

    if sec == 0:
        tempo_texto['text'] = 'Tempo esgotado!'

    else:
        sec = sec - 1
        tempo_texto['text'] = sec
        cancel = janela.after(1000, lambda: cronometro(sec))

        if sec < 30:
            tempo_texto['foreground'] = '#bf231b'
            palavra_texto['foreground'] = '#bf231b'

        elif sec < 60:
            tempo_texto['foreground'] = '#bfbc1b'
            palavra_texto['foreground'] = '#bfbc1b'


# ---------------------------------------------------------------------------------------------------------------------
lista = ['abolir', 'abraçar', 'abrir', 'abster-se', 'acabar', 'aceitar', 'acender', 'acender', 'achar', 'achar-se',
         'aconselhar', 'acontecer', 'acreditar', 'adequar', 'aderir', 'adoecer', 'adquirir', 'agradar', 'agradecer',
         'aguerrir', 'almoçar', 'alvorecer', 'amanhecer', 'amar', 'andar', 'anoitecer', 'ansiar', 'ansiar', 'aparecer',
         'apiedar-se', 'aprazer', 'aprender', 'apresentar', 'arrepender-se', 'assistir', 'atinar', 'atirar', 'atirar',
         'atribuir', 'atribuir-se', 'atropelar', 'aturdir', 'avisar', 'banir', 'barbear-se', 'bastar', 'beber',
         'bramar', 'brilhar', 'brincar', 'caber', 'cacarejar', 'cair', 'caminhar', 'cantar', 'carecer', 'casar',
         'causar', 'ceder', 'chamar', 'chega', 'chegar', 'chorar', 'chover', 'chuviscar', 'coaxar', 'cobrir', 'colorir',
         'combalir', 'começar', 'comedir', 'comemorar', 'comer', 'comparecer', 'complicar', 'compor', 'comprar',
         'compreender', 'comunicar', 'concernir', 'concordar', 'condoer', 'condoer-se', 'confiar', 'confundir',
         'conseguir', 'conspirar', 'constar', 'construir', 'contar', 'contentar-se', 'continuar', 'contribuir',
         'conversar', 'convidar', 'convir', 'correr', 'corrigir', 'cortar', 'cortar-se', 'costumar', 'costurar', 'crer',
         'crer', 'crescer', 'cricrilar', 'cuidar', 'cumprir', 'custar', 'dançar', 'dar', 'debater', 'debater-se',
         'decidir', 'deitar', 'deitar-se', 'deixar', 'delinquir', 'demolir', 'demorar', 'depender', 'derrubar',
         'descobrir', 'desculpar', 'desfrutar', 'desistir', 'destruir', 'dever', 'devolver', 'dignar-se', 'discutir',
         'dividir', 'dizer', 'doar', 'doer', 'dormir', 'duvidar', 'eleger', 'elogiar', 'emendar-se', 'emitir',
         'empedernir', 'emprestar', 'encontrar', 'encontrar-se', 'encostar-se', 'enganar-se', 'ensinar', 'entrar',
         'entregar', 'entregar', 'envolver', 'envolver-se', 'enxaguar', 'esbaforir', 'escolher', 'escrever', 'esculpir',
         'escurecer', 'esperar', 'esquecer-se', 'estar', 'estiar', 'estrear', 'estudar', 'exaurir', 'exercer',
         'expelir', 'explicar', 'explodir', 'expressar', 'exprimir', 'expulsar', 'extinguir', 'extorquir', 'falar',
         'falir', 'fazer', 'feder', 'ferir-se', 'ficar', 'fingir', 'florir', 'frigir', 'fugir', 'ganhar', 'ganir',
         'garantir', 'garoar', 'gostar', 'grassar', 'haver', 'imitar', 'impingir', 'importar', 'imprimir', 'imprimir',
         'inchar', 'incluir', 'influenciar', 'informar', 'ingressar', 'insistir', 'interessar', 'intrometer-se',
         'invadir', 'ir', 'jogar', 'ladrar', 'latir', 'lavar-se', 'lembrar-se', 'ler', 'levantar', 'levantar-se',
         'levar', 'limpar', 'lutar', 'mandar', 'matar', 'medir', 'mentir', 'merecer', 'miar', 'morar', 'morrer',
         'morrer', 'mudar', 'mugir', 'murchar', 'nadar', 'namorar', 'narrar', 'nascer', 'necessitar', 'nevar',
         'obedecer', 'ocorrer', 'oferecer', 'ofertar', 'olhar', 'olhar-se', 'orvalhar', 'ouvir', 'pagar', 'parar',
         'parecer', 'participar', 'partir', 'passar', 'passear', 'pedir', 'pegar', 'pensar', 'pentear-se', 'perder',
         'perdoar', 'perguntar', 'permanecer', 'permitir', 'perseguir', 'pilotar', 'pintar', 'pintar-se', 'poder',
         'polir', 'pôr', 'pôr-se', 'precaver', 'precisar', 'prender', 'preocupar-se', 'prescindir', 'pretender',
         'proceder', 'produzir', 'progredir', 'prometer', 'propor', 'proporcionar', 'pular', 'puxar', 'quebrar',
         'queixar-se', 'querer', 'questionar', 'reaver', 'receber', 'recorrer', 'relampejar', 'relatar', 'remediar',
         'renhir', 'resistir', 'responder', 'ressequir', 'retorquir', 'revolver', 'rir', 'rosnar', 'ruir', 'saber',
         'saber', 'sacudir', 'sair', 'salvar', 'saraivar', 'sentar', 'sentar-se', 'sentir', 'ser', 'servir',
         'simpatizar', 'sofrer', 'sonhar', 'suar', 'submergir', 'suceder', 'suceder', 'suicidar-se', 'sumir',
         'suspender', 'tentar', 'ter', 'tornar', 'tornar-se', 'trabalhar', 'tratar', 'trazer', 'tremer', 'trovejar',
         'urgir', 'usar', 'valer', 'varrer', 'vazar', 'vencer', 'vender', 'ventar', 'ver', 'vestir-se', 'viajar', 'vir',
         'virar', 'visitar', 'viver', 'voltar', 'votar', 'zangar-se', 'zombar', 'zurrar']
# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('Mímica')

largura_janela = 300
altura_janela = 190

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicaol = float(largura_janela / 2 - largura_tela / 2)
posicaoa = float(altura_janela / 2 - altura_tela / 2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posicaol, posicaoa))
janela.resizable(width=False, height=False)
# ---------------------------------------------------------------------------------------------------------------------
cancel = ''
# ---------------------------------------------------------------------------------------------------------------------
jogo_texto = tkinter.Label(janela, text='351 verbos restantes', font=('', 12), justify='center')
jogo_texto.place(x=0, y=10, width=300)
# ---------------------------------------------------------------------------------------------------------------------
jogo_btn = tkinter.Button(janela, text='Sortear', command=lambda: sorteia(), font=('', 20), bg='#45e610')
jogo_btn.place(x=50, y=40, width=200, height=40)
# ---------------------------------------------------------------------------------------------------------------------
palavra_texto = tkinter.Label(janela, text='', font=('', 25), justify='center')
palavra_texto.place(x=0, y=85, width=300)
# ---------------------------------------------------------------------------------------------------------------------
tempo_texto = tkinter.Label(janela, font=('', 25), justify='center')
tempo_texto.place(x=0, y=130, width=300)
# ---------------------------------------------------------------------------------------------------------------------
keyboard.on_press_key('ENTER', lambda _: sorteia())
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()
