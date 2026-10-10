<div align="center">

# 📋 Sistema de Cadastro de Clientes

*Projeto desenvolvido no 1º semestre do curso de Análise e Desenvolvimento de Sistemas*

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![Linguagem](https://img.shields.io/badge/Linguagem-Python%203.14+-yellow?style=for-the-badge)
![Database](https://img.shields.io/badge/Database-SQLite-blue?style=for-the-badge)

---

### 🛠️ Tecnologias e Ferramentas Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

</div>

---

## 🎯 Sobre o Projeto

Sistema de cadastro de clientes desenvolvido com o objetivo de praticar **lógica de programação**, **Python** e **banco de dados SQL**. O projeto mantém os dados persistidos em um banco SQLite local, com validação de e-mails duplicados e operações completas de CRUD.

---

## ✨ Funcionalidades

| Status | Funcionalidade |
| :---: | :--- |
| ✅ | Cadastrar novos clientes |
| ✅ | Listar todos os clientes cadastrados |
| ✅ | Buscar clientes por nome |
| ✅ | Atualizar dados de um cliente |
| ✅ | Excluir um cliente |
| ✅ | Validação de e-mail duplicado |

---

## 📂 Estrutura dos Arquivos

```
cadastro_clientes/
├── 📜 main.py                  # Código principal do sistema
├── 📄 README.md                # Arquivo de apresentação e documentação
└── 📂 database/
    └── 💾 cadastro.db          # Banco de dados (criado automaticamente)
```

---

## 🚀 Como Executar o Projeto

### ✅ Pré-requisito
- 🐍 Ter o **Python 3.14+** instalado na máquina

### Passo a passo

```bash
# 1. Clone ou baixe a pasta do projeto
git clone <url-do-repositorio>

# 2. Acesse a pasta
cd cadastro_clientes

# 3. Abra no VS Code (opcional)
code .

# 4. Execute o sistema
python main.py
```

> 💡 O banco de dados `cadastro.db` é criado automaticamente na primeira execução, dentro da pasta `database/`.

---

## 🗄️ Detalhes Técnicos

- **SQLite:** banco relacional leve, sem necessidade de instalar servidor — tudo fica em um único arquivo.
- **Validação:** o sistema verifica se o e-mail já existe antes de cadastrar, evitando duplicatas.
- **Persistência:** os dados permanecem salvos mesmo após fechar o programa.
- **CRUD completo:** Create, Read, Update e Delete implementados em Python puro.

---

<div align="center">

Feito com 💙 por **Leekhan**

</div>
