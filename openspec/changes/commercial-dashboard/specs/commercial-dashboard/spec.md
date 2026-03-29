## ADDED Requirements

### Requirement: Visualização do Dashboard Comercial
O sistema MUST prover uma interface visual para acompanhamento dos indicadores comerciais.

#### Scenario: Acesso ao dashboard
- **WHEN** o usuário (gestor ou vendedor) acessar a plataforma
- **THEN** o sistema exibirá uma visão consolidada (em dark theme) com os principais KPIs comerciais.

### Requirement: Exibição de KPIs Chave
O dashboard MUST exibir indicadores calculados de Faturamento (R$), Volume (Kg), Positivação e Ticket Médio, comparando o Ano Atual com o Ano Anterior (YoY).
*Nota Técnica: Os cálculos básicos da base de dados operam com os filtros de faturamento `COD_OPER` filtrados em `S` (Saída) e `SM` (Saída de Mercadoria).*

#### Scenario: Visualização de faturamento e volume
- **WHEN** os dados forem carregados com sucesso
- **THEN** o painel mostrará cards em destaque com o Faturamento Total em R$ e Volume Total em Kg.

### Requirement: Tabela de Evolução Mensal
O dashboard MUST conter uma tabela ou gráfico de evolução mês a mês dos indicadores.

#### Scenario: Análise temporal das vendas
- **WHEN** visualizar a seção de evolução mensal
- **THEN** devem ser exibidos os dados de Faturamento, Kg, Positivação e Ticket Médio mes a mes.

### Requirement: Ranking Top Marcas
O dashboard MUST apresentar um ranking das 10 principais marcas vendidas, incluindo volume em Kg.

#### Scenario: Análise de performance de produtos
- **WHEN** visualizar a seção de ranking
- **THEN** uma lista hierárquica das Top 10 marcas deverá ser exibida ordenada pelo maior faturamento ou volume.
