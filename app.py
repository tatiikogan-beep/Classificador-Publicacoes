import streamlit as st
import json
import requests

# ─── CONFIG ───────────────────────────────────────────────────────────────────
API_KEY = st.secrets["ANTHROPIC_API_KEY"]
MODEL   = "claude-sonnet-4-20250514"
MAX_TOK = 1200

CLIENTES = [
    "CASA DE SAUDE E MATERNIDADE SAO RAIMUNDO SA",
    "SOCIEDADE BENEFICENTE SAO CAMILO",
    "COOP - COOPERATIVA DE CONSUMO",
    "UNIAO DE CLINICAS DO CEARA S/S LTDA",
]

SYSTEM_PROMPT = """Você é um especialista em direito do trabalho que classifica publicações judiciais em workflows de controladoria jurídica.

Os workflows possíveis são:
1. Sinalizar
2. Interlocutória trabalhista
3. Interlocutória CPC
4. Providencias em Execução Trabalhista
5. Sentença trabalhista
6. Sinalizar audiência
7. Sinalizar pauta de julgamento
8. Acórdão TRT
9. Contrarrazões Trabalhista
10. Sentença CPC
11. Decisão TST
12. Acordão TJ TRF
13. Decisão Presidencia TRT
14. Sinalizar Perícia
15. Decisão STJ/STF
16. Decisão TJ TRF sobre REsp e RE

========== REGRA DO RESUMO (OBRIGATÓRIA) ==========
O campo "resumo" deve ter NO MÁXIMO 3 frases curtas.
Escreva APENAS o que aconteceu na publicação — nada mais.
NUNCA inclua: fundamentação jurídica, jurisprudência, impugnações, análise da decisão, sugestões, recursos cabíveis, orientações de qualquer tipo, ou conclusões sobre o que o cliente deve ou não fazer (ex: "não há prazo para o cliente", "não há providências necessárias", "não há prazo", "cliente não precisa agir"). O resumo descreve APENAS o que aconteceu — nunca avalia consequências.

MODELO OBRIGATÓRIO para acórdãos e sentenças — siga EXATAMENTE este padrão:
"[Dispositivo] ao [tipo de recurso] interposto pelo/pela [nome da parte que recorreu]."

EXEMPLOS CORRETOS:
- "Denegado seguimento ao Recurso de Revista interposto pelo HOSPITAL SAO CARLOS LTDA."
- "Desprovido o Recurso Ordinário interposto pela reclamante MARIA DA SILVA."
- "Provido o Agravo de Instrumento interposto pela reclamada COOP - COOPERATIVA DE CONSUMO."
- "Julgados procedentes os Embargos à Execução opostos pela SOCIEDADE BENEFICENTE SAO CAMILO."

REGRAS para acórdãos e sentenças:
- Comece sempre pelo dispositivo (Denegado / Provido / Desprovido / Procedente / Improcedente / Extinto)
- Identifique o tipo de recurso e pelo nome quem o interpôs, extraído do texto
- NUNCA descreva análise, pressupostos, fundamentação ou "foi intimado para tomar ciência"
- Se o dispositivo não estiver claro no texto, escreva: "[Dispositivo não localizado no texto]"

MODELO OBRIGATÓRIO para homologação de cálculos:
"Houve homologação de cálculos. Crédito bruto fixado em R$ [valor numérico exato] em [data-base]. A [reclamada/reclamante] deve efetuar o pagamento em [prazo exato]."
— o prazo só deve ser incluído se estiver EXPLICITAMENTE escrito na publicação. Se não houver prazo mencionado, encerrar em: "Houve homologação de cálculos. Crédito bruto fixado em R$ [valor] em [data-base]."

MODELO para outros tipos de publicação:
"[O que aconteceu em 1 frase]. [Quem deve fazer o quê, se houver]."

REGRA GLOBAL SOBRE PRAZOS NO RESUMO:
- Se a publicação mencionar explicitamente um prazo em dias para qualquer ato, esse prazo DEVE constar no resumo.
- Se o prazo não estiver escrito na publicação, NUNCA presuma, calcule ou indique prazo — simplesmente não mencione.
- EXCEÇÃO: quando a publicação mencionar o art. 880 da CLT como fundamento para pagamento, o prazo é de 48 horas — indique "pagamento em 48 horas (art. 880 da CLT)" no resumo.

MODELO para audiências:
- Presencial: "AUDIÊNCIA [TIPO] PRESENCIAL (AUD. DD/MM/AAAA ÀS HH:MM)."
- Virtual: "AUDIÊNCIA [TIPO] VIRTUAL (AUD. DD/MM/AAAA ÀS HH:MM). [link] ID da reunião: [ID] Senha: [senha]."

MODELO para pauta de julgamento:
"PAUTA DE JULGAMENTO VIRTUAL/PRESENCIAL (AUD. DD/MM/AAAA)."

MODELO para perícia:
"PERÍCIA [TIPO] PRESENCIAL/VIRTUAL (AUD. DD/MM/AAAA ÀS HH:MM). [local se presencial]. Perito: [nome do perito se constar]."

Se não souber resumir em 3 frases, escolha apenas os 3 fatos mais importantes.
====================================================

IDENTIFICAÇÃO DO NÚMERO CNJ (Res. 65/2008):
O número único segue o formato NNNNNNN-DD.AAAA.J.TR.OOOO. O dígito J identifica a natureza:
- J=5: Justiça do Trabalho (TRTs/TST) — ramo federal especializado em conflitos trabalhistas, regido pela CLT. Use SEMPRE workflows trabalhistas.
- J=4: Justiça Federal Comum (TRFs) — causas com União, autarquias. Use workflows CPC/Federal.
- J=8: Justiça Estadual (TJs). Use workflows CPC/Estadual.
- J=1: STF | J=3: STJ
⚠️ TRT é Justiça do Trabalho (J=5), NÃO é Justiça Federal Comum (J=4). São ramos distintos com regras processuais diferentes.

Regras de classificação:

- IDENTIFICAÇÃO DO POLO: Sempre identifique quem foi intimado na publicação e verifique se coincide com o polo do nosso cliente. Se houver dúvida sobre quem deve agir, sinalize "duvida_polo" como true.

- PRAZO URGENTE 48H: Sempre que a publicação mencionar prazo de 48 horas, 48h, 2 dias, 2 (dois) dias, "48 horas antes" ou "2 dias antes" para qualquer ato — defina "prazo_urgente" como true. Isso inclui expressões como "48 horas antes da audiência", mesmo que o ato futuro seja distante.

- REGRA GERAL SOBRE RECURSOS: Sempre que a publicação comunicar uma SENTENÇA ou ACÓRDÃO, há prazo de recurso a cumprir. EXCEÇÃO IMPORTANTE: sentença de EXTINÇÃO DO PROCESSO ("julgo extinta a execução", "arquivamento definitivo") NÃO gera prazo recursal — use "Sinalizar".

- "Sinalizar": use quando NÃO existe nenhuma medida ou prazo para o NOSSO CLIENTE.

- "Interlocutória trabalhista": decisões intermediárias onde o CLIENTE deve agir, em processos da JUSTIÇA DO TRABALHO (J=5).

- "Interlocutória CPC": decisões intermediárias onde o CLIENTE deve agir, em processos da JUSTIÇA ESTADUAL (J=8) ou JUSTIÇA FEDERAL COMUM (J=4).

- "Providencias em Execução Trabalhista": homologação de cálculos, penhora, bloqueio Sisbajud, intimação para pagar, execução na Justiça do Trabalho. Também quando o juiz deliberou sobre impugnação já protocolada ou julgou Embargos à Execução opostos pelo NOSSO CLIENTE.

- "Sentença trabalhista": sentenças de mérito na Justiça do Trabalho. EXCEÇÃO: extinção com arquivamento → "Sinalizar".

- "Sinalizar audiência": publicação informa data e hora de audiência agendada.

- "Sinalizar pauta de julgamento": processo incluído em pauta de tribunal.

- "Acórdão TRT": inteiro teor de acórdão do TRT.

- "Contrarrazões Trabalhista": cliente intimado para apresentar contrarrazões.

- "Sentença CPC": sentenças de mérito em processos CPC/Estadual/Federal.

- "Decisão TST": decisões do Tribunal Superior do Trabalho.

- "Acordão TJ TRF": acórdãos de TJ ou TRF.

- "Decisão Presidencia TRT": decisões da presidência/vice-presidência do TRT sobre admissibilidade.

- "Sinalizar Perícia": SOMENTE quando a publicação informa DATA AGENDADA para realização da perícia. Incluir nome do perito se constar. Quando houver perícia agendada E prazo ao perito concomitantemente, prevalece "Sinalizar Perícia".

- "Decisão STJ/STF": decisões do STJ ou STF.

- "Decisão TJ TRF sobre REsp e RE": juízo de admissibilidade de REsp ou RE no TJ/TRF.

IMPORTANTE: O nome do nosso cliente será informado. Use-o para:
1. Identificar se a publicação gera obrigação/prazo para ELE ou para outra parte.
2. Verificar se o nome aparece no texto (seja flexível com variações). Só defina "cliente_nao_identificado" como true se não houver NENHUMA correspondência razoável.

Responda APENAS em JSON válido, sem markdown, sem explicação fora do JSON:
{
  "workflow": "nome exato do workflow",
  "confianca": número de 0 a 100,
  "justificativa": "frase curta explicando o motivo principal",
  "resumo": "resumo conforme REGRA DO RESUMO acima",
  "cliente_nao_identificado": true ou false,
  "alerta": "mensagem explicando o impedimento, ou null se não houver",
  "duvida_polo": true ou false,
  "duvida_polo_info": "explicação se houver dúvida, ou null",
  "prazo_recurso": true ou false,
  "prazo_recurso_info": "descrição se true, ou null",
  "prazo_urgente": true ou false,
  "prazo_urgente_info": "descrição se true, ou null",
  "alternativas": [
    {"workflow": "segundo mais provável", "confianca": número},
    {"workflow": "terceiro mais provável", "confianca": número}
  ]
}"""

