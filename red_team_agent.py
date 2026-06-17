import time
from blue_team_agent import IABlueTeamAgent

class RedTeamAttacker:
    def __init__(self, target_agent):
        self.target = target_agent

    def launch_script_kiddie_attack(self):
        print("\n🔴 [RED TEAM] Tática 1: Brute Force Tradicional (Nível: Script Kiddie)")
        print("📝 Descrição: Disparar requisições de um IP estrangeiro sem se esconder.")
        ip = "185.15.2.1" # IP da Rússia
        country = "Russia"
        
        for i in range(2):
            print(f"   [⚔️] Atacante disparando payload (Falha de Login) via {ip}...")
            self.target.analyze_login(ip, False, country)
            time.sleep(1)

    def launch_apt_attack(self):
        print("\n🔴 [RED TEAM] Tática 2: Low & Slow com VPN (Nível: APT - Ameaça Avançada)")
        print("📝 Descrição: Usar IP do Brasil (Proxy) e simular falhas para burlar a IA.")
        
        ip = "200.20.10.99" # IP Falso do Brasil
        country = "Brazil"
        
        # Atacante vai tentar 5 vezes errar a senha com IP BR
        for i in range(5):
            print(f"   [🥷] Atacante camuflado tentando acesso (Falha) via {ip}...")
            self.target.analyze_login(ip, False, country)
            time.sleep(1)

if __name__ == "__main__":
    print("🔥 Iniciando Agente Ethical Hacker (Red Team) 🔥\n")
    
    print("🛡️ Levantando as defesas do Blue Team no servidor local...")
    blue_team = IABlueTeamAgent(use_ml=True)
    time.sleep(1)

    attacker = RedTeamAttacker(blue_team)
    attacker.launch_script_kiddie_attack()
    time.sleep(2)
    attacker.launch_apt_attack()