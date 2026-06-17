import csv
import random
import time

def generate_realistic_logs(num_rows=1000):
    print("⏳ Gerando massa de dados para treinamento da IA...")
    
    normal_ips = ['10.0.0.5', '200.20.10.1', '192.168.1.50']
    hacker_ips = ['185.15.2.1', '45.178.23.9', '110.10.1.55']
    
    data = []
    base_time = int(time.time()) - (86400 * 7) # Começa 7 dias atrás

    # 1. Gerar Tráfego NORMAL (A maioria dos acessos)
    for _ in range(num_rows - 200):
        ip = random.choice(normal_ips)
        timestamp = base_time + random.randint(1, 86400 * 7)
        # 90% de chance de sucesso (humanos erram a senha às vezes, é normal)
        success = 1 if random.random() > 0.1 else 0 
        country = 'Brazil'
        data.append([ip, timestamp, success, country, 0]) # is_attack = 0

    # 2. Gerar Tráfego MALICIOSO (Ataques Brute Force)
    for _ in range(200):
        ip = random.choice(hacker_ips)
        timestamp = base_time + random.randint(1, 86400 * 7)
        success = 0 # Robôs de ataque geralmente falham muito
        country = random.choice(['Russia', 'China', 'North Korea'])
        data.append([ip, timestamp, success, country, 1]) # is_attack = 1

    # Ordenar cronologicamente para parecer um log real de servidor
    data.sort(key=lambda x: x[1])

    # Salvar no arquivo CSV, substituindo o antigo
    with open("login_attempts_dataset.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ip_address", "timestamp", "success", "country", "is_attack"])
        writer.writerows(data)

    print(f"✅ Sucesso! O arquivo 'login_attempts_dataset.csv' foi atualizado com {len(data)} registros.")

if __name__ == "__main__":
    generate_realistic_logs(1000)