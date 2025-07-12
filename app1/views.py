from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import *
# Create your views here.


def login(request):
    if request.method == "POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            data=UserRegister.objects.get(email=email1,password=password1)
            if data:
                request.session['email']=data.email
                print(request.session['email'])
                return redirect('index')
            else:
                return render(request,'login.html',{'message':'Invalid email or password'})
        except:
            return render(request,'login.html',{'message':'Invalid email or password'})
    return render(request,'login.html')

def logout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('index')
    else:
        return redirect('index')

def index(request):
    if 'email' in request.session:
        a=request.session['email']
        data=Category.objects.all()
        return render(request,'base.html',{'data':data,'a':a})
    else:
        data=Category.objects.all()
        return render(request,'base.html',{'data':data})

def productall(request):
    if 'email' in request.session:
        a=request.session['email']
        data=Product.objects.all()
        return render(request,'productall.html',{'data':data,'a':a})
    else:
        data=Product.objects.all()
        return render(request,'productall.html',{'data':data})

def productcategorywise(request,id):
    if 'email' in request.session:
        a=request.session['email']
        data=Product.objects.filter(category=id)
        return render(request,'productall.html',{'data':data,'a':a})
    else:
        data=Product.objects.filter(category=id)
        return render(request,'productall.html',{'data':data})  

def singleproduct(request,id):
    if 'email' in request.session:
        a=request.session['email']
        data=Product.objects.get(pk=id)
        return render(request,'singleproduct.html',{'data':data,'a':a})
    else:
        data=Product.objects.get(pk=id)
        return render(request,'singleproduct.html',{'data':data})
    
def register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        password1=request.POST['password']
        phone1=request.POST['phone']
        address1=request.POST['address']
        print(name1,email1,password1,address1,phone1)
        data=UserRegister(name=name1,email=email1,password=password1,phone=phone1,address=address1)
        a=UserRegister.objects.filter(email=email1)
        if len(a)==0:
            data.save()
            return redirect('login1')
        else:
            return render(request,'register.html',{'message':"user alredy exist"}) 

    return render(request,'register.html')  
    
def profile(request):
    if 'email' in request.session:
        a=request.session['email']
        user_profile = UserRegister.objects.get(email=a)
        user_orders = Ordermodel.objects.filter(userEmail=a)
        prolist=[]
        for i in user_orders:
            pro={}
            print(111111)
            productdata=Product.objects.get(id=i.productid)
            pro['img']=productdata.img
            pro['id']=i.productid
            pro['name']=productdata.name
            pro['orderDate']=i.orderDate
            pro['productqty']=i.productqty
            pro['transactionId']=i.transactionId
            pro['paymentMethod']=i.paymentMethod
            pro['orderAmount']=i.orderAmount
            prolist.append(pro)
        context = {
            'profile': user_profile,
            'orders': prolist,
            'a':a
        }
        if request.method == 'POST' and 'logout' in request.POST:
            logout(request)
            return redirect('login1')
        else:
            return render(request, 'profile.html', context)
    else:
        return redirect('login1')
    
def myorder(request):
    if 'email' in request.session:
        print("aaaaaa")
        a = request.session['email']
        user_orders = Ordermodel.objects.filter(userEmail=a)
        print(user_orders)
        print("aaaaaa")
        prolist=[]
        for i in user_orders:
            pro={}
            print(111111)
            productdata=Product.objects.get(id=i.productid)
            pro['img']=productdata.img
            pro['id']=i.productid
            pro['name']=productdata.name
            pro['orderDate']=i.orderDate
            pro['productqty']=i.productqty
            pro['transactionId']=i.transactionId
            pro['paymentMethod']=i.paymentMethod
            pro['orderAmount']=i.orderAmount
            prolist.append(pro)
            print(prolist)
        return render(request, 'myorder.html', {'a':a, 'prolist':prolist})
        # if user_orders.exists():
        #     context = {
        #         'orders': user_orders,
        #         'a':a
        #     }
        #     return render(request, 'myorder.html', context)
        # else:
        #     return render(request, 'myorder.html', {'message': "No orders placed",'a':a})
    else:
        return redirect('login1')


def changepass(request):
    if 'email' in request.session:
        a=request.session['email']
        user=UserRegister.objects.get(email=a)
        if request.method=="POST":
            old=request.POST['oldpass']
            newpass=request.POST['newpass']
            newpass1=request.POST['newpass1']
            if old==user.password:
                if newpass==newpass1:
                    user.password=newpass
                    user.save()
                    return render(request,'changepass.html',{'message':"New password update",'a':a})
                else:
                    return render(request,'changepass.html',{'message':"New password not match",'a':a})
            else:
                return render(request,'changepass.html',{'message':"Old password not match",'a':a})
            
        return render(request,'changepass.html',{'a':a})
    else:
        return redirect('login1')
    

