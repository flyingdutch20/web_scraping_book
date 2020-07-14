import requests

#s = requests.session()
url = "https://classfit.com/"
login_route = "index.php/c/Login/"
#token = s.get(url).cookies

pwd = input("Enter password: ")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
params = {"Email": "sessions@wetherbyrunnersac.co.uk", "Pass": pwd,
          "Lat": 53.9564126, "Long": -1.4418947, "PlyTkn": ""}
#r = s.post(url + login_route, headers=headers, data=params)
#print("Cookie is set to:")
#print(r.cookies.get_dict())
#print(r.ok)
#print(r.status_code)
#print("Going to profile page...")
#r = requests.get("https://classfit.com/index.php/c/SearchClass", cookies=r.cookies)
#print(r.text)

with requests.Session() as session:
    post = session.post(url + login_route, data=params, headers=headers)
    r = session.get(url + "index.php/c/MBOClasses")
    print(r.text)