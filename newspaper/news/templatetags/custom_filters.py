from django import template


register = template.Library()


@register.filter(name='censor')  # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def censor(value):  # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
    # badwords = ["asshole","idiot"]
    badwords = open('bad_words.txt', "r", encoding="utf-8")
    n = ""
    for i in badwords:
        i = i.replace(",", "")
        n += i
    badwords = n.split()

    for badword in badwords:
        value = value.replace(badword,"*"*len(badword))
    return value  # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон