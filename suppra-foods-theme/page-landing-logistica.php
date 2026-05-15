<?php
/**
 * Template Name: Landing Page Logística
 * Description: Landing page focada em conversão para logística de cadeia fria.
 */

defined('ABSPATH') || exit;

// Helper para Icons
function suppra_icon($name, $size = 22) {
    $icons = [
        'snow' => '<path d="M12 2v20M4 6l16 12M4 18 20 6M2 12h20" /><path d="m8 4 4 2 4-2M8 20l4-2 4 2M4 8l-2 4 2 4M20 8l2 4-2 4" />',
        'truck' => '<path d="M3 7h11v9H3z" /><path d="M14 10h4l3 3v3h-7" /><circle cx="7.5" cy="17.5" r="1.8" /><circle cx="17" cy="17.5" r="1.8" />',
        'box' => '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5v-9Z" /><path d="M3 7.5 12 12l9-4.5M12 12v9" />',
        'warehouse' => '<path d="M3 21V9l9-5 9 5v12" /><path d="M7 21v-7h10v7M7 14h10" />',
        'check' => '<path d="m5 12 5 5L20 7" />',
        'phone' => '<path d="M5 4h4l2 5-2 1a11 11 0 0 0 5 5l1-2 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z" />',
        'mail' => '<path d="M3 6h18v12H3z" /><path d="m3 7 9 7 9-7" />',
        'arrow' => '<path d="M5 12h14M13 6l6 6-6 6" />',
        'plus' => '<path d="M12 5v14M5 12h14" />',
        'clock' => '<circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" />',
        'thermometer' => '<path d="M14 14V5a2 2 0 1 0-4 0v9a4 4 0 1 0 4 0Z" />',
        'wa' => '<path d="M19.1 4.9A10 10 0 0 0 4.5 17.4L3 22l4.7-1.5A10 10 0 0 0 22 12a9.9 9.9 0 0 0-2.9-7.1Zm-7 15.3a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-2.8.9.9-2.7-.2-.3a8.2 8.2 0 1 1 14.4-5.4 8.2 8.2 0 0 1-7.8 8.8Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.5.1-.2.2-.6.8-.7 1-.1.1-.3.1-.5 0a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3a.4.4 0 0 0 0-.4l-.7-1.6c-.2-.4-.4-.4-.5-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.1 5.1 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c.6.2 1.1.4 1.5.5.6.2 1.2.2 1.7.1.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2 0-.1-.2-.2-.4-.3Z" />',
        'ig' => '<rect x="3" y="3" width="18" height="18" rx="5" /><circle cx="12" cy="12" r="4" /><circle cx="17.5" cy="6.5" r=".8" fill="currentColor" />',
        'in' => '<path d="M4.5 3.5a2 2 0 1 1 0 4 2 2 0 0 1 0-4ZM3 9h3v12H3V9Zm6 0h3v1.7c.6-1 1.7-2 3.6-2 3.8 0 4.4 2.5 4.4 5.7V21h-3v-5.6c0-1.4 0-3.1-1.9-3.1s-2.1 1.5-2.1 3v5.7H9V9Z" />',
        'pin' => '<path d="M12 22s7-7.5 7-13a7 7 0 0 0-14 0c0 5.5 7 13 7 13Z" /><circle cx="12" cy="9" r="2.5" />',
    ];
    $svg = $icons[$name] ?? '';
    $fill = ($name === 'wa' || $name === 'in' || $name === 'ig') ? 'currentColor' : 'none';
    $stroke = ($name === 'wa' || $name === 'in') ? 'none' : 'currentColor';
    
    return sprintf(
        '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="%s" stroke="%s" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</svg>',
        $size, $size, $fill, $stroke, $svg
    );
}

// Enqueue Assets para esta página específica
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style('suppra-landing-css', get_template_directory_uri() . '/assets/css/landing-page.css', [], '1.0.0');
    wp_enqueue_script('suppra-landing-js', get_template_directory_uri() . '/assets/js/landing-page.js', [], '1.0.0', true);
});

get_header('landing'); // Criaremos um header simplificado se necessário, ou usamos o padrão
?>

