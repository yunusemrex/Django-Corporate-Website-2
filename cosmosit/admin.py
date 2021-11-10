from django.contrib import admin
from .models.hero import Hero
from .models.about import About
from .models.services_headers import ServiceHeaders
from .models.detail import Detail
from .models.call_action import CallAction
from .models.team import TeamMembers
from .models.contact import Contact
from .models.icons import Icons
from .models.features import Features
from .models.testimionals import Testimionals


@admin.register(Testimionals)
class TestimionalsAdmin(admin.ModelAdmin):
    list_display = ('value','description',)
    search_fields = ('value','description',)


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('hero1','h_service',)
    search_fields = ('hero1','h_service',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('header','content',)
    search_fields = ('header','content',)


@admin.register(ServiceHeaders)
class ServiceHeadersAdmin(admin.ModelAdmin):
    list_display = ('header1','header2',)
    search_fields = ('header1','header2',)


@admin.register(Detail)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name','title','detail',)
    search_fields = ('name','title','detail',)


@admin.register(CallAction)
class CallAction(admin.ModelAdmin):
    list_display = ('call_action_title','call_action_text',)
    search_fields = ('call_action_title','call_action_text',)


@admin.register(TeamMembers)
class Team(admin.ModelAdmin):
    list_display = ('full_name','jobs',)
    search_fields = ('full_name','jobs',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','subject','message','created_date',)
    search_fields = ('email','subject','message')


@admin.register(Icons)
class IconAdmin(admin.ModelAdmin):
    list_display = ('section',)
    search_fields = ('section',)


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)


