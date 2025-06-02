📊 Análise de Campeões do League of Legends (até 2024)
Este projeto em Python permite realizar diversas análises sobre campeões do jogo League of Legends, utilizando um arquivo CSV contendo dados como nome, classe, tipo de recurso, custo em Blue Essence (BE) e data de lançamento.

📁 Arquivo necessário
Certifique-se de que o arquivo personagens.csv esteja presente no mesmo diretório do script. Ele deve conter os seguintes campos:

Name

Classes

Blue Essence

Release Date

Resourse type

🚀 Funcionalidades
Ao rodar o script, um menu interativo será exibido com as seguintes opções:

Busca de personagens por preço
Filtra campeões com base no custo em Blue Essence, listando-os em ordem alfabética.

Busca de personagens por ano de lançamento
Retorna os campeões lançados em um ano específico.

Todos os personagens agrupados por ano de lançamento
Agrupa todos os campeões por ano de lançamento, mostrando total por ano.

Lista de classes e valor total de Blue Essence
Agrupa campeões por classe e exibe o total de campeões e soma de seus preços.

Análise de personagem sem determinado atributo
Filtra campeões de uma classe específica que não possuem um atributo (ex: mana, energy).

Campeões que pertencem a duas classes específicas
Lista campeões que pertencem simultaneamente a duas classes informadas.

Finalizar
Encerra o programa.

💻 Como executar
Instale o Python 3.9+ no seu sistema, se ainda não tiver.

Certifique-se de que o arquivo personagens.csv está no mesmo diretório do script.

Execute o programa com o seguinte comando:

bash
Copiar
Editar
python nome_do_arquivo.py
🧠 Tecnologias usadas
Python 3

Biblioteca csv

defaultdict da collections para agrupamentos

📌 Observações
O script trata automaticamente dados faltantes em campos críticos como Classes, Blue Essence, e Release Date.

É altamente recomendável utilizar um dataset bem formatado para evitar resultados inconsistentes.

📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.
