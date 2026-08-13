/**
 * CareerAI — Interactive AI Mock Interview Suite
 * Full wizard, speech-to-text recording, dynamic timer, real-time evaluation & scorecard.
 * Includes seamless client-side AI Demo Engine for 100% GitHub Pages compatibility!
 */

// Comprehensive Client-side Question Bank for GitHub Pages & Offline Use
const CLIENT_QUESTION_BANK = {
  "Software Developer": {
    "Beginner": [
      "Explain the four core principles of Object-Oriented Programming (OOP) with real-world analogies.",
      "What is the difference between an Array and a Linked List? When would you choose one over the other?",
      "How does a Hash Table achieve average O(1) time complexity for search operations?",
      "Explain the difference between SQL (relational) and NoSQL databases.",
      "What is a RESTful API? Explain the significance of standard HTTP methods like GET, POST, PUT, and DELETE."
    ],
    "Intermediate": [
      "Explain how Python manages memory internally. What is reference counting and garbage collection?",
      "Design a scalable REST API endpoint for user authentication with JWT and security best practices.",
      "Compare SQL indexing methods. What happens under the hood when a B-Tree index is created?",
      "Explain how you would design a rate limiter to prevent API abuse in a web application.",
      "What are microservices compared to monolithic architectures? What are key trade-offs?"
    ],
    "Advanced": [
      "Architect a high-throughput, distributed event-driven notification system handling 100,000 req/min.",
      "Explain the CAP theorem and trade-offs between CP and AP consistency models.",
      "How would you optimize a slow database query operating on a table with 50 million rows?",
      "Discuss memory leak diagnostics and profiling tools in long-running backend services.",
      "How do you implement distributed locking using Redis or ZooKeeper to prevent race conditions?"
    ]
  },
  "Python Developer": {
    "Beginner": [
      "What are the main differences between Python lists, tuples, dictionaries, and sets?",
      "How does Python's `is` operator differ from the `==` operator?",
      "Explain Python list comprehensions and dictionary comprehensions with syntax examples.",
      "What is the difference between `break`, `continue`, and `pass` in Python loops?",
      "How do you handle exceptions in Python using `try`, `except`, `else`, and `finally` blocks?"
    ],
    "Intermediate": [
      "Explain Python decorators: how they work using closures, and provide an execution timer example.",
      "What are Python generators and the `yield` keyword? How do they provide memory efficiency?",
      "Explain the Global Interpreter Lock (GIL) in CPython and how it affects CPU vs I/O concurrency.",
      "How do you structure a scalable Flask application using Blueprints and Config objects?",
      "Explain Python magic/dunder methods (e.g., `__init__`, `__str__`, `__enter__`, `__exit__`)."
    ],
    "Advanced": [
      "Deep dive into CPython object memory representation, small integer caching, and string interning.",
      "Architect a distributed Python worker pool using Celery, Redis, and Asyncio for batch processing.",
      "Explain the Python descriptor protocol (`__get__`, `__set__`) and how properties leverage it.",
      "How would you profile CPU and memory bottlenecks in a production Flask API using py-spy and memory_profiler?",
      "Compare Cython, PyPy, and C-extensions for accelerating numerical compute routines."
    ]
  },
  "Web Developer": {
    "Beginner": [
      "Explain the CSS Box Model (Content, Padding, Border, Margin) and `box-sizing: border-box`.",
      "What is the difference between `let`, `const`, and `var` in modern JavaScript?",
      "Explain how CSS Flexbox works: difference between `justify-content` and `align-items`.",
      "What are semantic HTML tags and why are they critical for accessibility (a11y) and SEO?",
      "How does the browser DOM work, and how does JavaScript modify DOM elements?"
    ],
    "Intermediate": [
      "Explain the JavaScript Event Loop, Call Stack, Microtask Queue (Promises), and Macrotask Queue.",
      "How do CSS Grid and Flexbox differ in mental model and use cases?",
      "Explain Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF) defenses.",
      "How do you optimize Core Web Vitals (Largest Contentful Paint, Interaction to Next Paint)?",
      "Explain how WebSockets enable full-duplex communication compared to HTTP polling."
    ],
    "Advanced": [
      "Explain the browser Critical Rendering Path: DOM, CSSOM, Render Tree, Layout, Paint, and Composite.",
      "Architect a Progressive Web App (PWA) with Service Workers for offline-first caching and sync.",
      "How do you implement micro-frontends with module federation and manage performance trade-offs?",
      "Explain JavaScript memory leaks (detached DOM nodes, forgotten event listeners) and how to debug them.",
      "How do you design a high-performance virtualized list rendering 100,000 rows with 60fps scrolling?"
    ]
  },
  "Data Analyst": {
    "Beginner": [
      "Explain the difference between `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL OUTER JOIN`.",
      "What is the difference between `WHERE` and `HAVING` clauses in SQL queries?",
      "How do you handle missing or null values in a dataset using Python Pandas (`fillna`, `dropna`)?",
      "Explain Mean, Median, and Mode. In what distribution is Median preferred over Mean?",
      "What is the difference between qualitative (categorical) and quantitative (numerical) data?"
    ],
    "Intermediate": [
      "Explain SQL Window Functions (`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LEAD()`, `LAG()`).",
      "How do you detect and handle outliers in skewed distributions (IQR vs Z-score)?",
      "Explain how to perform exploratory data analysis (EDA) using Pandas and visualization tools.",
      "What is database normalization (1NF, 2NF, 3NF)? When is denormalization preferred?",
      "Explain hypothesis testing, p-values, Type I/II errors, and statistical significance."
    ],
    "Advanced": [
      "Architect a Star Schema vs Snowflake Schema data warehouse with Fact and Dimension tables.",
      "Explain query optimization in distributed SQL engines: partitioning, clustering, and execution plans.",
      "How do you implement statistical anomaly detection and forecasting on IoT time-series telemetry?",
      "Discuss data lineage, Change Data Capture (CDC), and Slowly Changing Dimensions (SCD Type 2).",
      "Explain Monte Carlo simulations and multivariate regression modeling for predictive analytics."
    ]
  },
  "AI/ML Beginner": {
    "Beginner": [
      "What is the difference between Supervised, Unsupervised, and Reinforcement Learning?",
      "Explain Overfitting and Underfitting in Machine Learning. How do you prevent them?",
      "What are the differences between Classification and Regression tasks? Give examples.",
      "Explain how facial detection works in OpenCV using Haar Cascades or deep learning models.",
      "What is a Confusion Matrix, and what do True Positive, True Negative, False Positive, False Negative mean?"
    ],
    "Intermediate": [
      "Explain Precision, Recall, F1-Score, and ROC-AUC. When is Recall prioritized over Precision?",
      "How do Random Forests and Gradient Boosting (XGBoost/LightGBM) algorithms work and differ?",
      "Explain how Convolutional Neural Networks (CNNs) process images: kernels, ReLU, pooling.",
      "How do you perform real-time anti-spoofing and liveness detection in computer vision face recognition?",
      "Explain the Bias-Variance Tradeoff and regularization techniques (L1 Lasso, L2 Ridge, Dropout)."
    ],
    "Advanced": [
      "Deep dive into Transformers: Explain Self-Attention, Multi-Head Attention, and Positional Encodings.",
      "Architect an edge AI pipeline deploying quantized TinyML models on ESP32 microcontrollers.",
      "Explain generative models: VAEs, Diffusion Models, and LLMs latent representations.",
      "How do you mitigate hallucination in LLM fine-tuning and Retrieval-Augmented Generation (RAG)?",
      "Discuss distributed model training: Data Parallelism, Tensor Parallelism, and Pipeline Parallelism."
    ]
  },
  "ECE Engineer": {
    "Beginner": [
      "Explain the difference between a Microprocessor and a Microcontroller (e.g. ESP32).",
      "What is Pulse Width Modulation (PWM) and how is it used to control motor speeds or LED brightness?",
      "Explain the working principle of the I2C communication protocol. Why are pull-up resistors required?",
      "What is an Analog-to-Digital Converter (ADC)? Explain ADC resolution (e.g. 10-bit vs 12-bit).",
      "Explain Ohm's Law and Kirchhoff's Laws (KCL and KVL) with a simple circuit example."
    ],
    "Intermediate": [
      "Explain ESP32 power management modes (Active, Modem-sleep, Light-sleep, Deep-sleep) and wake-up interrupts.",
      "How do you implement an AI anomaly detection model on real-time voltage and temperature sensor telemetry?",
      "Explain the Nyquist-Shannon sampling theorem and anti-aliasing low-pass filters.",
      "Compare MQTT, HTTP, and WebSockets for real-time IoT device telemetry streaming.",
      "Explain the operation of Op-Amps in inverting, non-inverting, and differential configurations."
    ],
    "Advanced": [
      "Architect an industrial IoT digital twin gateway aggregating 50+ sensor nodes over Modbus/RS485 and LoRa.",
      "Design a hardware-software watchdog and brownout detection strategy for remote microcontrollers.",
      "Explain how you would design a digital Kalman Filter to denoise sensor telemetry on an edge microcontroller.",
      "Discuss PCB layout design rules for high-speed digital and RF traces to minimize EMI and crosstalk.",
      "How do you implement TinyML / TensorFlow Lite for Microcontrollers on ESP32 or ARM Cortex-M4?"
    ]
  }
};

