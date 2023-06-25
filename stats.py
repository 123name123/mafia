import pdfkit


def generate_statistics(player_data):
    path = f"player_stats_{player_data[0]}.pdf"

    html = f'''
    <h1>Name: {player_data[0]}</h1>
    <p>Game count: {player_data[1]}</p>
    <p>Win count: {player_data[2]}</p>
    <p>Lose count: {player_data[3]}</p>
    <p>Time in game: {player_data[4]} minutes</p>
    '''

    # Генерация PDF-документа с помощью библиотеки pdfkit
    pdfkit.from_string(html, 'static/' + path,
                       configuration=pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf'))

    # Возвращение URL, по которому можно получить сгенерированный PDF-документ
    return f'http://127.0.0.1:3001/open_pdf/{path}'
