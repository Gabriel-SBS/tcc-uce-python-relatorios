# Relatórios do TCC sobre a UCE "Ensino de Programação em Python"

Gráficos e tabelas dos três questionários do meu TCC em Engenharia de Computação na UEFS, orientado pela
profa. Pâmela Cortez. O artigo analisa a UCE 008, em que veteranos do curso ensinam Python a estudantes do
Ensino Médio, a partir de três grupos: os mentores, os calouros e os professores de Algoritmos e Programação I.

O artigo traz só os gráficos resumidos. Aqui estão todos, um por pergunta, para quem quiser conferir os
números.

**Site:** https://gabriel-sbs.github.io/tcc-uce-python-relatorios/

## O que tem em cada página

| Página | Conteúdo |
|---|---|
| [G1 · Mentores](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/relatorio_g1_mentores.html) | 43 mentores. Itens por bloco e a opinião sobre IA antes e depois da mentoria |
| [G2 · Por tema](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/relatorio_graficos_barras_resumido.html) | 38 calouros, 50 itens em seis temas, com os três subgrupos lado a lado |
| [G2 · Barras por item](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/relatorio_graficos_barras.html) | Um gráfico por pergunta, com o enunciado completo |
| [G2 · Pizzas por item](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/relatorio_graficos_pizza.html) | Os mesmos dados em pizza, com filtro por subgrupo |
| [G2 · Por subgrupo](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/graficos_egressos.html) | Comparação entre os subgrupos |
| [G3 · Professores](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/relatorio_g3_professores.html) | Respostas dos 2 docentes, com contagem e percentual |

No G2, os calouros estão divididos em três subgrupos: quem fez a UCE (EG, 8), quem já sabia programar por
outro caminho (CP, 11) e quem chegou sem saber (SC, 19). O arquivo `Anexo_Questoes_G2_Dicionario.csv` tem o
texto integral de cada pergunta.

## Como ler as cores

Algumas perguntas descrevem uma dificuldade ("o ritmo de Algoritmos I era rápido demais") e outras uma
facilidade ("eu conseguia identificar o que estudar"). Por isso cada item tem um sinal. Nos itens (+),
concordar é bom; nos itens (−), concordar é ruim. A cor segue esse sentido: verde para o lado favorável,
vermelho para o desfavorável e amarelo para quem marcou 3.

A exceção é o bloco de IA do G1. Ali não existe resposta certa, então azul é concordar e cinza é discordar.

## Sobre os dados

Nenhum dado aqui identifica participante. Os questionários não coletaram nome, e-mail nem IP, e o que aparece
são percentuais e contagens. A pesquisa foi aprovada pelo Comitê de Ética em Pesquisa da UEFS. As respostas
brutas não estão no repositório e não vão estar.

## Atualizar o site

Os relatórios são gerados pelos scripts em `analise/`, na pasta do projeto, que não fica pública. Depois de
copiar uma versão nova para cá, rode `python navegacao.py` para refazer a barra de navegação entre as
páginas e faça o commit. O GitHub Pages publica sozinho em um ou dois minutos.

---

Gabriel Sena Barbosa Silva e Pâmela Michele Cândida Cortez, UEFS, 2026.
