"""Gera um arquivo `index.html` com o conteúdo do site e inicia
um servidor HTTP simples para servir o arquivo na porta 8000.

Uso:
    python site_fixed.py
    Depois abra: http://localhost:8000/index.html
"""

import http.server
import socketserver
from pathlib import Path

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Os 6 Stands de JoJo Mais Desconhecidos</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
            color: #e0e0e0;
            line-height: 1.6;
        }
        
        header {
            background: linear-gradient(135deg, #ff6b6b 0%, #c92a2a 100%);
            padding: 40px 20px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }
        
        header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-transform: uppercase;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .container {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }
        
        .intro {
            text-align: center;
            margin-bottom: 50px;
            background: rgba(255, 107, 107, 0.1);
            padding: 30px;
            border-radius: 10px;
            border-left: 5px solid #ff6b6b;
        }
        
        .stands-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            margin-bottom: 50px;
        }
        
        .stand-card {
            background: linear-gradient(135deg, #2d2d44 0%, #3d3d5c 100%);
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
            border-top: 4px solid #ff6b6b;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
        }
        
        .stand-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(255, 107, 107, 0.3);
        }
        
        .stand-card h2 {
            color: #ff6b6b;
            margin-bottom: 15px;
            font-size: 1.5em;
            text-transform: uppercase;
        }
        
        .stand-card .user-name {
            color: #a0a0c0;
            font-style: italic;
            margin-bottom: 15px;
            font-size: 0.9em;
        }
        
        .stand-card p {
            margin-bottom: 12px;
            text-align: justify;
            color: #d0d0e0;
        }
        
        .power-level {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 107, 107, 0.3);
        }
        
        .power-item {
            text-align: center;
            flex: 1;
        }
        
        .power-item label {
            display: block;
            color: #ff6b6b;
            font-size: 0.8em;
            margin-bottom: 8px;
            font-weight: bold;
        }
        
        .stars {
            color: #ffd700;
            font-size: 1.2em;
        }
        
        footer {
            text-align: center;
            padding: 40px 20px;
            border-top: 2px solid rgba(255, 107, 107, 0.3);
            color: #a0a0c0;
            margin-top: 50px;
        }
        
        .curiosidade {
            background: rgba(255, 215, 0, 0.1);
            border-left: 4px solid #ffd700;
            padding: 15px;
            margin-top: 15px;
            border-radius: 5px;
            font-size: 0.95em;
            color: #ffd700;
        }
    </style>
