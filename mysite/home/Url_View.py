PAGE = ['index', 'DATA', 'introduction','login','notice','search','upper']



def urls(AA):
    for p in AA:
        print(f"path('{p}/', views.{p}, name='{p}'),")

def views(AA):
    for p in AA:
        print(f"def {p}(request):\n    return render(request, '{p}.html')\n")



def staticcss(asd):
    for x in asd:
        file_path = f"""<link rel="stylesheet" type="text/css" href="{{% static 'css/{x}.css' %}}">"""
        print(file_path)

def viewpaths(asd):
    for x in asd:
        file_path = f"""def {x}(request):
        return render(request, 'pybo/{x}.html'),"""
        print(file_path)

def urlpath(asd):
    for x in asd:
        file_path = f"""path('pybo/{x}/', views.{x}, name='{x}'),  # {x} 페이지"""
        print(file_path)

page=["a01_index","a02_data","a03_notice","a04_CF","a05_intro","a06_law","a07_search","a08_login"]

print(urlpath(page))
# for p in page:
#     # print(f'<img id={p} src="{% static 'images/afg.png' %}" alt={p}>)
#     print(f'<img id="{p}" src="{{% static \'images/{p}.png\' %}}" alt="{p}">\n')

for x in page:
    print(f'pybo/templates/pybo/{x}.html',)

print(staticimage(login_image))

# <img id={p} src="{% static 'images/afg.png' %}" alt={p}>

