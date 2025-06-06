# Security in LLMs: Validation of Risks in Simulated Environments

This repository contains the artifacts, source code, and simulated environments developed as part of the final thesis of Érico Panazzolo, a Computer Science student at PUCRS. The project aims to validate the main security risks associated with Large Language Models (LLMs), based on the OWASP document titled "2025 Top 10 Risks & Mitigations for LLMs and Gen AI Apps".

## Objective

Investigate, analyze, and mitigate the risks associated with the use of Large Language Models (LLMs), highlighting how such risks impact the confidentiality, integrity, and availability of systems, while also proposing both technical and strategic defense measures tailored for corporate environments. The work focuses on simulating the ten main risks identified by OWASP and validating the effectiveness of the proposed mitigation strategies.

## Top 10 Risks

Each risk was tested in an isolated environment and validated through manual/automated testing. The risks addressed include:

- `LLM01: Prompt Injection`
- `LLM02: Sensitive Information Disclosure`
- `LLM03: Supply Chain`
- `LLM04: Data and Model Poisoning`
- `LLM05: Improper Output Handling`
- `LLM06: Excessive Agency`
- `LLM07: System Prompt Leakage`
- `LLM08: Vector and Embedding Weaknesses`
- `LLM09: Misinformation`
- `LLM10: Unbounded Consumption`

## Project Structure

Each Git branch corresponds to a different security risk. Inside each branch, you will find a dedicated environment and instructions on how to run and test the specific risk scenario.

## How to test the project

1. **Clone the project**

```bash
git clone https://github.com/EricoPanazzolo/Security-in-LLMs-Validation-of-Risks-in-Simulated-Environments.git
```

2. **Navigate to the project directory**

```bash
cd Security-in-LLMs-Validation-of-Risks-in-Simulated-Environments
```

3. **Select a specific branch corresponding to the risk you want to test**

```bash
git checkout <branch-name>
```

4. **Read the instructions in `challenge.md`**

5. For all branches, you need to set your Hugging Face API token, which can be obtained from [Hugging Face](https://huggingface.co/).

## Results

Test results are automatically recorded in `.csv` files and logs within the `/app/shared` directory, containing:

- Executed prompt

- Model responses

- Whether the attack was successful or not

## Author

**Érico Panazzolo**

Graduating in Computer Science at PUCRS, with a focus on Information Security.
Currently works with Penetration Testing and Technical Project Manager for Cybersecurity projects.

Contact: ericopanazzolo@gmail.com

Linkedin: [linkedin.com/in/erico-panazzolo](https://www.linkedin.com/in/érico-panazzolo-a98406221/)

Medium: [medium.com/@ericopanazzolo](https://medium.com/@ericopanazzolo)

## Legal Disclaimer

This project was developed exclusively for academic and research purposes. None of the experiments are intended to compromise real-world systems. The techniques documented here must be used only in controlled environments, strictly for educational purposes, or in scenarios where their use has been explicitly agreed upon by all involved parties.
