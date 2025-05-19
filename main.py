from tkinter import *
from tkinter import filedialog, messagebox
import cv2
import base64
import hashlib
from cryptography.fernet import Fernet
from encryption import encrypt, decrypt
from utils import load_image, show_image_on_label, encode_message, decode_message


class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography Tool")
        self.root.geometry("800x600")

        self.image_path = None
        self.image = None

        # Canvas with scrollbars
        self.canvas = Canvas(root, bg="gray")
        self.canvas.pack(fill=BOTH, expand=True, side=TOP)

        self.scroll_y = Scrollbar(root, orient=VERTICAL, command=self.canvas.yview)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.scroll_x = Scrollbar(root, orient=HORIZONTAL, command=self.canvas.xview)
        self.scroll_x.pack(side=BOTTOM, fill=X)

        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.img_label = Label(self.canvas)
        self.canvas.create_window((0, 0), window=self.img_label, anchor="nw")

        # Controls
        self.load_btn = Button(root, text="Load Image", command=self.load_image)
        self.load_btn.pack(pady=5)

        self.message_entry = Text(root, height=5, width=60)
        self.message_entry.pack()
        self.message_entry.insert(END, "Enter secret message here...")

        self.key_entry = Entry(root, width=30)
        self.key_entry.pack()
        self.key_entry.insert(0, "Enter encryption key")

        self.encode_btn = Button(root, text="Encode & Save Image", command=self.encode_and_save)
        self.encode_btn.pack(pady=5)

        self.decode_btn = Button(root, text="Load Image & Decode Message", command=self.decode_message_from_image)
        self.decode_btn.pack()

    def load_image(self):
        try:
            path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.bmp *.jpg *.jpeg")]
            )
            if path:
                self.image_path = path
                self.image = load_image(path)
                show_image_on_label(self.image, self.img_label)

                self.canvas.update_idletasks()
                self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image:\n{e}")

    def encode_and_save(self):
        if self.image is None:
            messagebox.showerror("Error", "Load an image first!")
            return

        secret_msg = self.message_entry.get("1.0", END).strip()
        if not secret_msg:
            messagebox.showerror("Error", "Enter a secret message!")
            return

        key = self.key_entry.get().strip()
        if not key:
            messagebox.showerror("Error", "Enter an encryption key!")
            return

        encrypted_msg = encrypt(secret_msg, key)
        encrypted_msg += "#####"  # Add delimiter

        try:
            encoded_img = encode_message(self.image, encrypted_msg)
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG Images", "*.png")]
            )
            if save_path:
                cv2.imwrite(save_path, encoded_img)
                messagebox.showinfo("Success", "Image saved with hidden message!")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encode and save image:\n{e}")

    def decode_message_from_image(self):
        try:
            path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.bmp *.jpg *.jpeg")]
            )
            if not path:
                return

            img = load_image(path)
            hidden_message = decode_message(img)

            print("Hidden message extracted:", repr(hidden_message))

            if "#####" not in hidden_message:
                messagebox.showerror("Error", "No hidden message found or it's corrupted.")
                return

            hidden_message = hidden_message.split("#####")[0]

            key = self.key_entry.get().strip()
            if not key:
                messagebox.showerror("Error", "Enter encryption key to decrypt message!")
                return

            try:
                decrypted_msg = decrypt(hidden_message, key)
                messagebox.showinfo("Hidden Message", decrypted_msg)
            except Exception:
                messagebox.showerror(
                    "Error",
                    "Failed to decrypt message. Possibly wrong key or corrupted data."
                )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load or decode image:\n{e}")


if __name__ == "__main__":
    root = Tk()
    app = SteganographyApp(root)
    root.mainloop()
