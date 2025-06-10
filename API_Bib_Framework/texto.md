# Diferença entre API, Biblioteca e Framework

Esses três conceitos são muito utilizados no desenvolvimento de software, mas frequentemente são confundidos. Vamos entender melhor cada um deles:

---

## 📚 Biblioteca

Uma **biblioteca** é um conjunto de códigos reutilizáveis com funcionalidades genéricas que podem ser utilizadas em diferentes aplicações. 

Você **escolhe quando e como utilizá-la**, ou seja, você tem o controle do fluxo da aplicação.

### Características:
- Contém funções, métodos e classes prontas para serem usadas.
- Pode ser importada para ajudar em tarefas específicas, como gerar gráficos, manipular strings, validar dados etc.
- Não impõe uma estrutura de projeto.
- Utilizada sob demanda.

### Exemplo:
- `Math` (Java) — oferece funções matemáticas.
- `jQuery` ou `React` — ajudam na manipulação da interface com o usuário (UI).

---

## 🧩 API (Interface de Programação de Aplicações)

Uma **API** é um conjunto de rotinas, protocolos e ferramentas que permite a comunicação entre diferentes softwares. 

É como um **contrato**: você sabe o que pode usar (os métodos disponíveis), mas não precisa saber como aquilo é implementado por dentro.

### Características:
- Usada para **integrar aplicações** ou sistemas diferentes.
- Permite **enviar e receber dados**.
- Pode ser construída usando bibliotecas e frameworks.
- Muito utilizada para **consumir serviços externos** como cotações, clima, localização etc.

### Exemplo:
- API do **Google Maps**: Permite usar mapas dentro de um site ou app.
- API de cotação de moedas.
- API de busca de CEP.

---

## 🏗️ Framework

Um **framework** é uma estrutura de desenvolvimento que já traz um conjunto de ferramentas, bibliotecas e boas práticas para agilizar o desenvolvimento de software.

Diferente da biblioteca, **o framework controla o fluxo da aplicação** (inversão de controle).

### Características:
- Impõe uma **estrutura pré-definida**.
- Oferece componentes prontos: login, leitura de arquivos, conexão com banco, etc.
- Utiliza bibliotecas internas ou de terceiros.
- Pode incluir ou usar APIs.

### Exemplo:
- `AngularJS`, `Vue.js` (JavaScript)
- `.NET` (C#)
- `Bootstrap` (CSS)

---

## 🧠 Diferenças principais

| Conceito    | Controle de Fluxo | Uso Principal                         | Exemplo                  |
|-------------|-------------------|---------------------------------------|--------------------------|
| Biblioteca  | Você               | Resolver problemas específicos        | Math, jQuery, React      |
| API         | Você               | Integração entre aplicações           | API Google Maps, REST    |
| Framework   | Framework          | Estrutura para desenvolvimento completo | Angular, .NET, Bootstrap |

---

## 🔄 Como se relacionam?

- Um **framework** pode implementar **APIs** e usar **bibliotecas**.
- Uma **API** pode ser implementada por **bibliotecas** ou **frameworks**.
- Uma **biblioteca** pode conter sua própria **API** e ser usada em diferentes **frameworks**.

---

## 🧩 Analogias para facilitar

- **Biblioteca**: É como um conjunto de ferramentas. Você escolhe qual usar e quando.
- **API**: É como um cardápio de restaurante — você vê o que pode pedir, mas não vê a cozinha.
- **Framework**: É como montar um móvel com manual — você precisa seguir as instruções e encaixar as peças no lugar certo.

---

## 🔗 Referências

- StackOverflow: [Qual é a diferença de API, biblioteca e framework?](https://pt.stackoverflow.com/questions/17501/qual-%C3%A9-a-diferen%C3%A7a-de-api-biblioteca-e-framework)
- YouTube: [Vídeo explicativo](https://youtu.be/bhE9cpG66DI?si=SJgaUOP6M89WnAsP)
- Dev.to: [Diferença entre Biblioteca x API x Framework](https://dev.to/franolv/diferenca-entre-biblioteca-x-api-x-framework-8i9)
- Alura:
  - [O que é API](https://www.alura.com.br/artigos/api?srsltid=AfmBOoopkM1qS5NiXlFF8k7Lipc-xgZ3yysEoBVzcszyJZl0oRulnB5V)
  - [O que é Framework](https://cursos.alura.com.br/forum/topico-nao-entendi-o-que-e-um-framework-153708)
- Wikipedia:
  - [Framework](https://pt.wikipedia.org/wiki/Framework)
  - [Biblioteca (computação)](https://pt.wikipedia.org/wiki/Biblioteca_(computa%C3%A7%C3%A3o))
