from pytube import YouTube

links = [
    # aqui vai os links
]
path = r'' # Aqui vai o caminho da pasta onde vão os videos 
for link in links:
    yt = YouTube(link)
    print(f'Título: {yt.title}')
    print(f'Tamanho do vídeo {yt.length / 60:.2f} Minutos')
    # try:
    #     ys = yt.streams.get_by_resolution("720p")
    #     print(f'Baixando')
    #     ys.download(path)
    #     print(f'Download Completo!')
    # except:
    #     ys = yt.streams.get_highest_resolution()
    #     print(f'Baixando')
    #     ys.download(path)
    #     print(f'Download Completo!')
    ys = yt.streams.get_highest_resolution()
    print(f'Baixando')
    ys.download(path)
    print(f'Download Completo!')

print('Todos os downloads completos!')
