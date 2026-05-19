import base64

with open('/home/claude/igsa_b64.txt') as f:
    LOGO = 'data:image/jpeg;base64,' + f.read().strip()

# Build the HTML in Python parts to avoid any escaping issues
CSS = """
:root{
  --c9:#6B0010;--c8:#8B0E1A;--c7:#A81020;--c6:#C01020;--c5:#D42030;
  --c4:#E05060;--c3:#E89090;--c2:#F5C8CC;--c1:#FDE8EA;--c0:#FFF5F6;
  --gd:#C4A85A;--gd2:#E8D8A0;
  --bg:#F7F4F4;--wh:#FFF;--tx:#1A0810;--mu:#7A5060;--bd:#EDD8DA;
  --sh:0 2px 8px rgba(100,0,20,.1);--shm:0 4px 20px rgba(100,0,20,.15);
  --r:8px;--r2:14px;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--tx);font-size:14px}
h1,h2,.sf{font-family:'Libre Baskerville',serif}
/* CONFIG */
#cfg{min-height:100vh;background:linear-gradient(150deg,var(--c9),var(--c7) 60%,var(--c6));display:flex;flex-direction:column;align-items:center;justify-content:center;padding:32px 20px}
.cfgh{text-align:center;margin-bottom:24px}
.cfgh img{height:84px;margin:0 auto 12px;display:block;filter:drop-shadow(0 4px 12px rgba(0,0,0,.4))}
.cfgh h1{color:#fff;font-size:1.7rem}
.cfgh p{color:var(--c2);font-size:.82rem;margin-top:5px}
.card{background:#fff;border-radius:var(--r2);box-shadow:0 8px 40px rgba(0,0,0,.28);padding:32px;width:100%;max-width:840px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.stl{font-family:'Libre Baskerville',serif;font-size:.88rem;font-weight:700;color:var(--c7);padding-bottom:7px;border-bottom:2px solid var(--c1);margin-bottom:12px;display:flex;align-items:center;gap:7px}
.sn{width:20px;height:20px;background:var(--c7);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.65rem;font-weight:700;flex-shrink:0}
.dz{border:2px dashed var(--c3);border-radius:var(--r);padding:14px 10px;text-align:center;cursor:pointer;background:var(--c0);transition:.2s;position:relative;overflow:hidden}
.dz:hover{border-color:var(--c6);background:var(--c1)}
.dz.ok{border-style:solid;border-color:var(--c7);background:var(--c1)}
.dz input[type=file]{position:absolute;inset:0;opacity:0;cursor:pointer;width:100%;height:100%}
.dzi{font-size:1.5rem;margin-bottom:4px}
.dzl{font-size:.75rem;color:var(--c7);font-weight:600}
.dzs{font-size:.68rem;color:var(--mu);margin-top:2px}
.dzst{font-size:.68rem;color:var(--c8);font-weight:700;margin-top:4px;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
.up3{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:16px}
.fld{margin-bottom:12px}
.fld label{display:block;font-size:.72rem;font-weight:600;color:var(--mu);margin-bottom:4px;text-transform:uppercase;letter-spacing:.04em}
.fld input{width:100%;padding:9px 12px;border:1.5px solid var(--bd);border-radius:var(--r);font-family:'Inter',sans-serif;font-size:.86rem;color:var(--tx);background:#fff;transition:border-color .2s;outline:none}
.fld input:focus{border-color:var(--c6)}
.fld small{display:block;font-size:.67rem;color:var(--mu);margin-top:3px}
.bgen{width:100%;padding:13px;background:var(--c7);color:#fff;border:none;border-radius:var(--r);font-family:'Inter',sans-serif;font-size:.92rem;font-weight:700;cursor:pointer;letter-spacing:.04em;transition:.2s;margin-top:4px}
.bgen:hover{background:var(--c9)}
.err{color:#900;font-size:.75rem;padding:8px 12px;background:#fff0f0;border-radius:6px;margin-top:8px;border-left:3px solid #c00;display:none}
/* TOOLBAR */
#dsh,#rpt{display:none}
.tbar{background:var(--c9);padding:9px 22px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:200;gap:10px}
.thi{font-size:.82rem;color:var(--c3);font-weight:500;letter-spacing:.01em}
.tbtns{display:flex;gap:7px}
.tb{padding:6px 13px;border-radius:6px;font-size:.72rem;font-weight:700;cursor:pointer;border:none;transition:.2s;letter-spacing:.03em}
.tbk{background:rgba(255,255,255,.15);color:#fff}.tbk:hover{background:rgba(255,255,255,.28)}
.trl{background:var(--gd);color:var(--c9)}.trl:hover{background:var(--gd2)}
.tpd{background:var(--c3);color:var(--c9)}.tpd:hover{background:#fff}
/* DASH */
.dw{padding:0 26px 36px;max-width:1360px;margin:0 auto}
.dh{display:flex;align-items:center;justify-content:space-between;padding:22px 0 16px;border-bottom:2px solid var(--c1);margin-bottom:20px;gap:14px}
.dhl img{height:62px}
.dht{text-align:center;flex:1;padding:0 14px}
.dmt{font-size:1.6rem;font-weight:700;color:var(--c9)}
.dsb{font-size:.7rem;color:var(--mu);margin-top:4px;text-transform:uppercase;letter-spacing:.05em}
.clo img{max-height:56px;max-width:120px;object-fit:contain}
.clph{width:110px;height:46px;border:1.5px solid var(--bd);border-radius:var(--r);display:flex;align-items:center;justify-content:center;font-size:.65rem;color:var(--mu);text-align:center}
.warn{background:#FFF8E0;border:1.5px solid #C4A020;border-radius:var(--r);padding:10px 14px;margin-bottom:14px}
.warn h4{color:#7A6000;font-size:.76rem;font-weight:700;margin-bottom:5px}
.warn li{font-size:.7rem;color:#7A6000;padding:2px 0 2px 16px;position:relative;list-style:none}
.warn li::before{content:'⚠';position:absolute;left:0}
.sbn{background:var(--c8);color:#fff;padding:9px 16px;border-radius:var(--r);margin-bottom:14px;display:flex;align-items:center;gap:8px}
.sbn h2{font-family:'Libre Baskerville',serif;font-size:1.05rem;font-weight:700;letter-spacing:.03em}
.kr{display:grid;grid-template-columns:repeat(auto-fit,minmax(128px,1fr));gap:12px;margin-bottom:12px}
.kp{background:var(--wh);border-radius:var(--r);padding:14px 14px 10px;box-shadow:var(--sh);border-top:3px solid var(--c6)}
.kl{font-size:.62rem;color:var(--mu);text-transform:uppercase;letter-spacing:.06em;font-weight:600}
.kv{font-family:'Libre Baskerville',serif;font-size:2rem;color:var(--c8);font-weight:700;line-height:1;margin-top:2px}
.kd{font-size:.64rem;color:var(--mu);margin-top:2px}
.cg{display:grid;gap:12px;margin-bottom:12px}
.c3{grid-template-columns:1fr 1fr 1fr}
.c2{grid-template-columns:1fr 1fr}
.c1{grid-template-columns:1fr}
.cc{background:var(--wh);border-radius:var(--r);padding:16px;box-shadow:var(--sh)}
.ct{font-size:.67rem;color:var(--mu);text-transform:uppercase;letter-spacing:.06em;font-weight:600;margin-bottom:12px;padding-bottom:7px;border-bottom:1px solid var(--c0)}
.ch{position:relative}
.sd{height:2px;background:var(--c1);margin:20px 0}
/* REPORT */
.rw{max-width:1100px;margin:0 auto;padding:28px 36px;background:#fff;min-height:100vh}
.rh{display:flex;align-items:center;justify-content:space-between;padding-bottom:14px;border-bottom:3px solid var(--c7);margin-bottom:20px}
.rh img{height:64px}
.rtb h1{font-family:'Libre Baskerville',serif;font-size:1.3rem;color:var(--c9);text-align:right}
.rtb p{font-size:.72rem;color:var(--mu);text-align:right;margin-top:3px}
.rnote{background:#FFF8E0;border-left:3px solid var(--gd);padding:8px 14px;border-radius:4px;margin-bottom:16px;font-size:.71rem;color:#6A5000}
.rbtns{display:flex;gap:10px;margin-bottom:18px}
.rb{padding:9px 18px;border-radius:var(--r);font-size:.78rem;font-weight:700;cursor:pointer;border:none;transition:.2s}
.rxl{background:var(--gd);color:var(--c9)}.rxl:hover{background:var(--gd2)}
.rpf{background:var(--c7);color:#fff}.rpf:hover{background:var(--c9)}
.rks{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:20px}
.rk{background:var(--c0);border-radius:var(--r);padding:12px;border-top:3px solid var(--c6);text-align:center}
.rk .l{font-size:.6rem;color:var(--mu);text-transform:uppercase;letter-spacing:.04em;font-weight:600}
.rk .v{font-family:'Libre Baskerville',serif;font-size:1.65rem;color:var(--c8);font-weight:700}
.rs{font-family:'Libre Baskerville',serif;font-size:.92rem;color:var(--c8);margin:18px 0 8px;padding-bottom:5px;border-bottom:2px solid var(--c2)}
.pt{width:100%;border-collapse:collapse;font-size:.71rem}
.pt th{background:var(--c8);color:#fff;padding:7px 8px;text-align:left;font-weight:600;font-size:.65rem;text-transform:uppercase;letter-spacing:.04em;white-space:nowrap}
.pt td{padding:6px 8px;border-bottom:1px solid var(--bd);vertical-align:top}
.pt tr:nth-child(even) td{background:var(--c0)}
@media print{
  #cfg,.tbar,.rbtns{display:none!important}
  body[data-print=dash] #rpt{display:none!important}
  body[data-print=dash] #dsh{display:block!important}
  body[data-print=report] #dsh{display:none!important}
  body[data-print=report] #rpt{display:block!important}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .cc,.kp,.rk{break-inside:avoid}
  .rw{padding:14px}
  .dw{padding:10px;max-width:none}
}
@media(max-width:860px){
  .grid2,.up3,.c3,.c2{grid-template-columns:1fr}
  .kr{grid-template-columns:repeat(2,1fr)}
}
"""

