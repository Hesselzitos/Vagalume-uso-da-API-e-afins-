import requests
import json
import collections
from stop_words import get_stop_words


class requisicoes:
  def __init__(self):
    self.artista = input("Qual banda/artista?\n")
    self.artista=self.artista.split()
    self.artista='-'.join(self.artista)
    try:
      self.ranking = requests.get('https://api.vagalume.com.br/search.php?art='+self.artista+'&extra=rank')

      self.album = requests.get('https://www.vagalume.com.br/'+self.artista+'/discografia/index.js')

      self.topL = requests.get('https://www.vagalume.com.br/'+self.artista+'/index.js')
    except:
      print('Erro')
      exit()

  def posicao(self):
    dicionario = json.loads(self.ranking.text)
    print("\nO ranking do artista é: " + dicionario['art']['rank']['pos'])
    return(x.iniciarPrograma())

  def ultimoAlbum(self):
    dicionario = json.loads(self.album.text)
    Albuns=[]
    for i in range(len(dicionario['discography']['item'])):
      Albuns += [dicionario['discography']['item'][i]['desc']]    
    print("")
    print(Albuns[1])
    return(x.iniciarPrograma())

  def topLyrics(self):
    dicionario = json.loads(self.topL.text)
    n=int(input("\nRankig de quantas musicas mais acessadas?\n"))
    print("")
    for i in range(1,n+1):
      top= dicionario['artist']['toplyrics']['item'][i]['desc']
      print(' %d. %s'%(i,top))
    print("\nRanking construido com sucesso!")
    return(x.iniciarPrograma())

  def maisFrequentes(self):
    musica = input("\nDigite o nome da musica:")    
    print("")
    musica = musica.replace(' ','%20')
    try:
      letra = requests.get('https://api.vagalume.com.br/search.php?art='+self.artista+'&mus='+musica)
    except:
      print("\nNome da musica esta errado.")
      exit()

    dicionario = json.loads(letra.text)
    Letra = dicionario['mus'][0]['text'].lower()

    Letra = Letra.replace('.',' ')
    Letra = Letra.replace('!',' ')
    Letra = Letra.replace('?',' ')

    frase_lista = Letra.split()

    stop_words = get_stop_words('english')
    Letra_filtrada = []

    for w in frase_lista:
      if w not in stop_words:
        Letra_filtrada.append(w)

    c = collections.Counter(Letra_filtrada)
    print('\nAs palavras mais frequentes são:', c.most_common(10))
    return(x.iniciarPrograma())

  def iniciarPrograma(self):
    print("\nO que você deseja do seu artista preferido? \n  1-Saber quais são as musicas mais populares\n  2-Posição no ranking do vagalume \n  3-O ultimo album \n  4-A frequencia das palavras em uma musica específica \n  5-Sair")
    n = int(input())
    if n == 1:
      x.topLyrics()
    elif n==2:
      x.posicao()
    elif n==3:
      x.ultimoAlbum()
    elif n==4:
      x.maisFrequentes()
    else:
      exit()

x = requisicoes()
x.iniciarPrograma()
