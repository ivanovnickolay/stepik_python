# В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица.
# Просуммируйте все числа в ней. Теперь мы добавили разных тегов для изменения стиля отображения.
# Для доступа к ячейкам используйте возможности BeautifulSoup.

from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("https://stepik.org/media/attachments/lesson/209723/4.html").read().decode('utf-8')
s = str(html)
cnt = 0
soup = BeautifulSoup(s, "html.parser")
for f in soup.find_all('td'):
    cnt += int(f.text)
print(cnt)