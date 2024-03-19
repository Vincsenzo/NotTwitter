from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Message
from .forms import MessageForm


def messages(request):
    if request.method == 'POST':
        message_post = request.POST['message']
        sender = request.user
        Message.objects.create(message_content=message_post, sender_name=sender)
        return redirect('messaging:messages')

    messages = Message.objects.all().order_by('-time_sent')
    if request.GET.get('all') == 'true':
        messages = messages
    else:
        messages = messages[:66]

    current_user = request.user
    context = {'messages': messages, 'current_user': current_user}
    return render(request, 'messaging/message.html', context)
