from django.http import HttpResponse
from django.shortcuts import redirect

def UnoutheticatedUser(view_func):
    def WrapperFunc(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('employeedashboard')

        else:
            return view_func(request, *args,**kwargs)

        return view_func(request, args,**kwargs)

    return WrapperFunc

def AllowedUsers(allowed_roles=[]):
    def Decorator(view_func):
        def WrapperFunc(request,*args,**kwargs):
            print('working:',allowed_roles)


            return view_func(request, *args, **kwargs)

        return WrapperFunc

    return Decorator
