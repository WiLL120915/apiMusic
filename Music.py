import requests
from bs4 import BeautifulSoup
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit,QDialog, QVBoxLayout
      
from PyQt5.QtGui import QIcon




def limpaCampos():

    caixaArtista.clear()
    caixaMusica.clear()
    caixaArtista.setFocus()

def buscarCifra():
    artista = caixaArtista.text().lower().replace(" ", "-")
    musica = caixaMusica.text().lower().replace(" ", "-")
    url = f"https://www.cifraclub.com.br/{artista}/{musica}/"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            cifra = soup.find("pre")

            if cifra:
                QMessageBox.information(telaBusca, "Cifra/tab Encontrada", "Cifra/tab encontrada com sucesso!" )
                mostrarCifra(cifra.get_text())

            else:
                QMessageBox.warning(telaBusca, "Aviso", "Cifra/tab não encontrada na página.")
        else:
            QMessageBox.critical(telaBusca, "Erro", f"Erro na requisição. Código: {response.status_code}")
    except Exception as e:
        QMessageBox.critical(telaBusca, "Erro", f"Ocorreu uma exceção: {str(e)}")

        




def validaCampo():
    artista = caixaArtista.text().strip()
    musica = caixaMusica.text().strip()

    if artista == "":
            QMessageBox.critical(telaBusca, "Atenção", "Artista/Banda precisa ser informado, verifique.")
            caixaArtista.setFocus()

    elif musica == "":
            QMessageBox.critical(telaBusca, "Atenção", "Música não encontrada, verifique.")
            caixaMusica.setFocus()     

    else:
        buscarCifra()


    
app = QApplication(sys.argv)

telaBusca = QWidget()
telaBusca.setWindowTitle("Busca Cifra/Tab Musicas")
telaBusca.setGeometry(100, 100, 550, 350)
telaBusca.setWindowIcon(QIcon("guitar.png"))
telaBusca.setFixedSize(550, 350)

telaBusca.setStyleSheet("""
QWidget {
    /* Imagem de Fundo (Assumindo que a imagem está na pasta raiz do código) */
    background-image: url(guitar2.png);
    background-repeat: no-repeat;
    /* FIX: Posiciona a imagem 10px do topo e à direita para garantir que ela suba */
    background-position: right 10px;
    background-size: 250px; /* Ajusta o tamanho da imagem de fundo */
    background-color: rgba(0, 0, 0, 0.2); /* Fundo claro e semi-transparente (ajusta a cor base) */
    border: 3px solid #black; 
    border-radius: 5px; 
}
                        
QLabel {
        border: none; /* Sem borda */
        font-size: 15px; /* Tamanho da fonte */                
        color: white; /* Cor do texto do rótulo */
        
                        
}
QLineEdit {
    border: 1px solid #bdc3c7;
    border-radius: 5px;
    padding: 5px;
    background-color: white; /* Garante fundo branco para o campo */
    font-size: 15px; /* Tamanho do texto dentro da caixa */
}                        
QPushButton {
        background-color: #3498bd; /* Cor de fundo do botão */
        color: white; /* Cor do texto do botão */
        border: 1px solid black; /* Borda preta */
        border-radius: 5px; /* Bordas arredondadas */
        padding: 10px; /* Espaçamento interno */                
        font-size: 14px; /* Tamanho da fonte */
} 
                        /* --- ESTILO ESPECÍFICO: BOTÃO BUSCAR (VERDE) --- */
QPushButton#botaoBuscarCifra {
    background-color: #2ecc71; /* Verde esmeralda */
    border-color: #27ae60;
}
QPushButton#botaoBuscarCifra:hover {
    background-color: #27ae60; /* Verde mais escuro no hover */
}
QPushButton#botaoBuscarCifra:pressed {
    background-color: #1e8449; /* Verde escuro no pressionar */
} 

/* --- ESTILO ESPECÍFICO: BOTÃO LIMPAR (VERMELHO) --- */
QPushButton#botaoLimparCampos {
    background-color: #e74c3c; /* Vermelho forte */
    border-color: #c0392b;
}
QPushButton#botaoLimparCampos:hover {
    background-color: #c0392b; /* Vermelho mais escuro no hover */
}
QPushButton#botaoLimparCampos:pressed {
    background-color: #a93226; /* Vermelho escuro no pressionar */
} 
    
QPushButton:hover {
        background-color: #2980b9; /* Cor ao passar o mouse */
}
                        
QPushButton:pressed {
        background-color: #1f639e; /* Cor ao pressionar */
}                                                                 
""")

labelArtista = QLabel("Artista/Banda:", telaBusca)
labelArtista.move(20, 90)
labelArtista.setStyleSheet("QLabel { font-weight: bold; }")

caixaArtista = QLineEdit(telaBusca)
caixaArtista.move(150, 90)
caixaArtista.resize(250, 25)
caixaArtista.setMaxLength(100)
caixaArtista.setFocus()

labelMusica = QLabel("Música:", telaBusca)
labelMusica.move(20, 150)
labelMusica.setStyleSheet("QLabel { font-weight: bold; }")

caixaMusica = QLineEdit(telaBusca)
caixaMusica.move(150, 150)
caixaMusica.resize(250, 25)
caixaMusica.setMaxLength(100)


botaoBuscar = QPushButton("Buscar", telaBusca)
botaoBuscar.setObjectName("botaoBuscarCifra")
botaoBuscar.move(120, 250)
botaoBuscar.clicked.connect(validaCampo)


botaoLimpar = QPushButton("Limpar", telaBusca)
botaoLimpar.setObjectName("botaoLimparCampos")
botaoLimpar.move(350, 250)
botaoLimpar.clicked.connect(limpaCampos)


def mostrarCifra(texto):
    alerta = QDialog()
    alerta.setWindowTitle("Cifra/Tab Encontrada")
    alerta.setGeometry(200, 200, 500, 700)
    alerta.setWindowIcon(QIcon("guitar.png"))

    layout = QVBoxLayout()

    campoTexto = QTextEdit()
    campoTexto.setPlainText(texto)
    campoTexto.setReadOnly(True)
    

    layout.addWidget(campoTexto)
    alerta.setLayout(layout)
    alerta.exec_()





telaBusca.show()
sys.exit(app.exec_())



    






        
            


