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


valor_cao = 120

def br(valor):
    return f"{valor:,.0f}".replace(",", ".")

# ==========================================
# CÁLCULOS PRINCIPAIS
# ==========================================

investimento_padrao = 500000

investimento = investimento_padrao

custo_painel = 1500
energia_por_painel = 650

paineis = investimento_padrao / custo_painel

energia_preservada = paineis * energia_por_painel

agua_preservada = energia_preservada * 0.8

cao = energia_preservada / 80

receita_cao = cao * valor_cao

# ==========================================
# CABEÇALHO
# ==========================================

st.title("🌊 HydroSolar Nexus")

st.subheader(
    "Transformando água preservada em energia e valor econômico"
)


st.info("""
A HydroSolar Nexus combina energia solar flutuante,
agrivoltaica e um mercado de água temporário para reduzir
conflitos entre irrigação e geração hidrelétrica.

A água preservada gera Créditos de Água Otimizada (CAO),
criando valor econômico para irrigantes, hidrelétricas e investidores.
""")

st.markdown("---")

st.header("🚀 Como Funciona")

st.markdown("""
### Transformando água preservada em valor econômico

A HydroSolar Nexus conecta geração de energia renovável,
preservação hídrica e valorização econômica através dos
Créditos de Água Otimizada (CAO).
""")

st.subheader("🔄 Fluxo de Geração de Valor")

st.image(
    "imagens/fluxograma.png",
    use_container_width=True
)

st.markdown("---")

st.header("📊 Indicadores Principais")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💧 Água Preservada",
        f"{br(agua_preservada)} hm³"
    )

with col2:
    st.metric(
        "⚡ Energia Gerada",
        f"{br(energia_preservada)} MWh"
    )

with col3:
    st.metric(
        "💎 CAO Gerado",
        f"{br(cao)}"
    )

with col4:
    st.metric(
        "💰 Receita Potencial",
        f"R$ {br(receita_cao)}"
    )

# ==========================================
# ABAS
# ==========================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏢 Quem Somos",
    "🖼️ Soluções",
    "💧 Mercado de Água",
    "📈 Retorno Financeiro",
    "💎 CAO",
    "📚 Engenharia"
])


# ==========================================
# ABA 2
# ==========================================

