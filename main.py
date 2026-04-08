import os
import time
import sys
import shutil
import platform
import signal
import random

# Tool: TEAM-CZUCA-Dashboard-Ultimate (Password Section Fixed)
# Author: LEVIATHAN DRIFT 419
# Version: 11.0 (Login System Patch)
# Repo: https://github.com/Tigermate-u/LEVIATHAN_BANNER.git

# --- CONFIGURATION ---
GITHUB_REPO_URL = "https://github.com/Tigermate-u/LEVIATHAN_BANNER.git"
TOOL_DIR_NAME = "LEVIATHAN_BANNER"

# --- COLORS ---
R = '\033[1;31m'  # Red
G = '\033[1;32m'  # Green
C = '\033[1;36m'  # Cyan
Y = '\033[1;33m'  # Yellow
P = '\033[1;35m'  # Purple
W = '\033[1;37m'  # White
BK = '\033[1;30m'  # Black
RESET = '\033[0m'

system_os = platform.system()

# Check Pyfiglet
try:
    import pyfiglet
except ImportError:
    pyfiglet = None

def get_cols():
    try:
        cols, _ = shutil.get_terminal_size()
    except Exception:
        cols = 80
    return cols

def clear():
    if system_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# --- ⚡ CORE TYPING FUNCTIONS ⚡ ---
