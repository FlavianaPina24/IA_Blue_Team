# 🧠 🛡️ Projeto: IA Blue Team + Ethical Hacker Agent

## 🎯 Objetivo
Criar um ecossistema autônomo de cibersegurança e testes defensivos focado em:
- 🔵 **Blue Team:** Detectar ameaças em tempo real.
- 🔴 **Red Team / Ethical Hacker:** Simular ataques de forma controlada.
- 🤖 **Inteligência Artificial:** Analisar logs, aprender comportamentos e agir automaticamente.

---

## 🏗️ 📊 Arquitetura do Sistema

### 🔹 1. Coleta de Dados (A Base)
Fonte de verdade para a IA trabalhar:
- Logs de sistema (Windows/Linux)
- Logs de rede e Firewalls
- Eventos de login
- **Ferramentas Integráveis:** Wazuh (SIEM Free), OSQuery, Sysmon.

### 🔹 2. Motor de Detecção (Heurística)
Identificação inicial de comportamento suspeito baseada em regras:
- Múltiplas tentativas de login → *Alerta (Brute Force)*
- IPs anômalos/estrangeiros → *Alerta*
- Mapeamento direto com o framework **MITRE ATT&CK**.

### 🔹 3. Camada Inteligente (IA)
Evolução do motor de regras para análises preditivas:
- **V1 (Atual):** Regras Heurísticas.
- **V2 (Planejado):** Scikit-learn (Machine Learning) para classificação Normal/Suspeito/Ataque.
- **V3 (Avançado):** LLM (GPT ou modelos locais) para análise contextual de ataques.

### 🔹 4. Resposta Automática (SOAR)
Ação autônoma do Blue Team (Security Orchestration):
- Bloqueio dinâmico de IP (Blacklisting).
- Isolamento de máquina ou encerramento de processo suspeito.

### 🔹 5. Ethical Hacker (Ataque Controlado)
Agente de simulação para treinar as defesas:
- Simulação de Brute Force.
- Scan de portas.
- Tentativas de exploração de vulnerabilidades.
- **Ferramentas:** Python Scripts, Nmap, Hydra, Metasploit.

### 🔁 6. Loop Inteligente (Adaptive System)
O diferencial do projeto: **Atacante simula → Defesa detecta → IA aprende → Resposta melhora.**

---

## 📚 🧠 Stack Tecnológica

* **Linguagens:** Python (Core), Bash (Automação de SO).
* **Ferramentas Blue Team:** Wazuh, ELK Stack, Docker (Ambientes Isolados).
* **Ferramentas Red Team:** Kali Linux, OWASP Top 10.
* **Inteligência Artificial:** Scikit-learn, Pandas, Modelos LLM.

---

## 🪜 📈 Roadmap do Projeto

- [x] **Fase 1: Fundamentos**
  - [x] Criação do repositório e arquitetura de pastas.
  - [x] Criação do script inicial `blue_team_agent.py` em Python.

- [x] **Fase 2: Blue Team (Estamos Aqui)**
  - [x] Motor de detecção heurística para Brute Force.
  - [x] Simulação de SOAR (Isolamento de IP).
  - [ ] Integração com leitura de logs reais.

- [x] **Fase 3: Ethical Hacker (Concluído com Sucesso 🔴)**
  - [x] Criação do agente de Pentest básico (Simulador de ataques).
  - [x] Execução de ataques contra o Agente Blue Team.

- [x] **Fase 4: IA e Machine Learning (Concluído com Sucesso 🚀)**
  - [x] Substituição das regras fixas por modelo em **Scikit-learn**.
  - [x] Treinamento da IA com *datasets* de tráfego de rede (Normal vs Malicioso).

- [ ] **Fase 5: Sistema Completo**
  - [ ] Integração total (Red Team vs Blue Team vs IA) em um ambiente Docker.

---

## 💻 🧪 Status Atual: Projeto Inicial

**Mini projeto implementado:** Detector de login suspeito com resposta autônoma.
O arquivo `blue_team_agent.py` simula o recebimento de logs de rede, analisa falhas sucessivas (Heurística) e aplica uma regra de firewall simulada (Blacklist) utilizando as táticas do **MITRE ATT&CK (T1110)**.

---

### ⚠️ Aviso Legal e Ético
Todo o código, scripts e simulações ofensivas (Red Team) contidos neste projeto são desenvolvidos estritamente para **fins educacionais e de pesquisa em cibersegurança**. 

**Regras de Uso:**
✅ Utilizar somente em ambientes de laboratório, máquinas virtuais locais ou redes explicitamente autorizadas.
❌ NUNCA utilizar estas técnicas ou scripts contra sistemas reais, públicos ou de terceiros sem o consentimento prévio e documentado.