def contact(request):
    if 'email' in request.session:
        a=request.session['email']
        data=UserRegister.objects.get(email=a)
        if request.method=="POST":
            contact_us=Contactus()
            contact_us.name=request.POST['name']
            contact_us.email=request.POST['email']
            contact_us.phone=request.POST['phone']
            contact_us.message=request.POST['message']
            contact_us.save()
            return render(request,'contactus.html',{'message':"Message Sent Successfully",'a':a})
        return render(request,'contactus.html',{'data':data,'a':a})
    else:
        if request.method=="POST":
            contact_us=Contactus()
            contact_us.name=request.POST['name']
            contact_us.email=request.POST['email']
            contact_us.phone=request.POST['phone']
            contact_us.message=request.POST['message']
            contact_us.save()
            return render(request,'contactus.html',{'message':"Message Sent Successfully"})
        return render(request,'contactus.html')

def feedback(request):
    if 'email' in request.session:
        a=request.session['email']
        data=UserRegister.objects.get(email=a)
        if request.method=="POST":
            fb=Feedback()
            fb.name=request.POST['name']
            fb.email=request.POST['email']
            fb.phone=request.POST['phone']
            fb.feedback=request.POST['feedback']
            fb.save()
            return render(request,'feedback.html',{'message':"Feedback submitted Successfully",'a':a})
        return render(request,'feedback.html',{'data':data,'a':a})
    else:
        if request.method=="POST":
            fb=Feedback()
            fb.name=request.POST['name']
            fb.email=request.POST['email']
            fb.phone=request.POST['phone']
            fb.feedback=request.POST['feedback']
            fb.save()
            return render(request,'feedback.html',{'message':"Feedback submitted Successfully"})
        return render(request,'feedback.html')


import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.contrib import messages
def buynow(request):
    if 'email' in request.session:
        a = UserRegister.objects.get(email=request.session['email'])
        if request.method == "POST":
            product_id = request.POST['id']
            quantity = int(request.POST['quantity'])
            product = Product.objects.get(id=product_id)

            if quantity <= product.quantity:  # Check if requested quantity is available
                request.session['productid'] = product_id
                request.session['quantity'] = quantity
                request.session['userid'] = a.pk
                request.session['username'] = a.name
                request.session['userEmail'] = a.email
                request.session['userContact'] = a.phone
                request.session['address'] = a.address
                request.session['orderAmount'] = product.price * quantity
                request.session['paymentMethod'] = "Razorpay"
                request.session['transactionId'] = ""
                return redirect('razorpayView')
            else:
                messages.error(request, 'Requested quantity exceeds available quantity')
                return redirect(request.META.get('HTTP_REFERER', 'index'))
    else:
        return redirect('login1')


RAZOR_KEY_ID = 'rzp_test_PCLwUnDh0gx1EM'
RAZOR_KEY_SECRET = '5X09bgMznDr8vOIuQ0xCkZ53'
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['orderAmount'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'    
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)

@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            
            amount = int(request.session['orderAmount'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            #Order Save Code
            orderModel = Ordermodel()
            orderModel.productid=request.session['productid']
            orderModel.productqty=request.session['quantity']
            orderModel.userId = request.session['userid']
            orderModel.userName = request.session['username']
            orderModel.userEmail = request.session['userEmail']
            orderModel.userContact = request.session['userContact']
            orderModel.address = request.session['address']
            orderModel.orderAmount = request.session['orderAmount']
            orderModel.paymentMethod = request.session['paymentMethod']
            orderModel.transactionId = payment_id
            productdata=Product.objects.get(id=request.session['productid'])
            productdata.quantity=productdata.quantity-int(request.session['quantity'])
            productdata.save()
            orderModel.save()
            del request.session['productid']
            del request.session['quantity']
            del request.session['userid']
            del request.session['username']
            del request.session['userEmail']
            del request.session['userContact']
            del request.session['address']
            del request.session['orderAmount']
            del request.session['paymentMethod']
            # render success page on successful caputre of payment
            return redirect('orderSuccessView')
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello1")
       # if other than POST request is made.
        return HttpResponseBadRequest()

def successview(request):
    if 'email' in request.session:
        a=request.session['email']
        return render(request,'order_sucess.html',{'a':a})
    else:
        return HttpResponseBadRequest()