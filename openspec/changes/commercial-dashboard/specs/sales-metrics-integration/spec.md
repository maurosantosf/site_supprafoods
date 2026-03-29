## ADDED Requirements

### Requirement: Integração de Dados do ERP GTEX
O sistema MUST extrair dados consistentes e atualizados do banco de dados do ERP GTEX para alimentar o dashboard comercial.

#### Scenario: Extração de dados de vendas
- **WHEN** o script de integração (ETL) for executado
- **THEN** o sistema extrairá as informações granulares de vendas, notas fiscais e cadastro de clientes operantes.

### Requirement: Cálculo de Indicadores Comerciais
O processo de integração MUST processar e calcular faturamento, volume (Kg), ticket médio mensais e taxa de positivação baseado nos dados extraídos.

#### Scenario: Processamento de dados agregados
- **WHEN** a extração do banco de dados for concluída
- **THEN** os scripts agregarão os dados gerando totais de faturamento e volume por marca/mês, além de comparar com o mesmo período do ano anterior.

### Requirement: Carga de Dados no Dashboard
O sistema MUST carregar os dados processados na estrutura que alimenta o painel visual (ex: planilha 'Pagina1' no Sheets ou dataset no Power BI).

#### Scenario: Atualização da origem de dados do dashboard
- **WHEN** os indicadores forem todos calculados
- **THEN** o sistema atualizará a base de leitura final do painel para refletir os números mais recentes.
