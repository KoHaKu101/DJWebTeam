from django.shortcuts import render
def secondpage(request):
    name = "Pen"
    price = 10.50
    description = "ปากกาลูกลื่นสีน้ำเงิน หัว 0.5 มิลลิเมตร"
    quantity = 300
    return render(request, 'secondpage.html',
                  {'name': name, 'price': price, 'description': description, 'quantity': quantity})
# Create your views here.