# JavaScript - written carefully without embedded HTML in template literals
JS = r"""
const ST={proc:null,serv:null,aud:null,dec:null,logo:null};
const CH={};


const TAX = {
// AUDIÊNCIA
'Audiência':'Audiência','Audiência - Cível':'Audiência','Audiência / Audiência Cível':'Audiência',
'Audiência / Conciliação':'Audiência','Audiência / Inaugural':'Audiência',
'Audiência / Instrução':'Audiência','Audiência / Instrução e Julgamento':'Audiência',
'Audiência / Julgamento':'Audiência','Audiência / Justificação Prévia':'Audiência',
'Audiência / Una':'Audiência','Audiência Una':'Audiência',
'Serviço / Audiência':'Audiência','Pauta de Julgamento':'Audiência',
'Workflow / Registro de audiência':'Audiência','Workflow / Sinalizar audiência':'Audiência',
'Serviço / Conciliação Extrajudicial':'Audiência',
// REUNIÃO
'Reunião':'Reunião','Reunião / Cliente':'Reunião','Reunião / Coordenadores':'Reunião',
'Reunião / Prospect':'Reunião','Reunião / Sócios':'Reunião','Reunião / Treinamento':'Reunião',
'Reunião de Captação':'Reunião','Reunião de Consultoria':'Reunião','Reunião Interna':'Reunião',
'Reunião / Reunião':'Reunião','Serviço / Reunião':'Reunião',
'Serviço / Acompanhamento em Reunião':'Acompanhamento em Reunião',
// CONSULTA
'Serviço / Consulta':'Consulta','Serviço / Orientação':'Consulta',
// DESPACHO
'Despacho com Magistrado':'Despacho com Magistrado',
// DILIGÊNCIA
'Diligência externa':'Diligência','Serviço / Diligência':'Diligência',
'Diversos / Diligência':'Diligência',
// TREINAMENTO
'TREINAMENTO':'Treinamento','Elaboração de Plano de Treinamento':'Elaboração de Plano de Treinamento',
// PALESTRA
'Serviço / Palestra':'Palestra',
// PARECER
'Serviço / Parecer':'Parecer','Serviço / Parecer Complexo':'Parecer',
// ACOMPANHAMENTO
'Serviço / Acompanhamento em Depoimento/Oitiva':'Acompanhamento em Depoimento/Oitiva',
// DEMANDA SEFAZ
'Serviço / Demanda Sefaz':'Demanda Sefaz',
// SERVIÇOS ESPECÍFICOS
'Serviço / Serviços Redesim':'Serviços Redesim','Serviço / Serviços Siscoex':'Serviços Siscoex',
'Serviços Redesim':'Serviços Redesim','Serviços Siscoex':'Serviços Siscoex',
// ANÁLISE CONTRATUAL/SOCIETÁRIA
'Serviço / Análise de Aditivo':'Análise de Aditivo',
'Serviço / Análise de Contrato':'Análise de Contrato',
'Serviço / Revisão Contratual':'Análise de Contrato',
'Serviço / Análise de Distrato':'Análise de Distrato',
'Serviço / Análise de Inst. Societário':'Análise de Inst. Societário',
// ALTERAÇÃO
'Serviço / Alteração AGE':'Alteração AGE','Serviço / Alteração Contratual':'Alteração Contratual',
'Serviço / Alteração Estatuto':'Alteração Estatuto',
'Serviço / Alteração Inst. Societário':'Alteração Inst. Societário',
// ELABORAÇÃO CONTRATUAL/SOCIETÁRIA
'Serviço / Elaboração de Aditivo':'Elaboração de Aditivo',
'Serviço / Protocolo de Aditivo':'Elaboração de Aditivo',
'Aditivo contratual de cláusulas de Proteção de Dados':'Elaboração de Aditivo',
'Serviço / Elaboração de cláusula':'Elaboração de Cláusula',
'Elaboração de cláusula contratual':'Elaboração de Contrato',
'Serviço / Elaboração de Contrato':'Elaboração de Contrato',
'Serviço / Contratual Comum':'Elaboração de Contrato',
'Serviço / Contratual Complexo':'Elaboração de Contrato',
'Serviço / Contratual Extraordinário':'Elaboração de Contrato',
'Serviço':'Elaboração de Contrato',
'Serviço / Elaboração de Distrato':'Elaboração de Distrato',
'Serviço / Elaboração de doc societário':'Elaboração de Inst. Societário',
'Serviço / Elaboração de Inst. Societário':'Elaboração de Inst. Societário',
'Serviço / Elaboração de Minuta':'Elaboração de Minuta',
'Serviço / Elaboração de Notificação.':'Elaboração de Notificação',
'Serviço / Elaboração de Ofício':'Elaboração de Ofício',
'Serviço / Elaboração de Requerimento':'Elaboração de Requerimento',
'Serviço / Elaboração de Termo de Compromisso':'Elaboração de Termo de Compromisso',
'ELABORAÇÃO DE TERMO DE COMPROMISSO':'Elaboração de Termo de Compromisso',
'Elaboração de Termo':'Elaboração de Termo',
// LGPD
'Análise de Inventario de processos com dados pessoais':'Análise de Inventário de Processos com Dados Pessoais',
'Análise de Política de Privacidade':'Análise de Política de Privacidade',
'Análise de Política de Segurança da Informação':'Análise de Política de Segurança da Informação',
'ANÁLISE DE TERMO DE COMPROMISSO':'Análise de Termo de Compromisso',
'Atendimento Titular de Dados -DPO':'Atendimento Titular de Dados DPO',
'Atualização Be Compliance':'Atualização Be Compliance',
'Elaboração de Aviso de cookies':'Elaboração de Aviso de Cookies',
'Elaboração de Aviso de Privacidade':'Elaboração de Aviso de Privacidade',
'Elaboração de Plano de Notificações':'Elaboração de Plano de Notificações',
'Elaboração de Política':'Elaboração de Política',
'Elaboração de Política de Privacidade':'Elaboração de Política de Privacidade',
'Elaboração de Política de Segurança da Informação':'Elaboração de Política de Segurança da Informação',
'Elaboração de relatório da análise dos riscos':'Elaboração de Relatório da Análise dos Riscos',
'Elaboração de ROPA':'Elaboração de ROPA',
'Elaboração de termos de uso':'Elaboração de Termos de Uso',
// ELABORAÇÃO DE PEÇA PROCESSUAL
'Prazo':'Elaboração de Peça Processual',
'Prazo / Ação Rescisória-Razões Finais (art. 973 CPC)':'Elaboração de Peça Processual',
'Prazo / Acompanhar Julgamento.':'Elaboração de Peça Processual',
'Prazo / Aditivo do contrato':'Elaboração de Peça Processual',
'Prazo / Agravo contra decisão que inadmite na origem Resp ou Rext - Contrarrazões (art. 1.042, § 3º, CPC)':'Elaboração de Peça Processual',
'Prazo / Agravo contra decisão que inadmite na origem Resp ou Rext (art. 1.042 c/c art. 1.003, § 5º CPC)':'Elaboração de Peça Processual',
'Prazo / Agravo de Instrumento':'Elaboração de Peça Processual',
'Prazo / Agravo de Instrumento Civel pz em dobro (Art. 525 c/c 191 CPC)':'Elaboração de Peça Processual',
'Prazo / Agravo de Instrumento Trabalhista':'Elaboração de Peça Processual',
'Prazo / Agravo de Instrumento Trabalhista (art. 897, b CLT)':'Elaboração de Peça Processual',
'Prazo / Agravo de Petição (art. 897, § 1º, CLT)':'Elaboração de Peça Processual',
'Prazo / Agravo de Petição (art. 897, a, CLT)':'Elaboração de Peça Processual',
'Prazo / Agravo Interno - Contrarrazões (art. 1.021, § 2º, CPC)':'Elaboração de Peça Processual',
'Prazo / Agravo Interno de decisão TRT':'Elaboração de Peça Processual',
'Prazo / Agravo Interno/Regimental':'Elaboração de Peça Processual',
'Prazo / Agravo Retido':'Elaboração de Peça Processual',
'Prazo / AIRO':'Elaboração de Peça Processual',
'Prazo / AIRR':'Elaboração de Peça Processual',
'Prazo / Apelação - Contrarrazões (art. 1.010, § 1º, CPC)':'Elaboração de Peça Processual',
'Prazo / Apelação Civel':'Elaboração de Peça Processual',
'Prazo / Apresentação De-Documentos':'Elaboração de Peça Processual',
'Prazo / Ato processual sem prazo fixado (art. 218, § 3º CPC)':'Elaboração de Peça Processual',
'Prazo / Contestação':'Elaboração de Peça Processual',
'Contestação (art. 190 c/c 240, III CPC - Prazo em dobro)':'Elaboração de Peça Processual',
'Prazo / Contestação (art. 335 CPC)':'Elaboração de Peça Processual',
'Prazo / Contestação Trabalhista':'Elaboração de Peça Processual',
'Prazo / Contra Razões em Recurso Trabalhista (4d)':'Elaboração de Peça Processual',
'Prazo / Contrarrazões':'Elaboração de Peça Processual',
'Prazo / Contrarrazões Embargos à Execução':'Elaboração de Peça Processual',
'Prazo / Contrarrazões RO/RR':'Elaboração de Peça Processual',
'Prazo / Cumprimento de Sentença':'Elaboração de Peça Processual',
'Prazo / Defesa Administrativa':'Elaboração de Peça Processual',
'Prazo / Defesa Administrativa - SEMACE':'Elaboração de Peça Processual',
'Prazo / Defesa Penal':'Elaboração de Peça Processual',
'Prazo / Defesa Penal - Arts. 396 e 396 A do CPP':'Elaboração de Peça Processual',
'Prazo / Elaborar e protocolar Agravo para CARF':'Elaboração de Peça Processual',
'Prazo / Elaborar e Protocolar ED para CARF':'Elaboração de Peça Processual',
'Prazo / Embargos à Execução':'Elaboração de Peça Processual',
'Prazo / Embargos à Execução Fiscal':'Elaboração de Peça Processual',
'Prazo / Embargos à Execução Trabalhista':'Elaboração de Peça Processual',
'Prazo / Embargos a Execução Trabalhista (art. 884 CLT)':'Elaboração de Peça Processual',
'Prazo / Embargos de Declaração':'Elaboração de Peça Processual',
'Prazo / Embargos de Declaração (art. 1.023/1.024 CPC)':'Elaboração de Peça Processual',
'Prazo / Embargos de Divergência (art. 1.003 CPC)':'Elaboração de Peça Processual',
'Prazo / Embargos de Terceiro':'Elaboração de Peça Processual',
'Prazo / Embargos Monitórios':'Elaboração de Peça Processual',
'Prazo / Emenda da petição inicial na tutela antecipada em caráter antecedente denegada (art. 303, § 6º, CPC)':'Elaboração de Peça Processual',
'Prazo / Emendar Inicial':'Elaboração de Peça Processual',
'Prazo / Especificar provas e temas sobre provas':'Elaboração de Peça Processual',
'Prazo / Exceção de Pré-Executividade':'Elaboração de Peça Processual',
'Prazo / Exceção Pré Executividade Trabalhista':'Elaboração de Peça Processual',
'Prazo / Habilitação - Manifestação dos Requeridos (art. 690, CPC)':'Elaboração de Peça Processual',
'Prazo / Impugnação aos Embargos Monitórios':'Elaboração de Peça Processual',
'Prazo / Impugnação Auto de Infração SRFB':'Elaboração de Peça Processual',
'Prazo / Impugnação de Cálculos Trabalhista 8d':'Elaboração de Peça Processual',
'Prazo / Indicação de bens À-Penhora':'Elaboração de Peça Processual',
'Prazo / Indicação de testemunhas (CPC art. 357) ou assistente técnico e apresentação de quesitos à perícia (art. 465, CPC)':'Elaboração de Peça Processual',
'Prazo / Juntar Documentos':'Elaboração de Peça Processual',
'Prazo / Liminar':'Elaboração de Peça Processual',
'Prazo / Mandado de Segurança':'Elaboração de Peça Processual',
'Prazo / Manfestação Diversa (20d)':'Elaboração de Peça Processual',
'Prazo / Manif Trab 48h':'Elaboração de Peça Processual',
'Prazo / Manifestação diversa':'Elaboração de Peça Processual',
'Prazo / Manifestação Diversa (30d)':'Elaboração de Peça Processual',
'Prazo / Manifestação Diversa 10d':'Elaboração de Peça Processual',
'Prazo / Manifestação Diversa 15d':'Elaboração de Peça Processual',
'Prazo / Manifestação Diversa 5d':'Elaboração de Peça Processual',
'Prazo / Manifestação Diversa 8d':'Elaboração de Peça Processual',
'Prazo / Manifestação do sócio ou da pessoa jurídica no pedido de desconsideração da personalidade jurídica (art. 135, CPC)':'Elaboração de Peça Processual',
'Prazo / Manifestação Prévia - Improbidade Administrativa':'Elaboração de Peça Processual',
'Prazo / Manifestação sobre documentos (art. 437, § 1º CPC)':'Elaboração de Peça Processual',
'Prazo / Manifestação Sobre Laudo Pericial CONAT - CE':'Elaboração de Peça Processual',
'Prazo / Nomeação de bens ou depósito em Execução Trabalhista':'Elaboração de Peça Processual',
'Prazo / Pagamento de acordo':'Elaboração de Peça Processual',
'Prazo / Pagamento de custas sob pena de cancelamento da distribuição (art. 290, CPC)':'Elaboração de Peça Processual',
'Prazo / Pagamento em execução trabalhista -15d':'Elaboração de Peça Processual',
'Prazo / Pagamento em execução trabalhista -48h':'Elaboração de Peça Processual',
'Prazo / Pedido de esclarecimentos ou correções da decisão de saneamento e organização do processo (art. 357, § 1º, CPC)':'Elaboração de Peça Processual',
'Prazo / Pedido Inicial- Emendar ou Completar (art. 321 e 801 CPC)':'Elaboração de Peça Processual',
'Prazo para apresentação de rol de testemunhas (prazo máximo - art. 357, § 4º, CPC)':'Elaboração de Peça Processual',
'Prazo / Protocolar apelação':'Elaboração de Peça Processual',
'Prazo / Protocolar prova depósito 30% em Execução':'Elaboração de Peça Processual',
'Prazo / PROTOCOLAR prova depósito parcelamento em Execução 1':'Elaboração de Peça Processual',
'Prazo / PROTOCOLAR prova depósito parcelamento em Execução 2':'Elaboração de Peça Processual',
'Prazo / PROTOCOLAR prova depósito parcelamento em Execução 3':'Elaboração de Peça Processual',
'Prazo / PROTOCOLAR prova depósito parcelamento em Execução 4':'Elaboração de Peça Processual',
'Prazo / PROTOCOLAR prova depósito parcelamento em Execução 5':'Elaboração de Peça Processual',
'Prazo / PROTOCOLAR prova depósito parcelamento em Execução 6':'Elaboração de Peça Processual',
'Prazo / Protocolar Recurso decisao TJ TRF':'Elaboração de Peça Processual',
'Prazo / Protocolar Recurso Hierárquico DRF':'Elaboração de Peça Processual',
'Prazo / Protocolar Recurso sobre decisão de Relator e Colegiados TJ TRF':'Elaboração de Peça Processual',
'Prazo / Protocolar Recurso sobre Decisão STJ STF':'Elaboração de Peça Processual',
'Prazo / Protocolar recurso sobre Decisão TJ TRF de inadmissibilidade de REsp / RE':'Elaboração de Peça Processual',
'Prazo / Protocolar recurso sobre decisão TST (4d)':'Elaboração de Peça Processual',
'Prazo / Protocolar recurso sobre sentença':'Elaboração de Peça Processual',
'Prazo / Protocolar Recurso voluntário para CARF':'Elaboração de Peça Processual',
'Prazo / Protocolar Recurso Voluntario Sefaz':'Elaboração de Peça Processual',
'Prazo / Protocolar REsp para CARF':'Elaboração de Peça Processual',
'Prazo / Protocolo Penal 2d corridos D-0':'Elaboração de Peça Processual',
'Prazo / Razões Finais Trabalhista (10 dias)':'Elaboração de Peça Processual',
'Prazo / Razões Finais Trabalhista (5 dias)':'Elaboração de Peça Processual',
'Prazo / Recurso Adesivo':'Elaboração de Peça Processual',
'Prazo / Recurso Administrativo':'Elaboração de Peça Processual',
'Prazo / Recurso de Revista':'Elaboração de Peça Processual',
'Prazo / Recurso Especial':'Elaboração de Peça Processual',
'Prazo / Recurso Especial - CARF':'Elaboração de Peça Processual',
'Prazo / Recurso Especial ou Extraordinário - Contrarrazões (art. 1.030, caput, CPC)':'Elaboração de Peça Processual',
'Prazo / Recurso Extraordinário':'Elaboração de Peça Processual',
'Prazo / Recurso Extraordinário PAF SEFAZ':'Elaboração de Peça Processual',
'Prazo / Recurso Inominado':'Elaboração de Peça Processual',
'Prazo / Recurso Ordinário':'Elaboração de Peça Processual',
'Prazo / Recurso Ordinário (JECF)':'Elaboração de Peça Processual',
'Prazo / Recurso Ordinário em Habeas Corpus':'Elaboração de Peça Processual',
'Prazo / Recurso Ordinário-Trabalhista (art. 895 CLT)':'Elaboração de Peça Processual',
'Prazo / Recurso Voluntário':'Elaboração de Peça Processual',
'Prazo / Recurso Voluntário - SEFIN - FOR':'Elaboração de Peça Processual',
'Prazo / Réplica':'Elaboração de Peça Processual',
'Prazo / Réplica a contestação - (art 350 e 351 CPC)':'Elaboração de Peça Processual',
'Prazo / Requerer o que entender De-Direito':'Elaboração de Peça Processual',
'Prazo / Vista aos Autos (art. 107, II CPC)':'Elaboração de Peça Processual',
'Razões finais escritas - Prazos sucessivos autor réu Ministério Público (art. 364 § 2º CPC)':'Elaboração de Peça Processual',
'Protocolo':'Elaboração de Peça Processual',
'Protocolo / Protocolar REsp Sefaz':'Elaboração de Peça Processual',
'Serviços/COOP':'Elaboração de Peça Processual',
'Serviço / Notificação Extrajudicial':'Elaboração de Peça Processual',
'Serviço / Requerimento':'Elaboração de Peça Processual',
'Serviço / Requerimento Administrativo':'Elaboração de Peça Processual',
'Serviço / Requerimento Complexo':'Elaboração de Peça Processual',
'Elaboração de Manifestação':'Elaboração de Peça Processual',
'Diversos / Elaborar apelação':'Elaboração de Peça Processual',
'Diversos / Manifestação Diversa (1d)':'Elaboração de Peça Processual',
'Diversos / Manifestação diversa (2d)':'Elaboração de Peça Processual',
'Diversos / Manifestação diversa (5d)':'Elaboração de Peça Processual',
'Workflow / Elaborar Agravo':'Elaboração de Peça Processual',
'Workflow / Elaborar agravo de petição':'Elaboração de Peça Processual',
'Workflow / Elaborar Agravo Interno - negativa de segmento a RE e REsp (duas peças)':'Elaboração de Peça Processual',
'Workflow / Elaborar Agravo Interno - negativa de segmento a RE ou REsp':'Elaboração de Peça Processual',
'Workflow / Elaborar Agravo Interno TST':'Elaboração de Peça Processual',
'Workflow / Elaborar apelação':'Elaboração de Peça Processual',
'Workflow / Elaborar Apelação Penal':'Elaboração de Peça Processual',
'Workflow / Elaborar ARE e AREsp (duas peças)':'Elaboração de Peça Processual',
'Workflow / Elaborar ARE ou AREsp':'Elaboração de Peça Processual',
'Workflow / Elaborar ED':'Elaboração de Peça Processual',
'Workflow / Elaborar ED Penal':'Elaboração de Peça Processual',
'Workflow / Elaborar Embargos à Execução':'Elaboração de Peça Processual',
'Workflow / Elaborar Embargos de Divergência':'Elaboração de Peça Processual',
'Workflow / Elaborar Emenda a inicial':'Elaboração de Peça Processual',
'Workflow / Elaborar Mandado de Segurança':'Elaboração de Peça Processual',
'Workflow / Elaborar Manifestação Diversa 10d':'Elaboração de Peça Processual',
'Workflow / Elaborar Manifestação Diversa 15d':'Elaboração de Peça Processual',
'Workflow / Elaborar Manifestação Diversa 20d':'Elaboração de Peça Processual',
'Workflow / Elaborar Manifestação Diversa 30d':'Elaboração de Peça Processual',
'Workflow / Elaborar Manifestação Diversa 5d':'Elaboração de Peça Processual',
'Workflow / Elaborar Manifestação Diversa 8 d':'Elaboração de Peça Processual',
'Workflow / Elaborar Pet Custas complementares':'Elaboração de Peça Processual',
'Workflow / Elaborar Razões Finais':'Elaboração de Peça Processual',
'Workflow / Elaborar RE':'Elaboração de Peça Processual',
'Workflow / Elaborar RE e REsp':'Elaboração de Peça Processual',
'Workflow / Elaborar Recurso de Sentença Penal em Juizado':'Elaboração de Peça Processual',
'Workflow / Elaborar Recurso Hierárquico Lei 9.874/99':'Elaboração de Peça Processual',
'Workflow / Elaborar Recurso para Juizado':'Elaboração de Peça Processual',
'Workflow / Elaborar Recurso Sefin':'Elaboração de Peça Processual',
'Workflow / Elaborar Recurso voluntário para CARF':'Elaboração de Peça Processual',
'Workflow / Elaborar Recurso Voluntário Sefaz':'Elaboração de Peça Processual',
'Workflow / Elaborar Replica à contestação':'Elaboração de Peça Processual',
'Workflow / Elaborar REsp':'Elaboração de Peça Processual',
'Workflow / Elaborar REsp para CARF':'Elaboração de Peça Processual',
'Workflow / Elaborar RO':'Elaboração de Peça Processual',
'Workflow / Elaborar: Especificar provas e temas sobre provas':'Elaboração de Peça Processual',
// CONTRATOS ESPECIAIS
'Diversos / Reajuste contratual':'Reajuste contratual',
'Diversos / Renovação contratual':'Renovação contratual',
// ATIVIDADE INTERNA
'Alvara':'Atividade Interna','ANÁLISE DE DOCUMENTAÇÃO':'Atividade Interna',
'ANÁLISE DE PROPOSTA':'Atividade Interna','Andamento':'Atividade Interna',
'Atendimento/Ligação':'Atividade Interna','Canal de Denúncia':'Atividade Interna',
'Criação de conteúdo':'Atividade Interna','Diversos':'Atividade Interna',
'Diversos / Contato Telefônico':'Atividade Interna',
'Diversos / Informar sentença ao cliente':'Atividade Interna',
'Diversos / Resposta de E-mail':'Atividade Interna',
'Edital':'Atividade Interna','Elaboração de certificados':'Atividade Interna',
'Elaboração de material treinamento':'Atividade Interna',
'Estudo de Caso':'Atividade Interna','Intimação':'Atividade Interna',
'Intimação Eletrônica':'Atividade Interna','Intimação Eletrônica / Verificação':'Atividade Interna',
'Intimações Iprazos':'Atividade Interna','Pesquisas/Estudos':'Atividade Interna',
'Pesquisas/Estudos / Elaboração de Nova Tese':'Atividade Interna',
'Pesquisas/Estudos / Elaboração de Relatório':'Atividade Interna',
'Publicação':'Atividade Interna','Publicação / Intimação':'Atividade Interna',
'Publicação / Verificação':'Atividade Interna','Publicações Iprazos':'Atividade Interna',
'Relatório de Processos':'Atividade Interna','Resposta de E-mail':'Atividade Interna',
'Revisão':'Atividade Interna','Revisão / Agravo contra decisão que inadmite na origem Resp ou Rext (art. 1.042 c/c art. 1.003, § 5º CPC)':'Atividade Interna',
'Saneamento de relatório':'Atividade Interna','Tratativa de Acordo':'Atividade Interna',
'Venda':'Atividade Interna','Verificar protocolo':'Atividade Interna',
'Verificar protocolo / Apelação':'Atividade Interna',
'VISTO JURÍDICO':'Atividade Interna',
'Workflow / Informar acórdão ao cliente':'Atividade Interna',
'Workflow / Enviar ao cliente petição inicial RT e documentos':'Atividade Interna',
'Workflow / Enviar sentença ao cliente (2d)':'Atividade Interna',
'Workflow / Enviar sentença ao cliente (3d)':'Atividade Interna',
'Workflow / Informar sentença ao cliente (4d)':'Atividade Interna',
'Workflow / Analisar se há honorários contratuais':'Atividade Interna',
'Workflow / Análise de execução de honorários (20d)':'Atividade Interna',
'Workflow / Atos de Impulso (15d)':'Atividade Interna','Workflow / Atos de Impulso (5d)':'Atividade Interna',
'Workflow / Conferência (4d)':'Atividade Interna','Workflow / Conferencia (7d)':'Atividade Interna',
'Workflow / Decidir providências PAT':'Atividade Interna',
'Workflow / Habilitar Dra. Imaculada no Processo':'Atividade Interna',
'Workflow / Interlocutória CPC':'Atividade Interna','Workflow / Interlocutória trabalhista':'Atividade Interna',
'Workflow / Interlocutória Trabalhista em Audiência':'Atividade Interna',
'Workflow / Memoriais (25d)':'Atividade Interna',
'Workflow / Pagamento de parcelamento execução CPC Art. 916':'Atividade Interna',
'Workflow / Parcelamento CPC Art. 916 em execução parcela 1':'Atividade Interna',
'Workflow / Parcelamento CPC Art. 916 em execução parcela 2':'Atividade Interna',
'Workflow / Parcelamento CPC Art. 916 em execução parcela 3':'Atividade Interna',
'Workflow / Parcelamento CPC Art. 916 em execução parcela 4':'Atividade Interna',
'Workflow / Parcelamento CPC Art. 916 em execução parcela 5':'Atividade Interna',
'Workflow / Parcelamento CPC Art. 916 em execução parcela 6':'Atividade Interna',
'Workflow / Protocolo (14d)':'Atividade Interna','Workflow / Protocolo (2d)':'Atividade Interna',
'Workflow / Protocolo (4d)':'Atividade Interna','Workflow / Protocolo (7d)':'Atividade Interna',
'Workflow / Protocolo (9d)':'Atividade Interna',
'Workflow / Providenciar REsp Sefaz':'Atividade Interna',
'Workflow / Providências (1d)':'Atividade Interna','Workflow / Providências (2d)':'Atividade Interna',
'Workflow / Providencias em Execução Trabalhista':'Atividade Interna',
'Workflow / Saneamento de dados (10d)':'Atividade Interna','Workflow / Saneamento de dados (1d)':'Atividade Interna',
'Workflow / Saneamento de dados (20d)':'Atividade Interna','Workflow / Saneamento de dados (35d)':'Atividade Interna',
'Workflow / Sinalizar':'Atividade Interna','Workflow / Sinalizar Perícia':'Atividade Interna',
'Workflow / Acordão TJ TRF':'Atividade Interna','Workflow / Acórdão TRT':'Atividade Interna',
'Workflow / Contrarrazões Trabalhista':'Atividade Interna',
'Workflow / Decidir providências PAT':'Atividade Interna',
'Workflow / Decisão complexa':'Atividade Interna','Workflow / Decisão Presidencia TRT':'Atividade Interna',
'Workflow / Decisão STJ/STF':'Atividade Interna','Workflow / Decisão TJ TRF sobre REsp e RE':'Atividade Interna',
'Workflow / Decisão TST':'Atividade Interna',
'Workflow / Elaborar Pet Custas complementares':'Elaboração de Peça Processual',
'Workflow / Gerar taxa recurso Sefaz':'Atividade Interna',
'Workflow / Providenciar REsp Sefaz':'Atividade Interna',
'Workflow / Registro de audiência':'Audiência',
'Memoriais':'Atividade Interna',
'Elaboração de Política de Segurança da Informação':'Elaboração de Política de Segurança da Informação',
'Serviço / Análise de Procuração':'Atividade Interna',
'Serviço / Elaboração de Procuração':'Atividade Interna',
'Serviço / Elaboração de Proposta':'Atividade Interna',
'Serviço / Elaboração de Recibo':'Atividade Interna',
'Pagamento Solidário/Subsidiário':'Atividade Interna',
'Honorários - Verificar / Monitorar':'Atividade Interna',
'Cobrança de honorarios':'Atividade Interna',
'Diversos / Reajuste contratual':'Reajuste contratual',
'Diversos / Renovação contratual':'Renovação contratual',
'Diversos / Ida à Delegacia':'Atividade Interna','Diversos / Ida à Secretaria':'Atividade Interna',
'Diversos / CJ Atualizar Sistema de Cliente':'Atividade Interna',
'Diversos / CJ Solicitações equipe técnica':'Atividade Interna',
'Diversos / CJ Verificar Trânsito em Julgado/ Cadastrar eSocial':'Atividade Interna',
'Diversos / ET Solicitações CJ':'Atividade Interna',
'Diversos / Encaminhar inicial e solicitar documentos / habilitar no processo':'Atividade Interna',
'Diversos / Verificar Processo Especial':'Atividade Interna',
'Diversos / Verificar se contrato é por ato e fazer a cobrança':'Atividade Interna',
'Reunião / Prospect':'Reunião',
  'Audiência / Audiência - Cível':'Audiência',
  'Serviço /':'Elaboração de Contrato',
  'Audiência /':'Audiência',
  'Reunião /':'Reunião',
  'Reunião / Reunião':'Reunião',
};

// Natureza simplification map (from services spreadsheet full name → short name)
const NAT_MAP = {
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área administrativa':'Societária',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Ambiental':'Ambiental',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Cível':'Cível',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Cível / Consultas':'Consultas',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Cível / Processos':'Cível',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Contratual':'Contratual',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Empresarial / Societária':'Societária',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Hospitalar':'Hospitalar',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Hospitalar / Pareceres':'Hospitalar',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / LGPD':'LGPD',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Operações e Negocios':'Operações e Negócios',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Penal':'Penal',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Penal / Processos':'Penal',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Regulatório':'Regulatório',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Trabalhista':'Trabalhista',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Trabalhista / Consultas':'Consultas',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Trabalhista / Pareceres':'Trabalhista',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Trabalhista / Processos':'Trabalhista',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Tributário':'Tributário',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Tributário / Consultas':'Consultas',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Tributário / Processos':'Tributário',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Direito Administrativo':'Direito Administrativo',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Direito Administrativo / Processos':'Direito Administrativo',
'IMACULADA GORDIANO SOCIEDADE DE ADVOGADOS / Área operacional / Consumidor':'Consumidor',
};

// Robust year extractor — handles dd/MM/yyyy, yyyy-MM-dd, Date objects, any format
function parseYear(d){
  if(!d) return NaN;
  if(d instanceof Date) return isNaN(d.getTime()) ? NaN : d.getFullYear();
  var s = String(d).trim();
  if(!s || s==='null' || s==='undefined') return NaN;
  var m = s.match(/\b(19\d{2}|20\d{2})\b/);
  return m ? parseInt(m[1], 10) : NaN;
}

function uT(t){
  if(!t || String(t).trim()==='' || t==='nan') return 'Consulta';
  var raw = String(t).trim();
  if(TAX[raw]) return TAX[raw];
  // Normalize new export format: 'Tipo - Subtipo' or 'Tipo - ' (trailing dash)
  var s = raw.replace(/\s*-\s*$/, '').trim();   // strip trailing ' - ' or ' -'
  if(TAX[s]) return TAX[s];
  s = s.replace(/ - /, ' / ');                    // replace first ' - ' with ' / '
  if(TAX[s]) return TAX[s];
  return raw;
}
function uNat(n){
  if(!n || String(n).trim()==='') return 'Não informado';
  return NAT_MAP[String(n).trim()] || String(n).trim();
}


function uT(t){
  if(!t || String(t).trim()==='' || t==='nan') return 'Consulta';
  var raw = String(t).trim();
  if(TAX[raw]) return TAX[raw];
  // Normalize new export format: 'Tipo - Subtipo' or 'Tipo - ' (trailing dash)
  var s = raw.replace(/\s*-\s*$/, '').trim();   // strip trailing ' - ' or ' -'
  if(TAX[s]) return TAX[s];
  s = s.replace(/ - /, ' / ');                    // replace first ' - ' with ' / '
  if(TAX[s]) return TAX[s];
  return raw;
}

function showErr(m){
  var el = document.getElementById('errbox');
  el.textContent = m;
  el.style.display = 'block';
}
function clrErr(){
  var el = document.getElementById('errbox');
  el.textContent = '';
  el.style.display = 'none';
}
function showWarns(list){
  var el = document.getElementById('warnblock');
  if(!list || list.length===0){ el.innerHTML=''; return; }
  var html = '<div class="warn"><h4>Atenção — '+list.length+' inconsistência(s)</h4><ul>';
  list.forEach(function(w){ html += '<li>'+w+'</li>'; });
  html += '</ul></div>';
  el.innerHTML = html;
}

function loadF(inp, key){
  var f = inp.files[0];
  if(!f) return;
  var reader = new FileReader();
  reader.onload = function(e){
    try{
      var wb = XLSX.read(new Uint8Array(e.target.result), {type:'array', cellDates:true});
      var ws = wb.Sheets[wb.SheetNames[0]];
      var rows = XLSX.utils.sheet_to_json(ws, {defval:null, raw:false});
      if(key==='serv' && rows.length>0){
        var firstVals = Object.values(rows[0]);
        if(firstVals.indexOf('Pasta')>=0 || firstVals.indexOf('Natureza')>=0){
          var oldKeys = Object.keys(rows[0]);
          var newKeys = oldKeys.map(function(k){ return rows[0][k]; });
          rows = rows.slice(1).map(function(r){
            var o={};
            oldKeys.forEach(function(ok,i){ if(newKeys[i]) o[newKeys[i]]=r[ok]; });
            return o;
          });
        }
      }
      ST[key] = rows;
      document.getElementById('dz-'+key).classList.add('ok');
      var ids = {proc:'sp', serv:'ss', aud:'sa', dec:'sd'};
      document.getElementById(ids[key]).textContent = '✓ '+f.name+' ('+rows.length+')';
    }catch(ex){
      showErr('Erro ao ler '+f.name+': '+ex.message);
    }
  };
  reader.readAsArrayBuffer(f);
}

function loadLogo(inp){
  var f = inp.files[0]; if(!f) return;
  var r = new FileReader();
  r.onload = function(e){
    ST.logo = e.target.result;
    var p = document.getElementById('lprev');
    p.src = e.target.result; p.style.display='block';
    document.getElementById('sl').textContent = '✓ '+f.name;
    document.getElementById('dz-logo').classList.add('ok');
  };
  r.readAsDataURL(f);
}

var COLORS = ['#8B0E1A','#A81020','#C01020','#D42030','#E05060','#E89090','#F5C8CC','#C4A85A','#A89860','#6B6040'];
var GOLD = '#C4A85A';

function mkBar(id, labels, vals, horiz, colors){
  if(CH[id]) CH[id].destroy();
  var bg = colors || vals.map(function(_,i){ return COLORS[i]||COLORS[COLORS.length-1]; });
  var dlPlugin = {};
  try{
    if(window.ChartDataLabels){
      dlPlugin = {datalabels:{
        anchor: horiz?'end':'end', align: horiz?'end':'top',
        color: '#333', font:{size:10, weight:'700', family:"Inter,sans-serif"},
        formatter: function(v){ return v>0?v:''; },
        clamp:true, clip:false,
        padding: horiz?{right:6}:{top:2}
      }};
    }
  }catch(e){}
  CH[id] = new Chart(document.getElementById(id), {
    type:'bar',
    data:{labels:labels, datasets:[{data:vals, backgroundColor:bg, borderRadius:4, borderSkipped:false}]},
    options:{
      indexAxis: horiz?'y':'x', responsive:true, maintainAspectRatio:false,
      plugins: Object.assign({legend:{display:false}}, dlPlugin),
      scales:{
        x:{grid:{color:horiz?'#F5E8EA':'transparent'}, ticks:{color:'#9A5060',font:{size:10}}, border:{display:false}},
        y:{grid:{color:horiz?'transparent':'#F5E8EA'}, ticks:{color:'#4A2030',font:{size:10}}, border:{display:false}}
      },
      layout:{padding:{right:horiz?40:0, top:24}}
    }
  });
}

function mkDonut(id, labels, vals){
  if(CH[id]) CH[id].destroy();
  var dlPlugin = {};
  try{
    if(window.ChartDataLabels){
      dlPlugin = {datalabels:{
        color:'#fff', font:{size:10, weight:'700'},
        formatter:function(v,ctx){
          var t=ctx.dataset.data.reduce(function(a,b){return a+b;},0);
          return v>0 ? Math.round(v/t*100)+'%' : '';
        }
      }};
    }
  }catch(e){}
  CH[id] = new Chart(document.getElementById(id), {
    type:'doughnut',
    data:{labels:labels, datasets:[{data:vals, backgroundColor:['#8B0E1A','#E89090','#C4A85A'], borderWidth:2, borderColor:'#fff'}]},
    options:{
      cutout:'56%', responsive:true, maintainAspectRatio:false,
      plugins: Object.assign({legend:{position:'bottom', labels:{font:{family:'Inter,sans-serif',size:10},color:'#4A2030',padding:8}},
        tooltip:{callbacks:{label:function(ctx){return ' '+ctx.label+': '+ctx.parsed;}}}
      }, dlPlugin)
    }
  });
}

function fDate(v){
  if(!v) return '';
  try{ var d=new Date(v); return isNaN(d)?String(v):d.toLocaleDateString('pt-BR'); }catch(e){return String(v);}
}
function fVal(v){
  var n=parseFloat(v);
  return isNaN(n)||n===0?'R$ 0,00':'R$ '+n.toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
}
function fValBlankAsZero(v){
  var n=parseFloat(v);
  return isNaN(n)?'R$ 0,00':'R$ '+n.toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});
}
function esc(v){
  return String(v||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function getField(rows, candidates){
  if(!rows||rows.length===0) return null;
  for(var i=0;i<candidates.length;i++){
    if(candidates[i] in rows[0]) return candidates[i];
  }
  return null;
}

function filterClients(rows, field, clients){
  if(!rows||!field||!clients) return rows||[];
  return rows.filter(function(r){ return r[field] && clients.indexOf(String(r[field]).trim())>=0; });
}

function generate(){
  clrErr();
  if(!ST.proc){ showErr('Faça upload da planilha de Processos.'); return; }
  if(!ST.serv){ showErr('Faça upload da planilha de Serviços.'); return; }

  var title = document.getElementById('ttl').value.trim() || 'Dashboard Jurídico';
  var cliRaw = document.getElementById('cli').value.trim();
  var yrRaw = document.getElementById('ayr').value.trim();
  var clients = cliRaw ? cliRaw.split(';').map(function(s){return s.trim();}).filter(Boolean) : null;

  Object.keys(CH).forEach(function(k){ try{CH[k].destroy();}catch(e){} });
  var warns = [];

  var procFld = getField(ST.proc, ['Cliente principal','cliente principal']);
  var servFld = getField(ST.serv, ['Cliente principal','cliente principal']);
  var audFld  = ST.aud ? getField(ST.aud,  ['Cliente Processo','Cliente processo']) : null;

  if(clients && !procFld) warns.push('Campo "Cliente principal" não encontrado na planilha de Processos.');
  if(clients && !servFld) warns.push('Campo "Cliente principal" não encontrado na planilha de Serviços.');
  if(ST.aud && clients && !audFld) warns.push('Campo "Cliente Processo" não encontrado na planilha de Audiências/Prazos.');

  var proc = (clients && procFld) ? filterClients(ST.proc, procFld, clients) : ST.proc;
  var serv = (clients && servFld) ? filterClients(ST.serv, servFld, clients) : ST.serv;
  var aud  = ST.aud ? ((clients && audFld) ? filterClients(ST.aud, audFld, clients) : ST.aud) : [];

  if(proc.length===0){
    warns.push('ERRO: Nenhum processo encontrado. Verifique os nomes dos clientes.');
    showWarns(warns);
    showErr('Nenhum processo encontrado. Verifique os nomes dos clientes.');
    return;
  }

  // Processes — Ativo+Suspenso = Ativo; ignore Inativo
  var active   = proc.filter(function(r){ return r['Status']==='Ativo'||r['Status']==='Suspenso'; });
  var archived = proc.filter(function(r){ return r['Status']==='Arquivado'; });

  var natC={};
  active.forEach(function(r){ var n=r['Natureza']||'N/A'; natC[n]=(natC[n]||0)+1; });
  var natSort = Object.entries(natC).sort(function(a,b){return b[1]-a[1];});

  var compC={};
  active.forEach(function(r){ var c=r[procFld||'Cliente principal']||'N/A'; compC[c]=(compC[c]||0)+1; });
  var compSort = Object.entries(compC).sort(function(a,b){return b[1]-a[1];}).slice(0,8);
  var multi = compSort.length > 1;

  var regY={};
  proc.filter(function(r){ return r['Status']==='Ativo'||r['Status']==='Suspenso'||r['Status']==='Arquivado'; })
      .forEach(function(r){
        var d=r['Data do cadastro']; if(!d) return;
        var y=parseYear(d); if(y>=2008&&y<=2030) regY[y]=(regY[y]||0)+1;
      });

  var archY={};
  archived.forEach(function(r){
    var d=r['Data do encerramento']; if(!d) return;
    var y=parseYear(d); if(y>=2008&&y<=2030) archY[y]=(archY[y]||0)+1;
  });

  // Services
  // Detect date column name (old files use 'Data', new exports use 'Data do cadastro')
  var servDateFld = (serv.length>0 && serv[0]['Data do cadastro']!==undefined) ? 'Data do cadastro' : 'Data';
  var servY={};
  serv.forEach(function(r){
    var d=r[servDateFld]; if(!d) return;
    var y=parseYear(d); if(y>=2012&&y<=2030) servY[y]=(servY[y]||0)+1;
  });
  var syArr = Object.keys(servY).map(Number).sort();
  var refY = yrRaw ? parseInt(yrRaw) : (syArr[syArr.length-1] || new Date().getFullYear());
  var refYCount = servY[refY] || 0;
  if(refYCount===0 && serv.length>0) warns.push('Nenhum serviço encontrado para '+refY+'. Deixe o campo em branco para usar o ano mais recente.');

  // Audiências — current year only
  var nAud=0, nPrz=0, nPer=0;
  if(aud.length===0 && ST.aud && clients) warns.push('Nenhum registro de Aud/Prazos/Perícias encontrado para os clientes. Verifique os nomes no campo "Cliente Processo".');
  aud.forEach(function(r){
    var d=r['Data de início']; if(!d) return;
    if(parseYear(d)!==refY) return;
    var t=String(r['Tipo']||'');
    if(t==='Audiência') nAud++;
    else if(t==='Prazo') nPrz++;
    else if(t==='Perícia'||t==='Pauta de Julgamento') nPer++;
  });


  // ── Item 2: Cadastrados vs Encerrados por mês no ano vigente ──
  var MONTHS = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'];
  var cmpRegMon = new Array(12).fill(0);
  var cmpArcMon = new Array(12).fill(0);
  proc.filter(function(r){return r['Status']==='Ativo'||r['Status']==='Suspenso'||r['Status']==='Arquivado';})
      .forEach(function(r){
        var d=r['Data do cadastro']; if(!d) return;
        var dt=d instanceof Date?d:new Date(String(d).trim());
        if(isNaN(dt.getTime())) return;
        if(parseYear(d)===refY) cmpRegMon[dt.getMonth()]++;
      });
  proc.filter(function(r){return r['Status']==='Arquivado';})
      .forEach(function(r){
        var d=r['Data do encerramento']; if(!d) return;
        var dt=d instanceof Date?d:new Date(String(d).trim());
        if(isNaN(dt.getTime())) return;
        if(parseYear(d)===refY) cmpArcMon[dt.getMonth()]++;
      });

  // ── Item 3: Distribuição de fases (ativos+suspensos) ──
  var faseC = {};
  active.forEach(function(r){
    var f = r['Fase'] || 'Não informado';
    faseC[f] = (faseC[f]||0)+1;
  });
  var faseSort = Object.entries(faseC).sort(function(a,b){return b[1]-a[1];});

  // ── Item 4: Passivo processual — probabilidade Provável ──
  var provTotalCausa = 0, provTotalEnvolvido = 0, provQtd = 0;
  active.forEach(function(r){
    var prob = String(r['Tipo da probabilidade atual']||'').trim();
    if(prob !== 'Provável' && prob !== 'Perda' && prob !== 'Perda Provável') return;
    var causa = parseFloat(r['Valor da causa']) || 0;
    var envol  = parseFloat(r['Valor envolvido']) || 0;
    if(causa > 0 || envol > 0){
      provTotalCausa    += causa;
      provTotalEnvolvido += envol;
      provQtd++;
    }
  });
  var provReducao = provTotalCausa - provTotalEnvolvido;

  // ── Item 5: Audiências últimos 3 anos ──
  var audYears = [refY-2, refY-1, refY];
  var audByYear = {};
  audYears.forEach(function(y){ audByYear[y]=0; });
  aud.forEach(function(r){
    var d=r['Data de início']; if(!d) return;
    var y=parseYear(d);
    if(audYears.indexOf(y)>=0 && String(r['Tipo']||'')==='Audiência') audByYear[y]=(audByYear[y]||0)+1;
  });

  var sCompY={};
  serv.forEach(function(r){
    var d=r[servDateFld]; if(!d) return;
    if(parseYear(d)!==refY) return;
    var c=r[servFld||'Cliente principal']||'N/A'; sCompY[c]=(sCompY[c]||0)+1;
  });
  var sCYS = Object.entries(sCompY).sort(function(a,b){return b[1]-a[1];}).slice(0,8);

  var sTipoY={};
  serv.forEach(function(r){
    var d=r[servDateFld]; if(!d) return;
    if(parseYear(d)!==refY) return;
    var t=uT(r['Tipo']); if(t==='Atividade Interna') return;
    sTipoY[t]=(sTipoY[t]||0)+1;
  });
  var sTYS = Object.entries(sTipoY).sort(function(a,b){return b[1]-a[1];}).slice(0,10);
  // Services by Natureza (refYear)
  var sNatY={};
  serv.forEach(function(r){
    var d=r[servDateFld]; if(!d) return;
    if(parseYear(d)!==refY) return;
    var n=uNat(r['Natureza']); sNatY[n]=(sNatY[n]||0)+1;
  });
  var sNYS = Object.entries(sNatY).sort(function(a,b){return b[1]-a[1];}).slice(0,12);


  showWarns(warns);

  // Header
  document.getElementById('dtitle').textContent = title;
  document.getElementById('dsub').textContent = 'Dashboard Jurídico Executivo — Referência '+refY;
  // Build services row dynamically — hide company chart for single client
  var sMulti = sCYS.length > 1;
  var rowserv = document.getElementById('rowserv');
  rowserv.className = 'cg ' + (sMulti ? 'c3' : 'c2');
  var compCard = sMulti
    ? '<div class="cc"><div class="ct" id="sct1">—</div><div class="ch" style="height:210px"><canvas id="chsc"></canvas></div></div>'
    : '';
  rowserv.innerHTML = compCard +
    '<div class="cc"><div class="ct" id="sct2">—</div><div class="ch" style="height:210px"><canvas id="chst"></canvas></div></div>' +
    '<div class="cc"><div class="ct" id="sct3">—</div><div class="ch" style="height:210px"><canvas id="chsn"></canvas></div></div>';

  if(sMulti) document.getElementById('sct1').textContent = 'Total de Serviços por Empresa Realizados em '+refY;
  document.getElementById('sct2').textContent = 'Total de Serviços Realizados em '+refY+' – As 10 Atividades Mais Executadas';
  document.getElementById('sct3').textContent = 'Total de Serviços Realizados em '+refY+' por Natureza';
  if(ST.logo){
    document.getElementById('clogoimg').src=ST.logo;
    document.getElementById('clogoimg').style.display='block';
    document.getElementById('clph').style.display='none';
  }

  // KPI row 1
  document.getElementById('kpi1').innerHTML =
    kpiCard('c7','Processos Ativos',active.length,'Ativos') +
    kpiCard('c8x','Processos Arquivados',archived.length,'Encerrados') +
    kpiCard('c4','Total da Carteira',active.length+archived.length,'Ativos e Encerrados') +
    kpiCard('gd','Serviços em '+refY,refYCount,'Serviços realizados');

  var audLbl = ST.aud ? 'Clientes filtrados' : 'Planilha não carregada';
  document.getElementById('kpi2').innerHTML =
    kpiCard('c6','Audiências em '+refY,nAud,audLbl) +
    kpiCard('c5','Prazos em '+refY,nPrz,audLbl) +
    kpiCard('gd','Perícias em '+refY,nPer,audLbl);

  // Top charts row
  var rtop = document.getElementById('rowtop');
  rtop.className = 'cg '+(multi?'c3':'c2');
  var compHtml = multi ? '<div class="cc"><div class="ct">Processos Ativos por Empresa</div><div class="ch" style="height:210px"><canvas id="chcmp"></canvas></div></div>' : '';
  rtop.innerHTML =
    '<div class="cc"><div class="ct">Distribuição por Status</div><div class="ch" style="height:210px"><canvas id="chpie"></canvas></div></div>' +
    '<div class="cc"><div class="ct">Processos Ativos por Natureza</div><div class="ch" style="height:210px"><canvas id="chnat"></canvas></div></div>' +
    compHtml;

  // Draw charts
  mkDonut('chpie', ['Ativos','Arquivados'], [active.length, archived.length]);
  mkBar('chnat', natSort.map(function(e){return e[0];}), natSort.map(function(e){return e[1];}), true,
    natSort.map(function(_,i){return COLORS[i]||COLORS[COLORS.length-1];}));
  if(multi && document.getElementById('chcmp')){
    mkBar('chcmp',
      compSort.map(function(e){return e[0].length>22?e[0].substring(0,22)+'…':e[0];}),
      compSort.map(function(e){return e[1];}), true,
      compSort.map(function(_,i){return COLORS[i]||COLORS[COLORS.length-1];}));
  }

  var ryK = Object.keys(regY).map(Number).sort();
  mkBar('chry', ryK, ryK.map(function(y){return regY[y]||0;}), false,
    ryK.map(function(y){return y>=2017?'#8B0E1A':'#E89090';}));

  var ayK = Object.keys(archY).map(Number).sort();
  mkBar('chay', ayK, ayK.map(function(y){return archY[y]||0;}), false,
    ayK.map(function(){return GOLD;}));

  // ── Item 2: Cadastrados vs Encerrados por mês no ano vigente ──
  document.getElementById('ctcmp').textContent = 'Processos Cadastrados × Encerrados em '+refY+' (por mês)';
  if(CH['chcmp2']) CH['chcmp2'].destroy();
  CH['chcmp2'] = new Chart(document.getElementById('chcmp2'), {
    type:'bar',
    data:{
      labels: MONTHS,
      datasets:[
        {label:'Cadastrados', data:cmpRegMon,
          backgroundColor:'#8B0E1A',borderRadius:3,borderSkipped:false},
        {label:'Encerrados',  data:cmpArcMon,
          backgroundColor:GOLD,borderRadius:3,borderSkipped:false}
      ]
    },
    options:{responsive:true,maintainAspectRatio:false,
      plugins:{
        legend:{position:'bottom',labels:{font:{family:'Inter,sans-serif',size:10},color:'#4A2030',padding:8}},
        datalabels:{anchor:'end',align:'top',color:'#333',font:{size:9,weight:'700'},
          formatter:function(v){return v>0?v:'';},clamp:true,clip:false}},
      scales:{
        x:{grid:{display:false},ticks:{color:'#4A2030',font:{size:10}},border:{display:false}},
        y:{grid:{color:'#F5E8EA'},ticks:{color:'#9A5060',font:{size:10},stepSize:1},border:{display:false}}},
      layout:{padding:{top:24}}}
  });

  // ── Item 3: Fases processuais ──
  if(CH['chfase']) CH['chfase'].destroy();
  CH['chfase'] = new Chart(document.getElementById('chfase'), {
    type:'bar',
    data:{labels:faseSort.map(function(e){return e[0];}),
      datasets:[{data:faseSort.map(function(e){return e[1];}),
        backgroundColor:faseSort.map(function(_,i){return COLORS[i]||COLORS[COLORS.length-1];}),
        borderRadius:4,borderSkipped:false}]},
    options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,
      plugins:{legend:{display:false},
        datalabels:{anchor:'end',align:'end',color:'#333',font:{size:10,weight:'700'},
          formatter:function(v){return v;},clamp:true,clip:false,padding:{right:6}}},
      scales:{x:{grid:{color:'#F5E8EA'},ticks:{color:'#9A5060',font:{size:10}},border:{display:false}},
              y:{grid:{display:false},ticks:{color:'#4A2030',font:{size:11}},border:{display:false}}},
      layout:{padding:{right:40}}}
  });

  // ── Item 4: Passivo processual ──
  (function(){
    var fmt = function(v){return 'R$ '+v.toLocaleString('pt-BR',{minimumFractionDigits:2,maximumFractionDigits:2});};
    var pct = provTotalCausa>0 ? Math.round(provReducao/provTotalCausa*100) : 0;
    var html = '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:8px">';
    html += '<div style="background:var(--c0);border-radius:8px;padding:14px;text-align:center;border-top:3px solid var(--c6)">';
    html += '<div style="font-size:.62rem;color:var(--mu);text-transform:uppercase;letter-spacing:.05em;font-weight:600">Valor da Causa</div>';
    html += '<div style="font-family:Libre Baskerville,serif;font-size:1.1rem;color:var(--c8);font-weight:700;margin-top:4px">'+fmt(provTotalCausa)+'</div>';
    html += '<div style="font-size:.65rem;color:var(--mu);margin-top:3px">'+provQtd+' processo'+(provQtd!==1?'s':'')+'</div></div>';
    html += '<div style="background:var(--c0);border-radius:8px;padding:14px;text-align:center;border-top:3px solid var(--gd)">';
    html += '<div style="font-size:.62rem;color:var(--mu);text-transform:uppercase;letter-spacing:.05em;font-weight:600">Valor Envolvido</div>';
    html += '<div style="font-family:Libre Baskerville,serif;font-size:1.1rem;color:var(--c8);font-weight:700;margin-top:4px">'+fmt(provTotalEnvolvido)+'</div>';
    html += '<div style="font-size:.65rem;color:var(--mu);margin-top:3px">Exposição real</div></div>';
    html += '<div style="background:#EAF5EA;border-radius:8px;padding:14px;text-align:center;border-top:3px solid #4A8A4A">';
    html += '<div style="font-size:.62rem;color:#2A5A2A;text-transform:uppercase;letter-spacing:.05em;font-weight:600">Redução Obtida</div>';
    html += '<div style="font-family:Libre Baskerville,serif;font-size:1.1rem;color:#2A5A2A;font-weight:700;margin-top:4px">'+fmt(provReducao)+'</div>';
    html += '<div style="font-size:.65rem;color:#2A5A2A;margin-top:3px">'+pct+'% de redução</div></div>';
    html += '</div>';
    if(provQtd===0) html='<div style="padding:20px;text-align:center;color:var(--mu);font-size:.82rem">Nenhum processo com probabilidade de perda e valores cadastrados.</div>';
    document.getElementById('passivo-content').innerHTML=html;
  })();

  // ── Item 5: Audiências últimos 3 anos ──
  document.getElementById('ctaud3').textContent = 'Audiências Realizadas — '+audYears[0]+' a '+audYears[2];
  if(CH['chaud3']) CH['chaud3'].destroy();
  CH['chaud3'] = new Chart(document.getElementById('chaud3'), {
    type:'bar',
    data:{labels:audYears.map(String),
      datasets:[{data:audYears.map(function(y){return audByYear[y]||0;}),
        backgroundColor:audYears.map(function(y,i){return i===2?'#8B0E1A':i===1?'#C01020':'#E89090';}),
        borderRadius:5,borderSkipped:false}]},
    options:{responsive:true,maintainAspectRatio:false,
      plugins:{legend:{display:false},
        datalabels:{anchor:'end',align:'top',color:'#333',font:{size:14,weight:'700'},
          formatter:function(v){return v||0;},clamp:true,clip:false}},
      scales:{x:{grid:{display:false},ticks:{color:'#4A2030',font:{size:12,weight:'600'}},border:{display:false}},
              y:{grid:{color:'#F5E8EA'},ticks:{color:'#9A5060',font:{size:10}},border:{display:false}}},
      layout:{padding:{top:30}}}
  });

  mkBar('chsy', syArr, syArr.map(function(y){return servY[y]||0;}), false,
    syArr.map(function(y){return y===refY?'#8B0E1A':'#E89090';}));

  if(sMulti && document.getElementById('chsc')){
    mkBar('chsc',
      sCYS.map(function(e){return e[0].length>22?e[0].substring(0,22)+'…':e[0];}),
      sCYS.map(function(e){return e[1];}), true,
      sCYS.map(function(_,i){return COLORS[i]||COLORS[COLORS.length-1];}));
  }

  mkBar('chst',
    sTYS.map(function(e){return e[0];}),
    sTYS.map(function(e){return e[1];}), true,
    sTYS.map(function(_,i){return COLORS[i]||COLORS[COLORS.length-1];}));

  mkBar('chsn',
    sNYS.map(function(e){return e[0];}),
    sNYS.map(function(e){return e[1];}), true,
    sNYS.map(function(_,i){return COLORS[i]||COLORS[COLORS.length-1];}));

  // ── Decisões: classification & chart ──
  (function(){
    var decBlock = document.getElementById('decblock');
    if(!ST.dec || ST.dec.length===0){ decBlock.innerHTML=''; return; }

    // Detect columns from first row
    var sample = ST.dec[0];
    var keys = Object.keys(sample);
    // Column positions (0-based): Natureza=0, Polo=3, ResultadoDecisao=15, DataPublicacao=21
    var poloFld    = keys[3]  || '';
    var resultFld  = keys[15] || '';
    var dataPubFld = keys[21] || '';
    var clientFld  = keys[2]  || '';

    // Filter by clients if provided
    var decRows = clients
      ? ST.dec.filter(function(r){ return r[clientFld] && clients.indexOf(String(r[clientFld]).trim())>=0; })
      : ST.dec;

    if(decRows.length===0){ decBlock.innerHTML=''; return; }

    // Classify decisions
    var nFav=0, nDesfav=0, nAcordo=0;
    var minDate=null, maxDate=null;

    // ── Text-based classification using decision verbs + pole rule ──
    function classifyDecision(polo, texto){
      var polo_l = String(polo||'').trim().toLowerCase();
      var polAt = polo_l==='ativo'||polo_l==='autor';
      var polPas= polo_l==='passivo'||polo_l==='réu'||polo_l==='reu';
      if(!polAt && !polPas) return null;

      var t = String(texto||'').toLowerCase();
      if(!t||t==='nan'||t==='null') return null;

      // Extinção
      if(/declaro\s+extint|extingo\s+o\s+processo|extinta\s+a\s+execu|extinção.*processo/.test(t))
        return 'extinto';

      // Parcial procedência
      if(/parcialmente\s+proced|julgo\s+parcial|procedente\s+em\s+parte|em\s+parte\s+procedente/.test(t)){
        return polAt ? 'favoravel_parcial' : 'desfavoravel_parcial';
      }
      // Procedência
      if(/julgo\s+proced[ea]nte(?!\s*ncia)|julgado\s+proced(?!ência)|julgar\s+proced(?!ência)|procedência\s+do|dou\s+provimento|concedo\s+(parcialmente\s+)?a\s+seguran|condeno\s+[ao]\s+r[eéu]|acolho\s+os?\s+pedidos?/.test(t)){
        return polAt ? 'favoravel' : 'desfavoravel';
      }
      // Improcedência (inclui "REJEITAR preliminar...julgar IMPROCEDENTES", "decide...IMPROCEDENTES")
      if(/julgo\s+improced[ea]nte|julgado\s+improced|julgar\s+improced|improcedência\s+do|improcedentes\s+os\s+pedidos|totalmente\s+improcedentes|pedidos?.*improced|rejeito\s+os?\s+pedidos?|decide.*julgar\s+improced|decide.*improcedente|julgar\s+os\s+pedidos.*improced/.test(t)){
        return polAt ? 'desfavoravel' : 'favoravel';
      }
      return null; // verb not identified
    }

    decRows.forEach(function(r){
      var datePub = r[dataPubFld];
      if(datePub){
        var dp = datePub instanceof Date ? datePub : new Date(String(datePub).split('/').reverse().join('-'));
        if(!isNaN(dp.getTime())){
          if(!minDate||dp<minDate) minDate=dp;
          if(!maxDate||dp>maxDate) maxDate=dp;
        }
      }
      var cls = classifyDecision(r[poloFld], r[keys[keys.length-1]]);
      if(cls==='favoravel'||cls==='favoravel_parcial')            nFav++;
      else if(cls==='desfavoravel'||cls==='desfavoravel_parcial') nDesfav++;
      else if(cls==='extinto')                                    nAcordo++;
    });

    var total = nFav+nDesfav+nAcordo;
    if(total===0){ decBlock.innerHTML=''; return; }

    // Period label
    var fmtD=function(d){ return d?d.toLocaleDateString('pt-BR',{month:'short',year:'numeric'}):''; };
    var period = (minDate&&maxDate)
      ? (minDate.getMonth()===maxDate.getMonth()&&minDate.getFullYear()===maxDate.getFullYear()
          ? fmtD(minDate)
          : fmtD(minDate)+' a '+fmtD(maxDate))
      : '';
    var chartTitle = 'Resultado das Decisões'+(period?' — '+period:'');

    // Build chart HTML
    decBlock.innerHTML = '<div class="sd"></div><div class="sbn" style="background:var(--c9)"><h2>🏛️ Decisões Judiciais</h2></div>' +
      '<div class="cg c2" style="margin-bottom:12px">' +
      '<div class="cc"><div class="ct">'+chartTitle+'</div>' +
      '<div class="ch" style="height:220px"><canvas id="chdec"></canvas></div></div>' +
      '<div class="cc"><div class="ct">Resultado por Tipo</div>' +
      '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;padding:12px 0" id="dec-kpis"></div></div>' +
      '</div>';

    // KPI cards
    var pctFav   = Math.round(nFav/total*100);
    var pctDesfav= Math.round(nDesfav/total*100);
    var pctAcordo= nAcordo>0?Math.round(nAcordo/total*100):0;
    var kpiHtml =
      '<div style="background:#EAF5EA;border-radius:8px;padding:14px;text-align:center;border-top:3px solid #4A8A4A">'+
        '<div style="font-size:.6rem;color:#2A5A2A;text-transform:uppercase;letter-spacing:.05em;font-weight:600">Favoráveis</div>'+
        '<div style="font-family:Libre Baskerville,serif;font-size:1.8rem;color:#2A5A2A;font-weight:700">'+nFav+'</div>'+
        '<div style="font-size:.65rem;color:#2A5A2A">'+pctFav+'% do total</div></div>'+
      '<div style="background:var(--c0);border-radius:8px;padding:14px;text-align:center;border-top:3px solid var(--c7)">'+
        '<div style="font-size:.6rem;color:var(--mu);text-transform:uppercase;letter-spacing:.05em;font-weight:600">Desfavoráveis</div>'+
        '<div style="font-family:Libre Baskerville,serif;font-size:1.8rem;color:var(--c8);font-weight:700">'+nDesfav+'</div>'+
        '<div style="font-size:.65rem;color:var(--mu)">'+pctDesfav+'% do total</div></div>'+
      (nAcordo>0?
        '<div style="background:#FFF8E0;border-radius:8px;padding:14px;text-align:center;border-top:3px solid var(--gd)">'+
          '<div style="font-size:.6rem;color:#7A6000;text-transform:uppercase;letter-spacing:.05em;font-weight:600">Extintos</div>'+
          '<div style="font-family:Libre Baskerville,serif;font-size:1.8rem;color:#7A6000;font-weight:700">'+nAcordo+'</div>'+
          '<div style="font-size:.65rem;color:#7A6000">'+pctAcordo+'% do total</div></div>'
        :'<div style="background:var(--c0);border-radius:8px;padding:14px;text-align:center;border-top:3px solid var(--bd)">'+
          '<div style="font-size:.6rem;color:var(--mu);text-transform:uppercase;letter-spacing:.05em;font-weight:600">Total Analisado</div>'+
          '<div style="font-family:Libre Baskerville,serif;font-size:1.8rem;color:var(--c8);font-weight:700">'+total+'</div>'+
          '<div style="font-size:.65rem;color:var(--mu)">decisões classificadas</div></div>');
    document.getElementById('dec-kpis').innerHTML = kpiHtml;

    // Chart
    if(CH['chdec']) CH['chdec'].destroy();
    var decLabels = ['Favoráveis','Desfavoráveis'];
    var decVals   = [nFav, nDesfav];
    var decColors = ['#4A8A4A','#8B0E1A'];
    if(nAcordo>0){ decLabels.push('Extintos'); decVals.push(nAcordo); decColors.push('#C4A85A'); }
    CH['chdec'] = new Chart(document.getElementById('chdec'),{
      type:'doughnut',
      data:{labels:decLabels,datasets:[{data:decVals,backgroundColor:decColors,borderWidth:3,borderColor:'#fff'}]},
      options:{cutout:'55%',responsive:true,maintainAspectRatio:false,
        plugins:{
          legend:{position:'bottom',labels:{font:{family:'Inter,sans-serif',size:11},color:'#4A2030',padding:10}},
          datalabels:{color:'#fff',font:{size:11,weight:'700'},
            formatter:function(v,ctx){
              var t=ctx.dataset.data.reduce(function(a,b){return a+b;},0);
              return v>0?Math.round(v/t*100)+'%':'';
            }},
          tooltip:{callbacks:{label:function(ctx){return ' '+ctx.label+': '+ctx.parsed+' ('+Math.round(ctx.parsed/total*100)+'%)';}}}
        }}
    });
  })();

  window._rpt = {proc:proc, active:active, archived:archived, natSort:natSort, title:title, refY:refY, nAud:nAud, nPrz:nPrz, nPer:nPer};

  document.getElementById('cfg').style.display = 'none';
  document.getElementById('dsh').style.display = 'block';
  window.scrollTo(0,0);
}

function kpiCard(col, lbl, val, det){
  var colors = {'c7':'var(--c7)','c8x':'#8A6060','c4':'var(--c4)','gd':'var(--gd)','c6':'var(--c6)','c5':'var(--c5)'};
  var bc = colors[col] || 'var(--c6)';
  return '<div class="kp" style="border-top-color:'+bc+'">' +
    '<div class="kl">'+lbl+'</div>' +
    '<div class="kv">'+val+'</div>' +
    '<div class="kd">'+det+'</div></div>';
}

function showReport(){
  var d = window._rpt; if(!d) return;
  document.getElementById('rtitle').textContent = 'Relatório de Processos — '+d.title;
  var now = new Date().toLocaleDateString('pt-BR',{day:'2-digit',month:'long',year:'numeric'});
  document.getElementById('rsub').textContent = 'Gerado em: '+now;
  document.getElementById('rfdate').textContent = now;
  document.getElementById('rnote').textContent = 'Processos com status Ativo e Suspenso, ordenados por Natureza. Os campos Data da Distribuição e Contrário principal são preenchidos quando disponíveis na planilha.';
  document.getElementById('rkpis').innerHTML =
    '<div class="rk"><div class="l">Ativos</div><div class="v">'+d.active.length+'</div></div>' +
    '<div class="rk"><div class="l">Arquivados</div><div class="v">'+d.archived.length+'</div></div>' +
    '<div class="rk"><div class="l">Total</div><div class="v">'+(d.active.length+d.archived.length)+'</div></div>' +
    '<div class="rk"><div class="l">Audiências '+d.refY+'</div><div class="v">'+d.nAud+'</div></div>' +
    '<div class="rk"><div class="l">Prazos '+d.refY+'</div><div class="v">'+d.nPrz+'</div></div>';

  var nh = '<table class="pt"><thead><tr><th>Natureza</th><th style="text-align:right">Qtd.</th><th style="text-align:right">%</th></tr></thead><tbody>';
  d.natSort.forEach(function(e){
    nh += '<tr><td>'+esc(e[0])+'</td><td style="text-align:right;font-weight:700">'+e[1]+'</td><td style="text-align:right">'+Math.round(e[1]/d.active.length*100)+'%</td></tr>';
  });
  nh += '</tbody></table>';
  document.getElementById('rnat').innerHTML = nh;

  var sorted = d.active.slice().sort(function(a,b){return (a['Natureza']||'').localeCompare(b['Natureza']||'');});
  var tbody = document.getElementById('rtbody'); tbody.innerHTML='';
  sorted.forEach(function(r,i){
    var dtD = r['Data da distribuição'] || r['Data do cadastro'];
    var tr = '<tr>' +
      '<td>'+(i+1)+'</td>' +
      '<td><b>'+esc(r['Natureza'])+'</b></td>' +
      '<td title="'+esc(r['Ação'])+'">'+esc((r['Ação']||'').substring(0,35))+'</td>' +
      '<td style="white-space:nowrap">'+fDate(dtD)+'</td>' +
      '<td>'+esc((r['Cliente principal']||'').substring(0,28))+'</td>' +
      '<td>'+esc(r['Posição']||'')+'</td>' +
      '<td>'+esc((r['Contrário principal']||'').substring(0,28))+'</td>' +
      '<td>'+esc((r['Órgão']||'').substring(0,25))+'</td>' +
      '<td>'+esc(r['Cidade']||'')+'</td><td>'+esc(r['UF']||'')+'</td>' +
      '<td style="text-align:right;white-space:nowrap">'+fVal(r['Valor da causa'])+'</td>' +
      '<td style="text-align:right;white-space:nowrap">'+fVal(r['Valor envolvido'])+'</td>' +
      '<td>'+esc(r['Tipo da probabilidade atual']||'')+'</td>' +
      '<td>'+esc(r['Faixa de probabilidade atual']||'')+'</td>' +
      '<td>'+esc(r['Classificação do Processo']||'Comum')+'</td>' +
      '</tr>';
    tbody.innerHTML += tr;
  });
  document.getElementById('dsh').style.display = 'none';
  document.getElementById('rpt').style.display = 'block';
  window.scrollTo(0,0);
}

function exportXLS(){
  var d = window._rpt; if(!d) return;
  var sorted = d.active.slice().sort(function(a,b){return (a['Natureza']||'').localeCompare(b['Natureza']||'');});

  var H='#8B0E1A', H2='#A81020', ALT='#FDE8EA', GC='#C4A85A', BD='#EDD8DA';
  var co='style="padding:5px 8px;border:1px solid '+BD+';font-family:Calibri;font-size:9pt;vertical-align:top;background:';
  var coH='style="padding:7px 8px;background:'+H+';color:#fff;font-weight:700;border:1px solid #6B0010;font-family:Calibri;font-size:9pt;text-align:left"';

  var headers=['Natureza','Ação','Data da Distribuição','Cliente principal','Posição','Contrário principal','Órgão','Cidade','UF','Valor da causa (R$)','Valor envolvido (R$)','Tipo da probabilidade atual','Faixa de probabilidade atual','Classificação do Processo'];
  var hRow = '<tr>'+headers.map(function(h){return '<th '+coH+'>'+h+'</th>';}).join('')+'</tr>';

  var dRows = sorted.map(function(r,i){
    var bg = i%2 ? ALT : '#fff';
    var cols=[
      '<b style="color:'+H+'">'+esc(r['Natureza'])+'</b>',
      esc(r['Ação']),
      fDate(r['Data da distribuição']||r['Data do cadastro']),
      esc(r['Cliente principal']),
      esc(r['Posição']),
      esc(r['Contrário principal']||''),
      esc(r['Órgão']),
      esc(r['Cidade']),
      esc(r['UF']),
      fValBlankAsZero(r['Valor da causa']).replace('R$ ',''),
      fValBlankAsZero(r['Valor envolvido']).replace('R$ ',''),
      esc(r['Tipo da probabilidade atual']),
      esc(r['Faixa de probabilidade atual']),
      esc(r['Classificação do Processo']||'Comum')
    ];
    return '<tr>'+cols.map(function(v){return '<td '+co+bg+'">'+(v||'')+'</td>';}).join('')+'</tr>';
  }).join('');

  var natRows = d.natSort.map(function(e,i){
    var bg = i%2?ALT:'#fff';
    return '<tr><td style="padding:6px 10px;border:1px solid '+BD+';background:'+bg+';font-family:Calibri;font-weight:600">'+esc(e[0])+'</td><td style="padding:6px 10px;border:1px solid '+BD+';background:'+bg+';text-align:center;font-weight:700;color:'+H+'">'+e[1]+'</td><td style="padding:6px 10px;border:1px solid '+BD+';background:'+bg+';text-align:center">'+Math.round(e[1]/d.active.length*100)+'%</td></tr>';
  }).join('');

  var proc_table =
    '<table>' +
    '<tr><td colspan="'+headers.length+'" style="padding:12px;background:'+H+';color:#fff;font-size:14pt;font-weight:700;font-family:Calibri">'+esc(d.title)+' — Processos Ativos</td></tr>' +
    '<tr><td colspan="'+headers.length+'" style="padding:5px 12px;background:'+H2+';color:#fff;font-size:9pt;font-family:Calibri">Total: '+sorted.length+' processos · Gerado em '+new Date().toLocaleDateString('pt-BR')+'</td></tr>' +
    hRow + dRows + '</table>';

  var res_table =
    '<table>' +
    '<tr><td colspan="3" style="padding:12px;background:'+H+';color:#fff;font-size:14pt;font-weight:700;font-family:Calibri">'+esc(d.title.toUpperCase())+' — RESUMO</td></tr>' +
    '<tr><td colspan="3" style="padding:6px 12px;background:'+H2+';color:#fff;font-size:10pt;font-family:Calibri">Gerado em: '+new Date().toLocaleDateString('pt-BR',{day:'2-digit',month:'long',year:'numeric'})+'</td></tr>' +
    '<tr><td colspan="3" style="padding:4px"></td></tr>' +
    '<tr><td style="padding:8px 12px;background:'+GC+';color:#fff;font-weight:700;border:1px solid '+BD+';font-family:Calibri">INDICADOR</td><td style="padding:8px 12px;background:'+GC+';color:#fff;font-weight:700;border:1px solid '+BD+';font-family:Calibri">VALOR</td><td style="background:'+GC+';border:1px solid '+BD+'"></td></tr>' +
    '<tr><td style="padding:6px 12px;border:1px solid '+BD+';font-family:Calibri">Processos Ativos</td><td style="padding:6px 12px;border:1px solid '+BD+';font-weight:700;color:'+H+';text-align:center;font-family:Calibri">'+d.active.length+'</td><td style="border:1px solid '+BD+'"></td></tr>' +
    '<tr><td style="padding:6px 12px;border:1px solid '+BD+';background:'+ALT+';font-family:Calibri">Processos Arquivados</td><td style="padding:6px 12px;border:1px solid '+BD+';background:'+ALT+';font-weight:700;color:'+H+';text-align:center;font-family:Calibri">'+d.archived.length+'</td><td style="border:1px solid '+BD+';background:'+ALT+'"></td></tr>' +
    '<tr><td style="padding:6px 12px;border:1px solid '+BD+';font-family:Calibri">Total Carteira</td><td style="padding:6px 12px;border:1px solid '+BD+';font-weight:700;color:'+H+';text-align:center;font-family:Calibri">'+(d.active.length+d.archived.length)+'</td><td style="border:1px solid '+BD+'"></td></tr>' +
    '<tr><td colspan="3" style="padding:4px"></td></tr>' +
    '<tr><td style="padding:8px;background:'+H2+';color:#fff;font-weight:700;border:1px solid '+BD+';font-family:Calibri">NATUREZA</td><td style="padding:8px;background:'+H2+';color:#fff;font-weight:700;border:1px solid '+BD+';font-family:Calibri;text-align:center">QTD.</td><td style="padding:8px;background:'+H2+';color:#fff;font-weight:700;border:1px solid '+BD+';font-family:Calibri;text-align:center">%</td></tr>' +
    natRows + '</table>';

  var xls = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel">\n<head><meta charset="UTF-8">\n<!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets>\n<x:ExcelWorksheet><x:Name>Processos Ativos</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet>\n<x:ExcelWorksheet><x:Name>Resumo</x:Name></x:ExcelWorksheet>\n</x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]-->\n</head>\n<body>\n<div id="Processos Ativos">'+proc_table+'</div>\n<div id="Resumo">'+res_table+'</div>\n</body>\n</html>';

  var blob = new Blob(['\ufeff'+xls], {type:'application/vnd.ms-excel;charset=utf-8'});
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href=url; a.download=(d.title||'Relatorio').replace(/[^a-zA-Z0-9\u00C0-\u024F ]/g,'_')+' - Processos Ativos.xls';
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  setTimeout(function(){URL.revokeObjectURL(url);}, 5000);
}

function goBack(){ document.getElementById('dsh').style.display='none'; document.getElementById('cfg').style.display='flex'; }
function hideReport(){ document.getElementById('rpt').style.display='none'; document.getElementById('dsh').style.display='block'; }
function printDash(){ document.body.setAttribute('data-print','dash'); window.print(); setTimeout(function(){document.body.removeAttribute('data-print');},2000); }
function printReport(){ document.body.setAttribute('data-print','report'); window.print(); setTimeout(function(){document.body.removeAttribute('data-print');},2000); }

window.addEventListener('load', function(){
  try{ if(window.ChartDataLabels) Chart.register(ChartDataLabels); }catch(e){}
});
"""

