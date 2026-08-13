/**
 * CareerAI — Interactive AI Mock Interview Suite
 * Full wizard, speech-to-text recording, dynamic timer, real-time evaluation & scorecard.
 */

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
  // Role selection
  document.querySelectorAll('.role-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.role-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      currentInterviewState.role = card.getAttribute('data-role');
    });
  });

  // Difficulty selection
  document.querySelectorAll('.diff-card').forEach(card => {
    card.addEventListener('click', () => {
      document.querySelectorAll('.diff-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      currentInterviewState.difficulty = card.getAttribute('data-diff');
    });
  });

  // Type selection
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

      const data = await response.json();
      currentInterviewState.interviewId = data.interview_id;
      currentInterviewState.questions = data.questions;
      currentInterviewState.currentIndex = 0;
      currentInterviewState.answersLog = [];

      // Transition views
      document.getElementById('interview-setup-section').style.display = 'none';
      document.getElementById('interview-chamber-section').style.display = 'block';
      window.scrollTo({ top: 100, behavior: 'smooth' });

      loadQuestion(0);
    } catch (err) {
      console.error(err);
      showToast('Error starting interview session. Please try again.', 'error');
      startBtn.disabled = false;
      startBtn.innerHTML = '<i class="fas fa-play"></i> Start AI Interview';
    }
  });
}

/* ===================================================================
   QUESTION LOADER & TIMER
   =================================================================== */
function loadQuestion(index) {
  if (index >= currentInterviewState.questions.length) {
    finalizeInterview();
    return;
  }

  currentInterviewState.currentIndex = index;
  const questionText = currentInterviewState.questions[index];

  // Update DOM
  document.getElementById('current-q-num').textContent = `Question ${index + 1} of ${currentInterviewState.questions.length}`;
  document.getElementById('current-question-text').textContent = questionText;
  document.getElementById('user-answer-input').value = '';
  document.getElementById('answer-word-count').textContent = '0 words';

  // Hide evaluation & show submit
  document.getElementById('eval-result-container').style.display = 'none';
  document.getElementById('submit-answer-btn').style.display = 'inline-flex';
  document.getElementById('submit-answer-btn').disabled = false;
  document.getElementById('user-answer-input').disabled = false;

  // Reset & Start Timer
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

/* ===================================================================
   SPEECH-TO-TEXT INTEGRATION
   =================================================================== */
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

  currentInterviewState.recognition.onerror = (e) => {
    console.warn('Speech recognition error:', e);
    stopRecording();
  };

  micBtn.addEventListener('click', () => {
    if (currentInterviewState.isRecording) {
      stopRecording();
    } else {
      startRecording();
    }
  });

  // Track word count on typing
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
  } catch (err) {
    console.error(err);
  }
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

    const res = await response.json();
    const evalData = res.evaluation;
    currentInterviewState.answersLog.push(evalData);

    // Render Evaluation Card
    renderEvaluation(evalData);
    submitBtn.style.display = 'none';
    answerInput.disabled = true;

  } catch (err) {
    console.error(err);
    showToast('Failed to evaluate answer. Please retry.', 'error');
    submitBtn.disabled = false;
    submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Submit Answer';
  }
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
async function finalizeInterview() {
  document.getElementById('interview-chamber-section').style.display = 'none';
  const scorecard = document.getElementById('interview-scorecard-section');
  scorecard.style.display = 'block';
  window.scrollTo({ top: 100, behavior: 'smooth' });

  try {
    const res = await fetch('/api/interview/finish', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        interview_id: currentInterviewState.interviewId,
        role: currentInterviewState.role,
        difficulty: currentInterviewState.difficulty
      })
    });

    const data = await res.json();
    const sum = data.summary;

    document.getElementById('final-overall-score').textContent = sum.overall_score;
    document.getElementById('final-readiness-badge').textContent = sum.readiness_rating;
    document.getElementById('final-summary-text').textContent = sum.summary;

    // Strengths
    const strList = document.getElementById('final-strengths-list');
    strList.innerHTML = '';
    (sum.strengths || []).forEach(s => {
      const li = document.createElement('li');
      li.innerHTML = `<i class="fas fa-check-circle" style="color: var(--accent-emerald)"></i> ${s}`;
      strList.appendChild(li);
    });

    // Weaknesses
    const weakList = document.getElementById('final-weaknesses-list');
    weakList.innerHTML = '';
    (sum.weaknesses || []).forEach(w => {
      const li = document.createElement('li');
      li.innerHTML = `<i class="fas fa-exclamation-triangle" style="color: var(--accent-amber)"></i> ${w}`;
      weakList.appendChild(li);
    });

    // Topics
    const topicCloud = document.getElementById('final-topics-cloud');
    topicCloud.innerHTML = '';
    (sum.recommended_topics || []).forEach(t => {
      const span = document.createElement('span');
      span.className = 'badge badge-cyan';
      span.textContent = t;
      topicCloud.appendChild(span);
    });

    showToast('Interview session completed and saved to dashboard history!', 'success');
  } catch (err) {
    console.error(err);
  }
}
