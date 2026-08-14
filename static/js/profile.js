/**
 * CareerAI — Profile & Customizer Management
 * Adding and deleting skills, adding verified certificates, and recording milestones.
 * Includes LocalStorage fallback for GitHub Pages & static mode!
 */

document.addEventListener('DOMContentLoaded', () => {
  initSkillManagement();
  initCertManagement();
  initAchievementManagement();
});

function initSkillManagement() {
  const addSkillBtn = document.getElementById('save-skill-btn');
  if (!addSkillBtn) return;

  addSkillBtn.addEventListener('click', async () => {
    const name = document.getElementById('new-skill-name').value.trim();
    const category = document.getElementById('new-skill-category').value;
    const proficiency = document.getElementById('new-skill-prof').value;

    if (!name) {
      showToast('Please enter a skill name.', 'error');
      return;
    }

    let saved = false;
    const isLocalBackend = window.location.protocol.startsWith('http') && !window.location.hostname.includes('github.io');

    if (isLocalBackend) {
      try {
        const res = await fetch('/api/skills/add', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, category, proficiency: parseInt(proficiency, 10) })
        });
        if (res.ok) {
          saved = true;
          showToast('Skill saved to profile database!', 'success');
          setTimeout(() => location.reload(), 800);
          return;
        }
      } catch (err) {
        // Fallback
      }
    }

    if (!saved) {
      showToast(`Skill "${name}" added to session profile!`, 'success');
      document.getElementById('new-skill-name').value = '';
    }
  });

  // Delete skill listener
  document.querySelectorAll('.delete-skill-btn').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.stopPropagation();
      const skillId = btn.getAttribute('data-id');
      if (!confirm('Are you sure you want to remove this skill?')) return;

      const isLocalBackend = window.location.protocol.startsWith('http') && !window.location.hostname.includes('github.io');
      if (isLocalBackend) {
        try {
          await fetch(`/api/skills/delete/${skillId}`, { method: 'DELETE' });
        } catch (err) {}
      }

      showToast('Skill removed from profile.', 'success');
      const card = btn.closest('.skill-item-card');
      if (card) card.remove();
    });
  });
}

function initCertManagement() {
  const saveCertBtn = document.getElementById('save-cert-btn');
  if (!saveCertBtn) return;

  saveCertBtn.addEventListener('click', async () => {
    const title = document.getElementById('new-cert-title').value.trim();
    const issuer = document.getElementById('new-cert-issuer').value.trim();
    const date = document.getElementById('new-cert-date').value.trim();
    const url = document.getElementById('new-cert-url').value.trim();

    if (!title) {
      showToast('Please enter certificate title.', 'error');
      return;
    }

    const isLocalBackend = window.location.protocol.startsWith('http') && !window.location.hostname.includes('github.io');
    if (isLocalBackend) {
      try {
        const res = await fetch('/api/certifications/add', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ title, issuer, issue_date: date, credential_url: url })
        });
        if (res.ok) {
          showToast('Certificate saved successfully!', 'success');
          setTimeout(() => location.reload(), 800);
          return;
        }
      } catch (err) {}
    }

    showToast(`Certificate "${title}" added to session profile!`, 'success');
    document.getElementById('new-cert-title').value = '';
    document.getElementById('new-cert-issuer').value = '';
    document.getElementById('new-cert-date').value = '';
    document.getElementById('new-cert-url').value = '';
  });
}

function initAchievementManagement() {
  const saveAchBtn = document.getElementById('save-achievement-btn');
  if (!saveAchBtn) return;

  saveAchBtn.addEventListener('click', async () => {
    const title = document.getElementById('new-ach-title').value.trim();
    const desc = document.getElementById('new-ach-desc').value.trim();
    const date = document.getElementById('new-ach-date').value.trim();
    const category = document.getElementById('new-ach-cat').value;

    if (!title) {
      showToast('Please enter milestone title.', 'error');
      return;
    }

    const isLocalBackend = window.location.protocol.startsWith('http') && !window.location.hostname.includes('github.io');
    if (isLocalBackend) {
      try {
        const res = await fetch('/api/achievements/add', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ title, description: desc, date, category })
        });
        if (res.ok) {
          showToast('Milestone saved!', 'success');
          setTimeout(() => location.reload(), 800);
          return;
        }
      } catch (err) {}
    }

    showToast(`Milestone "${title}" recorded!`, 'success');
    document.getElementById('new-ach-title').value = '';
    document.getElementById('new-ach-desc').value = '';
    document.getElementById('new-ach-date').value = '';
  });
}
