from django.shortcuts import render
from django.views.generic import View
from calculator.forms import OperationForm,FactForm
# Create your views here.
class AddView(View):
    def get(self,request):
        form=OperationForm()     #object creation,two text field forms
        context={"form":form}
        return render(request,"add.html",context)
    def post(self,request):
        form=OperationForm(request.POST)  #  parse in toform variable  html                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  n
        if form.is_valid():
            print("in view ",form.cleaned_data)# if form has no errors   automatically many validation check default clean validations
            num1=form.cleaned_data.get("num1") #take value from dictipython manage.py
            # onary using get
            num2=form.cleaned_data.get("num2")


        #submit  button working
        # num1=request.POST.get("num1")
        # num2=request.POST.get("num2")
            res=int(num1)+int(num2)
            context = {"result":res}
            return render(request,"add.html",{"result":res})
        else:
            return render(request,"add.html",{"form":form})


class SubView(View):
    def get(self, request):
        form = OperationForm()

        return render(request, "sub.html",{"form":form})
    def post(self, request):
        form=OperationForm(request.POST)
        if form.is_valid():
            num1 = request.POST.get("num2")
            num2= request.POST.get("num2")
            res = (int(num1)-int(num2))
            return render(request, "sub.html",{"result":res})
        else:
            return render(request, "sub.html", {"form": form})

#also we can import from math module
class FactView(View):
    def get(self, request):
        form = FactForm()  # object creation,two text field forms
        context = {"form": form}
        return render(request, "factorial.html",context)
    def post(self, request):
        num = int(request.POST.get("num"))
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        context={"result":fact}
        return render(request,"factorial.html",context)


 #context always dictionary type context is the third argument client side display
class PrimeView(View):
    def get(self,request):
        form = OperationForm()  # object creation,two text field forms
        context = {"form": form}
        return  render(request,"primenumber.html",context)
    def post(self,request):
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))
        primenumbers=[]
        for i in range(num1,(num2+1)):
            flag=0
            for j in range(2,i):
                if(i%j==0):
                    flag=1
                    break
            if (flag==0):
                primenumbers.append(i)
        context={"result":primenumbers}
        return render(request,"primenumber.html",context)


class IndexView(View):
    def get(self,request):
        return render(request,'home.html')
