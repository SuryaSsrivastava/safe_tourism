from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account,profile


class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','first_name','last_name','age')


admin.site.register(Account, AccountAdmin)
admin.site.register(profile,ProfileAdmin)