def type_print(text, speed=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def type_input(text, speed=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    return input()

# --- 🔧 DEPENDENCY FIXER 🔧 ---
def check_dependencies():
    if not shutil.which("git"):
        print(f"{Y}[!] Git is missing. Installing...{RESET}")
        if system_os != "Windows":
            os.system("pkg install git -y")
        else:
            print(f"{R}[!] Please install Git for Windows manually.{RESET}")

    reqs = ["figlet", "lolcat", "curl"]
    if system_os != "Windows":
        for r in reqs:
            if not shutil.which(r):
                os.system(f"pkg install {r} -y > /dev/null 2>&1")

# --- 🔄 UPDATE SYSTEM FUNCTION 🔄 ---
def update_tool():
    clear()
    print(f"\n{C}╔══════════════════════════════════════════╗")
    print(f"{C}║ {Y}      CHECKING FOR UPDATES...             {C}║")
    print(f"{C}╚══════════════════════════════════════════╝{RESET}\n")
    time.sleep(1)

    if not shutil.which("git"):
        type_print(f"{R}[ERROR] Git not found! Cannot update.{RESET}", 0.02)
        if system_os != "Windows":
            type_print(f"{Y}[*] Installing Git automatically...", 0.02)
            os.system("pkg install git -y")
        else:
            return

    if os.path.exists(".git"):
        type_print(f"{G}[*] Git Repository Found. Pulling changes...", 0.02)
        os.system("git pull")
        type_print(f"\n{G}[✔] UPDATE COMPLETE! RESTARTING...", 0.02)
        time.sleep(2)
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        type_print(f"{Y}[!] Repairing Repository...", 0.02)
        try:
            current_dir = os.getcwd()
            parent_dir = os.path.dirname(current_dir)
            print(f"{BK}Downloading latest version from: {GITHUB_REPO_URL}{RESET}")
            os.chdir(parent_dir)
            if os.path.exists(TOOL_DIR_NAME):
                shutil.rmtree(TOOL_DIR_NAME, ignore_errors=True)
            ret = os.system(f"git clone {GITHUB_REPO_URL}")
            if ret == 0:
                type_print(f"\n{G}[✔] UPDATED SUCCESSFULLY!{RESET}", 0.02)
                cmd_line = f"cd {TOOL_DIR_NAME} && python {sys.argv[0]}"
                print(f"{C}Please type: {W}{cmd_line}{RESET}")
                sys.exit()
            else:
                msg = "[X] Clone failed. Check internet connection."
                type_print(f"{R}{msg}{RESET}", 0.02)
                os.chdir(current_dir)
        except Exception as e:
            print(f"{R}[X] Update Failed: {e}{RESET}")
            input("Press Enter to continue...")

# --- 1. INTRO BOOT ANIMATION ---
def intro_animation():
    clear()
    type_print(f"\n{BK} [INIT] CONNECTION HOBE TEAM CZUCA...{RESET}", 0.04)
    time.sleep(0.3)
    logs =[
        "LOADING_KERNEL_MODULES",
        "VERIFYING_ROOT_ACCESS",
        "CHECKING_GIT_DEPENDENCIES",
        "OPTIMIZING_INTERFACE",
        "ACCESS_GRANTED_CORE_SYSTEM"
    ]
    for log in logs:
        sys.stdout.write(f"\r {C}:: SYSTEM_BOOT >> {log:<30} {Y}[WAIT]")
        time.sleep(0.1)
        sys.stdout.write(f"\r {C}:: SYSTEM_BOOT >> {log:<30} {G}[OK]  \n")
        time.sleep(0.05)
    time.sleep(0.3)
    clear()

# --- 2. SETUP LOADING ANIMATION ---
def install_loaders():
    clear()
    type_print(f"\n{G}[*] INITIALIZING INSTALLATION PROTOCOLS...{RESET}\n", 0.03)
    time.sleep(0.3)
    steps =[
        "CONFIGURING DASHBOARD LAYOUT",
        "DOWNLOADING HIGH-RES ASSETS",
        "INJECTING BASH CONFIGURATION",
        "OPTIMIZING PERFORMANCE",
        "FINALIZING SYSTEM VERIFICATION"
    ]
    for step in steps:
        for i in range(4):
            chars = "/-\\|"
            sys.stdout.write(f"\r {C}[PROCESS] {step}... {Y}{chars[i]} ")
            sys.stdout.flush()
            time.sleep(0.08)
        sys.stdout.write(f"\r {C}[PROCESS] {step:<35} {G}[DONE] \n")
        time.sleep(0.1)
    type_print(f"\n{BK} [LOG] SYSTEM REBOOT REQUIRED...{RESET}", 0.05)
    time.sleep(1)
    clear()

# --- HEADER ART ---
def print_uca_header():
    logo = f"""
{C} ████████╗███████╗ █████╗ ███╗   ███╗      ██████╗███████╗██╗   ██╗ ██████╗ █████╗
{C} ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║     ██╔════╝╚══███╔╝██║   ██║██╔════╝██╔══██╗
{C}    ██║   █████╗  ███████║██╔████╔██║     ██║       ███╔╝ ██║   ██║██║     ███████║
{C}    ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║     ██║      ███╔╝  ██║   ██║██║     ██╔══██║
{C}    ██║   ███████╗██║  ██║██║ ╚═╝ ██║     ╚██████╗███████╗╚██████╔╝╚██████╗██║  ██║
{C}    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝╚══════╝ ╚═════╝ ╚═════╝╚═╝  ╚═╝
"""
    print(logo)
    div_line = f"{BK}=========================================================================={RESET}"
    print(div_line)
    head_txt = f"{Y}[ TEAM CZUCA TERMINAL ]            {R}OWNER: LEVIATHAN DRIFT 419   {G}STATUS: ONLINE{RESET}"
    type_print(head_txt, 0.01)
    print(div_line)

# --- FONTS ---
font_db =[
    ("Standard", "standard"), ("Slant", "slant"), ("Shadow", "shadow"),
    ("Small", "small"), ("Script", "script"), ("Bubble", "bubble"),
    ("Digital", "digital"), ("Block", "block"), ("Lean", "lean"),
    ("Mini", "mini"), ("Banner", "banner"), ("Banner3", "banner3"),
    ("Big", "big"), ("Doom", "doom"), ("Epic", "epic"),
    ("Graffiti", "graffiti"), ("Speed", "speed"), ("Star Wars", "starwars"),
    ("Rectangles", "rectangles"), ("Bloody", "bloody"), ("Cyber Large", "cyberlarge"),
    ("Cyber Medium", "cybermedium"), ("Cyber Small", "cybersmall"), ("Gold", "gold"),
    ("Invita", "invita"), ("Isometric1", "isometric1"), ("Isometric2", "isometric2"),
    ("Isometric3", "isometric3"), ("Isometric4", "isometric4"), ("Italic", "italic"),
    ("Ivory", "ivory"), ("Larry 3D", "larry3d"), ("LCD", "lcd"),
    ("Linux", "linux"), ("Lockergnome", "lockergnome"), ("Madrid", "madrid"),
    ("Marquee", "marquee"), ("Maxfour", "maxfour"), ("Mike", "mike"),
    ("Mirror", "mirror"), ("NancyJ", "nancyj"), ("Nipples", "nipples"),
    ("Ogre", "ogre"), ("Pawp", "pawp"), ("Peaks", "peaks"),
    ("Puffy", "puffy"), ("Pyramid", "pyramid"), ("Relief", "relief"),
    ("Roman", "roman"), ("Rounded", "rounded")
]

# --- PREVIEW FUNCTION (FIXED) ---
def show_preview(name, font_file, font_name):
    clear()
    cols = get_cols()
    print(f"{C}╔{'═'*(cols-2)}╗")
    preview_text = f"{C}║ {P}PREVIEW MODE  {R}●  {W}STYLE: {Y}{font_name.upper()} {C}"
    type_print(preview_text.center(cols+18), 0.005)
    print(f"{C}╠{'═'*(cols-2)}╣")
    print(f"{C}╚{'═'*(cols-2)}╝{RESET}")
    print("")

    if system_os == "Windows":
        if pyfiglet:
            try:
                if font_file not in pyfiglet.FigletFont.getFonts():
                    font_file = "standard"
                art = pyfiglet.figlet_format(name, font=font_file, justify="center", width=cols)
                print(f"{C}{art}{RESET}")
            except Exception:
                print(f"{R}[!] Font error.{RESET}")
    else:
        font_dir = "/data/data/com.termux/files/usr/share/figlet"
        path = f"{font_dir}/{font_file}.flf"
        if not os.path.exists(font_dir):
            try:
                os.makedirs(font_dir, exist_ok=True)
            except Exception:
                pass

        std_fonts =[
            "standard", "slant", "shadow", "small", "script", "bubble",
            "digital", "block", "lean", "mini", "banner", "big"
        ]

        if not os.path.exists(path) and font_file not in std_fonts:
            type_print(f"{BK}Downloading font assets...{RESET}", 0.02)
            base_url = "https://github.com/xero/figlet-fonts/raw/master"
            url = f"{base_url}/{font_file}.flf".replace(" ", "%20")
            os.system(f"curl -f -sL {url} -o \"{path}\"")

            if os.path.exists(path) and os.path.getsize(path) < 50:
                try:
                    os.remove(path)
                except Exception:
                    pass

        # Robust execution with fallback ensuring PREVIEW always shows
        f_cmd = f"figlet -f '{font_file}' -w {cols} -c '{name}' 2>/dev/null"
        f_std = f"figlet -f standard -w {cols} -c '{name}' 2>/dev/null"

        if shutil.which("lolcat"):
            os.system(f"{f_cmd} | lolcat || {f_std} | lolcat")
        else:
            os.system(f"{f_cmd} || {f_std}")

    print("")
    print(f"{C}╔{'═'*(cols-2)}╗")
    print(f"{C}║{f'{Y}>>> Made By LEVIATHAN DRIFT 419 <<<'.center(cols+8)}{C}║")
    print(f"{C}╚{'═'*(cols-2)}╝{RESET}")

# --- MAIN ---
def main():
    check_dependencies()
    intro_animation()
    print_uca_header()
    print(f"\n {C}┌──[ {P}IDENTITY {C}]")

    try:
        msg = f" {C}└─➤ {Y}ENTER NAME (Default: TEAM-CZUCA) :: {W}"
        name = type_input(msg, 0.03).strip()
    except Exception:
        name = "TEAM-CZUCA"

    if not name:
        name = "TEAM-CZUCA"

    while True:
        clear()
        print_uca_header()
        type_print(f"{G} [✔] USER: {W}{name.upper()}{RESET}\n", 0.02)
        rows = (len(font_db) // 3) + 1
        for i in range(rows):
            idx1, idx2, idx3 = i, i + rows, i + (rows * 2)
            s1 = f"{C}[{idx1+1:03}] {W}{font_db[idx1][0]:<14}" if idx1 < len(font_db) else ""
            s2 = f"{C}[{idx2+1:03}] {W}{font_db[idx2][0]:<14}" if idx2 < len(font_db) else ""
            s3 = f"{C}[{idx3+1:03}] {W}{font_db[idx3][0]:<14}" if idx3 < len(font_db) else ""
            if s1 or s2 or s3:
                print(f" {s1} {s2} {s3}")

        print(f"\n {C}┌──[ {P}CONFIG {C}]")
        print(f"{BK} [U] CHECK FOR UPDATES{RESET}")
        try:
            choice_str = type_input(f" {C}└─➤ {Y}SELECT ID/OPTION :: {W}", 0.02).lower()
            if choice_str == 'u':
                update_tool()
                continue
            choice = int(choice_str)
            if 1 <= choice <= len(font_db):
                sel_name, sel_file = font_db[choice-1]
            else:
                sel_name, sel_file = font_db[0]
        except Exception:
            sel_name, sel_file = font_db[0]

        show_preview(name, sel_file, sel_name)
        type_print(f"\n {R}[?] {Y}ACTIVATE DASHBOARD? {R}(y/n)", 0.03)
        confirm = type_input(f" {C}└─➤ {W}", 0.02).strip().lower()

        if confirm == 'y':
            print("")
            type_print(f" {P}[SYSTEM] {Y}DO YOU WANT TO SET A PASSWORD LOCK? (y/n)", 0.03)
            want_pass = type_input(f" {C}└─➤ {W}", 0.02).strip().lower()
            user_pass = ""
            recovery_code = ""

            if want_pass == 'y':
                type_print(f" {P}[SYSTEM] {Y}ENTER YOUR NEW PASSWORD:", 0.03)
                user_pass = type_input(f" {C}└─➤ {W}", 0.02).strip()
                recovery_code = str(random.randint(11111, 99999))
                print(f"\n{R}╔══════════════════════════════════════════╗")
                type_print(f"{R}║ {Y}      IMPORTANT: RECOVERY CODE GENERATED  {R}║", 0.02)
                print(f"{R}╠══════════════════════════════════════════╣")
                type_print(f"{R}║ {W}      CODE: {G}{recovery_code}                   {R}║", 0.05)
                type_print(f"{R}║ {BK} (If you forget password, use this code)  {R}║", 0.02)
                print(f"{R}╚══════════════════════════════════════════╝{RESET}")
                type_input(f"\n{C} Press Enter to continue installation...{RESET}", 0.03)

            install_loaders()
            break

    # --- FIXED PASSWORD LOGIC ---
    pass_script = ""
    if user_pass:
        pass_script = f"""
# Secure Password Logic
TARGET_PASS='{user_pass}'
RECOVERY_KEY='{recovery_code}'

while true; do
    echo -e "\\033[1;33m"
    echo -n "[🔒] ENTER PASSWORD: "
    read -s input_pass
    echo "" # Newline after silent input

    if[ "$input_pass" == "$TARGET_PASS" ]; then
        echo -e "\\033[1;32m [✔] ACCESS GRANTED.\\033[0m"
        sleep 0.5
        break
    elif[ "$input_pass" == "$RECOVERY_KEY" ]; then
        echo -e "\\033[1;35m [!] RECOVERY CODE ACCEPTED.\\033[0m"
        sleep 0.5
        break
    else
        echo -e "\\033[1;31m [X] WRONG PASSWORD! TRY AGAIN.\\033[0m"
        sleep 0.8
        clear
        echo -e "\\033[1;31m TEAM CZUCA SECURITY SYSTEM V2.0 \\033[0m"
    fi
done
"""

    # --- BASHRC GENERATION ---
    bashrc_content = f"""
# --- TEAM CZUCA SYSTEM ---
clear
{pass_script}
clear
printf "\\a"

C="\\033[1;36m"; R="\\033[1;31m"; W="\\033[1;37m"; Y="\\033[1;33m"
G="\\033[1;32m"; P="\\033[1;35m"; BK="\\033[1;30m"; RESET="\\033[0m"
COLS=$(tput cols)

H=$(date +%H)
if [ $H -lt 12 ]; then
    GR="GOOD MORNING"
elif [ $H -lt 18 ]; then
    GR="GOOD AFTERNOON"
else
    GR="GOOD EVENING"
fi

# --- 1. DATA COLLECTION ---
IP_CMD=$(ifconfig 2>/dev/null | grep -Eo 'inet (addr:)?([0-9]*\\.){{3}}[0-9]*')
IP_RAW=$(echo "$IP_CMD" | grep -v '127.0.0.1' | head -n 1 | awk '{{print $2}}')
if [ -z "$IP_RAW" ]; then IP_RAW="OFFLINE"; fi

RAM_VAL=$(free -m | awk 'NR==2{{printf "%.2f%%", $3*100/$2}}')
DISK_VAL=$(df /data | tail -1 | awk '{{print $5}}')
TIME_VAL=$(date +'%I:%M %p')

# --- 2. UI DRAWING ---
# BOX 1: INFO
printf "$C╔"; for ((i=1; i<=COLS-2; i++)); do printf "═"; done; printf "╗\\n"

TXT_L=" $GR, {name.upper()}"
TXT_R="[⚡] RAM: $RAM_VAL  [💾] STG: $DISK_VAL "

LEN_L=${{#TXT_L}}
LEN_R=${{#TXT_R}}
GAP=$((COLS - 2 - LEN_L - LEN_R))
if [ $GAP -lt 0 ]; then GAP=0; fi

printf "$C║"
printf "$Y%s" "$TXT_L"
printf "%*s" "$GAP" ""
printf "$R%s" "$TXT_R"
printf "$C║\\n"

# DIVIDER
printf "$C╠"; for ((i=1; i<=COLS-2; i++)); do printf "═"; done; printf "╣\\n"

TXT_L2=" [🌐] IP: $IP_RAW"
TXT_R2="[🕒] TM : $TIME_VAL "

LEN_L2=${{#TXT_L2}}
LEN_R2=${{#TXT_R2}}
GAP2=$((COLS - 2 - LEN_L2 - LEN_R2))
if[ $GAP2 -lt 0 ]; then GAP2=0; fi

printf "$C║"
printf "$P%s" "$TXT_L2"
printf "%*s" "$GAP2" ""
printf "$P%s" "$TXT_R2"
printf "$C║\\n"

printf "$C╚"; for ((i=1; i<=COLS-2; i++)); do printf "═"; done; printf "╝\\n"
echo ""

# BOX 2: ASCII NAME + FOOTER
printf "$C╔"; for ((i=1; i<=COLS-2; i++)); do printf "═"; done; printf "╗\\n"

# ASCII ART (Error Free Logic)
echo -e "$C"
CMD1="figlet -f '{sel_file}' -w $COLS -c '{name}' 2>/dev/null"
CMD2="figlet -f standard -w $COLS -c '{name}' 2>/dev/null"

if command -v lolcat > /dev/null 2>&1; then
    eval "$CMD1" | lolcat || eval "$CMD2" | lolcat
else
    eval "$CMD1" || eval "$CMD2"
fi
echo -e "$RESET"

printf "$C╠"; for ((i=1; i<=COLS-2; i++)); do printf "═"; done; printf "╣\\n"

MSG=">>> Made By LEVIATHAN DRIFT 419 <<<"
printf "$C║"
printf "%*s" $(( (COLS + ${{#MSG}}) / 2 - 1 )) "$MSG"
printf "\\n"

printf "$C╚"; for ((i=1; i<=COLS-2; i++)); do printf "═"; done; printf "╝\\n"
echo ""

P1='\\[\\033[1;36m\\]┌──(\\[\\033[1;31m\\]TEAM-CZUCA💀Termux\\[\\033[1;36m\\])'
P2='-[\\[\\033[1;37m\\]\\w\\[\\033[1;36m\\]]\\n\\[\\033[1;36m\\]└─\\[\\033[1;33m\\]$\\[\\033[0m\\] '
PS1="${{P1}}${{P2}}"

alias cls='clear'
alias update='pkg update && pkg upgrade'
alias exit='kill -9 $PPID'
"""

    if system_os != "Windows":
        home = os.environ.get('HOME', '/data/data/com.termux/files/home')
        path = os.path.join(home, '.bashrc')
        if os.path.exists(path):
            os.system(f"cp {path} {path}.bak")

        with open(path, 'w') as f:
            f.write(bashrc_content)

        print(f"\n{R}╔══════════════════════════════════════════╗")
        type_print(f"{R}║ {G}   SETUP SUCCESSFUL! RESTARTING TERMUX...  {R}║", 0.02)
        print(f"{R}╚══════════════════════════════════════════╝{RESET}\n")

        for i in range(5, 0, -1):
            sys.stdout.write(f"\r {Y}[!] Auto-Exit in {R}{i} {Y}seconds...{RESET}")
            sys.stdout.flush()
            time.sleep(1)

        try:
            os.kill(os.getppid(), signal.SIGKILL)
        except Exception:
            try:
                os.system(f"kill -9 {os.getppid()}")
            except Exception:
                pass

        print(f"\n\n{R}[!] Auto-Exit Failed! Please restart Termux manually.{RESET}")
        sys.exit()

if __name__ == "__main__":
    main()
