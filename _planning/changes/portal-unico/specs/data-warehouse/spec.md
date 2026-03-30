## ADDED Requirements

### Requirement: Hospedagem Independente
O Data Warehouse ("DW") corporativo DEVE ser provisionado no Microsoft SQL Server rodando na VPS Windows já disponível (acessível via RDP preexistente), atuando como hub central de dados desvinculado de limites do Dataverse.

#### Scenario: Conexão bem-sucedida do Power BI
- **WHEN** um serviço interno (Power BI) tenta ler dados
- **THEN** a string de conexão (via Gateway ou IP direto configurado) autentica no banco SQL Server e retorna os dados tabelados do ERP.

### Requirement: Consumo Contínuo do ERP GTEX
O SQL Server DEVE possuir rotinas automatizadas ou tabelas espelhadas do fluxo de vendas e entradas originadas do sistema ERP oficial (GTEX) para viabilizar relatórios táticos/estratégicos atualizados.

#### Scenario: Atualização diária dos dados comerciais
- **WHEN** a rotina noturna (a ser definida: SSIS, Python, etc.) é executada
- **THEN** o banco de dados SQL Server reflete fielmente as novas notas e movimentos registrados no GTEX no modelo dimensional adequado.
