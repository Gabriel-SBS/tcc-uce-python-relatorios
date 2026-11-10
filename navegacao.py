"""Insere (ou atualiza) a mesma barra de navegação no topo de todas as páginas do site.

Uso: python navegacao.py   (rodar dentro de relatorios_site, depois de copiar relatórios novos)
A barra fica entre os marcadores NAV-TCC; rodar de novo substitui a versão anterior.
"""
from pathlib import Path
import re

PASTA = Path(__file__).resolve().parent

# (arquivo, rótulo) na ordem em que aparecem na barra. Páginas ausentes são ignoradas.
PAGINAS = [
    ("index.html", "Início"),
    ("relatorio_g1_mentores.html", "G1 · Mentores"),
    ("relatorio_graficos_barras_resumido.html", "G2 · Por tema"),
    ("relatorio_graficos_barras.html", "G2 · Barras por item"),
    ("relatorio_graficos_pizza.html", "G2 · Pizzas por item"),
    ("graficos_egressos.html", "G2 · Por subgrupo"),
    ("relatorio_g3_professores.html", "G3 · Professores"),
]

INICIO, FIM = "<!-- NAV-TCC:inicio -->", "<!-- NAV-TCC:fim -->"

ESTILO = """<style>
.navtcc{position:sticky;top:0;z-index:9999;background:#0f172a;padding:8px 16px;
  font:600 13.5px/1.3 system-ui,-apple-system,"Segoe UI",sans-serif;box-shadow:0 1px 4px rgba(0,0,0,.25)}
.navtcc ul{list-style:none;margin:0 auto;padding:0;max-width:1200px;display:flex;flex-wrap:wrap;gap:6px}
.navtcc li{margin:0;padding:0;border:0;background:none}
.navtcc a{display:block;color:#e2e8f0;text-decoration:none;padding:6px 11px;border-radius:6px;border:0;
  background:none;box-shadow:none;margin:0;font-weight:600}
.navtcc a:hover{background:#1e293b}
.navtcc a[aria-current=page]{background:#e2e8f0;color:#0f172a}
</style>"""


def barra(atual: str, existentes: set[str]) -> str:
    itens = []
    for arq, rotulo in PAGINAS:
        if arq not in existentes:
            continue
        cur = ' aria-current="page"' if arq == atual else ""
        itens.append(f'<li><a href="{arq}"{cur}>{rotulo}</a></li>')
    return (f'{INICIO}\n{ESTILO}\n<nav class="navtcc" aria-label="Relatórios"><ul>'
            + "".join(itens) + f"</ul></nav>\n{FIM}")


def main() -> None:
    existentes = {p.name for p in PASTA.glob("*.html")}
    for arq, _ in PAGINAS:
        caminho = PASTA / arq
        if not caminho.exists():
            continue
        html = caminho.read_text(encoding="utf-8")
        html = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIM) + r"\n?", "", html, flags=re.S)
        html = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + "\n" + barra(arq, existentes), html, count=1)
        caminho.write_text(html, encoding="utf-8")
        print("ok", arq)


if __name__ == "__main__":
    main()
