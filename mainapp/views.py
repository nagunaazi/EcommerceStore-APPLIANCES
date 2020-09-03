from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from mainapp.forms import ProductForm
import json


@method_decorator(csrf_exempt,name='dispatch')
class InsertOneProduct(View):
    def post(self,request):
        data = request.body
        json_data = json.loads(data)
        pf = ProductForm(json_data)
        if pf.is_valid():
            pf.save()
            json_data = json.dumps({"success":"Product is saved"})
        else:
            json_data = json.dumps(pf.errors)
        return HttpResponse(json_data, content_type="application/json")