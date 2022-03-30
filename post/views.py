from django.shortcuts import render, HttpResponse,redirect
from . models import Catalogue, Product, Cart
from django.contrib import messages
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from datetime import date

# Create your views here.
def post(request):
    result = Catalogue.objects.all()
    ctx = {"res":result}
    return render(request,'main/dashboard.html', ctx)
def Entry(request,pk):
    result = Catalogue.objects.get(id=pk)
    pro = Product.objects.all()
    my_cart = Cart.objects.filter(user=request.user)
    ctx = {"res":result,"pro":pro,"cart":my_cart}
    return render(request, "entry.html", ctx)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
        
def product(request,pk):
    res = Product.objects.get(id=pk)
  
    quantity = ''
    if request.method == "POST":
        try:
            quantity = int(request.POST.get('quantity'))
        except ValueError:
            print("no input") 
            quantity = 1
            return redirect("product",pk=pk)
        try:
            if quantity == "":
                quantity = 1
            cart = Cart.objects.create(
                user = request.user,
                product = res,
                quantity = quantity,
                unit_price = res.price,
                total = (res.price * quantity),
            )
            messages.success(request, "Successfully Added to Cart!!")
            return redirect("entry",pk=pk)
        except Exception as e:
            messages.success(request, "You can only add an item once")
            return redirect("entry",pk=pk)
    
    ctx = {"res":res}
    return render(request, 'main/product.html',ctx)



def ViewPDF(request,pk):
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    my_cart = Cart.objects.filter(user=request.user)
    data = {"user":request.user,"cart":my_cart,"Today":d2}
    if request.method == "POST":
        pdf = render_to_pdf('pdf/invoice.html',data)
        return HttpResponse(pdf,content_type='application/pdf')
    return redirect("product",pk=pk)