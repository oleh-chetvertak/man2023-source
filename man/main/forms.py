from django.forms import Form, Textarea, TextInput, CharField, FileField, RadioSelect


class MainForm(Form):
    text = CharField(label='', widget=Textarea(
        attrs={'placeholder': 'Текст, який буде аналізуватись', 'rows': 10, 'id': 'textar'}), required=False)
    file = FileField(label='', required=False)


class TextForm(MainForm):
    CHOICES = [
        ('1', 'Часто вживані слова'),
        ('2', 'Рідко вживані слова'),
    ]
    rad = CharField(label='', widget=RadioSelect(choices=CHOICES))


class SearchForm(MainForm):
    name = CharField(widget=TextInput(), label='Пошуковий запит')


class NLTKForm(MainForm):
    min_ton = CharField(widget=TextInput(attrs={'class': 'minmax-input'}), label='Мінімальний настрій (у процентах від -100 до 100)', required=False)
    max_ton = CharField(widget=TextInput(attrs={'class': 'minmax-input'}), label='Максимальний настрій', required=False)


class SettingsForm(Form):
    group_size = CharField(widget=TextInput(attrs={'class': 'minmax-input', 'type': 'number'}), label='Розмір групи слів (5 за замовчуванням, ЧВС)', required=False)
    freq = CharField(widget=TextInput(attrs={'class': 'minmax-input', 'type': 'number'}), label='Частота рідкісних слів (1 за замовчуванням)', required=False)