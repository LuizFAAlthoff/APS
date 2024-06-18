import PySimpleGUI as sg
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

class AtorJogadorInterface(DogPlayerInterface):
    def __init__(self):
        self.dog_server_interface = DogActor()
        self.layout_nome = [
            [sg.Text("Digite seu nome:")],
            [sg.InputText(key='NOME')],
            [sg.Button('OK')]
        ]

        self.window_nome = sg.Window('Informe seu nome', self.layout_nome)

        event, values = self.window_nome.read()
        if event == sg.WINDOW_CLOSED or event == 'OK':
            self.nome_do_usuario = values['NOME']
            message = self.dog_server_interface.initialize(self.nome_do_usuario, self)
            sg.popup('Mensagem do servidor:', message)  
        self.window_nome.close()

        self.layout = [
            [sg.Menu([['File', ['Iniciar Jogo', 'Restaurar Estado Inicial']]])],  
            [sg.Image(filename='imagens/player_1.png', key='PLAYER1', pad=(16, None)), 
             sg.Image(filename='imagens/player_2.png', key='PLAYER2', pad=(16, None)), 
             sg.Image(filename='imagens/player_3.png', key='PLAYER3', pad=(16, None)), 
             sg.Image(filename='imagens/player_4.png', key='PLAYER4', pad=(16, None))]
        ]

        self.layout += [
            [sg.Image(filename='imagens/contador.png', key='CONTADOR'), 
             sg.Image(filename='imagens/carta_atual_mesa.png', key='CURRENT_CARD', size=(350, 300), background_color='orange'),
             sg.Button('Comprar carta', size=(12, 2), button_color=('brown'), key='COMPRAR'),
             sg.Button('Finalizar jogada', size=(15, 2), button_color=('green'), key='FINALIZAR')]
        ]

        self.layout += [
            [sg.Image(filename='imagens/azul_roxo_1.png', key='CARD1', enable_events=True, pad=(14, None)), 
             sg.Image(filename='imagens/laranja_azul_3.png', key='CARD2', enable_events=True, pad=(14, None)), 
             sg.Image(filename='imagens/block.png', key='CARD3', enable_events=True, pad=(14, None)),
             sg.Image(filename='imagens/anil_amarelo_1.png', key='CARD4', enable_events=True, pad=(14, None)),
             sg.Image(filename='imagens/vermelho_laranja_3.png', key='CARD5', enable_events=True, pad=(14, None))]
        ]

        self.window = sg.Window('Rainbow Cards', self.layout, size=(800, 750), background_color='orange')

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'EXIT':
                break
            elif event == 'COMPRAR':
                sg.popup_quick_message('Você comprou uma carta!', auto_close_duration=2, location=(self.window.CurrentLocation()[0] + self.window.Size[0]/2, self.window.CurrentLocation()[1] + self.window.Size[1]/2))
            elif event == 'FINALIZAR':
                sg.popup_quick_message('Jogada finalizada!', auto_close_duration=2, location=(self.window.CurrentLocation()[0] + self.window.Size[0]/2, self.window.CurrentLocation()[1] + self.window.Size[1]/2))
            elif event in ('CARD1', 'CARD3'):
                sg.popup_quick_message('Carta válida para jogada!', auto_close_duration=2, location=(self.window.CurrentLocation()[0] + self.window.Size[0]/2, self.window.CurrentLocation()[1] + self.window.Size[1]/2))
            elif event == 'Iniciar Jogo':
                self.start_match()  
            elif event == 'Restaurar Estado Inicial':
                self.dog_server_interface.restore_initial_state()
                sg.popup('Estado inicial restaurado com sucesso!')
                
        self.window.close()

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        sg.popup(message)

    def receive_start(self, start_status):
        message = start_status.get_message()
        sg.popup(message)

if __name__ == "__main__":
    app = AtorJogadorInterface()
    app.run()