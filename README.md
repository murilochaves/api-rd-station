<p align="center">
	<a href="" rel="noopener">
	<img src="https://i.postimg.cc/YCKWfB1f/rdstation.png" alt="Project logo"></a>
</p>

<h3 align="center">
	🚀 Facilitando a Integração com a API do RD Station CRM
</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/murilochaves/api-rd-station)
  [![GitHub Issues](https://img.shields.io/github/issues/murilochaves/api-rd-station.svg)](https://github.com/murilochaves/api-rd-station/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">
  Uma biblioteca construída em Python para simplificar as chamadas à API do RD Station com foco no CRM.
  <br> 
</p>

## 📌 Sumário

- [Sobre](#sobre)
- [Objetivos](#objetivos)
- [Como usar](#como_usar)
- [Testes](#testes)
- [Bibliotecas](#bibliotecas)
- [Contribuição](#contribuicao)
- [Autores](#autores)
- [Agradecimentos](#agradecimentos)

## ℹ️ Sobre <a name = "sobre"></a>

O **RD Station CRM** é uma ferramenta poderosa para gerenciar leads, negociações e vendas, oferecendo uma **API RESTful** para integração com outros sistemas. No entanto, trabalhar diretamente com APIs pode ser um desafio, especialmente para quem precisa de agilidade no dia a dia.

**Para tornar a integração com o RD Station CRM mais simples e intuitiva, criei uma biblioteca Python que abstrai sua API.**  

Com ela, você pode interagir com os endpoints do RD Station CRM sem precisar lidar diretamente com requisições HTTP ou formatação de JSON. Isso facilita a integração e economiza tempo no desenvolvimento.

## 🎯 Objetivos <a name = "objetivos"></a>

✅ Facilitar chamadas para os principais recursos do RD Station CRM (Negociações, Contatos, Empresas, Produtos e mais)

✅ Eliminar a complexidade de requisições HTTP e manipulação manual de respostas JSON

✅ Ajudar desenvolvedores a economizar tempo na construção de integrações

## 📖 Como usar <a name = "como_usar"></a>

Estas instruções ajudarão você a configurar e rodar o projeto localmente.

### 📌 Requisitos

- Python 3.x instalado
- Conta no **RD Station CRM** ([acesse aqui](https://accounts.rdstation.com.br/))
- **Token de Instância** (obtenha nas configurações da conta)
  - Faça login e vá até **Configurações da Conta**
  - Copie seu **Token de Instância** (24 caracteres)

### 📥 Instalação

1️⃣ Instale a biblioteca via PyPI (_em breve_):  
```sh
  pip install api-rd-station
```

2️⃣ Configure um ambiente virtual (opcional, mas recomendado):  
```sh
  python -m venv .venv
  source .venv/bin/activate  # Linux/macOS
  .venv\Scripts\activate  # Windows
  pip install -r requirements.txt
```

3️⃣ Teste a conexão com a API:  
```sh
  python teste.py <SEU_TOKEN>
```

## 🧪 Testes <a name="testes"></a>

Para interagir com a API, você pode usar a biblioteca da seguinte maneira:

```python
  from RDStation.CRM import APIRDStationCRM

  token = "SEU_TOKEN"
  rd = APIRDStationCRM(token)

  # Exemplo: Informações do Token
  info = api.exibir_token()
  print(info)
```

## 📚 Bibliotecas <a name = "bibliotecas"></a>

- [Pandas](https://pandas.pydata.org/) - Biblioteca de análise de dados
- [Python](https://www.python.org/) - Linguagem principal
- [Requests](https://docs.python-requests.org/) - Biblioteca HTTP

## 🤝 Contribuição <a name = "contribuicao"></a>

**Sugestões, feedbacks e PRs no GitHub são mais do que bem-vindos. Vamos construir juntos!**

Essa biblioteca está disponível sob a licença MIT, ou seja, qualquer um pode usar, contribuir e melhorar.

Se encontrou um bug ou tem uma ideia de melhoria:

  1. Faça um **fork** do projeto
  2. Crie uma **branch** (`git checkout -b feat-nome_melhoria`)
  3. Faça o **commit** das alterações (`git commit -m "Descrição da Melhoria"`)
  4. Faça um **push** para a branch (`git push origin feat-nome_melhoria`)
  5. Abra um **Pull Request**

## ✍️ Autores <a name = "autores"></a>

- [@murilochaves](https://github.com/murilochaves/) - Desenvolvimento inicial

Veja a lista completa de [contribuidores](https://github.com/murilochaves/api-rd-station/contributors) para mais informações.

## 🙏 Agradecimentos <a name = "agradecimentos"></a>

  - A equipe do RD Station CRM pela API aberta
  - A comunidade Python pela colaboração contínua
