import streamlit as st
import time
from datetime import datetime
import streamlit.components.v1 as components
import json

# ---------------------------
# CONFIG & INITIALIZATION
# ---------------------------
st.set_page_config(
    page_title="Ranjit Saroj - Cybersecurity Professional", 
    layout="wide", 
    page_icon="🔒",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/ranjit-dev-prog',
        'Report a bug': "https://github.com/ranjit-dev-prog",
        'About': "Professional Cybersecurity Portfolio by Ranjit Saroj"
    }
)

# Initialize session state
if 'page_loaded' not in st.session_state:
    st.session_state.page_loaded = False

# ---------------------------
# PURPLE CYBERSECURITY THEME CSS
# ---------------------------
def load_purple_cybersecurity_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&family=Orbitron:wght@400;500;600;700;800;900&display=swap');

    :root {
        --primary-dark: #0a0118;
        --secondary-dark: #1a0b2e;
        --tertiary-dark: #16213e;
        --purple-primary: #7c3aed;
        --purple-secondary: #a855f7;
        --purple-light: #c084fc;
        --pink-accent: #ec4899;
        --cyan-accent: #06b6d4;
        --gradient-primary: linear-gradient(135deg, #7c3aed 0%, #a855f7 50%, #ec4899 100%);
        --gradient-secondary: linear-gradient(135deg, #1a0b2e 0%, #16213e 100%);
        --gradient-card: linear-gradient(135deg, rgba(124, 58, 237, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%);
        --text-white: #ffffff;
        --text-light: #e2e8f0;
        --text-muted: #94a3b8;
        --glass-bg: rgba(255, 255, 255, 0.1);
        --glass-border: rgba(255, 255, 255, 0.2);
        --shadow-purple: 0 25px 50px rgba(124, 58, 237, 0.3);
        --shadow-glow: 0 0 30px rgba(124, 58, 237, 0.5);
        --shadow-card: 0 8px 32px rgba(0, 0, 0, 0.3);
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body, [class*="stApp"], .stApp {
        background: var(--primary-dark);
        color: var(--text-white);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        scroll-behavior: smooth;
        line-height: 1.6;
        overflow-x: hidden;
    }

    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;} 
    footer {visibility: hidden;} 
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    .stDecoration {display: none;}

    /* Animated Background */
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 80%, rgba(124, 58, 237, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(168, 85, 247, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(236, 72, 153, 0.2) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
        animation: backgroundShift 20s ease-in-out infinite;
    }

    @keyframes backgroundShift {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }

    @keyframes glow {
        0%, 100% { box-shadow: var(--shadow-glow); }
        50% { box-shadow: 0 0 60px rgba(124, 58, 237, 0.8); }
    }

    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(60px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Professional Header */
    .cybersecurity-header {
        background: rgba(26, 11, 46, 0.8);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid var(--glass-border);
        position: sticky;
        top: 0;
        z-index: 100;
        padding: 1rem 0;
    }

    .header-content {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .cyber-logo {
        font-family: 'Orbitron', monospace;
        font-size: 1.8rem;
        font-weight: 800;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-decoration: none;
        animation: glow 3s ease-in-out infinite;
    }

    .nav-menu {
        display: flex;
        gap: 2.5rem;
        align-items: center;
    }

    .nav-link {
        color: var(--text-light);
        text-decoration: none;
        font-weight: 500;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .nav-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: var(--gradient-primary);
        transition: left 0.3s ease;
        z-index: -1;
    }

    .nav-link:hover::before {
        left: 0;
    }

    .nav-link:hover {
        color: white;
        transform: translateY(-2px);
    }

    /* Hero Section */
    .cyber-hero {
        background: var(--gradient-secondary);
        padding: 8rem 2rem 6rem 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .hero-container {
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }

    .hero-badge {
        display: inline-block;
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        color: var(--purple-light);
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 3rem;
        animation: float 4s ease-in-out infinite;
    }

    .hero-title {
        font-family: 'Orbitron', monospace;
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 900;
        margin-bottom: 1.5rem;
        line-height: 1.1;
        animation: slideInUp 1s ease-out;
    }

    .hero-title .gradient-text {
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-subtitle {
        font-size: 1.5rem;
        color: var(--purple-light);
        margin-bottom: 2rem;
        font-weight: 600;
        animation: slideInUp 1s ease-out 0.2s both;
    }

    .hero-description {
        font-size: 1.2rem;
        color: var(--text-muted);
        max-width: 800px;
        margin: 0 auto 4rem auto;
        line-height: 1.8;
        animation: slideInUp 1s ease-out 0.4s both;
    }

    .cta-buttons {
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        flex-wrap: wrap;
        animation: slideInUp 1s ease-out 0.6s both;
    }

    .btn-cyber-primary {
        background: var(--gradient-primary);
        color: white;
        padding: 1.2rem 3rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        gap: 0.75rem;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-purple);
        border: none;
        cursor: pointer;
        font-size: 1.1rem;
    }

    .btn-cyber-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 35px 70px rgba(124, 58, 237, 0.4);
        color: white;
    }

    .btn-cyber-secondary {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        color: var(--text-white);
        padding: 1.2rem 3rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 0.75rem;
        border: 2px solid var(--glass-border);
        transition: all 0.3s ease;
        font-size: 1.1rem;
    }

    .btn-cyber-secondary:hover {
        border-color: var(--purple-primary);
        transform: translateY(-5px);
        box-shadow: var(--shadow-card);
        color: var(--text-white);
    }

    /* Floating Elements */
    .floating-elements {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: none;
        z-index: 1;
    }

    .floating-icon {
        position: absolute;
        color: var(--purple-light);
        opacity: 0.3;
        animation: float 6s ease-in-out infinite;
    }

    .floating-icon:nth-child(1) { top: 20%; left: 10%; animation-delay: 0s; font-size: 2rem; }
    .floating-icon:nth-child(2) { top: 60%; right: 15%; animation-delay: 2s; font-size: 1.5rem; }
    .floating-icon:nth-child(3) { bottom: 30%; left: 20%; animation-delay: 4s; font-size: 1.8rem; }

    /* Stats Section */
    .cyber-stats {
        background: var(--primary-dark);
        padding: 6rem 2rem;
        position: relative;
    }

    .stats-container {
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
    }

    .stat-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }

    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--gradient-primary);
    }

    .stat-card:hover {
        transform: translateY(-10px);
        box-shadow: var(--shadow-purple);
        border-color: var(--purple-primary);
    }

    .stat-icon {
        color: var(--purple-light);
        margin-bottom: 1.5rem;
    }

    .stat-number {
        font-family: 'Orbitron', monospace;
        font-size: 3rem;
        font-weight: 800;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }

    .stat-label {
        font-size: 1rem;
        color: var(--text-muted);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Section Styles */
    .cyber-section {
        padding: 6rem 2rem;
        max-width: 1400px;
        margin: 0 auto;
    }

    .section-header {
        text-align: center;
        margin-bottom: 5rem;
    }

    .section-title {
        font-family: 'Orbitron', monospace;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .section-subtitle {
        font-size: 1.2rem;
        color: var(--text-muted);
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.7;
    }

    /* Expertise Cards */
    .expertise-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 2.5rem;
        margin: 3rem 0;
    }

    .expertise-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 25px;
        padding: 3rem;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }

    .expertise-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, var(--purple-primary) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.4s ease;
        z-index: -1;
    }

    .expertise-card:hover::before {
        opacity: 0.1;
    }

    .expertise-card:hover {
        transform: translateY(-10px);
        box-shadow: var(--shadow-purple);
        border-color: var(--purple-primary);
    }

    .card-header {
        display: flex;
        align-items: center;
        gap: 1.5rem;
        margin-bottom: 2rem;
    }

    .card-icon {
        width: 70px;
        height: 70px;
        background: var(--gradient-primary);
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2rem;
        box-shadow: var(--shadow-glow);
    }

    .card-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-white);
    }

    .card-description {
        color: var(--text-muted);
        margin-bottom: 2rem;
        line-height: 1.7;
        font-size: 1.1rem;
    }

    .skill-list {
        list-style: none;
        padding: 0;
    }

    .skill-list li {
        padding: 0.75rem 0;
        color: var(--text-light);
        position: relative;
        padding-left: 2rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .skill-list li::before {
        content: '⚡';
        position: absolute;
        left: 0;
        color: var(--purple-light);
        font-size: 1.2rem;
    }

    .skill-list li:last-child {
        border-bottom: none;
    }

    /* Terminal Section */
    .cyber-terminal {
        background: var(--secondary-dark);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        margin: 4rem 0;
        overflow: hidden;
        box-shadow: var(--shadow-card);
    }

    .terminal-header {
        background: var(--tertiary-dark);
        padding: 1rem 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        border-bottom: 1px solid var(--glass-border);
    }

    .terminal-dot {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: #ff5f57;
    }

    .terminal-dot:nth-child(2) { background: #ffbd2e; }
    .terminal-dot:nth-child(3) { background: #28ca42; }

    .terminal-title {
        color: var(--text-muted);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        margin-left: 1rem;
    }

    .terminal-body {
        padding: 2rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.95rem;
        line-height: 1.8;
        background: linear-gradient(45deg, var(--secondary-dark) 0%, var(--tertiary-dark) 100%);
    }

    .terminal-line {
        margin-bottom: 1rem;
    }

    .terminal-prompt {
        color: var(--cyan-accent);
        font-weight: 600;
    }

    .terminal-command {
        color: var(--purple-light);
        font-weight: 500;
    }

    .terminal-output {
        color: var(--text-light);
        margin-left: 1.5rem;
        opacity: 0.9;
    }

    /* Experience Timeline */
    .timeline-container {
        max-width: 900px;
        margin: 0 auto;
    }

    .timeline-item {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        padding: 3rem;
        border-radius: 25px;
        border: 1px solid var(--glass-border);
        box-shadow: var(--shadow-card);
        position: relative;
        margin-bottom: 2rem;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: -2px;
        top: 0;
        bottom: 0;
        width: 6px;
        background: var(--gradient-primary);
        border-radius: 3px;
    }

    .timeline-header {
        margin-bottom: 2rem;
    }

    .timeline-role {
        font-family: 'Orbitron', monospace;
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--text-white);
        margin-bottom: 0.75rem;
    }

    .timeline-company {
        font-size: 1.2rem;
        color: var(--purple-light);
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .timeline-period {
        font-size: 0.95rem;
        color: var(--text-muted);
        background: var(--glass-bg);
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        display: inline-block;
        border: 1px solid var(--glass-border);
    }

    /* Skills Grid */
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }

    .skill-category {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        padding: 2.5rem;
        border-radius: 20px;
        border: 1px solid var(--glass-border);
        transition: all 0.3s ease;
    }

    .skill-category:hover {
        transform: translateY(-5px);
        border-color: var(--purple-primary);
        box-shadow: var(--shadow-card);
    }

    .skill-category-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--text-white);
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .skill-tag {
        background: var(--gradient-primary);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        cursor: default;
    }

    .skill-tag:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: var(--shadow-glow);
    }

    /* Contact Grid */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        max-width: 1000px;
        margin: 3rem auto 0;
    }

    .contact-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        text-align: center;
        padding: 3rem 2rem;
        border-radius: 25px;
        border: 1px solid var(--glass-border);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .contact-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: var(--gradient-primary);
        transition: left 0.3s ease;
        z-index: -1;
        opacity: 0.1;
    }

    .contact-card:hover::before {
        left: 0;
    }

    .contact-card:hover {
        transform: translateY(-8px);
        border-color: var(--purple-primary);
        box-shadow: var(--shadow-purple);
    }

    .contact-icon {
        width: 80px;
        height: 80px;
        background: var(--gradient-primary);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.5rem;
        font-size: 2rem;
        color: white;
        box-shadow: var(--shadow-glow);
    }

    .contact-title {
        font-family: 'Orbitron', monospace;
        font-size: 1.2rem;
        font-weight: 700;
        color: var(--text-white);
        margin-bottom: 1rem;
    }

    .contact-link {
        color: var(--purple-light);
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }

    .contact-link:hover {
        color: var(--text-white);
        text-shadow: 0 0 10px var(--purple-light);
    }

    /* Footer */
    .cyber-footer {
        background: var(--secondary-dark);
        padding: 4rem 2rem;
        border-top: 1px solid var(--glass-border);
        text-align: center;
        margin-top: 6rem;
    }

    .footer-content {
        max-width: 1400px;
        margin: 0 auto;
        color: var(--text-muted);
        font-size: 1.1rem;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .nav-menu {
            display: none;
        }
        
        .cyber-hero {
            padding: 6rem 1rem 4rem 1rem;
        }
        
        .cyber-section {
            padding: 4rem 1rem;
        }
        
        .expertise-grid {
            grid-template-columns: 1fr;
            gap: 2rem;
        }
        
        .expertise-card {
            padding: 2rem;
        }
        
        .cta-buttons {
            flex-direction: column;
            align-items: center;
        }
        
        .btn-cyber-primary, .btn-cyber-secondary {
            width: 100%;
            max-width: 350px;
            justify-content: center;
        }
        
        .stats-container {
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
        }
        
        .stat-card {
            padding: 2rem;
        }

        .skills-grid {
            grid-template-columns: 1fr;
        }

        .contact-grid {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 480px) {
        .stats-container {
            grid-template-columns: 1fr;
        }
        
        .hero-title {
            font-size: 3rem;
        }
        
        .section-title {
            font-size: 2rem;
        }

        .expertise-card, .stat-card, .contact-card {
            padding: 1.5rem;
        }
    }

    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: var(--primary-dark);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--gradient-primary);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--purple-secondary);
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------
# ENHANCED DATA STRUCTURE
# ---------------------------
portfolio_data = {
    "personal": {
        "name": "Ranjit Saroj",
        "title": "Cybersecurity Specialist",
        "subtitle": "SOC Operations | Vulnerability Assessment | Security Architecture",
        "location": "Mumbai, India",
        "phone": "+91 98674 70628",
        "email": "ranjitsaroj393@gmail.com",
        "github": "https://github.com/ranjit-dev-prog",
        "linkedin": "https://www.linkedin.com/in/ranjit-saroj-593786244/",
        "status": "Your trusted cybersecurity partner"
    },
    "stats": [
        {"number": "5+", "label": "Years Experience"},
        {"number": "50+", "label": "Security Assessments"},
        {"number": "15+", "label": "Tools Developed"},
        {"number": "100%", "label": "Success Rate"}
    ],
    "expertise": [
        {
            "icon": "🛡️",
            "title": "Security Operations Center (SOC)",
            "description": "Comprehensive security monitoring, incident response, and threat analysis with expertise in SIEM platforms and security orchestration.",
            "skills": [
                "24/7 Security Monitoring",
                "Incident Response & Analysis",
                "SIEM Implementation & Management",
                "Threat Intelligence Analysis",
                "Security Automation & Orchestration"
            ]
        },
        {
            "icon": "🔍",
            "title": "Vulnerability Assessment & Penetration Testing",
            "description": "Systematic evaluation of security weaknesses across applications, networks, and infrastructure with detailed remediation guidance.",
            "skills": [
                "Web Application Security Testing",
                "Network Infrastructure Assessment",
                "Cloud Security Evaluation",
                "Compliance Security Auditing",
                "Risk Assessment & Management"
            ]
        },
        {
            "icon": "⚙️",
            "title": "Security Tool Development",
            "description": "Custom security solutions and automation frameworks designed to enhance organizational security posture and operational efficiency.",
            "skills": [
                "Python Security Automation",
                "Custom Security Tools",
                "API Security Testing",
                "Automated Scanning Frameworks",
                "Security Reporting Solutions"
            ]
        }
    ],
    "experience": {
        "role": "Cybersecurity Specialist",
        "company": "Nexcore Alliance",
        "period": "July 2025 - Present",
        "achievements": [
            "Developed automated security tools reducing manual assessment time by 75%",
            "Conducted comprehensive security assessments for enterprise clients",
            "Implemented threat detection systems with improved accuracy",
            "Created detailed security reports with actionable recommendations",
            "Maintained 100% client satisfaction through effective communication and results"
        ]
    },
    "projects": [
        {
            "title": "Security Automation Framework",
            "description": "Comprehensive Python-based toolkit for automated security testing and vulnerability assessment.",
            "features": [
                "Automated port scanning and service detection",
                "Directory enumeration with intelligent wordlists",
                "Subdomain discovery and DNS analysis",
                "SSL/TLS certificate validation",
                "Comprehensive security reporting"
            ]
        },
        {
            "title": "Threat Detection System",
            "description": "Advanced monitoring solution for proactive threat identification and incident response.",
            "features": [
                "Real-time log analysis and correlation",
                "Behavioral anomaly detection",
                "Automated alert prioritization",
                "Integration with existing security tools",
                "Executive dashboard and reporting"
            ]
        },
        {
            "title": "Cloud Security Assessment Tool",
            "description": "Specialized framework for evaluating cloud infrastructure security and compliance.",
            "features": [
                "Multi-cloud environment scanning",
                "IAM configuration analysis",
                "Resource security evaluation",
                "Compliance framework mapping",
                "Automated remediation guidance"
            ]
        }
    ],
    "skills": {
        "technical": [
            "Python", "Bash", "PowerShell", "JavaScript", "SQL",
            "Linux/Unix", "Windows Server", "VMware", "Docker"
        ],
        "security_tools": [
            "Burp Suite", "Nmap", "Metasploit", "Wireshark", "Nessus",
            "OWASP ZAP", "OpenVAS", "Nuclei", "SQLMap", "Gobuster"
        ],
        "platforms": [
            "AWS", "Azure", "Google Cloud", "Splunk", "ELK Stack",
            "QRadar", "Sentinel", "CrowdStrike", "Rapid7"
        ],
        "certifications": [
            "CISSP (In Progress)", "CEH", "Security+", "CySA+",
            "GCIH", "AWS Security", "Azure Security"
        ]
    }
}

# ---------------------------
# COMPONENT FUNCTIONS
# ---------------------------
def create_header():
    """Create cybersecurity header with navigation"""
    st.markdown("""
    <div class="cybersecurity-header">
        <div class="header-content">
            <a href="#home" class="cyber-logo">RANJIT SAROJ</a>
            <nav class="nav-menu">
                <a href="#expertise" class="nav-link">Expertise</a>
                <a href="#experience" class="nav-link">Experience</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#contact" class="nav-link">Contact</a>
            </nav>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_hero_section():
    """Create cybersecurity hero section"""
    data = portfolio_data["personal"]
    
    st.markdown(f"""
    <div id="home" class="cyber-hero">
        <div class="floating-elements">
            <div class="floating-icon">🔒</div>
            <div class="floating-icon">🛡️</div>
            <div class="floating-icon">⚡</div>
        </div>
        
        <div class="hero-container">
            <div class="hero-badge">{data['status']}</div>
            
            <h1 class="hero-title">
                Safeguarding<br>
                your digital <span class="gradient-text">world</span>
            </h1>
            
            <p class="hero-subtitle">{data['subtitle']}</p>
            
            <p class="hero-description">
                We provide advanced security solutions to safeguard your business
                from cyber threats. Experienced cybersecurity professional specializing in security operations, 
                vulnerability assessment, and custom security tool development.
            </p>
            
            <div class="cta-buttons">
                <a href="mailto:{data['email']}" class="btn-cyber-primary">
                    Get a free consultation
                </a>
                <a href="{data['linkedin']}" class="btn-cyber-secondary" target="_blank">
                    View Portfolio
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_stats_section():
    """Create cybersecurity statistics section"""
    stats_html = ""
    for stat in portfolio_data["stats"]:
        stats_html += f"""
        <div class="stat-card">
            <div class="stat-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2L2 7v10c0 5.55 3.84 9.74 9 9 5.16.74 9-3.45 9-9V7l-10-5z"/>
                </svg>
            </div>
            <div class="stat-number">{stat['number']}</div>
            <div class="stat-label">{stat['label']}</div>
        </div>
        """
    
    st.markdown(f"""
    <div class="cyber-stats">
        <div class="stats-container">
            {stats_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_expertise_section():
    """Create expertise section with cybersecurity cards"""
    st.markdown("""
    <div id="expertise" class="cyber-section">
        <div class="section-header">
            <h2 class="section-title">Core Expertise</h2>
            <p class="section-subtitle">
                Comprehensive cybersecurity capabilities across security operations, assessment, and tool development
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    cards_html = ""
    for item in portfolio_data["expertise"]:
        skills_list = "".join([f"<li>{skill}</li>" for skill in item["skills"]])
        cards_html += f"""
        <div class="expertise-card">
            <div class="card-header">
                <div class="card-icon">{item['icon']}</div>
                <h3 class="card-title">{item['title']}</h3>
            </div>
            <p class="card-description">{item['description']}</p>
            <ul class="skill-list">
                {skills_list}
            </ul>
        </div>
        """
    
    st.markdown(f"""
        <div class="expertise-grid">
            {cards_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_terminal_section():
    """Create cybersecurity terminal showcase"""
    st.markdown("""
    <div class="cyber-terminal">
        <div class="terminal-header">
            <div class="terminal-dot"></div>
            <div class="terminal-dot"></div>
            <div class="terminal-dot"></div>
            <div class="terminal-title">security-operations@cyberlab</div>
        </div>
        <div class="terminal-body">
            <div class="terminal-line">
                <span class="terminal-prompt">ranjit@cyberlab:~$</span> 
                <span class="terminal-command">whoami</span>
            </div>
            <div class="terminal-output">Cybersecurity Specialist - SOC Operations & VAPT Expert</div>
            
            <div class="terminal-line">
                <span class="terminal-prompt">ranjit@cyberlab:~$</span> 
                <span class="terminal-command">cat /etc/skills.conf</span>
            </div>
            <div class="terminal-output">Python | Penetration Testing | Security Automation | Threat Analysis</div>
            
            <div class="terminal-line">
                <span class="terminal-prompt">ranjit@cyberlab:~$</span> 
                <span class="terminal-command">ls /projects/</span>
            </div>
            <div class="terminal-output">security-automation-suite/  threat-detection-system/  cloud-security-tools/</div>
            
            <div class="terminal-line">
                <span class="terminal-prompt">ranjit@cyberlab:~$</span> 
                <span class="terminal-command">systemctl status threat-monitoring</span>
            </div>
            <div class="terminal-output">● threat-monitoring.service - Active and monitoring cyber threats 24/7</div>
            
            <div class="terminal-line">
                <span class="terminal-prompt">ranjit@cyberlab:~$</span> 
                <span class="terminal-command">nmap -sC -sV target.com</span>
            </div>
            <div class="terminal-output">Starting Nmap scan... Vulnerability assessment in progress...</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_experience_section():
    """Create professional experience section"""
    exp = portfolio_data["experience"]
    achievements_list = "".join([f"<li>{achievement}</li>" for achievement in exp["achievements"]])
    
    st.markdown(f"""
    <div id="experience" class="cyber-section">
        <div class="section-header">
            <h2 class="section-title">Professional Experience</h2>
            <p class="section-subtitle">
                Proven track record in cybersecurity operations and client engagement
            </p>
        </div>
        
        <div class="timeline-container">
            <div class="timeline-item">
                <div class="timeline-header">
                    <h3 class="timeline-role">{exp['role']}</h3>
                    <div class="timeline-company">{exp['company']}</div>
                    <span class="timeline-period">{exp['period']}</span>
                </div>
                <ul class="skill-list">
                    {achievements_list}
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_projects_section():
    """Create projects section with cybersecurity cards"""
    st.markdown("""
    <div id="projects" class="cyber-section">
        <div class="section-header">
            <h2 class="section-title">Highlighted Projects</h2>
            <p class="section-subtitle">
                Key security tools and solutions designed and implemented for real-world challenges
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    cards_html = ""
    for project in portfolio_data["projects"]:
        features_list = "".join([f"<li>{feature}</li>" for feature in project["features"]])
        cards_html += f"""
        <div class="expertise-card">
            <div class="card-header">
                <div class="card-icon">💻</div>
                <h3 class="card-title">{project['title']}</h3>
            </div>
            <p class="card-description">{project['description']}</p>
            <ul class="skill-list">
                {features_list}
            </ul>
        </div>
        """
    
    st.markdown(f"""
        <div class="expertise-grid">
            {cards_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_skills_section():
    """Create skills section with cybersecurity tag grids"""
    skills = portfolio_data["skills"]
    
    st.markdown("""
    <div id="skills" class="cyber-section">
        <div class="section-header">
            <h2 class="section-title">Technical Arsenal</h2>
            <p class="section-subtitle">
                Core competencies in security tools, platforms, and professional certifications
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    categories = [
        {"title": "Technical Skills", "icon": "⚙️", "items": skills["technical"]},
        {"title": "Security Tools", "icon": "🛡️", "items": skills["security_tools"]},
        {"title": "Platforms & Cloud", "icon": "☁️", "items": skills["platforms"]},
        {"title": "Certifications", "icon": "📜", "items": skills["certifications"]}
    ]
    
    grid_html = ""
    for category in categories:
        tags_html = "".join([
            f'<span class="skill-tag">{item}</span>' for item in category["items"]
        ])
        grid_html += f"""
        <div class="skill-category">
            <h4 class="skill-category-title">
                <span>{category["icon"]}</span> {category["title"]}
            </h4>
            <div class="skill-tags">
                {tags_html}
            </div>
        </div>
        """
    
    st.markdown(f"""
        <div class="skills-grid">
            {grid_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_contact_section():
    """Create contact section with cybersecurity cards"""
    personal = portfolio_data["personal"]
    
    st.markdown("""
    <div id="contact" class="cyber-section">
        <div class="section-header">
            <h2 class="section-title">Get in Touch</h2>
            <p class="section-subtitle">
                Let's discuss how I can help strengthen your security posture
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    cards_html = f"""
    <div class="contact-card">
        <div class="contact-icon">📍</div>
        <h4 class="contact-title">Location</h4>
        <p>{personal["location"]}</p>
    </div>
    <div class="contact-card">
        <div class="contact-icon">📞</div>
        <h4 class="contact-title">Phone</h4>
        <a href="tel:{personal["phone"]}" class="contact-link">{personal["phone"]}</a>
    </div>
    <div class="contact-card">
        <div class="contact-icon">✉️</div>
        <h4 class="contact-title">Email</h4>
        <a href="mailto:{personal["email"]}" class="contact-link">{personal["email"]}</a>
    </div>
    <div class="contact-card">
        <div class="contact-icon">🔗</div>
        <h4 class="contact-title">LinkedIn</h4>
        <a href="{personal["linkedin"]}" class="contact-link" target="_blank">View Profile</a>
    </div>
    <div class="contact-card">
        <div class="contact-icon">💻</div>
        <h4 class="contact-title">GitHub</h4>
        <a href="{personal["github"]}" class="contact-link" target="_blank">View Repositories</a>
    </div>
    """
    
    st.markdown(f"""
        <div class="contact-grid">
            {cards_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_footer():
    """Create cybersecurity footer"""
    current_year = datetime.now().year
    st.markdown(f"""
    <footer class="cyber-footer">
        <div class="footer-content">
            <p>© {current_year} Ranjit Saroj. All rights reserved. | Safeguarding Digital Worlds | Built with Streamlit</p>
            <p style="margin-top: 1rem; opacity: 0.8;">🛡️ Cybersecurity Professional | SOC Operations | Penetration Testing | Security Automation</p>
        </div>
    </footer>
    """, unsafe_allow_html=True)

# ---------------------------
# MAIN APPLICATION
# ---------------------------
if __name__ == "__main__":
    load_purple_cybersecurity_css()
    create_header()
    create_hero_section()
    create_stats_section()
    create_expertise_section()
    create_terminal_section()
    create_experience_section()
    create_projects_section()
    create_skills_section()
    create_contact_section()
    create_footer()
