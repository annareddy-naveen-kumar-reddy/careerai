/**
 * CareerAI — Skill Gap Analyzer & Job Role Matcher Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initSkillGapCalculator();
  initRoleMatcherCalculator();
});

/* ===================================================================
   SKILL GAP ANALYZER
   =================================================================== */
function initSkillGapCalculator() {
  const roleSelect = document.getElementById('gap-target-role');
  if (!roleSelect) return;

  roleSelect.addEventListener('change', () => {
    fetchSkillGapAnalysis(roleSelect.value);
  });

  // Initial load
  fetchSkillGapAnalysis(roleSelect.value || 'Software Developer');
}

async function fetchSkillGapAnalysis(role) {
  const container = document.getElementById('skill-gap-table-body');
  if (!container) return;

  container.innerHTML = '<tr><td colspan="5" style="text-align:center; padding: 2rem;"><i class="fas fa-spinner fa-spin"></i> Calculating skill alignment...</td></tr>';

  try {
    const res = await fetch('/api/skills/gap-analysis', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ target_role: role })
    });

    const data = await res.json();
    renderSkillGapResults(data);
  } catch (err) {
    console.error(err);
  }
}

function renderSkillGapResults(data) {
  const tbody = document.getElementById('skill-gap-table-body');
  const readinessText = document.getElementById('gap-readiness-val');
  const readinessBar = document.getElementById('gap-readiness-bar');

  if (readinessText) readinessText.textContent = `${data.readiness_percentage}%`;
  if (readinessBar) readinessBar.style.width = `${data.readiness_percentage}%`;

  tbody.innerHTML = '';

  (data.skills_analyzed || []).forEach(item => {
    const tr = document.createElement('tr');
    tr.style.borderBottom = '1px solid var(--border-subtle)';

    const priorityBadge = item.priority === 'High' 
      ? '<span class="badge badge-amber">High Priority</span>'
      : (item.priority === 'Medium' ? '<span class="badge badge-cyan">Medium</span>' : '<span class="badge badge-emerald">On Track</span>');

    const statusBadge = item.gap_status === 'Proficient'
      ? '<span style="color: var(--accent-emerald); font-weight: 600;"><i class="fas fa-check-circle"></i> Proficient</span>'
      : (item.gap_status === 'Needs Practice' 
        ? '<span style="color: var(--accent-amber); font-weight: 600;"><i class="fas fa-wrench"></i> Needs Practice</span>'
        : '<span style="color: var(--accent-rose); font-weight: 600;"><i class="fas fa-arrow-up"></i> Skill Gap</span>');

    tr.innerHTML = `
      <td style="padding: 1rem 0.75rem; font-weight: 600; color: var(--text-primary);">${item.skill}</td>
      <td style="padding: 1rem 0.75rem;">${item.importance}</td>
      <td style="padding: 1rem 0.75rem;">${priorityBadge}</td>
      <td style="padding: 1rem 0.75rem;">${statusBadge}</td>
      <td style="padding: 1rem 0.75rem;">
        <div class="progress-wrapper" style="height: 6px; width: 100px;">
          <div class="progress-fill ${item.current_proficiency >= 3 ? 'progress-fill-emerald' : ''}" style="width: ${(item.current_proficiency / 5) * 100}%"></div>
        </div>
      </td>
    `;
    tbody.appendChild(tr);
  });

  // Recommended Projects
  const projList = document.getElementById('gap-recommended-projects');
  if (projList) {
    projList.innerHTML = '';
    (data.recommended_projects || []).forEach(p => {
      const li = document.createElement('li');
      li.style.marginBottom = '0.5rem';
      li.innerHTML = `<i class="fas fa-project-diagram" style="color: var(--accent-cyan)"></i> ${p}`;
      projList.appendChild(li);
    });
  }

  // Interview Topics
  const topicList = document.getElementById('gap-interview-topics');
  if (topicList) {
    topicList.innerHTML = '';
    (data.interview_topics || []).forEach(t => {
      const li = document.createElement('li');
      li.style.marginBottom = '0.5rem';
      li.innerHTML = `<i class="fas fa-book" style="color: var(--accent-emerald)"></i> ${t}`;
      topicList.appendChild(li);
    });
  }
}