# Build complete HTML
html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Dashboard Jurídico — IGSA</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
""" + CSS + """
</style>
</head>
<body>

<!-- CONFIG -->
<div id="cfg">
<div class="cfgh">
  <img src=\"""" + LOGO + """\" alt="IGSA">
  <h1 class="sf">Gerador de Dashboard Jurídico</h1>
  <p>Imaculada Gordiano Sociedade de Advogados</p>
</div>
<div class="card">
<div class="grid2">
<div>
  <div class="stl"><span class="sn">1</span>Planilhas de dados</div>
  <div class="up3">
    <div class="dz" id="dz-proc">
      <input type="file" accept=".xlsx,.xls" onchange="loadF(this,'proc')">
      <div class="dzi">📋</div><div class="dzl">Processos</div>
      <div class="dzs">.xlsx / .xls</div><div class="dzst" id="sp">Nenhum arquivo</div>
    </div>
    <div class="dz" id="dz-serv">
      <input type="file" accept=".xlsx,.xls" onchange="loadF(this,'serv')">
      <div class="dzi">⚖️</div><div class="dzl">Serviços</div>
      <div class="dzs">.xlsx / .xls</div><div class="dzst" id="ss">Nenhum arquivo</div>
    </div>
    <div class="dz" id="dz-aud">
      <input type="file" accept=".xlsx,.xls" onchange="loadF(this,'aud')">
      <div class="dzi">🗓️</div><div class="dzl">Aud / Prazos / Perícias</div>
      <div class="dzs">.xlsx / .xls</div><div class="dzst" id="sa">Nenhum arquivo</div>
    </div>
    <div class="dz" id="dz-dec">
      <input type="file" accept=".xlsx,.xls" onchange="loadF(this,'dec')">
      <div class="dzi">⚖️</div><div class="dzl">Decisões <em style="font-size:.62rem;font-weight:400">(opcional)</em></div>
      <div class="dzs">.xlsx / .xls</div><div class="dzst" id="sd">Nenhum arquivo</div>
    </div>
  </div>
  <div class="stl"><span class="sn">2</span>Logo do cliente / grupo</div>
  <div class="dz" id="dz-logo" style="display:flex;align-items:center;gap:12px;text-align:left">
    <input type="file" accept="image/*" onchange="loadLogo(this)">
    <div style="font-size:1.5rem">🏢</div>
    <div style="flex:1"><div class="dzl">Carregar logo do cliente</div>
    <div class="dzs">PNG, JPG, SVG</div><div class="dzst" id="sl">Nenhuma imagem</div></div>
    <img id="lprev" style="display:none;max-height:42px;max-width:80px;border-radius:4px" src="" alt="">
  </div>
