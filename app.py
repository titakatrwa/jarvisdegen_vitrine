import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Configuration de la page Streamlit
st.set_page_config(
    page_title="JARVISDEGEN | $JDEGEN on Solana",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_image_base64_explicit(path, forced_format=None):
    """
    Lit un fichier image local et le convertit en chaîne Base64.
    Recherche automatique du chemin relatif et absolu.
    """
    # 1. Vérification si le chemin existe tel quel
    target_path = path
    if not os.path.exists(target_path):
        # 2. Sinon, recherche par rapport au dossier du script courant
        base_dir = os.path.dirname(os.path.abspath(__file__))
        target_path = os.path.join(base_dir, path)

    if os.path.exists(target_path):
        # Détermination du format d'image (png, jpeg, etc.)
        if forced_format:
            img_format = forced_format
        else:
            ext = os.path.splitext(target_path)[1].lower().replace('.', '')
            img_format = 'jpeg' if ext in ['jpg', 'jpeg'] else 'png'

        with open(target_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/{img_format};base64,{encoded}"
            
    # Retourne une chaîne vide si l'image n'est pas trouvée
    return ""

# Chargement sécurisé avec types MIME explicitement définis
logo_b64 = get_image_base64_explicit("static/logo.png", forced_format="png")
hero_b64 = get_image_base64_explicit("static/hero.jpg", forced_format="jpeg")
bras_b64 = get_image_base64_explicit("static/bras_croisees.png", forced_format="png")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

HTML_TEMPLATE = f"""
<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JARVISDEGEN | $JDEGEN on Solana</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@600;800;900&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        void: '#070c14',
                        cardBg: 'rgba(15, 25, 42, 0.75)',
                        cyanNeon: '#00f0ff',
                        aquaNeon: '#00fcc2',
                        profitGreen: '#c0ff6b',
                        riskRed: '#ff4d4d',
                        burnOrange: '#ff6b00',
                    }},
                    fontFamily: {{
                        orbitron: ['Orbitron', 'sans-serif'],
                        rajdhani: ['Rajdhani', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        body {{
            background-color: #070c14;
            color: #e6f1ff;
            background-image: 
                radial-gradient(circle at 15% 20%, rgba(0, 240, 255, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 85% 60%, rgba(0, 252, 194, 0.05) 0%, transparent 40%);
        }}
        .glow-cyan {{
            box-shadow: 0 0 25px rgba(0, 240, 255, 0.35);
        }}
        .border-glow {{
            border: 1px solid rgba(0, 240, 255, 0.25);
        }}
        .border-glow:hover {{
            border-color: #00f0ff;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
        }}
        .border-glow-burn:hover {{
            border-color: #ff6b00;
            box-shadow: 0 0 15px rgba(255, 107, 0, 0.4);
        }}
        
        @keyframes spinSlow {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        @keyframes flamePulse {{
            0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 8px rgba(255,107,0,0.8)); }}
            50% {{ transform: scale(1.18); filter: drop-shadow(0 0 18px rgba(255,107,0,1)); }}
        }}
        .animate-spin-slow {{
            animation: spinSlow 12s linear infinite;
        }}
        .animate-flame {{
            animation: flamePulse 1.5s ease-in-out infinite;
        }}
    </style>
</head>
<body class="font-rajdhani antialiased selection:bg-cyanNeon selection:text-black min-h-screen">

    <!-- NAVIGATION BAR -->
    <nav class="border-b border-gray-800/80 bg-void/80 backdrop-blur-md sticky top-0 z-50 px-6 py-3">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <div class="flex items-center gap-3">
                <img src="{logo_b64}" alt="Jarvis Logo" class="w-10 h-10 rounded-full border border-cyanNeon object-cover">
                <div>
                    <h1 class="font-orbitron font-extrabold text-lg tracking-wider text-white">JARVISDEGEN</h1>
                    <span class="text-xs font-mono text-cyanNeon tracking-widest">$JDEGEN</span>
                </div>
            </div>

            <div class="hidden md:flex items-center gap-6 text-sm font-semibold tracking-wider text-gray-300">
                <a href="#home" class="text-cyanNeon hover:text-white transition">HOME</a>
                <a href="#about" class="hover:text-cyanNeon transition">ABOUT</a>
                <a href="#works" class="hover:text-cyanNeon transition">HOW IT WORKS</a>
                <a href="#tokenomics" class="hover:text-cyanNeon transition">TOKENOMICS</a>
                <a href="#roadmap" class="hover:text-cyanNeon transition">ROADMAP</a>
                <a href="#faq" class="hover:text-cyanNeon transition">FAQ</a>
            </div>

            <div class="flex items-center gap-3">
                <a href="#" class="px-4 py-2 text-xs font-mono border border-cyanNeon text-cyanNeon rounded hover:bg-cyanNeon/10 transition">
                    ✈ TELEGRAM
                </a>
                <a href="#" class="px-4 py-2 text-xs font-mono border border-gray-700 text-gray-300 rounded hover:border-white transition">
                    𝕏 / TWITTER
                </a>
            </div>
        </div>
    </nav>

    <!-- HERO SECTION -->
    <section id="home" class="max-w-7xl mx-auto px-6 pt-12 pb-16 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-5 space-y-6">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyanNeon/10 border border-cyanNeon/40 text-xs font-mono text-cyanNeon">
                <span class="w-2 h-2 rounded-full bg-profitGreen animate-pulse"></span>
                LIVE AI AGENT ONLINE
            </div>

            <h1 class="font-orbitron text-4xl lg:text-5xl font-black leading-tight text-white tracking-wide">
                THE AI THAT TRADES THE <span class="text-cyanNeon">SOLANA TRENCHES.</span>
            </h1>

            <p class="font-mono text-lg text-cyanNeon">
                I DON'T SLEEP.<br>
                I SCAN. I TRADE. I BURN.
            </p>

            <p class="text-gray-400 text-sm leading-relaxed">
                JarvisDegen is an autonomous AI agent managing a live trading portfolio on Solana. Profits fuel the engine. 30% buyback & burn. 100% transparent.
            </p>

            <div class="flex flex-wrap gap-4 pt-2">
                <a href="#terminal" class="px-6 py-3 font-orbitron font-bold text-sm bg-cyanNeon text-black rounded glow-cyan hover:bg-white transition">
                    ENTER THE TERMINAL &gt;
                </a>
                <a href="#" class="px-6 py-3 font-orbitron font-bold text-sm border border-gray-700 text-white rounded hover:border-cyanNeon transition">
                    WHITEPAPER
                </a>
            </div>
        </div>

        <div class="lg:col-span-3 flex justify-center">
            <div class="relative w-full max-w-xs h-[420px] rounded-2xl bg-cardBg border border-cyanNeon/40 flex flex-col items-center justify-between p-3 overflow-hidden glow-cyan group">
                <div class="w-full h-full rounded-xl overflow-hidden relative border border-cyanNeon/20">
                    <img src="{hero_b64}" alt="Jarvis AI Agent" class="w-full h-full object-cover object-center transform group-hover:scale-105 transition duration-500">
                </div>
                <div class="mt-2 text-center">
                    <div class="font-orbitron text-cyanNeon text-xs tracking-widest font-bold">JARVIS AGENT</div>
                    <div class="text-[10px] text-gray-400 font-mono">AUTONOMOUS MODE</div>
                </div>
            </div>
        </div>

        <div id="terminal" class="lg:col-span-4 bg-cardBg border-glow rounded-xl p-5 font-mono text-xs">
            <div class="flex justify-between items-center border-b border-gray-800 pb-3 mb-4">
                <span class="font-bold text-white font-orbitron text-sm">JARVIS TERMINAL</span>
                <span class="flex items-center gap-1.5 text-profitGreen text-2xl leading-none">• <span class="text-xs text-profitGreen font-mono">ONLINE</span></span>
            </div>

            <div class="space-y-3">
                <div class="flex justify-between text-gray-400">
                    <span>TREASURY</span>
                    <span class="text-white font-bold">$124,580.00</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>24H P&amp;L</span>
                    <span class="text-profitGreen font-bold">+18.42%</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>TOTAL TRADES</span>
                    <span class="text-white font-bold">1,482</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>WIN RATE</span>
                    <span class="text-cyanNeon font-bold">78.5%</span>
                </div>
                <div class="flex justify-between text-gray-400">
                    <span>$JDEGEN BURNED</span>
                    <span class="text-profitGreen font-bold">2,450,000</span>
                </div>
            </div>

            <div class="mt-5 p-3 bg-black/60 rounded border border-gray-800 text-gray-300 font-mono text-[11px] space-y-1.5">
                <p class="text-gray-500">&gt; SYSTEM LOG</p>
                <p class="text-cyanNeon">&gt; SCANNING SOLANA TRENCHES...</p>
                <p class="text-profitGreen">&gt; SEARCHING FOR OPPORTUNITIES...</p>
                <p class="text-yellow-400 animate-pulse">&gt; WAITING FOR SIGNAL...</p>
            </div>
        </div>
    </section>

    <!-- ROADMAP & FLYWHEEL SECTION -->
    <section id="roadmap" class="max-w-7xl mx-auto px-6 py-12 grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- FLYWHEEL -->
        <div class="bg-cardBg border-glow p-6 rounded-xl flex flex-col justify-between relative overflow-hidden">
            <h3 class="font-orbitron text-lg font-bold text-white text-center mb-4">THE $JDEGEN FLYWHEEL</h3>
            
            <div class="relative my-8 flex justify-center items-center h-64">
                <div class="absolute w-56 h-56 rounded-full border-2 border-dashed border-cyanNeon/60 animate-spin-slow"></div>

                <div class="absolute w-64 h-64 flex items-center justify-center pointer-events-none">
                    <div class="absolute -top-1 text-cyanNeon animate-pulse">
                        <svg class="w-6 h-6 transform rotate-90" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
                        </svg>
                    </div>
                    <div class="absolute -bottom-1 text-profitGreen animate-pulse">
                        <svg class="w-6 h-6 transform -rotate-90" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
                        </svg>
                    </div>
                </div>

                <div class="z-10 flex flex-col items-center justify-center text-center">
                    <span class="font-orbitron font-extrabold text-cyanNeon text-base tracking-widest mb-1">$JDEGEN</span>
                    <div class="flex items-center gap-1.5 my-1">
                        <span class="font-orbitron text-xs font-bold text-burnOrange tracking-wider">BURN</span>
                        <div class="text-burnOrange animate-flame">
                            <svg class="w-10 h-10" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-1.048c-2.5 1.249-4.87 3.324-5.32 6.002-.32 1.905.15 3.82 1.28 5.308-1.5-.27-2.82-.87-3.905-1.745a1 1 0 00-1.52 1.205c1.69 2.58 4.54 4.28 7.74 4.67 5.12.63 9.8-3.05 10.23-8.15.22-2.58-.69-5.11-2.45-6.94-.31-.33-.78-.45-1.205-.3-.425.15-.72.525-.72.98 0 1.16-.39 2.27-1.12 3.17-.55-.91-1.1-1.89-1.56-3.15z" clip-rule="evenodd"/>
                            </svg>
                        </div>
                    </div>
                </div>

                <div class="absolute top-2 left-2 md:left-6 text-xs font-mono text-cyanNeon bg-black/90 p-2.5 rounded-lg border border-cyanNeon/40 backdrop-blur-md shadow-lg">
                    <span class="font-bold text-sm block font-orbitron">70%</span> RE-TRADE
                </div>

                <div class="absolute bottom-2 right-2 md:right-6 text-xs font-mono text-profitGreen bg-black/90 p-2.5 rounded-lg border border-profitGreen/40 backdrop-blur-md shadow-lg">
                    <span class="font-bold text-sm block font-orbitron">30%</span> BUYBACK
                </div>
            </div>

            <p class="text-center text-xs font-mono text-gray-400 mt-2">
                Profits from trading fuel the engine.<br>More volume. More burns. More scarcity.
            </p>
        </div>

        <!-- ROADMAP -->
        <div class="bg-cardBg border-glow p-6 rounded-xl">
            <h3 class="font-orbitron text-lg font-bold text-white mb-6">ROADMAP</h3>

            <div class="space-y-6 font-mono text-xs">
                <div class="flex gap-4">
                    <div class="w-8 h-8 rounded-full bg-cyanNeon/20 border border-cyanNeon text-cyanNeon flex items-center justify-center shrink-0">01</div>
                    <div>
                        <h4 class="font-orbitron text-white font-bold text-sm">PROTOCOL 01 - AWAKEN JARVIS</h4>
                        <p class="text-gray-400 mt-1">Branding • AI personality • Architecture • Paper trading</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <div class="w-8 h-8 rounded-full bg-cyanNeon/20 border border-cyanNeon text-cyanNeon flex items-center justify-center shrink-0">02</div>
                    <div>
                        <h4 class="font-orbitron text-white font-bold text-sm">PROTOCOL 02 - CONNECT JARVIS</h4>
                        <p class="text-gray-400 mt-1">Solana data • Market scanner • Risk engine • Telegram &amp; X</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <div class="w-8 h-8 rounded-full bg-cyanNeon/20 border border-cyanNeon text-cyanNeon flex items-center justify-center shrink-0">03</div>
                    <div>
                        <h4 class="font-orbitron text-white font-bold text-sm">PROTOCOL 03 - RELEASE $JDEGEN</h4>
                        <p class="text-gray-400 mt-1">Fair launch • Token deployment • Public treasury</p>
                    </div>
                </div>

                <div class="flex gap-4">
                    <div class="w-8 h-8 rounded-full bg-cyanNeon/20 border border-cyanNeon text-cyanNeon flex items-center justify-center shrink-0">04</div>
                    <div>
                        <h4 class="font-orbitron text-white font-bold text-sm">PROTOCOL 04 - AUTONOMOUS MODE</h4>
                        <p class="text-gray-400 mt-1">Live trading • Public trades • Buyback &amp; burn • Dashboard</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- MATRIX CTA SECTION -->
    <section class="max-w-7xl mx-auto px-6 py-8">
        <div class="bg-cardBg border-glow rounded-2xl p-6 lg:p-8 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center relative overflow-hidden">
            
            <!-- Robot Image (bras_croisees.png) -->
            <div class="lg:col-span-4 flex justify-center lg:justify-start">
                <img src="{bras_b64}" alt="Jarvis Robot Bras Croisés" class="max-h-72 w-auto object-contain drop-shadow-[0_0_20px_rgba(0,240,255,0.3)]">
            </div>

            <!-- Middle Text & Buttons -->
            <div class="lg:col-span-4 space-y-4 text-center lg:text-left">
                <h2 class="font-orbitron text-2xl lg:text-3xl font-black text-white leading-tight">
                    READY TO ENTER<br>THE <span class="text-cyanNeon">MATRIX?</span>
                </h2>
                <p class="text-gray-400 text-xs font-mono">
                    Join the degen army and follow Jarvis on his mission.
                </p>

                <div class="flex flex-wrap gap-3 justify-center lg:justify-start pt-2">
                    <a href="#" class="px-5 py-2.5 bg-cyanNeon text-black font-orbitron font-bold text-xs rounded-md hover:bg-white transition flex items-center gap-2">
                        JOIN TELEGRAM ✈
                    </a>
                    <a href="#" class="px-5 py-2.5 border border-cyanNeon/60 text-cyanNeon font-orbitron font-bold text-xs rounded-md hover:bg-cyanNeon/10 transition flex items-center gap-2">
                        𝕏 FOLLOW ON X
                    </a>
                </div>
            </div>

            <!-- Right Subscription Box -->
            <div class="lg:col-span-4 bg-black/40 border border-gray-800 p-6 rounded-xl space-y-3">
                <h4 class="font-orbitron text-sm font-bold text-white uppercase tracking-wider">GET JARVIS SIGNALS</h4>
                <p class="text-gray-400 text-xs font-mono">Enter your email to receive updates.</p>
                
                <div class="space-y-3 pt-2">
                    <input type="email" placeholder="Your email address" class="w-full bg-black/80 border border-gray-700 rounded-md px-3 py-2 text-xs font-mono text-white placeholder-gray-600 focus:outline-none focus:border-cyanNeon">
                    <button class="w-full py-2.5 bg-cyanNeon text-black font-orbitron font-bold text-xs rounded-md hover:bg-white transition">
                        SUBSCRIBE
                    </button>
                </div>
            </div>

        </div>
    </section>

    <!-- FOOTER -->
    <footer class="border-t border-gray-800 bg-void py-8 px-6 text-xs font-mono text-gray-500">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
            
            <div class="flex items-center gap-3">
                <img src="{logo_b64}" alt="Logo" class="w-8 h-8 rounded-full border border-cyanNeon">
                <div>
                    <span class="font-orbitron font-bold text-white text-sm block">JARVISDEGEN</span>
                    <span class="text-cyanNeon text-xs">$JDEGEN</span>
                </div>
            </div>

            <div class="text-center">
                <span class="text-gray-300 font-bold block">CA: NOT DEPLOYED YET</span>
                <p class="text-[11px] text-gray-500">Token launching soon on Solana.</p>
            </div>

            <div class="flex flex-col items-center md:items-end gap-2">
                <span class="text-[10px] text-cyanNeon font-orbitron tracking-widest">FOLLOW JARVIS</span>
                <div class="flex gap-2">
                    <a href="#" class="w-8 h-8 rounded-full border border-cyanNeon/40 text-cyanNeon flex items-center justify-center hover:bg-cyanNeon/20 transition">✈</a>
                    <a href="#" class="w-8 h-8 rounded-full border border-cyanNeon/40 text-cyanNeon flex items-center justify-center hover:bg-cyanNeon/20 transition">𝕏</a>
                    <a href="#" class="w-8 h-8 rounded-full border border-cyanNeon/40 text-cyanNeon flex items-center justify-center hover:bg-cyanNeon/20 transition">🔗</a>
                </div>
            </div>

        </div>

        <div class="max-w-7xl mx-auto mt-6 pt-4 border-t border-gray-800/60 text-center md:text-right text-[11px] text-gray-600">
            © 2026 JARVISDEGEN. All rights reserved.
        </div>
    </footer>

</body>
</html>
"""

components.html(HTML_TEMPLATE, height=2700, scrolling=True)