let currentInterviewState = {
  interviewId: null,
  role: 'Software Developer',
  difficulty: 'Intermediate',
  interviewType: 'Technical',
  questions: [],
  currentIndex: 0,
  timerInterval: null,
  timeLeft: 120,
  recognition: null,
  isRecording: false,
  answersLog: []
};

document.addEventListener('DOMContentLoaded', () => {
  initSelectionCards();
  initSpeechRecognition();
  initStartButton();
});

/* ===================================================================
   SELECTION WIZARD CONTROLS
   =================================================================== */
function initSelectionCards() {
  document.querySelectorAll('.role-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.role-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      currentInterviewState.role = card.getAttribute('data-role');
    });
  });

  document.querySelectorAll('.diff-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.diff-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      currentInterviewState.difficulty = card.getAttribute('data-diff');
    });
  });

  document.querySelectorAll('.type-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.type-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      currentInterviewState.interviewType = card.getAttribute('data-type');
    });
  });
}

function initStartButton() {
  const startBtn = document.getElementById('start-interview-btn');
  if (!startBtn) return;

  startBtn.addEventListener('click', async () => {
    startBtn.disabled = true;
    startBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Initializing AI Session...';

    // Try server API first, fallback instantly to client question bank
    let questions = [];
    let interviewId = 'int-' + Math.random().toString(36).substring(2, 9);

    try {
      const response = await fetch('/api/interview/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          role: currentInterviewState.role,
          difficulty: currentInterviewState.difficulty,
          interview_type: currentInterviewState.interviewType,
          count: 5
        })
      });
      if (response.ok) {
        const data = await response.json();
        questions = data.questions;
        interviewId = data.interview_id;
      } else {
        throw new Error('Fallback to client engine');
      }
    } catch (e) {
      // Client-side fallback engine for GitHub Pages
      const roleBank = CLIENT_QUESTION_BANK[currentInterviewState.role] || CLIENT_QUESTION_BANK["Software Developer"];
      questions = roleBank[currentInterviewState.difficulty] || roleBank["Intermediate"];
    }

    currentInterviewState.interviewId = interviewId;
    currentInterviewState.questions = questions;
    currentInterviewState.currentIndex = 0;
    currentInterviewState.answersLog = [];

    document.getElementById('interview-setup-section').style.display = 'none';
    document.getElementById('interview-chamber-section').style.display = 'block';
    window.scrollTo({ top: 100, behavior: 'smooth' });

    loadQuestion(0);
  });
}

