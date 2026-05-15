/**
 * SUPPRA FOODS — Landing Page Scripts
 * Vanilla JS implementation of design interactivity
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Scroll header effect
    const nav = document.querySelector('.nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            nav.classList.add('is-scrolled');
        } else {
            nav.classList.remove('is-scrolled');
        }
    }, { passive: true });

    // 2. FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const btn = item.querySelector('.q');
        btn.addEventListener('click', () => {
            const isOpen = item.classList.contains('is-open');
            // Close all
            faqItems.forEach(i => i.classList.remove('is-open'));
            // Toggle current
            if (!isOpen) item.classList.add('is-open');
        });
    });

    // 3. Process Tabs
    const steps = document.querySelectorAll('.step');
    const stages = document.querySelectorAll('.stage');
    let currentStep = 0;

    const setActiveStep = (index) => {
        steps.forEach(s => s.classList.remove('is-active'));
        stages.forEach(s => s.classList.remove('is-active'));
        steps[index].classList.add('is-active');
        stages[index].classList.add('is-active');
        currentStep = index;
    };

    steps.forEach((step, i) => {
        step.addEventListener('click', () => setActiveStep(i));
    });

    // Auto cycle process steps
    setInterval(() => {
        let next = (currentStep + 1) % steps.length;
        setActiveStep(next);
    }, 6000);

    // 4. Modal Logic
    const modalBackdrop = document.querySelector('.modal-backdrop');
    const openBtns = document.querySelectorAll('[data-open-quote]');
    const closeBtn = document.querySelector('.modal .close');
    const modalSteps = document.querySelectorAll('.modal-body-step');
    const nextBtn = document.querySelector('#modal-next');
    const prevBtn = document.querySelector('#modal-prev');
    let modalStep = 0;

    const openModal = () => {
        modalBackdrop.classList.add('is-active');
        document.body.style.overflow = 'hidden';
    };

    const closeModal = () => {
        modalBackdrop.classList.remove('is-active');
        document.body.style.overflow = '';
    };

    openBtns.forEach(btn => btn.addEventListener('click', openModal));
    closeBtn.addEventListener('click', closeModal);
    modalBackdrop.addEventListener('click', (e) => {
        if (e.target === modalBackdrop) closeModal();
    });

    const updateModalStep = (step) => {
        modalSteps.forEach(s => s.style.display = 'none');
        modalSteps[step].style.display = 'block';
        modalStep = step;
        
        // Update progress pips
        const pips = document.querySelectorAll('.pip');
        pips.forEach((p, i) => {
            p.classList.remove('is-active', 'is-done');
            if (i < step) p.classList.add('is-done');
            if (i === step) p.classList.add('is-active');
        });

        // Toggle buttons
        if (step === 0) {
            prevBtn.style.display = 'none';
        } else {
            prevBtn.style.display = 'inline-flex';
        }

        if (step === modalSteps.length - 1) {
            nextBtn.textContent = 'Enviar Solicitação';
        } else {
            nextBtn.textContent = 'Próximo';
        }
    };

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            if (modalStep < modalSteps.length - 1) {
                updateModalStep(modalStep + 1);
            } else {
                // Show success state
                document.querySelector('.modal-form-content').style.display = 'none';
                document.querySelector('.success-state').style.display = 'block';
                document.querySelector('.modal .actions').style.display = 'none';
            }
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            if (modalStep > 0) updateModalStep(modalStep - 1);
        });
    }

    // 5. Choices Selection
    const choices = document.querySelectorAll('.choice');
    choices.forEach(choice => {
        choice.addEventListener('click', () => {
            // If it's a radio-style (profile)
            if (choice.closest('.choice-grid').dataset.type === 'single') {
                choice.closest('.choice-grid').querySelectorAll('.choice').forEach(c => c.classList.remove('is-selected'));
            }
            choice.classList.toggle('is-selected');
        });
    });

    // 6. Dynamic Temp Card Drift
    const tempVal = document.querySelector('.temp-card .val-num');
    if (tempVal) {
        setInterval(() => {
            let base = -19.8;
            let drift = (Math.random() - 0.5) * 0.4;
            tempVal.textContent = (base + drift).toFixed(1).replace('-', '−');
        }, 3000);
    }
});