# ─── FUNÇÕES ──────────────────────────────────────────────────────────────────
def classificar(texto: str, cliente: str, processo: str) -> dict:
    prompt = f"Nome do nosso cliente: {cliente}\n"
    if processo:
        prompt += f"Número do processo: {processo}\n"
    prompt += f"\nTexto da publicação:\n{texto[:8000]}"

    resp = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": MODEL,
            "max_tokens": MAX_TOK,
            "system": SYSTEM_PROMPT,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    resp.raise_for_status()
    raw = resp.json()["content"][0]["text"].strip()
    raw = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(raw)


def badge_confianca(v):
    if v >= 85:
        return f"🟢 {v}%"
    elif v >= 65:
        return f"🟡 {v}%"
    else:
        return f"🔴 {v}%"


# ─── UI ───────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Classificador de Publicações Judiciais",
    page_icon="⚖️",
    layout="centered",
)

st.title("⚖️ Classificador de Publicações Judiciais")
st.caption("Imaculada Gordiano Advogados · Análise automática por IA · 16 workflows · 2.032 publicações treinadas")

st.divider()

# ── Formulário ────────────────────────────────────────────────────────────────
processo = ""
cliente = st.text_input("Nome do cliente", placeholder="Digite o nome do cliente...")

texto = st.text_area(
    "Texto da publicação",
    height=280,
    placeholder="Cole aqui o texto completo da publicação judicial...",
)

