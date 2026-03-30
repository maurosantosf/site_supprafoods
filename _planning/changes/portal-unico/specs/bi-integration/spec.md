## ADDED Requirements

### Requirement: Embarque (Embed) de Relatórios Seguros
O portal DEVE suportar a renderização embarcada (embedded) dos relatórios construídos no Power BI (iniciando pelo Dashboard Comercial). As camadas de segurança do Tenant M365 DEVEM ser mantidas para garantir que o usuário veja apenas o que o Entra ID permite.

#### Scenario: Visualização do Dashboard Comercial
- **WHEN** um usuário da diretoria acessa a aba "Comercial" no Portal
- **THEN** o relatório do Power BI é renderizado on-page, lendo os dados diretamente do SQL Server DW.
- **AND** a performance de renderização não exige que o usuário abra o aplicativo do Power BI Service separadamente.
