# 🎸 Projeto Buscador de Cifras e Tabs com PyQt5

Este projeto é um aplicativo de desktop simples desenvolvido em Python que permite ao usuário buscar cifras e tablaturas de músicas no site **Cifra Club** através de uma interface gráfica (GUI).

## 🎯 Objetivo

O objetivo principal é demonstrar a integração entre:
1.  **Interface Gráfica (GUI):** Criada com a biblioteca **PyQt5** para uma interação amigável.
2.  **Web Scraping:** Utilizando as bibliotecas **`requests`** e **`BeautifulSoup`** para realizar requisições HTTP e extrair o conteúdo da cifra da página web.

A busca é realizada filtrando a música através do nome do **Artista/Banda** e da **Música**.

## 💻 Tecnologias Utilizadas

* **Python 3.x**
* **`requests`**: Para fazer requisições HTTP.
* **`beautifulsoup4` (bs4)**: Para parsear o HTML e extrair o conteúdo da cifra.
* **`PyQt5`**: Para a construção da interface gráfica do usuário.

## ⚙️ Funcionalidades

* Busca de cifras e tablaturas de músicas.
* Validação de campos obrigatórios (Artista/Banda e Música).
* Tratamento de erros para códigos de status HTTP (ex: 404 - Não Encontrado) e exceções de conexão.
* Exibição da cifra em uma janela pop-up dedicada (`QDialog`).

## 🚀 Como Clonar e Executar o Projeto

Para rodar este projeto na sua máquina, siga os passos abaixo:

### 1. Pré-requisitos

Você deve ter o Python instalado e as seguintes bibliotecas Python:

```bash
pip install requests beautifulsoup4 pyqt5
