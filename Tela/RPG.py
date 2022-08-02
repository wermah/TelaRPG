import PySimpleGUI as sg
import random
import math

rolls = 0
lados = 0
gold = 0
newGold = 0
lifeMax = 0
life = 0
level = 0
levelAtual = 0
xp = 0
newXp = 0
level1 = 0
level2 = 300
level3 = 900
level4 = 2700
level5 = 6500
level6 = 14000
level7 = 23000
level8 = 34000
level9 = 48000
level10 = 64000
level11 = 85000
level12 = 100000
level13 = 120000
level14 = 140000
level15 = 165000
level16 = 195000
level17 = 225000
level18 = 265000
level19 = 305000
level20 = 355000

sg.change_look_and_feel('DarkBlue4')

parteLevel = [
    [sg.Text('Quantos pontos de experiência você tem?'), sg.Input(key = '-INPUT_XP-')],
    [sg.Text('', key='-BARRA_LEVEL-')],
    [sg.Button('Salvar Level', key = '-CONFIRMAR_LEVEL-'), sg.Button('Limpar', key = '-LIMPAR_XP-')],
    [sg.Text('Receber XP'), sg.Input(key='-INPUT_NEWXP-')],
    [sg.Button('Receber', key = '-RECEBER_XP-')]
]

parteVida = [
    [sg.Text('Qual seu HP máximo? ', key = '-LIFE-'), sg.Input(key = '-INPUT_LIFE-')],
    [sg.Button('-', key = '-PERDER_LIFE-'), sg.Text('', key = '-LIFE_ATUAL-'), sg.Button('+', key = '-GANHAR_LIFE-'), sg.Text(size=(10,0)), sg.Button('Ok', key = '-CONFIRMAR_LIFE-')]
]

parteGold = [
    [sg.Text('Qual sua quantidade atual de gold?', key = '-QTD_GOLD-'),sg.Text('', size = (12, 0)) , sg.Input(key = '-INPUT_QTD_GOLDS-')],
    [sg.Text('', key='-GOLDS_PLAYER-')],
    [sg.Button('Salvar número de golds', key = '-BUTTON_GOLDS-')], 
    [sg.Button('+10', key = '-BUTTON_+10-'),
    sg.Button('+5', key = '-BUTTON_+5-'), 
    sg.Button('+1', key = '-BUTTON_+1-'),
    sg.Button('-1', key = '-BUTTON_-1-'),
    sg.Button('-5', key = '-BUTTON_-5-'),
    sg.Button('-10', key = '-BUTTON_-10-')]
]

parteDado = [
    [sg.Text('Quantas jogadas você deseja fazer? ', size = (40, 0)), sg.Input( key='-ROLLS-' )],
    [sg.Text('Quantos lados o dado que você irá jogar deve ter? ', size=(40, 0)), sg.Input( key='-LADOS-' )],
    [sg.Button('Rodar', size = (80, 0), key='-RODAR-')]
]

layout = [ 
    [sg.Frame('Rolar Dados', parteDado, key ='-CONTAINERDADO-')],
    [sg.Output(size=(90, 10), key='-OUTPUT-')],
    [sg.Frame('Life', parteVida, key = 'CONTAINERVIDA')],
    [sg.Frame('Golds', parteGold, key = '-CONTAINERGOLD-')],
    [sg.Frame('Levels', parteLevel, key = '-CONTAINERLEVEL-')]
]

# Janela
janela = sg.Window('Rolagem de dados', layout = layout, resizable=True)    


