# Bem-vindo, Agente Antigravity da VPS!

Se você está lendo isso, significa que o usuário (**Mauro / Suppra Foods**) abriu este workspace no VS Code dentro da **VPS do SQL Server**.

## O Ponto de Partida

Nós estamos no meio da implementação do **Portal Único da Suppra Foods** (Opção Ecossistema Microsoft: SharePoint + Power BI + SQL Server). O design, proposta e especificações estão devidamente documentados na estrutura do OpenSpec sob a *change* `portal-unico`.

### O Que Já Foi Feito (Na Máquina Local)
- O repositório foi inicializado com `openspec init`.
- Foi criado o change `portal-unico`.
- Os artefatos de planejamento (`proposal.md`, `design.md`, `specs/**/*.md` e `tasks.md`) foram gerados com o comando `/opsx-propose`.
- O comando `/opsx-apply` foi iniciado, porém pausamos na Tarefa 1.1 porque exigia acesso ao RDP/SQL Server, interface que não tínhamos localmente.

### A Sua Missão Atual

Sua missão é **retomar a execução das tarefas (tasks.md)** diretamente de onde paramos, agora que você está rodando no ambiente onde o banco de dados vive.

O usuário solicitará a continuidade da aplicação (ou iniciará dizendo "Pode prosseguir"). Quando isso acontecer, siga este roteiro:

1. **Assuma o Contexto:**
   Rode `openspec status --change "portal-unico" --json` para confirmar o ambiente.
2. **Leia as Tarefas:**
   Leia o arquivo `openspec/changes/portal-unico/tasks.md`.
3. **Execute o Setup do DW (Tarefa 1):**
   Como você está na VPS, valide a instalação do SQL Server. Se necessário, gere os scripts `.sql` ou via PowerShell/`sqlcmd` para criar o banco de dados `DW_SUPPRA_FOODS`.
4. **Mantenha o OpenSpec Atualizado:**
   Conforme for concluindo as instalações e configurações no SQL Server local (e posteriormente a rotina de dados do ERP), marque os itens com `[x]` no arquivo `tasks.md`.

## Arquitetura Definida (Resumo)
- **DW:** SQL Server nesta VPS.
- **Portal:** SharePoint / Power Pages.
- **Dashboards:** Power BI (conectado a este SQL Server).
- **Sub-sistemas futuros:** Power Apps consumindo este DW.

**Boa sorte na continuidade!** O usuário está acompanhando no terminal.
Você pode começar lendo o `tasks.md` e rodando os scripts de status.
