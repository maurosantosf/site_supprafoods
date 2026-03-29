## Context

A Suppra Foods possui um domínio e uma hospedagem na Hostinger, onde já existe um início de trabalho em WordPress. O site atual não reflete o posicionamento multissetorial da empresa (Logística, Indústria e Distribuição) e precisa de um recomeço (*clean slate*) para garantir alta performance, segurança e uma arquitetura de navegação segmentada focada no público B2B.

## Goals / Non-Goals

**Goals:**
- Criar um site WordPress do zero, super rápido e seguro.
- Estruturar uma "Home HUB" que distribua o tráfego para os três pilares estratégicos.
- Apresentar a nova marca de queijos Beneva (Indústria) e a infraestrutura logística.
- Gerar leads qualificados B2B através de formulários eficientes.

**Non-Goals:**
- **Não** reaproveitaremos nada da instalação atual do WordPress. O ambiente será completamente limpo antes de iniciar.
- **Não** será um e-commerce (vendas diretas online com checkout e pagamento). É um site institucional/catálogo e gerador de leads (B2B).

## Decisions

- **Plataforma:** WordPress (Self-hosted na Hostinger).
  - *Rationale*: Permite que a equipe de marketing/comercial da Suppra atualize facilmente banners e catálogos no futuro, garantindo agilidade.
- **Abordagem de Build:** Tema Base Leve (ex: Hello Elementor ou Astra) + Page Builder (Elementor/Bricks).
  - *Rationale*: Evita temas prontos e pesados (bloatware). Permite criar as interfaces personalizadas sugeridas (referências: Tranzilli, S.A. Alimentos, Farias) mantendo a perfomance alta.
- **Limpeza do Ambiente (Clean Slate):** A hospedagem atual na Hostinger sofrerá um "reset" do banco de dados e arquivos existentes.
  - *Rationale*: Evitar lentidão, conflitos de plugins e falhas de segurança deixadas por tentativas anteriores de criação de site.
- **Captação de Leads:** WPForms ou Fluent Forms.
  - *Rationale*: Permite segmentar os formulários e rotear os contatos (Indústria / Revenda) por e-mail de forma simples e direta para o time comercial.

## Risks / Trade-offs

- **[Risco] Perda de e-mails corporativos (Hostinger):** Se o reset do WordPress na Hostinger não for feito com cuidado (ex: apagando a zona DNS ou a conta de painel inteira em vez de apenas focar no diretório `public_html`), as caixas de e-mail ativas podem cair.
  - *Mitigation*: O processo de "clean slate" será restrito apenas à desinstalação via Script do WordPress ou limpeza do diretório `public_html`/banco de dados, sem tocar em serviços de e-mail (Titan/Hostinger Email) ou DNS.
- **[Risco] Performance de Page Builders:** Construtores visuais tendem a carregar muito CSS/JS desnecessário.
  - *Mitigation*: Uso restrito de plugins (apenas o essencial) e implementação futura de cache pesado (WP Rocket / Litespeed).
