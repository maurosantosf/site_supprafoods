## ADDED Requirements

### Requirement: Autenticação Única Corporativa
O portal DEVE exigir autenticação utilizando as credenciais da conta Microsoft corporativa do usuário (Microsoft Entra ID), garantindo acesso seguro e perfilamento de permissões (Estratégico, Tático ou Operacional).

#### Scenario: Login de funcionário válido
- **WHEN** um funcionário acessa a URL do Portal Único
- **THEN** o sistema redireciona para a tela de login da Microsoft
- **WHEN** as credenciais foram validadas com sucesso
- **THEN** o funcionário é redirecionado de volta ao portal com a sessão ativa e permissões carregadas.

### Requirement: Navegação Centralizada (Hub)
O portal DEVE possuir um menu de navegação persistente contendo links para as três frentes principais: Dashboards, Ferramentas (Power Apps) e Intranet (Documentos).

#### Scenario: Acesso ao menu de Dashboards
- **WHEN** o usuário clica na aba "Dashboards"
- **THEN** o portal lista as categorias de painéis disponíveis para o nível hierárquico daquele usuário (ex: Comercial, Financeiro).
