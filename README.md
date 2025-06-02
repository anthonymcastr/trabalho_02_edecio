# 📊 Análise de Campeões do League of Legends (até 2024)

Este projeto em Python permite realizar diversas análises sobre campeões do jogo **League of Legends**, utilizando um arquivo CSV contendo dados como nome, classe, tipo de recurso, custo em Blue Essence (BE) e data de lançamento.

## 📁 Arquivo necessário

Certifique-se de que o arquivo `personagens.csv` esteja presente no mesmo diretório do script. Ele deve conter os seguintes campos:

- `Name`
- `Classes`
- `Blue Essence`
- `Release Date`
- `Resourse type`

## 🚀 Funcionalidades

Ao rodar o script, um menu interativo será exibido com as seguintes opções:

1. **Busca de personagens por preço**  
   Filtra campeões com base no custo em Blue Essence, listando-os em ordem alfabética.

2. **Busca de personagens por ano de lançamento**  
   Retorna os campeões lançados em um ano específico.

3. **Todos os personagens agrupados por ano de lançamento**  
   Agrupa todos os campeões por ano de lançamento, mostrando o total por ano.

4. **Lista de classes e valor total de Blue Essence**  
   Agrupa campeões por classe e exibe o total de campeões e soma de seus preços.

5. **Análise de personagem sem determinado atributo**  
   Filtra campeões de uma classe específica que **não possuem** um determinado atributo (ex: mana, energy).

6. **Campeões que pertencem a duas classes específicas**  
   Lista campeões que pertencem simultaneamente a **duas** classes informadas.

7. **Finalizar**  
   Encerra o programa.

## 💻 Como executar

1. Instale o Python 3.9 ou superior no seu sistema, se ainda não tiver.
2. Certifique-se de que o arquivo `personagens.csv` está no mesmo diretório do script.
3. Execute o programa com o seguinte comando:

```bash
python nome_do_arquivo.py

📌 Observações
O script trata automaticamente dados faltantes em campos críticos como Classes, Blue Essence, e Release Date.

É altamente recomendável utilizar um dataset bem formatado para evitar resultados inconsistentes.

📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.
