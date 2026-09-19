/**
 * Er. Pankaj Kumar - Physics Mentor (B.Tech, IIT Kanpur)
 * Interactive Features, Physics Simulator & WhatsApp Booking Integration
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initFaqAccordion();
  initPhysicsSimulator();
  initDemoForm();
  initScrollSpy();
});

/* ================= Mobile Navigation ================= */
function initMobileNav() {
  const hamburgerBtn = document.getElementById('hamburgerBtn');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (!hamburgerBtn || !navMenu) return;

  hamburgerBtn.addEventListener('click', () => {
    navMenu.classList.toggle('open');
    hamburgerBtn.classList.toggle('active');
  });

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('open');
      hamburgerBtn.classList.remove('active');
    });
  });
}

/* ================= FAQ Accordion ================= */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      
      // Close other open FAQs
      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
      });

      // Toggle clicked item
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });
}

/* ================= Course Card Prefill Helper ================= */
window.prefillCourse = function(courseName) {
  const classSelect = document.getElementById('studentClass');
  const examSelect = document.getElementById('targetExam');
  const messageArea = document.getElementById('userMessage');

  if (courseName.includes('Class 8-9')) {
    if (classSelect) classSelect.value = 'Class 8';
    if (examSelect) examSelect.value = 'Foundation & Olympiad';
  } else if (courseName.includes('Class 10')) {
    if (classSelect) classSelect.value = 'Class 10';
    if (examSelect) examSelect.value = 'CBSE / ICSE Board Mastery';
  } else if (courseName.includes('Class 11')) {
    if (classSelect) classSelect.value = 'Class 11';
    if (examSelect) examSelect.value = 'IIT-JEE (Main + Advanced)';
  } else if (courseName.includes('Class 12')) {
    if (classSelect) classSelect.value = 'Class 12';
    if (examSelect) examSelect.value = 'IIT-JEE (Main + Advanced)';
  } else if (courseName.includes('Dropper')) {
    if (classSelect) classSelect.value = 'Dropper / Repeater';
    if (examSelect) examSelect.value = 'IIT-JEE (Main + Advanced)';
  }

  if (messageArea && !messageArea.value) {
    messageArea.value = `Interested in the ${courseName} batch.`;
  }
};

/* ================= Demo Booking Form & WhatsApp ================= */
function initDemoForm() {
  const form = document.getElementById('demoForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const studentName = document.getElementById('studentName').value.trim();
    const parentContact = document.getElementById('parentContact').value.trim();
    const studentClass = document.getElementById('studentClass').value;
    const targetExam = document.getElementById('targetExam').value;
    const learningMode = document.getElementById('learningMode').value;
    const userMessage = document.getElementById('userMessage').value.trim();

    // Construct formatted message
    let waMessage = `*New Physics Demo / Inquiry Request*\n\n`;
    waMessage += `*Student Name:* ${studentName}\n`;
    waMessage += `*Contact:* ${parentContact}\n`;
    waMessage += `*Current Class:* ${studentClass}\n`;
    waMessage += `*Target Goal:* ${targetExam}\n`;
    waMessage += `*Mode Preferred:* ${learningMode}\n`;
    if (userMessage) {
      waMessage += `*Student Query:* ${userMessage}\n`;
    }
    waMessage += `\n(Sent via Er. Pankaj Kumar Physics Portal)`;

    const encodedMessage = encodeURIComponent(waMessage);
    const waUrl = `https://wa.me/917567220274?text=${encodedMessage}`;

    // Open WhatsApp
    window.open(waUrl, '_blank');

    // UI feedback
    alert(`Thank you, ${studentName}! Your demo consultation request is ready. WhatsApp is opening now to connect you directly with Er. Pankaj Kumar.`);
  });
}

