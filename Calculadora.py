import PySimpleGUI as sg


class Tela_Principal:
    def __init__(self):

        layout = [
            [sg.Output(size=(25, 7), k='-OUTPUT-', pad=(0, 0))],
            [sg.Button('%', size=(5, 2), k=('-%-'), pad=(0, 0)),
             sg.Button('', size=(5, 2), k=('-1,2-'), pad=(0, 0),
                       disabled=True, button_color='yellow on gray'),
             sg.Button('Voltar', size=(5, 2), k=('-BACK-'), pad=(0, 0)),
             sg.Button('Limpar', size=(5, 2), k=('-CLEAR-'), pad=(0, 0))],
            [sg.Button('1/x', size=(5, 2), k=('-1/x-'), pad=(0, 0)),
             sg.Button('x²', size=(5, 2), k=('-x²-'), pad=(0, 0)),
             sg.Button('²√x', size=(5, 2), k=('-²√-'), pad=(0, 0)),
             sg.Button('÷', size=(5, 2), k=('-÷-'), pad=(0, 0))],
            [sg.Button('7', size=(5, 2), k=('7'), pad=(0, 0)),
             sg.Button('8', size=(5, 2), k=('8'), pad=(0, 0)),
             sg.Button('9', size=(5, 2), k=('9'), pad=(0, 0)),
             sg.Button('x', size=(5, 2), k=('-x-'), pad=(0, 0))],
            [sg.Button('4', size=(5, 2), k=('4'), pad=(0, 0)),
             sg.Button('5', size=(5, 2), k=('5'), pad=(0, 0)),
             sg.Button('6', size=(5, 2), k=('6'), pad=(0, 0)),
             sg.Button('-', size=(5, 2), k=('---'), pad=(0, 0))],
            [sg.Button('1', size=(5, 2), k=('1'), pad=(0, 0)),
             sg.Button('2', size=(5, 2), k=('2'), pad=(0, 0)),
             sg.Button('3', size=(5, 2), k=('3'), pad=(0, 0)),
             sg.Button('+', size=(5, 2), k=('-+-'), pad=(0, 0))],
            [sg.Button('+/-', size=(5, 2), k=('-+/--'), pad=(0, 0)),
             sg.Button('0', size=(5, 2), k=('0'), pad=(0, 0)),
             sg.Button('.', size=(5, 2), k=('-.-'), pad=(0, 0)),
             sg.Button('=', size=(5, 2), k=('-=-'), pad=(0, 0),
                       button_color='yellow on green')]
        ]

        self.window = sg.Window('calculadora', layout)

    def Executar_Tela(self):
        operacao = Operacoes()
        num01 = []
        num02 = []
        num01exten = ''
        num02exten = ''
        resultado = ''
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            elif event.isnumeric():
                num01.append(event)
                num01exten = ''.join(num01)
                resultado = num01exten
                self.window['-OUTPUT-'](num01exten)
            elif event == '-.-':
                if '.' not in num01 and num01 != []:
                    num01.append('.')
                    num01exten = ''.join(num01)
                    self.window['-OUTPUT-'](num01exten)
                    resultado = num01exten
                else:
                    pass
            elif event == '-%-':
                self.window['-OUTPUT-'](f'{num01exten}% de')
                while True:
                    event, values = self.window.read()
                    if event.isnumeric():
                        print(num02)
                        num02.append(event)
                        print(num02)
                        num02exten = ''.join(num02)
                        print(num02)
                        self.window['-OUTPUT-'](
                            f'{num01exten}% de {num02exten} ')
                    elif event == '-.-':
                        if '.' not in num02 and num02 != []:
                            num02.append('.')
                            num02exten = ''.join(num02)
                            self.window['-OUTPUT-'](
                                f'{num01exten}% de {num02exten} ')
                            resultado = num01exten
                        else:
                            pass
                    elif event == '-BACK-':
                        if num02exten == '':
                            self.window['-OUTPUT-'](f'{num01exten}')
                            resultado = num01exten
                            break
                        else:
                            self.window['-OUTPUT-'](f'{num01exten}% de')
                            resultado = num01exten
                            num02 = []
                            num02exten = ''
                    elif event == '-=-':
                        if num02exten == '':
                            pass
                        else:
                            resultado = operacao.Porcentagem(num01exten,
                                                             num02exten)
                            print(f'= {resultado}')
                            num01exten = str(resultado)
                            num01 = []
                            num02 = []
                            break
                    else:
                        pass
            elif event == '-BACK-':
                num01exten = ''
                resultado = ''
                num01 = []
                self.window['-OUTPUT-']('')
            elif event == '-CLEAR-':
                num01 = []
                num02 = []
                num01exten = ''
                num02exten = ''
                resultado = ''
                self.window['-OUTPUT-']('')
            elif event == '-1/x-':
                self.window['-OUTPUT-'](f'1/{num01exten} ')
                resultado = operacao.Inversor(num01exten)
                event, values = self.window.read()
                if event == '-BACK-':
                    self.window['-OUTPUT-'](f'{num01exten}')
                    resultado = num01exten
                    num01 = []
                elif event == '-=-':
                    print(f'= {resultado}')
                    num01exten = str(resultado)
                    num01 = []
            elif event == '-x²-':
                self.window['-OUTPUT-'](f'{num01exten}² ')
                resultado = operacao.Potencia2(num01exten)
                event, values = self.window.read()
                if event == '-BACK-':
                    self.window['-OUTPUT-'](f'{num01exten}')
                    resultado = num01exten
                    num01 = []
                elif event == '-=-':
                    print(f'= {resultado}')
                    num01exten = str(resultado)
                    num01 = []
            elif event == '-²√-':
                self.window['-OUTPUT-'](f'²√{num01exten} ')
                resultado = operacao.Raiz2(num01exten)
                if resultado == -1:
                    print('Erro: Raiz quadrada não aceita base negativa')
                    resultado = ''
                    break
                event, values = self.window.read()
                if event == '-BACK-':
                    self.window['-OUTPUT-'](f'{num01exten}')
                    resultado = num01exten
                    num01 = []
                elif event == '-=-':
                    print(f'= {resultado}')
                    num01 = []
            elif event == '-÷-':
                self.window['-OUTPUT-'](f'{num01exten}÷')
                while True:
                    event, values = self.window.read()
                    if event.isnumeric():
                        num02.append(event)
                        num02exten = ''.join(num02)
                        self.window['-OUTPUT-'](
                            f'{num01exten}÷{num02exten} ')
                    elif event == '-.-':
                        if '.' not in num02 and num02 != []:
                            num02.append('.')
                            num02exten = ''.join(num02)
                            self.window['-OUTPUT-'](
                                f'{num01exten}÷{num02exten} ')
                            resultado = num01exten
                        else:
                            pass
                    elif event == '-BACK-':
                        if num02exten == '':
                            self.window['-OUTPUT-'](f'{num01exten}')
                            resultado = num01exten
                            break
                        else:
                            self.window['-OUTPUT-'](f'{num01exten}÷')
                            resultado = num01exten
                            num02 = []
                            num02exten = ''
                    elif event == '-=-':
                        if num02exten == '':
                            pass
                        else:
                            resultado = operacao.Divisao(num01exten,
                                                         num02exten)
                            if num02exten == '0':
                                self.window['-OUTPUT-']('')
                                print('Erro: Divisão não admite' +
                                      ' divisor igual a 0')
                                resultado = ''
                                num02exten = ''
                            else:
                                print(f'= {resultado}')
                                num01exten = str(resultado)
                            num01 = []
                            num02 = []
                            break
                    else:
                        pass
            elif event == '-x-':
                self.window['-OUTPUT-'](f'{num01exten}x')
                while True:
                    event, values = self.window.read()
                    if event.isnumeric():
                        num02.append(event)
                        num02exten = ''.join(num02)
                        self.window['-OUTPUT-'](f'{num01exten}x{num02exten} ')
                    elif event == '-.-':
                        if '.' not in num02 and num02 != []:
                            num02.append('.')
                            num02exten = ''.join(num02)
                            self.window['-OUTPUT-'](
                                f'{num01exten}x{num02exten} ')
                            resultado = num01exten
                        else:
                            pass
                    elif event == '-BACK-':
                        if num02exten == '':
                            self.window['-OUTPUT-'](f'{num01exten}')
                            resultado = num01exten
                            break
                        else:
                            self.window['-OUTPUT-'](f'{num01exten}x')
                            resultado = num01exten
                            num02 = []
                            num02exten = ''
                    elif event == '-=-':
                        if num02exten == '':
                            pass
                        else:
                            resultado = operacao.Multiplicacao(num01exten,
                                                               num02exten)
                            print(f'= {resultado}')
                            num01exten = str(resultado)
                            num01 = []
                            num02 = []
                            break
                    else:
                        pass
            elif event == '---':
                self.window['-OUTPUT-'](f'{num01exten}-')
                while True:
                    event, values = self.window.read()
                    if event.isnumeric():
                        num02.append(event)
                        num02exten = ''.join(num02)
                        self.window['-OUTPUT-'](f'{num01exten}-{num02exten} ')
                    elif event == '-.-':
                        if '.' not in num02 and num02 != []:
                            num02.append('.')
                            num02exten = ''.join(num02)
                            self.window['-OUTPUT-'](
                                f'{num01exten}-{num02exten} ')
                            resultado = num01exten
                        else:
                            pass
                    elif event == '-BACK-':
                        if num02exten == '':
                            self.window['-OUTPUT-'](f'{num01exten}')
                            resultado = num01exten
                            break
                        else:
                            self.window['-OUTPUT-'](f'{num01exten}-')
                            resultado = num01exten
                            num02 = []
                            num02exten = ''
                    elif event == '-=-':
                        if num02exten == '':
                            pass
                        else:
                            resultado = operacao.Subtracao(num01exten,
                                                           num02exten)
                            print(f'= {resultado}')
                            num01exten = str(resultado)
                            num01 = []
                            num02 = []
                            break
                    else:
                        pass
            elif event == '-+-':
                self.window['-OUTPUT-'](f'{num01exten}+')
                while True:
                    event, values = self.window.read()
                    if event.isnumeric():
                        num02.append(event)
                        num02exten = ''.join(num02)
                        self.window['-OUTPUT-'](
                            f'{num01exten}+{num02exten} ')
                    elif event == '-.-':
                        if '.' not in num02 and num02 != []:
                            num02.append('.')
                            num02exten = ''.join(num02)
                            self.window['-OUTPUT-'](
                                f'{num01exten}+{num02exten} ')
                            resultado = num01exten
                        else:
                            pass
                    elif event == '-BACK-':
                        if num02exten == '':
                            self.window['-OUTPUT-'](f'{num01exten}')
                            resultado = num01exten
                            break
                        else:
                            self.window['-OUTPUT-'](f'{num01exten}+')
                            resultado = num01exten
                            num02 = []
                            num02exten = ''
                    elif event == '-=-':
                        if num02exten == '':
                            pass
                        else:
                            resultado = operacao.Soma(num01exten, num02exten)
                            print(f'= {resultado}')
                            num01exten = str(resultado)
                            num01 = []
                            num02 = []
                            break
                    else:
                        pass
            elif event == '-+/--':
                resultado = operacao.Trocar_Sinal(num01exten)
                self.window['-OUTPUT-']('')
                print(resultado)
                num01exten = str(resultado)
                num01 = []
            elif event == '-=-':
                self.window['-OUTPUT-']('')
                print(resultado)
            elif event == '-DEFAULT-':
                break
            else:
                break
        self.window.close()


