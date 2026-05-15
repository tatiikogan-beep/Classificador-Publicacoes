# Classificador de Publicações Judiciais
**Imaculada Gordiano Advogados · Controladoria Jurídica**

Painel web para classificação automática de publicações judiciais em 16 workflows, usando IA (Claude API).

---

## Como publicar no Streamlit Cloud (5 minutos)

### 1. Criar repositório no GitHub
1. Acesse github.com e faça login
2. Clique em **New repository**
3. Nome: `Classificador-Publicacoes`
4. Marque **Public**
5. Clique em **Create repository**

### 2. Fazer upload dos arquivos
1. No repositório criado, clique em **Add file → Upload files**
2. Arraste os 3 arquivos:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. Clique em **Commit changes**

### 3. Publicar no Streamlit Cloud
1. Acesse **share.streamlit.io**
2. Faça login com sua conta GitHub
3. Clique em **New app**
4. Selecione o repositório `Classificador-Publicacoes`
5. Branch: `main`
6. Main file path: `app.py`
7. Clique em **Deploy**
8. Aguarde ~2 minutos → URL pública gerada automaticamente

---

## Funcionalidades
- Classificação em 16 workflows
- Detecção automática por número CNJ (J=5 Trabalho / J=8 Estadual / J=4 Federal)
- Resumo estruturado para o campo Descrição do LegalOne
- Alertas: prazo urgente 48h, dúvida de polo, cliente não identificado
- Confiança da IA com indicador visual
- Workflows alternativos sugeridos
- Campos para copiar Descrição e Tipo diretamente

## Clientes cadastrados
- CASA DE SAUDE E MATERNIDADE SAO RAIMUNDO SA
- SOCIEDADE BENEFICENTE SAO CAMILO
- COOP - COOPERATIVA DE CONSUMO
- UNIAO DE CLINICAS DO CEARA S/S LTDA
