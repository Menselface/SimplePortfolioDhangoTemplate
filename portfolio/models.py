from django.db import models

from cloudinary.models import CloudinaryField



class MyName(models.Model):
    title = models.CharField(max_length=50, verbose_name='Full Name')
    about = models.TextField(max_length=150, verbose_name='Your skills')
    profile_photo = CloudinaryField(
        folder=lambda instance: f'my_portfolio.com/header',
        blank=True, null=True, verbose_name='Your photo here'
    )
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = 'name'
        verbose_name = "Full Name"
        verbose_name_plural = "Full Name"


class SocialMedias(models.Model):
    icon = models.CharField(max_length=20, verbose_name='Icon-name')
    url = models.CharField(max_length=150, verbose_name='URL')
    
    def __str__(self):
        return f"{self.icon}"
    
    class Meta:
        db_table = 'SocialMedias'
        verbose_name = "SocialMedias"
        verbose_name_plural = "SocialMedias"


class About(models.Model):
    title = models.CharField(max_length=150, verbose_name='H2 title')
    second_title = models.CharField(max_length=150, verbose_name='H3 title')
    first_about = models.TextField(max_length=450, verbose_name='About')
    second_about = models.TextField(max_length=450, verbose_name='Second paragraph')
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = 'About'
        verbose_name = "About"
        verbose_name_plural = "About"


class AboutLeftSection(models.Model):
    key = models.CharField(max_length=150, verbose_name='Key:')
    value = models.TextField(max_length=450, verbose_name='Value')
    
    def __str__(self):
        return f"{self.key}"
    
    class Meta:
        db_table = 'Additional About Info '
        verbose_name = "Additional About Info "
        verbose_name_plural = "Additional About Info "


class Resume(models.Model):
    project_name = models.CharField(max_length=150, verbose_name='Project name')
    project_link = models.CharField(max_length=150, verbose_name='Project link')
    description = models.TextField(max_length=450, verbose_name='Description')
    
    def __str__(self):
        return f"{self.project_name}"
    
    class Meta:
        db_table = 'Resume'
        verbose_name = "Resume"
        verbose_name_plural = "Resume"


class Services(models.Model):
    icon = models.CharField(max_length=20, verbose_name='Icon-name')
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField(max_length=450, verbose_name='Description')
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = 'Services'
        verbose_name = "Services"
        verbose_name_plural = "Services"


class Skills(models.Model):
    title = models.CharField(max_length=40, verbose_name='Title')
    description = models.CharField(max_length=5, verbose_name='Percent')
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = 'Skills'
        verbose_name = "Skills"
        verbose_name_plural = "Skills"


class WorkExemples(models.Model):
    name = models.CharField(max_length=140, verbose_name='Name')
    description = models.TextField(max_length=450, verbose_name='Description')
    link = models.CharField(max_length=100, verbose_name='Link')
    profile_photo = CloudinaryField(
        folder=lambda instance: f'my_portfolio.com/Works',
        blank=True, null=True, verbose_name='Your work here'
    )
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = 'Works'
        verbose_name = "Works"
        verbose_name_plural = "Works"