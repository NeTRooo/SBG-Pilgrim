from django.contrib import admin
from .models import UsersStats, UsersLvl

#  
#  configuring the display
#  

# user, total_check, new_accept, new_deny, new_dubls, update_accept, new_deny
class UsersStatsAdmin(admin.ModelAdmin):
    list_display = ('user_nick', 'total_check')
    list_display_links = ('user_nick', 'total_check')
    search_fields = ('user_nick', 'total_check')

# user, lvl, exp
class UsersLvlAdmin(admin.ModelAdmin):
    list_display = ('user_nick', 'lvl', 'exp')
    list_display_links = ('user_nick', 'lvl', 'exp',)
    search_fields = ('user_nick', 'lvl', 'exp')

#  
#  Register model
#  

admin.site.register(UsersStats, UsersStatsAdmin)
admin.site.register(UsersLvl, UsersLvlAdmin)