with tab3:

    st.header("💧 Mercado de Água")

    agua_formatada = f"{agua_preservada:,.0f}".replace(",", ".")
    receita_formatada = f"{receita_cao:,.0f}".replace(",", ".")

    st.success(
        f"""
        O irrigante preserva aproximadamente {agua_formatada} hm³ de água.

        Em troca recebe aproximadamente
        R$ {receita_formatada} em CAOs.

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

with tab2:

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
    "💰 Quanto deseja investir? (R$)",
    min_value=10000,
    value=500000,
    step=10000
    )

    custo_painel = 1500
    energia_por_painel = 650

    paineis = investimento / custo_painel

    energia_preservada = paineis * energia_por_painel

    agua_preservada = energia_preservada * 0.8

    cao = energia_preservada / 80

    receita_cao = cao * valor_cao

    energia_gerada = energia_preservada

    agua_investidor = agua_preservada

    cao_investidor = cao

    receita_investidor = receita_cao

    retorno = (receita_investidor / investimento) * 100

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
        "☀️ Painéis Adquiridos",
        f"{br(paineis)}"
        )

        st.metric(
        "⚡ Energia Gerada",
        f"{br(energia_gerada)} MWh"
        )

        st.metric(
            "💧 Água Preservada",
            f"{br(agua_investidor)} hm³"
        )

    with col2:

        st.metric(
            "💎 CAO Gerado",
            f"{br(cao_investidor)}"
        )

        st.metric(
            "💰 Receita Estimada",
            f"R$ {br(receita_investidor)}"
        )

        st.metric(
            "📊 Retorno",
            f"{retorno:.1f}%".replace(".", ",")
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


# ==========================================
# ABA 5 - CAO
# ==========================================

with tab5:

    st.header("💎 Créditos de Água Otimizada (CAO)")


    custo_painel = 1500
    energia_por_painel = 650

    paineis = investimento / custo_painel
    energia_preservada = paineis * energia_por_painel
    agua_preservada = energia_preservada * 0.8
    cao = energia_preservada / 80
    receita_cao = cao * valor_cao

    st.info("""
    O Crédito de Água Otimizada (CAO) é um ativo ambiental criado
    para valorizar a preservação da água através da geração de energia renovável.

    A instalação de sistemas fotovoltaicos reduz a evaporação dos reservatórios,
    contribuindo para a manutenção do volume hídrico disponível.
    """)

    st.subheader("⚙️ Como funciona a geração de CAOs?")

    st.write("""
    A HydroSolar Nexus monitora continuamente a energia produzida pelos
    sistemas fotovoltaicos instalados.

    Para cada 80 MWh de energia produzidos, é gerado 1 Crédito de Água
    Otimizada (CAO).

    Ao final de cada mês, toda a energia gerada é contabilizada e convertida
    automaticamente em créditos negociáveis.
    """)

    cao_mensal = energia_preservada / 80

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "⚡ Energia Produzida",
            f"{br(energia_preservada)} MWh"
        )

    with col2:
        st.metric(
            "💎 CAOs Gerados",
            f"{br(cao_mensal)}"
        )

    st.markdown("---")

    st.metric(
        "💰 Valor Atual do CAO",
        f"R$ {br(valor_cao)}",
        "+5%"
    )

    st.subheader("📈 Cotação do CAO")

    historico_cao = [
        80,
        90,
        100,
        110,
        120,
        130,
        145,
        valor_cao,
    ]

    meses_cao = [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Hoje"
    ]

    fig_cao_hist = go.Figure()

    fig_cao_hist.add_trace(
        go.Scatter(
            x=meses_cao,
            y=historico_cao,
            mode="lines+markers",
            name="CAO"
        )
    )

    fig_cao_hist.update_layout(
        title="Evolução do Valor do CAO",
        yaxis_title="R$"
    )

    st.plotly_chart(
        fig_cao_hist,
        use_container_width=True
    )

    st.write("""
    A cotação do CAO varia de acordo com a demanda das hidrelétricas,
    disponibilidade hídrica e benefícios ambientais gerados.
    """)

# ==========================================
# ABA 6 - QUEM SOMOS
# ==========================================

with tab1:

    st.header("🏢 Quem Somos")

    col1, col2 = st.columns(2)

    with col1:
        st.image("imagens/1.jpeg", use_container_width=True)
        st.image("imagens/3.jpeg", use_container_width=True)

    with col2:
        st.image("imagens/5.jpeg", use_container_width=True)
        st.image("imagens/7.jpeg", use_container_width=True)

    st.write("""
    A HydroSolar Nexus é uma startup focada em soluções inovadoras
    para o setor Water-Energy Nexus, integrando geração de energia,
    preservação hídrica e valorização econômica dos recursos naturais.
    """)

    st.subheader("☀️ Nossa atuação")

    st.write("""
    Nossa startup trabalha com a instalação de painéis fotovoltaicos
    sobre a superfície de reservatórios e em propriedades rurais.

    Essas soluções aumentam a geração de energia renovável e contribuem
    diretamente para a redução da evaporação da água.
    """)

    st.subheader("💧 Preservação dos reservatórios")

    st.write("""
    A instalação de painéis fotovoltaicos sobre reservatórios cria uma
    barreira física que reduz a incidência direta da radiação solar.

    Como resultado, ocorre diminuição da taxa de evaporação da água,
    contribuindo para a preservação do volume dos reservatórios.
    """)

    st.subheader("💎 Plataforma HydroSolar Exchange")

    st.write("""
    Nossa plataforma quantifica a energia produzida pelos sistemas
    fotovoltaicos e converte os benefícios gerados em Créditos de Água
    Otimizada (CAO).

    Os proprietários que cedem parte de suas áreas para instalação dos
    sistemas podem converter a energia produzida em CAOs e gerar uma
    nova fonte de receita sustentável.
    """)

    st.success("""
    Nossa missão é transformar água preservada em valor econômico,
    conectando produtores rurais, hidrelétricas e investidores por meio
    de um mercado inovador de créditos ambientais.
    """)


with tab6:

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