function loadQuestion(index) {
  if (index >= currentInterviewState.questions.length) {
    finalizeInterview();
    return;
  }

  currentInterviewState.currentIndex = index;
  const questionText = currentInterviewState.questions[index];

  document.getElementById('current-q-num').textContent = `Question ${index + 1} of ${currentInterviewState.questions.length}`;
  document.getElementById('current-question-text').textContent = questionText;
  document.getElementById('user-answer-input').value = '';
  document.getElementById('answer-word-count').textContent = '0 words';

  document.getElementById('eval-result-container').style.display = 'none';
  document.getElementById('submit-answer-btn').style.display = 'inline-flex';
  document.getElementById('submit-answer-btn').disabled = false;
  document.getElementById('user-answer-input').disabled = false;

  resetTimer(120);
}

function resetTimer(seconds) {
  clearInterval(currentInterviewState.timerInterval);
  currentInterviewState.timeLeft = seconds;
  updateTimerDisplay();

  const timerBox = document.getElementById('timer-box');
  timerBox.classList.remove('timer-warning');

  currentInterviewState.timerInterval = setInterval(() => {
    currentInterviewState.timeLeft--;
    updateTimerDisplay();

    if (currentInterviewState.timeLeft <= 20) {
      timerBox.classList.add('timer-warning');
    }

    if (currentInterviewState.timeLeft <= 0) {
      clearInterval(currentInterviewState.timerInterval);
      showToast('Time is up for this question! Auto-submitting response.', 'info');
      submitAnswer();
    }
  }, 1000);
}

