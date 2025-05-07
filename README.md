# 💼 Projeto de Previsão de Churn de Clientes

Este projeto tem como objetivo prever o **churn** (cancelamento) de clientes com base em dados históricos. Utilizamos técnicas de análise exploratória de dados, engenharia de atributos, algoritmos de machine learning e deployment via API para entregar um sistema completo e funcional.

---

## 🧠 Objetivo

Ajudar empresas a identificar **clientes com alta probabilidade de cancelamento**, permitindo ações proativas de retenção e tomada de decisão com base em dados.

---

## 📂 Estrutura do Projeto
PREVISAO_DE_CHURN/
├── dados/
│ ├── dado.csv # Dados originais
│ └── dados_preparados.csv # Dados tratados para modelagem
│
├── modelo/
│ └── modelo.pkl # Modelo final salvo em formato pickle
│
├── notebooks/
│ ├── 01_eda.ipynb # Análise exploratória de dados
│ └── 02_modeling.ipynb # Treinamento e avaliação dos modelos
│
├── relatorio_churn.ipynb # Relatório final com insights do modelo
├── app.py # API com endpoint para previsão de churn
├── requirements.txt # Lista de bibliotecas necessárias
└── README.md # Documentação do projeto


---

## 🧪 Tecnologias e Bibliotecas

- **Python 3.9+**
- **Pandas**, **NumPy** – Manipulação de dados
- **Matplotlib**, **Seaborn** – Visualizações
- **Scikit-learn** – Machine Learning
- **Pickle** – Salvamento do modelo
- **Flask** – API para consumo do modelo
- **Jupyter Notebook** – Análise interativa

---

## 📈 Etapas do Projeto

### 1. Análise Exploratória de Dados (`01_eda.ipynb`)

- Leitura e entendimento da base de dados (`dado.csv`)
- Limpeza de dados: remoção de valores nulos, formatação de colunas
- Visualizações: gráficos de dispersão, boxplots, histograma e heatmap de correlação
- Identificação de padrões relevantes ao churn

### 2. Modelagem Preditiva (`02_modeling.ipynb`)

- Pré-processamento:
  - Label encoding de variáveis categóricas
  - Normalização/Padronização
- Divisão entre treino e teste
- Treinamento de algoritmos como:
  - Random Forest
- Avaliação com métricas:
  - Acurácia
  - Precisão
  - Recall
  - F1-Score
  - Matriz de confusão
  - AUC-ROC

### 3. Relatório Final (`relatorio_churn.ipynb`)

- Apresentação dos principais resultados e gráficos
- Interpretação dos fatores mais importantes que influenciam o churn
- Sugestões de negócio para retenção de clientes

✅ Resultados Esperados
Identificação dos principais fatores que levam ao cancelamento

Modelo com desempenho equilibrado entre precisão e recall

API simples e funcional para integrar com sistemas reais

📎 Arquivos Importantes
dados/dado.csv: Base original de clientes

modelo/modelo.pkl: Modelo treinado pronto para uso

app.py: API para fazer previsões

relatorio_churn.ipynb: Conclusões e recomendações

📬 Contato
Caso tenha sugestões, dúvidas ou deseje contribuir:

Email: michaelsantosa5@gmail.com

LinkedIn: (https://www.linkedin.com/in/michael-santos-ab27a2152/)

⚖️ Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.


