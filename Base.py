import PySimpleGUI as sg
from pytubefix import YouTube
lista = []


# definições


def ytb():
    yt = YouTube(valores['link'])
    janela['text'].update(f" Título: {yt.title}")
    janela['text'].update(visible=True)
    janela['LISTBOX'].update(yt.streams)


def check():
    yt = YouTube(valores['link'])
    if valores['MP4'] and valores['checkbox'] is True:
        janela['LISTBOX'].update(yt.streams.filter(only_audio=True, file_extension='mp4'))
    elif valores['MP4'] and valores['checkbox2'] is True:
        janela['LISTBOX'].update(yt.streams.filter(only_video=True, file_extension='mp4'))
    elif valores['checkbox'] is True:
        janela['LISTBOX'].update(yt.streams.filter(only_audio=True))
    elif valores['checkbox2'] is True:
        janela['LISTBOX'].update(yt.streams.filter(only_video=True))
    elif valores['MP4'] is True:
        janela['LISTBOX'].update(yt.streams.filter(file_extension='mp4'))
    elif valores['Webm'] is True:
        janela['LISTBOX'].update(yt.streams.filter(file_extension='webm'))
    elif valores['DASH'] is True:
        janela['LISTBOX'].update(yt.streams.filter(adaptive=True))
    elif valores['pro'] is True:
        janela['LISTBOX'].update(yt.streams.filter(progressive=True))


def download(itag):
    yt = YouTube(valores['link'])
    stream = yt.streams.get_by_itag(itag)
    stream.download(output_path=r'/Users/lfbf/Downloads')


def check2():
    if acoes == 'botao':
        ytb()
    elif acoes == 'botao2':
        check()
    elif acoes == 'botao3':
        download(valores['itag'])
    elif valores['link'] == '':
        janela['botao'].update(disabled=True)
        janela['botao2'].update(disabled=True)
        janela['botao3'].update(disabled=True)
    elif valores['link'] != '':
        janela['botao'].update(disabled=False)
        janela['botao2'].update(disabled=False)
        janela['botao3'].update(disabled=False)


# geranado a interface
sg.theme("DarkAmber")

layout = [
    [sg.Text('Insira o link desejado:', size=(30, 1), font='Lucida', justification='left')],
    [sg.Input(key='link'), sg.Button('Pesquisar', font=('Lucida', 12), key='botao')],
    [sg.Text('', size=(60, 1), font='Lucida, 12', key='text', visible=False)],
    [sg.Listbox(lista, size=(90, 10), no_scrollbar=False, key='LISTBOX')],
    [sg.Text('Filtros:', font=('Lucida', 12))],
    [sg.Checkbox('Apenas audio', key='checkbox'), sg.Checkbox('Apenas vídeo', key='checkbox2'),
     sg.Checkbox('MP4', key='MP4'), sg.Checkbox('Webm', key='Webm'), sg.Checkbox('DASH', key='DASH'),
     sg.Checkbox('Progressive', key='pro'), sg.Button('Aplicar', font=('Lucida', 12), key='botao2')],
    [sg.Text('Insira a chave:', font=('Lucida', 12))],
    [sg.Input(key='itag', size=(14, 1)), sg.Button('Baixar', font=('Lucida', 12,), key='botao3')],
]

janela = sg.Window('FreeTube', layout, finalize=True)

while True:
    acoes, valores = janela.read(timeout=10)

    if acoes == sg.WINDOW_CLOSED:
        break
    else:
        check2()

janela.close()
