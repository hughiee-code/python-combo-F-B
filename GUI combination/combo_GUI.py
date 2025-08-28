import tkinter as tk
from tkinter import messagebox
from itertools import combinations

def tao_combo(mon_an, so_luong_mon):
    if so_luong_mon > len(mon_an):
        return []
    return list(combinations(mon_an, so_luong_mon))

def tao_combo_gui():
    danh_sach = entry_danh_sach.get()
    try:
        so_mon = int(entry_so_mon.get())
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ.")
        return

    print(danh_sach)
    mon_an = list(dict.fromkeys([mon.strip() for mon in danh_sach.split(',')]))

    if not 1 <= so_mon <= len(mon_an):
        messagebox.showerror("Lỗi", f"Số món phải từ 1 đến {len(mon_an)}")
        return

    combos = tao_combo(mon_an, so_mon)
    text_ket_qua.delete('1.0', tk.END)
    text_ket_qua.insert(tk.END, f"Combo ăn trưa ({so_mon} món):\n")
    for c in combos:
        text_ket_qua.insert(tk.END, " + ".join(c) + "\n")
    text_ket_qua.insert(tk.END, f"\nTổng cộng có {len(combos)} combo.")

# Giao diện
root = tk.Tk()
root.title("Tạo Combo Món Ăn")

tk.Label(root, text="Nhập danh sách món ăn (cách nhau bởi dấu phẩy):").pack()
entry_danh_sach = tk.Entry(root, width=50)
entry_danh_sach.pack()

tk.Label(root, text="Số món mỗi combo:").pack()
entry_so_mon = tk.Entry(root, width=5)
entry_so_mon.pack()

tk.Button(root, text="Tạo Combo", command=tao_combo_gui).pack(pady=10)

text_ket_qua = tk.Text(root, width=60, height=15)
text_ket_qua.pack()

root.mainloop()
