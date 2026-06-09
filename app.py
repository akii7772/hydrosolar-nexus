import streamlit as st
import plotly.graph_objects as go

# ==========================================
# CONFIGURAÇÃO
# ==========================================

st.set_page_config(
    page_title="HydroSolar Nexus",
    page_icon="🌊",
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🌊 HydroSolar Nexus")

    st.markdown("""
    ### Water-Energy Nexus

    Plataforma de negociação hídrica e geração de valor através da preservação da água.
    """)

    st.markdown("---")

    agua_preservada = st.slider(
        "Água Preservada (hm³)",
        1,
        100,
        20
    )

# ==========================================
# CÁLCULOS PRINCIPAIS
# ==========================================

valor_cao = 120

cao = agua_preservada * 1000

receita_cao = cao * valor_cao

energia_preservada = agua_preservada * 500

co2_ev = energia_preservada * 0.5

# ==========================================
# CABEÇALHO
# ==========================================

st.title("🌊 HydroSolar Nexus")

st.subheader(
    "Transformando água preservada em energia e valor econômico"
)

st.image(
    "imagens/1.jpeg",
    use_container_width=True
)

st.info("""
A HydroSolar Nexus combina energia solar flutuante,
agrivoltaica e um mercado de água temporário para reduzir
conflitos entre irrigação e geração hidrelétrica.

A água preservada gera Créditos de Água Otimizada (CAO),
criando valor econômico para irrigantes, hidrelétricas e investidores.
""")

# ==========================================
# ABAS
# ==========================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Indicadores",
    "💧 Mercado de Água",
    "🖼️ Soluções",
    "💰 Investidor",
    "📚 Engenharia"
])

# ==========================================
# ABA 1
# ==========================================

with tab1:

    st.header("Indicadores do Sistema")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💧 Água Preservada",
            f"{agua_preservada} hm³"
        )

    with col2:
        st.metric(
            "💎 CAO Gerado",
            f"{cao:,.0f}"
        )

    with col3:
        st.metric(
            "⚡ Energia Preservada",
            f"{energia_preservada:,.0f} MWh"
        )

    with col4:
        st.metric(
            "💰 Receita Potencial",
            f"R$ {receita_cao:,.0f}"
        )

    st.markdown("---")

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=[
                "Água",
                "CAO",
                "Energia"
            ],
            y=[
                agua_preservada,
                cao/100,
                energia_preservada/100
            ]
        )
    )

    fig.update_layout(
        title="Impacto da HydroSolar Nexus"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# ABA 2
# ==========================================

with tab2:

    st.header("💧 Mercado de Água")

    st.success(
        f"""
        O irrigante preserva {agua_preservada} hm³ de água.

        Em troca recebe aproximadamente
        R$ {receita_cao:,.0f} em CAOs.

        A hidrelétrica aumenta sua capacidade de geração,
        reduzindo o risco de acionamento de termelétricas.
        """
    )

    st.markdown("""
    ### Fluxo da Negociação

    Irrigante ➜ HydroSolar Exchange ➜ Hidrelétrica

    • O irrigante disponibiliza água.

    • A HydroSolar converte essa preservação em CAOs.

    • A hidrelétrica compra os créditos para garantir
      segurança energética.
    """)

# ==========================================
# ABA 3
# ==========================================

with tab3:

    st.header("🖼️ Soluções Implementadas")

    st.subheader("☀️ Solar Flutuante")

    col1, col2 = st.columns(2)

    with col1:
        st.image("imagens/1.jpeg")
        st.image("imagens/2.jpeg")

    with col2:
        st.image("imagens/3.jpeg")
        st.image("imagens/4.jpeg")

    st.markdown("---")

    st.subheader("🌱 Agrivoltaica")

    col3, col4 = st.columns(2)

    with col3:
        st.image("imagens/5.jpeg")
        st.image("imagens/6.jpeg")

    with col4:
        st.image("imagens/7.jpeg")
        st.image("imagens/8.jpeg")

# ==========================================
# ABA 4
# ==========================================

with tab4:

    st.header("💰 Simulador do Investidor")

    investimento = st.number_input(
        "Quanto deseja investir? (R$)",
        min_value=10000,
        value=500000,
        step=10000
    )

    custo_painel = 1500

    energia_por_painel = 650

    paineis = investimento / custo_painel

    energia_gerada = paineis * energia_por_painel

    agua_investidor = energia_gerada * 0.8

    cao_investidor = agua_investidor / 100

    receita_investidor = cao_investidor * valor_cao

    retorno = (receita_investidor / investimento) * 100

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "☀️ Painéis Adquiridos",
            f"{paineis:,.0f}"
        )

        st.metric(
            "⚡ Energia Gerada",
            f"{energia_gerada:,.0f} kWh"
        )

        st.metric(
            "💧 Água Preservada",
            f"{agua_investidor:,.0f} L"
        )

    with col2:

        st.metric(
            "💎 CAO Gerado",
            f"{cao_investidor:,.0f}"
        )

        st.metric(
            "💰 Receita Estimada",
            f"R$ {receita_investidor:,.0f}"
        )

        st.metric(
            "📊 Retorno",
            f"{retorno:.1f}%"
        )

    if retorno > 30:

        st.success(
            "🟢 Investimento altamente atrativo"
        )

    elif retorno > 15:

        st.warning(
            "🟡 Investimento moderadamente atrativo"
        )

    else:

        st.error(
            "🔴 Investimento de baixo retorno"
        )

    st.markdown("---")

    st.subheader("📈 HydroSolar Exchange")

    historico = [
        80,
        85,
        90,
        95,
        110,
        120,
        135,
        145,
        155,
        170,
        180,
        valor_cao
    ]

    meses = [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Hoje"
    ]

    fig_cao = go.Figure()

    fig_cao.add_trace(
        go.Scatter(
            x=meses,
            y=historico,
            mode="lines+markers"
        )
    )

    fig_cao.update_layout(
        title="Cotação do CAO",
        yaxis_title="R$"
    )

    st.plotly_chart(
        fig_cao,
        use_container_width=True
    )

# ==========================================
# ABA 5
# ==========================================

with tab5:

    st.header("📚 Fundamentação")

    with st.expander(
        "Como a Engenharia Elétrica e Ambiental resolvem juntas?"
    ):

        st.write("""
A Engenharia Elétrica calcula a geração de energia,
o valor econômico da água e os impactos no sistema elétrico.

A Engenharia Ambiental e Sanitária avalia a disponibilidade
hídrica, os impactos ambientais e a sustentabilidade do sistema.

A união dessas áreas cria o conceito Water-Energy Nexus.
""")

    with st.expander(
        "Como garantir sustentabilidade?"
    ):

        st.write("""
A solução reduz evaporação, respeita critérios ambientais,
preserva reservatórios e cria incentivos econômicos para o uso eficiente da água.
""")

    with st.expander(
        "Por que investidores devem aprovar?"
    ):

        st.write("""
O projeto gera receitas através dos CAOs,
energia renovável, redução de riscos energéticos e possui
alto potencial de expansão para outras bacias hidrográficas.
""")

