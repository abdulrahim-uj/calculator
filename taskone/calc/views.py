from django.shortcuts import render


def calcop(request):
    return render(request, "calc/home.html")


def calcresult(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    context = {
        'add': addition,
        'sub': subtraction,
        'mul': multiplication,
        'div': division
    }
    # return render(request, "calc/result.html",
    #               {'add': addition, 'sub': subtraction, 'mul': multiplication,
    #                'div': division})
    return render(request, "calc/result.html", context=context)
