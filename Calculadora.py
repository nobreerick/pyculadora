import PySimpleGUI as sg

class Tela_Principal:
    def __init__(self):
        
        layout = [
            [sg.Output(size=(25,7), k='-OUTPUT-', pad=(0,0))],
            [sg.Button('%',size=(5,2),k=('-%-'), pad=(0,0)),\
                sg.Button('',size=(5,2),k=('-1,2-'), pad=(0,0), disabled=True, button_color=('white', '#8999a1')),\
                sg.Button('Voltar',size=(5,2),k=('-BACK-'), pad=(0,0)), sg.Button('Limpar',size=(5,2),k=('-CLEAR-'), pad=(0,0))],
            [sg.Button('1/x',size=(5,2),k=('-INVERT-'), pad=(0,0)), sg.Button('x²',size=(5,2),k=('-SQR-'), pad=(0,0)),\
                sg.Button('root(x)',size=(5,2),k=('-ROOT-'), pad=(0,0)), sg.Button('/',size=(5,2),k=('-/-'), pad=(0,0))],
            [sg.Button('7',size=(5,2),k=('7'), pad=(0,0)), sg.Button('8',size=(5,2),k=('8'), pad=(0,0)),\
                sg.Button('9',size=(5,2),k=('9'), pad=(0,0)), sg.Button('*',size=(5,2),k=('-*-'), pad=(0,0))],
            [sg.Button('4',size=(5,2),k=('4'), pad=(0,0)), sg.Button('5',size=(5,2),k=('5'), pad=(0,0)),\
                sg.Button('6',size=(5,2),k=('6'), pad=(0,0)), sg.Button('-',size=(5,2),k=('---'), pad=(0,0))],
            [sg.Button('1',size=(5,2),k=('1'), pad=(0,0)), sg.Button('2',size=(5,2),k=('2'), pad=(0,0)),\
                sg.Button('3',size=(5,2),k=('3'), pad=(0,0)), sg.Button('+',size=(5,2),k=('-+-'), pad=(0,0))],
            [sg.Button('+/-',size=(5,2),k=('-+/--'), pad=(0,0)), sg.Button('0',size=(5,2),k=('-0-'), pad=(0,0)),\
                sg.Button('',size=(5,2),k=('-6,3-'), pad=(0,0), disabled=True, button_color=('white', '#8999a1')),\
                sg.Button('=',size=(5,2),k=('-=-'), pad=(0,0), button_color='yellow on green')]
        ]
        
        
        self.window = sg.Window('calculadora', layout)


    def Executar_Tela(self):
        num01 = []
        while True:            
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            elif event == '-CLEAR-':
                self.window['-OUTPUT-']('')
            elif event == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
                num01.append(event)
                print(num01)

        self.window.close()

class Calculadora:    
    def Porcentagem(self, num01, num02):
        porc = int(num01)/100
        resultado = porc*int(num02)
        return resultado

    def Inversor(self, num01):
        resultado = 1/int(num01)
        return resultado

    def Potencia2(self, num01):
        resultado = int(num01)**2
        return resultado
    
    def Raiz2(self, num01):
        resultado = int(num01)**(1/2)
        return resultado
    
    def Divisao(self, num01, num02):
        resultado = int(num01)/int(num02)
        return resultado
    
    def Multiplicacao(self, num01, num02):
        resultado = int(num01)*int(num02)
        return resultado

    def Subtracao(self, num01, num02):
        resultado = int(num01)-int(num02)
        return resultado

    def Soma(self, num01, num02):
        resultado = int(num01)+int(num02)
        return resultado
        

    
Tela = Tela_Principal()
Tela.Executar_Tela()