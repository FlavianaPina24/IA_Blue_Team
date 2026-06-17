import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    print("🧠 Iniciando o treinamento da IA Blue Team...")

    # 1. Carregar o Dataset
    df = pd.read_csv("login_attempts_dataset.csv")
    
    # 2. Preparação de Dados (O famoso One-Hot Encoding que conversamos!)
    # Isso vai transformar a coluna 'country' em 'country_Brazil', 'country_Russia', etc. (Colunas de 0 e 1)
    df = pd.get_dummies(df, columns=['country'])

    # Para essa IA, não queremos que ela decore IPs ou horários específicos, mas sim o COMPORTAMENTO.
    # Então vamos remover as colunas 'ip_address' e 'timestamp' do treinamento.
    X = df.drop(columns=['ip_address', 'timestamp', 'is_attack'])
    y = df['is_attack'] # A coluna 'is_attack' é o nosso gabarito

    # 3. Separar os dados: 80% para Treino (Estudar) e 20% para Teste (A prova final da IA)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Escolher o Algoritmo e Treinar (Random Forest é o "queridinho" para classificação e cibersegurança)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 5. Aplicar a "Prova" (Teste) para ver se ela aprendeu
    y_pred = model.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    print(f"🎯 Treinamento concluído! Acurácia da IA na detecção: {acuracia * 100:.2f}%")

    # 6. Salvar o "Cérebro" da IA para o nosso agente Blue Team usar depois
    joblib.dump(model, "ia_model.pkl")
    joblib.dump(list(X.columns), "ia_features.pkl") # Salva também o padrão das colunas que ela aprendeu
    print("💾 Inteligência salva com sucesso! (Arquivos .pkl gerados)")

if __name__ == "__main__":
    train_model()