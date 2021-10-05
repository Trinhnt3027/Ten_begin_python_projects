from django.shortcuts import render
from googletrans import Translator

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['src_text']
        print("Src text: ", original_text)

        trans = Translator()
        des_text = trans.translate(text=original_text, dest='vi').text
        print("Des text to Vietnamese: ", des_text)
        
        return render(request, 'translator.html', {'src_text': original_text, 'des_text': des_text})
    else:
        return render(request, 'translator.html')

# Create your views here.
