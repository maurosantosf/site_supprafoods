## 1. Configuração e Infraestrutura

- [ ] 1.1 Configurar ambiente do projeto (estruturar pastas e dependências)
- [ ] 1.2 Estabelecer e testar conexão de leitura com o banco de dados ERP GTEX

## 2. Processamento de Dados (ETL)

- [x] 2.1 Desenvolver script de extração de dados brutos (`vps_etl_extractor.py` com ODBC)
- [x] 2.2 Desenvolver lógicas de cálculo para agregados: faturamento mensal, ticket médio e YoY (`vps_kpi_calculator.py`)
- [ ] 2.3 Desenvolver script para o ranking Top 10 marcas (ordenação por faturamento e volume)
- [ ] 2.4 Automatizar exportação da base final consolidada (ex: Google Sheets - 'Pagina1' ou CSV para PowerBI)

## 3. Construção do Dashboard Visual

- [ ] 3.1 Desenhar layout estrutural do painel em Dark Theme
- [ ] 3.2 Implementar os Cards Principais (Faturamento Total, Volume Total, Positivação)
- [ ] 3.3 Implementar Tabela/Gráfico de Evolução Mensal (incluindo Kg e comparações)
- [ ] 3.4 Implementar a visão do Ranking de Marcas
- [ ] 3.5 Validar os valores exibidos no dashboard contra relatórios nativos do ERP
