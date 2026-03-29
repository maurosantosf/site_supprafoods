## 1. Configuração do Data Warehouse
- [ ] 1.1 Acessar a VPS via RDP (`VPS_MAURO.rdp`) e validar se a instância do SQL Server está ativa e acessível.
- [ ] 1.2 Criar o banco de dados principal (Ex: `DW_SUPPRA_FOODS`) e configurar o modelo de chaves e permissões de acesso externo (porta 1433/Gateway).
- [ ] 1.3 Mapear as tabelas cruciais do ERP (GTEX) que alimentarão o Data Warehouse.
- [ ] 1.4 Criar script/rotina diária de replicação de dados (Vendas, Estoque, Clientes) do ERP GTEX para o DW na VPS.

## 2. Configuração do Portal Único (Casca Microsoft)
- [ ] 2.1 Acessar o ambiente de administração do Microsoft 365 e validar licenciamento do SharePoint/Power Pages e Power BI. 
- [ ] 2.2 Provisionar uma nova Intranet no SharePoint ou Site no Power Pages chamada "Portal Corporativo Suppra Foods".
- [ ] 2.3 Criar a estrutura básica de navegação (Menu Principal: Intranet, Dashboards, Ferramentas).
- [ ] 2.4 Configurar os grupos de segurança no Microsoft Entra ID (Nível Estratégico, Tático e Operacional) para definir quem pode acessar cada área do portal.

## 3. Integração do Dashboard Comercial 
- [ ] 3.1 Conectar o Power BI Desktop (Dashboard Comercial em andamento) à nova base de dados DW do SQL Server, substituindo conexões de planilhas temporárias se houverem.
- [ ] 3.2 Publicar o Dashboard Comercial no Power BI Service corporativo (Workspace de Produção).
- [ ] 3.3 Obter o link/embed seguro do Power BI e inserir na página "Dashboards > Comercial" do Portal Único.
- [ ] 3.4 Validar o acesso simulando perfis (para confirmar que o RLS e o Embed funcionam sem dor para os usuários).
