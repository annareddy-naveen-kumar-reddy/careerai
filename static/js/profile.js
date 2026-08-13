/**
 * CareerAI — Profile & Customizer Management
 * Adding and deleting skills, adding verified certificates, and recording milestones.
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

    try {
      const res = await fetch('/api/skills/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, category, proficiency: parseInt(proficiency, 10) })
      });

      const data = await res.json();
      if (res.ok) {
        showToast(data.message, 'success');
        setTimeout(() => location.reload(), 800);
      } else {
        showToast(data.error || 'Failed to add skill.', 'error');
      }
    } catch (err) {
      console.error(err);
      showToast('Error saving skill.', 'error');
    }
  });

  // Delete skill listener
  document.querySelectorAll('.delete-skill-btn').forEach(btn => {
    btn.addEventListener('click', async (e) => {
      e.stopPropagation();
      const skillId = btn.getAttribute('data-id');
      if (!confirm('Are you sure you want to remove this skill?')) return;

      try {
        const res = await fetch(`/api/skills/delete/${skillId}`, { method: 'DELETE' });
        if (res.ok) {
          showToast('Skill removed.', 'success');
          btn.closest('.skill-item-card').remove();
        }
      } catch (err) {
        console.error(err);
      }
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

    try {
      const res = await fetch('/api/certifications/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, issuer, issue_date: date, credential_url: url })
      });

      if (res.ok) {
        showToast('Certificate saved successfully!', 'success');
        setTimeout(() => location.reload(), 800);
      }
    } catch (err) {
      console.error(err);
    }
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

    try {
      const res = await fetch('/api/achievements/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description: desc, date, category })
      });

      if (res.ok) {
        showToast('Milestone saved!', 'success');
        setTimeout(() => location.reload(), 800);
      }
    } catch (err) {
      console.error(err);
    }
  });
}