<div class="landing-page-body">

    <!-- Topbar -->
    <div class="topbar">
        <div class="container">
            <div class="row">
                <div class="left">
                    <span><span class="dot"></span> Operação contínua · Grande Goiânia</span>
                    <span style="opacity:0.6">·</span>
                    <span><?php echo suppra_icon('pin', 14); ?> Goiânia e região metropolitana</span>
                </div>
                <div class="right">
                    <span>Fale conosco</span>
                    <div class="social">
                        <a href="#"><?php echo suppra_icon('ig', 14); ?></a>
                        <a href="#"><?php echo suppra_icon('in', 14); ?></a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Nav -->
    <header class="nav">
        <div class="container">
            <div class="row">
                <a href="#home" class="logo">
                    <span class="mark"><?php echo suppra_icon('snow', 22); ?></span>
                    <span class="wm"><span class="slash">/</span><span class="a">suppra</span><span class="b">foods</span></span>
                </a>
                <nav class="nav-links">
                    <a href="#home" class="is-active">Início</a>
                    <a href="#sobre">Sobre</a>
                    <a href="#infra">Infraestrutura</a>
                    <a href="#processo">Como trabalhamos</a>
                    <a href="#contato">Contato</a>
                </nav>
                <div class="nav-phone">
                    <span class="ic"><?php echo suppra_icon('phone', 18); ?></span>
                    <div>
                        <div class="lab">Comercial</div>
                        <div class="num">(62) 3638-3994</div>
                    </div>
                </div>
                <button class="btn btn-dark" data-open-quote>
                    Falar com a Suppra
                    <span class="arr"><?php echo suppra_icon('arrow', 14); ?></span>
                </button>
            </div>
        </div>
    </header>

    <main>
        <!-- Hero -->
        <section id="home" class="hero">
            <div class="container">
                <div class="row">
                    <div>
                        <span class="badge">
                            <span class="ic"><?php echo suppra_icon('snow', 14); ?></span>
                            Operação Logística em Cadeia Fria
                        </span>
                        <h1>Resfriados e congelados <br> na Grande Goiânia. <br> <span class="accent">Sem improviso.</span></h1>
                        <p class="lede">Há 5 anos atuamos como operador logístico de resfriados e congelados na Grande Goiânia. Câmaras próprias, controle térmico 100% da operação e responsabilidade da Suppra do recebimento à entrega final.</p>
                        <div class="cta-row">
                            <button class="btn btn-primary" data-open-quote>
                                Falar com a Suppra
                                <span class="arr"><?php echo suppra_icon('arrow', 14); ?></span>
                            </button>
                            <a href="#processo" class="btn" style="color: #fff; border: 1.5px solid rgba(255,255,255,0.3)">Conhecer a operação</a>
                        </div>
                        <div class="meta">
                            <div class="item"><div class="k">5 anos</div><div class="v">de operação real</div></div>
                            <div class="item"><div class="k">−20°C</div><div class="v">temp. máxima</div></div>
                            <div class="item"><div class="k">2 câmaras</div><div class="v">próprias</div></div>
                        </div>
                    </div>
                    <div class="hero-visual">
                        <div class="warehouse">
                            <div class="photo photo-hero-warehouse"></div>
                        </div>
                        <div class="truck">
                            <div class="photo photo-hero-truck"></div>
                        </div>
                        <div class="temp-card">
                            <div class="lab">Câmara 02 · Congelados</div>
                            <div class="val"><span class="val-num">−19.8</span><span>°C</span></div>
                            <div style="height:6px; border-radius:999px; background:linear-gradient(90deg, #8FB7FF, var(--blue-500)); margin-top:12px;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Stats Band -->
        <section class="stats">
            <div class="container">
                <div class="row">
                    <div class="item">
                        <span class="ic"><?php echo suppra_icon('clock', 20); ?></span>
                        <div class="k">5<span class="u"> anos</span></div>
                        <div class="v">de operação real em cadeia fria</div>
                    </div>
                    <div class="item">
                        <span class="ic"><?php echo suppra_icon('snow', 20); ?></span>
                        <div class="k"><span class="p">−</span>20<span class="u">°C</span></div>
                        <div class="v">temperatura máxima de congelamento</div>
                    </div>
                    <div class="item">
                        <span class="ic"><?php echo suppra_icon('warehouse', 20); ?></span>
                        <div class="k">2</div>
                        <div class="v">câmaras frigoríficas próprias</div>
                    </div>
                    <div class="item">
                        <span class="ic"><?php echo suppra_icon('pin', 20); ?></span>
                        <div class="k">6<span class="u"> cidades</span></div>
                        <div class="v">atendidas na Grande Goiânia</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About -->
        <section id="sobre" class="about">
            <div class="container">
                <div class="row">
                    <div>
                        <span class="eyebrow">Quem somos</span>
                        <h2 style="margin-top:14px">Foi na rotina — e não na teoria — que vivemos as dores da cadeia fria.</h2>
                        <p style="margin-top:18px">A Suppra Foods nasceu em 2021 como distribuidora de alimentos refrigerados na Grande Goiânia. Identificamos um gap real no mercado regional e transformamos isso em serviço.</p>
                        <ul class="checks">
                            <li><span class="ic"><?php echo suppra_icon('check', 16); ?></span> 5 anos de operação real</li>
                            <li><span class="ic"><?php echo suppra_icon('check', 16); ?></span> 2 câmaras próprias</li>
                            <li><span class="ic"><?php echo suppra_icon('check', 16); ?></span> Até −20°C</li>
                            <li><span class="ic"><?php echo suppra_icon('check', 16); ?></span> Frota refrigerada</li>
                        </ul>
                        <button class="btn btn-dark" data-open-quote>Solicitar contato <span class="arr"><?php echo suppra_icon('arrow', 14); ?></span></button>
                    </div>
                    <div class="about-collage">
                        <div class="main"></div>
                        <div class="sub"></div>
                        <div class="badge">
                            <div class="k">SINCE</div>
                            <div class="v">2021</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Infra -->
        <section id="infra" class="infra">
            <div class="container">
                <div style="text-align:center; margin-bottom:48px;">
                    <span class="eyebrow">Infraestrutura</span>
                    <h2>Duas câmaras. Uma só obsessão.</h2>
                </div>
                <div class="infra-grid">
                    <article class="infra-card">
                        <div class="img">
                            <div class="photo photo-hero-warehouse"></div>
                            <span class="floater"><?php echo suppra_icon('snow', 20); ?></span>
                        </div>
                        <div class="body">
                            <div style="display:flex; justify-content:space-between; align-items:baseline;">
                                <div class="tag">Câmara 01</div>
                                <div class="area" style="font-size:32px; font-weight:700;">261 m²</div>
                            </div>
                            <div style="color:var(--ink-500); font-size:12px; margin-bottom:18px;">19,2 × 13,6 × 3,07 m</div>
                            <ul style="list-style:none; padding:0; display:grid; gap:10px;">
                                <li style="display:flex; gap:10px; font-size:14px;"><?php echo suppra_icon('check', 14); ?> 4 evaporadoras + 4 condensadoras</li>
                                <li style="display:flex; gap:10px; font-size:14px;"><?php echo suppra_icon('check', 14); ?> Setorização por faixa térmica</li>
                            </ul>
                        </div>
                    </article>
                    <article class="infra-card">
                        <div class="img">
                            <div class="photo photo-process-dispatch"></div>
                            <span class="floater"><?php echo suppra_icon('snow', 20); ?></span>
                        </div>
                        <div class="body">
                            <div style="display:flex; justify-content:space-between; align-items:baseline;">
                                <div class="tag">Câmara 02</div>
                                <div class="area" style="font-size:32px; font-weight:700;">458 m²</div>
                            </div>
                            <div style="color:var(--ink-500); font-size:12px; margin-bottom:18px;">22,9 × 20,0 × 3,18 m</div>
                            <ul style="list-style:none; padding:0; display:grid; gap:10px;">
                                <li style="display:flex; gap:10px; font-size:14px;"><?php echo suppra_icon('check', 14); ?> 2 compressores + 6 evaporadoras</li>
                                <li style="display:flex; gap:10px; font-size:14px;"><?php echo suppra_icon('check', 14); ?> Antecâmara e cortina de ar</li>
                            </ul>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- Process -->
        <section id="processo" class="process">
            <div class="container">
                <div style="text-align:center; margin-bottom:56px;">
                    <span class="eyebrow">Como trabalhamos</span>
                    <h2>Três etapas. Uma cadeia controlada.</h2>
                </div>
                <div class="row">
                    <div class="steps">
                        <div class="step is-active" data-step="0">
                            <div class="num">1</div>
                            <div><h3>Armazenagem</h3><p>Recebimento e estocagem em câmara fria setorizada.</p></div>
                        </div>
                        <div class="step" data-step="1">
                            <div class="num">2</div>
                            <div><h3>Expedição</h3><p>Separação de pedidos com controle de temperatura.</p></div>
                        </div>
                        <div class="step" data-step="2">
                            <div class="num">3</div>
                            <div><h3>Entrega</h3><p>Distribuição com baú refrigerado de ponta a ponta.</p></div>
                        </div>
                    </div>
                    <div class="vis">
                        <div class="stage is-active"><div class="photo photo-hero-warehouse"></div></div>
                        <div class="stage"><div class="photo photo-process-dispatch"></div></div>
                        <div class="stage"><div class="photo photo-hero-truck"></div></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ -->
        <section class="faq">
            <div class="container">
                <div class="row">
                    <div>
                        <span class="eyebrow">Perguntas frequentes</span>
                        <h2 style="margin-top:14px">O que clientes costumam perguntar.</h2>
                        <button class="btn btn-dark" style="margin-top:24px" data-open-quote>Falar com especialista <span class="arr"><?php echo suppra_icon('arrow', 14); ?></span></button>
                    </div>
                    <div class="faq-list">
                        <div class="faq-item is-open">
                            <button class="q"><span>Qual a faixa de temperatura das câmaras?</span> <?php echo suppra_icon('plus', 16); ?></button>
                            <div class="a">Operamos com capacidade de congelamento de até −20°C e câmaras setorizadas por faixa térmica.</div>
                        </div>
                        <div class="faq-item">
                            <button class="q"><span>Em quais cidades vocês entregam?</span> <?php echo suppra_icon('plus', 16); ?></button>
                            <div class="a">Atendemos Goiânia e mais 5 cidades da região metropolitana: Aparecida, Trindade, Senador Canedo, Goianira e Abadia.</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- CTA -->
        <section id="contato" class="cta">
            <div class="container">
                <div class="row">
                    <div>
                        <span class="eyebrow" style="color:#8FB7FF">Vamos conversar</span>
                        <h2 style="margin-top:14px">A cadeia fria que sua operação merece.</h2>
                        <div class="contact-card" style="margin-top:28px; background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.18); border-radius:12px; padding:18px 22px;">
                            <div style="font-weight:700;">Mauro Santos</div>
                            <div style="font-size:12px; color:#8FB7FF; text-transform:uppercase;">Suppra Foods · Operação Logística</div>
                        </div>
                    </div>
                    <div class="cta-actions">
                        <button class="btn btn-light" data-open-quote>Falar com a Suppra <span class="arr" style="background:var(--frost-100)"><?php echo suppra_icon('arrow', 14); ?></span></button>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div>
                    <a href="#home" class="logo">
                        <span class="mark" style="background:rgba(255,255,255,0.1)"><?php echo suppra_icon('snow', 22); ?></span>
                        <span class="wm"><span class="slash" style="color:#8FB7FF">/</span><span class="a" style="color:#fff">suppra</span><span class="b" style="color:#8FB7FF">foods</span></span>
                    </a>
                    <p style="margin-top:18px; font-size:14px;">Operação logística em cadeia fria na Grande Goiânia desde 2021.</p>
                </div>
                <div>
                    <h4>Operação</h4>
                    <ul style="list-style:none; padding:0; display:grid; gap:10px;">
                        <li><a href="#">Armazenagem</a></li>
                        <li><a href="#">Expedição</a></li>
                        <li><a href="#">Entrega</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Contato</h4>
                    <div style="font-size:14px;">
                        <div style="font-weight:600; color:#fff;">(62) 3638-3994</div>
                        <div>mauro.santos@supprafoods.com.br</div>
                    </div>
                </div>
            </div>
            <div style="margin-top:56px; border-top:1px solid rgba(255,255,255,0.1); padding-top:22px; font-size:13px; display:flex; justify-content:space-between;">
                <span>© 2026 Suppra Foods · Logística</span>
                <span>/ s u p p r a f o o d s</span>
            </div>
        </div>
    </footer>

    <!-- WhatsApp Fab -->
    <a href="https://wa.me/556236383994" target="_blank" class="wa-fab" style="position:fixed; right:22px; bottom:22px; background:#25D366; width:58px; height:58px; border-radius:999px; display:flex; align-items:center; justify-content:center; color:#fff; box-shadow:0 14px 34px -10px rgba(37,211,102,0.55); text-decoration:none;">
        <?php echo suppra_icon('wa', 26); ?>
    </a>

    <!-- Modal Backdrop -->
    <div class="modal-backdrop">
        <div class="modal">
            <div class="body">
                <div class="modal-form-content">
                    <div style="display:flex; justify-content:space-between; align-items:start;">
                        <div>
                            <span class="eyebrow">Falar com a Suppra</span>
                            <h2 style="margin-top:6px">Conte sobre sua operação</h2>
                        </div>
                        <button class="close" style="width:40px; height:40px; border-radius:999px; background:var(--frost-100); display:flex; align-items:center; justify-content:center;"><?php echo suppra_icon('plus', 18); ?></button>
                    </div>
                    
                    <div class="progress" style="display:flex; gap:8px; margin-top:22px;">
                        <div class="pip is-active" style="flex:1; height:5px; border-radius:999px; background:var(--line);"></div>
                        <div class="pip" style="flex:1; height:5px; border-radius:999px; background:var(--line);"></div>
                        <div class="pip" style="flex:1; height:5px; border-radius:999px; background:var(--line);"></div>
                    </div>

                    <div class="modal-body-step" style="margin-top:22px;">
                        <h3 style="font-size:17px; margin-bottom:16px;">Qual o perfil da sua empresa?</h3>
                        <div class="choice-grid" data-type="single">
                            <div class="choice is-selected"><span class="nm">Indústria de Alimentos</span></div>
                            <div class="choice"><span class="nm">Distribuidor / Atacadista</span></div>
                            <div class="choice"><span class="nm">Rede Varejista</span></div>
                            <div class="choice"><span class="nm">Outro segmento</span></div>
                        </div>
                    </div>

                    <div class="modal-body-step" style="margin-top:22px; display:none;">
                        <h3 style="font-size:17px; margin-bottom:16px;">Que tipo de operação precisa?</h3>
                        <div class="choice-grid" data-type="multi">
                            <div class="choice"><span class="nm">Armazenagem Congelada</span></div>
                            <div class="choice"><span class="nm">Entrega Refrigerada</span></div>
                        </div>
                    </div>

                    <div class="modal-body-step" style="margin-top:22px; display:none;">
                        <h3 style="font-size:17px; margin-bottom:16px;">Dados de contato</h3>
                        <div style="display:grid; gap:14px;">
                            <input type="text" placeholder="Nome completo" style="width:100%; padding:14px; border:1px solid var(--line); border-radius:10px;">
                            <input type="email" placeholder="E-mail corporativo" style="width:100%; padding:14px; border:1px solid var(--line); border-radius:10px;">
                        </div>
                    </div>

                    <div class="actions" style="margin-top:30px; display:flex; justify-content:space-between;">
                        <button id="modal-prev" class="btn btn-ghost" style="display:none;">Voltar</button>
                        <button id="modal-next" class="btn btn-primary">Próximo <span class="arr"><?php echo suppra_icon('arrow', 14); ?></span></button>
                    </div>
                </div>

                <div class="success-state" style="display:none; text-align:center; padding:40px 0;">
                    <div style="width:80px; height:80px; background:var(--blue-500); border-radius:999px; display:flex; align-items:center; justify-content:center; color:#fff; margin:0 auto 20px;">
                        <?php echo suppra_icon('check', 36); ?>
                    </div>
                    <h2>Solicitação recebida!</h2>
                    <p>Mauro Santos retornará em breve.</p>
                    <button class="btn btn-dark close" style="margin-top:24px;">Fechar</button>
                </div>
            </div>
        </div>
    </div>

</div>

<?php wp_footer(); ?>
</body>
</html>
