import requests

session = requests.Session()

params = {"email": "sessions@wetherbyrunnersac.co.uk", "password": "TheMightyOrange"}
r = requests.get("https://classfit.com/index.php/c/Login", auth=("sessions@wetherbyrunnersac.co.uk", "TheMightyOrange"))
print("Cookie is set to:")
print(r.cookies.get_dict())
print("Going to profile page...")
r = requests.get("https://classfit.com/index.php/c/MBOClasses?v=742", auth=("sessions@wetherbyrunnersac.co.uk", "TheMightyOrange"))
print(r.text)

