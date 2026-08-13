/**
 * CareerAI — Dashboard Analytics & Interactive Charts
 * Pure SVG dynamic chart renderers for line performance & radar skill polygon.
 */

document.addEventListener('DOMContentLoaded', () => {
  renderLineChart();
  renderRadarChart();
});

/* ===================================================================
   INTERACTIVE SVG LINE CHART (Interview Performance Trend)
   =================================================================== */
function renderLineChart() {
  const container = document.getElementById('perf-line-chart');
  if (!container) return;

  const dataPoints = [
    { label: 'Session 1', score: 68 },
    { label: 'Session 2', score: 74 },
    { label: 'Session 3', score: 79 },
    { label: 'Session 4', score: 84 },
    { label: 'Session 5', score: 88 }
  ];

  const svgNS = 'http://www.w3.org/2000/svg';
  const width = container.clientWidth || 500;
  const height = 240;
  const padding = 40;

  const svg = document.createElementNS(svgNS, 'svg');
  svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
  svg.setAttribute('width', '100%');
  svg.setAttribute('height', '100%');

  // Draw Grid Lines & Labels
  [40, 60, 80, 100].forEach(val => {
    const y = height - padding - ((val - 30) / 70) * (height - padding * 2);
    const line = document.createElementNS(svgNS, 'line');
    line.setAttribute('x1', padding);
    line.setAttribute('y1', y);
    line.setAttribute('x2', width - padding);
    line.setAttribute('y2', y);
    line.setAttribute('stroke', 'rgba(255,255,255,0.06)');
    line.setAttribute('stroke-dasharray', '4 4');
    svg.appendChild(line);

    const text = document.createElementNS(svgNS, 'text');
    text.setAttribute('x', padding - 10);
    text.setAttribute('y', y + 4);
    text.setAttribute('text-anchor', 'end');
    text.setAttribute('fill', 'var(--text-muted)');
    text.setAttribute('font-size', '11px');
    text.textContent = `${val}%`;
    svg.appendChild(text);
  });

  // Calculate coordinates
  const points = dataPoints.map((d, i) => {
    const x = padding + (i / (dataPoints.length - 1)) * (width - padding * 2);
    const y = height - padding - ((d.score - 30) / 70) * (height - padding * 2);
    return { x, y, score: d.score, label: d.label };
  });

  // Area Path
  let areaD = `M ${points[0].x} ${height - padding}`;
  points.forEach(p => { areaD += ` L ${p.x} ${p.y}`; });
  areaD += ` L ${points[points.length - 1].x} ${height - padding} Z`;

  const areaPath = document.createElementNS(svgNS, 'path');
  areaPath.setAttribute('d', areaD);
  areaPath.setAttribute('fill', 'url(#accent-gradient-area)');
  areaPath.setAttribute('opacity', '0.25');

  // Gradient Def
  const defs = document.createElementNS(svgNS, 'defs');
  defs.innerHTML = `
    <linearGradient id="accent-gradient-area" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.0"/>
    </linearGradient>
  `;
  svg.appendChild(defs);
  svg.appendChild(areaPath);

  // Line Path
  let lineD = `M ${points[0].x} ${points[0].y}`;
  for (let i = 1; i < points.length; i++) {
    lineD += ` L ${points[i].x} ${points[i].y}`;
  }

  const linePath = document.createElementNS(svgNS, 'path');
  linePath.setAttribute('d', lineD);
  linePath.setAttribute('fill', 'none');
  linePath.setAttribute('stroke', 'var(--accent-cyan)');
  linePath.setAttribute('stroke-width', '3');
  linePath.setAttribute('stroke-linecap', 'round');
  svg.appendChild(linePath);

  // Circles & Tooltips
  points.forEach(p => {
    const circle = document.createElementNS(svgNS, 'circle');
    circle.setAttribute('cx', p.x);
    circle.setAttribute('cy', p.y);
    circle.setAttribute('r', '5');
    circle.setAttribute('fill', '#ffffff');
    circle.setAttribute('stroke', 'var(--accent-cyan)');
    circle.setAttribute('stroke-width', '3');
    svg.appendChild(circle);

    const text = document.createElementNS(svgNS, 'text');
    text.setAttribute('x', p.x);
    text.setAttribute('y', p.y - 12);
    text.setAttribute('text-anchor', 'middle');
    text.setAttribute('fill', 'var(--text-primary)');
    text.setAttribute('font-size', '12px');
    text.setAttribute('font-weight', '600');
    text.textContent = `${p.score}%`;
    svg.appendChild(text);
  });

  container.innerHTML = '';
  container.appendChild(svg);
}

