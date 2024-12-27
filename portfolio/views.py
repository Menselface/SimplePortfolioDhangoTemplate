import os

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from portfolio.forms import ContactForm
from portfolio.models import MyName, SocialMedias, AboutLeftSection, About, Resume, Services, Skills, WorkExemples


def index(request):
    name = MyName.objects.first()
    social_medias = SocialMedias.objects.all()
    about = About.objects.first()
    additional_info = AboutLeftSection.objects.all()
    resume = Resume.objects.all()
    services = Services.objects.all()
    skills = Skills.objects.all()
    works = WorkExemples.objects.all()
    context = {
        'title': 'Home',
        'name': name.title,
        'skills_about': name.about,
        'photo': name.profile_photo,
        'social_medias': social_medias,
        'about': about,
        'left_info': additional_info,
        'resume': resume,
        'services': services,
        'skills': skills,
        'works': works
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            send_message(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['message']
            )
            context['sucess'] = "Thank you for your message!"
    else:
        context['form'] = ContactForm()
    return render(request, 'index.html', context)


def send_message(name, email, message=None):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {
        'name': name,
        'email': email,
        'message': message,
    }
    subject = 'Новое сообщение с вашего сайта'
    from_email = "webselface@mail.com"
    text_content = text.render(context)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [os.getenv('MY_MAIL')])
    msg.attach_alternative(text_content, "text/html")
    msg.send()