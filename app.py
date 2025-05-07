import streamlit as st
import pickle
import pandas as pd

# Carregar o modelo salvo
with open('modelo/modelo.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Previsão de Churn de Cliente")

# Inputs numéricos (valores diretos)
gender = st.selectbox("Gênero", [0, 1], format_func=lambda x: "Feminino" if x == 0 else "Masculino")
SeniorCitizen = st.selectbox("É idoso?", [0, 1], format_func=lambda x: "Não" if x == 0 else "Sim")
Partner = st.selectbox("Possui parceiro(a)?", [0, 1], format_func=lambda x: "Não" if x == 0 else "Sim")
Dependents = st.selectbox("Possui dependentes?", [0, 1], format_func=lambda x: "Não" if x == 0 else "Sim")
tenure = st.slider("Tempo de contrato (meses)", 0, 72)
PhoneService = st.selectbox("Possui serviço telefônico?", [0, 1], format_func=lambda x: "Não" if x == 0 else "Sim")
MultipleLines = st.selectbox("Possui múltiplas linhas?", [-1, 0, 1])
InternetService = st.selectbox("Tipo de serviço de internet", [0, 1, 2])
OnlineSecurity = st.selectbox("Possui segurança online?", [-1, 0, 1])
OnlineBackup = st.selectbox("Possui backup online?", [-1, 0, 1])
DeviceProtection = st.selectbox("Possui proteção de dispositivo?", [-1, 0, 1])
TechSupport = st.selectbox("Possui suporte técnico?", [-1, 0, 1])
StreamingTV = st.selectbox("Assiste TV por streaming?", [-1, 0, 1])
StreamingMovies = st.selectbox("Assiste filmes por streaming?", [-1, 0, 1])
Contract = st.selectbox("Tipo de contrato", [0, 1, 2])
PaperlessBilling = st.selectbox("Fatura sem papel?", [0, 1], format_func=lambda x: "Não" if x == 0 else "Sim")
PaymentMethod = st.selectbox("Método de pagamento", [0, 1, 2, 3])
MonthlyCharges = st.number_input("Valor mensal", min_value=0.0, max_value=300.0)
TotalCharges = st.number_input("Valor total pago", min_value=0.0, max_value=10000.0)

# Função para transformar inputs em DataFrame com valores numéricos
def preprocess_inputs():
    data = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }
    df = pd.DataFrame([data])
    return df

# Botão de previsão
if st.button("Prever"):
    df = preprocess_inputs()
    prediction = model.predict(df)[0]
    
    if prediction == 1:
        st.error("Cliente provavelmente vai cancelar (1 = Sim).")
    else:
        st.success("Cliente provavelmente NÃO vai cancelar (0 = Não).")