from django.contrib import admin

from portfolio.models import *


@admin.register(MyName)
class MyNameAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialMedias)
class SocialMediasAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutLeftSection)
class AboutLeftSectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkExemples)
class WorkExemplesAdmin(admin.ModelAdmin):
    pass
