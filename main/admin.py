from django.contrib import admin

from main.models import Section, Content, Subsection


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

    class Meta:
        verbose_name = 'Розділ'
        verbose_name_plural = 'Розділи'

@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ('section', 'type_subsection', 'title',)
    list_display_links = ('section', 'type_subsection', 'title')

    class Meta:
        verbose_name = 'Підрозділ'
        verbose_name_plural = 'Підрозділи'

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('tag', 'content')
    list_display_links = ('tag', 'content')

    class Meta:
        verbose_name = 'Вміст'
        verbose_name_plural = 'Вміст'