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

# Fonction pour convertir une image locale en base64 pour l'injecter dans le HTML
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            ext = path.split('.')[-1]
            return f"data:image/{ext};base64,{encoded}"
    return ""

# Récupération des images depuis le dossier static (si présentes)
logo_b64 = get_image_base64("static/logo.png")
hero_b64 = get_image_base64("static/hero.jpg")

# Masquer la barre de navigation et le footer par défaut de Streamlit
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

# Code HTML complet
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
        .text-glow {{
            text-shadow: 0 0 10px rgba(0, 240, 255, 0.6);
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
        
        <!-- Left Content -->
        <div class="lg:col-span-5 space-y-6">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyanNeon/10 border border-cyanNeon/40 text-xs font-mono text-cyanNeon">
                <span class="w-2 h-2 rounded-full bg-profitGreen animate-pulse"></span>
                LIVE AI AGENT ONLINE
            </div>

            <h1 class="font-orbitron text-4xl lg:text-5xl font-black leading-tight text-white tracking-wide">
                THE AI THAT TRADES THE <span class="text-cyanNeon text-glow">SOLANA TRENCHES.</span>
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

            <div class="flex gap-4 pt-4 text-xs font-mono text-gray-400">
                <span class="px-3 py-1 bg-gray-900 border border-gray-800 rounded text-cyanNeon">$JDEGEN</span>
                <span class="px-3 py-1 bg-gray-900 border border-gray-800 rounded text-purple-400">⚡ SOLANA</span>
            </div>
        </div>

        <!-- Center Image Avatar (HERO IMAGE) -->
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

        <!-- Right Terminal Dashboard -->
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
                <p class="text-gray-300">&gt; ANALYZING LIQUIDITY...</p>
                <p class="text-profitGreen">&gt; SEARCHING FOR OPPORTUNITIES...</p>
                <p class="text-yellow-400 animate-pulse">&gt; WAITING FOR SIGNAL...</p>
            </div>
        </div>
    </section>

    <!-- HIGHLIGHTS BAR -->
    <section class="border-y border-gray-800 bg-black/40 py-6 my-8">
        <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-5 gap-4 text-center font-mono text-xs">
            <div class="p-2 border-r border-gray-800/60">
                <p class="text-cyanNeon font-bold text-sm">AI POWERED</p>
                <p class="text-gray-500">Autonomous agent</p>
            </div>
            <div class="p-2 border-r border-gray-800/60">
                <p class="text-cyanNeon font-bold text-sm">ON CHAIN</p>
                <p class="text-gray-500">100% Transparent</p>
            </div>
            <div class="p-2 border-r border-gray-800/60">
                <p class="text-cyanNeon font-bold text-sm">SOLANA</p>
                <p class="text-gray-500">Built for speed</p>
            </div>
            <div class="p-2 border-r border-gray-800/60">
                <p class="text-cyanNeon font-bold text-sm">BUYBACK &amp; BURN</p>
                <p class="text-gray-500">Value goes up</p>
            </div>
            <div class="p-2 col-span-2 md:col-span-1">
                <p class="text-cyanNeon font-bold text-sm">COMMUNITY FIRST</p>
                <p class="text-gray-500">Degen army</p>
            </div>
        </div>
    </section>

    <!-- HOW MY BRAIN WORKS -->
    <section id="works" class="max-w-7xl mx-auto px-6 py-12">
        <div class="text-center mb-12">
            <span class="text-xs font-mono text-cyanNeon tracking-widest uppercase">// NEURAL EXECUTION FLOW</span>
            <h2 class="font-orbitron text-3xl font-black text-white mt-1 tracking-wider">
                HOW MY BRAIN WORKS
            </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-4">
            
            <!-- 01 SCAN -->
            <div class="bg-cardBg border-glow p-5 rounded-xl flex flex-col items-center text-center justify-between hover:-translate-y-1 transition duration-300">
                <div class="w-full flex justify-end">
                    <span class="text-[10px] font-mono text-cyanNeon/60">01</span>
                </div>
                <!-- Radar SVG -->
                <div class="w-14 h-14 my-3 rounded-xl bg-cyanNeon/10 border border-cyanNeon/40 flex items-center justify-center text-cyanNeon">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="12" cy="12" r="9" stroke-width="1.5" stroke-dasharray="2 2"/>
                        <circle cx="12" cy="12" r="5" stroke-width="1.5"/>
                        <circle cx="12" cy="12" r="1.5" fill="currentColor"/>
                        <path stroke-linecap="round" stroke-width="1.5" d="M12 12L18 6"/>
                    </svg>
                </div>
                <div>
                    <h3 class="font-orbitron text-sm font-bold text-white mb-1">SCAN</h3>
                    <p class="text-[11px] text-gray-400 font-mono">Solana market data in real-time</p>
                </div>
            </div>

            <!-- 02 THINK -->
            <div class="bg-cardBg border-glow p-5 rounded-xl flex flex-col items-center text-center justify-between hover:-translate-y-1 transition duration-300">
                <div class="w-full flex justify-end">
                    <span class="text-[10px] font-mono text-cyanNeon/60">02</span>
                </div>
                <!-- Neural Brain SVG -->
                <div class="w-14 h-14 my-3 rounded-xl bg-cyanNeon/10 border border-cyanNeon/40 flex items-center justify-center text-cyanNeon">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.75 3.104v1.244m4.5-1.244v1.244M3.104 9.75h1.244m15.304 0h1.244M3.104 14.25h1.244m15.304 0h1.244M9.75 19.652v1.244m4.5-1.244v1.244M7 7h10v10H7V7z"/>
                        <circle cx="12" cy="12" r="2" fill="currentColor"/>
                    </svg>
                </div>
                <div>
                    <h3 class="font-orbitron text-sm font-bold text-white mb-1">THINK</h3>
                    <p class="text-[11px] text-gray-400 font-mono">AI analysis + sentiment</p>
                </div>
            </div>

            <!-- 03 RISK CHECK -->
            <div class="bg-cardBg border-glow p-5 rounded-xl flex flex-col items-center text-center justify-between hover:-translate-y-1 transition duration-300">
                <div class="w-full flex justify-end">
                    <span class="text-[10px] font-mono text-cyanNeon/60">03</span>
                </div>
                <!-- Shield Check SVG -->
                <div class="w-14 h-14 my-3 rounded-xl bg-cyanNeon/10 border border-cyanNeon/40 flex items-center justify-center text-cyanNeon">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                    </svg>
                </div>
                <div>
                    <h3 class="font-orbitron text-sm font-bold text-white mb-1">RISK CHECK</h3>
                    <p class="text-[11px] text-gray-400 font-mono">Position limits &amp; risk engine</p>
                </div>
            </div>

            <!-- 04 TRADE -->
            <div class="bg-cardBg border-glow p-5 rounded-xl flex flex-col items-center text-center justify-between hover:-translate-y-1 transition duration-300">
                <div class="w-full flex justify-end">
                    <span class="text-[10px] font-mono text-cyanNeon/60">04</span>
                </div>
                <!-- Candlestick Chart SVG -->
                <div class="w-14 h-14 my-3 rounded-xl bg-cyanNeon/10 border border-cyanNeon/40 flex items-center justify-center text-cyanNeon">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-width="1.5" d="M6 3v3m0 12v3M6 6h2v12H6V6zm12-3v5m0 8v5m-1-13h2v8h-2V5zM12 2v6m0 8v6m-1-14h2v8h-2V8z"/>
                    </svg>
                </div>
                <div>
                    <h3 class="font-orbitron text-sm font-bold text-white mb-1">TRADE</h3>
                    <p class="text-[11px] text-gray-400 font-mono">Execute via Jupiter &amp; Jito</p>
                </div>
            </div>

            <!-- 05 PROFIT -->
            <div class="bg-cardBg border-glow p-5 rounded-xl flex flex-col items-center text-center justify-between hover:-translate-y-1 transition duration-300">
                <div class="w-full flex justify-end">
                    <span class="text-[10px] font-mono text-cyanNeon/60">05</span>
                </div>
                <!-- Eye Icon SVG (👁️) -->
                <div class="w-14 h-14 my-3 rounded-xl bg-cyanNeon/10 border border-cyanNeon/40 flex items-center justify-center text-cyanNeon">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
                    </svg>
                </div>
                <div>
                    <h3 class="font-orbitron text-sm font-bold text-white mb-1">PROFIT</h3>
                    <p class="text-[11px] text-gray-400 font-mono">Treasury grows</p>
                </div>
            </div>

            <!-- 06 BURN -->
            <div class="bg-cardBg border-glow-burn p-5 rounded-xl flex flex-col items-center text-center justify-between hover:-translate-y-1 transition duration-300">
                <div class="w-full flex justify-end">
                    <span class="text-[10px] font-mono text-burnOrange">06</span>
                </div>
                <!-- Flame / Fire SVG (🔥 Orange) -->
                <div class="w-14 h-14 my-3 rounded-xl bg-burnOrange/10 border border-burnOrange/40 flex items-center justify-center text-burnOrange">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"/>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.879 16.121A3 3 0 1012.015 11L11 14H9.879z"/>
                    </svg>
                </div>
                <div>
                    <h3 class="font-orbitron text-sm font-bold text-burnOrange mb-1">BURN</h3>
                    <p class="text-[11px] text-gray-400 font-mono">30% buyback &amp; burn $JDEGEN</p>
                </div>
            </div>

        </div>
    </section>

    <!-- ROADMAP & FLYWHEEL -->
    <section id="roadmap" class="max-w-7xl mx-auto px-6 py-12 grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-cardBg border-glow p-6 rounded-xl flex flex-col justify-between">
            <h3 class="font-orbitron text-lg font-bold text-white text-center mb-6">THE $JDEGEN FLYWHEEL</h3>
            
            <div class="relative py-8 flex justify-center items-center">
                <div class="w-48 h-48 rounded-full border-2 border-dashed border-cyanNeon flex flex-col items-center justify-center text-center p-4">
                    <span class="font-orbitron font-bold text-cyanNeon text-sm">$JDEGEN</span>
                    <span class="font-orbitron text-xs text-profitGreen">BURN 🔥</span>
                </div>
                
                <div class="absolute top-0 left-4 text-xs font-mono text-cyanNeon bg-black/80 p-2 rounded border border-cyanNeon/30">
                    <span class="font-bold text-sm block">70%</span> RE-TRADE
                </div>

                <div class="absolute bottom-0 right-4 text-xs font-mono text-profitGreen bg-black/80 p-2 rounded border border-profitGreen/30">
                    <span class="font-bold text-sm block">30%</span> BUYBACK
                </div>
            </div>

            <p class="text-center text-xs font-mono text-gray-400 mt-4">
                Profits from trading fuel the engine.<br>More volume. More burns. More scarcity.
            </p>
        </div>

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

    <!-- FOOTER -->
    <footer class="border-t border-gray-800 bg-void py-8 px-6 text-xs font-mono text-gray-500">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
            <div class="flex items-center gap-2">
                <img src="{logo_b64}" alt="Logo" class="w-6 h-6 rounded-full border border-cyanNeon">
                <span class="font-orbitron font-bold text-white text-sm">JARVISDEGEN</span>
                <span class="text-cyanNeon">$JDEGEN</span>
            </div>

            <div class="text-center">
                <span class="text-gray-400">CA: NOT DEPLOYED YET</span>
                <p class="text-[10px] text-gray-600">Token launching soon on Solana.</p>
            </div>

            <div class="text-right">
                <p>© 2026 JARVISDEGEN. All rights reserved.</p>
            </div>
        </div>
    </footer>

</body>
</html>
"""

# Affichage dans l'application Streamlit
components.html(HTML_TEMPLATE, height=2200, scrolling=True)
