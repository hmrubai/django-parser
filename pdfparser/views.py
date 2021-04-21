from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf import settings

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # file = settings.MEDIA_DIR + '/page.png'
        # text = pytesseract.image_to_string(file)
        # context['text'] = text

        return context

class UploadFileView(TemplateView):
    template_name = "upload.html"
    
    def post(self, request, *args, **kwargs):
        text = ''
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        if(filename):
            file = settings.MEDIA_DIR + '/' + filename
            text = pytesseract.image_to_string(file)
        
        writefile = open(os.path.join(settings.MEDIA_DIR, filename + '_text.txt'), 'a')
        writefile.write("\n" + text)
        writefile.close()

        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'text': text
        })
        return render(request, 'upload.html')

