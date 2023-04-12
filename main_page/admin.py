from django.contrib import admin
from .models import UsersStats, UsersLvl, LinkPassword, LinkData

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

# encrypted, password, tgdata
class LinkPasswordAdmin(admin.ModelAdmin):
    list_display = ('encrypted', 'password', 'tgdata')
    list_display_links = ('encrypted', 'password', 'tgdata')
    search_fields = ('encrypted', 'password', 'tgdata')

# user, tgdata
class LinkDataAdmin(admin.ModelAdmin):
    list_display = ('tgdata',)
    list_display_links = ('tgdata',)
    search_fields = ('tgdata',)

#  
#  Register model
#  

admin.site.register(UsersStats, UsersStatsAdmin)
admin.site.register(UsersLvl, UsersLvlAdmin)
admin.site.register(LinkPassword, LinkPasswordAdmin)
admin.site.register(LinkData, LinkDataAdmin)