## Context

A empresa possui dados e regras de negócios vitais espalhados entre o ERP principal (GTEX), controles manuais, formulários diversos e arquivos desconexos. Há uma licença ativa do Microsoft 365, bem como uma VPS com Windows Server disponível.
Para o crescimento ordenado e para evitar silos de informação, a proposta estabelecida no `proposal.md` é adotar a arquitetura de "Portal Único", consumindo um "Data Warehouse" centralizado.

## Goals / Non-Goals

**Goals:**
- Criação de uma interface unificada e amigável (o Hub) para acesso a ferramentas corporativas e dashboards.
- Utilizar a VPS existente como o nó central de armazenamento (SQL Server Database).
- Reduzir custos de desenvolvimento inicial aproveitando as ferramentas da Power Platform que já compõem o licenciamento M365 da instituição.
- Solucionar imediatamente os fluxos paralelos ao ERP, como o controle de estoque de entradas.

**Non-Goals:**
- Substituir o ERP atual (GTEX), que continuará sendo o sistema transacional oficial.
- Criar a interface (Front-end) customizada em frameworks Web pesados (React/Next) nesta primeira fase (Opção B foi descartada nesta iteração em favor de agilidade).

## Decisions

1. **Front-end Corporativo (A"Casca"): SharePoint Online / Power Pages**
   - *Rationale:* Aproveita a autenticação nativa do Microsoft Entra ID para segurança e governança de acessos imediatos. Reduz tempo de "codificação de tela" e foca na disponibilização de dados.
   - *Alternative Considered:* Desenvolvimento web customizado com React. Descartado por conta de tempo de configuração inicial e manutenção de infra de hospedagem.
2. **Back-end de Dados (DW e Aplicações): Microsoft SQL Server na VPS**
   - *Rationale:* Há uma VPS com .rdp (`VPS_MAURO.rdp`) já disponível. O SQL Server provê a robustez necessária para atuar como DW das leituras do ERP e também armazenar de forma relacional os dados oriundos de Power Apps.
   - *Alternative Considered:* Dataverse ou SharePoint Lists. Descartados devido ao volume de dados de um ERP e pelos custos adicionais/limites de armazenamento.
3. **Plataforma de Sub-aplicações: Power Apps e Power Automate**
   - *Rationale:* Os fluxos falhos que originaram a dor (ex: Entradas no Estoque) e as necessidades futuras (Mini-CRM WhatsApp) serão desenvolvidos via Power Apps Canvas, operando como "microsserviços" e consumindo o banco no SQL Server diretamente através de um gateway de dados (On-Premises Data Gateway).

## Risks / Trade-offs

- **[Dependência da VPS] ->** O SQL Server será o coração do sistema. Como é autogerenciado (IaaS), exige configuração firme de backups e rotinas de manutenção por parte da TI.
- **[Licenciamento Microsoft] ->** Para que os Power Apps possam interagir via conector Premium com o SQL Server local (via gateway), podem haver necessidades de licenças Power Apps Per User ou Per App. *Mitigação:* Avaliar arquiteturas de dados híbridas (Virtual Tables) caso o custo Premium seja impeditivo nesse estágio (embora o SQL on-premise seja recomendado para o volume esperado).
- **[Conectividade ERP -> SQL Server] ->** Necessidade de extração eficiente. *Mitigação:* Desenvolver scripts agendados (Python, SSIS ou dbt) para fazer o push incremental noturno (ou D-1) do GTEX para o DW.