/* ===================================================================
   SVG RADAR CHART (5-Axis Skill Distribution)
   =================================================================== */
function renderRadarChart() {
  const container = document.getElementById('skill-radar-chart');
  if (!container) return;

  const axes = [
    { label: 'Software Dev', value: 85 },
    { label: 'Python / Flask', value: 90 },
    { label: 'ECE & IoT', value: 88 },
    { label: 'AI & Vision', value: 80 },
    { label: 'Communication', value: 82 }
  ];

  const svgNS = 'http://www.w3.org/2000/svg';
  const size = 260;
  const center = size / 2;
  const radius = size * 0.38;
  const numAxes = axes.length;

  const svg = document.createElementNS(svgNS, 'svg');
  svg.setAttribute('viewBox', `0 0 ${size} ${size}`);
  svg.setAttribute('width', '100%');
  svg.setAttribute('height', '100%');

  // Background Web Rings
  [0.3, 0.6, 1.0].forEach(level => {
    let polyPoints = '';
    for (let i = 0; i < numAxes; i++) {
      const angle = (i * 2 * Math.PI / numAxes) - (Math.PI / 2);
      const x = center + radius * level * Math.cos(angle);
      const y = center + radius * level * Math.sin(angle);
      polyPoints += `${x},${y} `;
    }
    const polygon = document.createElementNS(svgNS, 'polygon');
    polygon.setAttribute('points', polyPoints.trim());
    polygon.setAttribute('fill', 'none');
    polygon.setAttribute('stroke', 'rgba(255,255,255,0.08)');
    polygon.setAttribute('stroke-width', '1');
    svg.appendChild(polygon);
  });

  // Axis Spokes & Labels
  axes.forEach((axis, i) => {
    const angle = (i * 2 * Math.PI / numAxes) - (Math.PI / 2);
    const x = center + radius * Math.cos(angle);
    const y = center + radius * Math.sin(angle);

    const spoke = document.createElementNS(svgNS, 'line');
    spoke.setAttribute('x1', center);
    spoke.setAttribute('y1', center);
    spoke.setAttribute('x2', x);
    spoke.setAttribute('y2', y);
    spoke.setAttribute('stroke', 'rgba(255,255,255,0.1)');
    svg.appendChild(spoke);

    // Label position
    const labelX = center + (radius + 22) * Math.cos(angle);
    const labelY = center + (radius + 22) * Math.sin(angle);

    const text = document.createElementNS(svgNS, 'text');
    text.setAttribute('x', labelX);
    text.setAttribute('y', labelY + 4);
    text.setAttribute('text-anchor', 'middle');
    text.setAttribute('fill', 'var(--text-secondary)');
    text.setAttribute('font-size', '10px');
    text.setAttribute('font-weight', '600');
    text.textContent = axis.label;
    svg.appendChild(text);
  });

  // Data Polygon
  let dataPoints = '';
  axes.forEach((axis, i) => {
    const angle = (i * 2 * Math.PI / numAxes) - (Math.PI / 2);
    const dist = (axis.value / 100) * radius;
    const x = center + dist * Math.cos(angle);
    const y = center + dist * Math.sin(angle);
    dataPoints += `${x},${y} `;
  });

  const dataPoly = document.createElementNS(svgNS, 'polygon');
  dataPoly.setAttribute('points', dataPoints.trim());
  dataPoly.setAttribute('fill', 'rgba(56, 189, 248, 0.25)');
  dataPoly.setAttribute('stroke', 'var(--accent-cyan)');
  dataPoly.setAttribute('stroke-width', '2.5');
  svg.appendChild(dataPoly);

  container.innerHTML = '';
  container.appendChild(svg);
}
