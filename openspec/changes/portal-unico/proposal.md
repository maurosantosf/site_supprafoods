## Why

Precisamos de um ecossistema digital integrado (Portal Único) para centralizar informações estratégicas, ferramentas operacionais e documentos corporativos. Atualmente, os dados estão distribuídos entre o sistema ERP (GTEX), planilhas avulsas e processos manuais que geram divergências (como no controle de estoque). Construir essa fundação agora, aproveitando a assinatura existente do Microsoft 365 e a VPS disponível com SQL Server, criará uma base escalável, segura e de baixo custo para suportar o crescimento e digitalização da empresa.

## What Changes

- **Portal Central (Hub):** Criação de uma Intranet/Portal utilizando SharePoint ou Power Pages como porta de entrada conectada ao Microsoft Entra ID (SSO).
- **Data Warehouse (DW):** Implantação de um banco de dados SQL Server na VPS já existente para consolidar dados do ERP e das futuras ferramentas.
- **Integração de BI:** Embarque (embed) nativo dos Dashboards em Power BI no Portal Central, começando pelo Dashboard Comercial (Estratégico, Tático e Operacional).
- **Fundação para Aplicativos:** Preparação do ambiente para receber futuras ferramentas em Power Apps, como o Mini-CRM integrado ao WhatsApp e o Controle de Estoque padronizado.

## Capabilities

### New Capabilities
- `portal-base`: Estrutura do hub central, navegação corporativa e gestão de acessos baseada em Microsoft Entra ID.
- `data-warehouse`: Infraestrutura de dados (SQL Server) atuando como fonte única da verdade para consumo dos painéis e registro de novos apps corporativos.
- `bi-integration`: Mecanismos de conexão e exibição segura dos relatórios do Power BI dentro da casca do portal.

### Modified Capabilities
- N/A

## Impact

- **Usuários:** Toda a equipe terá um novo ponto de acesso único e autenticado (Portal) para consumo de informações, alterando a rotina de busca de dados.
- **Infraestrutura:** A VPS passará a hospedar o banco de dados principal (DW), exigindo rotinas iniciais de segurança e backup.
- **Sistemas Legados (ERP GTEX):** Passará a ser fonte de leitura recorrente via extração/API para alimentar o SQL Server, retirando a carga direta de consultas analíticas do sistema de origem.
