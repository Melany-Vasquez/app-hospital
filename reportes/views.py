from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from cita.models import Cita
import inicio.views
from django.contrib.auth.decorators import login_required


@login_required
def reporte_citas(request):
    print('IMPRIME EL PDF')
    citas_con_covid = Cita.objects.filter(estado_covid='S')
    citas_sin_covid = Cita.objects.filter(estado_covid='N')
    
    total = citas_con_covid.count() + citas_sin_covid.count()

    html_string = render_to_string('reportes/reporte_citas.html', {
        'citas_con_covid': citas_con_covid,
        'citas_sin_covid': citas_sin_covid,
        'total': total
    })

    # Genera el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_citas.pdf"'
    HTML(string=html_string).write_pdf(response)

    return response
