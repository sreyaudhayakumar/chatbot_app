from django.shortcuts import render
from django.http import JsonResponse
import spacy


nlp = spacy.load('en_core_web_sm')

responses = {
    'hi': 'Hello there!',
    'name': 'I am a chatbot built with Django and spaCy.',
    'favorite_food': 'I do not have preferences as I am just a program.',
    'how_are_you': 'I am just a program, so I don\'t have feelings, but thank you for asking!',
    'weather': 'I don\'t have real-time information, but you can check your local weather on a weather website.',
    'goodbye': 'Goodbye! If you have more questions, feel free to ask.',
    'default': 'I did not understand that. Can you please rephrase?',
    'time': 'I don\'t have real-time clock information, but you can check the time on your device.',
    'joke': 'Sure, here is a joke: Why don\'t scientists trust atoms? Because they make up everything!',
    'meaning_of_life': 'The meaning of life is a philosophical question. Many people find their own meaning and purpose.',
}

def home(request):
    return render(request, 'index.html')

def getResponse(request):
    
    userMessage = request.GET.get('userMessage')

    doc = nlp(userMessage.lower())

    
    if any(token.text == 'hi' for token in doc):
        botResponse = responses['hi']
    elif any(token.text == 'name' for token in doc):
        botResponse = responses['name']
    elif any(token.text == 'favorite' and doc[token.i + 1].text == 'food' for token in doc):
        botResponse = responses['favorite_food']
    elif any(token.text == 'how' and doc[token.i + 1].text == 'are' and doc[token.i + 2].text == 'you' for token in doc):
        botResponse = responses['how_are_you']
    elif any(token.text == 'weather' for token in doc):
        botResponse = responses['weather']
    elif any(token.text == 'goodbye' for token in doc):
        botResponse = responses['goodbye']
    elif any(token.text == 'time' for token in doc):
        botResponse = responses['time']
    elif any(token.text == 'joke' for token in doc):
        botResponse = responses['joke']
    elif any(token.text == 'meaning' and doc[token.i + 1].text == 'of' and doc[token.i + 2].text == 'life' for token in doc):
        botResponse = responses['meaning_of_life']
    else:
        botResponse = responses['default']

    
    return JsonResponse({'botResponse': botResponse})