/* ================= Interactive Physics Simulator (2D Kinematics) ================= */
function initPhysicsSimulator() {
  const canvas = document.getElementById('projectileCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const velSlider = document.getElementById('velSlider');
  const angleSlider = document.getElementById('angleSlider');
  const velVal = document.getElementById('velVal');
  const angleVal = document.getElementById('angleVal');
  const gravityName = document.getElementById('gravityName');
  const planetButtons = document.querySelectorAll('.btn-planet');
  const launchBtn = document.getElementById('launchBtn');
  const resetBtn = document.getElementById('resetSimBtn');

  const roMaxHeight = document.getElementById('roMaxHeight');
  const roTime = document.getElementById('roTime');
  const roRange = document.getElementById('roRange');

  let velocity = parseFloat(velSlider.value);
  let angleDeg = parseFloat(angleSlider.value);
  let g = 9.8;
  let isAnimating = false;
  let animationProgress = 1.0; // 0.0 to 1.0
  let animFrameId = null;

  function updateReadouts() {
    const theta = (angleDeg * Math.PI) / 180;
    const timeOfFlight = (2 * velocity * Math.sin(theta)) / g;
    const maxHeight = (Math.pow(velocity * Math.sin(theta), 2)) / (2 * g);
    const range = (Math.pow(velocity, 2) * Math.sin(2 * theta)) / g;

    roMaxHeight.textContent = `${maxHeight.toFixed(2)} m`;
    roTime.textContent = `${timeOfFlight.toFixed(2)} s`;
    roRange.textContent = `${range.toFixed(2)} m`;
    velVal.textContent = `${velocity} m/s`;
    angleVal.textContent = `${angleDeg}°`;
  }

  function drawScene() {
    const width = canvas.width;
    const height = canvas.height;

    ctx.clearRect(0, 0, width, height);

    // Coordinate space configuration
    const originX = 60;
    const originY = height - 50;
    const maxDrawWidth = width - 120;
    const maxDrawHeight = height - 100;

    const theta = (angleDeg * Math.PI) / 180;
    const timeOfFlight = (2 * velocity * Math.sin(theta)) / g;
    const maxHeight = (Math.pow(velocity * Math.sin(theta), 2)) / (2 * g);
    const range = (Math.pow(velocity, 2) * Math.sin(2 * theta)) / g;

    // Dynamic scaling so any launch fits nicely on the canvas
    const scaleX = maxDrawWidth / Math.max(range * 1.15, 80);
    const scaleY = maxDrawHeight / Math.max(maxHeight * 1.3, 30);

    // Draw coordinate axes & ground
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 1;

    // Subtle background grid
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    for (let x = originX; x < width - 20; x += 40) {
      ctx.beginPath();
      ctx.moveTo(x, 20);
      ctx.lineTo(x, originY);
      ctx.stroke();
    }
    for (let y = originY; y > 20; y -= 40) {
      ctx.beginPath();
      ctx.moveTo(originX, y);
      ctx.lineTo(width - 20, y);
      ctx.stroke();
    }

    // Ground line
    ctx.strokeStyle = '#475569';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(20, originY);
    ctx.lineTo(width - 20, originY);
    ctx.stroke();

    // Grass / Ground accent
    ctx.strokeStyle = '#10B981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(20, originY);
    ctx.lineTo(width - 20, originY);
    ctx.stroke();

    // Origin Launcher canon/platform
    ctx.fillStyle = '#F59E0B';
    ctx.beginPath();
    ctx.arc(originX, originY, 7, 0, Math.PI * 2);
    ctx.fill();

    // Draw Full Trajectory Path (dotted guide)
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.25)';
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(originX, originY);

    const steps = 100;
    for (let i = 0; i <= steps; i++) {
      const t = (i / steps) * timeOfFlight;
      const x = velocity * Math.cos(theta) * t;
      const y = velocity * Math.sin(theta) * t - 0.5 * g * Math.pow(t, 2);
      ctx.lineTo(originX + x * scaleX, originY - y * scaleY);
    }
    ctx.stroke();
    ctx.setLineDash([]); // Reset line dash

    // Draw Animated Solid Trajectory
    const currentT = animationProgress * timeOfFlight;
    ctx.strokeStyle = '#38BDF8';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(originX, originY);

    const activeSteps = Math.floor(steps * animationProgress);
    for (let i = 0; i <= activeSteps; i++) {
      const t = (i / steps) * timeOfFlight;
      const x = velocity * Math.cos(theta) * t;
      const y = velocity * Math.sin(theta) * t - 0.5 * g * Math.pow(t, 2);
      ctx.lineTo(originX + x * scaleX, originY - y * scaleY);
    }
    ctx.stroke();

    // Current Projectile Position
    const curX = velocity * Math.cos(theta) * currentT;
    const curY = Math.max(0, velocity * Math.sin(theta) * currentT - 0.5 * g * Math.pow(currentT, 2));
    const projCanvasX = originX + curX * scaleX;
    const projCanvasY = originY - curY * scaleY;

    // Glowing Projectile Ball
    ctx.save();
    ctx.shadowColor = '#F59E0B';
    ctx.shadowBlur = 12;
    ctx.fillStyle = '#FBBF24';
    ctx.beginPath();
    ctx.arc(projCanvasX, projCanvasY, 8, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    // Velocity vector arrows
    const vx = velocity * Math.cos(theta);
    const vy = velocity * Math.sin(theta) - g * currentT;
    const arrowLen = 0.5;

    ctx.strokeStyle = '#F59E0B';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(projCanvasX, projCanvasY);
    ctx.lineTo(projCanvasX + vx * arrowLen, projCanvasY - vy * arrowLen);
    ctx.stroke();

    // Draw Apex Point (Hmax)
    const apexT = (velocity * Math.sin(theta)) / g;
    if (currentT >= apexT || animationProgress >= 1.0) {
      const apexX = originX + (range / 2) * scaleX;
      const apexY = originY - maxHeight * scaleY;

      ctx.fillStyle = '#EF4444';
      ctx.beginPath();
      ctx.arc(apexX, apexY, 4, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#CBD5E1';
      ctx.font = '11px Plus Jakarta Sans';
      ctx.fillText(`Hmax = ${maxHeight.toFixed(1)}m`, apexX - 35, apexY - 10);
    }

    // Landing marker & label
    const landingX = originX + range * scaleX;
    ctx.fillStyle = '#38BDF8';
    ctx.beginPath();
    ctx.arc(landingX, originY, 4, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#94A3B8';
    ctx.font = '11px Plus Jakarta Sans';
    ctx.fillText(`R = ${range.toFixed(1)}m`, landingX - 25, originY + 22);
  }

  function startAnimation() {
    if (animFrameId) cancelAnimationFrame(animFrameId);
    isAnimating = true;
    animationProgress = 0.0;

    let lastTime = performance.now();
    const duration = 2000; // 2 seconds animation

    function step(now) {
      const delta = now - lastTime;
      animationProgress += delta / duration;

      if (animationProgress >= 1.0) {
        animationProgress = 1.0;
        isAnimating = false;
        drawScene();
      } else {
        drawScene();
        animFrameId = requestAnimationFrame(step);
      }
      lastTime = now;
    }

    animFrameId = requestAnimationFrame(step);
  }

  // Event Listeners
  velSlider.addEventListener('input', (e) => {
    velocity = parseFloat(e.target.value);
    updateReadouts();
    if (!isAnimating) {
      animationProgress = 1.0;
      drawScene();
    }
  });

  angleSlider.addEventListener('input', (e) => {
    angleDeg = parseFloat(e.target.value);
    updateReadouts();
    if (!isAnimating) {
      animationProgress = 1.0;
      drawScene();
    }
  });

  planetButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      planetButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      g = parseFloat(btn.dataset.g);
      gravityName.textContent = btn.dataset.name;
      updateReadouts();
      if (!isAnimating) {
        animationProgress = 1.0;
        drawScene();
      }
    });
  });

  launchBtn.addEventListener('click', () => {
    startAnimation();
  });

  resetBtn.addEventListener('click', () => {
    velSlider.value = 45;
    angleSlider.value = 45;
    velocity = 45;
    angleDeg = 45;
    g = 9.8;
    planetButtons.forEach(b => {
      if (b.dataset.g === '9.8') b.classList.add('active');
      else b.classList.remove('active');
    });
    gravityName.textContent = 'Earth (9.8 m/s²)';
    updateReadouts();
    animationProgress = 1.0;
    drawScene();
  });

  // Initial render
  updateReadouts();
  drawScene();
}

/* ================= ScrollSpy for Active Links ================= */
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id], header[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPosition = window.pageYOffset + 150;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });
}
