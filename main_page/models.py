from django.db import models
from django.contrib.auth.models import User

# user, total_check, new_accept, new_deny, new_dubls, update_accept, new_deny
class UsersStats(models.Model):

    user = models.ManyToManyField(User, verbose_name='Пользователь')
    user_nick = models.TextField(verbose_name='Имя пользователя', null=True)
    total_check = models.BigIntegerField(verbose_name='Всего просмотрено', null=True)
    new_accept = models.BigIntegerField(verbose_name='Поинтов одобрено', null=True)
    new_deny = models.BigIntegerField(verbose_name='Поинтов отклонено', null=True)
    new_dubls = models.BigIntegerField(verbose_name='Найдено дублей', null=True)
    update_accept = models.BigIntegerField(verbose_name='Обновлений одобрено', null=True)
    update_deny = models.BigIntegerField(verbose_name='Обновлений отклонено', null=True)

    class Meta:
        verbose_name = 'Статистика игрока'
        verbose_name_plural = 'Статистика игроков'

# user, lvl, exp
class UsersLvl(models.Model):

    user = models.ManyToManyField(User, verbose_name='Пользователь')
    user_nick = models.TextField(verbose_name='Имя пользователя', null=True)
    lvl = models.BigIntegerField(verbose_name='Уровень', null=True)
    exp = models.BigIntegerField(verbose_name='Опыт', null=True)

    class Meta:
        verbose_name = 'Уровень игрока'
        verbose_name_plural = 'Уровни игроков'

# encrypted, password, tgdata
class LinkPassword(models.Model):

    encrypted = models.TextField(verbose_name='Уникальный ключ')
    password = models.TextField(verbose_name='Пароль', null=True)
    tgdata = models.TextField(verbose_name='Инфа с тг', null=True)

    class Meta:
        verbose_name = 'Линк пароль'
        verbose_name_plural = 'Линк пароли'

# user, tgdata
class LinkData(models.Model):

    user = models.ManyToManyField(User, verbose_name='Пользователь')
    tgdata = models.TextField(verbose_name='Инфа с тг')

    class Meta:
        verbose_name = 'Линк дата'
        verbose_name_plural = 'Линк дата'
