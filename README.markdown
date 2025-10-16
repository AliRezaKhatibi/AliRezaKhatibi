<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>👋 Welcome to My AI & Data Science Universe</title>
  <meta name="description" content="Data Scientist & AI Innovator — Portfolio landing section with skills, projects, and contact links." />
  <style>
    :root{
      --bg1:#e6e9f0;
      --bg2:#eef1f5;
      --brand:#4a2a9f;
      --text:#2d2d2d;
      --muted:#555;
      --card:#ffffff;
      --shadow:0 6px 24px rgba(0,0,0,.15);
      --shadow-sm:0 3px 10px rgba(0,0,0,.1);
      --shadow-hover:0 8px 16px rgba(0,0,0,.2);
      --radius-lg:16px;
      --radius-md:12px;
      --radius-sm:10px;
      --trans:all .3s ease;
      --gutter:20px;
      --maxw:1000px;
    }

    /* Base */
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color:var(--text);
      background:linear-gradient(135deg,var(--bg1) 0%, var(--bg2) 100%);
    }
    a{color:inherit}
    img{max-width:100%;height:auto;display:inline-block}

    /* Container */
    .shell{
      max-width:var(--maxw);
      margin:0 auto;
      padding:40px 20px;
    }
    .panel{
      background:#fff0; /* for gradient background beneath */
      border-radius:var(--radius-lg);
      box-shadow:var(--shadow);
      position:relative;
      overflow:hidden;
      padding:0;
    }
    .panel__inner{
      padding:40px;
      background:transparent;
    }
    .soft-bg{
      position:absolute; inset:0;
      background:linear-gradient(135deg,var(--bg1) 0%, var(--bg2) 100%);
      z-index:-2;
    }

    /* Header */
    .hdr{
      text-align:center;
      margin-bottom:50px;
      position:relative;
      padding-top:20px;
    }
    .hdr__particles{
      position:absolute; inset:0;
      background:url("https://media.giphy.com/media/l4KibWpBGWZN4WykE/giphy.gif") center/cover no-repeat;
      opacity:.10; z-index:-1;
    }
    .hdr__wave{
      width:140px; margin:0 auto 16px;
      filter:drop-shadow(0 3px 6px rgba(0,0,0,.3));
      animation:float 4s ease-in-out infinite;
    }
    .title{
      color:var(--brand);
      font-size:2.4rem;
      margin:0;
      text-transform:uppercase;
      letter-spacing:2px;
      animation:neonGlow 1.5s ease-in-out infinite alternate;
    }
    .subtitle{
      color:var(--muted);
      font-size:1.05rem;
      margin-top:12px;
      font-weight:400;
    }
    .cta{
      display:inline-block;
      margin-top:16px;
      padding:10px 20px;
      background:var(--brand);
      color:#fff;
      text-decoration:none;
      border-radius:25px;
      transition:var(--trans);
    }
    .cta:hover{transform:scale(1.06); background:#6e48aa}

    /* Cards / blocks */
    .block{
      background:var(--card);
      padding:25px;
      border-radius:var(--radius-md);
      box-shadow:var(--shadow-sm);
      margin-bottom:50px;
    }
    .h2{
      color:var(--brand);
      font-size:1.6rem;
      border-bottom:3px solid #e0e0e0;
      padding-bottom:10px;
      display:flex; align-items:center; gap:10px;
      margin:0 0 16px;
    }
    .grid{
      display:grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap:var(--gutter);
      margin-top:20px;
    }
    .skill, .tool{
      background:#fff;
      padding:15px;
      border-radius:var(--radius-sm);
      display:flex; align-items:center; gap:12px;
      transition:var(--trans);
      box-shadow:var(--shadow-sm);
      transform:translateY(0);
    }
    .skill:hover, .tool:hover{
      transform:translateY(-6px);
      box-shadow:var(--shadow-hover);
    }
    .spin{ animation:rotate 5s linear infinite }

    /* Expertise list */
    .expertise{ padding-left:22px; font-size:1.05rem; color:#333; line-height:1.7; margin:0 }
    .expertise li{ margin:.4rem 0; animation:slideIn 0.8s ease-out both }
    .expertise li:nth-child(1){animation-delay:0s}
    .expertise li:nth-child(2){animation-delay:.1s}
    .expertise li:nth-child(3){animation-delay:.2s}
    .expertise li:nth-child(4){animation-delay:.3s}
    .expertise li:nth-child(5){animation-delay:.4s}
    .expertise li:nth-child(6){animation-delay:.5s}
    .expertise li:nth-child(7){animation-delay:.6s}

    /* Featured projects */
    .projects{
      text-align:center;
      padding:30px;
      border-radius:var(--radius-md);
      box-shadow:var(--shadow-sm);
      background:#ffffff;
      margin-bottom:50px;
    }
    .projects__wrap{
      display:flex; justify-content:center; flex-wrap:wrap; gap:25px;
    }
    .card{
      background:#f9f9f9; padding:20px; border-radius:10px; width:240px;
      transition:var(--trans); box-shadow:var(--shadow-sm);
      transform:translateY(0);
    }
    .card:hover{ transform:translateY(-6px); box-shadow:var(--shadow-hover) }
    .card img{ border-radius:8px; margin-bottom:12px }

    /* Contact */
    .contact{ text-align:center; margin-bottom:30px }
    .contact__icons{ display:flex; justify-content:center; gap:20px }
    .icon-link{ display:inline-block; transition:transform .3s ease }
    .icon-link:hover{ transform:scale(1.1) }

    /* Animations */
    @keyframes neonGlow{
      0%{ text-shadow:0 0 5px rgba(74,42,159,.4), 0 0 10px rgba(74,42,159,.6) }
      100%{ text-shadow:0 0 10px rgba(74,42,159,.8), 0 0 20px rgba(74,42,159,1) }
    }
    @keyframes rotate{ from{transform:rotate(0)} to{transform:rotate(360deg)} }
    @keyframes slideIn{ from{opacity:0; transform:translateX(-30px)} to{opacity:1; transform:translateX(0)} }
    @keyframes float{ 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }

    /* Reduced motion for accessibility */
    @media (prefers-reduced-motion: reduce){
      .spin, .hdr__wave, .title, .expertise li{ animation:none !important }
      .cta, .skill, .tool, .card{ transition:none !important }
    }

    /* Small screens */
    @media (max-width:600px){
      .panel__inner{ padding:24px }
      .title{ font-size:1.9rem }
    }
  </style>
</head>
<body>
  <div class="shell">
    <div class="panel">
      <div class="soft-bg" aria-hidden="true"></div>
      <div class="panel__inner">
        <!-- Header -->
        <header class="hdr" role="banner">
          <div class="hdr__particles" aria-hidden="true"></div>
          <img class="hdr__wave" src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" alt="Waving hand" width="140" height="140" />
          <h1 class="title">Data Scientist &amp; AI Innovator</h1>
          <p class="subtitle">
            <img src="https://media.giphy.com/media/LMt9638dO8dftAjtco/giphy.gif" alt="" width="28" height="28" style="vertical-align:middle;margin-right:8px" />
            Pioneering AI Solutions | Computer Vision | Data-Driven Insights
          </p>
          <!-- TODO: replace your-username with your GitHub handle -->
          <a class="cta" href="https://github.com/your-username" rel="noopener">Explore My Work</a>
        </header>

        <!-- About -->
        <section class="block" aria-labelledby="about">
          <h2 id="about" class="h2">
            <img src="https://media.giphy.com/media/26tPplGWjN0xLybiU/giphy.gif" alt="" width="32" height="32" />
            About Me
          </h2>
          <p style="color:#333; line-height:1.7; font-size:1.05rem; margin:0">
            I'm a passionate Data Scientist and AI enthusiast with expertise in <strong>Machine Learning</strong>, <strong>Deep Learning</strong>, and <strong>Data Engineering</strong>. I transform complex datasets into actionable insights and build scalable AI solutions for real-world problems—from predictive modeling to computer vision and NLP.
          </p>
        </section>

        <!-- Core Skills -->
        <section aria-labelledby="skills" style="margin-bottom:50px">
          <h2 id="skills" class="h2">
            <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" alt="" width="32" height="32" />
            Core Skills
          </h2>
          <div class="grid" aria-label="Skill badges">
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="32" height="32" alt="Python" /><span>Python</span></div>
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg" width="32" height="32" alt="R" /><span>R</span></div>
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" width="32" height="32" alt="TensorFlow" /><span>TensorFlow</span></div>
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" width="32" height="32" alt="PyTorch" /><span>PyTorch</span></div>
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="32" height="32" alt="NumPy" /><span>NumPy</span></div>
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="32" height="32" alt="Pandas" /><span>Pandas</span></div>
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" width="32" height="32" alt="OpenCV" /><span>OpenCV</span></div>
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg" width="32" height="32" alt="Scikit-Learn" /><span>Scikit-Learn</span></div>
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="32" height="32" alt="Docker" /><span>Docker</span></div>
            <!-- AWS icon: use wordmark variant (exists on Devicon CDN) -->
            <div class="skill"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" width="32" height="32" alt="Amazon Web Services" /><span>AWS</span></div>
          </div>
        </section>

        <!-- Expertise -->
        <section aria-labelledby="expertise" style="margin-bottom:50px">
          <h2 id="expertise" class="h2">
            <img src="https://media.giphy.com/media/RbDKaczqWovIugyJmW/giphy.gif" alt="" width="32" height="32" />
            Data Science &amp; AI Expertise
          </h2>
          <ul class="expertise">
            <li><strong>Deep Neural Networks</strong>: CNNs, RNNs/LSTMs, Transformers برای تصویر، سری زمانی و مولدها.</li>
            <li><strong>Computer Vision</strong>: YOLO/SSD، U-Net/Mask R-CNN، Face ID، GANs.</li>
            <li><strong>NLP</strong>: Sentiment، Chatbots، ترجمه با BERT/GPT.</li>
            <li><strong>Predictive Modeling</strong>: رگرسیون/طبقه‌بندی/خوشه‌بندی و Ensembleها.</li>
            <li><strong>Data Engineering</strong>: ETL، پاک‌سازی، Spark/Airflow/SQL.</li>
            <li><strong>Optimization &amp; Deployment</strong>: TensorRT/ONNX، Docker/K8s، AWS/GCP.</li>
            <li><strong>Big Data &amp; BI</strong>: Hadoop/Spark، Tableau/Power BI.</li>
          </ul>
        </section>

        <!-- Projects -->
        <section class="projects" aria-labelledby="projects">
          <h3 id="projects" class="h2" style="border:0; justify-content:center">
            <img src="https://media.giphy.com/media/IauL6LvGNlT3ffhcqq/giphy.gif" alt="" width="32" height="32" />
            Featured Projects
          </h3>
          <div class="projects__wrap">
            <article class="card">
              <img src="https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif" alt="Image Classifier preview" width="140" height="140" loading="lazy" />
              <p style="margin:0; font-weight:600; color:#333">Image Classifier</p>
              <p style="margin:6px 0 0; font-size:.9rem; color:#666">CNN با دقت 95%+ روی 10 دسته.</p>
              <a href="https://github.com/your-username/image-classifier" style="display:inline-block; margin-top:10px; color:var(--brand); text-decoration:none; font-weight:500" rel="noopener">View Project</a>
            </article>
            <article class="card">
              <img src="https://media.giphy.com/media/Ll22OhMLAlVDb8UQWe/giphy.gif" alt="Object Detection preview" width="140" height="140" loading="lazy" />
              <p style="margin:0; font-weight:600; color:#333">Object Detection</p>
              <p style="margin:6px 0 0; font-size:.9rem; color:#666">تشخیص آنی با YOLOv5 برای خودران.</p>
              <a href="https://github.com/your-username/object-detection" style="display:inline-block; margin-top:10px; color:var(--brand); text-decoration:none; font-weight:500" rel="noopener">View Project</a>
            </article>
            <article class="card">
              <img src="https://media.giphy.com/media/3o7TKsQ8k8b3oH6zC8/giphy.gif" alt="Sentiment Analysis preview" width="140" height="140" loading="lazy" />
              <p style="margin:0; font-weight:600; color:#333">Sentiment Analysis</p>
              <p style="margin:6px 0 0; font-size:.9rem; color:#666">تحلیل احساسات شبکه‌های اجتماعی با BERT.</p>
              <a href="https://github.com/your-username/sentiment-analysis" style="display:inline-block; margin-top:10px; color:var(--brand); text-decoration:none; font-weight:500" rel="noopener">View Project</a>
            </article>
          </div>
        </section>

        <!-- Tools -->
        <section aria-labelledby="tools" style="margin-bottom:50px">
          <h2 id="tools" class="h2">
            <img src="https://media.giphy.com/media/3o6Zta4k8b7F8zZ6Te/giphy.gif" alt="" width="32" height="32" />
            Tools &amp; Platforms
          </h2>
          <div class="grid" aria-label="Tool badges">
            <div class="tool"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="32" height="32" alt="Jupyter" /><span>Jupyter</span></div>
            <div class="tool"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="32" height="32" alt="MySQL / SQL" /><span>SQL</span></div>
            <div class="tool"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="32" height="32" alt="Git" /><span>Git</span></div>
            <div class="tool"><img class="spin" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg" width="32" height="32" alt="Kubernetes" /><span>Kubernetes</span></div>
          </div>
        </section>

        <!-- Contact -->
        <section class="contact" aria-labelledby="contact">
          <h3 id="contact" class="h2" style="border:0; margin-bottom:16px">
            <img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" alt="" width="32" height="32" />
            Connect with Me
          </h3>
          <div class="contact__icons">
            <!-- TODO: replace with your real profiles -->
            <a class="icon-link" href="https://linkedin.com/in/your-profile" aria-label="LinkedIn" rel="noopener">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="40" height="40" alt="LinkedIn" loading="lazy" />
            </a>
            <a class="icon-link" href="https://twitter.com/your-profile" aria-label="Twitter" rel="noopener">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/twitter/twitter-original.svg" width="40" height="40" alt="Twitter" loading="lazy" />
            </a>
            <a class="icon-link" href="mailto:your-email@example.com" aria-label="Email">
              <img src="https://media.giphy.com/media/3o7bu8sRnYp0kAvaA0/giphy.gif" width="40" height="40" alt="Email" loading="lazy" />
            </a>
          </div>
        </section>
      </div>
    </div>
  </div>
</body>
</html>
