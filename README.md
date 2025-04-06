## Hi there 👋

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>پروفایل تخصصی هوش مصنوعی</title>
    <style>
        :root {
            --primary: #6e48aa;
            --secondary: #9d50bb;
            --dark: #1a1a2e;
            --light: #f1f1f1;
            --success: #4CAF50;
            --info: #2196F3;
            --warning: #ff9800;
            --danger: #f44336;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        
        .header {
            text-align: center;
            padding: 40px 0;
            background: linear-gradient(to right, var(--primary), var(--secondary));
            color: white;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .section {
            background: white;
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 25px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        .skills-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }
        
        .skill-card {
            background: white;
            border-radius: 8px;
            padding: 15px;
            display: flex;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .skill-card:hover {
            transform: translateY(-5px);
        }
        
        .skill-icon {
            width: 40px;
            height: 40px;
            margin-right: 15px;
        }
        
        .progress-container {
            width: 100%;
            background-color: #f1f1f1;
            border-radius: 5px;
            margin: 10px 0;
        }
        
        .progress-bar {
            height: 20px;
            border-radius: 5px;
            color: white;
            text-align: center;
            line-height: 20px;
        }
        
        h1, h2, h3 {
            color: var(--primary);
        }
        
        .badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            margin-right: 5px;
            margin-bottom: 5px;
        }
        
        .ml-badge { background: var(--primary); color: white; }
        .dl-badge { background: var(--secondary); color: white; }
        .cv-badge { background: var(--info); color: white; }
        .nlp-badge { background: var(--success); color: white; }
    </style>
</head>
<body>
    <div class="header">
        <h1>سید محمد حسین علم الهدی</h1>
        <h2>متخصص یادگیری ماشین و شبکه‌های عصبی</h2>
        <p>توسعه‌دهنده هوش مصنوعی | پژوهشگر یادگیری عمیق | مدرس</p>
    </div>
    
    <div class="section">
        <h2>🛠️ مهارت‌های تخصصی</h2>
        <div class="skills-container">
            <div class="skill-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" class="skill-icon" alt="Python">
                <div>
                    <h3>Python</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 95%; background-color: #3776AB;">95%</div>
                    </div>
                </div>
            </div>
            
            <div class="skill-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/1200px-Tensorflow_logo.svg.png" class="skill-icon" alt="TensorFlow">
                <div>
                    <h3>TensorFlow</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 90%; background-color: #FF6F00;">90%</div>
                    </div>
                </div>
            </div>
            
            <div class="skill-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" class="skill-icon" alt="Keras">
                <div>
                    <h3>Keras</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 88%; background-color: #D00000;">88%</div>
                    </div>
                </div>
            </div>
            
            <div class="skill-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" class="skill-icon" alt="Scikit-learn">
                <div>
                    <h3>Scikit-learn</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 85%; background-color: #F7931E;">85%</div>
                    </div>
                </div>
            </div>
            
            <div class="skill-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/NumPy_logo.svg/1200px-NumPy_logo.svg.png" class="skill-icon" alt="NumPy">
                <div>
                    <h3>NumPy</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 92%; background-color: #4D77CF;">92%</div>
                    </div>
                </div>
            </div>
            
            <div class="skill-card">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" class="skill-icon" alt="Pandas">
                <div>
                    <h3>Pandas</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 90%; background-color: #150458;">90%</div>
                    </div>
                </div>
            </div>
            
            <div class="skill-card">
                <img src="https://matplotlib.org/stable/_static/images/logo2.svg" class="skill-icon" alt="Matplotlib">
                <div>
                    <h3>Matplotlib</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 87%; background-color: #11557C;">87%</div>
                    </div>
                </div>
            </div>
            
            <div class="skill-card">
                <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" class="skill-icon" alt="Seaborn">
                <div>
                    <h3>Seaborn</h3>
                    <div class="progress-container">
                        <div class="progress-bar" style="width: 83%; background-color: #5B8AC6;">83%</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="section">
        <h2>🧠 تخصص‌های هوش مصنوعی</h2>
        <div style="margin-top: 20px;">
            <span class="badge ml-badge">یادگیری ماشین</span>
            <span class="badge dl-badge">یادگیری عمیق</span>
            <span class="badge cv-badge">بینایی کامپیوتر</span>
            <span class="badge nlp-badge">پردازش زبان طبیعی</span>
        </div>
        
        <div style="margin-top: 25px;">
            <h3>شبکه‌های عصبی</h3>
            <ul>
                <li>شبکه‌های عصبی کانولوشنی (CNN) برای پردازش تصویر</li>
                <li>شبکه‌های عصبی بازگشتی (RNN/LSTM) برای داده‌های سری زمانی</li>
                <li>مبدل‌ها (Transformers) برای پردازش زبان طبیعی</li>
                <li>شبکه‌های مولد تخاصمی (GAN) برای تولید داده‌های مصنوعی</li>
            </ul>
        </div>
    </div>
    
    <div class="section">
        <h2>📚 پروژه‌های برجسته</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; margin-top: 20px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3>تشخیص اشیا در تصاویر</h3>
                <p>سیستم تشخیص اشیا با دقت 95% با استفاده از YOLOv5</p>
                <div style="display: flex; flex-wrap: wrap; margin-top: 10px;">
                    <span style="background: #FF6F00; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px; margin-bottom: 5px;">TensorFlow</span>
                    <span style="background: #3776AB; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px; margin-bottom: 5px;">OpenCV</span>
                </div>
            </div>
            
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3>دسته‌بندی متن هوشمند</h3>
                <p>سیستم طبقه‌بندی خودکار متون با استفاده از BERT</p>
                <div style="display: flex; flex-wrap: wrap; margin-top: 10px;">
                    <span style="background: #FFD700; color: black; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px; margin-bottom: 5px;">PyTorch</span>
                    <span style="background: #4B8BBE; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px; margin-bottom: 5px;">Transformers</span>
                </div>
            </div>
        </div>
    </div>
    
    <div class="section" style="text-align: center; padding: 20px; background: linear-gradient(to right, var(--primary), var(--secondary)); color: white; border-radius: 10px;">
        <h2>📞 تماس با من</h2>
        <p>برای همکاری در پروژه‌های هوش مصنوعی و یادگیری ماشین می‌توانید با من در ارتباط باشید</p>
        <div style="margin-top: 15px;">
            <a href="mailto:your.email@example.com" style="color: white; margin: 0 10px;">📧 ایمیل</a>
            <a href="https://linkedin.com/in/yourprofile" style="color: white; margin: 0 10px;">🔗 لینکدین</a>
            <a href="https://github.com/yourusername" style="color: white; margin: 0 10px;">🐱 گیت‌هاب</a>
        </div>
    </div>
</body>
</html>