</div>
<div>
  <div class="stl"><span class="sn">3</span>Configurações</div>
  <div class="fld"><label>Título do dashboard</label>
    <input type="text" id="ttl" placeholder="Ex: Alscience Metrologia">
  </div>
  <div class="fld"><label>Cliente(s) — separe por ; para múltiplos</label>
    <input type="text" id="cli" placeholder="Ex: EMPRESA LTDA.;SÓCIO NOME">
    <small>💡 Nomes idênticos ao campo "Cliente principal" / "Cliente Processo" das planilhas</small>
  </div>
  <div class="fld"><label>Ano de referência dos serviços <em style="font-weight:300;text-transform:none">(opcional)</em></label>
    <input type="text" id="ayr" placeholder="Deixe em branco para usar o ano mais recente">
  </div>
  <div id="errbox" class="err"></div>
  <button class="bgen" onclick="generate()">▶ Gerar Dashboard</button>
  <div id="warnblock"></div>
  <div style="text-align:center;font-size:.65rem;color:var(--mu);margin-top:7px">Processamento 100% local — sem envio de dados externos</div>
</div>
</div>
</div>
</div>

<!-- DASHBOARD -->
<div id="dsh">
<div class="tbar">
  <button class="tb tbk" onclick="goBack()">← Voltar</button>
  <span class="thi">Imaculada Gordiano Sociedade de Advogados · Dashboard Jurídico</span>
  <div class="tbtns">
    <button class="tb trl" onclick="showReport()">📄 Relatório de Processos</button>
    <button class="tb tpd" onclick="printDash()">⬇ Exportar PDF</button>
  </div>
