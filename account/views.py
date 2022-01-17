import re

from datetime import datetime

from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth import login, logout, authenticate

from account.models import User, aws_account


def account(request):
    if request.method == 'GET':
        return render(request, 'account.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password-confirm')
        name = request.POST.get('name')
        major_type = request.POST.get('type')
        phone = request.POST.get('phone')

        message = ""

        if User.objects.filter(email=email):
            message = "이미 사용중인 이메일입니다."
        elif re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password) is None:
            message = "비밀번호는 최소 8자, 최소 하나의 문자 및 하나의 숫자를 사용해야 합니다."
        elif password != password_confirm:
            message = "비밀번호 확인이 일치하지 않습니다."
        elif major_type == '0':
            message = "과를 반드시 선택해야합니다."
        elif re.match('010[0-9]{8}$', phone) is None:
            message = "전화번호 형식이 올바르지 않습니다."
        else:
            pass

        if message != "":
            return HttpResponse("""
                <script>
                    alert('""" + message + """');
                    window.history.back();
                </script>
            """)
        else:
            user = User()
            user.email = email
            user.name = name
            user.major_type = int(major_type)
            user.phone = phone
            user.set_password(password)

            try:
                user.save()

                user = authenticate(email=email, password=password)
                login(request, user)

                return redirect(reverse('mypage'))

            except:
                return HttpResponse("""
                        <script>
                            alert('오류가 발생했습니다. 해당 오류가 지속되면 개발자에게 연락주세요. (ACCOUNT_DB_ERROR)');
                            window.history.back();
                        </script>
                    """)


def mypage(request):
    return render(request, 'mypage.html')


def aws(request):
    if request.method == 'GET':
        aws_acc = aws_account.objects.filter(user=request.user).last()
        email = None
        password = None

        if aws_acc is not None:
            email = aws_acc.email
            password = aws_acc.password

        open_time = datetime.now() - datetime.strptime('2022-02-07 03:00:00', '%Y-%m-%d %H:%M:%S')

        return render(request, 'aws.html',
                      {'open_time': open_time.total_seconds(), 'email': email, 'password': password})

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        aws_acc = aws_account()
        aws_acc.email = email
        aws_acc.password = password
        aws_acc.user = request.user

        try:
            aws_acc.save()

            return redirect(reverse('aws'))

        except:
            return HttpResponse("""
                    <script>
                        alert('오류가 발생했습니다. 해당 오류가 지속되면 개발자에게 연락주세요. (AWS_DB_ERROR)');
                        window.history.back();
                    </script>
                """)


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)

            return redirect(reverse('mypage'))
        else:
            return HttpResponse("""
                    <script>
                        alert('이메일 또는 비밀번호가 잘못되었습니다.');
                        window.history.back();
                    </script>
                """)


def signout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect(reverse('index'))
