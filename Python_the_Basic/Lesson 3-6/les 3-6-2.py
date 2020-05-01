# В этой задаче вам необходимо воспользоваться API сайта artsy.net
#
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
#
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
#
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый
# год рождения, выведите их имена в лексикографическом порядке.
#
# Работа с API Artsy
# Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для
# получения доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить
# уникальный ключ (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа.
# Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу
# документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться,
# создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.
# После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как
# можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.
# Примечание:
# ﻿В качестве имени художника используется параметр sortable_name в кодировке UTF-8.
#
# Пример входных данных:
# 4d8b92b34eb68a1b2c0003f4
# 537def3c139b21353f0006a6
# 4e2ed576477cc70001006f99
#
# Пример выходных данных:
# Abbott Mary
# Warhol Andy
# Abbas Hamra

import requests
import json

result = {}

client_id = '934a9be53e6e33eb3745'
client_secret = '0a66f23588889d8b154c55feec36479e'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

with open('test 3-6-2.txt') as f:
    for uid in f:

        url_token = 'https://api.artsy.net/api/artists/'
        # инициируем запрос с заголовком
        # r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)
        r = requests.get("https://api.artsy.net/api/artists/"+uid.strip(), headers=headers)
        # разбираем ответ сервера
        res_request = json.loads(r.text)
        # формируем словарь {год рождения: [имена]}
        if res_request['birthday'] in result:
            # если год рождения уже есть в списке то
            t = result[res_request['birthday']]
            # добавляем в список новую фамилию
            t.append(res_request['sortable_name'])
            result[res_request['birthday']] = 0
            result[res_request['birthday']] = t
        else:
            # если нет года раождения в списке то
            # создаем новый список добавляем новую фамилию
            r = list()
            r.append(res_request['sortable_name'])
            result[res_request['birthday']] = r

# сортируем ключи о возрастанию
list_keys = list(result.keys())
list_keys.sort()
for y in list_keys:
    name = result.get(y)
    for i in range(len(name)):
        print(name[i])
