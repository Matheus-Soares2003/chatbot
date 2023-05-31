# Chatbot de Futebol Brasileiro
Projeto do 5º semestre da uninove
O objetivo desse projeto é criar um chatbot inteligente capaz de responder perguntas sobre os 40 clubes do futebol brasileiro que compõem a **série A e série B** do **Campeonato Brasileiro**.
Aqui estão as instruções e algumas explicações de como funciona este chatbot.

## Dados
Neste projeto os dados foram coletados de diversas fontes confiáveis e foram armazenados no formato **JSON** para facilitar a estruturação dos dados e a pesquisa dos mesmos pelo nosso chatbot.
Nesse JSON é possível encontrar informações sobre:
* Os 40 times que compõem a série A e B do Campeonato Brasileiro;
* Os **ídolos** de cada time;
* Os **rivais** de cada time;
* O **mascote** de cada time;
* Os **jogadores** que estão no elenco de cada time;
* Seus **títulos**;
* Algumas **curiosidades** sobre cada time;

## Instruções de uso
Nosso chatbot está em sua primeira versão portanto ainda é um pouco limitado, mas ainda consegue atender muito bem as suas necessidades se você seguir estas instruções na hora de mandar sua pergunta ao chatbot:
1. Faça perguntas sobre um dos tópicos pesquisáveis (ídolos, rivais, mascote, jogadores, titulos e curiosidade) e sobre algum dos times que estão na base de dados (os 40 times da série A e B);

2. Para times com sua UF ao lado do nome (exemplo: Atlético-MG e Athletico-PR) escreva sem espaços antes e depois do hífen e coloque a sigla do estado desse time. (Atlético Mineiro -> Atlético-MG);

3. Por enquanto o nome dos times devem estar escritos sem erros e sem apelidos;

## Compilação e Execução do código
Caso você queira executar o código em sua máquina, será necessário ter algum software para a compilção do próprio. Recomendo usar o Visual Studio Code.
Além disso, no VScode deve estar instalado o pluggin do live server para rodar a parte do Front-End em **localhost** e também um compilador python.
Para execução do código em python, a única biblioteca que precisará ser instalada é o Flask e o flask.cors.
### No cmd digite:
* **pip install flask**;
* **pip install flask.cors**

Rode o código python e o live server e você estará pronto para testar o chatbot :D
