from bs4 import BeautifulSoup

html_content = """
<!DOCTYPE html>
... (<html>
<head>
    <title>Мій HTML-файл</title>
</head>
<body>
    <header>
        <h1 class="main-heading">Мій html-сайт</h1>
    </header>
    <nav>
        <ul class="menu">
            <li><a href="#" class="menu-item">Головна</a></li>
            <li><a href="#" class="menu-item">Про нас</a></li>
            <li><a href="#" class="menu-item">Контакти</a></li>
        </ul>
    </nav>
    <main>
        <section class="content-section">
            <h2 class="section-heading">Мої послуги</h2>
            <ul class="service-list">
                <li class="service-item">Веб-дизайн</li>
                <li class="service-item">Тестування ігор</li>
            </ul>
        </section>
    </main>
    <footer>
        <p class="footer-text">© 2023</p>
    </footer>
</body>
"""

soup = BeautifulSoup(html_content, 'html.parser')

main_heading = soup.find('h1', class_='main-heading').text

menu_items = soup.find_all('a', class_='menu-item')
menu_texts = [item.text for item in menu_items]

print("Заголовок:", main_heading)
print("Меню:", menu_texts)