function updateTimerDisplay() {
  const m = Math.floor(currentInterviewState.timeLeft / 60).toString().padStart(2, '0');
  const s = (currentInterviewState.timeLeft % 60).toString().padStart(2, '0');
  document.getElementById('timer-val').textContent = `${m}:${s}`;
}

function initSpeechRecognition() {
  const micBtn = document.getElementById('mic-toggle-btn');
  if (!micBtn) return;

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    micBtn.title = 'Speech Recognition is not supported in this browser.';
    micBtn.style.opacity = '0.6';
    return;
  }

  currentInterviewState.recognition = new SpeechRecognition();
  currentInterviewState.recognition.continuous = true;
  currentInterviewState.recognition.interimResults = true;
  currentInterviewState.recognition.lang = 'en-US';

  currentInterviewState.recognition.onresult = (event) => {
    let transcript = '';
    for (let i = event.resultIndex; i < event.results.length; i++) {
      transcript += event.results[i][0].transcript;
    }
    const textarea = document.getElementById('user-answer-input');
    textarea.value = (textarea.value + ' ' + transcript).trim();
    updateWordCount();
  };

  currentInterviewState.recognition.onerror = () => stopRecording();

  micBtn.addEventListener('click', () => {
    if (currentInterviewState.isRecording) {
      stopRecording();
    } else {
      startRecording();
    }
  });

  const textarea = document.getElementById('user-answer-input');
  textarea.addEventListener('input', updateWordCount);
}

function startRecording() {
  if (!currentInterviewState.recognition) return;
  try {
    currentInterviewState.recognition.start();
    currentInterviewState.isRecording = true;
    const micBtn = document.getElementById('mic-toggle-btn');
    micBtn.classList.add('recording');
    document.getElementById('mic-btn-text').textContent = 'Listening...';
    showToast('Microphone active. Speak your answer clearly.', 'info');
  } catch (err) {}
}

function stopRecording() {
  if (!currentInterviewState.recognition) return;
  try {
    currentInterviewState.recognition.stop();
  } catch (err) {}
  currentInterviewState.isRecording = false;
  const micBtn = document.getElementById('mic-toggle-btn');
  if (micBtn) {
    micBtn.classList.remove('recording');
    document.getElementById('mic-btn-text').textContent = 'Voice Answer';
  }
}

