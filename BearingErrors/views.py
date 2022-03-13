from django.shortcuts import render

# Create your views here.


def test(request):
    return render(request, 'index.html', {'user': 'Anon'})


def welcome(request):
    return render(request, 'welcome.html')


def bearing_info(request):
    list_form = [{'轴承代号': 'sc23', '轴承名称': '滚动轴承', '查看': 'tree'}]
    return render(request, 'bearing_info.html', {'list_form': list_form})


def show_tree(request):
    return render(request, 'error_tree.html')


def bearing_process(request):
    return render(request, 'bearing_process.html')