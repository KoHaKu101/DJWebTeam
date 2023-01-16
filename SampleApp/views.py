from django.shortcuts import render, HttpResponse
# Create your views here.
def FirstWeb(request):
    name = "Phichitchai"
    surname = "Thammachai"
    age = 21
    salary = 15000.0
    status = "Student"
    context = { 'name' : name,
                'surname' : surname,
                'age' : age,
                'salary' : salary,
                'status' : status,
                }
    return render(request,'FirstWeb.html',context)
def secondpage(request):
    name = "Pen"
    price = 10.50
    description = "ปากกาลูกลื่นสีน้ำเงิน หัว 0.5 มิลลิเมตร"
    quantity = 300
    return render(request, 'secondpage.html',
                  {'name': name, 'price': price, 'description': description, 'quantity': quantity})