</div>
<div class="dw">
  <div class="dh">
    <div class="dhl"><img src=\"""" + LOGO + """\" alt="IGSA"></div>
    <div class="dht">
      <div class="dmt sf" id="dtitle">—</div>
      <div class="dsb" id="dsub">Dashboard Jurídico Executivo</div>
    </div>
    <div class="clo">
      <img id="clogoimg" src="" style="display:none" alt="">
      <div id="clph" class="clph">Logo do Cliente</div>
    </div>
  </div>
  <div class="sbn"><h2>📋 Processos Judiciais</h2></div>
  <div class="kr" id="kpi1"></div>
  <div class="kr" id="kpi2" style="margin-bottom:18px"></div>
  <div class="cg c3" id="rowtop"></div>
  <div class="cg c2" style="margin-bottom:12px">
    <div class="cc"><div class="ct">Processos Cadastrados por Ano</div><div class="ch" style="height:190px"><canvas id="chry"></canvas></div></div>
    <div class="cc"><div class="ct">Processos Encerrados por Ano</div><div class="ch" style="height:190px"><canvas id="chay"></canvas></div></div>
  </div>
  <div class="cg c2" style="margin-bottom:12px">
    <div class="cc"><div class="ct" id="ctcmp">—</div><div class="ch" style="height:200px"><canvas id="chcmp2"></canvas></div></div>
    <div class="cc"><div class="ct">Distribuição por Fase Processual</div><div class="ch" style="height:200px"><canvas id="chfase"></canvas></div></div>
  </div>
  <div class="cg c2" style="margin-bottom:12px">
    <div class="cc" id="passivo-card">
      <div class="ct">Redução do Passivo Processual — Probabilidade de Perda</div>
      <div id="passivo-content" style="padding:8px 0"></div>
    </div>
    <div class="cc"><div class="ct" id="ctaud3">—</div><div class="ch" style="height:200px"><canvas id="chaud3"></canvas></div></div>
  </div>
  <div id="decblock"></div>
  <div class="sd"></div>
  <div class="sbn" style="background:var(--c7)"><h2>⚖️ Serviços Realizados</h2></div>
  <div class="cg c1" style="margin-bottom:12px">
    <div class="cc"><div class="ct">Total de Serviços por Ano</div><div class="ch" style="height:150px"><canvas id="chsy"></canvas></div></div>
  </div>
  <div id="rowserv"></div>
