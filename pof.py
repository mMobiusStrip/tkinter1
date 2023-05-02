import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

def run_selected():
    if cleanup_var.get():
        messagebox.showinfo("Sistem Temizleme", "Sistem temizleme işlemi başlatılıyor...")
        # Sistem temizleme işlemini burada gerçekleştirin
        print("Sistem temizleme işlemi gerçekleştirildi.")

    if disable_firewall_var.get():
        messagebox.showinfo("Güvenlik Duvarı Devre Dışı", "Güvenlik duvarını devre dışı bırakma işlemi başlatılıyor...")
        # Güvenlik duvarını devre dışı bırakma işlemini burada gerçekleştirin
        print("Güvenlik duvarı devre dışı bırakıldı.")
        
    if enable_firewall_var.get():
        messagebox.showinfo("Güvenlik Duvarı Etkin", "Güvenlik duvarını etkinleştirme işlemi başlatılıyor...")
        # Güvenlik duvarını etkinleştirme işlemini burada gerçekleştirin
        print("Güvenlik duvarı etkinleştirildi.")

def main():
    global cleanup_var, disable_firewall_var, enable_firewall_var
    
    root = tk.Tk()
    root.title("Basit WinUtil")

    cleanup_var = tk.BooleanVar()
    disable_firewall_var = tk.BooleanVar()
    enable_firewall_var = tk.BooleanVar()

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Checkbutton(frame, text="Sistem Temizleme", variable=cleanup_var).grid(row=0, column=0, sticky=tk.W)
    tk.Checkbutton(frame, text="Güvenlik Duvarını Devre Dışı Bırak", variable=disable_firewall_var).grid(row=1, column=0, sticky=tk.W)
    tk.Checkbutton(frame, text="Güvenlik Duvarını Etkinleştir", variable=enable_firewall_var).grid(row=2, column=0, sticky=tk.W)

    run_button = tk.Button(frame, text="Run Selected", command=run_selected)
    run_button.grid(row=3, column=0, pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
