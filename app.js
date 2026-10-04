/**
 * THE CRYPTO MARKET CYCLE - INTERACTIVE VISUAL ENGINE
 * SVG Animation, Telemetry HUD, Web Audio Synthesizer & State Machine
 * Clean Editorial Fintech Style (Zero Emojis)
 */

(function () {
  'use strict';

  // --- STAGES DATA SCHEMA ---
  const STAGES = [
    {
      id: 1,
      name: "Accumulation Base",
      shortName: "Accumulate",
      title: "1. Smart money accumulates",
      desc: "Price is flat and boring. Whales and experienced investors quietly build massive positions over months while nobody on Crypto Twitter is talking about the coin.",
      actor: "Smart money quietly accumulating",
      price: "$12.50",
      priceChange: "+0.0%",
      portfolio: "$0",
      portfolioSub: "Sitting on the sidelines",
      pnlTag: "Unopened",
      pnlClass: "tag-green",
      sentiment: "Boredom",
      sentimentSub: "Zero timeline activity",
      sentimentClass: "tag-green",
      color: "var(--smart-money)",
      soundType: "calm"
    },
    {
      id: 2,
      name: "Trend Reversal",
      shortName: "Breakout",
      title: "2. Breakout, early longs",
      desc: "Price starts to move upward with expanding volume. Early technical traders notice the trend change, but the broader crowd is still completely oblivious.",
      actor: "Early technical traders buying",
      price: "$28.00",
      priceChange: "+124%",
      portfolio: "$0",
      portfolioSub: "Watching from afar",
      pnlTag: "Unopened",
      pnlClass: "tag-green",
      sentiment: "Curiosity",
      sentimentSub: "Chartists notice trend",
      sentimentClass: "tag-green",
      color: "var(--smart-money)",
      soundType: "pump"
    },
    {
      id: 3,
      name: "Retail Infiltration",
      shortName: "KOL Hype",
      title: "3. KOLs start shilling & You buy in",
      desc: "Influencers post target threads and hype charts ('Next 100x gem'). This is where retail FOMO strikes. You buy in with $10,000 capital at $100/token.",
      actor: "KOL promotion / Retail entry",
      price: "$100.00",
      priceChange: "+700%",
      portfolio: "$10,000",
      portfolioSub: "Entry price locked: $100.00",
      pnlTag: "0.0% PnL",
      pnlClass: "tag-orange",
      sentiment: "Excitement",
      sentimentSub: "Retail buys the narrative",
      sentimentClass: "tag-purple",
      color: "var(--kols)",
      soundType: "chime"
    },
    {
      id: 4,
      name: "Blow-Off Peak",
      shortName: "Top FOMO",
      title: "4. Retail FOMO at the top",
      desc: "Newbies pile in dreaming of 100x returns. Smart money and early callers aggressively dump their accumulated bags into this massive wave of retail liquidity.",
      actor: "Smart money dumps on retail",
      price: "$145.00",
      priceChange: "+1,060%",
      portfolio: "$14,500",
      portfolioSub: "Peak unrealized profit: +$4,500",
      pnlTag: "+45.0% PnL",
      pnlClass: "tag-gold",
      sentiment: "Euphoria",
      sentimentSub: "Peak 100x mindset",
      sentimentClass: "tag-gold",
      color: "var(--moonshot)",
      soundType: "pump"
    },
    {
      id: 5,
      name: "The First Drop",
      shortName: "Retrace",
      title: "5. \"Just a healthy retracement\"",
      desc: "Price violently rolls over. Influencers post reassurance threads insisting it's just a 'healthy correction before $500'. You believe them and refuse to take profit.",
      actor: "Distribution selloff underway",
      price: "$65.00",
      priceChange: "-55% from peak",
      portfolio: "$6,500",
      portfolioSub: "Unrealized loss: -$3,500",
      pnlTag: "-35.0% PnL",
      pnlClass: "tag-red",
      sentiment: "Denial / Cope",
      sentimentSub: "'Buy the dip' sentiment",
      sentimentClass: "tag-red",
      color: "var(--dump)",
      soundType: "dump"
    },
    {
      id: 6,
      name: "The Bull Trap",
      shortName: "Dead Cat",
      title: "6. Dead cat bounce",
      desc: "A short relief rally gives retail one final realistic chance to exit near break-even. Instead, hope surges, you celebrate too early, and you hold.",
      actor: "Relief trap rally fades",
      price: "$92.00",
      priceChange: "+41% from dip",
      portfolio: "$9,200",
      portfolioSub: "Near breakeven escape window",
      pnlTag: "-8.0% PnL",
      pnlClass: "tag-orange",
      sentiment: "False Hope",
      sentimentSub: "Trapped longs holding",
      sentimentClass: "tag-orange",
      color: "var(--dump)",
      soundType: "alert"
    },
    {
      id: 7,
      name: "The Bleed",
      shortName: "-90% Hold",
      title: "7. You hold, down 90%",
      desc: "The brutal, agonizing slow bleed. Volume evaporates, liquidity vanishes, and your token loses 90%+ of its value. You feel trapped and can't bear to look at your balance.",
      actor: "Total retail capitulation",
      price: "$10.00",
      priceChange: "-93% from ATH",
      portfolio: "$1,000",
      portfolioSub: "Severe capital destruction",
      pnlTag: "-90.0% PnL",
      pnlClass: "tag-red",
      sentiment: "Despair / Apathy",
      sentimentSub: "Portfolio deleted",
      sentimentClass: "tag-red",
      color: "var(--dump)",
      soundType: "dump"
    },
    {
      id: 8,
      name: "Floor Re-Accumulation",
      shortName: "Re-accumulate",
      title: "8. Smart money buys again",
      desc: "At the absolute depths of despair, the exact same smart money quietly begins accumulating for the next cycle while retail has checked out and given up.",
      actor: "Whales buying cycle floor",
      price: "$10.50",
      priceChange: "+5% off lows",
      portfolio: "$1,050",
      portfolioSub: "Still holding your bag",
      pnlTag: "-89.5% PnL",
      pnlClass: "tag-red",
      sentiment: "Silence",
      sentimentSub: "'Crypto is dead' narrative",
      sentimentClass: "tag-green",
      color: "var(--smart-money)",
      soundType: "calm"
    },
    {
      id: 9,
      name: "The Rebirth",
      shortName: "Recovery",
      title: "9. Fundamentals bring it back",
      desc: "A legitimate project survives the winter. Real builders ship protocol upgrades, organic fees surge, and price steadily climbs all the way back to your original entry price.",
      actor: "Organic fundamental markup",
      price: "$100.00",
      priceChange: "+900% from bottom",
      portfolio: "$10,000",
      portfolioSub: "Breakeven reached after 2 years",
      pnlTag: "0.0% Breakeven",
      pnlClass: "tag-green",
      sentiment: "Desperate Relief",
      sentimentSub: "Waiting to exit flat",
      sentimentClass: "tag-green",
      color: "var(--smart-money)",
      soundType: "pump"
    },
    {
      id: 10,
      name: "The Final Trap",
      shortName: "Break-Even Exit",
      title: "10. You sell at break-even",
      desc: "You exit flat, and then the coin pumps without you. You endured an agonizing 90% drawdown just to break even, and the moment you sell, price launches into parabolic all-time highs.",
      actor: "Retail exits / Parabolic continuation",
      price: "$320.00+",
      priceChange: "+3,100% from bottom",
      portfolio: "$10,000 SOLD FLAT",
      portfolioSub: "Missed value: $32,000+",
      pnlTag: "Sold At Breakeven",
      pnlClass: "tag-orange",
      sentiment: "Agony / Regret",
      sentimentSub: "Watching from the sidelines",
      sentimentClass: "tag-gold",
      color: "var(--moonshot)",
      soundType: "cashout"
    }
  ];

  const TOTAL_STAGES = STAGES.length;

  // --- ENGINE STATE ---
  let currentStage = 0;
  let isRunning = false;
  let isBusy = false;
  let playbackSpeed = 1;
  let runSessionId = 0;
  let soundEnabled = false;

  // Audio Context (Synthesizer)
  let audioCtx = null;

  // DOM Elements
  const playBtn = document.getElementById('playBtn');
  const playText = document.getElementById('playText');
  const stepperNav = document.getElementById('stepperNav');
  const narrativeCard = document.getElementById('narrativeCard');
  const narrativeNum = document.getElementById('narrativeNum');
  const narrativeTag = document.getElementById('narrativeTag');
  const narrativeTitle = document.getElementById('narrativeTitle');
  const narrativeDesc = document.getElementById('narrativeDesc');
  const lessonsSection = document.getElementById('lessons');
  const breakEvenGroup = document.getElementById('breakEvenLineGroup');
  const tracerGroup = document.getElementById('tracerGroup');

  // HUD Elements
  const hudStageTag = document.getElementById('hudStageTag');
  const hudPhaseName = document.getElementById('hudPhaseName');
  const hudActorAction = document.getElementById('hudActorAction');
  const hudPriceValue = document.getElementById('hudPriceValue');
  const hudPriceChange = document.getElementById('hudPriceChange');
  const hudPriceSub = document.getElementById('hudPriceSub');
  const hudPortfolioVal = document.getElementById('hudPortfolioVal');
  const hudPnlTag = document.getElementById('hudPnlTag');
  const hudPortfolioSub = document.getElementById('hudPortfolioSub');
  const hudSentimentText = document.getElementById('hudSentimentText');
  const hudSentimentTag = document.getElementById('hudSentimentTag');
  const hudSentimentSub = document.getElementById('hudSentimentSub');

  // --- AUDIO SYNTHESIS ENGINE ---
  function getAudioContext() {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        audioCtx = new AudioContextClass();
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  }

  function playTone(freq, type = 'sine', duration = 0.15, gainVal = 0.06) {
    if (!soundEnabled) return;
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, ctx.currentTime);
      gain.gain.setValueAtTime(gainVal, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch (e) {
      // Audio silent fallback
    }
  }

  function playStageSound(soundType) {
    if (!soundEnabled) return;
    try {
      const ctx = getAudioContext();
      if (!ctx) return;

      if (soundType === 'pump') {
        playTone(330, 'triangle', 0.1, 0.05);
        setTimeout(() => playTone(440, 'triangle', 0.12, 0.05), 70);
        setTimeout(() => playTone(660, 'sine', 0.2, 0.06), 140);
      } else if (soundType === 'dump') {
        playTone(380, 'sawtooth', 0.1, 0.04);
        setTimeout(() => playTone(230, 'sawtooth', 0.14, 0.04), 80);
        setTimeout(() => playTone(130, 'sine', 0.25, 0.05), 180);
      } else if (soundType === 'cashout') {
        playTone(523.25, 'sine', 0.1, 0.06);
        setTimeout(() => playTone(659.25, 'sine', 0.12, 0.06), 70);
        setTimeout(() => playTone(783.99, 'sine', 0.14, 0.06), 140);
        setTimeout(() => playTone(1046.50, 'triangle', 0.3, 0.07), 210);
      } else if (soundType === 'alert') {
        playTone(380, 'sine', 0.1, 0.04);
        setTimeout(() => playTone(490, 'sine', 0.12, 0.05), 80);
      } else {
        playTone(280, 'sine', 0.08, 0.03);
      }
    } catch (e) {
      // Ignore
    }
  }

  // --- INITIALIZE SVG PATHS ---
  function initSvgSegments() {
    for (let i = 1; i <= TOTAL_STAGES; i++) {
      const group = document.getElementById('g' + i);
      if (!group) continue;

      const segs = group.querySelectorAll('.curve-seg, .curve-glow');
      segs.forEach(seg => {
        const len = seg.getTotalLength ? seg.getTotalLength() : 200;
        seg.dataset.len = len;
        seg.style.transition = 'none';
        seg.style.strokeDasharray = len;
        seg.style.strokeDashoffset = len;
      });

      const ann = group.querySelectorAll('.annotation');
      ann.forEach(a => {
        a.style.opacity = '0';
        a.style.transform = 'translateY(4px)';
      });
    }

    if (breakEvenGroup) {
      breakEvenGroup.style.opacity = '0';
    }
    if (tracerGroup) {
      tracerGroup.setAttribute('opacity', '0');
    }
  }

  // --- GENERATE STEPPER PILLS ---
  function renderStepper() {
    stepperNav.innerHTML = '';
    STAGES.forEach((stage) => {
      const pill = document.createElement('div');
      pill.className = 'step-pill';
      pill.id = 'stepPill_' + stage.id;
      pill.style.setProperty('--pill-color', stage.color);
      pill.onclick = () => jumpToStage(stage.id);

      pill.innerHTML = `
        <span class="step-num">${String(stage.id).padStart(2, '0')}</span>
        <div class="step-bar"></div>
        <span class="step-name">${stage.shortName}</span>
      `;
      stepperNav.appendChild(pill);
    });
  }

  function updateStepperUi() {
    STAGES.forEach((stage) => {
      const pill = document.getElementById('stepPill_' + stage.id);
      if (!pill) return;
      if (stage.id < currentStage) {
        pill.className = 'step-pill completed';
      } else if (stage.id === currentStage) {
        pill.className = 'step-pill active';
      } else {
        pill.className = 'step-pill';
      }
    });
  }

  // --- ANIMATE CURVE TRACER HEAD ---
  function animateTracerHead(pathEl, durationMs) {
    if (!pathEl || !tracerGroup) return;
    const len = parseFloat(pathEl.dataset.len || pathEl.getTotalLength());
    tracerGroup.setAttribute('opacity', '1');

    const startTime = performance.now();

    function stepTracer(now) {
      const elapsed = now - startTime;
      const progress = Math.min(1, elapsed / durationMs);
      const eased = progress < 0.5 
        ? 4 * progress * progress * progress 
        : 1 - Math.pow(-2 * progress + 2, 3) / 2;

      const pt = pathEl.getPointAtLength(eased * len);
      tracerGroup.setAttribute('transform', `translate(${pt.x}, ${pt.y})`);

      if (progress < 1) {
        requestAnimationFrame(stepTracer);
      }
    }

    requestAnimationFrame(stepTracer);
  }

  // --- HUD & NARRATIVE UPDATE ---
  function updateHudAndNarrative(stageData) {
    hudStageTag.textContent = `Stage ${String(stageData.id).padStart(2, '0')}`;
    hudStageTag.className = `hud-tag ${stageData.pnlClass}`;
    hudPhaseName.textContent = stageData.name;
    hudActorAction.textContent = stageData.actor;

    hudPriceValue.textContent = stageData.price;
    hudPriceChange.textContent = stageData.priceChange;
    hudPriceChange.className = `hud-tag ${stageData.pnlClass}`;
    hudPriceSub.textContent = stageData.actor;

    hudPortfolioVal.textContent = stageData.portfolio;
    hudPnlTag.textContent = stageData.pnlTag;
    hudPnlTag.className = `hud-tag ${stageData.pnlClass}`;
    hudPortfolioSub.textContent = stageData.portfolioSub;

    hudSentimentText.textContent = stageData.sentiment;
    hudSentimentTag.textContent = `Phase ${stageData.id}`;
    hudSentimentTag.className = `hud-tag ${stageData.sentimentClass}`;
    hudSentimentSub.textContent = stageData.sentimentSub;

    // Narrative card
    narrativeNum.textContent = String(stageData.id).padStart(2, '0');
    narrativeTag.textContent = `Stage ${String(stageData.id).padStart(2, '0')} • ${stageData.name}`;
    narrativeTag.style.color = stageData.color;
    narrativeTitle.textContent = stageData.title;
    narrativeDesc.textContent = stageData.desc;
    narrativeCard.style.borderColor = stageData.color;
  }

  // --- REVEAL STAGE ANIMATION ---
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms / playbackSpeed));
  }

  async function revealStage(stageNum) {
    isBusy = true;
    const stageData = STAGES[stageNum - 1];
    updateHudAndNarrative(stageData);
    playStageSound(stageData.soundType);

    // Show Break-even line once retail enters at Stage 3
    if (stageNum >= 3 && breakEvenGroup) {
      breakEvenGroup.style.opacity = '1';
    }

    const group = document.getElementById('g' + stageNum);
    let maxDuration = 450;

    if (group) {
      const segs = group.querySelectorAll('.curve-seg, .curve-glow');
      const primarySeg = group.querySelector('.curve-seg');

      segs.forEach(s => {
        const len = parseFloat(s.dataset.len || 200);
        const ms = Math.max(360, Math.round(len * 5.0 / playbackSpeed));
        maxDuration = Math.max(maxDuration, ms);
        s.style.transition = `stroke-dashoffset ${ms}ms cubic-bezier(0.2, 0.8, 0.2, 1)`;
        s.style.strokeDashoffset = '0';
      });

      if (primarySeg) {
        animateTracerHead(primarySeg, maxDuration);
      }

      await sleep(maxDuration * 0.7);

      const anns = group.querySelectorAll('.annotation');
      anns.forEach(a => {
        a.style.opacity = '1';
        a.style.transform = 'translateY(0)';
      });
    }

    currentStage = stageNum;
    updateStepperUi();
    updateButtonStates();

    // Trigger lessons section on final stage
    if (stageNum === TOTAL_STAGES) {
      if (lessonsSection && !lessonsSection.classList.contains('revealed')) {
        lessonsSection.classList.add('revealed');
        showToast('Cycle complete. Survival rules unlocked below.');
      }
    }

    isBusy = false;
  }

  // --- INSTANT JUMP TO SPECIFIC STAGE ---
  function jumpToStage(targetNum) {
    if (isBusy) return;
    pausePlay();

    initSvgSegments();

    for (let i = 1; i <= targetNum; i++) {
      const group = document.getElementById('g' + i);
      if (group) {
        group.querySelectorAll('.curve-seg, .curve-glow').forEach(s => {
          s.style.transition = 'none';
          s.style.strokeDashoffset = '0';
        });
        group.querySelectorAll('.annotation').forEach(a => {
          a.style.opacity = '1';
          a.style.transform = 'translateY(0)';
        });
      }
    }

    if (targetNum >= 3 && breakEvenGroup) {
      breakEvenGroup.style.opacity = '1';
    }

    currentStage = targetNum;
    const stageData = STAGES[targetNum - 1];
    updateHudAndNarrative(stageData);
    updateStepperUi();
    updateButtonStates();

    // Position tracer head at tip
    const curGroup = document.getElementById('g' + targetNum);
    if (curGroup) {
      const curPath = curGroup.querySelector('.curve-seg');
      if (curPath && tracerGroup) {
        const len = curPath.getTotalLength();
        const pt = curPath.getPointAtLength(len);
        tracerGroup.setAttribute('transform', `translate(${pt.x}, ${pt.y})`);
        tracerGroup.setAttribute('opacity', '1');
      }
    }

    if (targetNum === TOTAL_STAGES && lessonsSection) {
      lessonsSection.classList.add('revealed');
    }
  }

  // --- PLAYBACK CONTROLS ---
  function updateButtonStates() {
    if (isRunning) {
      playText.textContent = 'Pause';
      playBtn.className = 'btn btn-primary';
    } else if (currentStage >= TOTAL_STAGES) {
      playText.textContent = 'Replay';
      playBtn.className = 'btn btn-primary';
    } else if (currentStage > 0) {
      playText.textContent = 'Resume';
      playBtn.className = 'btn btn-primary';
    } else {
      playText.textContent = 'Play Cycle';
      playBtn.className = 'btn btn-primary';
    }
  }

  function pausePlay() {
    isRunning = false;
    runSessionId++;
    updateButtonStates();
  }

  async function togglePlay() {
    if (isRunning) {
      pausePlay();
      return;
    }

    if (isBusy) return;

    if (currentStage >= TOTAL_STAGES) {
      resetCycle();
      await sleep(150);
    }

    isRunning = true;
    const mySessionId = ++runSessionId;
    updateButtonStates();

    while (isRunning && mySessionId === runSessionId && currentStage < TOTAL_STAGES) {
      await revealStage(currentStage + 1);
      if (!(isRunning && mySessionId === runSessionId)) break;
      await sleep(1200);
    }

    if (mySessionId === runSessionId) {
      isRunning = false;
      updateButtonStates();
    }
  }

  async function nextStage() {
    if (isBusy || currentStage >= TOTAL_STAGES) return;
    pausePlay();
    await revealStage(currentStage + 1);
  }

  function prevStage() {
    if (isBusy || currentStage <= 1) return;
    pausePlay();
    jumpToStage(currentStage - 1);
  }

  function resetCycle() {
    pausePlay();
    initSvgSegments();
    currentStage = 0;
    updateStepperUi();
    updateButtonStates();

    // Reset HUD
    const firstStage = STAGES[0];
    updateHudAndNarrative(firstStage);
    hudStageTag.textContent = "Standby";
    hudPortfolioVal.textContent = "$0";
    hudPnlTag.textContent = "Unopened";
    hudPriceValue.textContent = "$12.50";
    hudPriceChange.textContent = "+0.0%";

    narrativeNum.textContent = "00";
    narrativeTag.textContent = "Ready";
    narrativeTag.style.color = "var(--text-muted)";
    narrativeTitle.textContent = "Press Play to Watch the Cycle";
    narrativeDesc.textContent = "Each stage draws the next part of the curve and visualizes how smart money, influencers, and retail interact across time.";
    narrativeCard.style.borderColor = "var(--card-border)";
  }

  function setSpeed(speedVal, btnEl) {
    playbackSpeed = speedVal;
    document.querySelectorAll('.speed-opt').forEach(b => b.classList.remove('active'));
    if (btnEl) btnEl.classList.add('active');
    showToast(`Speed: ${speedVal}x`);
  }

  // --- SOUND TOGGLE ---
  function toggleSound() {
    soundEnabled = !soundEnabled;
    const label = document.getElementById('soundLabel');
    const soundBtn = document.getElementById('soundBtn');

    if (soundEnabled) {
      getAudioContext();
      label.textContent = 'Sound On';
      soundBtn.classList.add('active');
      showToast('Sound enabled');
      playTone(440, 'sine', 0.08, 0.04);
    } else {
      label.textContent = 'Sound Off';
      soundBtn.classList.remove('active');
      showToast('Sound muted');
    }
  }

  // --- THEME TOGGLE ---
  function toggleTheme() {
    const html = document.documentElement;
    const isDark = html.getAttribute('data-theme') !== 'light';
    const themeLabel = document.getElementById('themeLabel');

    if (isDark) {
      html.setAttribute('data-theme', 'light');
      if (themeLabel) themeLabel.textContent = 'Dark';
      localStorage.setItem('cycle_theme', 'light');
      showToast('Light mode active');
    } else {
      html.setAttribute('data-theme', 'dark');
      if (themeLabel) themeLabel.textContent = 'Light';
      localStorage.setItem('cycle_theme', 'dark');
      showToast('Dark mode active');
    }
  }

  function initTheme() {
    const saved = localStorage.getItem('cycle_theme');
    const themeLabel = document.getElementById('themeLabel');
    if (saved === 'light') {
      document.documentElement.setAttribute('data-theme', 'light');
      if (themeLabel) themeLabel.textContent = 'Dark';
    } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      if (themeLabel) themeLabel.textContent = 'Light';
    }
  }

  // --- TOAST NOTIFICATION ---
  let toastTimer = null;
  function showToast(msg) {
    const toast = document.getElementById('toast');
    const toastMsg = document.getElementById('toastMsg');
    if (!toast || !toastMsg) return;

    toastMsg.textContent = msg;
    toast.classList.add('show');

    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, 2500);
  }

  // --- X / TWITTER SHARING HELPERS ---
  function downloadCardImage() {
    const a = document.createElement('a');
    a.href = 'card-v3.png';
    a.download = 'crypto-cycle-card.png';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  function shareToTwitterWithPhoto() {
    // 1. Trigger photo download automatically
    downloadCardImage();

    // 2. Copy short post text to clipboard
    copyPostText(false);

    // 3. Open X compose intent with post text and URL
    const textarea = document.getElementById('xPostContent');
    const textToShare = textarea ? textarea.value : 
      "The crypto cycle in 5 steps:\n\n1. Smart money accumulates\n2. KOLs hype the top (you buy in)\n3. You hold down -90%\n4. You sell at break-even\n5. Coin pumps to new ATH without you\n\nHow to not be the exit liquidity:\nhttps://crypto-cycles.vercel.app";

    showToast('Photo downloaded! Attach it to your post on X.');

    setTimeout(() => {
      const url = `https://twitter.com/intent/tweet?text=${encodeURIComponent(textToShare)}`;
      window.open(url, '_blank');
    }, 400);
  }

  function shareToTwitter() {
    shareToTwitterWithPhoto();
  }

  function copyPostText(showFeedback = true) {
    const textarea = document.getElementById('xPostContent');
    if (textarea) {
      textarea.select();
      if (navigator.clipboard) {
        navigator.clipboard.writeText(textarea.value).then(() => {
          if (showFeedback) showToast('Post text copied to clipboard');
        }).catch(() => {
          document.execCommand('copy');
          if (showFeedback) showToast('Post text copied to clipboard');
        });
      } else {
        document.execCommand('copy');
        if (showFeedback) showToast('Post text copied to clipboard');
      }
    }
  }

  // --- KEYBOARD SHORTCUTS ---
  function setupKeyboard() {
    window.addEventListener('keydown', (e) => {
      if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

      if (e.code === 'Space') {
        e.preventDefault();
        togglePlay();
      } else if (e.code === 'ArrowRight') {
        e.preventDefault();
        nextStage();
      } else if (e.code === 'ArrowLeft') {
        e.preventDefault();
        prevStage();
      } else if (e.code === 'KeyR') {
        e.preventDefault();
        resetCycle();
      }
    });
  }

  // --- EXPOSE GLOBAL METHODS ---
  window.togglePlay = togglePlay;
  window.nextStage = nextStage;
  window.prevStage = prevStage;
  window.resetCycle = resetCycle;
  window.setSpeed = setSpeed;
  window.jumpToStage = jumpToStage;
  window.toggleSound = toggleSound;
  window.toggleTheme = toggleTheme;
  window.shareToTwitter = shareToTwitter;
  window.shareToTwitterWithPhoto = shareToTwitterWithPhoto;
  window.copyPostText = copyPostText;
  window.downloadCardImage = downloadCardImage;

  // --- BOOTSTRAP ---
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    renderStepper();
    initSvgSegments();
    resetCycle();
    setupKeyboard();
  });

})();
