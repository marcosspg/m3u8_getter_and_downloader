import chromedriver_autoinstaller 
chromedriver_autoinstaller.install()
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

removeGUI = """
$('html,body').animate({scrollTop: document.body.scrollHeight},\"fast\");
var elems = document.querySelector(\"#cuerpo > strong > strong\")
document.body.innerHTML = \"\";
document.body.appendChild(elems);
document.querySelector(\"div[align=center]\").parentNode.removeChild(document.querySelector(\"div[align=center]\"));
document.querySelector(\"div[align=center]\").parentNode.removeChild(document.querySelector(\"div[align=center]\"));
document.querySelector("input[name=g-recaptcha-response]").type = "text";
""";


def getEval(url:str):
    if url.__contains__("embed-"):
        url = url.replace("embed-", "").replace(".html", "")
    options = Options();
    #options.add_argument("--headless");
    options.add_argument("start-maximized");
    #options.add_argument("--window-size=1280x720")
    options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36")

    driver = uc.Chrome(options=options)
    driver.get(url);
    try:
        driver.execute_async_script(removeGUI);
    except: None
    input("");


getEval("https://powvideo.net/embed-pt0jzc2lgsnb.html");