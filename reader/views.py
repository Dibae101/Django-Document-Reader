from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic import ListView
from .models import Document

class DocumentListView(ListView):
    model = Document
    template_name = 'reader/main.html'

def document_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    document = get_object_or_404(Document, pk=pk)
    
    template_path = 'reader/document2.html'
    context = {'document': document}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #to avoid download
    # response['Content-Disposition'] = 'attachment; filename="document.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="document.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_pdf_view(request):
    template_path = 'reader/document.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #to avoid download
    # response['Content-Disposition'] = 'attachment; filename="document.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="document.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
