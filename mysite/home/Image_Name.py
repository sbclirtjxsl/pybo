import re

page=["01index","02data","03notice","04CF","05intro","06law","07search","08login"]

main = ["aae"]
mapp = ["abh"]
law = ["abs"]
wfile = ["abu"]
head = ["abw"]
call = ["aby"]
logo = ["acl", "adj","afm","agb","aht","aii","ajp","ake","alu","amj","any","aon","apq","aqy","arv"]
wtext = ["aco","ail","age","amm","akh","aoq"]
bottom = ["ain","amo","agg","akj","aos","acq"]
buger = ["acx","afa","ali","ahh","anm","ape","ajd","aqm","arj"]
search = ["acz","afc","alk","ano","ahj","apg","aox","aqo","ajf","arl"]
loginn = ["ade","afh","apl","aho","aqt","arq","ajk","alp","ant"]
btext = ["adm","ahw","ajs","alx","aob","apt","arb","ary","afp"]
bfile = ["aeh","aej","ael","aen","aep","aer","aet"]
bb = ["adp","agh"]
# all = [main, mapp, law, wfile, head, call, logo, wtext, bottom, buger, search, loginn, btext, bfile,bb]

replacements = {
    "main": main,
    "mapp": mapp,
    "law": law,
    "wfile": wfile,
    "head": head,
    "call": call,
    "logo": logo,
    "wtext": wtext,
    "bottom": bottom,
    "buger": buger,
    "search": search,
    "loginn": loginn,
    "btext": btext,
    "bfile":bfile,
    "bb":bb
}

file_path_HTML = [
    '../pybo/templates/pybo/a01index.html',
    '../pybo/templates/pybo/a02data.html',
    '../pybo/templates/pybo/a03notice.html',
    '../pybo/templates/pybo/a04CF.html',
    '../pybo/templates/pybo/a05intro.html',
    '../pybo/templates/pybo/a06law.html',
    '../pybo/templates/pybo/a07search.html',
    '../pybo/templates/pybo/a08login.html'
]
file_path_CSS = [
    '../static/css/a01index.css',
    '../static/css/a02data.css',
    '../static/css/a03notice.css',
    '../static/css/a04CF.css',
    '../static/css/a05intro.css',
    '../static/css/a06law.css',
    '../static/css/a07search.css',
    '../static/css/a08login.css'
]


def html_fixed(ffile_path):
    with open(ffile_path, 'r', encoding='utf-8') as file:
        textt = file.read()

    # 각 그룹에 대해 대체가 일어나면 다음 그룹에서는 이미 대체된 부분을 건드리지 않도록 함
    for name, group in replacements.items():
        for y in group:
            # y가 이미 다른 그룹으로 대체된 경우, 재대체하지 않도록 함
            pattern = r'\b' + re.escape(y) + r'\b'  # 단어 단위로 정확히 일치하는지 확인
            if re.search(pattern, textt):
                print(f"'{y}'를 '{name}'로 대체 중...")
                textt = re.sub(pattern, name, textt)
            else:
                print(f"'{y}'가 {ffile_path}에 없음.")

    with open(ffile_path, 'w', encoding='utf-8') as file:
        file.write(textt)

# def ccss(ffile_path):
#     # try:
#     with open(ffile_path, 'r', encoding='utf-8') as file:
#         textt = file.read()
#     for name, group in replacements.items():
#         for y in group:
#             textt = re.sub(y, name, textt)
#     with open(ffile_path, 'w', encoding='utf-8') as file:
#         file.write(textt)
#     # except Exception as e:
#     #     print(f"{ffile_path}에서 오류 발생: {e}")


for xx in file_path_HTML:
    html_fixed(xx)
    print(xx, 'html 수정')

# for xx in file_path_CSS:
#     ccss(xx)
#     print(xx, 'css 수정')

for xx in file_path_CSS:
    html_fixed(xx)
    print(xx, 'CSS 수정')


print("수정 완료!")

# <a href="{% url 'pybo:login' %}">
#     <img id="logo1" src="{% static 'images/logo1.png' %}" alt="logo1">


# <img id="mapp" src="mapp.png" srcset="mapp.png 1x, mapp@2x.png 2x">

# <img id="mapp" src="{% static 'images/logo1.png' %}" alt="logo1">

# src="
# src="{% static 'image/
# <img id="main" src="main.png" srcset="main.png 1x">
# <img id="main" src="{% static 'images/main.png' %}" alt="main">


old_template = '<img id="{name}" src="{{% static \'{name}.png\' %}}" srcset="{name}.png 1x">'
new_template = '<img id="{name}" src="{{% static \'images/{name}.png\' %}}" alt="{name}">'



# def wkdrhfldzm(all):
#
#     with open(ffile_path, 'r', encoding='utf-8') as file:
#         textt = file.read()
#
#     # 각 그룹에 대해 대체가 일어나면 다음 그룹에서는 이미 대체된 부분을 건드리지 않도록 함
#     for name, group in replacements.items():
#         for x in
#         for y in group:
#             # y가 이미 다른 그룹으로 대체된 경우, 재대체하지 않도록 함
#             pattern = r'\b' + re.escape(y) + r'\b'  # 단어 단위로 정확히 일치하는지 확인
#             if re.search(pattern, textt):
#                 print(f"'{y}'를 '{name}'로 대체 중...")
#                 textt = re.sub(pattern, name, textt)
#             else:
#                 print(f"'{y}'가 {ffile_path}에 없음.")
#
#     with open(ffile_path, 'w', encoding='utf-8') as file:
#         file.write(textt)


    #
    # for name in all:
    #     old = old_template.format(name=name)
    #     new = new_template.format(name=name)
    #     html = html.replace(old, new)
    # print(html)


print("수정 완료!")