</head>
<body>
    <header>
        <h1>🌟 Os 6 Stands de JoJo Mais Desconhecidos 🌟</h1>
        <p>Explorando os poderes ocultos do universo JoJo's Bizarre Adventure</p>
    </header>
    
    <div class="container">
        <div class="intro">
            <h2>Bem-vindo ao guia dos stands mais obscuros!</h2>
            <p>Nem todo Stand é conhecido mundialmente. Nesta página, você descobrirá alguns dos poderes mais misteriosos e pouco comentados da série JoJo's Bizarre Adventure. Prepare-se para uma jornada através de habilidades extraordinárias!</p>
        </div>
        
        <div class="stands-grid">
            <!-- Stand 1 -->
            <div class="stand-card">
                <h2>Cheap Trick</h2>
                <div class="user-name">Usuário: Koji Herokane</div>
                <p>Um Stand que literalmente se cola nas costas do hospedeiro. Sua existência é parasitária - ele não pode ser removido e causa dissociação entre o usuário e seu próprio corpo, deixando-o sem controle enquanto Cheap Trick se move livremente.</p>
                <div class="power-level">
                    <div class="power-item">
                        <label>Poder</label>
                        <div class="stars">★★★☆☆</div>
                    </div>
                    <div class="power-item">
                        <label>Periculosidade</label>
                        <div class="stars">★★★★☆</div>
                    </div>
                    <div class="power-item">
                        <label>Conhecimento</label>
                        <div class="stars">★☆☆☆☆</div>
                    </div>
                </div>
                <div class="curiosidade">💡 Curiosidade: Cheap Trick é praticamente impossível de detectar!</div>
            </div>
            
            <!-- Stand 2 -->
            <div class="stand-card">
                <h2>The Lock</h2>
                <div class="user-name">Usuária: Mãe de Emporio Alnino</div>
                <p>Um Stand que manifesta o remorso e a culpa do hospedeiro. Ele toma forma de um pequeno cadeado que prende as ações da vítima quando ela experimenta culpa, incapacitando-a completamente enquanto durarem seus sentimentos de arrependimento.</p>
                <div class="power-level">
                    <div class="power-item">
                        <label>Poder</label>
                        <div class="stars">★★★☆☆</div>
                    </div>
                    <div class="power-item">
                        <label>Periculosidade</label>
                        <div class="stars">★★★★☆</div>
                    </div>
                    <div class="power-item">
                        <label>Conhecimento</label>
                        <div class="stars">★★☆☆☆</div>
                    </div>
                </div>
                <div class="curiosidade">💡 Curiosidade: Funciona baseado em emoções humanas reais!</div>
            </div>
            
            <!-- Stand 3 -->
            <div class="stand-card">
                <h2>Soft Machine</h2>
                <div class="user-name">Usuário: Larry Geil</div>
                <p>Um Stand que amolece qualquer coisa ao seu toque, incluindo corpos. Ele pode transformar seus alvo em massa gelatinosa, tornando-os praticamente inúteis. Apesar de simples, é extremamente eficaz em combate corpo a corpo.</p>
                <div class="power-level">
                    <div class="power-item">
                        <label>Poder</label>
                        <div class="stars">★★★★☆</div>
                    </div>
                    <div class="power-item">
                        <label>Periculosidade</label>
                        <div class="stars">★★★★☆</div>
                    </div>
                    <div class="power-item">
                        <label>Conhecimento</label>
                        <div class="stars">★★☆☆☆</div>
                    </div>
                </div>
                <div class="curiosidade">💡 Curiosidade: Aparece no primeiro arco, mas logo é esquecido!</div>
            </div>
            
            <!-- Stand 4 -->
            <div class="stand-card">
                <h2>Blue Moon</h2>
                <div class="user-name">Usuário: Emporio Alacino</div>
                <p>Um Stand que aumenta a hiperatividade e a agressividade do seu hospedeiro durante a noite de lua cheia. Embora pareça fraco, seu efeito psicológico é devastador, transformando seu usuário em uma criatura selvagem praticamente incontrolável.</p>
                <div class="power-level">
                    <div class="power-item">
                        <label>Poder</label>
                        <div class="stars">★★☆☆☆</div>
                    </div>
                    <div class="power-item">
                        <label>Periculosidade</label>
                        <div class="stars">★★★☆☆</div>
                    </div>
                    <div class="power-item">
                        <label>Conhecimento</label>
                        <div class="stars">★☆☆☆☆</div>
                    </div>
                </div>
                <div class="curiosidade">💡 Curiosidade: Poucos fãs lembram deste Stand!</div>
            </div>
            
            <!-- Stand 5 -->
            <div class="stand-card">
                <h2>Ratt</h2>
                <div class="user-name">Usuário: Ratos Vampiro (Naturaleza)</div>
                <p>Um Stand que permite criar agulhas venenosas de ácido. Suas agulhas podem ser atiradas com precisão impressionante e dissolver praticamente qualquer coisa, incluindo tecido humano. Um dos Stands mais simples mas potencialmente letais.</p>
                <div class="power-level">
                    <div class="power-item">
                        <label>Poder</label>
                        <div class="stars">★★★★☆</div>
                    </div>
                    <div class="power-item">
                        <label>Periculosidade</label>
                        <div class="stars">★★★★★</div>
                    </div>
                    <div class="power-item">
                        <label>Conhecimento</label>
                        <div class="stars">★☆☆☆☆</div>
                    </div>
                </div>
                <div class="curiosidade">💡 Curiosidade: Criado por um rato é revolucionário!</div>
            </div>
            
            <!-- Stand 6 -->
            <div class="stand-card">
                <h2>Boy II Man</h2>
                <div class="user-name">Usuário: Emporio Alacino</div>
                <p>Um Stand que rouba e transfere dano físico para seus alvos através de um jogo de par ou ímpar. Seu poder é único - quanto mais ferido está seu hospedeiro, mais força o Stand ganha para transferir dano aos outros através da dinâmica do jogo.</p>
                <div class="power-level">
                    <div class="power-item">
                        <label>Poder</label>
                        <div class="stars">★★★☆☆</div>
                    </div>
                    <div class="power-item">
                        <label>Periculosidade</label>
                        <div class="stars">★★★★☆</div>
                    </div>
                    <div class="power-item">
                        <label>Conhecimento</label>
                        <div class="stars">★☆☆☆☆</div>
                    </div>
                </div>
                <div class="curiosidade">💡 Curiosidade: Sua lógica é única e desconcertante!</div>
            </div>
        </div>
    </div>
    
    <footer>
        <p><strong>JoJo's Bizarre Adventure</strong> - Uma série de Hirohiko Araki</p>
        <p>Documento informativo sobre Stands pouco conhecidos | Atualizado em 2026</p>
    </footer>
</body>
</html>
"""


def write_index(path: Path = Path("index.html")) -> None:
    path.write_text(HTML_CONTENT, encoding="utf-8")


def serve(port: int = 8000) -> None:
    write_index()
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Servindo em http://localhost:{port}/index.html")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor interrompido pelo usuário")


if __name__ == "__main__":
    serve(8000)
