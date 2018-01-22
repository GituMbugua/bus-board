from django.http import HttpResponse
from django.views.generic import View
from final.utils import render_to_pdf 
from bus_board.views import bus_details
from bus_board.models import Ticket

# class GeneratePdf(View):

#     def get(self, request, *args, **kwargs):

#         # data = {
#         #     'today': datetime.date.today(), 
#         #     'amount': 39.99,
#         #     'customer_name': 'Cooper Mann',
#         #     'order_id': 1233434,
#         # }
#         # print(Ticket.get_single_ticket(ticket_id))

#         pdf = render_to_pdf('pdf/ticket.html')

#         return HttpResponse(pdf, content_type='application/pdf')



def generate_view(request, ticket_id):

    # data = {
    #     'today': datetime.date.today(), 
    #     'amount': 39.99,
    #     'customer_name': 'Cooper Mann',
    #     'order_id': 1233434,
    # }
    gotten_ticket = Ticket.get_single_ticket(ticket_id)

    pdf = render_to_pdf('pdf/ticket.html', {'gotten_ticket':gotten_ticket})

    if pdf:

        response = HttpResponse(pdf, content_type='application/pdf')

        filename = "Ticket_%s.pdf" %(gotten_ticket.ticket_number)

        content = "inline; filename='%s'"%(filename)

        download = request.GET.get("download")

        if download:

            content = "attachment; filename='%s'"%(filename)

        response['Content-Disposition'] = content

        return response

    return HttpResponse('Not Found')