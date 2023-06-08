def generateHtml(tabela):
    trs = ""
    for registro in tabela:
        trs = f'''{trs}
        <tr class="g4" id="1">
            <td>1</td>
            <td>{registro['nome_time']}</td>
            <td>{registro['pontos']}</td>
            <td>{registro['total_jogos']}</td>
            <td>{registro['vitorias']}</td>
            <td>{registro['saldo']}</td>
            <td>{registro['gols_pro']}</td>
        </tr>'''

    html = f'''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        <title>Tabela Brasileirão</title>
    </head>
    <body>
        <div class="central">
            <table>
                <tr>
                    <th colspan="2">Classificacao</th>
                    <th>P</th>
                    <th>J</th>
                    <th>V</th>
                    <th>SG</th>
                    <th>GP</th>
                </tr>
                {trs}
            </table>
        </div>
    </body>
    </html>
    '''

    # abre o arquivo HTML para escrita
    arq_html = open('index.html', 'w')

    # escrevendo no arquivo HTML
    arq_html.write(html)

    # fechando os arquivos
    arq_html.close()