/* ===================================================================
   JOB ROLE MATCHER
   =================================================================== */
function initRoleMatcherCalculator() {
  const checkboxes = document.querySelectorAll('.matcher-skill-checkbox');
  const calcBtn = document.getElementById('calculate-match-btn');
  if (!calcBtn) return;

  calcBtn.addEventListener('click', async () => {
    const selectedSkills = [];
    document.querySelectorAll('.matcher-skill-checkbox:checked').forEach(chk => {
      selectedSkills.push(chk.value);
    });

    const expLevel = document.getElementById('matcher-exp-select') ? document.getElementById('matcher-exp-select').value : 'Fresher';

    calcBtn.disabled = true;
    calcBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Calculating Fit...';

    try {
      const res = await fetch('/api/role-matcher/match', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ skills: selectedSkills, experience_level: expLevel })
      });

      const data = await res.json();
      renderRoleMatchCards(data.matches);
      showToast('Role matching calculated successfully!', 'success');
    } catch (err) {
      console.error(err);
      showToast('Error calculating role match.', 'error');
    } finally {
      calcBtn.disabled = false;
      calcBtn.innerHTML = '<i class="fas fa-calculator"></i> Match My Profile';
    }
  });
}

function renderRoleMatchCards(matches) {
  const container = document.getElementById('role-matches-grid');
  if (!container) return;

  container.innerHTML = '';

  (matches || []).forEach((m, i) => {
    const card = document.createElement('div');
    card.className = 'glass-card hover-lift';
    card.style.display = 'flex';
    card.style.flexDirection = 'column';
    card.style.gap = '1rem';

    const matchColor = m.match_percentage >= 75 ? 'var(--accent-emerald)' : (m.match_percentage >= 50 ? 'var(--accent-cyan)' : 'var(--accent-amber)');

    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <span class="badge badge-cyan" style="margin-bottom: 0.4rem;">${m.category}</span>
          <h3 style="font-size: 1.25rem;">${m.role}</h3>
        </div>
        <div style="text-align: right;">
          <span style="font-size: 1.85rem; font-weight: 800; color: ${matchColor};">${m.match_percentage}%</span>
          <div style="font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase;">Match Score</div>
        </div>
      </div>

      <p style="font-size: 0.88rem;">${m.description}</p>

      <div class="progress-wrapper" style="height: 6px;">
        <div class="progress-fill" style="width: ${m.match_percentage}%; background: ${matchColor};"></div>
      </div>

      <div>
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-emerald); margin-bottom: 0.4rem; text-transform: uppercase;">
          <i class="fas fa-check-circle"></i> Matching Skills (${m.matched_skills.length})
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.35rem;">
          ${m.matched_skills.slice(0, 4).map(s => `<span class="skill-pill tech" style="font-size: 0.75rem;">${s}</span>`).join('')}
        </div>
      </div>

      ${m.missing_skills.length ? `
      <div>
        <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-rose); margin-bottom: 0.4rem; text-transform: uppercase;">
          <i class="fas fa-exclamation-circle"></i> Recommended to Learn
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 0.35rem;">
          ${m.missing_skills.slice(0, 3).map(s => `<span class="skill-pill missing" style="font-size: 0.75rem;">${s}</span>`).join('')}
        </div>
      </div>
      ` : ''}

      <div style="margin-top: auto; pt: 0.5rem;">
        <a href="/interview" class="btn btn-secondary btn-sm" style="width: 100%;">
          <i class="fas fa-microphone"></i> Practice ${m.role} Interview
        </a>
      </div>
    `;

    container.appendChild(card);
  });

  container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