while True:
    # Extrair dados da tela
    event, values = janela.Read()
    if event == sg.WIN_CLOSED:
        break    

    # Rolagem de dados

    if values['-ROLLS-'] == '' or values['-LADOS-'] == '':    
        pass
    else:    
        rolls = int(values['-ROLLS-'])
        lados = int(values['-LADOS-'])

    resultado = []
    qtd_jogadas = 0

    while rolls > qtd_jogadas:
        resultado.append(random.randint(1, lados))
        qtd_jogadas += 1

    if event == '-RODAR-':
        if rolls != 0 or lados != 0:
            print(f'{rolls}d{lados}: {resultado}, soma={sum(resultado)}')
        else:
            pass    

    # Contagem de gold

    
    if levelAtual > 0:
        level = levelAtual

    if event == '-BUTTON_GOLDS-':
        gold = int(values['-INPUT_QTD_GOLDS-']) 
        newGold = gold
        janela['-GOLDS_PLAYER-'].update(f'Você tem {gold} golds!!')

    if event == '-BUTTON_+1-':
        newGold += 1
        janela['-GOLDS_PLAYER-'].update(f'Você tem {newGold} golds!!')
        janela['-INPUT_QTD_GOLDS-'].update(f'{newGold}')

    if event == '-BUTTON_+5-':
        newGold += 5
        janela['-GOLDS_PLAYER-'].update(f'Você tem {newGold} golds!!')
        janela['-INPUT_QTD_GOLDS-'].update(f'{newGold}')        

    if event == '-BUTTON_+10-':
        newGold += 10
        janela['-GOLDS_PLAYER-'].update(f'Você tem {newGold} golds!!')
        janela['-INPUT_QTD_GOLDS-'].update(f'{newGold}')

    if event == '-BUTTON_-1-':
        newGold -= 1
        janela['-GOLDS_PLAYER-'].update(f'Você tem {newGold} golds!!')
        janela['-INPUT_QTD_GOLDS-'].update(f'{newGold}')

    if event == '-BUTTON_-5-':
        newGold -= 5
        janela['-GOLDS_PLAYER-'].update(f'Você tem {newGold} golds!!')
        janela['-INPUT_QTD_GOLDS-'].update(f'{newGold}')

    if event == '-BUTTON_-10-':
        newGold -= 10
        janela['-GOLDS_PLAYER-'].update(f'Você tem {newGold} golds!!')
        janela['-INPUT_QTD_GOLDS-'].update(f'{newGold}')

    # Life
    
    if event == '-CONFIRMAR_LIFE-':
        lifeMax = int(values['-INPUT_LIFE-'])
        life = lifeMax
        janela['-LIFE_ATUAL-'].update(f'Sua vida atual é de {life}/{lifeMax}')

    if event == '-PERDER_LIFE-':
        life -= 1
        janela['-LIFE_ATUAL-'].update(f'Sua vida atual é de {life}/{lifeMax}')

    if event == '-GANHAR_LIFE-':
        if life < lifeMax:
            life += 1
            janela['-LIFE_ATUAL-'].update(f'Sua vida atual é de {life}/{lifeMax}')
        else:
            pass

    # Level

    list_levels = [level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12, level13, level14, level15, level16, level17, level18, level19, level20]    

    if values['-INPUT_NEWXP-'] != '':
        if event == '-RECEBER_XP-':
            newXp = int(values['-INPUT_NEWXP-'])
            xp = xp + newXp
    

    if values['-INPUT_XP-'] != '':
        if event == '-CONFIRMAR_LEVEL-':
            xp = int(values['-INPUT_XP-'])
            if (xp - level1) > 0 and (xp - level2) < 0:
                restante = (xp - level2) * (-1)
                level = 1
            if (xp - level2) > 0 and (xp - level3) < 0:
                restante = (xp - level3) * (-1)
                level = 2
            if (xp - level3) > 0 and (xp - level4) < 0:
                restante = (xp - level4) * (-1)
                level = 3
            if (xp - level4) > 0 and (xp - level5) < 0:
                restante = (xp - level5) * (-1)
                level = 4
            if (xp - level5) > 0 and (xp - level6) < 0:
                restante = (xp - level6) * (-1)
                level = 5
            if (xp - level6) > 0 and (xp - level7) < 0:
                restante = (xp - level7) * (-1)
                level = 6
            if (xp - level7) > 0 and (xp - level8) < 0:
                restante = (xp - level8) * (-1)
                level = 7
            if (xp - level8) > 0 and (xp - level9) < 0:
                restante = (xp - level9) * (-1)
                level = 8
            if (xp - level9) > 0 and (xp - level10) < 0:
                restante = (xp - level10) * (-1)
                level = 9
            if (xp - level10) > 0 and (xp - level11) < 0:
                restante = (xp - level11) * (-1)
                level = 10
            if (xp - level11) > 0 and (xp - level12) < 0:
                restante = (xp - level12) * (-1)
                level = 11
            if (xp - level12) > 0 and (xp - level13) < 0:
                restante = (xp - level13) * (-1)
                level = 12
            if (xp - level13) > 0 and (xp - level14) < 0:
                restante = (xp - level14) * (-1)
                level = 13
            if (xp - level14) > 0 and (xp - level15) < 0:
                restante = (xp - level15) * (-1)
                level = 14
            if (xp - level15) > 0 and (xp - level16) < 0:
                restante = (xp - level16) * (-1)
                level = 15
            if (xp - level16) > 0 and (xp - level17) < 0:
                restante = (xp - level17) * (-1)
                level = 16
            if (xp - level17) > 0 and (xp - level18) < 0:
                restante = (xp - level18) * (-1)
                level = 17
            if (xp - level18) > 0 and (xp - level19) < 0:
                restante = (xp - level19) * (-1)
                level = 18
            if (xp - level19) > 0 and (xp - level20) < 0:
                restante = (xp - level20) * (-1)
                level = 19
            if (xp - level20) > 0:
                level = 20
            janela['-BARRA_LEVEL-'].update(f'Você está no nível {level} com {xp} de pontos de experiência! Faltam {restante} de pontos de experiência para upar!')     
            
        if event == '-RECEBER_XP-':

            janela['-BARRA_LEVEL-'].update(f'Você está no nível {level} com {xp} de pontos de experiência! Faltam {restante} de pontos de experiência para upar!')


        else:
            pass
    else:
        pass

    if event == '-LIMPAR_XP-':    
        janela['-BARRA_LEVEL-'].update(f'')
        values['-INPUT_XP-'] = ''
        values['-INPUT_NEWXP-'] = ''
                                          
janela.close()
