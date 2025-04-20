# LLM05: Improper Output Handling – Simulação de XSS via LLM

## 🎯 Objetivo

Neste desafio, o atacante deve induzir a LLM a gerar uma resposta maliciosa contendo código HTML/JavaScript. Essa resposta será exibida sem sanitização no navegador da vítima, permitindo a execução de um ataque de **Cross-Site Scripting (XSS)**. O objetivo é simular a extração de um cookie de sessão fictício atribuído ao usuário.

---

## 🧠 Contexto

A vulnerabilidade conhecida como **Improper Output Handling** ocorre quando o conteúdo gerado por um modelo de linguagem é exibido ou processado por um sistema sem validação ou sanitização. Isso permite que atacantes utilizem o LLM como vetor para injetar scripts maliciosos que afetem outros componentes da aplicação.

Neste cenário, a resposta da LLM é renderizada diretamente no DOM por meio de `innerHTML`, e o usuário tem um cookie de sessão simulado (`PUCRS-XSS-SESSION-ABC123`). O atacante pode tentar capturar esse valor via XSS.

---

## 🚀 Instructions

### 1. Build the container

`docker build -t llm-ctf-output-handling .`

### 2. Run the container (with log sharing enabled)

`docker run -p 5000:5000 -v $(pwd)/shared:/app/shared --name llm_ctf-05 llm-ctf-output-handling`

### 3. Access the challenge

`http://localhost:5000`