</div>
</div>

<!-- RELATÓRIO -->
<div id="rpt">
<div class="tbar">
  <button class="tb tbk" onclick="hideReport()">← Voltar ao Dashboard</button>
  <span class="thi" style="color:var(--c3)">Relatório de Processos — Imaculada Gordiano</span>
  <button class="tb tpd" onclick="printReport()">⬇ Exportar PDF</button>
</div>
<div class="rw">
  <div class="rh">
    <img src=\"""" + LOGO + """\" alt="IGSA">
    <div class="rtb">
      <h1 id="rtitle">Relatório de Processos</h1>
      <p id="rsub">—</p>
    </div>
  </div>
  <div class="rnote" id="rnote"></div>
  <div class="rbtns">
    <button class="rb rxl" onclick="exportXLS()">⬇ Exportar Excel (.xls)</button>
    <button class="rb rpf" onclick="printReport()">⬇ Exportar PDF (Imprimir)</button>
  </div>
  <div class="rks" id="rkpis"></div>
  <div class="rs">Processos Ativos e Suspensos por Natureza</div>
  <div id="rnat"></div>
  <div class="rs">Lista Completa — Processos Ativos e Suspensos</div>
  <table class="pt" id="rptable">
    <thead><tr>
      <th>#</th><th>Natureza</th><th>Ação</th><th>Data Distribuição</th>
      <th>Cliente principal</th><th>Posição</th><th>Contrário principal</th>
      <th>Órgão</th><th>Cidade</th><th>UF</th>
      <th>Valor da causa</th><th>Valor envolvido</th>
      <th>Probabilidade</th><th>Faixa</th><th>Classificação</th>
    </tr></thead>
    <tbody id="rtbody"></tbody>
  </table>
  <div style="margin-top:32px;padding-top:12px;border-top:1px solid var(--bd);font-size:.63rem;color:var(--mu);text-align:center">
    Imaculada Gordiano Sociedade de Advogados · Gerado em <span id="rfdate"></span>
  </div>
</div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-datalabels/2.2.0/chartjs-plugin-datalabels.min.js"></script>
<script>
""" + JS + """
</script>
</body>
</html>"""

with open('/home/claude/dashboard_final.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done:', len(html), 'chars')

# Quick sanity checks
assert html.count('function generate()') == 1
assert html.count('<script>') == 1
assert html.count('</script>') >= 1  # CDN scripts are separate tags
# No </script> inside the JS content
js_start = html.rfind('<script>') + 8
js_end = html.rfind('</script>')
js_content = html[js_start:js_end]
assert '</script>' not in js_content.lower(), 'FATAL: </script> inside script!'
# Brace balance
opens = js_content.count('{'); closes = js_content.count('}')
assert opens == closes, f'Brace mismatch: {opens} vs {closes}'
print('All checks passed')
print('Braces balanced:', opens)
