from django.shortcuts import render
import pyautogui


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        from django.contrib import auth
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            from .models import uploads
            d = uploads.objects.all()
            return render(request, 'upload.html', {'d': d})

        else:
            pyautogui.alert("wrong username or password")
            return render(request, 'loginpage.html')

    else:
        return render(request, 'loginpage.html')


def load(request):
    p = request.FILES['image']
    from .models import uploads
    d = uploads(pic=p)
    d.save()
    pyautogui.alert("upload done")
    d = uploads.objects.all()
    return render(request, 'upload.html', {'d': d})
