# Вам дан шаблон для функции test_substring, которая принимает два значения: full_string и substring.
#
# Функция должна проверить вхождение строки substring в строку full_string с помощью оператора
# assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.
#
# Важно! Формат ошибки должен точно совпадать с приведенным в примере, чтобы его засчитала
# проверяющая система!

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected {substring} to be substring of {full_string}"


test_substring("fulltext", "some_value")
