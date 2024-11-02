# from django.shortcuts import render

# Create your views here.
"""
## 編寫我們要的內容
from django.http import HttpResponse

def message_view(request):
    return HttpResponse("Hello!!!")


## GET method
def say_hello(request):
    ## 直接指定 name 參數
    # name = "OKOK"

    ## 用HTTP method GET 取得前端browser中用戶輸入的參數, request.GET 回傳dict
    ## 測試用: http://127.0.0.1:8000/say_hello/?name=Jojo
    ## 報錯的: http://127.0.0.1:8000/say_hello/
    # name = request.GET["name"]

    ## 同上的方法, 比較冗長的寫法
    ## 用Http method GET 取得回傳的dict
    get_parms = request.GET
    ## 從GET參數(dict) 中尋找name的值, 找不到就回應unknown, 才不會報錯
    name = get_parms.get("name", "unknown")

    return HttpResponse(f"Hello {name}")
"""

## 編寫我們要的內容
from django.http import HttpResponse

## 匯入 POST method 用的render
from django.shortcuts import render


def message_view(request):
    return HttpResponse("Hello!!!")


## GET method
def say_hello(request):
    ## 直接指定 name 參數
    # name = "OKOK"

    ## 用HTTP method GET 取得前端browser中用戶輸入的參數, request.GET 回傳dict
    ## 測試用: http://127.0.0.1:8000/say_hello/?name=Jojo
    ## 報錯的: http://127.0.0.1:8000/say_hello/
    # name = request.GET["name"]

    ## 同上的方法, 比較冗長的寫法
    ## 用Http method GET 取得回傳的dict
    get_parms = request.GET
    ## 從GET參數(dict) 中尋找name的值, 找不到就回應unknown, 才不會報錯
    name = get_parms.get("name", "unknown")

    return HttpResponse(f"Hello {name}")


##def say_hello_template(request):
##    return render(request, "say_hello_template.html")


## 改寫 template, 由views 傳參數到 say_hello_template.html
## def say_hello_template(request):
##    ## 定義names list
##     names = ["neung", "song", "sam"]
##    ## 用django template 語法印出 list內容, 再用render 印出給browser
##     return render(request, "say_hello_template.html", {"names": names})


## 用POST方式, 要用CSRF
## POST 請求常用在請求、交易、授權等, 因此要等後端處理完回傳，如果user一直按會有重覆問題, 因此browser會設計詢問
## 改寫 template 用表單方式 由views 傳參數到 say_hello.html
def say_hello_template(request):
    # 把names dict 改成由網頁傳遞過來的參數, 沒有收到參數則show "unknown"
    # 用 GET 時, 在payload 可看到用戶端的傳值, 但不會show在畫面
    # name = request.GET.get("name", "unknown")

    # 改用POST方法, 取得用戶傳值
    name = request.POST.get("name", "unknown")
    return render(request, "say_hello.html", {"name": name})
    # return render(request, "say_hello_v2.html", {"name": name})


def say_hello_to(request, name):
    return HttpResponse(f"Hello {name}")
