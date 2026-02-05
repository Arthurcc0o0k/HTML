"""
Site simples em Flask sobre Minecraft (arquivo único).

Instalação:
    pip install flask

Execução:
    python .vscode/branch.py

Abra http://127.0.0.1:5000 no navegador.
"""

from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "minecraft-dev-key"

BASE_TEMPLATE = """
<!doctype html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Minecraft — Guia Simples</title>
    <style>
      :root{--bg:#0b1220;--card:#0f1724;--accent:#ffcc00;--muted:#9aa6b2;--glass:rgba(255,255,255,0.03)}
      body{font-family:Inter,Segoe UI,Arial;background:linear-gradient(180deg,#071023 0%,#081226 100%);color:#e6eef6;margin:0}
      .nav{display:flex;gap:12px;align-items:center;padding:18px 24px;background:linear-gradient(90deg,rgba(0,0,0,0.1),transparent)}
      .brand{font-weight:700;color:var(--accent)}
      a.navlink{color:var(--muted);text-decoration:none;padding:8px;border-radius:6px}
      a.navlink:hover{color:white;background:var(--glass)}
      .container{max-width:1000px;margin:28px auto;padding:18px}
      .card{background:linear-gradient(180deg,rgba(255,255,255,0.02),transparent);padding:18px;border-radius:10px;box-shadow:0 6px 18px rgba(2,6,23,0.6)}
      h1{margin:0 0 12px 0}
      .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:14px}
      .tile{background:var(--card);padding:12px;border-radius:8px}
      footer{margin-top:22px;color:var(--muted);font-size:14px;text-align:center}
      .gallery{display:flex;gap:10px;flex-wrap:wrap}
      .block{width:120px;height:80px;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#071022;font-weight:700}
      .grass{background:linear-gradient(#7dbb3a,#4e8b2b)}
      .dirt{background:#8b5a2b}
      .water{background:linear-gradient(#5fb3ff,#2b7fcc);color:white}
      .stone{background:#9aa0a6;color:#102023}
      form input, form textarea{width:100%;padding:8px;margin:6px 0;border-radius:6px;border:1px solid rgba(255,255,255,0.06);background:transparent;color:inherit}
      form button{background:var(--accent);border:none;padding:10px 14px;border-radius:8px;color:#071022;font-weight:700}
    </style>
  </head>
  <body>
    <nav class="nav">
      <div class="brand">Minecraft Guia</div>
      <div style="flex:1"></div>
      <a class="navlink" href="/">Home</a>
      <a class="navlink" href="/sobre">Sobre</a>
      <a class="navlink" href="/galeria">Galeria</a>
      <a class="navlink" href="/contato">Contato</a>
    </nav>
    <main class="container">
      {% with messages = get_flashed_messages() %}
        {% if messages %}
          <div class="card">
            {% for m in messages %}
              <div style="color:var(--accent);">{{ m }}</div>
            {% endfor %}
          </div>
        {% endif %}
      {% endwith %}
      <div class="card">{{ content|safe }}</div>
      <footer>Feito com Python + Flask • Conteúdo sobre Minecraft</footer>
    </main>
  </body>
</html>
"""


HOME_CONTENT = """
<h1>Bem-vindo ao Guia Minecraft</h1>
<p>Este é um site simples que apresenta fatos, dicas e uma pequena galeria sobre <strong>Minecraft</strong>.</p>
<div class="grid">
  <div class="tile">
    <h3>O que é Minecraft?</h3>
    <p>Minecraft é um jogo de construção e aventura em mundo aberto onde os jogadores exploram, coletam recursos e criam estruturas usando blocos.</p>
  </div>
  <div class="tile">
    <h3>Modos de Jogo</h3>
    <p>Survival, Creative e Adventure são os modos principais. Survival foca em recursos e sobrevivência; Creative dá recursos ilimitados.</p>
  </div>
  <div class="tile">
    <h3>Dicas Rápidas</h3>
    <ul>
      <li>Coloque uma cama antes de anoitecer para definir respawn.</li>
      <li>Leve sempre comida e uma picareta de ferro.</li>
      <li>Use tochas para iluminar cavernas e evitar mobs.</li>
    </ul>
  </div>
</div>
"""


SOBRE_CONTENT = """
<h1>Sobre Minecraft</h1>
<p>Minecraft foi criado por Markus Persson e desde então cresceu para se tornar um dos jogos mais populares do mundo.</p>
<h3>Elementos notáveis</h3>
<ul>
  <li>Crafting: combine itens para criar ferramentas.</li>
  <li>Redstone: eletrônica em Minecraft para criar mecanismos.</li>
  <li>Mobs: entidades como zumbis, creepers e aldeões.</li>
</ul>
"""


GALLERY_CONTENT = """
<h1>Galeria (blocos representativos)</h1>
<p>Blocos ilustrativos (cores apenas).</p>
<div class="gallery">
  <div class="block grass">Grama</div>
  <div class="block dirt">Terra</div>
  <div class="block water">Água</div>
  <div class="block stone">Pedra</div>
</div>
"""


CONTACT_CONTENT = """
<h1>Contato</h1>
<p>Envie uma mensagem (exemplo: formulário de contato não envia e-mail, apenas demonstração local).</p>
<form method="post">
  <label>Nome</label>
  <input name="nome" placeholder="Seu nome" required>
  <label>Mensagem</label>
  <textarea name="mensagem" rows="4" placeholder="Escreva sua mensagem" required></textarea>
  <button type="submit">Enviar</button>
</form>
"""


@app.route("/")
def home():
    return render_template_string(BASE_TEMPLATE, content=HOME_CONTENT)


@app.route("/sobre")
def sobre():
    return render_template_string(BASE_TEMPLATE, content=SOBRE_CONTENT)


@app.route("/galeria")
def galeria():
    return render_template_string(BASE_TEMPLATE, content=GALLERY_CONTENT)


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form.get("nome", "Anônimo")
        mensagem = request.form.get("mensagem", "")
        flash(f"Obrigado, {nome}! Mensagem recebida.")
        return redirect(url_for('contato'))
    return render_template_string(BASE_TEMPLATE, content=CONTACT_CONTENT)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
