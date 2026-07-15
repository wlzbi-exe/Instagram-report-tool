from cfonts import render
import time
import os
import random
import sys
COLOR_COMBOS = [
    ['green', 'yellow'],
    ['magenta', 'red'],
    ['blue', 'cyan'],
    ['white', 'gray'],
    ['red', 'magenta'],
    ['yellow', 'green']
]
wlzbi_colors, wlzbii_colors, enc_colors, trail_colors = random.sample(COLOR_COMBOS, 4)
WLZBI = render('IG-TOOL', colors=wlzbi_colors, align='center', font='block', background='black')
WLZBII = render('Telegram: @Wlzbi | Join @wlzbii', colors=wlzbii_colors, align='right', font='console', background='black')
print(WLZBI)
print(WLZBII)
version=f"{sys.version_info.major}.{sys.version_info.minor}"
print(f"\033[1;31mbro... your python version giving vintage energy 🥀 {version} \033[0m")
import os 
import sys
import instaloader
import requests 
from rich import print
import datetime
import webbrowser
from typing import Any

class Wlzbi:
  def __init__(self):
    self.g=0
  def exit_csr(self)->any:
    api=requests.get('https://www.instagram.com').cookies.get('csrftoken')
    return api
  def user_for_id(self,user_id :str,)->any:
    B = instaloader.Instaloader()
    username = user_id
    profile = instaloader.Profile.from_username(B.context, username)
    return profile.userid
  def Send_Report(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
        try:
          url = "https://www.instagram.com/api/v1/web/reports/get_frx_prompt/"
          payload = {
    'container_module': "profilePage",
    'entry_point': "1",
    'location': "2",
    'object_id': f"{USER_E!r}",
    'object_type': "5",
    'context': "{\"tags\":[\"ig_report_account\",\"ig_its_inappropriate\",\"violence_hate_or_exploitation\"],\"ixt_context_from_www\":\"QVFZWlRaZldlWnlJVlRtRklPMmRrNEoyd1p5WWVVRG9jblN3Slhra2JXY210QmJP[...]
    'selected_tag_types': "[\"violent_hateful_or_disturbing-credible_threat\"]",
    'frx_prompt_request_type': "2",
    'jazoest': "22668"
  }
          headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36",
    'sec-ch-ua-full-version-list': "\"Chromium\";v=\"140.0.7339.51\", \"Not=A?Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"140.0.7339.51\"",
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua': "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    'sec-ch-ua-model': "\"SM-A217F\"",
    'sec-ch-ua-mobile': "?1",
    'x-ig-app-id': "1217981644879628",
    'x-requested-with': "XMLHttpRequest",
    'x-instagram-ajax': "1026809190",
    'x-csrftoken': crf_tt,
    'x-web-session-id': "mriw1e:1s55q9:caluxw",
    'x-asbd-id': "359341",
    'sec-ch-prefers-color-scheme': "light",
    'x-ig-www-claim': "hmac.AR0Dchf5POXAfONXZuR6v_xVPZEe6hWkp5biFfX9JWzI4lC7",
    'sec-ch-ua-platform-version': "\"12.0.0\"",
    'origin': "https://www.instagram.com",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://www.instagram.com/sherinsbeauty/",
    'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i",
    'Cookie': f"csrftoken={crf_tt}; sessionid={Sessionid}"
  }

          response = requests.post(url, data=payload, headers=headers).text
          if '"status":"ok"' in response:
            self.g+=1
            return f" [{self.g}] Report successfully  "
          else:
            return response
        except Exception as e:
          return e

  def lite_report(self,Sessionid:str,crf_tt:str,USER_E:str,)->any:
          try:
            url = f"https://i.instagram.com/users/{USER_E!r}/flag/"
            headers = {
    "User-Agent": "Mozilla/5.0",
    "Host": "i.instagram.com",
    "cookie": f"sessionid={Sessionid}",
    "X-CSRFToken":crf_tt,
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
            data = f"source_name=&reason_id=5&frx_context="

            r3 = requests.post(url, headers=headers, data=data, allow_redirects=False).text
            return r3		
          except Exception as e:
            return e				

Wlzbii=Wlzbi()
if __name__=='__main__':
        def Start_Wlzbi():
          try:
            print('')
            print('')
            
            Sessionid=input('\033[1;35m[ ✟ ] SESSION ID ☞ :\033[0m')
            if not Sessionid:
              raise Exception ('Session ID missing? 🤡 Even bots don't recognize you now.')
            user_id=input('\033[1;36m[ ⸸ ] ENTER USERNAME TO REPORT ☞ :\033[0m ')
            if not user_id or len(user_id)<=2:
              raise Exception('Nothing entered? Bro trying to impress Python with invisible rizz🥀💔')
            crf_tt=Wlzbii.exit_csr()
            USER_E=Wlzbii.user_for_id(user_id)
            print('''[yellow][bold]
[red][bold][1][red] [bold]instagram report 
[green][bold][2][bold] [green][bold]instagram report [green][[red]Lite[green]] [bold][red][green] [bold]
[blue][bold][3][bold][blue][bold] Contact Wlzbi🥀				
            ''')
            choice=input('''\033[1;36m WHAT DO YOU WANT NIGGER ☞ :   \033[0m ''')
            if choice=='1':
              while True:								
                Wlzbi_Report=Wlzbii.Send_Report(Sessionid,crf_tt,USER_E)
                print(Wlzbi_Report)														
            elif choice=='2':
              while True:
                USER_lite=Wlzbii.lite_report(Sessionid,crf_tt,USER_E)
                print(USER_lite)

            elif choice=='3':
              webbrowser.open('https://t.me/+w6_Kos9AuPo4N2I1')
              exit('Redirected to Wlzbi python ')		
            else:
              Start_Wlzbi()
          except Exception as e:
            print(e)		
Start_Wlzbi()
