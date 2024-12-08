def all_variants(text):
    # Длина строки: n = len(text) определяет длину строки text.
    n = len(text)
    # Внешний цикл: for i in range(n) проходит по индексам от 0 до n-1.
    # Этот индекс i определяет длину подстроки, которую мы хотим создать.
    for i in range(n):
        # Внутренний цикл: for j in range(n - i) проходит по индексам от 0 до (n-i)-1.
        # Этот индекс j определяет начальную позицию подстроки.
        for j in range(n - i):
            # Создание подстроки: yield text[j:j+i+1] возвращает подстроку, начиная с индекса j и заканчивая на индексе j+i.
            # Это позволяет поочередно создавать и возвращать все возможные подстроки длины i+1.
            yield text[j:j + i + 1]


a = all_variants("abc")
for i in a:
    print(i)
