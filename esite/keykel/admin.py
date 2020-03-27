from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

# Register your registration related models here.

from .models import KeyKel

class KeyKelAdmin(ModelAdmin):
    model = KeyKel
    menu_label = "KeyKel"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False

    # Listed in the registration overview
    list_display = ('is_active', 'key_name', 'key_from', 'key_to')
    search_fields = ('is_active', 'key_name', 'key_from', 'key_to')

modeladmin_register(KeyKelAdmin)
