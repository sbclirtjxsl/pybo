old_template = '<img id="{name}" src="{{% static \'{name}.png\' %}}" srcset="{name}.png 1x">'
new_template = '<img id="{name}" src="{{% static \'images/{name}.png\' %}}" alt="{name}">'


all=["main","call","head","wfile","bfile","logo","buger","black","mapp","search","law","loginn","bottom","wtext","btext"]


html="""
{% load static %}
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>08 login</title>
	<script id="applicationScript" type="text/javascript" src="08_login.js"></script>
	<link rel="stylesheet" type="text/css" href="{% static 'CSS/a08login.css' %}">
</head>
<body>
	<div id="n_8_login">
	<svg class="apv">
		<rect id="apv" rx="30.5" ry="30.5" x="0" y="0" width="631" height="61">
		</rect>
	</svg>
	<svg class="apw">
		<rect id="apw" rx="30.5" ry="30.5" x="0" y="0" width="631" height="61">
		</rect>
	</svg>
	<div id="apx">
		<span>LOGIN</span>
	</div>
	<div id="apy">
		<span>Forgot Password ? Reset Now</span>
	</div>
	<div id="apz">
		<span>Don't have an account ? Sign up now</span>
	</div>
	<div id="aqa">
		<span>Sign up</span>
	</div>
	<div id="aqb">
		<span>LOGIN</span>
	</div>
	<div id="aqc">
		<span>NAME:</span>
	</div>
	<div id="aqd">
		<span>PASSWORD:</span>
	</div>
	<svg class="aqe">
		<rect id="aqe" rx="30.5" ry="30.5" x="0" y="0" width="631" height="61">
		</rect>
	</svg>
	<svg class="aqf">
		<rect id="aqf" rx="30.5" ry="30.5" x="0" y="0" width="631" height="61">
		</rect>
	</svg>
	<div id="aqg" class="_____">
		<svg class="aqh">
			<rect id="aqh" rx="0" ry="0" x="0" y="0" width="1920" height="197">
			</rect>
		</svg>
		<div id="aqi">
			<span>연구 및 공익사업</span>
		</div>
		<div id="aqj">
			<span>장애물 없는 생활환경 인증</span>
		</div>
		<div id="aqk">
			<span>사람과건축 소개</span>
		</div>
		<div id="aql">
			<img id="buger" src=\"{% static 'buger.png' %}\" srcset=\"buger.png 1x\">
				
			</svg>
		</div>
		<div id="aqn">
			<img id="search" src=\"{% static 'search.png' %}\" srcset=\"search.png 1x\">
				
			</svg>
		</div>
		<div id="aqp">
			<div id="aqq">
				<span>KR</span>
			</div>
			<svg class="aqr" viewBox="0 0 15.873 12.432">
				<path id="aqr" d="M 0 0.00030517578125 L 8.188465118408203 12.43235778808594 L 15.87321853637695 0.00030517578125 L 0 0.00030517578125 Z">
				</path>
			</svg>
		</div>
		<div id="aqs">
			<img id="loginn" src=\"{% static 'loginn.png' %}\" srcset=\"loginn.png 1x\">
				
			</svg>
		</div>
		<div id="aqu">
			<span>자료실</span>
		</div>
		<div id="aqv">
			<span>게시판</span>
		</div>
		<div id="aqw">
			<div id="aqx">
				<img id="logo" src=\"{% static 'logo.png' %}\" srcset=\"logo.png 1x\">
					
				</svg>
			</div>
			<div id="aqz">
				<span>사단법</span><span>인</span>
			</div>
			<div id="ara">
				<img id="btext" src=\"{% static 'btext.png' %}\" srcset=\"btext.png 1x\">
					
				</svg>
			</div>
			<div id="arc">
				<span>과</span>
			</div>
		</div>
	</div>
</div>
</body>
</html>
"""

for name in all:
    old = old_template.format(name=name)
    new = new_template.format(name=name)
    html = html.replace(old, new)
print(html)