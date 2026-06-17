import time
from collections import defaultdict
import pandas as pd
import joblib
import os

class IABlueTeamAgent:
    def __init__(self, block_threshold=5, use_ml=True):
        self.failed_attempts = defaultdict(int)
        self.block_threshold = block_threshold
        self.blocked_ips = set()
        self.use_ml = use_ml

        # Tenta carregar a IA se existir e se estiver ativada
        if self.use_ml and os.path.exists("ia_model.pkl"):
            print("🧠 [SISTEMA] Carregando Cérebro da IA (Machine Learning)...")
            self.model = joblib.load("ia_model.pkl")
            self.features = joblib.load("ia_features.pkl")
        else:
            print("⚠️ [SISTEMA] Modelo de IA não encontrado ou desativado. Usando Heurística Clássica.")
            self.use_ml = False

    def analyze_login(self, ip, success, country="Brazil"):
        if ip in self.blocked_ips:
            print(f"⛔ [SOAR/FIREWALL] Conexão recusada. O IP {ip} já está na Blacklist!")
            return

        if self.use_ml:
            is_malicious = self._analyze_with_ml(ip, success, country)
            if not is_malicious:
                self._analyze_with_heuristics(ip, success) # Fallback de Segurança
        else:
            self._analyze_with_heuristics(ip, success)

    def _analyze_with_ml(self, ip, success, country):
        # Cria um mini-dataset (DataFrame) com o evento atual
        df_event = pd.DataFrame([{'success': int(success), 'country': country}])
        
        # Aplica o One-Hot Encoding (mesmo processo do treinamento)
        df_event = pd.get_dummies(df_event, columns=['country'])
        
        # Alinha as colunas para ficar exatamente igual ao que a IA aprendeu
        df_event = df_event.reindex(columns=self.features, fill_value=0)
        
        # A IA faz a previsão (0 = Normal, 1 = Ataque)
        prediction = self.model.predict(df_event)[0]
        
        if prediction == 1:
            print(f"🤖🚨 [IA DETECTOU ANOMALIA] Comportamento malicioso do IP: {ip} (País: {country})!")
            self.trigger_soar_response(ip)
            return True
        else:
            print(f"🔎 [IA] Tráfego validado. Repassando para a Heurística (Segurança em Profundidade)...")
            return False

    def _analyze_with_heuristics(self, ip, success):
        if not success:
            self.failed_attempts[ip] += 1
            print(f"⚠️ [MONITORAMENTO] Falha de login do IP: {ip} (Tentativas: {self.failed_attempts[ip]}/{self.block_threshold})")
            if self.failed_attempts[ip] >= self.block_threshold:
                self.trigger_soar_response(ip)
        else:
            print(f"✅ [MONITORAMENTO] Login bem-sucedido do IP: {ip}")
            self.failed_attempts[ip] = 0

    def trigger_soar_response(self, ip):
        print(f"\n🚨 [ALERTA CRÍTICO MITRE ATT&CK: T1110] Ataque de Brute Force detectado do IP: {ip}!")
        print(f"🛡️ [RESPOSTA ATIVA] Isolando ameaça... Adicionando {ip} à regra de bloqueio do Iptables/Firewall.\n")
        self.blocked_ips.add(ip)

# ==========================================
# SIMULAÇÃO DO AMBIENTE (Fase de Testes)
# ==========================================
if __name__ == "__main__":
    print("🤖 Iniciando Agente IA Blue Team (V2.0 - Machine Learning)...\n")
    agent = IABlueTeamAgent(use_ml=True)

    # Simulando um fluxo de logs de rede (agora a IA analisa o País e o Sucesso)
    logs = [
        ("10.0.0.5", True, "Brazil"),         # Humano acessando normalmente
        ("192.168.1.50", False, "Brazil"),    # Humano errou a senha 1 vez (não deve bloquear)
        ("10.0.0.5", True, "Brazil"),         # Humano acessando novamente
        ("45.178.23.9", False, "Russia"),     # Hacker tentando acesso (IA deve detectar imediatamente!)
        ("45.178.23.9", False, "Russia"),     # Aqui ele já vai tomar o bloqueio direto do Firewall
    ]

    for ip, success, country in logs:
        agent.analyze_login(ip, success, country)
        time.sleep(1) 
        
    print("\n📊 Relatório do Agente:")
    print(f"IPs na Blacklist: {list(agent.blocked_ips)}")