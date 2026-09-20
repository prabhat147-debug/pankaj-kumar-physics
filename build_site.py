import os
import base64

def get_b64(rel_path):
    p = os.path.join(r'C:\Users\HP\.gemini\antigravity\scratch\pankaj-kumar-physics', rel_path)
    with open(p, 'rb') as f:
        return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode('utf-8')

logo_h = get_b64('assets/images/prepphy-logo-horizontal.jpg')
logo_sq = get_b64('assets/images/prepphy-logo-square.jpg')
sir_suit = get_b64('assets/images/pankaj-sir-suit.jpg')
sheet_vector = get_b64('assets/images/vector-revision-sheet.jpg')
poster1 = get_b64('assets/images/pankaj-sir-poster1.jpg')
poster2 = get_b64('assets/images/pankaj-sir-poster2.jpg')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>PrepPHY | Physics for Competitive Excellence | Er. Pankaj Kumar (B.Tech, IIT Kanpur)</title>
  <meta name="description" content="PrepPHY by Er. Pankaj Kumar (B.Tech IIT Kanpur) — Premier Physics coaching for Class 8 to 12, IIT-JEE (Main & Adv.) & NEET-UG in Faridabad. Mentored AIR-4 & AIR-75 in NEET, AIR-238 & AIR-490 in JEE." />
  <meta name="keywords" content="PrepPHY, Pankaj Kumar Physics, IIT Kanpur Physics, NEET Physics Faridabad, JEE Advanced Physics, MVN Faridabad Physics, Shiksha Sopan HC Verma, Physics Tutor Faridabad" />
  <meta name="author" content="Er. Pankaj Kumar" />

  <!-- OpenGraph -->
  <meta property="og:title" content="PrepPHY — Physics for Competitive Excellence | Er. Pankaj Kumar" />
  <meta property="og:description" content="Master Physics with IITian Pedigree. Mentored AIR-4 & AIR-75 in NEET, AIR-238 & AIR-490 in JEE. Batches for Class 8-12 in Faridabad & Online." />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="assets/images/prepphy-logo-horizontal.jpg" />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet" />

  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="announcement-bar">
    <div class="container announcement-content">
      <span class="badge-pulse"><i class="fa-solid fa-trophy"></i> Mentor to AIR-4 &amp; AIR-75 (NEET) | AIR-238 &amp; AIR-490 (JEE)</span>
      <span class="announcement-text">Admissions Open for Class 8th–12th &amp; Droppers (Faridabad Batches &amp; Live Online)</span>
      <a href="https://wa.me/917567220274?text=Hi%20Pankaj%20Sir,%20I%20am%20interested%20in%20PrepPHY%20Physics%20classes." target="_blank" class="announcement-cta">
        <i class="fa-brands fa-whatsapp"></i> WhatsApp: +91 75672 20274
      </a>
    </div>
  </div>

  <!-- Main Navigation Bar -->
  <header class="navbar" id="navbar">
    <div class="container nav-container">
      <a href="#home" class="brand-logo">
        <img src="{logo_h}" alt="PrepPHY - Physics for Competitive Excellence by Pankaj Kumar IIT Kanpur" class="brand-logo-img" />
      </a>

      <nav class="nav-menu" id="navMenu">
        <ul class="nav-links">
          <li><a href="#home" class="nav-link active">Home</a></li>
          <li><a href="#about" class="nav-link">About Sir</a></li>
          <li><a href="#results" class="nav-link">Hall of Fame</a></li>
          <li><a href="#courses" class="nav-link">Programs (8th–12th)</a></li>
          <li><a href="#materials" class="nav-link">Study Material</a></li>
          <li><a href="#simulator" class="nav-link"><i class="fa-solid fa-flask-vial"></i> Physics Lab</a></li>
          <li><a href="#contact" class="nav-link">Contact</a></li>
        </ul>
        <div class="nav-action-buttons mobile-only">
          <a href="tel:+917567220274" class="btn btn-outline-nav"><i class="fa-solid fa-phone"></i> Call: 75672 20274</a>
          <a href="#book-demo" class="btn btn-primary"><i class="fa-regular fa-calendar-check"></i> Book Free Demo</a>
        </div>
      </nav>

      <div class="nav-actions desktop-only">
        <a href="tel:+917567220274" class="phone-link">
          <i class="fa-solid fa-phone-volume"></i>
          <span>+91 75672 20274</span>
        </a>
        <a href="#book-demo" class="btn btn-primary btn-sm glow-btn">
          <i class="fa-regular fa-calendar-check"></i> Book Free Demo
        </a>
      </div>

      <button class="hamburger" id="hamburgerBtn" aria-label="Toggle navigation menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section" id="home">
    <div class="hero-bg-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="grid-overlay"></div>
    </div>

    <div class="container hero-container">
      <div class="hero-content">
        <div class="hero-badge">
          <span class="badge-icon"><i class="fa-solid fa-atom"></i></span>
          <span class="badge-text">Where Conceptual Clarity Meets Competitive Success</span>
        </div>

        <h1 class="hero-title">
          Concepts Build <span class="gradient-text">Confidence</span>.<br />
          Practice Builds <span class="gradient-text">Rank</span>.
        </h1>

        <p class="hero-description">
          Transform Physics from your toughest challenge into your highest scoring strength. Personalized, rigorous mentorship by <strong>Er. Pankaj Kumar</strong> — <strong>B.Tech from IIT Kanpur</strong>, 11+ years teaching experience, and Senior Faculty at <strong>MVN School, Sector-17, Faridabad</strong>.
        </p>

        <!-- Proven Pedigree Highlights -->
        <div class="cred-strip">
          <div class="cred-item">
            <i class="fa-solid fa-graduation-cap text-gold"></i>
            <span><strong>B.Tech, IIT Kanpur</strong> (AIR 1247)</span>
          </div>
          <div class="cred-item">
            <i class="fa-solid fa-award text-gold"></i>
            <span><strong>AIR-4 &amp; AIR-75</strong> in NEET</span>
          </div>
          <div class="cred-item">
            <i class="fa-solid fa-school text-gold"></i>
            <span><strong>Senior Faculty</strong>, MVN Sector-17</span>
          </div>
          <div class="cred-item">
            <i class="fa-solid fa-hand-holding-heart text-gold"></i>
            <span><strong>Shiksha Sopan</strong> (Prof. H.C. Verma)</span>
          </div>
        </div>

        <div class="hero-cta-group">
          <a href="#book-demo" class="btn btn-primary btn-lg glow-btn">
            <i class="fa-solid fa-calendar-plus"></i> Book Free 1-on-1 Demo
          </a>
          <a href="https://wa.me/917567220274?text=Hello%20Er.%20Pankaj%20Kumar,%20I%20would%20like%20to%20know%20more%20about%20PrepPHY%20Physics%20classes." target="_blank" class="btn btn-whatsapp btn-lg">
            <i class="fa-brands fa-whatsapp"></i> WhatsApp: +91 75672 20274
          </a>
        </div>

        <!-- Trust Stats Counter -->
        <div class="hero-stats">
          <div class="stat-card">
            <span class="stat-number">11+</span>
            <span class="stat-label">Years Excellence</span>
          </div>
          <div class="stat-card">
            <span class="stat-number">AIR-4</span>
            <span class="stat-label">NEET Top Rank</span>
          </div>
          <div class="stat-card">
            <span class="stat-number">AIR-238</span>
            <span class="stat-label">JEE Main Rank</span>
          </div>
          <div class="stat-card">
            <span class="stat-number">15–20</span>
            <span class="stat-label">Max Batch Size</span>
          </div>
        </div>
      </div>

      <!-- Hero Visual / Portrait Card -->
      <div class="hero-visual">
        <div class="portrait-card-wrapper">
          <div class="portrait-glow"></div>
          <div class="portrait-card">
            <div class="portrait-image-box">
              <img src="{sir_suit}" alt="Er. Pankaj Kumar - IIT Kanpur Alumnus & Senior Physics Faculty" class="portrait-img" />
              <div class="image-gradient-overlay"></div>
            </div>
            
            <div class="portrait-caption">
              <div class="caption-header">
                <h3>Er. Pankaj Kumar</h3>
                <span class="caption-tag">IIT Kanpur Alumnus</span>
              </div>
              <p class="caption-role"><i class="fa-solid fa-chalkboard-user"></i> Senior Physics Faculty • MVN Sector-17, Faridabad</p>
              
              <div class="floating-badge badge-top-right">
                <i class="fa-solid fa-trophy text-gold"></i>
                <span>Mentor to AIR-4 NEET</span>
              </div>
              
              <div class="floating-badge badge-bottom-left">
                <i class="fa-solid fa-lightbulb text-gold"></i>
                <span>100% Conceptual Clarity</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Hall of Fame / Key Results Strip -->
  <section class="section results-section" id="results">
    <div class="container">
      <div class="section-header text-center">
        <span class="sub-heading"><i class="fa-solid fa-medal"></i> Hall of Fame</span>
        <h2 class="section-title">Proven National Ranks in NEET &amp; JEE Advanced</h2>
        <p class="section-subtitle">Real, verified national ranks produced through rigorous concept building and tailored examination strategy.</p>
      </div>

      <div class="results-grid">
        <!-- AIR 4 NEET -->
        <div class="rank-card rank-gold">
          <div class="rank-badge"><i class="fa-solid fa-crown"></i> ALL INDIA RANK</div>
          <div class="rank-number">AIR-4</div>
          <div class="rank-exam">NEET 2019</div>
          <p class="rank-inst"><i class="fa-solid fa-building-columns"></i> MVN School, Sector-17, Faridabad</p>
          <span class="rank-highlight">Among the institute's best-ever national medical ranks</span>
        </div>

        <!-- AIR 75 NEET -->
        <div class="rank-card rank-silver">
          <div class="rank-badge"><i class="fa-solid fa-medal"></i> ALL INDIA RANK</div>
          <div class="rank-number">AIR-75</div>
          <div class="rank-exam">NEET 2021</div>
          <p class="rank-inst"><i class="fa-solid fa-building-columns"></i> MVN School, Sector-17, Faridabad</p>
          <span class="rank-highlight">Top 100 All-India Medical Selection</span>
        </div>

        <!-- AIR 238 JEE MAIN -->
        <div class="rank-card rank-bronze">
          <div class="rank-badge"><i class="fa-solid fa-award"></i> ALL INDIA RANK</div>
          <div class="rank-number">AIR-238</div>
          <div class="rank-exam">JEE MAIN 2017</div>
          <p class="rank-inst"><i class="fa-solid fa-building-columns"></i> KCM World School, Palwal</p>
          <span class="rank-highlight">Top engineering score in the region</span>
        </div>

        <!-- AIR 490 JEE ADV -->
        <div class="rank-card rank-blue">
          <div class="rank-badge"><i class="fa-solid fa-star"></i> ALL INDIA RANK</div>
          <div class="rank-number">AIR-490</div>
          <div class="rank-exam">JEE ADVANCED 2017</div>
          <p class="rank-inst"><i class="fa-solid fa-building-columns"></i> KCM World School, Palwal</p>
          <span class="rank-highlight">Direct selection into premier IIT</span>
        </div>
      </div>

      <!-- Quote Banner -->
      <div class="quote-banner">
        <div class="quote-icon"><i class="fa-solid fa-quote-left"></i></div>
        <blockquote>
          “Physics is not just a subject, it’s a way of thinking. Let’s Think. Let’s Solve. Let’s Succeed Together.”
        </blockquote>
        <cite>— Er. Pankaj Kumar (B.Tech, IIT Kanpur)</cite>
      </div>
    </div>
  </section>

  <!-- About Er. Pankaj Kumar -->
  <section class="section about-section" id="about">
    <div class="container">
      <div class="section-header text-center">
        <span class="sub-heading"><i class="fa-solid fa-user-tie"></i> Meet Your Mentor</span>
        <h2 class="section-title">Er. Pankaj Kumar (B.Tech, IIT Kanpur)</h2>
        <p class="section-subtitle">11+ Years of Dedicated Mentorship, Curriculum Leadership &amp; Proven Competitive Excellence.</p>
      </div>

      <div class="about-grid">
        <div class="about-image-col">
          <div class="about-card-frame">
            <img src="{poster2}" alt="Pankaj Kumar - IIT Kanpur Mentor" class="about-poster-preview" />
            <div class="pedigree-card">
              <div class="pedigree-icon"><i class="fa-solid fa-building-columns"></i></div>
              <div>
                <strong>Indian Institute of Technology Kanpur</strong>
                <span>B.Tech Alumnus • Chemical Engineering (2011)</span>
              </div>
            </div>
          </div>
        </div>

        <div class="about-text-col">
          <h3 class="about-heading">“To transform the way students think, practice, and excel in Physics.”</h3>
          
          <p class="lead-p">
            I am <strong>Er. Pankaj Kumar</strong>, an IIT Kanpur graduate who discovered early on that teaching Physics is my life's true calling. Having secured <strong>AIR 1247 in IIT-JEE 2007</strong> and <strong>AIR 613 (State Rank 18) in AIEEE</strong>, I understand exactly what it takes to rise from a confused school student to a national top ranker.
          </p>

          <p>
            Over the past <strong>11+ years</strong>, I have served as Senior Physics Faculty at premier schools including <strong>MVN School, Sector-17, Faridabad</strong> (leading JEE Advanced &amp; NEET programs) and <strong>KCM World School</strong>. I also had the profound honour of serving as a volunteer tutor at <strong>Shiksha Sopan</strong>, the renowned educational initiative founded by <strong>Prof. H.C. Verma (author of Concepts of Physics)</strong> at IIT Kanpur. That experience cemented my belief in accessible, first-principles physics teaching.
          </p>

          <!-- 5 PrepPHY Pillars -->
          <div class="philosophy-boxes">
            <div class="ph-box">
              <div class="ph-icon"><i class="fa-solid fa-compass-drafting"></i></div>
              <div class="ph-text">
                <h5>1. Concept-First Approach</h5>
                <p>Build unshakeable fundamentals. Derivations and boundary conditions explained intuitively from real physical reality.</p>
              </div>
            </div>

            <div class="ph-box">
              <div class="ph-icon"><i class="fa-solid fa-bullseye"></i></div>
              <div class="ph-text">
                <h5>2. Rank-Oriented Training</h5>
                <p>Graded problem solving: NCERT &rarr; HC Verma &rarr; Previous 15 Years PYQs &rarr; Irodov / Advanced twists.</p>
              </div>
            </div>

            <div class="ph-box">
              <div class="ph-icon"><i class="fa-solid fa-clipboard-check"></i></div>
              <div class="ph-text">
                <h5>3. Test – Analyze – Improve</h5>
                <p>Weekly tests under real exam conditions. Mistakes are logged in an Error Diary and systematically resolved.</p>
              </div>
            </div>

            <div class="ph-box">
              <div class="ph-icon"><i class="fa-solid fa-users"></i></div>
              <div class="ph-text">
                <h5>4. Mentorship That Matters</h5>
                <p>Strictly capped small batches (15-20 students). Every student has direct access to Pankaj Sir for doubt clearing.</p>
              </div>
            </div>
          </div>

          <div class="about-action">
            <a href="#book-demo" class="btn btn-primary"><i class="fa-solid fa-calendar-check"></i> Book a Free Demo Session</a>
            <a href="tel:+917567220274" class="btn btn-outline"><i class="fa-solid fa-phone"></i> Call Directly: 75672 20274</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Programs & Courses Offered -->
  <section class="section courses-section" id="courses">
    <div class="container">
      <div class="section-header text-center">
        <span class="sub-heading"><i class="fa-solid fa-layer-group"></i> Structured Curriculum</span>
        <h2 class="section-title">Comprehensive Physics Programs (Class 8th to 12th)</h2>
        <p class="section-subtitle">Meticulously designed for foundation building in junior classes and high-yield rank generation for JEE &amp; NEET.</p>
      </div>

      <div class="courses-grid">
        <!-- Class 8 & 9 -->
        <div class="course-card">
          <div class="course-header">
            <span class="course-badge foundation">Foundation</span>
            <h3 class="course-title">Class VIII &amp; IX: Junior Foundation</h3>
            <span class="course-sub">CBSE / ICSE / Olympiads (NSEJS, PRMO)</span>
          </div>
          <div class="course-body">
            <p class="course-desc">Igniting genuine scientific curiosity through hands-on observations, intuitive mechanics, and essential math toolkits.</p>
            <ul class="course-features">
              <li><i class="fa-solid fa-check"></i> Motion, Force, Energy, Gravitation, Sound &amp; Light</li>
              <li><i class="fa-solid fa-check"></i> Foundational Vectors, Basic Graphs &amp; Algebraic Physics</li>
              <li><i class="fa-solid fa-check"></i> Early exposure to competitive problem solving</li>
              <li><i class="fa-solid fa-check"></i> 100% school exam &amp; Olympiad readiness</li>
            </ul>
          </div>
          <div class="course-footer">
            <div class="course-mode"><i class="fa-solid fa-users"></i> Max 15 Students</div>
            <a href="#book-demo" class="btn btn-sm btn-outline course-btn" onclick="prefillCourse('Class 8-9 Junior Foundation')">Inquire / Book Demo</a>
          </div>
        </div>

        <!-- Class 10 -->
        <div class="course-card">
          <div class="course-header">
            <span class="course-badge boards">Boards + Bridge</span>
            <h3 class="course-title">Class X: Senior Foundation &amp; Boards</h3>
            <span class="course-sub">100% Board Mastery + 11th JEE/NEET Bridge</span>
          </div>
          <div class="course-body">
            <p class="course-desc">Targeting 95%+ marks in Class 10 Board Examinations combined with a smooth bridge into Class 11 competitive Physics.</p>
            <ul class="course-features">
              <li><i class="fa-solid fa-check"></i> Complete Light, Electricity, Magnetism &amp; Energy sources</li>
              <li><i class="fa-solid fa-check"></i> Step-by-step CBSE/ICSE answer writing techniques</li>
              <li><i class="fa-solid fa-check"></i> Pre-11th Calculus &amp; Vector Algebra headstart</li>
              <li><i class="fa-solid fa-check"></i> NTSE &amp; Science Olympiad problem solving</li>
            </ul>
          </div>
          <div class="course-footer">
            <div class="course-mode"><i class="fa-solid fa-users"></i> Max 15 Students</div>
            <a href="#book-demo" class="btn btn-sm btn-outline course-btn" onclick="prefillCourse('Class 10 Senior Foundation')">Inquire / Book Demo</a>
          </div>
        </div>

        <!-- Class 11 -->
        <div class="course-card popular">
          <div class="popular-ribbon">Crucial Foundation</div>
          <div class="course-header">
            <span class="course-badge advanced">IIT-JEE &amp; NEET</span>
            <h3 class="course-title">Class XI: Core Mechanics &amp; Thermal</h3>
            <span class="course-sub">JEE (Main &amp; Adv.) / NEET-UG / CBSE</span>
          </div>
          <div class="course-body">
            <p class="course-desc">The backbone of competitive Physics. Overcoming the 11th-grade numerical hurdle through deep conceptual intuition.</p>
            <ul class="course-features">
              <li><i class="fa-solid fa-check"></i> Kinematics, NLM, Work-Energy &amp; Rotational Dynamics</li>
              <li><i class="fa-solid fa-check"></i> Gravitation, Fluid Mechanics &amp; Thermal Physics</li>
              <li><i class="fa-solid fa-check"></i> SHM, Oscillations &amp; Wave Mechanics</li>
              <li><i class="fa-solid fa-check"></i> Systematic HC Verma + 15-Year PYQs drill</li>
            </ul>
          </div>
          <div class="course-footer">
            <div class="course-mode"><i class="fa-solid fa-users"></i> Intensive Mentorship</div>
            <a href="#book-demo" class="btn btn-sm btn-primary course-btn" onclick="prefillCourse('Class 11 IIT-JEE & NEET Physics')">Inquire / Book Demo</a>
          </div>
        </div>

        <!-- Class 12 -->
        <div class="course-card popular">
          <div class="popular-ribbon">Rank Maximizer</div>
          <div class="course-header">
            <span class="course-badge rank">Rank Booster</span>
            <h3 class="course-title">Class XII: Electrodynamics &amp; Modern</h3>
            <span class="course-sub">JEE Adv / Main / NEET + 100% Board Score</span>
          </div>
          <div class="course-body">
            <p class="course-desc">High-scoring domains decoded. Dual focus on flawless board derivations and high-speed competitive numericals.</p>
            <ul class="course-features">
              <li><i class="fa-solid fa-check"></i> Electrostatics, Capacitors, Current &amp; Magnetism</li>
              <li><i class="fa-solid fa-check"></i> EMI, AC Circuits &amp; Ray/Wave Optics</li>
              <li><i class="fa-solid fa-check"></i> Modern Physics, Atoms, Nuclei &amp; Semiconductors</li>
              <li><i class="fa-solid fa-check"></i> Full Board Revision + Full-Length Mock Series</li>
            </ul>
          </div>
          <div class="course-footer">
            <div class="course-mode"><i class="fa-solid fa-users"></i> Intensive Mentorship</div>
            <a href="#book-demo" class="btn btn-sm btn-primary course-btn" onclick="prefillCourse('Class 12 Electrodynamics & Modern Physics')">Inquire / Book Demo</a>
          </div>
        </div>

        <!-- Target / Repeaters -->
        <div class="course-card">
          <div class="course-header">
            <span class="course-badge dropper">Target Batch</span>
            <h3 class="course-title">Droppers &amp; Repeaters: JEE / NEET</h3>
            <span class="course-sub">High-Speed Rank Turnaround Course</span>
          </div>
          <div class="course-body">
            <p class="course-desc">Designed for repeaters aiming for a massive rank boost. Focused on gap diagnosis, speed drills, and mock test analytics.</p>
            <ul class="course-features">
              <li><i class="fa-solid fa-check"></i> High-yield topic prioritization and speed drills</li>
              <li><i class="fa-solid fa-check"></i> Advanced multi-concept synthesis questions</li>
              <li><i class="fa-solid fa-check"></i> Elimination of negative marking &amp; exam anxiety</li>
              <li><i class="fa-solid fa-check"></i> Full-length timed mock tests with in-depth analysis</li>
            </ul>
          </div>
          <div class="course-footer">
            <div class="course-mode"><i class="fa-solid fa-bolt"></i> Fast-Track &amp; Targeted</div>
            <a href="#book-demo" class="btn btn-sm btn-outline course-btn" onclick="prefillCourse('Droppers / Repeaters Physics')">Inquire / Book Demo</a>
          </div>
        </div>

        <!-- Doubt Clinic -->
        <div class="course-card">
          <div class="course-header">
            <span class="course-badge testseries">1-on-1 Special</span>
            <h3 class="course-title">1-on-1 Doubt Clinic &amp; Test Series</h3>
            <span class="course-sub">Personalized Academic Intervention</span>
          </div>
          <div class="course-body">
            <p class="course-desc">Targeted doubt clearance and chapter-wise test series for students enrolled in schools or other institutes who need expert physics clarity.</p>
            <ul class="course-features">
              <li><i class="fa-solid fa-check"></i> 1-on-1 doubt resolution directly with Pankaj Sir</li>
              <li><i class="fa-solid fa-check"></i> Chapter-wise &amp; Part-syllabus rigorous mock tests</li>
              <li><i class="fa-solid fa-check"></i> Original formula revision sheets &amp; memory maps</li>
              <li><i class="fa-solid fa-check"></i> Exam temperament &amp; psychological mentoring</li>
            </ul>
          </div>
          <div class="course-footer">
            <div class="course-mode"><i class="fa-solid fa-calendar"></i> Flexible Timings</div>
            <a href="#book-demo" class="btn btn-sm btn-outline course-btn" onclick="prefillCourse('1-on-1 Doubt Clinic')">Inquire / Book Demo</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Study Material & Revision Sheets Showcase -->
  <section class="section materials-section" id="materials">
    <div class="container">
      <div class="section-header text-center">
        <span class="sub-heading"><i class="fa-solid fa-book-bookmark"></i> Authentic PrepPHY Material</span>
        <h2 class="section-title">Authored Study Material &amp; Revision Sheets</h2>
        <p class="section-subtitle">Original institute-grade summary sheets, memory maps, and high-yield PYQ corners designed by Er. Pankaj Kumar.</p>
      </div>

      <div class="material-spotlight">
        <div class="material-preview-col">
          <div class="sheet-image-card" onclick="openSheetModal()">
            <img src="{sheet_vector}" alt="Vector Complete Revision Sheet for JEE Main & Advanced by Pankaj Kumar" class="sheet-img" />
            <div class="sheet-hover-overlay">
              <i class="fa-solid fa-magnifying-glass-plus"></i>
              <span>Click to Zoom / Preview Vector Revision Sheet</span>
            </div>
          </div>
        </div>

        <div class="material-info-col">
          <span class="sheet-tag"><i class="fa-solid fa-star text-gold"></i> Sample Resource Preview</span>
          <h3>Vector Complete Revision Sheet (JEE Main + JEE Advanced)</h3>
          <p class="sheet-desc">
            Every PrepPHY chapter comes with a comprehensive 1-page master revision sheet that consolidates definitions, dot/cross products, scalar triple products, <strong>JEE Advanced Tricks</strong>, <strong>Common Mistakes</strong>, and <strong>PYQ Corners</strong> into a high-retention visual map.
          </p>

          <div class="sheet-highlights">
            <div class="sh-item"><i class="fa-solid fa-check text-success"></i> <strong>Resolution &amp; Position Vectors:</strong> Visual 3D geometry rules.</div>
            <div class="sh-item"><i class="fa-solid fa-check text-success"></i> <strong>BAC-CAB Rule:</strong> Vector triple product memory tricks.</div>
            <div class="sh-item"><i class="fa-solid fa-check text-success"></i> <strong>Fast Angle Finding:</strong> Symmetry and projection shortcuts.</div>
            <div class="sh-item"><i class="fa-solid fa-check text-success"></i> <strong>Memory Map:</strong> Complete chapter logic on a single page.</div>
          </div>

          <div class="sheet-cta-group">
            <button class="btn btn-primary" onclick="openSheetModal()"><i class="fa-solid fa-eye"></i> View Full Sheet</button>
            <a href="https://wa.me/917567220274?text=Hi%20Pankaj%20Sir,%20please%20send%20me%20the%20complete%20Vector%20Revision%20Sheet%20PDF." target="_blank" class="btn btn-whatsapp">
              <i class="fa-brands fa-whatsapp"></i> Request Free PDF on WhatsApp
            </a>
          </div>
        </div>
      </div>

      <!-- Poster Gallery Showcase -->
      <div class="posters-gallery">
        <div class="gallery-card" onclick="openPosterModal('{poster1}')">
          <img src="{poster1}" alt="PrepPHY Poster 1 - Concepts that Clarify" />
          <div class="gallery-caption">
            <strong>Concepts That Clarify • Practice That Strengthens</strong>
            <span>Click to expand full poster</span>
          </div>
        </div>
        <div class="gallery-card" onclick="openPosterModal('{poster2}')">
          <img src="{poster2}" alt="PrepPHY Poster 2 - 11+ Years of Teaching Excellence" />
          <div class="gallery-caption">
            <strong>11+ Years of Teaching Excellence • Pankaj Kumar</strong>
            <span>Click to expand full poster</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Physics Lab (Canvas Simulator) -->
  <section class="section simulator-section" id="simulator">
    <div class="container">
      <div class="section-header text-center">
        <span class="sub-heading"><i class="fa-solid fa-flask"></i> Interactive Learning Demo</span>
        <h2 class="section-title">Experience How We Learn: Interactive Physics Lab</h2>
        <p class="section-subtitle">Adjust parameters below and launch the projectile to see kinematics formulas visualized in real time!</p>
      </div>

      <div class="simulator-wrapper">
        <div class="sim-controls">
          <div class="sim-header">
            <h3><i class="fa-solid fa-bullseye"></i> 2D Projectile Motion Simulator</h3>
            <p>Adjust the parameters below and press <strong>Launch</strong> to simulate 2D kinematics.</p>
          </div>

          <div class="control-group">
            <div class="control-label">
              <span>Initial Velocity (v):</span>
              <strong id="velVal">45 m/s</strong>
            </div>
            <input type="range" id="velSlider" min="15" max="80" value="45" class="slider" />
          </div>

          <div class="control-group">
            <div class="control-label">
              <span>Launch Angle (&theta;):</span>
              <strong id="angleVal">45°</strong>
            </div>
            <input type="range" id="angleSlider" min="10" max="85" value="45" class="slider" />
          </div>

          <div class="control-group">
            <div class="control-label">
              <span>Environment Gravity (g):</span>
              <span class="env-name" id="gravityName">Earth (9.8 m/s²)</span>
            </div>
            <div class="gravity-buttons">
              <button class="btn-planet active" data-g="9.8" data-name="Earth (9.8 m/s²)">Earth</button>
              <button class="btn-planet" data-g="1.62" data-name="Moon (1.6 m/s²)">Moon</button>
              <button class="btn-planet" data-g="3.71" data-name="Mars (3.7 m/s²)">Mars</button>
              <button class="btn-planet" data-g="24.79" data-name="Jupiter (24.8 m/s²)">Jupiter</button>
            </div>
          </div>

          <div class="sim-actions">
            <button id="launchBtn" class="btn btn-primary glow-btn"><i class="fa-solid fa-play"></i> Launch Projectile</button>
            <button id="resetSimBtn" class="btn btn-outline"><i class="fa-solid fa-rotate-left"></i> Reset</button>
          </div>

          <!-- Formula Results Panel -->
          <div class="sim-readouts">
            <div class="readout-card">
              <span class="ro-label">Maximum Height (H_max)</span>
              <span class="ro-value" id="roMaxHeight">51.66 m</span>
              <span class="ro-formula">H = (v² sin²&theta;) / 2g</span>
            </div>
            <div class="readout-card">
              <span class="ro-label">Time of Flight (T)</span>
              <span class="ro-value" id="roTime">6.49 s</span>
              <span class="ro-formula">T = (2v sin&theta;) / g</span>
            </div>
            <div class="readout-card">
              <span class="ro-label">Horizontal Range (R)</span>
              <span class="ro-value" id="roRange">206.63 m</span>
              <span class="ro-formula">R = (v² sin 2&theta;) / g</span>
            </div>
          </div>
        </div>

        <div class="sim-canvas-container">
          <canvas id="projectileCanvas" width="700" height="420"></canvas>
          <div class="canvas-legend">
            <span><span class="legend-dot trajectory"></span> Trajectory</span>
            <span><span class="legend-dot vector"></span> Velocity Vector</span>
            <span><span class="legend-dot apex"></span> Apex Point (H_max)</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Demo Booking & Contact Section -->
  <section class="section contact-section" id="book-demo">
    <div class="container">
      <div class="contact-wrapper">
        <div class="contact-info-col">
          <span class="sub-heading"><i class="fa-solid fa-calendar-check"></i> Take the First Step</span>
          <h2 class="contact-title">Book a Free 1-on-1 Demo Session</h2>
          <p class="contact-desc">
            Experience the difference an <strong>IIT Kanpur alumnus</strong> makes to your child's physics mastery. Attend a complimentary 45-minute concept session with zero obligation.
          </p>

          <div class="direct-contact-cards">
            <a href="tel:+917567220274" class="dc-card">
              <div class="dc-icon"><i class="fa-solid fa-phone"></i></div>
              <div class="dc-text">
                <span class="dc-label">Call Directly</span>
                <span class="dc-val">+91 75672 20274</span>
              </div>
            </a>

            <a href="https://wa.me/917567220274?text=Hi%20Pankaj%20Sir,%20I%20would%20like%20to%20schedule%20a%20Free%20Demo%20Session%20for%20PrepPHY%20Physics." target="_blank" class="dc-card whatsapp-highlight">
              <div class="dc-icon"><i class="fa-brands fa-whatsapp"></i></div>
              <div class="dc-text">
                <span class="dc-label">Instant WhatsApp Chat</span>
                <span class="dc-val">+91 75672 20274</span>
              </div>
            </a>

            <div class="dc-card">
              <div class="dc-icon"><i class="fa-solid fa-location-dot"></i></div>
              <div class="dc-text">
                <span class="dc-label">Faridabad Centers</span>
                <span class="dc-val">Sector-91 &amp; Sector-17, Faridabad, Haryana (Offline + Live Online)</span>
              </div>
            </div>

            <div class="dc-card">
              <div class="dc-icon"><i class="fa-solid fa-envelope"></i></div>
              <div class="dc-text">
                <span class="dc-label">Official Emails</span>
                <span class="dc-val">pankajk.iitk@gmail.com • pnkj.kum@gmail.com</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Interactive Form -->
        <div class="contact-form-col">
          <div class="form-container">
            <div class="form-header">
              <h3>Schedule Free Demo / Consultation</h3>
              <p>Fill out the details below to connect directly with Er. Pankaj Kumar.</p>
            </div>

            <form id="demoForm">
              <div class="form-group">
                <label for="studentName"><i class="fa-solid fa-user"></i> Student's Full Name *</label>
                <input type="text" id="studentName" required placeholder="e.g. Aryan Sharma" />
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="parentContact"><i class="fa-solid fa-phone"></i> Mobile / WhatsApp *</label>
                  <input type="tel" id="parentContact" required placeholder="e.g. 98765 43210" />
                </div>
                <div class="form-group">
                  <label for="studentClass"><i class="fa-solid fa-school"></i> Current Class *</label>
                  <select id="studentClass" required>
                    <option value="">Select Class</option>
                    <option value="Class 8">Class VIII (8th)</option>
                    <option value="Class 9">Class IX (9th)</option>
                    <option value="Class 10">Class X (10th)</option>
                    <option value="Class 11">Class XI (11th)</option>
                    <option value="Class 12">Class XII (12th)</option>
                    <option value="Dropper / Repeater">Dropper / Repeater (12th Passed)</option>
                  </select>
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="targetExam"><i class="fa-solid fa-bullseye"></i> Primary Goal *</label>
                  <select id="targetExam" required>
                    <option value="IIT-JEE (Main + Advanced)">IIT-JEE (Main + Advanced)</option>
                    <option value="NEET-UG (Medical)">NEET-UG (Medical)</option>
                    <option value="CBSE / ICSE Board Mastery">CBSE / ICSE Board Mastery</option>
                    <option value="Foundation & Olympiad">Foundation &amp; Olympiad</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="learningMode"><i class="fa-solid fa-chalkboard"></i> Preferred Mode *</label>
                  <select id="learningMode" required>
                    <option value="Offline Batch (Faridabad)">Offline Batch (Faridabad)</option>
                    <option value="Interactive Live Online">Interactive Live Online</option>
                    <option value="Either / To be Decided">Either / To be Decided</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label for="userMessage"><i class="fa-solid fa-pen-to-square"></i> Any Specific Problem in Physics? (Optional)</label>
                <textarea id="userMessage" rows="3" placeholder="e.g. Facing difficulty in rotational motion and numerical speed..."></textarea>
              </div>

              <button type="submit" class="btn btn-primary btn-block glow-btn">
                <i class="fa-brands fa-whatsapp"></i> Confirm &amp; Send to Pankaj Sir
              </button>

              <p class="privacy-note"><i class="fa-solid fa-lock"></i> Your contact details remain 100% confidential. No spam.</p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Image Lightbox Modal for Vector Sheet & Posters -->
  <div id="imageModal" class="image-modal" onclick="closeImageModal()">
    <span class="modal-close">&times;</span>
    <img id="modalImg" class="modal-content" />
    <div id="modalCaption" class="modal-caption"></div>
  </div>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-container">
      <div class="footer-col brand-col">
        <div class="footer-brand-wrap">
          <img src="{logo_h}" alt="PrepPHY by Pankaj Kumar" class="footer-logo-img" />
        </div>
        <p class="footer-bio">
          <strong>PrepPHY</strong> — Where Conceptual Clarity Meets Competitive Success. Mentored by Er. Pankaj Kumar (B.Tech, IIT Kanpur • Senior Faculty, MVN Sector-17, Faridabad).
        </p>
        <div class="footer-socials">
          <a href="https://wa.me/917567220274" target="_blank" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
          <a href="tel:+917567220274" aria-label="Phone"><i class="fa-solid fa-phone"></i></a>
          <a href="mailto:pankajk.iitk@gmail.com" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
        </div>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About Er. Pankaj Kumar</a></li>
          <li><a href="#results">Hall of Fame</a></li>
          <li><a href="#courses">Courses (8th–12th)</a></li>
          <li><a href="#materials">Study Material</a></li>
          <li><a href="#simulator">Physics Simulator</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Programs</h4>
        <ul class="footer-links">
          <li><a href="#courses">Class 8 &amp; 9 Junior Foundation</a></li>
          <li><a href="#courses">Class 10 Board + Bridge</a></li>
          <li><a href="#courses">Class 11 JEE / NEET Mechanics</a></li>
          <li><a href="#courses">Class 12 Electrodynamics &amp; Modern</a></li>
          <li><a href="#courses">Dropper / Target JEE &amp; NEET</a></li>
          <li><a href="#courses">1-on-1 Doubt Clinic</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4 class="footer-heading">Faridabad Centers</h4>
        <ul class="footer-contact">
          <li><i class="fa-solid fa-location-dot"></i> Sector-91 &amp; Sector-17, Faridabad</li>
          <li><i class="fa-solid fa-phone"></i> <a href="tel:+917567220274">+91 75672 20274</a></li>
          <li><i class="fa-brands fa-whatsapp"></i> <a href="https://wa.me/917567220274" target="_blank">+91 75672 20274</a></li>
          <li><i class="fa-solid fa-envelope"></i> <a href="mailto:pankajk.iitk@gmail.com">pankajk.iitk@gmail.com</a></li>
          <li><i class="fa-solid fa-envelope"></i> <a href="mailto:pnkj.kum@gmail.com">pnkj.kum@gmail.com</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-content">
        <p>&copy; 2026 PrepPHY • Er. Pankaj Kumar (B.Tech, IIT Kanpur). All Rights Reserved.</p>
        <p class="footer-subtext">Physics for IIT-JEE (Main &amp; Advanced), NEET-UG, CBSE &amp; ICSE Boards in Faridabad.</p>
      </div>
    </div>
  </footer>

  <!-- Floating Quick Action Buttons -->
  <div class="floating-contact">
    <a href="https://wa.me/917567220274?text=Hi%20Pankaj%20Sir,%20I%20am%20interested%20in%20PrepPHY%20Physics%20classes." target="_blank" class="float-btn float-wa" aria-label="Chat on WhatsApp">
      <i class="fa-brands fa-whatsapp"></i>
      <span class="float-tooltip">Chat on WhatsApp</span>
    </a>
    <a href="tel:+917567220274" class="float-btn float-phone mobile-only" aria-label="Call Now">
      <i class="fa-solid fa-phone"></i>
    </a>
  </div>

  <script src="script.js"></script>
</body>
</html>'''

with open(r'C:\Users\HP\.gemini\antigravity\scratch\pankaj-kumar-physics\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Assembled and wrote updated index.html successfully!')
