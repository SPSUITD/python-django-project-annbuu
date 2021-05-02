from django.shortcuts import render
from .models import Messages1, Messages2, Messages3, Messages4, Messages5
from .forms import MessagesForm1, MessagesForm2, MessagesForm3, MessagesForm4, MessagesForm5
from django.http import HttpResponseRedirect

#дальше функции комнат чата
def firstroom(request):
  #проверка сохраненно ли в сессии имя и если нет вместо имени ставится заглушка
  if 'name1' not in request.session:
    request.session['name1'] = 'none-1_session'
  #проверка пришла ли форма
  if request.method == 'POST':
    form = MessagesForm1(request.POST)
    if form.is_valid():
      #сохраняем имя из формы в сессию, чтоб потом вставить в форму и перезагружаем страницу,
      #чтоб очистить форму
      #ставим истечение сессии по закрытию браузера
      request.session.set_expiry(0)
      request.session['name1'] = form.cleaned_data['name']
      form.save()
      form = MessagesForm1
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  #забиваем в переменную последние пять сообщений из базы данных
  messages = Messages1.objects.order_by('-id')[0:5]
  #проверяем на заглушку и если в сесси не она вставляем значение из сессии в поле имя
  #и делаем это поле readonly
  if request.session['name1'] == 'none-1_session':
    form = MessagesForm1()
  else:
    form = MessagesForm1(initial={'name': request.session['name1']})
    form.fields['name'].widget.attrs['readonly'] = True
  context = {'messages': messages, 'form': form}
  return render(request, 'chatrooms/first.html', context)

#дальше тоже самое

def secondroom(request):
  if 'name2' not in request.session:
    request.session['name2'] = 'none-1_session'
  if request.method == 'POST':
    form = MessagesForm2(request.POST)
    if form.is_valid():
      request.session.set_expiry(0)
      request.session['name2'] = form.cleaned_data['name']
      form.save()
      form = MessagesForm2
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  messages = Messages2.objects.order_by('-id')[0:5]
  if request.session['name2'] == 'none-1_session':
    form = MessagesForm2()
  else:
    form = MessagesForm2(initial={'name': request.session['name2']})
    form.fields['name'].widget.attrs['readonly'] = True
  context = {'messages': messages, 'form': form}
  return render(request, 'chatrooms/second.html', context)


def thirdroom(request):
  if 'name3' not in request.session:
    request.session['name3'] = 'none-1_session'
  if request.method == 'POST':
    form = MessagesForm3(request.POST)
    if form.is_valid():
      request.session.set_expiry(0)
      request.session['name3'] = form.cleaned_data['name']
      form.save()
      form = MessagesForm3
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  messages = Messages3.objects.order_by('-id')[0:5]
  if request.session['name3'] == 'none-1_session':
    form = MessagesForm3()
  else:
    form = MessagesForm3(initial={'name': request.session['name3']})
    form.fields['name'].widget.attrs['readonly'] = True
  context = {'messages': messages, 'form': form}
  return render(request, 'chatrooms/third.html', context)


def fourthroom(request):
  if 'name4' not in request.session:
    request.session['name4'] = 'none-1_session'
  if request.method == 'POST':
    form = MessagesForm4(request.POST)
    if form.is_valid():
      request.session.set_expiry(0)
      request.session['name4'] = form.cleaned_data['name']
      form.save()
      form = MessagesForm4
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  messages = Messages4.objects.order_by('-id')[0:5]
  if request.session['name4'] == 'none-1_session':
    form = MessagesForm4()
  else:
    form = MessagesForm4(initial={'name': request.session['name4']})
    form.fields['name'].widget.attrs['readonly'] = True
  context = {'messages': messages, 'form': form}
  return render(request, 'chatrooms/fourth.html', context)


def fifthroom(request):
  if 'name5' not in request.session:
    request.session['name5'] = 'none-1_session'
  if request.method == 'POST':
    form = MessagesForm5(request.POST)
    if form.is_valid():
      request.session.set_expiry(0)
      request.session['name5'] = form.cleaned_data['name']
      form.save()
      form = MessagesForm5
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  messages = Messages5.objects.order_by('-id')[0:5]
  if request.session['name5'] == 'none-1_session':
    form = MessagesForm5()
  else:
    form = MessagesForm5(initial={'name': request.session['name5']})
    form.fields['name'].widget.attrs['readonly'] = True
  context = {'messages': messages, 'form': form}
  return render(request, 'chatrooms/fifth.html', context)