function updateWordCount() {
  const val = document.getElementById('user-answer-input').value.trim();
  const words = val ? val.split(/\s+/).length : 0;
  document.getElementById('answer-word-count').textContent = `${words} words`;
}

/* ===================================================================
   SUBMIT & EVALUATE ANSWER
   =================================================================== */
async function submitAnswer() {
  stopRecording();
  clearInterval(currentInterviewState.timerInterval);

  const answerInput = document.getElementById('user-answer-input');
  const userAns = answerInput.value.trim();
  const submitBtn = document.getElementById('submit-answer-btn');

  submitBtn.disabled = true;
  submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> AI Evaluating...';

  let evalData = null;

  try {
    const response = await fetch('/api/interview/evaluate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        interview_id: currentInterviewState.interviewId,
        question_number: currentInterviewState.currentIndex + 1,
        question_text: currentInterviewState.questions[currentInterviewState.currentIndex],
        user_answer: userAns,
        role: currentInterviewState.role,
        difficulty: currentInterviewState.difficulty
      })
    });
    if (response.ok) {
      const res = await response.json();
      evalData = res.evaluation;
    } else {
      throw new Error('Fallback evaluation');
    }
  } catch (e) {
    // Client-side deterministic evaluation for GitHub Pages
    evalData = evaluateAnswerClient(userAns, currentInterviewState.role, currentInterviewState.questions[currentInterviewState.currentIndex]);
  }

  currentInterviewState.answersLog.push(evalData);
  renderEvaluation(evalData);
  submitBtn.style.display = 'none';
  answerInput.disabled = true;
}

function evaluateAnswerClient(userAnswer, role, question) {
  const words = userAnswer ? userAnswer.trim().split(/\s+/).length : 0;
  let overall = 75;
  let tech = 78;
  let comm = 80;
  let conf = 76;
  let relev = 82;

  if (words < 5) {
    return {
      overall_score: 35,
      technical_score: 30,
      communication_score: 40,
      confidence_score: 35,
      relevance_score: 35,
      feedback_well: "Acknowledged the prompt prompt.",
      feedback_missed: "Answer is too brief to evaluate technical depth or implementation details.",
      feedback_improve: "Use the Definition + Technical Architecture + Project Example format.",
      better_example: `A strong answer for ${role} should explain the core definition, key trade-offs, and how you applied it in practice.`
    };
  }

  if (words > 40) overall += 6;
  if (words > 80) overall += 6;
  if (userAnswer.toLowerCase().includes('python') || userAnswer.toLowerCase().includes('data') || userAnswer.toLowerCase().includes('system') || userAnswer.toLowerCase().includes('performance')) {
    tech += 8;
    overall += 4;
  }

  overall = Math.min(95, Math.max(55, overall));
  tech = Math.min(96, Math.max(50, tech));

  return {
    overall_score: overall,
    technical_score: tech,
    communication_score: comm,
    confidence_score: conf,
    relevance_score: relev,
    feedback_well: `Articulated concepts clearly for ${role} with structured reasoning.`,
    feedback_missed: `Could deepen discussions on operational trade-offs, concurrency, and edge-case error handling.`,
    feedback_improve: `Incorporate quantified metrics from personal/academic projects (e.g. SmartLabTwinAI or OpenCV).`,
    better_example: `Start with a 1-sentence definition of '${question}', explain internal architectural trade-offs, and illustrate with an applied engineering example.`
  };
}

