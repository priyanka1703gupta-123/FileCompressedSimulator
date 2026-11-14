
import heapq
import tkinter as tk
from collections import Counter
from tkinter import filedialog

codes, encoded = {}, ""


def build_codes(text):
    
    heap = [[f, i, ch] for i, (ch, f) in enumerate(Counter(text).items())]
    if len(heap) == 1:                      # only one unique character
        return {heap[0][2]: "0"}
    heapq.heapify(heap)
    n = len(heap)
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        heapq.heappush(heap, [a[0] + b[0], n, (a, b)])
        n += 1
    result = {}

    def walk(node, code):
        if isinstance(node[2], tuple):      # internal node
            walk(node[2][0], code + "0")
            walk(node[2][1], code + "1")
        else:                               # leaf
            result[node[2]] = code
    walk(heap[0], "")
    return result


def show(msg):
    out.delete("1.0", "end")
    out.insert("end", msg)


def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if path:
        box.delete("1.0", "end")
        box.insert("end", open(path, encoding="utf-8").read())


def compress():
    global codes, encoded
    text = box.get("1.0", "end-1c")
    if not text:
        return show("Please type text or open a file first.")
    codes = build_codes(text)
    encoded = "".join(codes[c] for c in text)
    before, after = len(text) * 8, len(encoded)
    msg = f"Original size   : {before} bits\n"
    msg += f"Compressed size : {after} bits\n"
    msg += f"Space saved     : {100 * (before - after) / before:.1f} %\n\n"
    msg += "Char   Freq   Code\n" + "-" * 24 + "\n"
    freq = Counter(text)
    for ch, code in sorted(codes.items(), key=lambda x: len(x[1])):
        msg += f"{repr(ch):6} {freq[ch]:<6} {code}\n"
    msg += f"\nEncoded bits:\n{encoded[:200]}{'...' if len(encoded) > 200 else ''}"
    show(msg)


def decompress():
    if not encoded:
        return show("Compress something first.")
    rev, cur, text = {v: k for k, v in codes.items()}, "", ""
    for bit in encoded:
        cur += bit
        if cur in rev:
            text += rev[cur]
            cur = ""
    show("Decompressed text:\n\n" + text)


root = tk.Tk()
root.title("Huffman Coding - File Compression Simulator")
root.geometry("600x560")

tk.Label(root, text="File Compression Simulator",
         font=("Arial", 15, "bold")).pack(pady=8)
tk.Label(root, text="Input text:").pack(anchor="w", padx=10)
box = tk.Text(root, height=8)
box.pack(fill="x", padx=10)

bar = tk.Frame(root)
bar.pack(pady=8)
for label, cmd in [("Open File", open_file), ("Compress", compress),
                   ("Decompress", decompress)]:
    tk.Button(bar, text=label, width=12, command=cmd).pack(side="left", padx=5)

tk.Label(root, text="Output:").pack(anchor="w", padx=10)
out = tk.Text(root, height=18, font=("Courier", 10), bg="#f4f4f4")
out.pack(fill="both", expand=True, padx=10, pady=(0, 10))

root.mainloop()