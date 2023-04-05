from django.db import models
from django.contrib.auth.models import User

# user, total_check, new_accept, new_deny, new_dubls, update_accept, new_deny
class UsersStats(models.Model):

    user = models.ManyToManyField(User, verbose_name='Пользователь')
    user_nick = models.TextField(verbose_name='Имя пользователя')
    total_check = models.BigIntegerField(verbose_name='Всего просмотрено')
    new_accept = models.BigIntegerField(verbose_name='Поинтов одобрено')
    new_deny = models.BigIntegerField(verbose_name='Поинтов отклонено')
    new_dubls = models.BigIntegerField(verbose_name='Найдено дублей')
    update_accept = models.BigIntegerField(verbose_name='Обновлений одобрено')
    update_deny = models.BigIntegerField(verbose_name='Обновлений отклонено')

    class Meta:
        verbose_name = 'Статистика игрока'
        verbose_name_plural = 'Статистика игроков'

# user, lvl, exp
class UsersLvl(models.Model):

    user = models.ManyToManyField(User, verbose_name='Пользователь')
    user_nick = models.TextField(verbose_name='Имя пользователя')
    lvl = models.BigIntegerField(verbose_name='Уровень')
    exp = models.BigIntegerField(verbose_name='Опыт')

    class Meta:
        verbose_name = 'Уровень игрока'
        verbose_name_plural = 'Уровни игроков'

# # user, lvl, exp
# class UsersLvl(models.Model):

#     user = models.ManyToManyField(User, verbose_name='Пользователь')
#     lvl = models.BigIntegerField(verbose_name='Уровень')
#     exp = models.BigIntegerField(verbose_name='Опыт')

#     class Meta:
#         verbose_name = 'Уровень игрока'
#         verbose_name_plural = 'Уровни игроков'
