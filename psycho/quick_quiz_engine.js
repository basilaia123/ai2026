(function () {
    const cfg = window.QUIZ_CONFIG;
    if (!cfg) return;

    const state = {
        lang: 'ka',
        answers: Array(cfg.questions.length).fill(null)
    };

    const $ = (id) => document.getElementById(id);

    function t(key) {
        const v = cfg.text[state.lang][key];
        return v == null ? '' : v;
    }

    function setThemeFromStorage() {
        const isLight = localStorage.getItem('psycho-theme') === 'light';
        document.body.classList.toggle('light', isLight);
        $('themeToggle').textContent = isLight ? '🌙' : '☀️';
    }

    function toggleTheme() {
        const isLight = document.body.classList.toggle('light');
        localStorage.setItem('psycho-theme', isLight ? 'light' : 'dark');
        $('themeToggle').textContent = isLight ? '🌙' : '☀️';
    }

    function setLang(lang) {
        state.lang = lang;
        document.documentElement.lang = lang;
        $('btnKa').classList.toggle('active', lang === 'ka');
        $('btnEn').classList.toggle('active', lang === 'en');

        $('pageTitle').textContent = cfg.title[lang];
        $('subtitle').textContent = cfg.subtitle[lang];
        $('headerDesc').textContent = cfg.headerDesc[lang];
        $('disclaimer').innerHTML = cfg.disclaimer[lang];
        $('info').innerHTML = cfg.info[lang];
        $('submitBtn').textContent = t('submit');
        $('backLink').textContent = t('back');
        $('hint').textContent = remainingHint();

        renderQuestions();
        updateProgress();
        if ($('results').classList.contains('active')) renderResults();
    }

    function getAnsweredCount() {
        return state.answers.filter((x) => x !== null).length;
    }

    function remainingHint() {
        const rem = cfg.questions.length - getAnsweredCount();
        return rem === 0 ? t('allAnswered') : t('remaining').replace('{n}', String(rem));
    }

    function renderQuestions() {
        const wrap = $('questions');
        wrap.innerHTML = '';
        cfg.questions.forEach((q, i) => {
            const box = document.createElement('div');
            box.className = 'question';
            const title = document.createElement('div');
            title.className = 'q-title';
            title.textContent = (i + 1) + '. ' + q[state.lang];
            box.appendChild(title);

            cfg.options[state.lang].forEach((opt, score) => {
                const optEl = document.createElement('div');
                optEl.className = 'opt' + (state.answers[i] === score ? ' selected' : '');
                optEl.innerHTML = '<span class="score-dot">' + score + '</span><span>' + opt + '</span>';
                optEl.addEventListener('click', function () {
                    state.answers[i] = score;
                    renderQuestions();
                    updateProgress();
                });
                box.appendChild(optEl);
            });

            wrap.appendChild(box);
        });
    }

    function updateProgress() {
        const answered = getAnsweredCount();
        const total = cfg.questions.length;
        const pct = Math.round((answered / total) * 100);
        $('progressLabel').textContent = answered + ' / ' + total + ' ' + t('answered');
        $('progressPct').textContent = pct + '%';
        $('progressFill').style.width = pct + '%';
        $('hint').textContent = remainingHint();
        $('submitBtn').disabled = answered !== total;
    }

    function scoreWithReverse() {
        const maxOpt = cfg.options.en.length - 1;
        return state.answers.reduce((sum, ans, idx) => {
            const qNum = idx + 1;
            const raw = ans == null ? 0 : ans;
            if ((cfg.reverseScore || []).includes(qNum)) return sum + (maxOpt - raw);
            return sum + raw;
        }, 0);
    }

    function getBand(total) {
        for (let i = 0; i < cfg.bands.length; i++) {
            if (total <= cfg.bands[i].max) return cfg.bands[i];
        }
        return cfg.bands[cfg.bands.length - 1];
    }

    function renderResults() {
        const total = scoreWithReverse();
        const band = getBand(total);
        const lang = state.lang;

        const badgeBg = band.color === 'green' ? 'rgba(77,201,138,0.2)'
            : band.color === 'yellow' ? 'rgba(201,164,77,0.2)'
            : band.color === 'orange' ? 'rgba(201,140,77,0.2)'
            : 'rgba(201,77,109,0.2)';
        const badgeColor = band.color === 'green' ? 'var(--success)'
            : band.color === 'yellow' ? 'var(--warning)'
            : band.color === 'orange' ? '#c98c4d'
            : 'var(--danger)';

        let detailsHtml = '';
        cfg.questions.forEach((q, i) => {
            detailsHtml += '<div class="detail-row"><div>' + (i + 1) + '</div><div>' +
                q[lang] + '</div><div class="detail-score">' + state.answers[i] + '</div></div>';
        });

        const bandsHtml = cfg.bands.map((b) =>
            '<li>' + b.min + ' - ' + b.max + ': ' + b.label[lang] + '</li>'
        ).join('');

        $('results').innerHTML =
            '<div class="score-main">' +
            '<div style="font-size:36px">' + band.icon + '</div>' +
            '<div class="score" style="color:' + badgeColor + '">' + total + '</div>' +
            '<div class="score-max">/ ' + cfg.maxScore + '</div>' +
            '<div style="margin-top:8px;font-weight:700">' + band.title[lang] + '</div>' +
            '<div class="badge" style="background:' + badgeBg + ';color:' + badgeColor + '">' + band.label[lang] + '</div>' +
            '</div>' +
            '<div class="interpret"><h3>' + t('interpret') + '</h3><div class="box">' + cfg.interpret[lang] + '</div></div>' +
            '<div class="bands"><h3>' + t('bands') + '</h3><ul>' + bandsHtml + '</ul></div>' +
            '<div class="details"><h3>' + t('details') + '</h3>' + detailsHtml + '</div>' +
            '<div class="recommend"><h3>' + t('recommend') + '</h3><div class="box">' + cfg.recommend[lang] + '</div></div>' +
            '<div class="action-row"><button onclick="window.print()">' + t('print') + '</button><button id="restartBtn">' + t('restart') + '</button></div>';

        $('restartBtn').addEventListener('click', restart);
    }

    function showResults() {
        if (getAnsweredCount() !== cfg.questions.length) return;
        $('quizArea').classList.add('hidden');
        renderResults();
        $('results').classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function restart() {
        state.answers = Array(cfg.questions.length).fill(null);
        $('results').classList.remove('active');
        $('results').innerHTML = '';
        $('quizArea').classList.remove('hidden');
        renderQuestions();
        updateProgress();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    $('submitBtn').addEventListener('click', showResults);
    $('btnKa').addEventListener('click', function () { setLang('ka'); });
    $('btnEn').addEventListener('click', function () { setLang('en'); });
    $('themeToggle').addEventListener('click', toggleTheme);

    setThemeFromStorage();
    setLang('ka');
})();
