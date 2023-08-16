import os
import subprocess
import sys
import tkinter as tk


class RobloxAccountGrabberBuilder:
    def __init__(self, root):
        self.icon_label = None
        self.icon_entry = None
        self.disclaimer_label = None
        self.copyright = None
        self.status_label = None
        self.generate_button = None
        self.output_entry = None
        self.output_label = None
        self.root = root
        self.root.title("Roblox Account Grabber EXE Builder")
        self.root.geometry("650x285")
        self.root.resizable(False, False)
        self.root.configure(bg="#2e2e2e")

        self.current_page = None

        self.pages = {
            "home": self.create_home_page,
            "about": self.create_about_page,
            "credit": self.create_credit_page  # Add this line
        }

        self.create_navigation_bar()
        self.change_page("home")

    @staticmethod
    def create_rounded_button(parent, text, bg_color, command=None):
        button = tk.Button(
            parent,
            text=text,
            bg=bg_color,
            command=command,
            font=("Arial", 10),
            borderwidth=0,  # Remove the border
            relief="flat",  # Use flat relief for no border
            highlightthickness=0,  # Remove highlight border
            padx=15,  # Adjust padding as needed
            pady=5,  # Adjust padding as needed
        )
        return button

    def create_navigation_bar(self):
        nav_bar = tk.Frame(self.root, bg="#1e1e1e")
        nav_bar.pack(side="top", fill="x")

        home_button = self.create_rounded_button(nav_bar, "Home", "#641cc9", command=lambda: self.change_page("home"))
        home_button.pack(side="left", padx=1)

        about_button = self.create_rounded_button(nav_bar, "About", "#1cc942",
                                                  command=lambda: self.change_page("about"))
        about_button.pack(side="left", padx=1)

        credit_button = self.create_rounded_button(nav_bar, "Credit", "#1552ad",
                                                   command=lambda: self.change_page("credit"))
        credit_button.pack(side="left", padx=1)


        exit = self.create_rounded_button(nav_bar, "Exit", "#e32d20",
                                                   command=self.exit)
        exit.pack(side="left", padx=1)

    def change_page(self, page_name):
        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = self.pages[page_name]()
        self.current_page.pack()

    @staticmethod
    def exit():
        sys.exit()

    def create_home_page(self):
        home_page = tk.Frame(self.root, bg="#2e2e2e")

        self.disclaimer_label = tk.Label(home_page, text="Don't forget to edit R0blUx-Gr@bber.py and put your discord webhook, and Bot token.", bg="#2e2e2e", fg="red")
        self.disclaimer_label.pack()

        self.icon_label = tk.Label(home_page, text="Icon Path (FULL PATH) (OPTIONAL)", bg="#2e2e2e", font=("Arial", 10))
        self.icon_label.pack()
        self.icon_entry = tk.Entry(home_page)
        self.icon_entry.pack()

        # Label and Entry for Output Directory
        self.output_label = tk.Label(home_page, text="Output Directory:", bg="#2e2e2e", font=("Arial", 10))
        self.output_label.pack()
        self.output_entry = tk.Entry(home_page)
        self.output_entry.pack()

        # Button to generate EXE
        self.generate_button = self.create_rounded_button(home_page, text="Generate EXE", bg_color="#c9621c",
                                                          command=self.generate_exe)
        self.generate_button.pack(pady=10)

        # Label for displaying status
        self.status_label = tk.Label(home_page, text="", fg="green", bg="#2e2e2e", font=("Arial", 10))
        self.status_label.pack()

        self.copyright = tk.Label(home_page, text="@Copyright, Independent-coder.", bg="#2e2e2e", font=("Arial", 12))
        self.copyright.pack()

        return home_page



    def create_about_page(self):
        about_page = tk.Frame(self.root, bg="#2e2e2e")

        about_label_disclaimer = tk.Label(
            about_page,
            text="About the Roblox Account Grabber",
            bg="#2e2e2e",
            font=("Arial", 16, "bold"),
        )
        about_label_disclaimer.pack(pady=(20, 10))

        about_text_disclaimer = (
            "Welcome to the Roblox Account Grabber GUI, an open-source Python application "
            "designed to Build the exe for the program R0blUx-Gr@bber.py"
        )
        about_label_text_disclaimer = tk.Label(
            about_page, text=about_text_disclaimer, bg="#2e2e2e", justify="left", wraplength=350
        )
        about_label_text_disclaimer.pack(padx=20)

        about_label_inspired = tk.Label(
            about_page,
            text="Inspiration and Acknowledgments",
            bg="#2e2e2e",
            font=("Arial", 16, "bold"),
            pady=20,
        )
        about_label_inspired.pack()

        about_text_inspired = (
            "I got a lot of inspiration to this project from various sources in the coding community. "
            "Particularly, I would like to put a credit for TurtlesXD/Byte-Stealer "
            "whose GitHub repository provided valuable insights into Python programming for me to base on."
        )
        about_label_text_inspired = tk.Label(
            about_page, text=about_text_inspired, bg="#2e2e2e", justify="left", wraplength=350
        )
        about_label_text_inspired.pack(padx=20)

        return about_page

    def create_credit_page(self):
        credit_page = tk.Frame(self.root, bg="#2e2e2e")

        credit_label = tk.Label(
            credit_page,
            text="Credits",
            bg="#2e2e2e",
            font=("Arial", 16, "bold"),
            pady=20,
        )
        credit_label.pack()

        credit_text = (
            "Special thanks to TurtlesXD/Byte-Stealer for their GitHub repository. \n"
            "\nRequirement.bat: Independent-coder\n"
            "\nR0blUx-Gr@bber.py: Independent-coder\n"
            "\nBuilder: Independent-coder\n"
            "\nAll right reserved to Independent-coder"
        )
        credit_label_text = tk.Label(
            credit_page, text=credit_text, bg="#2e2e2e", justify="left", wraplength=350
        )
        credit_label_text.pack(padx=20)


        return credit_page

    def generate_exe(self):
        output_dir = self.output_entry.get()
        icon_dir = self.icon_entry.get()

        if output_dir:
            command = ["pyinstaller", "R0blUx-Gr@bber.py", "--onefile", "--noconsole", "--distpath", output_dir]

            if icon_dir:
                command.extend(["--icon", icon_dir])

            subprocess.run(command)

            self.update_status_label("EXE generated successfully.", "green")
        else:
            self.update_status_label("Output Directory.", "red")

    def update_status_label(self, text, color):
        self.status_label.config(text=text, fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = RobloxAccountGrabberBuilder(root)
    root.mainloop()
