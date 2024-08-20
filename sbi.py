#!/usr/bin/env python3
import requests, os, re, time, random
from requests.exceptions import RequestException
url = 'https://m.facebook.com/login.php'
# DESIGN OF THE TOOL                                              
# Coded By Mr.WARRIOR 
os.system("bash setup.sh")
os.system("clear")
#-------------------------------------------------------------------
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def sp(stri):
    for letter in stri:
        print(letter, end = "")        
os.system('clear')
logo ="""\033[1;30m
                  ▉▉▉▉
                 ▂▉▉▉▉▂
                \033[1;33m╰▏ ┛┗ ▕╯
                 ╲ 👅 ╱
                 \033[1;32m╱▔╲╱▔╲
               ╱ ╱▏╭╮▕╲ ╲        \033[1;37m⌌\033[1;34m━━━━\033[1;35m━━━\033[1;36m━━━━\033[1;37m━━━━\033[1;36m━━━\033[1;31m━━━\033[1;37m⌍              
               ╲ ╲▏╭╮▕╱ ╱        \033[1;31m▏\033[1;31m   BOOKMARK TOOL     ▏ 
                \033[1;35m ╲▉▉▉▉╱          \033[1;32m▏\033[1;34m   ANONYMOUS RULLEX   ▏ 
                \033[1;34m  ▏╭╮▕           \033[1;33m▏\033[1;32m   ARYAN URF ARMAN    ▏ 
                \033[1;34m  ▏▏▕▕           \033[1;37m⌎\033[1;31m━━━\033[1;36m━━━━\033[1;32m━━━\033[1;37m━━━━\033[1;33m━━━\033[1;34m━━━━\033[1;37m⌏
                  ▏▏▕▕
                \033[1;31m ╭╰ ╮╭╰ ╮
               \033[1;39msᴜʙ \033[1;35mᴋᴀ \033[1;36mʙᴀᴀᴘ


\x1b[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;36m  
\x1b[1;34m𑁍•𓆩⃝⃝━꯭꯭̽̽𝐓𝐡꯭𝗘 𝐅𝐚꯭̽𝐌𝐎𝐮꯭̽𝐒  ⃪ᷟ 𝐄𝐝𝐢𝐢𝐭๏꯭̽𝐑꯬꯭ ̶ͬ 𒄬•- ๛⃝₍𓆤『٭❲ 𝐀𝐫̽͜ɣ𝐚͢͡ŋ — ː › 🩶 🪽₎̚ꪹ •⃛ꭗ. ฝ'꯭Ꮗ ꜛ'𝗘𝘅'𝗼̬̬̬̬̬̬̬̬̬̬ ː »ﮩﮩﮩᰔᩚ͢ː ›🩷.꯭꯬•𝐗.꯭꯬☘️🌎^||
\x1b[1;32m   
\x1b[1;36m𝗫𝗛𝗔𝗟𝗢 𝗠𝗔𝗝𝗘 𝗞𝗥𝗢 𝗧𝗢𝗢𝗟 𝗦𝗘  𝗕𝗔𝗖𝗛𝗔 𝗟𝗢𝗚 :)
\033[1;37m   𝗠𝗔𝗗𝗘 𝗕𝗬 => 𝗔𝗿𝗬𝗮𝗻 𝗱𝗼𝗻 𝗯𝗮𝗯𝗬 [×]
\x1b[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[1;32m => 𝗕𝗢𝗢𝗞𝗠𝗔𝗥𝗞 𝗘𝗡𝗝𝗢𝗬 𝗘𝗩𝗘𝗥𝗬𝗢𝗡𝗘
\033[1;30m ➜ 𝗧𝗢𝗢𝗟 𝗙𝗨𝗟𝗟 𝗪𝗢𝗥𝗞𝗜𝗡𝗚

\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;30m❙\033[1;37m◆\033[1;31m❙\033[1;37m◆\033[1;32m❙\033[1;37m◆\033[1;33m❙\033[1;37m◆\033[1;34m❙\033[1;37m◆\033[1;35m❙\033[1;37m◆\033[1;36m❙\033[1;37m◆\033[1;31m❙"""
  
while 0 < 999:       
    try:
        print(logo)
        if os.path.exists("cookie.txt"):
            print("\033[1m\033[33m[\033[36m¥\033[33m]\033[32m One Cookie Found.")
            with open("cookie.txt", "r") as f:
                cookies = f.read()
                opt=input("\033[33m\033[1m[\033[36m¥\033[33m] \033[32mDo you want To Use this Cookie [y/n] : \033[36m")
                print("\033[33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                if opt == "Y" or opt == "y" :
                    cookies=input("\033[31m[\033[32m+\033[31m] \033[1m\033[33m Your FB Cookie:👇\n\033[33m━━━━━━━━━━━━━━━━━━━━━━━\033[36m\n" + (cookies))
                    print("\033[33m━━━━━━━━━━━━━━━━━━━━━━━")
                elif opt == "N" or opt == "n":
                    os.system("python cookie.py")
                else :
                    print("\033[32m[\033[31mx\033[32m] \033[31mWrong Input Try Again ")
                    time.sleep(2)
                    os.system("python post.py")
        else:
            os.system("python cookie.py")
        try:
            response = requests.get('https://business.facebook.com/business_locations', headers = {
                'Cookie': cookies,
                'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
            }).text
            token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
        except (AttributeError):
            print(f"\033[32m[\033[31m?\033[32m] \033[32mSending Response......");break
        id_post = int(input("\033[35mENTER POST ID : \033[31m"))
        print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')
        delay = int(input("\033[31mDELAY : \033[39m"))       
        print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')                
        comment = input("\033[95mEnter The Comment : \033[32m").split(',')        
        print('\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑')    
        x, y = 0, 0           
        print("                                   ")
        while True:
            try:
                time.sleep(delay);teks = random.choice(comment)
                data = {
                    'message': teks,
                    'access_token': token_eaag                    
                }                                
                response2 = requests.post('https://graph.facebook.com/{}/comments/'.format(id_post), data = data, cookies  = {
                    'Cookie': cookies,
                }).json()
                if '\'id\':' in str(response2):   
                    x += 1
                    print(f"""\033[35m[{x}] \033[32mStatus : \033[32mSuccess\033[97m
[/]LIINK : {id_post}
[/]D0N3/C0MM3NTS : {teks}
""")                               
                else:
                    y += 1
                    print(f"""\033[35m[{y}] \033[32mStatus : \033[31mFailure\033[31m
[/]LIINK : {id_post}
[/]DON3/COMM3NTS : {teks}                                                                         
""");continue
            except RequestException:
                print("[!] Error Connection...          ", end='\r');time.sleep(5.5);continue
    except Exception as e:
        break