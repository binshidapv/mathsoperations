from django import forms
class OperationForm(forms.Form):
    num1=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    num2=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))   #num1,nu2 are take n django as post
    #for styling,widget takes input ,attrs are attributes,class=formcontrol'dicitionary class:value formcontrol
class FactForm(forms.Form):
    num = forms.IntegerField()

#validation
    def clean(self):
        cleaned_data=super().clean()
        print("here in form",cleaned_data)
        n1=cleaned_data.get("num1")
        n2=cleaned_data("num2")
        if n1<0:
            msg="invalid number"
            self.add_error("num1",msg)
        if n2<0:
            msg="invalid number"
            self.add_error("num2",msg)



                          #method overriding,#DJANGO FIELD VALIDATION  DOCUMENTATION


