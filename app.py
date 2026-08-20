from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Template HTML/CSS/JS complet avec Tailwind CSS, effets Neon et police Orbitron
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JARVISDEGEN | $JDEGEN on Solana</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Orbitron:wght@600;800;900&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        void: '#070c14',
                        cardBg: 'rgba(15, 25, 42, 0.75)',
                        cyanNeon: '#00f0ff',
                        aquaNeon: '#00fcc2',
                        profitGreen: '#c0ff6b',
                        riskRed: '#ff4d4d',
                    },
                    fontFamily: {
                        orbitron: ['Orbitron', 'sans-serif'],
                        rajdhani: ['Rajdhani', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    }
                }
            }
        }
    </script>
    
    <style>
        body {
            background-color: #070c14;
            color: #e6f1ff;
            background-image: 
                radial-gradient(circle at 15% 20%, rgba(0, 240, 255, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 85% 60%, rgba(0, 252, 194, 0.05) 0%, transparent 40%);
        }
        .glow-cyan {
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.3);
        }
        .border-glow {
            border: 1px solid rgba(0, 240, 255, 0.25);
        }
        .border-glow:hover {
            border-color: #00f0ff;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
        }
        .text-glow {
            text-shadow: 0 0 10px rgba(0, 240, 255, 0.6);
        }
    </style>
