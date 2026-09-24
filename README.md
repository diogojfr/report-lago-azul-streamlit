# Easy Pallet – Lago Azul Dashboard (Streamlit)

Dashboard operacional no estilo do Looker/Easy Pallet, construído com **Streamlit + Plotly**.

## Estrutura do Projeto

```
report-lago-azul-streamlit/
│
├── app.py                      ← Ponto de entrada principal (run this)
│
├── requirements.txt
│
├── components/
│   ├── data_loader.py          ← Funções de leitura de CSV (cached)
│   └── ui_components.py        ← Componentes reutilizáveis (cards, gráficos, filtros)
│
├── pages/
│   ├── painel_geral.py         ← Painel Geral (KPIs + Donut + Bar + Line)
│   ├── painel_montagem.py      ← Painel Montagem (Bar + Tabelas)
│   ├── painel_conferencia.py   ← Painel Conferência (Tabelas por Conferente)
│   ├── painel_erros.py         ← Painel Erros (Donut + Bar Stacked + Tabela)
│   └── painel_operacoes.py     ← Painel Operações (duração, perfil, horas)
│
└── data/                       ← Coloque seus CSVs aqui
    ├── tab_orders.csv
    ├── tab_loads.csv
    ├── conf_registros.csv
    ├── tab_errors.csv
    ├── tab_erros_dia.csv
    ├── caixa_hora.csv
    ├── tempo_medio_mont.csv
    ├── media_conf_dia.csv
    ├── montagem_transporte.csv
    ├── tab_duracao_operacao.csv
    ├── tab_op_perfil.csv
    └── tab_horas_trabalhadas.csv
```

## Como Rodar

```bash
pip install -r requirements.txt
cp .env.example .env          # defina APP_PASSWORD
streamlit run app.py
```

## Autenticação

O app pede senha na entrada. A senha vem de `APP_PASSWORD`:

- **Local**: arquivo `.env` (veja `.env.example`)
- **Streamlit Cloud**: `st.secrets["APP_PASSWORD"]`

## Fontes de Dados

Cada loader em `components/data_loader.py` aponta para um CSV em `data/`.
As colunas de data são parseadas no próprio loader — ao trocar a origem dos
dados da Lago Azul, ajuste ali o nome do arquivo e as colunas de data.

## Adicionando um Novo Painel

1. Crie `pages/painel_novo.py` (código a nível de módulo, sem `render()`)
2. Adicione `st.Page("pages/painel_novo.py", title="...")` na lista `pages` em `app.py`
3. Opcionalmente adicione um loader em `components/data_loader.py`
