# 🏦 Sistema Bancário em Python

Este projeto foi desenvolvido como parte de um **curso introdutório de Python**, com o objetivo de praticar **pensamento computacional**, **lógica de programação** e **estrutura de dados**, utilizando **listas e dicionários** para armazenar informações em memória.

O foco principal **não é persistência de dados nem Programação Orientada a Objetos (POO)**, mas sim a correta implementação das regras de negócio e a organização do código em funções.

---

## 🎯 Objetivos do Projeto

* Exercitar lógica de programação com Python
* Trabalhar com **listas e dicionários** para representar usuários e contas
* Implementar regras de negócio de um sistema bancário simples
* Separar responsabilidades em funções
* Simular operações bancárias básicas em memória

---

## 🧠 Funcionalidades Implementadas

* Criar usuário (cliente)
* Criar conta bancária vinculada a um usuário
* Login em conta existente
* Depósito
* Saque (com limite de valor e quantidade)
* Consulta de extrato
* Controle de sessão (conta ativa)

---

## 🗂️ Estrutura do Projeto

```
Sistema-Bancario-Dio/
│
├── functions/
│   ├── contas/
│   ├── login/
│   └── operacoes/
│
├── main.py
└── README.md
```

* `main.py`: ponto de entrada do sistema, responsável pela interação com o usuário
* `functions/`: funções responsáveis pelas regras de negócio

  * `contas`: criação e gerenciamento de contas
  * `login`: controle de sessão e autenticação
  * `operacoes`: depósito, saque e extrato

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Estruturas de dados nativas (listas e dicionários)

---

## ⚠️ Observações Importantes

* Os dados **não são persistidos** (não há uso de arquivos, JSON ou banco de dados)
* Todas as informações são armazenadas em memória durante a execução
* O projeto segue as **restrições propostas pelo curso**, priorizando lógica e estrutura de dados
* **Não há tratamento avançado de entradas do usuário**  
  (validações de input serão implementadas em uma refatoração futura)

---

## 🚀 Possíveis Melhorias Futuras

* Refatoração para **Programação Orientada a Objetos (POO)**
* Persistência de dados com arquivos JSON ou banco de dados
* Validação e sanitização de entradas do usuário
* Criação de testes automatizados
* Melhor separação entre regra de negócio e interface

---

## 👨‍💻 Autor

Desenvolvido por **Bruno Rafael**
Projeto educacional para estudo de Python e desenvolvimento backend.