classificar_btn = st.button("⚡ Classificar e sugerir workflow", type="primary", use_container_width=True)

# ── Resultado ─────────────────────────────────────────────────────────────────
if classificar_btn:
    if not texto.strip():
        st.warning("Cole o texto da publicação antes de classificar.")
    elif not cliente:
        st.warning("Selecione o nome do cliente antes de classificar.")
    else:
        with st.spinner("Analisando publicação..."):
            try:
                r = classificar(texto, cliente, processo)
            except Exception as e:
                st.error(f"Erro ao conectar com a IA: {e}")
                st.stop()

        st.divider()

        # ── Alertas ──────────────────────────────────────────────────────────
        if r.get("prazo_urgente"):
            st.error(f"🚨 **PRAZO URGENTE — 48 HORAS**\n\n{r.get('prazo_urgente_info', '')}")

        if r.get("cliente_nao_identificado"):
            st.warning(f"⚠️ **Impedimento na análise** — cliente não identificado no texto.\n\nVerifique se o processo pertence a {cliente}.")

        if r.get("duvida_polo"):
            st.warning(f"⚠️ **Dúvida sobre o polo intimado**\n\n{r.get('duvida_polo_info', '')}")

        if r.get("alerta") and r["alerta"] not in [None, "null", ""]:
            st.warning(f"⚠️ {r['alerta']}")

        # ── Workflow sugerido ─────────────────────────────────────────────────
        st.subheader("Workflow sugerido")
        wf_col, conf_col = st.columns([3, 1])
        with wf_col:
            st.markdown(f"### `workflow/{r['workflow']}`")
        with conf_col:
            st.metric("Confiança", badge_confianca(r["confianca"]))

        st.caption(f"**Justificativa:** {r.get('justificativa', '')}")

        # ── Descrição (Resumo) ────────────────────────────────────────────────
        st.subheader("Descrição (campo LegalOne)")
        st.info(r.get("resumo", ""))

        # ── Copiar ────────────────────────────────────────────────────────────
        st.text_area(
            "📋 Copie o resumo abaixo",
            value=r.get("resumo", ""),
            height=100,
            key="resumo_copy",
        )
        st.text_input(
            "📋 Copie o tipo abaixo",
            value=f"workflow/{r['workflow']}",
            key="tipo_copy",
        )

        # ── Prazo recursal ────────────────────────────────────────────────────
        if r.get("prazo_recurso") and r.get("prazo_recurso_info"):
            with st.expander("📅 Informação sobre prazo recursal"):
                st.write(r["prazo_recurso_info"])

        # ── Alternativas ─────────────────────────────────────────────────────
        if r.get("alternativas"):
            with st.expander("🔄 Workflows alternativos"):
                for alt in r["alternativas"]:
                    st.write(f"- `workflow/{alt['workflow']}` — {badge_confianca(alt['confianca'])}")

st.divider()
st.caption("Imaculada Gordiano Advogados · Controladoria Jurídica · v2.0")
