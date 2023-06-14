import pdfkit


def generate_statistics(player_name):
    # Здесь должна быть ваша логика генерации статистики

    # Пример получения профиля игрока из базы данных
    player_profile = {}

    # Пример получения списка сессий игрока из базы данны

    # Инициализация HTML-страницы для генерации PDF
    path = f"player_stats_{player_name}.pdf"

    html = f'''
    <h1>Name {player_name}</h1>
    <p>Game count: {"TODO"}</p>
    <p>Win count: {"TODO"}</p>
    <p>Lose count: {"TODO"}</p>
    <p>Time in game: {"TODO"} минут</p>
    '''

    # Генерация PDF-документа с помощью библиотеки pdfkit
    pdfkit.from_string(html, path,
                       configuration=pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf'))

    # Возвращение URL, по которому можно получить сгенерированный PDF-документ
    return f'http://127.0.0.1:5000/open_pdf/{path}'
