/**
 * CareerAI — Project Live Simulations
 * 1. SmartLabTwinAI: Real-Time Digital Twin IoT Telemetry Streamer
 * 2. AI Smart Attendance System: Face Detection & Cloud Sync Simulator
 */

document.addEventListener('DOMContentLoaded', () => {
  initSmartLabTwinSimulator();
  initAttendanceSimulator();
});

/* ===================================================================
   SMARTLABTWINAI DIGITAL TWIN SIMULATION
   =================================================================== */
function initSmartLabTwinSimulator() {
  const tempVal = document.getElementById('twin-temp');
  const humidityVal = document.getElementById('twin-humidity');
  const voltageVal = document.getElementById('twin-voltage');
  const currentVal = document.getElementById('twin-current');
  const statusBadge = document.getElementById('twin-status-badge');
  const stressBtn = document.getElementById('twin-stress-btn');

  if (!tempVal) return;

  let isStressed = false;

  // Periodic Telemetry Updates
  setInterval(() => {
    if (isStressed) {
      // Elevated / Anomaly parameters
      tempVal.textContent = `${(36.5 + Math.random() * 2.5).toFixed(1)} °C`;
      humidityVal.textContent = `${(68 + Math.random() * 4).toFixed(0)} %`;
      voltageVal.textContent = `${(245 + Math.random() * 8).toFixed(1)} V`;
      currentVal.textContent = `${(8.4 + Math.random() * 1.8).toFixed(2)} A`;
    } else {
      // Normal operating parameters
      tempVal.textContent = `${(24.2 + Math.random() * 1.2).toFixed(1)} °C`;
      humidityVal.textContent = `${(52 + Math.random() * 3).toFixed(0)} %`;
      voltageVal.textContent = `${(228 + Math.random() * 3).toFixed(1)} V`;
      currentVal.textContent = `${(3.1 + Math.random() * 0.6).toFixed(2)} A`;
    }
  }, 2000);

  if (stressBtn) {
    stressBtn.addEventListener('click', () => {
      isStressed = !isStressed;
      if (isStressed) {
        stressBtn.innerHTML = '<i class="fas fa-undo"></i> Normalize Lab Telemetry';
        stressBtn.className = 'btn btn-outline btn-sm';
        statusBadge.className = 'badge badge-amber';
        statusBadge.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Anomaly Detected (High Current)';
        showToast('SmartLabTwinAI: Machine Learning Anomaly Classifier Triggered Alert!', 'error');
      } else {
        stressBtn.innerHTML = '<i class="fas fa-bolt"></i> Simulate High Load / Anomaly';
        stressBtn.className = 'btn btn-secondary btn-sm';
        statusBadge.className = 'badge badge-emerald';
        statusBadge.innerHTML = '<i class="fas fa-check-circle"></i> Digital Twin Nominal';
        showToast('SmartLabTwinAI: Lab parameters returned to nominal baseline.', 'success');
      }
    });
  }
}

/* ===================================================================
   AI SMART ATTENDANCE SIMULATION
   =================================================================== */
function initAttendanceSimulator() {
  const scanBtn = document.getElementById('attendance-scan-btn');
  const logBox = document.getElementById('attendance-log-box');
  const scanStatus = document.getElementById('attendance-scan-status');

  if (!scanBtn) return;

  scanBtn.addEventListener('click', () => {
    scanBtn.disabled = true;
    scanBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing Video Frame...';
    scanStatus.textContent = 'Status: Extracting 128-d Face Embeddings with OpenCV...';

    setTimeout(() => {
      scanStatus.textContent = 'Status: Face Matched (Confidence: 98.4%) — Logging to SQLite & Google Sheets...';

      setTimeout(() => {
        scanStatus.textContent = 'Status: Verified & Synced Successfully';
        scanBtn.disabled = false;
        scanBtn.innerHTML = '<i class="fas fa-camera"></i> Simulate Face Recognition Scan';

        const now = new Date().toLocaleTimeString();
        const newLog = document.createElement('div');
        newLog.style.fontSize = '0.82rem';
        newLog.style.padding = '0.4rem 0';
        newLog.style.borderBottom = '1px solid rgba(255,255,255,0.05)';
        newLog.innerHTML = `
          <span style="color: var(--accent-cyan); font-family: var(--font-mono); font-weight: 600;">[${now}]</span>
          <span style="color: var(--text-primary); font-weight: 600;"> Annareddy Naveen Kumar Reddy</span> 
          <span class="badge badge-emerald" style="font-size: 0.65rem; margin-left: 0.5rem;">Present</span>
          <span style="color: var(--text-muted); font-size: 0.75rem;">(Cloud Sync: OK)</span>
        `;

        if (logBox) {
          logBox.insertBefore(newLog, logBox.firstChild);
        }
        showToast('AI Attendance: Face recognized and attendance logged to Google Sheets.', 'success');
      }, 1000);
    }, 1200);
  });
}
