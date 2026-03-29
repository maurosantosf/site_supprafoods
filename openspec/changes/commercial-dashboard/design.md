## Context

A empresa possui dados de vendas em seu sistema ERP (GTEX) mas não tem uma visualização unificada em tempo real ou de fácil acesso para a equipe comercial acompanhar faturamento, positivação, vendas em Kg e ticket médio. Atualmente, partes das análises podem estar sendo feitas em planilhas ou sistemas separados. Precisamos de um painel de indicadores (Dashboard) focado no nível tático/operacional de vendas.

## Goals / Non-Goals

**Goals:**
- Prover um painel visual (Dark Theme) focado em KPIs comerciais: faturamento (R$), volume (Kg), ticket médio mensais e anuais, além de um ranking top 10 marcas.
- Automatizar o processo de leitura de dados do ERP GTEX para o dashboard.
- Garantir atualização e confiabilidade dos dados.

**Non-Goals:**
- Criação de dashboards de outros setores (RH, Produção), que ficarão para próximas etapas da iniciativa.
- Substituir o ERP atual; a solução é estritamente analítica e de leitura.

## Decisions

- **Ferramenta de Visualização**: A ser decidida no momento da implementação (Power BI, Google Sheets com custom HTML/Apps Script ou web app customizado com Python/Dash/Streamlit). Será priorizada a que oferecer melhor custo-benefício e menor atrito para a equipe comercial, mas as conversas anteriores indicam uma integração Google Sheets automada por Python ou Power BI.
- **Processamento de Dados (ETL)**: Scripts Python para extrair os dados granulares da base GTEX, realizar o cálculo (agrupamentos, YoY, ticket médio) e carregar para a plataforma do dashboard ativo (por exemplo, aba auxiliar 'Pagina1' no Sheets).
- **Estética**: Implementação de Dark Theme moderno para proporcionar usabilidade agradável aos gestores e rápida identificação de metas alcançadas (destaques em verde/vermelho).

## Risks / Trade-offs

- **[Risco] Acesso instável ao banco de dados ERP GTEX** -> **Mitigação**: Executar a extração de dados em background ou via cron, acumulando num banco intermediário ou planilha, sem fazer consultas SQL on-the-fly pelo dashboard, evitando onerar o sistema.
- **[Trade-off] Atualização em Tempo Real vs. Lote (Batch)** -> Optar por lote (ex: a cada 1 hora ou diário) melhora o desempenho e reduz custos de processamento, face ao benefício quase nulo do real-time estrito para ticket médio mensal.