function renderEvaluation(evalData) {
  const container = document.getElementById('eval-result-container');
  container.style.display = 'block';

  document.getElementById('eval-overall-score').textContent = `${evalData.overall_score}/100`;
  document.getElementById('eval-tech-score').textContent = `${evalData.technical_score}%`;
  document.getElementById('eval-comm-score').textContent = `${evalData.communication_score}%`;
  document.getElementById('eval-conf-score').textContent = `${evalData.confidence_score}%`;
  document.getElementById('eval-relev-score').textContent = `${evalData.relevance_score}%`;

  document.getElementById('eval-feedback-well').textContent = evalData.feedback_well;
  document.getElementById('eval-feedback-missed').textContent = evalData.feedback_missed;
  document.getElementById('eval-feedback-improve').textContent = evalData.feedback_improve;
  document.getElementById('eval-better-example').textContent = evalData.better_example;

  const nextBtn = document.getElementById('next-question-btn');
  const isLast = currentInterviewState.currentIndex >= currentInterviewState.questions.length - 1;
  nextBtn.innerHTML = isLast ? '<i class="fas fa-flag-checkered"></i> View Final Scorecard' : '<i class="fas fa-arrow-right"></i> Next Question';

  nextBtn.onclick = () => {
    loadQuestion(currentInterviewState.currentIndex + 1);
  };

  container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/* ===================================================================
   FINALIZE INTERVIEW & SCORECARD
   =================================================================== */
function finalizeInterview() {
  document.getElementById('interview-chamber-section').style.display = 'none';
  const scorecard = document.getElementById('interview-scorecard-section');
  scorecard.style.display = 'block';
  window.scrollTo({ top: 100, behavior: 'smooth' });

  const answers = currentInterviewState.answersLog;
  const avg = answers.length ? Math.round(answers.reduce((acc, cur) => acc + cur.overall_score, 0) / answers.length) : 85;

  document.getElementById('final-overall-score').textContent = avg;
  document.getElementById('final-readiness-badge').textContent = avg >= 80 ? 'Industry Placement Ready (High)' : 'Placement Ready (Intermediate)';
  document.getElementById('final-summary-text').textContent = `Candidate completed ${currentInterviewState.questions.length} questions for ${currentInterviewState.role} with an aggregate score of ${avg}/100. Demonstrates solid domain comprehension and technical communication.`;

  const strList = document.getElementById('final-strengths-list');
  strList.innerHTML = `
    <li><i class="fas fa-check-circle" style="color: var(--accent-emerald)"></i> Strong foundational knowledge in ${currentInterviewState.role}</li>
    <li><i class="fas fa-check-circle" style="color: var(--accent-emerald)"></i> Structured explanations with progressive clarity</li>
    <li><i class="fas fa-check-circle" style="color: var(--accent-emerald)"></i> Good confidence under time pressure</li>
  `;

  const weakList = document.getElementById('final-weaknesses-list');
  weakList.innerHTML = `
    <li><i class="fas fa-exclamation-triangle" style="color: var(--accent-amber)"></i> Elaborate more on edge-case concurrency handling</li>
    <li><i class="fas fa-exclamation-triangle" style="color: var(--accent-amber)"></i> Quantify impact metrics from project portfolio</li>
  `;

  const topicCloud = document.getElementById('final-topics-cloud');
  topicCloud.innerHTML = `
    <span class="badge badge-cyan">Data Structures</span>
    <span class="badge badge-cyan">System Architecture</span>
    <span class="badge badge-cyan">API Design</span>
    <span class="badge badge-cyan">IoT Telemetry & Optimization</span>
  `;

  // Save session to localStorage for dashboard history on GitHub Pages
  try {
    const history = JSON.parse(localStorage.getItem('careerai_interviews') || '[]');
    history.unshift({
      role: currentInterviewState.role,
      difficulty: currentInterviewState.difficulty,
      interview_type: currentInterviewState.interviewType,
      overall_score: avg,
      created_at: new Date().toISOString().split('T')[0]
    });
    localStorage.setItem('careerai_interviews', JSON.stringify(history.slice(0, 10)));
  } catch (e) {}

  showToast('Interview completed and scorecard generated!', 'success');
}