</head>
<body class="font-rajdhani antialiased selection:bg-cyanNeon selection:text-black">

    <!-- NAVIGATION BAR -->
    <nav class="border-b border-gray-800/80 bg-void/80 backdrop-blur-md sticky top-0 z-50 px-6 py-4">
        <div class="max-w-7xl mx-auto flex justify-between items-center">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-full bg-cyanNeon/20 border border-cyanNeon flex items-center justify-center font-orbitron font-bold text-cyanNeon">
                    J
                </div>
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

        <!-- Center Image Avatar Placeholder -->
        <div class="lg:col-span-3 flex justify-center">
            <div class="relative w-64 h-80 rounded-2xl bg-gradient-to-b from-cyanNeon/20 to-transparent border border-cyanNeon/30 flex flex-col items-center justify-center overflow-hidden glow-cyan">
                <!-- Replace with actual AI agent image -->
                <div class="text-7xl mb-4">🤖</div>
                <div class="font-orbitron text-cyanNeon text-sm tracking-widest font-bold">JARVIS AGENT</div>
                <div class="text-xs text-gray-400 font-mono mt-1">AUTONOMOUS MODE</div>
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
        <h2 class="font-orbitron text-center text-2xl font-bold text-white mb-10 tracking-wider">
            HOW MY BRAIN WORKS
        </h2>

        <div class="grid grid-cols-2 md:grid-cols-6 gap-4">
            <!-- Steps -->
            <div class="bg-cardBg border-glow p-4 rounded-xl text-center flex flex-col items-center">
                <div class="w-10 h-10 rounded-lg bg-cyanNeon/10 border border-cyanNeon text-cyanNeon flex items-center justify-center font-bold mb-3">01</div>
                <h3 class="font-orbitron text-xs font-bold text-white">SCAN</h3>
                <p class="text-[11px] text-gray-400 mt-2">Solana market data in real-time</p>
            </div>

            <div class="bg-cardBg border-glow p-4 rounded-xl text-center flex flex-col items-center">
                <div class="w-10 h-10 rounded-lg bg-cyanNeon/10 border border-cyanNeon text-cyanNeon flex items-center justify-center font-bold mb-3">02</div>
                <h3 class="font-orbitron text-xs font-bold text-white">THINK</h3>
                <p class="text-[11px] text-gray-400 mt-2">AI analysis + sentiment</p>
            </div>

            <div class="bg-cardBg border-glow p-4 rounded-xl text-center flex flex-col items-center">
                <div class="w-10 h-10 rounded-lg bg-cyanNeon/10 border border-cyanNeon text-cyanNeon flex items-center justify-center font-bold mb-3">03</div>
                <h3 class="font-orbitron text-xs font-bold text-white">RISK CHECK</h3>
                <p class="text-[11px] text-gray-400 mt-2">Position limits &amp; risk engine</p>
            </div>

            <div class="bg-cardBg border-glow p-4 rounded-xl text-center flex flex-col items-center">
                <div class="w-10 h-10 rounded-lg bg-cyanNeon/10 border border-cyanNeon text-cyanNeon flex items-center justify-center font-bold mb-3">04</div>
                <h3 class="font-orbitron text-xs font-bold text-white">TRADE</h3>
                <p class="text-[11px] text-gray-400 mt-2">Execute via Jupiter &amp; Jito</p>
            </div>

            <div class="bg-cardBg border-glow p-4 rounded-xl text-center flex flex-col items-center">
                <div class="w-10 h-10 rounded-lg bg-cyanNeon/10 border border-cyanNeon text-cyanNeon flex items-center justify-center font-bold mb-3">05</div>
                <h3 class="font-orbitron text-xs font-bold text-white">PROFIT</h3>
                <p class="text-[11px] text-gray-400 mt-2">Treasury grows</p>
            </div>

            <div class="bg-cardBg border-glow p-4 rounded-xl text-center flex flex-col items-center">
                <div class="w-10 h-10 rounded-lg bg-cyanNeon/10 border border-cyanNeon text-cyanNeon flex items-center justify-center font-bold mb-3">06</div>
                <h3 class="font-orbitron text-xs font-bold text-white">BURN</h3>
                <p class="text-[11px] text-gray-400 mt-2">30% buyback &amp; burn $JDEGEN</p>
            </div>
        </div>
    </section>

    <!-- FLYWHEEL & ROADMAP -->
    <section id="roadmap" class="max-w-7xl mx-auto px-6 py-12 grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- Flywheel -->
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

        <!-- Roadmap -->
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

    <!-- NEWSLETTER CTA -->
    <section class="max-w-7xl mx-auto px-6 py-12">
        <div class="bg-cardBg border-glow rounded-xl p-8 flex flex-col md:flex-row items-center justify-between gap-8">
            <div>
                <h3 class="font-orbitron text-2xl font-bold text-white">READY TO ENTER THE <span class="text-cyanNeon">MATRIX?</span></h3>
                <p class="text-gray-400 text-sm mt-2">Join the degen army and follow Jarvis on his mission.</p>
                
                <div class="flex gap-3 mt-4">
                    <a href="#" class="px-4 py-2 text-xs font-mono border border-cyanNeon text-cyanNeon rounded hover:bg-cyanNeon/10">JOIN TELEGRAM ✈</a>
                    <a href="#" class="px-4 py-2 text-xs font-mono border border-gray-700 text-gray-300 rounded hover:border-white">FOLLOW ON X 𝕏</a>
                </div>
            </div>

            <form action="/subscribe" method="POST" class="w-full md:w-auto flex flex-col gap-3">
                <span class="font-orbitron text-xs font-bold text-white">GET JARVIS SIGNALS</span>
                <input type="email" name="email" placeholder="Your email address" required class="px-4 py-3 bg-black/80 border border-gray-800 rounded text-sm text-white focus:outline-none focus:border-cyanNeon w-full md:w-72">
                <button type="submit" class="px-6 py-3 font-orbitron font-bold text-xs bg-cyanNeon text-black rounded hover:bg-white transition">
                    SUBSCRIBE
                </button>
            </form>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="border-t border-gray-800 bg-void py-8 px-6 text-xs font-mono text-gray-500">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
            <div>
                <span class="font-orbitron font-bold text-white text-sm">JARVISDEGEN</span>
                <span class="text-cyanNeon ml-2">$JDEGEN</span>
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

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    # Traitement de l'inscription à la newsletter
    return jsonify({"status": "success", "message": f"Inscrit avec succès : {email}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)