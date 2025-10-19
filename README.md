# Gera Marketing com IA

Este é um projeto que desenvolvi como parte de um minicurso prático sobre a aplicação de Inteligência Artificial no desenvolvimento de software. É uma aplicação web simples, construída com Flask e Python, que utiliza a API do Google Gemini para gerar textos de marketing criativos com base nas informações de um produto.

O objetivo foi passar por todo o ciclo de desenvolvimento: da ideia inicial, construção do front-end e back-end, integração com uma API externa, depuração de problemas do mundo real (como cache e parsing de dados), até a refatoração para seguir boas práticas de programação.



## 📋 Principais Funcionalidades

- **Interface web simples e intuitiva** para inserção de dados do produto (nome, características, público-alvo).
- **Integração com a API do Google Gemini** para geração de conteúdo dinâmico e inteligente.
- **Processador de Markdown customizado** no front-end que converte a resposta da IA (com cabeçalhos, negrito e itálico) para HTML formatado.
- **Front-end responsivo** com animações sutis para uma melhor experiência do usuário.
- **Código organizado** com separação de responsabilidades (HTML, CSS e Python em arquivos distintos).

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Flask
- **Inteligência Artificial:** Google Gemini API
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

---

## 🚀 Como Executar o Projeto Localmente

Para rodar este projeto no seu ambiente, siga os passos abaixo.

**1. Clone o repositório:**
```bash
git clone [https://github.com/Prof-JamesCampos/gera-marketing-ia.git](https://github.com/Prof-JamesCampos/gera-marketing-ia.git)
cd gera-marketing-ia
```

**2. Crie e ative um ambiente virtual:**
```bash
# Para Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Configure sua chave de API:**
   - Crie um arquivo chamado `.env` na raiz do projeto.
   - Dentro dele, adicione a seguinte linha, substituindo pela sua chave secreta do Google AI Studio:
     ```
     GOOGLE_API_KEY='SUA_CHAVE_SECRETA_AQUI'
     ```

**5. Execute a aplicação:**
```bash
python app.py
```

**6. Acesse no navegador:**
Abra seu navegador e vá para `http://127.0.0.1:5000`.

---

## ✍️ Autor

Feito com **James Campos**.

- **GitHub:** [Prof-JamesCampos](https://github.com/Prof-JamesCampos)