from django.shortcuts import render
from django.conf import settings
from .forms import TelegramMessageForm
from telegram import Bot

# Create your views here.
async def send_telegram_message(request):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    if request.method == 'POST':
        form = TelegramMessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']

            try:
                # Асинхронная отправка сообщения
                await bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)
                success = True
            except Exception as e:
                success = False
                print(f"Ошибка отправки: {e}")

            return render(request, 'telegram_app/confirmation.html', {'success': success})

    else:
        form = TelegramMessageForm()

    return render(request, 'telegram_app/send_message.html', {'form': form})