class Operacoes:
    def Tipificacao_De_String(self, num):
        if '.' in num:
            num = float(num)
        else:
            num = int(num)
        return num

    def Porcentagem(self, num01, num02):
        num01 = self.Tipificacao_De_String(num01)
        num02 = self.Tipificacao_De_String(num02)
        resultado = (num01/100)*num02
        return resultado

    def Inversor(self, num01):
        num01 = self.Tipificacao_De_String(num01)
        resultado = 1/num01
        return resultado

    def Potencia2(self, num01):
        num01 = self.Tipificacao_De_String(num01)
        resultado = num01**2
        return resultado

    def Raiz2(self, num01):
        num01 = self.Tipificacao_De_String(num01)
        if num01 < 0:
            return -1
        else:
            resultado = num01**(1/2)
            return resultado

    def Divisao(self, num01, num02):
        num01 = self.Tipificacao_De_String(num01)
        num02 = self.Tipificacao_De_String(num02)
        if num02 != 0:
            resultado = num01/num02
            return resultado
        else:
            return -1

    def Multiplicacao(self, num01, num02):
        num01 = self.Tipificacao_De_String(num01)
        num02 = self.Tipificacao_De_String(num02)
        resultado = num01*num02
        return resultado

    def Subtracao(self, num01, num02):
        num01 = self.Tipificacao_De_String(num01)
        num02 = self.Tipificacao_De_String(num02)
        resultado = num01-num02
        return resultado

    def Soma(self, num01, num02):
        num01 = self.Tipificacao_De_String(num01)
        num02 = self.Tipificacao_De_String(num02)
        resultado = num01+num02
        return resultado

    def Trocar_Sinal(self, num01):
        num01 = self.Tipificacao_De_String(num01)
        resultado = num01*-1
        return resultado


Tela = Tela_Principal()  # Execucao
Tela.Executar_Tela()
