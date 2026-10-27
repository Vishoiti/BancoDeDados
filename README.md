# 🐾 CRUD Petshop | Python + Oracle SQL

Projeto de aprendizado desenvolvido durante o curso na **FIAP**, com o objetivo de praticar os primeiros conceitos de **Python**, **SQL** e **banco de dados**, e servir de base para evoluir em direção à área de **dados**.

O sistema é um CRUD (Create, Read, Update, Delete) de pets, executado por um menu interativo no terminal e integrado a um banco de dados Oracle.

---

## 🎯 Objetivo

Este projeto faz parte da minha jornada de aprendizado. Ele reúne, em um só lugar, conceitos fundamentais que serão a base para projetos mais avançados com dados:

- Conexão do Python com um banco de dados relacional
- Primeiros passos em SQL (`INSERT`, `SELECT`, `UPDATE`, `DELETE`)
- Uso de bibliotecas externas
- Manipulação e exibição de dados com Pandas
- Tratamento de erros e estruturação de código

---

## ⚙️ Funcionalidades

| Opção | Funcionalidade | Descrição |
|-------|----------------|-----------|
| 1 | Cadastrar Pets | Insere um novo pet (tipo, nome e idade) no banco |
| 2 | Listar Pets | Exibe todos os registros em formato de tabela |
| 3 | Alterar Pets | Atualiza os dados de um pet a partir do ID |
| 4 | Excluir Pets | Remove um pet específico pelo ID |
| 5 | Apagar Todos | Exclui todos os registros e reinicia a contagem dos IDs |
| 0 | Sair | Encerra o programa |

---

## 🛠️ Tecnologias e bibliotecas

- **Python 3.10+** (utiliza `match/case`)
- **Oracle Database**
- **SQL**
- **[oracledb](https://pypi.org/project/oracledb/)**: conexão entre Python e Oracle
- **[Pandas](https://pandas.pydata.org/)**: organização e exibição dos dados em tabela

---

## 🗄️ Estrutura da tabela

```sql
CREATE TABLE petshop (
    id        INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tipo_pet  VARCHAR2(30),
    nome_pet  VARCHAR2(30),
    idade     INT
);
```

---

## 🚀 Como executar

**1. Clone o repositório**

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

**2. Instale as dependências**

```bash
pip install -r requirements.txt
```

**3. Configure suas credenciais**

No arquivo do projeto, substitua os valores de `usuario` e `senha` pelas suas credenciais do Oracle:

```python
usuario = "seu_usuario"
senha = "sua_senha"
```

> ⚠️ Nunca compartilhe ou publique suas credenciais reais.

**4. Execute o programa**

```bash
python main.py
```

---

## 📸 Demonstração

*(Adicione aqui um print do menu rodando no terminal)*

---

## 📚 O que aprendi

- Como conectar uma aplicação Python a um banco de dados Oracle
- Como executar comandos SQL a partir do código e manipular os resultados
- Como usar o Pandas para visualizar dados de forma organizada
- Como tratar exceções para deixar o programa mais robusto
- Como estruturar um sistema com menu interativo usando `match/case`

---

## 🔭 Próximos passos

Como este é um projeto de evolução, pretendo melhorá-lo e usá-lo como ponto de partida para estudos mais avançados:

- [ ] Usar *bind variables* nas consultas SQL (mais seguro e uma boa prática)
- [ ] Mover as credenciais para variáveis de ambiente (`.env`)
- [ ] Revisar o gerenciamento da conexão com o banco
- [ ] Criar consultas mais elaboradas (`JOIN`, `GROUP BY`, filtros)
- [ ] Realizar análises e visualizações dos dados com Pandas
- [ ] Evoluir para projetos de análise de dados


[LinkedIn](https://www.linkedin.com/in/seu-perfil) • [GitHub](https://github.com/seu-usuario)
