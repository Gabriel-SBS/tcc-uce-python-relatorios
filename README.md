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
| [G3 · Professores](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/relatorio_g3_professores.html) | Síntese das respostas dos 2 docentes. Com dois respondentes, qualquer contagem por item mostraria a resposta de cada um, então não há gráficos por item |
| [Respostas abertas](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/relatorio_abertas.html) | Categorias das respostas abertas dos mentores (G1) e dos calouros (G2) e o livro de códigos completo (Apêndice D) |
| [Fase 3 · Notas](https://gabriel-sbs.github.io/tcc-uce-python-relatorios/relatorio_fase3_notas.html) | Desempenho agregado no 1º semestre por subgrupo nas sete disciplinas (média, DP, mediana, mín.–máx., reprovações e gráfico) |

No G2, os calouros estão divididos em três subgrupos: quem fez a UCE (EG, 8), quem já sabia programar por
outro caminho (CP, 11) e quem chegou sem saber (SC, 19). O arquivo `Anexo_Questoes_G2_Dicionario.csv` tem o
texto integral de cada pergunta.

## Como ler as cores

Algumas perguntas descrevem uma dificuldade ("o ritmo de Algoritmos I era rápido demais") e outras uma
facilidade ("eu conseguia identificar o que estudar"). Por isso cada item tem um sinal. Nos itens (+),
concordar é bom; nos itens (−), concordar é ruim. A cor segue esse sentido: verde para o lado favorável,
vermelho para o desfavorável e amarelo para quem marcou 3.

No bloco de IA do G1, a referência é o uso de IA por iniciantes: verde é visão favorável a esse uso e
vermelho é visão crítica.

## Acessibilidade

Todas as páginas têm, na barra de navegação:
- **Modo daltonismo**: troca verde por azul, vermelho por laranja e amarelo por cinza em tabelas, gráficos e imagens;
- **Letra maior**: aumenta o texto e os gráficos da página;
- **Pular para o conteúdo**: aparece no primeiro Tab, para quem navega pelo teclado.

As duas escolhas ficam salvas no navegador. Os gráficos desenhados em canvas trazem uma descrição com os
rótulos e os valores, lida por leitores de tela; o contorno de foco fica sempre visível; as tabelas largas
rolam sozinhas no celular, sem empurrar a página para o lado; e quem pediu menos animação ao sistema
operacional vê os gráficos sem animação.

Os itens do G1 aparecem com códigos I01, I02 etc. No artigo, os códigos M01 a M43 identificam as falas dos
mentores, e não os itens.

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
