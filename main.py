import requests, sys, json, uuid, time, os
from colorama import init, Fore, Back, Style
import datetime 
import hashlib 

os.system('cls' if os.name=='nt' else 'clear')
init(autoreset=True)  
API="https://zefame-free.com/api_free.php?action=config"

# --- COLOR/HASH UTILITIES ---
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
kt_code = "</>" 
TODAY = datetime.date.today()

def hash_key(key_and_date):
    """Generates a secure SHA256 hash of the key and date string."""
    try:
        return hashlib.sha256(key_and_date.encode('utf-8')).hexdigest()
    except Exception:
        return ""
# --- END UTILITIES ---


logo = f"""
# (Logo definition remains the same)
\x1b[38;5;46m                        ¶¶¶¶¶¶
\x1b[38;5;46m                       ¶¶¶¶¶¶¶¶
\x1b[38;5;27m                      ¶¶¶¶¶¶¶¶¶¶
\x1b[38;5;27m                     ¶¶¶¶¶¶¶¶¶¶¶¶
\x1b[38;5;220m                     ¶¶¶¶__¶_¶¶¶¶
\x1b[38;5;220m                     ¶¶¶__¶___¶¶¶
\x1b[38;5;196m                     ¶¶¶___¶¶_¶¶¶
\x1b[38;5;196m                     ¶¶¶¶¶¶¶¶¶¶¶¶
\x1b[38;5;46m                      ¶¶_¶¶¶¶_¶¶
\x1b[38;5;46m                      ¶¶_¶¶¶¶_¶¶
\x1b[38;5;27m                      ¶¶_¶¶¶¶_¶¶
\x1b[38;5;27m                      ¶¶_¶¶¶¶_¶¶
\x1b[38;5;220m                      ¶¶_¶¶¶¶_¶¶
\x1b[38;5;220m                      ¶¶_¶¶¶¶_¶¶
\x1b[38;5;196m                      ¶¶_¶¶¶¶_¶¶
\x1b[38;5;196m_¶¶_¶¶¶¶_¶¶_________________________________¶¶_¶¶¶¶_¶¶
\x1b[38;5;46m_¶¶_¶¶¶¶_¶¶________________________________¶¶¶_¶¶¶¶_¶¶    
\x1b[38;5;46m_¶¶_¶¶¶¶_¶¶________________________________¶¶¶_¶¶¶¶_¶¶
\x1b[38;5;27m_¶¶_¶¶¶¶_¶¶____¶____¶____¶____¶____¶____¶___¶¶¶_¶¶¶¶ ¶
\x1b[38;5;27m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶¶
\x1b[38;5;220m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\x1b[38;5;220m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶¶
\x1b[38;5;196m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\x1b[38;5;196m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶¶
\x1b[38;5;46m_¶¶_¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\x1b[38;5;46m_¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶__¶¶¶¶
\x1b[38;5;27m_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mAuthor  : OptionsPremium01
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mGithub  : CyraxmodDOne
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mService : Paid
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mVersion : 1
\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# --- END: KHUFRA LOGO DEFINITION ---


names = {
    229: "TikTok Views",
    228: "TikTok Followers",
    232: "TikTok Free Likes",
    235: "TikTok Free Shares",
    236: "TikTok Free Favorites"
}

# --- FUNCTION: To display the logo and clear screen ONLY ---
def show_logo_and_clear():
    os.system('cls' if os.name=='nt' else 'clear')
    print(logo)
# --- END FUNCTION ---


# --- START: Run Telegram link ONCE at the top level ---
os.system('xdg-open https://t.me/OptionsPremium01')
# --- END: Run Telegram link ONCE ---


# --- START: PASSWORD CHECK LOGIC ---
FILE_NAME = "approved_keys.txt" 
APPROVED_HASHES = {}

try:
    with open(FILE_NAME, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                APPROVED_HASHES[line] = None
except FileNotFoundError:
    pass # Continue without checking if file is missing

MAX_ATTEMPTS = 3 
ACCESS_GRANTED = False

if APPROVED_HASHES: # Only run check if approved_keys.txt exists and has keys
    for attempt in range(MAX_ATTEMPTS):
        os.system('cls' if os.name=='nt' else 'clear')
        print(logo)
        print(f"{Fore.YELLOW}--- TIKTOK BOT ACCESS CHECK ---{Style.RESET_ALL}")
        print(f'{Fore.RED}[{Fore.WHITE}{kt_code}{Fore.RED}] {Fore.YELLOW}CONNECT TO TELEGRAM TO GET PASSWORD: {Fore.CYAN}OptionsPremium01{Style.RESET_ALL}')
        print(f'{Fore.WHITE}------------------------------------{Style.RESET_ALL}')
        
        password_input = input(f'{Fore.RED}[{Fore.WHITE}{kt_code}{Fore.RED}] {Fore.GREEN}ENTER KEY (e.g., vip_user_1): {Style.RESET_ALL}').strip()
        date_input = input(f'{Fore.RED}[{Fore.WHITE}{kt_code}{Fore.RED}] {Fore.GREEN}ENTER EXPIRY DATE (YYYY-MM-DD): {Style.RESET_ALL}').strip()
        print(f'{Fore.WHITE}------------------------------------{Style.RESET_ALL}')
        
        combined_user_input = f"{password_input}|{date_input}"
        user_hash = hash_key(combined_user_input)
        
        if user_hash in APPROVED_HASHES:
            try:
                expiry_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            except ValueError:
                print(f'{Fore.RED}[{Fore.WHITE}❌{Fore.RED}] Invalid date format! Use YYYY-MM-DD.')
                time.sleep(1)
                continue

            if TODAY <= expiry_date:
                # FIX: Corrected variable name to expiry_date
                print(f'{Fore.GREEN}[{Fore.WHITE}✅{Fore.GREEN}] ACCESS GRANTED. Expires: {expiry_date.strftime("%Y-%m-%d")}.{Style.RESET_ALL}')
                time.sleep(1) 
                ACCESS_GRANTED = True
                break
            else:
                print(f'{Fore.RED}[{Fore.WHITE}❌{Fore.RED}] KEY EXPIRED! This key expired on {expiry_date.strftime("%Y-%m-%d")}.{Style.RESET_ALL}')
                print(f'{Fore.RED}Please contact the administrator for a new key.{Style.RESET_ALL}')
                sys.exit()
                
        elif attempt < MAX_ATTEMPTS - 1:
            print(f'{Fore.RED}[{Fore.WHITE}❌{Fore.RED}] INCORRECT KEY or DATE. TRY AGAIN. ({MAX_ATTEMPTS - 1 - attempt} attempts remaining){Style.RESET_ALL}')
            time.sleep(1)
        else:
            print(f'{Fore.RED}[{Fore.WHITE}❌{Fore.RED}] MAX ATTEMPTS REACHED. EXITING.{Style.RESET_ALL}')
            sys.exit()
            
    if not ACCESS_GRANTED and APPROVED_HASHES:
        sys.exit()
# --- END: PASSWORD CHECK LOGIC ---


# --- Display Final Logo before Menu ---
os.system('cls' if os.name=='nt' else 'clear')
print(logo)


if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        data = json.load(f)
else:
    # Note: If the domain is unreachable, this requests.get will fail and exit the script.
    try:
        data = requests.get("https://zefame-free.com/api_free.php?action=config").json()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}ERROR: Could not fetch config from the server.{Style.RESET_ALL}")
        print(f"{Fore.RED}Please check the domain or your internet connection. ({e}){Style.RESET_ALL}")
        sys.exit()

services = data.get('data', {}).get('tiktok', {}).get('services', [])
for i, service in enumerate(services, 1):
    sid = service.get('id')
    name = names.get(sid, service.get('name', '').strip())
    rate = service.get('description', '').strip()
    if rate:
        # Translate description and replace 'vues' with 'views', etc.
        rate = f"[{rate.replace('vues', 'views').replace('partages', 'shares').replace('favoris', 'favorites')}]"
    
    status = f"{Fore.GREEN}[WORKING]{Style.RESET_ALL}" if service.get('available') else f"{Fore.RED}[DOWN]{Style.RESET_ALL}"
    print(f"{i}. {name} — {status}  {Fore.CYAN}{rate}{Style.RESET_ALL}")
    
# --- The Menu prompt now appears after the Logo and Service List ---
choice = input('Select number (Enter to exit): ').strip()
if not choice:
    sys.exit()

try:
    idx = int(choice)
    if idx < 1 or idx > len(services):
        print('Out of range')
        sys.exit()
except:
    print('Invalid')
    sys.exit()

selected = services[idx-1]
video_link = input('Enter video link: ')

id_check = requests.post("https://zefame-free.com/api_free.php?", data={"action": "checkVideoId", "link": video_link})
video_id = id_check.json().get("data", {}).get("videoId")
print("Parsed Video ID:", video_id)


print()

while True:
    order = requests.post("https://zefame-free.com/api_free.php?action=order", data={"service": selected.get('id'), "link": video_link, "uuid": str(uuid.uuid4()), "videoId": video_id})
    result = order.json()
    print(f"{Fore.GREEN}{json.dumps(result, separators=(',',':'))}{Style.RESET_ALL}")
    wait = result.get("data", {}).get("nextAvailable")
    if wait:
        try:
            wait = float(wait)
            # Only sleep if the next available time is in the future
            if wait > time.time(): 
                print(f"{Fore.YELLOW}Waiting for cooldown period...{Style.RESET_ALL}")
                time.sleep(wait - time.time() + 1)
        except:
            pass
