from flask import Flask, render_template
from perfil import Palestrante

app = Flask(__name__)

tannure = Palestrante("Márcio Tannure", 'Formado em Medicina no ano de 2004, pela Faculdade Gama Filho, no Rio de Janeiro, Márcio Tannure só conseguiu juntar os dois mundos quando seguiu para a residência na Universidade Federal do Estado do Rio de Janeiro (UNIRIO). Por conta do sonho de trabalhar com esporte, escolheu como especialidade a Ortopedia e Traumatologia, com pós em Medicina Ortomolecular. Antes mesmo de se formar na faculdade, foi bater na porta do Flamengo, em 2002, em busca de um estágio. Hoje, o Dr. Márcio Tannure é chefe do Departamento Médico do Flamengo e o médico oficial do UFC no Brasil. Além de Membro Titular da Sociedade Brasileira de Traumatologia e Ortopedia (SBOT) e da Sociedade Brasileira de Artroscopia e Trauma do Esporte (SBRATE).','Medicina Esportiva',"/static/img/speakers/marciotannure.jpg", 1)
gabrielbreier = Palestrante("Gabriel Breier",'Gabriel Breier, um TikToker de destaque, conquistou notoriedade por meio de seu perfil controverso. Com mais de 700k de seguidores, seus vídeos revelam seu estilo de vida, rotina de treinos e os resultados alcançados. Sua presença na plataforma digital atrai uma audiência ávida por suas orientações e dicas de aprimoramento pessoal.', 'Influencer', "/static/img/speakers/gabrielbreier.jpg", 2)
johann = Palestrante("Johann",'Personal Trainer e Coach, Johann é um profissional de destaque no mercado fitness. Com mais de 10 anos de experiência, Johann é especialista em treinamento de hipertrofia. Seu trabalho é reconhecido por sua abordagem personalizada e foco em resultados.', 'Personal Trainer', "/static/img/speakers/johann.jpg", 3)
renatogaucho = Palestrante("Renato Portaluppi",'Renato Gaúcho é um ex-jogador e treinador de futebol brasileiro. Atualmente, é técnico do Gremio. Como jogador, Renato Gaúcho foi um dos maiores ídolos da história do Grêmio, clube pelo qual conquistou a Libertadores e o Mundial de Clubes em 1983. Como treinador, Renato Gaúcho é conhecido por seu estilo ofensivo e por sua capacidade de motivar seus jogadores.', 'Técnico de Futebol', "/static/img/speakers/renatogaucho.jpg", 4)

PalestrantesList = [tannure, gabrielbreier, johann, renatogaucho]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detalhes')
def contato():
    return render_template('detalhes.html')

@app.route('/perfil')
def perfil():
    return render_template('palestrantesid.html', Palestrante=PalestrantesList)

@app.route('/perfil/<int:id>')
def perfil_palestrante(id:int):
    for palestrante in PalestrantesList:
        if palestrante.id == id:
            return render_template("palestrantesid.html", Palestrante=[palestrante]) 
    return "<h1>Ops! Palestrante não encontrado!</h1>"

if __name__ == '__main__':
    app.run()
