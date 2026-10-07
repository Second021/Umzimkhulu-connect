import tkinter as tk
from tkinter import messagebox, filedialog
import hashlib
import os
import re
import sqlite3
import shutil
import time
from datetime import datetime
from PIL import Image, ImageTk, ImageDraw


# ============================================================
# UMZIMKHULU CONNECT
# ============================================================

# -------------------- COLORS --------------------

DARK = "#12372A"
GREEN = "#2E7D5B"
DARK_GREEN = "#1B5E45"
MINT = "#DFF5E8"
LIGHT = "#EEF9F2"
WHITE = "#FFFFFF"
BG = "#F5F7F6"
TEXT = "#1F2933"
GREY = "#6B7280"
BORDER = "#DDE5E0"
ORANGE = "#F59E0B"
RED = "#DC4C4C"
BLUE = "#3B82F6"

SURFACE = "#FFFFFF"
SIDEBAR = "#102A22"
SIDEBAR_HOVER = "#1E4B3C"
SOFT_GREEN = "#E8F5EE"
SOFT_BLUE = "#EAF2FF"
SOFT_ORANGE = "#FFF4DE"
SOFT_RED = "#FDECEC"


# -------------------- ADMIN LOGIN --------------------

ADMIN_EMAIL = "Admin02@gmail.com"
ADMIN_PASSWORD = "Admin123"


# -------------------- DATABASE --------------------

PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "umzimkhulu_connect.db"
)

UPLOADS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "uploads"
)
os.makedirs(UPLOADS_DIR, exist_ok=True)


# ============================================================
# DEFAULT SETTINGS
# ============================================================

DEFAULT_SETTINGS = {
    "dark_mode": "0",
    "text_size": "Medium",
    "notify_reports": "1",
    "notify_jobs": "1",
    "notify_events": "1",
    "notify_news": "0"
}


# ============================================================
# JOB REQUIREMENTS
# ============================================================

JOB_REQUIREMENTS = {

    "IT Support Assistant": [
        "IT, Computer Science or related qualification/studies.",
        "Basic computer and troubleshooting skills.",
        "Basic knowledge of Windows and networking.",
        "Good communication and teamwork skills.",
        "Willingness to learn and assist community users."
    ],

    "Administrative Assistant": [
        "Grade 12.",
        "Computer literacy.",
        "Basic MS Word and Excel skills.",
        "Good organisation skills.",
        "Good communication skills."
    ],

    "Retail Sales Assistant": [
        "Grade 12.",
        "Customer service skills.",
        "Basic numeracy skills.",
        "Good communication.",
        "Ability to work in a team."
    ],

    "Data Capturer": [
        "Grade 12.",
        "Good typing skills.",
        "Basic Excel knowledge.",
        "Accuracy and attention to detail.",
        "Ability to handle information confidentially."
    ],

    "Community Outreach Assistant": [
        "Grade 12.",
        "Good communication skills.",
        "Community engagement skills.",
        "Ability to work in a team.",
        "Willingness to travel locally."
    ],

    "Junior Web Developer": [
        "IT or Web Development studies.",
        "Basic HTML, CSS and JavaScript.",
        "Basic Git knowledge.",
        "Problem-solving skills.",
        "Willingness to learn."
    ],

    "Bookkeeping Assistant": [
        "Grade 12.",
        "Basic accounting knowledge.",
        "Basic Excel knowledge.",
        "Good numeracy skills.",
        "Attention to detail."
    ],

    "Customer Service Representative": [
        "Grade 12.",
        "Computer literacy.",
        "Good communication skills.",
        "Customer service skills.",
        "Problem-solving ability."
    ],

    "General Worker": [
        "Grade 10 or Grade 12.",
        "Ability to follow instructions.",
        "Safety awareness.",
        "Ability to work in a team.",
        "Physical work readiness."
    ],

    "Social Media Assistant": [
        "Basic social media skills.",
        "Good writing skills.",
        "Smartphone and computer skills.",
        "Basic Canva or design skills.",
        "Creativity."
    ]
}


# ============================================================
# DEFAULT JOBS
# ============================================================

DEFAULT_JOBS = [
    ("IT Support Assistant", "Umzimkhulu Community Services", "Umzimkhulu", "Internship"),
    ("Administrative Assistant", "Umzimkhulu Community Office", "Umzimkhulu", "Full Time"),
    ("Retail Sales Assistant", "Local Retail Store", "Umzimkhulu", "Full Time"),
    ("Data Capturer", "Community Development Organisation", "Umzimkhulu", "Contract"),
    ("Community Outreach Assistant", "Local NGO", "Umzimkhulu", "Contract"),
    ("Junior Web Developer", "Local Digital Agency", "Umzimkhulu / Remote", "Internship"),
    ("Bookkeeping Assistant", "Small Business Services", "Umzimkhulu", "Full Time"),
    ("Customer Service Representative", "Community Service Centre", "Umzimkhulu", "Full Time"),
    ("General Worker", "Local Manufacturing Company", "Umzimkhulu", "Full Time"),
    ("Social Media Assistant", "Local Business Network", "Umzimkhulu", "Part Time")
]


# ============================================================
# DEFAULT BUSINESSES
# ============================================================

DEFAULT_BUSINESSES = [
    ("Bradlows Umzimkhulu", "Furniture", "Shop No 27, Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 39 259 0584", "Furniture and household products."),
    ("Russells Umzimkhulu", "Furniture", "Shop 45, Umzimkhulu Mall, R58, Umzimkulu, 3297", "+27 39 259 0541", "Furniture, appliances and household products."),
    ("OK Furniture", "Furniture", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Furniture and household products."),
    ("Shell Umzimkulu", "Petrol Station", "233 R56 Main Street, Umzimkulu, 3297", "+27 39 259 0477", "Fuel station and vehicle-related services."),
    ("Brandz Umzimkhulu", "Clothing", "Shop No 41, Umzimkhulu Mall, Umzimkulu, 3297", "+27 39 259 0017", "Clothing and fashion retail store."),
    ("Mr Price Umzimkhulu Mall", "Clothing", "Shop 4, Umzimkhulu Mall, R56, Umzimkulu, 3297", "+27 80 021 2535", "Clothing and fashion retail."),
    ("Markham - Umzimkhulu Mall", "Men's Clothing", "Shop 37, Umzimkhulu Mall, Bird Street, Umzimkulu, 3297", "+27 39 259 5100", "Men's clothing and fashion."),
    ("Ackermans", "Clothing", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Clothing and fashion retail."),
    ("Jet", "Clothing", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Clothing and general retail."),
    ("Edgars Active", "Clothing", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Sportswear and clothing."),
    ("Rage", "Footwear", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 39 259 0008", "Footwear and fashion."),
    ("Footgear Umzimkulu Mall", "Footwear", "Shop 47A, Umzimkhulu Mall, Main Street, Umzimkulu, 3297", "+27 87 159 9827", "Footwear store offering shoes and related products."),
    ("Sheet Street", "Homeware", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Homeware and household products."),
    ("Shoprite", "Supermarket", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Supermarket and grocery retailer."),
    ("Shoprite Liquor Shop", "Retail", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Retail store located at Umzimkhulu Mall."),
    ("Umzimkhulu Mall Superstores", "Supermarket", "114 Bird Street, Umzimkulu, 3297", "", "Supermarket and general retail."),
    ("PEP Stores", "Retail", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Affordable clothing and general merchandise."),
    ("Hungry Lion", "Fast Food", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Fast-food restaurant."),
    ("Debonairs Pizza", "Restaurant", "Shop 18A, Umzimkhulu Mall, Umzimkulu, 3297", "039 259 0022", "Pizza and takeaway restaurant."),
    ("KFC Umzimkhulu", "Fast Food", "New Shopping Centre, Shop 13, Umzimkulu, 3297", "+27 39 259 0115", "Fast-food restaurant."),
    ("Nando's Umzimkhulu", "Restaurant", "729 Main Street, Umzimkulu, 3297", "039 108 0001", "Restaurant and takeaway food."),
    ("Steers", "Fast Food", "Total Umzimkulu, Umzimkulu, 3297", "039 259 0000", "Fast-food restaurant."),
    ("Standard Bank Umzimkhulu", "Bank", "Umzimkhulu Mall, Umzimkulu, 3297", "+27 86 012 3000", "Banking and financial services."),
    ("African Bank", "Bank", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 39 259 0612", "Banking and financial services."),
    ("FNB Umzimkhulu Mall", "Bank", "Umzimkhulu Mall, Main Street, Umzimkulu, 3297", "+27 87 345 6080", "Banking and financial services."),
    ("Nedbank", "Bank", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Banking and financial services."),
    ("Capitec", "Bank", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Banking and financial services."),
    ("Absa Bank ATM", "ATM", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "0860 008 600", "ATM and banking services."),
    ("Atlas Finance", "Financial Services", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 87 702 1305", "Financial services."),
    ("Sanlam Development", "Financial Services", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 39 259 7500", "Financial services."),
    ("ABC Financial Services", "Financial Services", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 73 261 6797", "Financial services."),
    ("SM Consulting", "Accounting Services", "23 Riverbend Street, Umzimkulu, 3297", "+27 39 259 0111", "Accounting, bookkeeping and tax practitioner services."),
    ("Autozone Umzimkhulu", "Automotive", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 39 259 0138", "Automotive parts and vehicle products."),
    ("Build it Umzimkulu", "Hardware", "R53, Umzimkulu, 3297", "+27 39 259 0490", "Building materials and hardware."),
    ("Cashbuild Umzimkulu", "Hardware", "729 Bird Street, Umzimkulu, 3297", "+27 39 259 0789", "Building materials and hardware."),
    ("HOME BUILD HARDWARE", "Hardware", "Mzimkhulu Mlonyana Street, Umzimkulu, 3297", "+27 84 850 1746", "Hardware and building materials."),
    ("Bhejani Hardware & Furniture", "Hardware & Furniture", "46 Main Street, Umzimkulu, 3297", "+27 39 259 0970", "Building materials, hardware and furniture."),
    ("City Hardware", "Hardware", "Main Street, Umzimkulu, 3297", "", "Hardware and building materials."),
    ("Smart Shop Aluminium & Wood Umzimkhulu", "Aluminium & Wood Services", "Erf 729, Shop No 3, Cashbuild Center, Umzimkulu, 3297", "+27 63 376 0399", "Aluminium and wood products and services."),
    ("Timber Tech Converters", "Manufacturing", "Umzimkulu, 3297", "+27 79 012 0845", "Manufacturing business."),
    ("Mahlubi Transport and Plant Hire", "Transport & Construction", "Highlands Location, Umzimkulu, 3297", "+27 87 997 1027", "Transport, plant hire and construction services."),
    ("umkhala [pty] ltd", "Digital Printing", "Erf 1330, Newcity, Umzimkulu, 3297", "+27 60 364 4885", "Digital printing services."),
    ("Umzimkhulu Rapid Incubator", "Business Support", "113 Mankofu Road, Umzimkulu, 3297", "+27 39 940 4228", "Business administration and support services."),
    ("Umzimkulu Development Services", "Community Development", "235 Main Road, Umzimkulu, 3297", "+27 39 259 0659", "Community and development support services."),
    ("Umzimkulu Municipality", "Government", "169 Main Road, Umzimkulu, 3297", "+27 39 259 5000", "Local government and municipal services."),
    ("Department of Home Affairs - Umzimkulu Service Point", "Government", "Umzimkulu, 3297", "+27 71 619 2905", "Government identity and civic services."),
    ("Umzimkhulu Traffic Department", "Government", "Umzimkulu, 3297", "+27 39 259 5085", "Traffic and motor vehicle services."),
    ("Umzimkhulu Tourist Office", "Tourism", "Umzimkulu, 3297", "", "Tourism information and visitor assistance."),
    ("Umzimkhulu Hospital", "Healthcare", "Umzimkulu, 3297", "+27 39 259 0310", "Hospital and healthcare services."),
    ("Umzimkhulu Mall", "Shopping Centre", "114 Bird Street, Umzimkulu, 3297", "+27 39 259 0024", "Shopping centre with retail, banking, food, health and government services."),
    ("TotalEnergies Umzimkulu", "Petrol Station", "Main Street, Umzimkulu, 3297", "", "Fuel station and vehicle services."),
    ("Classic Hair Studio 1", "Beauty & Hair", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 78 030 7337", "Hair and beauty services."),
    ("Clicks", "Health & Beauty", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 39 259 4130", "Health, beauty and pharmacy-related retail."),
    ("Cosmetic Connection", "Beauty", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 73 209 9341", "Cosmetics and beauty products."),
    ("City Cell and Sound", "Cellphone & Electronics", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 78 684 3677", "Cellphones, accessories and electronics."),
    ("Cell 24", "Cellphone Services", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 84 211 2880", "Cellphone products and accessories."),
    ("MTN", "Telecommunications", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "Mobile network and telecommunications services."),
    ("Ideals", "Retail", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "", "General retail store."),
    ("Saliou Fashion", "Clothing", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 71 819 7057", "Fashion and clothing."),
    ("Royal Tombstones", "Memorial Services", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 79 446 7307", "Tombstone and memorial services."),
    ("Big Jo's", "Retail", "Umzimkhulu Mall, 114 Bird Street, Umzimkulu, 3297", "+27 73 484 8739", "Local retail business.")
]


# ============================================================
# DATABASE FUNCTIONS
# ============================================================

def connection():
    return sqlite3.connect(PATH)


def init():

    conn = connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS businesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            location TEXT NOT NULL,
            phone TEXT,
            information TEXT,
            created TEXT
        )
    """)

    cur.execute("PRAGMA table_info(businesses)")
    business_columns = [row[1] for row in cur.fetchall()]
    if "information" not in business_columns:
        cur.execute("ALTER TABLE businesses ADD COLUMN information TEXT")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            type TEXT,
            created TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT,
            location TEXT NOT NULL,
            created TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            created TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            location TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            reporter TEXT,
            document_path TEXT,
            created TEXT
        )
    """)

    cur.execute("PRAGMA table_info(reports)")
    report_columns = [row[1] for row in cur.fetchall()]
    if "document_path" not in report_columns:
        cur.execute("ALTER TABLE reports ADD COLUMN document_path TEXT")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT,
            created TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    for key, value in DEFAULT_SETTINGS.items():
        cur.execute("SELECT 1 FROM settings WHERE key=?", (key,))
        if not cur.fetchone():
            cur.execute(
                "INSERT INTO settings (key, value) VALUES (?, ?)",
                (key, value)
            )

    conn.commit()
    conn.close()


def q(sql, params=()):
    conn = connection()
    cur = conn.cursor()
    cur.execute(sql, params)
    result = cur.fetchall()
    conn.close()
    return result


def insert(table, data):
    conn = connection()
    cur = conn.cursor()
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["?"] * len(data))
    values = list(data.values())
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    cur.execute(sql, values)
    conn.commit()
    conn.close()


def delete(table, record_id):
    conn = connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table} WHERE id=?", (record_id,))
    conn.commit()
    conn.close()


def update(table, record_id, data):
    conn = connection()
    cur = conn.cursor()
    set_clause = ", ".join([f"{key}=?" for key in data.keys()])
    values = list(data.values()) + [record_id]
    sql = f"UPDATE {table} SET {set_clause} WHERE id=?"
    cur.execute(sql, values)
    conn.commit()
    conn.close()


def update_report_status(record_id, status):
    conn = connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE reports SET status=? WHERE id=?",
        (status, record_id)
    )
    conn.commit()
    conn.close()


# -------------------- SETTINGS HELPERS --------------------

def get_setting(key, default=None):
    result = q("SELECT value FROM settings WHERE key=?", (key,))
    if result:
        return result[0][0]
    return default if default is not None else DEFAULT_SETTINGS.get(key)


def set_setting(key, value):
    conn = connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO settings (key, value) VALUES (?, ?)
        ON CONFLICT(key) DO UPDATE SET value=excluded.value
        """,
        (key, str(value))
    )
    conn.commit()
    conn.close()


# ============================================================
# PASSWORD FUNCTIONS
# ============================================================

def hash_password(password):
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, 100000
    )
    return salt.hex() + ":" + key.hex()


def check_password(password, stored):
    try:
        salt_hex, key_hex = stored.split(":")
        salt = bytes.fromhex(salt_hex)
        new_key = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), salt, 100000
        )
        return new_key.hex() == key_hex
    except Exception:
        return False


# ============================================================
# SEED JOBS
# ============================================================

def seed_jobs():
    for (title, company, location, job_type) in DEFAULT_JOBS:
        exists = q(
            "SELECT 1 FROM jobs WHERE title=? AND company=?",
            (title, company)
        )
        if not exists:
            insert("jobs", {
                "title": title,
                "company": company,
                "location": location,
                "type": job_type,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            })


# ============================================================
# SEED BUSINESSES
# ============================================================

def seed_businesses():
    for (name, category, location, phone, information) in DEFAULT_BUSINESSES:
        exists = q("SELECT 1 FROM businesses WHERE name=?", (name,))
        if not exists:
            insert("businesses", {
                "name": name,
                "category": category,
                "location": location,
                "phone": phone,
                "information": information,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            })


# ============================================================
# SCROLL FRAME
# ============================================================

class ScrollFrame(tk.Frame):

    def __init__(self, parent, **kwargs):
        background = kwargs.pop("bg", BG)
        super().__init__(parent, bg=background, **kwargs)

        self.canvas = tk.Canvas(self, bg=background, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )
        self.body = tk.Frame(self.canvas, bg=background)

        self.body.bind(
            "<Configure>",
            lambda event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.window = self.canvas.create_window(
            (0, 0), window=self.body, anchor="nw"
        )

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind("<Configure>", self.resize_body)
        self.canvas.bind("<Enter>", self.enable_mouse_scroll)
        self.canvas.bind("<Leave>", self.disable_mouse_scroll)

    def resize_body(self, event):
        self.canvas.itemconfig(self.window, width=event.width)

    def enable_mouse_scroll(self, event=None):
        self.canvas.bind_all("<MouseWheel>", self.mouse_scroll)

    def disable_mouse_scroll(self, event=None):
        self.canvas.unbind_all("<MouseWheel>")

    def mouse_scroll(self, event):
        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)), "units"
        )


# ============================================================
# MAIN APPLICATION
# ============================================================

class App:

    def __init__(self, root):

        self.root = root
        self.root.title("Umzimkhulu Connect")
        self.root.geometry("1200x750")
        self.root.minsize(950, 650)
        self.root.configure(bg=BG)

        self.current_user = None
        self.current_role = None

        self.dark_mode = (get_setting("dark_mode") == "1")
        self.active_page = "DASHBOARD"
        self.menu_buttons = {}

        self.uploaded_doc_path = None

        init()
        seed_jobs()
        seed_businesses()

        self.load_welcome_logo()
        self.show_welcome()

    def load_welcome_logo(self):
        self.welcome_logo_photo = None
        logo_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "umzimkhulu_logo.png"
        )
        if os.path.exists(logo_path):
            try:
                img = Image.open(logo_path)
                img = img.resize((580, 480), Image.Resampling.LANCZOS)
                self.welcome_logo_photo = ImageTk.PhotoImage(img)
            except Exception:
                self.welcome_logo_photo = None


    # ========================================================
    # HELPER FUNCTIONS
    # ========================================================

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self._refresh_theme_after_build()

    def title_label(self, parent, text, size=24, color=TEXT):
        return tk.Label(
            parent, text=text, bg=parent.cget("bg"), fg=color,
            font=("Segoe UI", size, "bold")
        )

    def make_button(self, parent, text, command, color=GREEN, width=20):
        return tk.Button(
            parent, text=text, command=command,
            bg=color, fg=WHITE,
            activebackground=DARK_GREEN, activeforeground=WHITE,
            relief="flat", bd=0, cursor="hand2",
            font=("Segoe UI", 9, "bold"),
            width=width, pady=9
        )


    # ========================================================
    # LOGIN BACKGROUND HELPERS
    # ========================================================

    def _make_login_background(self, parent, width=1200, height=750):
        """Create a login background with the coat of arms plus a soft
        dark-green overlay so the white login card stands out.

        Returns the PhotoImage so we can keep a reference on self.
        Returns None if login_background.png is missing.
        """
        bg_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "login_background.png"
        )

        if not os.path.exists(bg_path):
            return None

        try:
            base = Image.open(bg_path).convert("RGB")
            base = base.resize((width, height), Image.Resampling.LANCZOS)

            # Create a dark-green translucent overlay
            overlay = Image.new("RGBA", (width, height), (18, 55, 42, 150))

            # Composite overlay on top of the background
            composed = Image.alpha_composite(
                base.convert("RGBA"),
                overlay
            ).convert("RGB")

            photo = ImageTk.PhotoImage(composed)

            label = tk.Label(parent, image=photo, bd=0)
            label.place(x=0, y=0, relwidth=1, relheight=1)
            label.lower()

            return photo
        except Exception:
            return None


    # ========================================================
    # THEME
    # ========================================================

    def apply_theme(self, widget=None):
        if widget is None:
            widget = self.root

        if self.dark_mode:
            bg_map = {
                WHITE: "#1E293B",
                BG: "#0F172A",
                LIGHT: "#16261D",
                MINT: "#18392A",
                DARK: "#0B1F18",
                DARK_GREEN: "#164E3B",
                BORDER: "#334155"
            }
            fg_map = {
                TEXT: "#F1F5F9",
                DARK: "#A7F3D0",
                GREY: "#94A3B8",
                WHITE: "#FFFFFF",
                DARK_GREEN: "#86EFAC"
            }
            active_map = {
                DARK_GREEN: "#236B50",
                GREEN: "#236B50",
                BLUE: "#2563EB",
                RED: "#B91C1C",
                ORANGE: "#D97706"
            }
        else:
            bg_map = {
                "#1E293B": WHITE,
                "#0F172A": BG,
                "#16261D": LIGHT,
                "#18392A": MINT,
                "#0B1F18": DARK,
                "#164E3B": DARK_GREEN,
                "#334155": BORDER
            }
            fg_map = {
                "#F1F5F9": TEXT,
                "#A7F3D0": DARK,
                "#94A3B8": GREY,
                "#86EFAC": DARK_GREEN,
                "#FFFFFF": WHITE
            }
            active_map = {
                "#236B50": DARK_GREEN,
                "#2563EB": BLUE,
                "#B91C1C": RED,
                "#D97706": ORANGE
            }

        try:
            widget_class = widget.winfo_class()

            if widget_class in ("Frame", "LabelFrame", "Canvas"):
                current_bg = widget.cget("bg")
                if current_bg in bg_map:
                    widget.configure(bg=bg_map[current_bg])

            elif widget_class == "Label":
                current_bg = widget.cget("bg")
                current_fg = widget.cget("fg")
                if current_bg in bg_map:
                    widget.configure(bg=bg_map[current_bg])
                if current_fg in fg_map:
                    widget.configure(fg=fg_map[current_fg])

            elif widget_class == "Button":
                current_bg = widget.cget("bg")
                current_fg = widget.cget("fg")
                current_active = widget.cget("activebackground")
                current_active_fg = widget.cget("activeforeground")
                if current_bg in bg_map:
                    widget.configure(bg=bg_map[current_bg])
                if current_bg in (GREEN, BLUE, RED, ORANGE, DARK, DARK_GREEN):
                    widget.configure(bg=current_bg)
                if current_fg in fg_map:
                    widget.configure(fg=fg_map[current_fg])
                if current_active in active_map:
                    widget.configure(activebackground=active_map[current_active])
                if current_active_fg in fg_map:
                    widget.configure(activeforeground=fg_map[current_active_fg])

            elif widget_class in ("Entry", "Spinbox"):
                current_bg = widget.cget("bg")
                current_fg = widget.cget("fg")
                if current_bg in bg_map:
                    widget.configure(
                        bg=bg_map[current_bg],
                        insertbackground=fg_map.get(current_fg, "#FFFFFF")
                    )
                if current_fg in fg_map:
                    widget.configure(fg=fg_map[current_fg])

            elif widget_class in ("Listbox", "Text"):
                current_bg = widget.cget("bg")
                current_fg = widget.cget("fg")
                if current_bg in bg_map:
                    widget.configure(bg=bg_map[current_bg])
                if current_fg in fg_map:
                    widget.configure(fg=fg_map[current_fg])

            elif widget_class == "Scrollbar":
                current_bg = widget.cget("bg")
                if current_bg in bg_map:
                    widget.configure(bg=bg_map[current_bg])

        except (tk.TclError, AttributeError):
            pass

        for child in widget.winfo_children():
            self.apply_theme(child)

    def set_theme(self, dark):
        self.dark_mode = dark
        set_setting("dark_mode", "1" if dark else "0")
        self.apply_theme()


    # ========================================================
    # SETTINGS WINDOW
    # ========================================================

    def show_settings(self):
        settings = tk.Toplevel(self.root)
        settings.title("Settings")
        settings.geometry("620x640")
        settings.resizable(False, False)
        settings.transient(self.root)
        settings.configure(bg=BG)

        header = tk.Frame(settings, bg=DARK, height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="SETTINGS", bg=DARK, fg=WHITE,
            font=("Segoe UI", 20, "bold")
        ).pack(anchor="w", padx=25, pady=(15, 0))
        tk.Label(
            header, text="Manage your Umzimkhulu Connect experience",
            bg=DARK, fg="#B8CEC6", font=("Segoe UI", 9)
        ).pack(anchor="w", padx=25)

        scroll = ScrollFrame(settings, bg=BG)
        scroll.pack(fill="both", expand=True)
        body = scroll.body

        def section(title, subtitle=""):
            block = tk.Frame(body, bg=WHITE, highlightbackground=BORDER,
                             highlightthickness=1)
            block.pack(fill="x", padx=20, pady=(14, 0))
            tk.Label(block, text=title, bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 11, "bold")).pack(
                anchor="w", padx=18, pady=(14, 0))
            if subtitle:
                tk.Label(block, text=subtitle, bg=WHITE, fg=GREY,
                         font=("Segoe UI", 8)).pack(anchor="w", padx=18)
            tk.Frame(block, bg=BORDER, height=1).pack(
                fill="x", padx=18, pady=(8, 0))
            return block

        # ---- APPEARANCE ----
        appearance = section("APPEARANCE", "Choose how the app looks to you.")

        row = tk.Frame(appearance, bg=WHITE)
        row.pack(fill="x", padx=18, pady=(12, 4))

        tk.Label(row, text="Theme", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(side="left")

        theme_var = tk.StringVar(value="Dark" if self.dark_mode else "Light")

        def apply_theme_choice():
            self.set_theme(theme_var.get() == "Dark")

        tk.Radiobutton(
            row, text="Light", variable=theme_var, value="Light",
            bg=WHITE, fg=TEXT, selectcolor=WHITE,
            font=("Segoe UI", 9), command=apply_theme_choice,
            activebackground=WHITE
        ).pack(side="left", padx=(15, 0))

        tk.Radiobutton(
            row, text="Dark", variable=theme_var, value="Dark",
            bg=WHITE, fg=TEXT, selectcolor=WHITE,
            font=("Segoe UI", 9), command=apply_theme_choice,
            activebackground=WHITE
        ).pack(side="left", padx=(10, 0))

        size_row = tk.Frame(appearance, bg=WHITE)
        size_row.pack(fill="x", padx=18, pady=(6, 14))

        tk.Label(size_row, text="Text Size", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(side="left")

        size_var = tk.StringVar(value=get_setting("text_size"))
        size_menu = tk.OptionMenu(size_row, size_var,
                                  "Small", "Medium", "Large")
        size_menu.config(bg=WHITE, fg=TEXT, font=("Segoe UI", 9),
                         relief="solid", bd=1, highlightthickness=0)
        size_menu["menu"].config(bg=WHITE, fg=TEXT)
        size_menu.pack(side="left", padx=(15, 0))

        def save_size(*args):
            set_setting("text_size", size_var.get())
            messagebox.showinfo(
                "Text Size",
                f"Text size set to {size_var.get()}.\n\n"
                "This will apply after you close and reopen the Settings window."
            )

        size_var.trace_add("write", save_size)

        # ---- NOTIFICATIONS ----
        notif = section("NOTIFICATIONS",
                        "Choose what you want to be notified about.")

        def make_toggle(parent, key, label):
            var = tk.BooleanVar(value=get_setting(key) == "1")
            cb = tk.Checkbutton(
                parent, text=label, variable=var,
                bg=WHITE, fg=TEXT, selectcolor=WHITE,
                font=("Segoe UI", 9), anchor="w",
                activebackground=WHITE,
                command=lambda: set_setting(key, "1" if var.get() else "0")
            )
            cb.pack(fill="x", padx=18, pady=3)

        make_toggle(notif, "notify_reports",
                    "Notify me when my report status changes")
        make_toggle(notif, "notify_jobs",
                    "Notify me about new job opportunities")
        make_toggle(notif, "notify_events",
                    "Notify me about new community events")
        make_toggle(notif, "notify_news",
                    "Notify me about new community news")

        tk.Frame(notif, bg=WHITE, height=10).pack()

        # ---- ACCOUNT ----
        account = section("ACCOUNT", "Manage your personal account details.")

        account_row = tk.Frame(account, bg=WHITE)
        account_row.pack(fill="x", padx=18, pady=(12, 6))

        tk.Label(account_row, text="Username:", bg=WHITE, fg=GREY,
                 font=("Segoe UI", 9)).pack(side="left")
        tk.Label(account_row, text=str(self.current_user or "Guest"),
                 bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(side="left", padx=6)

        role_row = tk.Frame(account, bg=WHITE)
        role_row.pack(fill="x", padx=18, pady=(0, 10))

        tk.Label(role_row, text="Role:", bg=WHITE, fg=GREY,
                 font=("Segoe UI", 9)).pack(side="left")
        tk.Label(
            role_row,
            text=("Administrator" if self.current_role == "admin" else "Resident"),
            bg=WHITE, fg=GREEN, font=("Segoe UI", 9, "bold")
        ).pack(side="left", padx=6)

        btn_row = tk.Frame(account, bg=WHITE)
        btn_row.pack(fill="x", padx=18, pady=(0, 14))

        self.make_button(
            btn_row, "CHANGE DISPLAY NAME",
            self._change_display_name, BLUE, 22
        ).pack(side="left", padx=(0, 8))

        self.make_button(
            btn_row, "CHANGE PASSWORD",
            self._change_password, DARK_GREEN, 20
        ).pack(side="left")

        # ---- ABOUT ----
        about = section("ABOUT", "")

        about_info = [
            ("Application", "Umzimkhulu Connect"),
            ("Version", "1.0.0"),
            ("Province", "KwaZulu-Natal"),
            ("Municipality", "Umzimkhulu"),
            ("Support", "Admin02@gmail.com")
        ]

        for label, value in about_info:
            r = tk.Frame(about, bg=WHITE)
            r.pack(fill="x", padx=18, pady=2)
            tk.Label(r, text=f"{label}:", bg=WHITE, fg=GREY,
                     font=("Segoe UI", 9), width=14,
                     anchor="w").pack(side="left")
            tk.Label(r, text=value, bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(side="left")

        tk.Frame(about, bg=WHITE, height=10).pack()

        # ---- RESET ----
        reset_row = tk.Frame(body, bg=BG)
        reset_row.pack(fill="x", padx=20, pady=(18, 6))

        def reset_all():
            if messagebox.askyesno(
                "Reset Settings",
                "Are you sure you want to reset all settings to default?"
            ):
                for key, value in DEFAULT_SETTINGS.items():
                    set_setting(key, value)
                self.dark_mode = False
                self.apply_theme()
                messagebox.showinfo(
                    "Settings Reset",
                    "All settings have been restored to default.\n"
                    "Please close and reopen the Settings window."
                )

        self.make_button(
            reset_row, "RESET ALL SETTINGS", reset_all, ORANGE, 22
        ).pack(side="left")

        # ---- CLOSE ----
        close_row = tk.Frame(body, bg=BG)
        close_row.pack(fill="x", padx=20, pady=(8, 20))

        self.make_button(
            close_row, "CLOSE", settings.destroy, GREY, 22
        ).pack(side="right")

        self.apply_theme(settings)


    # ========================================================
    # ACCOUNT ACTIONS
    # ========================================================

    def _change_display_name(self):
        if not self.current_user:
            messagebox.showerror("Error", "You are not logged in.")
            return

        dialog = tk.Toplevel(self.root)
        dialog.title("Change Display Name")
        dialog.geometry("420x260")
        dialog.configure(bg=WHITE)
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text="CHANGE DISPLAY NAME",
                 bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 16, "bold")).pack(pady=(25, 15))

        tk.Label(dialog, text="NEW FULL NAME", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=40)

        name_entry = tk.Entry(dialog, font=("Segoe UI", 10), width=35)
        name_entry.pack(pady=(4, 15))

        current = q(
            "SELECT full_name FROM users WHERE username=?",
            (self.current_user,)
        )
        if current:
            name_entry.insert(0, current[0][0])

        def save():
            new_name = name_entry.get().strip()
            if not new_name:
                messagebox.showerror("Error", "Please enter a name.")
                return

            update("users", self._user_id(), {"full_name": new_name})
            messagebox.showinfo("Success",
                                "Display name updated successfully.")
            dialog.destroy()

        self.make_button(dialog, "SAVE", save, GREEN, 20).pack(pady=10)


    def _change_password(self):
        if not self.current_user:
            messagebox.showerror("Error", "You are not logged in.")
            return

        dialog = tk.Toplevel(self.root)
        dialog.title("Change Password")
        dialog.geometry("420x360")
        dialog.configure(bg=WHITE)
        dialog.transient(self.root)
        dialog.grab_set()

        tk.Label(dialog, text="CHANGE PASSWORD",
                 bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 16, "bold")).pack(pady=(25, 15))

        tk.Label(dialog, text="CURRENT PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=40)
        current_entry = tk.Entry(dialog, font=("Segoe UI", 10),
                                 width=35, show="*")
        current_entry.pack(pady=(4, 12))

        tk.Label(dialog, text="NEW PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=40)
        new_entry = tk.Entry(dialog, font=("Segoe UI", 10),
                             width=35, show="*")
        new_entry.pack(pady=(4, 12))

        tk.Label(dialog, text="CONFIRM NEW PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=40)
        confirm_entry = tk.Entry(dialog, font=("Segoe UI", 10),
                                 width=35, show="*")
        confirm_entry.pack(pady=(4, 12))

        def save():
            cur_pwd = current_entry.get()
            new_pwd = new_entry.get()
            confirm_pwd = confirm_entry.get()

            if not cur_pwd or not new_pwd or not confirm_pwd:
                messagebox.showerror("Error", "Please complete all fields.")
                return

            result = q(
                "SELECT password FROM users WHERE username=?",
                (self.current_user,)
            )
            if not result or not check_password(cur_pwd, result[0][0]):
                messagebox.showerror("Error", "Current password is incorrect.")
                return

            if len(new_pwd) < 6:
                messagebox.showerror(
                    "Error",
                    "New password must be at least 6 characters."
                )
                return

            if new_pwd != confirm_pwd:
                messagebox.showerror("Error", "Passwords do not match.")
                return

            update("users", self._user_id(),
                   {"password": hash_password(new_pwd)})

            messagebox.showinfo(
                "Success", "Your password has been updated successfully."
            )
            dialog.destroy()

        self.make_button(dialog, "SAVE", save, GREEN, 20).pack(pady=10)


    def _user_id(self):
        result = q(
            "SELECT id FROM users WHERE username=?",
            (self.current_user,)
        )
        return result[0][0] if result else None


    def _refresh_theme_after_build(self):
        self.root.after_idle(self.apply_theme)


    # ========================================================
    # WELCOME PAGE
    # ========================================================

    def show_welcome(self):

        self.clear()

        main = tk.Frame(self.root, bg=BG)
        main.pack(fill="both", expand=True)

        card = tk.Frame(
            main, bg=WHITE,
            highlightbackground=BORDER, highlightthickness=1
        )
        card.place(relx=0.5, rely=0.5, anchor="center",
                   width=600, height=500)

        if self.welcome_logo_photo is not None:
            logo_bg = tk.Label(card, image=self.welcome_logo_photo, bg=WHITE)
            logo_bg.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="KWAZULU-NATAL", bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 11, "bold")).pack(pady=(40, 4))

        tk.Label(card, text="UMZIMKHULU CONNECT", bg=WHITE, fg=DARK,
                 font=("Segoe UI", 27, "bold")).pack(pady=(0, 10))

        tk.Label(card, text="Your digital community platform",
                 bg=WHITE, fg=GREY,
                 font=("Segoe UI", 12)).pack(pady=(0, 35))

        self.make_button(card, "RESIDENT SIGN IN",
                         self.show_login, GREEN, 25).pack(pady=8)
        self.make_button(card, "CREATE ACCOUNT",
                         self.show_signup, DARK, 25).pack(pady=8)
        self.make_button(card, "ADMIN SIGN IN",
                         self.show_admin_login, BLUE, 25).pack(pady=8)


    # ========================================================
    # RESIDENT SIGN UP
    # ========================================================

    def show_signup(self):

        self.clear()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="both", expand=True)

        self.signup_background_photo = self._make_login_background(frame)

        card = tk.Frame(frame, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center",
                   width=550, height=600)

        tk.Label(card, text="CREATE ACCOUNT", bg=WHITE, fg=DARK,
                 font=("Segoe UI", 24, "bold")).pack(pady=(35, 25))

        tk.Label(card, text="FULL NAME", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=60)
        full_name = tk.Entry(card, font=("Segoe UI", 11), width=40)
        full_name.pack(pady=(5, 15))

        tk.Label(card, text="USERNAME / EMAIL", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=60)
        username = tk.Entry(card, font=("Segoe UI", 11), width=40)
        username.pack(pady=(5, 15))

        tk.Label(card, text="PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=60)
        password = tk.Entry(card, font=("Segoe UI", 11), width=40, show="*")
        password.pack(pady=(5, 15))

        tk.Label(card, text="CONFIRM PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=60)
        confirm = tk.Entry(card, font=("Segoe UI", 11), width=40, show="*")
        confirm.pack(pady=(5, 20))

        def register():
            name = full_name.get().strip()
            user = username.get().strip()
            pwd = password.get()
            confirm_pwd = confirm.get()

            if not name or not user or not pwd:
                messagebox.showerror("Error", "Please complete all fields.")
                return

            if pwd != confirm_pwd:
                messagebox.showerror("Error", "Passwords do not match.")
                return

            if len(pwd) < 6:
                messagebox.showerror(
                    "Error",
                    "Password must contain at least 6 characters."
                )
                return

            if q("SELECT id FROM users WHERE username=?", (user,)):
                messagebox.showerror("Error", "Username already exists.")
                return

            insert("users", {
                "full_name": name,
                "username": user,
                "password": hash_password(pwd),
                "role": "resident",
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            })

            messagebox.showinfo(
                "Account Created",
                "Your account was created successfully.\n\n"
                "Please sign in using your new account."
            )
            self.show_login()

        self.make_button(card, "CREATE ACCOUNT",
                         register, GREEN, 25).pack()
        self.make_button(card, "BACK TO SIGN IN",
                         self.show_login, DARK, 25).pack(pady=10)


    # ========================================================
    # RESIDENT LOGIN
    # ========================================================

    def show_login(self):

        self.clear()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="both", expand=True)

        # Background photo with dark-green overlay
        self.login_background_photo = self._make_login_background(frame)

        card = tk.Frame(frame, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center",
                   width=520, height=520)

        tk.Label(card, text="KWAZULU-NATAL", bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 10, "bold")).pack(pady=(40, 2))

        tk.Label(card, text="RESIDENT SIGN IN", bg=WHITE, fg=DARK,
                 font=("Segoe UI", 24, "bold")).pack(pady=(0, 35))

        tk.Label(card, text="USERNAME / EMAIL", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=65)
        username = tk.Entry(card, font=("Segoe UI", 11), width=40)
        username.pack(pady=(5, 20))

        tk.Label(card, text="PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=65)
        password = tk.Entry(card, font=("Segoe UI", 11), width=40, show="*")
        password.pack(pady=(5, 20))

        def login():
            user = username.get().strip()
            pwd = password.get()

            result = q(
                "SELECT full_name, username, password, role "
                "FROM users WHERE username=?",
                (user,)
            )

            if not result:
                messagebox.showerror("Login Failed",
                                     "Invalid username or password.")
                return

            (full_name, db_username, stored_password, role) = result[0]

            if not check_password(pwd, stored_password):
                messagebox.showerror("Login Failed",
                                     "Invalid username or password.")
                return

            self.current_user = db_username
            self.current_role = role
            self.show_app()

        self.make_button(card, "SIGN IN", login, GREEN, 25).pack()

        forgot = tk.Button(
            card, text="FORGOT PASSWORD?",
            command=self.show_forgot_password,
            bg=WHITE, fg=BLUE, relief="flat", bd=0,
            cursor="hand2", font=("Segoe UI", 9, "bold")
        )
        forgot.pack(pady=12)

        self.make_button(card, "CREATE ACCOUNT",
                         self.show_signup, DARK, 25).pack(pady=5)
        self.make_button(card, "BACK",
                         self.show_welcome, GREY, 25).pack(pady=5)


    # ========================================================
    # RESIDENT FORGOT PASSWORD
    # ========================================================

    def show_forgot_password(self):

        self.clear()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="both", expand=True)

        self.forgot_background_photo = self._make_login_background(frame)

        card = tk.Frame(frame, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center",
                   width=540, height=520)

        tk.Label(card, text="FORGOT PASSWORD", bg=WHITE, fg=DARK,
                 font=("Segoe UI", 24, "bold")).pack(pady=(50, 30))

        tk.Label(card, text="USERNAME / EMAIL", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=65)
        username = tk.Entry(card, font=("Segoe UI", 11), width=40)
        username.pack(pady=(5, 20))

        tk.Label(card, text="NEW PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=65)
        new_password = tk.Entry(card, font=("Segoe UI", 11),
                                width=40, show="*")
        new_password.pack(pady=(5, 20))

        def reset_password():
            user = username.get().strip()
            new_pwd = new_password.get()

            if not user or not new_pwd:
                messagebox.showerror("Error",
                                     "Please complete all fields.")
                return

            if len(new_pwd) < 6:
                messagebox.showerror(
                    "Error",
                    "Password must contain at least 6 characters."
                )
                return

            result = q("SELECT id FROM users WHERE username=?", (user,))
            if not result:
                messagebox.showerror("Error", "Account not found.")
                return

            conn = connection()
            cur = conn.cursor()
            cur.execute(
                "UPDATE users SET password=? WHERE username=?",
                (hash_password(new_pwd), user)
            )
            conn.commit()
            conn.close()

            messagebox.showinfo("Password Updated",
                                "Your password has been updated successfully.")
            self.show_login()

        self.make_button(card, "RESET PASSWORD",
                         reset_password, GREEN, 25).pack()
        self.make_button(card, "BACK TO SIGN IN",
                         self.show_login, DARK, 25).pack(pady=12)


    # ========================================================
    # ADMIN LOGIN
    # ========================================================

    def show_admin_login(self):

        self.clear()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="both", expand=True)

        self.admin_login_background_photo = self._make_login_background(frame)

        card = tk.Frame(frame, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center",
                   width=540, height=550)

        tk.Label(card, text="KWAZULU-NATAL", bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 10, "bold")).pack(pady=(40, 2))

        tk.Label(card, text="ADMIN SIGN IN", bg=WHITE, fg=DARK,
                 font=("Segoe UI", 25, "bold")).pack(pady=(0, 35))

        tk.Label(card, text="EMAIL", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=65)
        email = tk.Entry(card, font=("Segoe UI", 11), width=40)
        email.pack(pady=(5, 20))

        tk.Label(card, text="PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=65)
        password = tk.Entry(card, font=("Segoe UI", 11),
                            width=40, show="*")
        password.pack(pady=(5, 20))

        def login():
            entered_email = email.get().strip()
            entered_password = password.get()

            if (entered_email.lower() == ADMIN_EMAIL.lower()
                    and entered_password == ADMIN_PASSWORD):
                self.current_user = ADMIN_EMAIL
                self.current_role = "admin"
                self.show_app()
            else:
                messagebox.showerror(
                    "Login Failed",
                    "Invalid administrator email or password."
                )

        self.make_button(card, "ADMIN SIGN IN",
                         login, BLUE, 25).pack()

        forgot = tk.Button(
            card, text="FORGOT PASSWORD?",
            command=self.show_admin_forgot_password,
            bg=WHITE, fg=BLUE, relief="flat", bd=0,
            cursor="hand2", font=("Segoe UI", 9, "bold")
        )
        forgot.pack(pady=12)

        self.make_button(card, "BACK",
                         self.show_welcome, GREY, 25).pack()


    # ========================================================
    # ADMIN FORGOT PASSWORD
    # ========================================================

    def show_admin_forgot_password(self):

        self.clear()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(fill="both", expand=True)

        self.admin_forgot_background_photo = self._make_login_background(frame)

        card = tk.Frame(frame, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center",
                   width=560, height=580)

        tk.Label(card, text="ADMIN PASSWORD", bg=WHITE, fg=DARK,
                 font=("Segoe UI", 23, "bold")).pack(pady=(45, 10))

        tk.Label(card, text="RESET ADMIN PASSWORD", bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 12, "bold")).pack(pady=(0, 30))

        tk.Label(card, text="ADMIN EMAIL", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=65)
        email = tk.Entry(card, font=("Segoe UI", 11), width=40)
        email.pack(pady=(5, 20))

        tk.Label(card, text="NEW PASSWORD", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=65)
        password = tk.Entry(card, font=("Segoe UI", 11),
                            width=40, show="*")
        password.pack(pady=(5, 20))

        tk.Label(
            card,
            text="NOTE: This demo uses the fixed administrator credentials.",
            bg=WHITE, fg=GREY, font=("Segoe UI", 9), wraplength=420
        ).pack(pady=5)

        def reset():
            entered_email = email.get().strip()
            new_password = password.get()

            if entered_email.lower() != ADMIN_EMAIL.lower():
                messagebox.showerror(
                    "Error",
                    "Administrator email is incorrect."
                )
                return

            if len(new_password) < 6:
                messagebox.showerror(
                    "Error",
                    "Password must contain at least 6 characters."
                )
                return

            messagebox.showinfo(
                "Password Reset",
                "For this demo version, the administrator "
                "password remains the fixed password:\n\n"
                "Admin123"
            )
            self.show_admin_login()

        self.make_button(card, "RESET PASSWORD",
                         reset, BLUE, 25).pack(pady=15)
        self.make_button(card, "BACK",
                         self.show_admin_login, GREY, 25).pack()


    # ========================================================
    # MAIN APP
    # ========================================================

    def show_app(self):

        self.clear()
        self.menu_buttons = {}

        self.sidebar = tk.Frame(self.root, bg=SIDEBAR, width=250)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        brand = tk.Frame(self.sidebar, bg=SIDEBAR)
        brand.pack(fill="x", padx=20, pady=(22, 8))

        logo = tk.Frame(brand, bg=GREEN, width=46, height=46)
        logo.pack(side="left")
        logo.pack_propagate(False)
        tk.Label(logo, text="UC", bg=GREEN, fg=WHITE,
                 font=("Segoe UI", 14, "bold")).pack(expand=True)

        brand_text = tk.Frame(brand, bg=SIDEBAR)
        brand_text.pack(side="left", padx=11)
        tk.Label(brand_text, text="Umzimkhulu", bg=SIDEBAR, fg=WHITE,
                 font=("Segoe UI", 14, "bold")).pack(anchor="w")
        tk.Label(brand_text, text="CONNECT", bg=SIDEBAR, fg="#8FE0B8",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w")

        tk.Label(self.sidebar, text="COMMUNITY DIGITAL SERVICES",
                 bg=SIDEBAR, fg="#7F9A91",
                 font=("Segoe UI", 7, "bold")).pack(
                     anchor="w", padx=22, pady=(0, 20))

        user_card = tk.Frame(self.sidebar, bg="#17382E",
                             highlightbackground="#285548",
                             highlightthickness=1)
        user_card.pack(fill="x", padx=14, pady=(0, 18))

        avatar = tk.Frame(user_card, bg=GREEN, width=34, height=34)
        avatar.pack(side="left", padx=12, pady=12)
        avatar.pack_propagate(False)
        initial = str(self.current_user or "R").strip()[:1].upper()
        tk.Label(avatar, text=initial, bg=GREEN, fg=WHITE,
                 font=("Segoe UI", 12, "bold")).pack(expand=True)

        identity = tk.Frame(user_card, bg="#17382E")
        identity.pack(side="left", fill="x", expand=True, pady=9)
        tk.Label(identity, text=str(self.current_user or "Resident"),
                 bg="#17382E", fg=WHITE,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        tk.Label(
            identity,
            text=("Administrator" if self.current_role == "admin" else "Resident"),
            bg="#17382E", fg="#8FE0B8", font=("Segoe UI", 8)
        ).pack(anchor="w", pady=(2, 0))

        tk.Label(self.sidebar, text="WORKSPACE", bg=SIDEBAR, fg="#78958A",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=22, pady=(0, 6))

        self.menu_button("DASHBOARD", self.show_dashboard)
        self.menu_button("LOCAL BUSINESSES", self.show_businesses)
        self.menu_button("JOBS & OPPORTUNITIES", self.show_jobs)
        self.menu_button("COMMUNITY EVENTS", self.show_events)
        self.menu_button("COMMUNITY NEWS", self.show_news)
        self.menu_button("REPORT A PROBLEM", self.show_reports)

        if self.current_role == "admin":
            self.menu_button("MANAGE REPORTS", self.show_manage_reports)

        self.menu_button("EMERGENCY SERVICES", self.show_emergency)

        tk.Frame(self.sidebar, bg=SIDEBAR).pack(fill="both", expand=True)

        status = tk.Frame(self.sidebar, bg="#102A22")
        status.pack(fill="x", padx=14, pady=(0, 8))
        tk.Label(status, text="●  SYSTEM ONLINE", bg="#102A22", fg="#72D6A2",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=10, pady=(9, 1))
        tk.Label(status, text="Services are operating normally",
                 bg="#102A22", fg="#78958A",
                 font=("Segoe UI", 7)).pack(anchor="w", padx=10, pady=(0, 9))

        self.menu_button("SETTINGS", self.show_settings)
        self.menu_button("LOG OUT", self.logout, RED)

        self.content = tk.Frame(self.root, bg=BG)
        self.content.pack(side="right", fill="both", expand=True)

        self.show_dashboard()

    def menu_button(self, text, command, color=None):
        if color is None:
            color = SIDEBAR

        button = tk.Button(
            self.sidebar,
            text="   " + text,
            command=lambda: self._open_menu(text, command),
            bg=color, fg=WHITE,
            activebackground=SIDEBAR_HOVER, activeforeground=WHITE,
            relief="flat", bd=0, cursor="hand2",
            anchor="w", padx=14,
            font=("Segoe UI", 9, "bold"), pady=10
        )
        button.pack(fill="x", padx=10, pady=2)
        self.menu_buttons[text] = button
        return button

    def _open_menu(self, text, command):
        self.active_page = text
        for name, button in self.menu_buttons.items():
            if name == text:
                button.configure(bg=GREEN, fg=WHITE, activebackground=GREEN)
            elif name != "LOG OUT":
                button.configure(bg=SIDEBAR, fg=WHITE,
                                 activebackground=SIDEBAR_HOVER)
        command()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()
        self._refresh_theme_after_build()

    def page_header(self, title, subtitle=""):
        header = tk.Frame(self.content, bg=BG)
        header.pack(fill="x", padx=32, pady=(22, 10))

        top = tk.Frame(header, bg=BG)
        top.pack(fill="x")

        left = tk.Frame(top, bg=BG)
        left.pack(side="left", fill="x", expand=True)

        tk.Label(left, text=title, bg=BG, fg=TEXT,
                 font=("Segoe UI", 25, "bold")).pack(anchor="w")
        if subtitle:
            tk.Label(left, text=subtitle, bg=BG, fg=GREY,
                     font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 0))

        right = tk.Frame(top, bg=BG)
        right.pack(side="right", anchor="n")
        tk.Label(right, text="UMZIMKHULU CONNECT  •  KWAZULU-NATAL",
                 bg=SOFT_GREEN, fg=GREEN,
                 font=("Segoe UI", 8, "bold"),
                 padx=12, pady=6).pack()

        tk.Frame(header, bg=BORDER, height=1).pack(fill="x", pady=(15, 0))

    def update_clock(self):
        now = datetime.now()
        time_str = now.strftime("%A, %d %B %Y  |  %I:%M:%S %p")
        if (hasattr(self, 'dashboard_time_label')
                and self.dashboard_time_label.winfo_exists()):
            self.dashboard_time_label.config(text=time_str)
        self.root.after(1000, self.update_clock)


    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear_content()

        command_bar = tk.Frame(self.content, bg=WHITE,
                               highlightbackground=BORDER,
                               highlightthickness=1)
        command_bar.pack(fill="x", padx=32, pady=(20, 0))

        left = tk.Frame(command_bar, bg=WHITE)
        left.pack(side="left", padx=18, pady=13)
        tk.Label(left, text="COMMUNITY PORTAL", bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 8, "bold")).pack(anchor="w")
        tk.Label(left, text="Umzimkhulu local services and information",
                 bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(2, 0))

        right = tk.Frame(command_bar, bg=WHITE)
        right.pack(side="right", padx=18, pady=13)
        tk.Label(right, text="● Online", bg=SOFT_GREEN, fg=GREEN,
                 font=("Segoe UI", 8, "bold"),
                 padx=10, pady=5).pack(side="left", padx=(0, 10))
        self.dashboard_time_label = tk.Label(right, text="", bg=WHITE,
                                             fg=GREY,
                                             font=("Segoe UI", 8, "bold"))
        self.dashboard_time_label.pack(side="left")

        if not hasattr(self, '_clock_running'):
            self._clock_running = True
            self.update_clock()

        self.page_header("DASHBOARD",
                         "A central view of community services, opportunities and reports.")

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=32, pady=(4, 20))
        body = scroll.body

        businesses = q("SELECT COUNT(*) FROM businesses")[0][0]
        jobs = q("SELECT COUNT(*) FROM jobs")[0][0]
        events = q("SELECT COUNT(*) FROM events")[0][0]
        reports = q("SELECT COUNT(*) FROM reports")[0][0]

        hero = tk.Frame(body, bg=DARK,
                        highlightbackground=DARK, highlightthickness=1)
        hero.pack(fill="x", pady=(5, 14))

        hero_left = tk.Frame(hero, bg=DARK)
        hero_left.pack(side="left", fill="both", expand=True,
                       padx=24, pady=22)
        tk.Label(hero_left, text="WELCOME BACK", bg=DARK, fg="#8FE0B8",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w")
        tk.Label(hero_left, text="Your community at a glance.",
                 bg=DARK, fg=WHITE,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w", pady=(4, 2))
        tk.Label(hero_left,
                 text="Find services, discover opportunities and stay informed.",
                 bg=DARK, fg="#B8CEC6",
                 font=("Segoe UI", 9)).pack(anchor="w")

        hero_right = tk.Frame(hero, bg="#1A4738", width=180)
        hero_right.pack(side="right", fill="y")
        hero_right.pack_propagate(False)
        tk.Label(hero_right, text="UC", bg="#1A4738", fg="#8FE0B8",
                 font=("Segoe UI", 34, "bold")).pack(expand=True)

        tk.Label(body, text="OVERVIEW", bg=BG, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(3, 9))

        stats = tk.Frame(body, bg=BG)
        stats.pack(fill="x")

        cards = [
            ("LOCAL BUSINESSES", businesses, GREEN, "Directory"),
            ("JOB OPPORTUNITIES", jobs, BLUE, "Opportunities"),
            ("COMMUNITY EVENTS", events, ORANGE, "Upcoming"),
            ("REPORTS SUBMITTED", reports, RED, "Community issues")
        ]

        for title, value, color, note in cards:
            card = tk.Frame(stats, bg=WHITE,
                            highlightbackground=BORDER, highlightthickness=1)
            card.pack(side="left", fill="both", expand=True, padx=(0, 8))
            accent = tk.Frame(card, bg=color, width=5)
            accent.pack(side="left", fill="y")
            inside = tk.Frame(card, bg=WHITE)
            inside.pack(fill="both", expand=True, padx=15, pady=13)
            tk.Label(inside, text=title, bg=WHITE, fg=GREY,
                     font=("Segoe UI", 8, "bold")).pack(anchor="w")
            tk.Label(inside, text=str(value), bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 23, "bold")).pack(anchor="w", pady=(5, 0))
            tk.Label(inside, text=note, bg=WHITE, fg=color,
                     font=("Segoe UI", 8, "bold")).pack(anchor="w", pady=(1, 0))

        tk.Label(body, text="SERVICES & SHORTCUTS", bg=BG, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(24, 9))

        quick = tk.Frame(body, bg=BG)
        quick.pack(fill="x")

        quick_items = [
            ("LOCAL BUSINESSES", "Find businesses and local services.",
             self.show_businesses, GREEN),
            ("JOBS & OPPORTUNITIES", "Explore employment opportunities.",
             self.show_jobs, BLUE),
            ("COMMUNITY EVENTS", "See events happening locally.",
             self.show_events, ORANGE),
            ("REPORT A PROBLEM", "Submit a community issue.",
             self.show_reports, RED)
        ]

        for title, description, command, color in quick_items:
            card = tk.Frame(quick, bg=WHITE,
                            highlightbackground=BORDER, highlightthickness=1)
            card.pack(side="left", fill="both", expand=True, padx=(0, 8))
            tk.Frame(card, bg=color, height=4).pack(fill="x")
            tk.Label(card, text=title, bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(
                         anchor="w", padx=15, pady=(13, 3))
            tk.Label(card, text=description, bg=WHITE, fg=GREY,
                     font=("Segoe UI", 8),
                     wraplength=160, justify="left").pack(
                         anchor="w", padx=15, pady=(0, 11))
            tk.Button(card, text="OPEN  →", command=command,
                      bg=WHITE, fg=color,
                      activebackground=WHITE, activeforeground=color,
                      relief="flat", bd=0, cursor="hand2",
                      font=("Segoe UI", 8, "bold")).pack(
                          anchor="w", padx=12, pady=(0, 12))

        info = tk.Frame(body, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        info.pack(fill="x", pady=(18, 5))
        tk.Label(info, text="SYSTEM INFORMATION", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(
                     anchor="w", padx=18, pady=(14, 4))
        tk.Label(info,
                 text="Umzimkhulu Connect provides one place to access community information and services.",
                 bg=WHITE, fg=GREY, font=("Segoe UI", 8)).pack(
                     anchor="w", padx=18, pady=(0, 14))


    # ========================================================
    # BUSINESSES
    # ========================================================

    def show_businesses(self):

        self.clear_content()
        self.page_header("LOCAL BUSINESSES",
                         "Discover businesses and services in Umzimkhulu.")

        search_frame = tk.Frame(self.content, bg=BG)
        search_frame.pack(fill="x", padx=35, pady=(0, 5))

        tk.Label(search_frame, text="SEARCH BUSINESSES", bg=BG, fg=TEXT,
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 5))

        search_row = tk.Frame(search_frame, bg=BG)
        search_row.pack(fill="x")

        search_entry = tk.Entry(search_row, font=("Segoe UI", 11),
                                relief="solid", bd=1)
        search_entry.pack(side="left", fill="x", expand=True, ipady=7)
        search_entry.insert(0, "Search business, category or location...")

        def clear_placeholder(event):
            if search_entry.get() == "Search business, category or location...":
                search_entry.delete(0, "end")

        search_entry.bind("<FocusIn>", clear_placeholder)

        def search_businesses():
            search_text = search_entry.get().strip()
            if (not search_text
                    or search_text == "Search business, category or location..."):
                self.show_businesses()
                return
            self.perform_business_search(search_text)

        search_entry.bind("<Return>", lambda e: search_businesses())

        self.make_button(search_row, "SEARCH", search_businesses,
                         BLUE, 14).pack(side="left", padx=8)
        self.make_button(search_row, "BACK TO ALL SITES",
                         self.show_businesses, GREEN, 18).pack(side="left")

        if self.current_role == "admin":
            self.make_button(self.content, "ADD BUSINESS",
                             self.add_business, GREEN, 18).pack(
                                 anchor="e", padx=35, pady=8)

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=35, pady=15)

        businesses = q(
            "SELECT id, name, category, location, phone, information "
            "FROM businesses ORDER BY name"
        )

        if not businesses:
            tk.Label(scroll.body, text="No businesses have been added yet.",
                     bg=BG, fg=GREY,
                     font=("Segoe UI", 11)).pack(pady=30)

        for business in businesses:
            self.business_card(scroll.body, *business)


    def perform_business_search(self, search_text):
        search_text = search_text.strip()
        if not search_text:
            self.show_businesses()
            return

        self.clear_content()
        self.page_header("SEARCH RESULTS",
                         "Businesses matching your search.")

        controls = tk.Frame(self.content, bg=BG)
        controls.pack(fill="x", padx=35, pady=5)

        search_entry = tk.Entry(controls, font=("Segoe UI", 11),
                                relief="solid", bd=1)
        search_entry.pack(side="left", fill="x", expand=True, ipady=7)
        search_entry.insert(0, search_text)

        self.make_button(controls, "SEARCH",
                         lambda: self.perform_business_search(search_entry.get()),
                         BLUE, 14).pack(side="left", padx=8)
        self.make_button(controls, "BACK TO ALL SITES",
                         self.show_businesses, GREEN, 18).pack(side="left")

        search_entry.bind(
            "<Return>",
            lambda e: self.perform_business_search(search_entry.get())
        )

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=35, pady=15)

        search_value = search_text.lower()
        results = q(
            """
            SELECT id, name, category, location, phone, information
            FROM businesses
            WHERE LOWER(name) LIKE ?
               OR LOWER(category) LIKE ?
               OR LOWER(location) LIKE ?
               OR LOWER(information) LIKE ?
            ORDER BY name
            """,
            ("%" + search_value + "%",) * 4
        )

        if not results:
            tk.Label(scroll.body, text="NO BUSINESSES FOUND",
                     bg=BG, fg=RED,
                     font=("Segoe UI", 14, "bold")).pack(pady=(45, 5))
            tk.Label(scroll.body,
                     text="Try another business name, category or location.",
                     bg=BG, fg=GREY,
                     font=("Segoe UI", 10)).pack()
            return

        tk.Label(scroll.body,
                 text=f"{len(results)} BUSINESS(ES) FOUND",
                 bg=BG, fg=GREEN,
                 font=("Segoe UI", 12, "bold")).pack(
                     anchor="w", pady=(0, 10))

        for business in results:
            self.business_card(scroll.body, *business)


    def business_card(self, parent, record_id, name, category,
                      location, phone, information):

        card = tk.Frame(parent, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="x", pady=6)

        tk.Label(card, text=name, bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(
                     anchor="w", padx=20, pady=(15, 3))

        tk.Label(card, text=f"{category}  •  {location}",
                 bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 10, "bold"),
                 wraplength=850, justify="left").pack(anchor="w", padx=20)

        if phone:
            tk.Label(card, text=f"PHONE: {phone}",
                     bg=WHITE, fg=GREY,
                     font=("Segoe UI", 9)).pack(
                         anchor="w", padx=20, pady=5)

        if information:
            tk.Label(card, text=f"INFORMATION: {information}",
                     bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 9),
                     wraplength=850, justify="left").pack(
                         anchor="w", padx=20, pady=(0, 10))

        if self.current_role == "admin":
            btn_frame = tk.Frame(card, bg=WHITE)
            btn_frame.pack(anchor="e", padx=20, pady=(5, 15))
            self.make_button(btn_frame, "UPDATE",
                             lambda rid=record_id: self.update_business(rid),
                             BLUE, 12).pack(side="left", padx=(0, 8))
            self.make_button(btn_frame, "DELETE",
                             lambda rid=record_id: self.delete_business(rid),
                             RED, 12).pack(side="left")


    def add_business(self):

        dialog = tk.Toplevel(self.root)
        dialog.title("Add Business")
        dialog.geometry("500x600")
        dialog.configure(bg=BG)

        frame = tk.Frame(dialog, bg=BG)
        frame.pack(fill="both", expand=True, padx=35, pady=30)

        tk.Label(frame, text="ADD BUSINESS", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(
                     anchor="w", pady=(0, 20))

        entries = {}
        for field in ["NAME", "CATEGORY", "LOCATION", "PHONE"]:
            tk.Label(frame, text=field, bg=BG, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            entry = tk.Entry(frame, font=("Segoe UI", 10))
            entry.pack(fill="x", pady=(3, 12))
            entries[field] = entry

        tk.Label(frame, text="INFORMATION", bg=BG, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        information = tk.Text(frame, height=5, font=("Segoe UI", 10))
        information.pack(fill="both", expand=True, pady=(3, 12))

        def save():
            if not all(entries[f].get().strip()
                       for f in ["NAME", "CATEGORY", "LOCATION"]):
                messagebox.showerror("Error",
                                     "Please complete the required fields.")
                return
            insert("businesses", {
                "name": entries["NAME"].get().strip(),
                "category": entries["CATEGORY"].get().strip(),
                "location": entries["LOCATION"].get().strip(),
                "phone": entries["PHONE"].get().strip(),
                "information": information.get("1.0", "end").strip(),
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            dialog.destroy()
            self.show_businesses()

        self.make_button(frame, "SAVE BUSINESS",
                         save, GREEN, 20).pack(pady=10)


    def update_business(self, record_id):

        business = q(
            "SELECT id, name, category, location, phone, information "
            "FROM businesses WHERE id=?",
            (record_id,)
        )
        if not business:
            return
        business = business[0]

        dialog = tk.Toplevel(self.root)
        dialog.title("Update Business")
        dialog.geometry("500x600")
        dialog.configure(bg=BG)

        frame = tk.Frame(dialog, bg=BG)
        frame.pack(fill="both", expand=True, padx=35, pady=30)

        tk.Label(frame, text="UPDATE BUSINESS", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(
                     anchor="w", pady=(0, 20))

        entries = {}
        fields = ["NAME", "CATEGORY", "LOCATION", "PHONE"]
        values = [business[1], business[2], business[3], business[4]]

        for field, value in zip(fields, values):
            tk.Label(frame, text=field, bg=BG, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            entry = tk.Entry(frame, font=("Segoe UI", 10))
            entry.pack(fill="x", pady=(3, 12))
            entry.insert(0, value if value else "")
            entries[field] = entry

        tk.Label(frame, text="INFORMATION", bg=BG, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        information = tk.Text(frame, height=5, font=("Segoe UI", 10))
        information.pack(fill="both", expand=True, pady=(3, 12))
        information.insert("1.0", business[5] if business[5] else "")

        def save():
            if not all(entries[f].get().strip()
                       for f in ["NAME", "CATEGORY", "LOCATION"]):
                messagebox.showerror("Error",
                                     "Please complete the required fields.")
                return
            update("businesses", record_id, {
                "name": entries["NAME"].get().strip(),
                "category": entries["CATEGORY"].get().strip(),
                "location": entries["LOCATION"].get().strip(),
                "phone": entries["PHONE"].get().strip(),
                "information": information.get("1.0", "end").strip()
            })
            dialog.destroy()
            self.show_businesses()

        self.make_button(frame, "UPDATE BUSINESS",
                         save, BLUE, 20).pack(pady=10)


    def delete_business(self, record_id):
        if messagebox.askyesno(
            "Delete Business",
            "Are you sure you want to delete this business?"
        ):
            delete("businesses", record_id)
            self.show_businesses()


    # ========================================================
    # JOBS
    # ========================================================

    def show_jobs(self):

        self.clear_content()
        self.page_header("JOBS & OPPORTUNITIES",
                         "Explore employment and internship opportunities.")

        if self.current_role == "admin":
            self.make_button(self.content, "ADD JOB",
                             self.add_job, GREEN, 18).pack(
                                 anchor="e", padx=35, pady=5)

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=35, pady=15)

        jobs = q(
            "SELECT id, title, company, location, type "
            "FROM jobs ORDER BY id DESC"
        )

        if not jobs:
            tk.Label(scroll.body,
                     text="No job opportunities available.",
                     bg=BG, fg=GREY,
                     font=("Segoe UI", 11)).pack(pady=30)

        for job in jobs:
            self.job_card(scroll.body, *job)


    def job_card(self, parent, record_id, title, company,
                 location, job_type):

        card = tk.Frame(parent, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="x", pady=7)

        inner = tk.Frame(card, bg=WHITE)
        inner.pack(fill="both", expand=True, padx=20, pady=17)

        tk.Label(inner, text=title, bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(anchor="w")
        tk.Label(inner, text=company, bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 10, "bold")).pack(
                     anchor="w", pady=(3, 2))
        tk.Label(inner, text=f"LOCATION: {location}",
                 bg=WHITE, fg=GREY,
                 font=("Segoe UI", 9)).pack(anchor="w")
        tk.Label(inner, text=f"TYPE: {job_type}",
                 bg=WHITE, fg=GREY,
                 font=("Segoe UI", 9)).pack(anchor="w", pady=(2, 0))

        self.make_button(
            inner, "REQUIREMENTS",
            lambda t=title, c=company, l=location, jt=job_type:
                self.show_job_requirements(t, c, l, jt),
            BLUE, 18
        ).pack(anchor="w", pady=(10, 0))

        if self.current_role == "admin":
            btn_frame = tk.Frame(inner, bg=WHITE)
            btn_frame.pack(anchor="w", pady=(7, 0))
            self.make_button(btn_frame, "UPDATE",
                             lambda rid=record_id: self.update_job(rid),
                             BLUE, 15).pack(side="left", padx=(0, 8))
            self.make_button(btn_frame, "DELETE JOB",
                             lambda rid=record_id: self.delete_job(rid),
                             RED, 15).pack(side="left")


    def show_job_requirements(self, title, company, location, job_type):

        dialog = tk.Toplevel(self.root)
        dialog.title("Job Requirements")
        dialog.geometry("650x560")
        dialog.configure(bg=BG)
        dialog.transient(self.root)
        dialog.grab_set()

        frame = tk.Frame(dialog, bg=BG)
        frame.pack(fill="both", expand=True, padx=30, pady=25)

        tk.Label(frame, text="JOB REQUIREMENTS", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(anchor="w")
        tk.Label(frame, text=title, bg=BG, fg=GREEN,
                 font=("Segoe UI", 15, "bold")).pack(
                     anchor="w", pady=(10, 2))
        tk.Label(frame,
                 text=f"{company} • {location} • {job_type}",
                 bg=BG, fg=GREY,
                 font=("Segoe UI", 9, "bold"),
                 wraplength=560, justify="left").pack(
                     anchor="w", pady=(0, 20))

        tk.Label(frame, text="REQUIREMENTS", bg=BG, fg=TEXT,
                 font=("Segoe UI", 11, "bold")).pack(anchor="w")

        requirements = JOB_REQUIREMENTS.get(
            title, ["Requirements information is not available yet."]
        )

        for requirement in requirements:
            tk.Label(frame, text="• " + requirement,
                     bg=BG, fg=TEXT, font=("Segoe UI", 10),
                     wraplength=560, justify="left").pack(
                         anchor="w", pady=4)

        self.make_button(frame, "CLOSE",
                         dialog.destroy, GREEN, 20).pack(pady=20)


    def add_job(self):

        dialog = tk.Toplevel(self.root)
        dialog.title("Add Job")
        dialog.geometry("500x500")
        dialog.configure(bg=BG)

        frame = tk.Frame(dialog, bg=BG)
        frame.pack(fill="both", expand=True, padx=35, pady=30)

        tk.Label(frame, text="ADD JOB", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(
                     anchor="w", pady=(0, 20))

        entries = {}
        for field in ["TITLE", "COMPANY", "LOCATION", "TYPE"]:
            tk.Label(frame, text=field, bg=BG, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            entry = tk.Entry(frame, font=("Segoe UI", 10))
            entry.pack(fill="x", pady=(3, 12))
            entries[field] = entry

        def save():
            if not all(entries[f].get().strip()
                       for f in ["TITLE", "COMPANY", "LOCATION", "TYPE"]):
                messagebox.showerror("Error",
                                     "Please complete all fields.")
                return
            insert("jobs", {
                "title": entries["TITLE"].get().strip(),
                "company": entries["COMPANY"].get().strip(),
                "location": entries["LOCATION"].get().strip(),
                "type": entries["TYPE"].get().strip(),
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            dialog.destroy()
            self.show_jobs()

        self.make_button(frame, "SAVE JOB",
                         save, GREEN, 20).pack(pady=10)


    def update_job(self, record_id):

        job = q(
            "SELECT id, title, company, location, type "
            "FROM jobs WHERE id=?",
            (record_id,)
        )
        if not job:
            return
        job = job[0]

        dialog = tk.Toplevel(self.root)
        dialog.title("Update Job")
        dialog.geometry("500x500")
        dialog.configure(bg=BG)

        frame = tk.Frame(dialog, bg=BG)
        frame.pack(fill="both", expand=True, padx=35, pady=30)

        tk.Label(frame, text="UPDATE JOB", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(
                     anchor="w", pady=(0, 20))

        entries = {}
        fields = ["TITLE", "COMPANY", "LOCATION", "TYPE"]
        values = [job[1], job[2], job[3], job[4]]

        for field, value in zip(fields, values):
            tk.Label(frame, text=field, bg=BG, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            entry = tk.Entry(frame, font=("Segoe UI", 10))
            entry.pack(fill="x", pady=(3, 12))
            entry.insert(0, value if value else "")
            entries[field] = entry

        def save():
            if not all(entries[f].get().strip() for f in fields):
                messagebox.showerror("Error",
                                     "Please complete all fields.")
                return
            update("jobs", record_id, {
                "title": entries["TITLE"].get().strip(),
                "company": entries["COMPANY"].get().strip(),
                "location": entries["LOCATION"].get().strip(),
                "type": entries["TYPE"].get().strip()
            })
            dialog.destroy()
            self.show_jobs()

        self.make_button(frame, "UPDATE JOB",
                         save, BLUE, 20).pack(pady=10)


    def delete_job(self, record_id):
        if messagebox.askyesno(
            "Delete Job",
            "Are you sure you want to delete this job?"
        ):
            delete("jobs", record_id)
            self.show_jobs()


    # ========================================================
    # EVENTS
    # ========================================================

    def show_events(self):

        self.clear_content()
        self.page_header("COMMUNITY EVENTS",
                         "See upcoming events in Umzimkhulu.")

        if self.current_role == "admin":
            self.make_button(self.content, "ADD EVENT",
                             self.add_event, GREEN, 18).pack(
                                 anchor="e", padx=35, pady=5)

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=35, pady=15)

        events = q(
            "SELECT id, name, date, time, location "
            "FROM events ORDER BY date"
        )

        if not events:
            tk.Label(scroll.body,
                     text="No community events available.",
                     bg=BG, fg=GREY,
                     font=("Segoe UI", 11)).pack(pady=30)

        for event in events:
            self.event_card(scroll.body, *event)


    def event_card(self, parent, record_id, name, date, time, location):

        card = tk.Frame(parent, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="x", pady=6)

        tk.Label(card, text=name, bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(
                     anchor="w", padx=20, pady=(15, 3))
        tk.Label(card, text=f"DATE: {date}",
                 bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 10, "bold")).pack(
                     anchor="w", padx=20)
        tk.Label(card, text=f"TIME: {time}",
                 bg=WHITE, fg=GREY,
                 font=("Segoe UI", 9)).pack(
                     anchor="w", padx=20, pady=2)
        tk.Label(card, text=f"LOCATION: {location}",
                 bg=WHITE, fg=GREY,
                 font=("Segoe UI", 9)).pack(anchor="w", padx=20)

        if self.current_role == "admin":
            btn_frame = tk.Frame(card, bg=WHITE)
            btn_frame.pack(anchor="e", padx=20, pady=(7, 15))
            self.make_button(btn_frame, "UPDATE",
                             lambda rid=record_id: self.update_event(rid),
                             BLUE, 12).pack(side="left", padx=(0, 8))
            self.make_button(btn_frame, "DELETE",
                             lambda rid=record_id: self.delete_event(rid),
                             RED, 12).pack(side="left")


    def add_event(self):

        dialog = tk.Toplevel(self.root)
        dialog.title("Add Event")
        dialog.geometry("500x500")
        dialog.configure(bg=BG)

        frame = tk.Frame(dialog, bg=BG)
        frame.pack(fill="both", expand=True, padx=35, pady=30)

        tk.Label(frame, text="ADD EVENT", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(
                     anchor="w", pady=(0, 20))

        entries = {}
        for field in ["NAME", "DATE", "TIME", "LOCATION"]:
            tk.Label(frame, text=field, bg=BG, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            entry = tk.Entry(frame, font=("Segoe UI", 10))
            entry.pack(fill="x", pady=(3, 12))
            entries[field] = entry

        def save():
            if not all(entries[f].get().strip()
                       for f in ["NAME", "DATE", "TIME", "LOCATION"]):
                messagebox.showerror("Error",
                                     "Please complete all fields.")
                return
            insert("events", {
                "name": entries["NAME"].get().strip(),
                "date": entries["DATE"].get().strip(),
                "time": entries["TIME"].get().strip(),
                "location": entries["LOCATION"].get().strip(),
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            dialog.destroy()
            self.show_events()

        self.make_button(frame, "SAVE EVENT",
                         save, GREEN, 20).pack(pady=10)


    def update_event(self, record_id):

        event = q(
            "SELECT id, name, date, time, location "
            "FROM events WHERE id=?",
            (record_id,)
        )
        if not event:
            return
        event = event[0]

        dialog = tk.Toplevel(self.root)
        dialog.title("Update Event")
        dialog.geometry("500x500")
        dialog.configure(bg=BG)

        frame = tk.Frame(dialog, bg=BG)
        frame.pack(fill="both", expand=True, padx=35, pady=30)

        tk.Label(frame, text="UPDATE EVENT", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(
                     anchor="w", pady=(0, 20))

        entries = {}
        fields = ["NAME", "DATE", "TIME", "LOCATION"]
        values = [event[1], event[2], event[3], event[4]]

        for field, value in zip(fields, values):
            tk.Label(frame, text=field, bg=BG, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            entry = tk.Entry(frame, font=("Segoe UI", 10))
            entry.pack(fill="x", pady=(3, 12))
            entry.insert(0, value if value else "")
            entries[field] = entry

        def save():
            if not all(entries[f].get().strip() for f in fields):
                messagebox.showerror("Error",
                                     "Please complete all fields.")
                return
            update("events", record_id, {
                "name": entries["NAME"].get().strip(),
                "date": entries["DATE"].get().strip(),
                "time": entries["TIME"].get().strip(),
                "location": entries["LOCATION"].get().strip()
            })
            dialog.destroy()
            self.show_events()

        self.make_button(frame, "UPDATE EVENT",
                         save, BLUE, 20).pack(pady=10)


    def delete_event(self, record_id):
        if messagebox.askyesno(
            "Delete Event",
            "Are you sure you want to delete this event?"
        ):
            delete("events", record_id)
            self.show_events()


    # ========================================================
    # NEWS
    # ========================================================

    def show_news(self):

        self.clear_content()
        self.page_header("COMMUNITY NEWS",
                         "Stay updated with community information.")

        if self.current_role == "admin":
            self.make_button(self.content, "ADD NEWS",
                             self.add_news, GREEN, 18).pack(
                                 anchor="e", padx=35, pady=5)

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=35, pady=15)

        news = q(
            "SELECT id, title, description "
            "FROM news ORDER BY id DESC"
        )

        if not news:
            tk.Label(scroll.body,
                     text="No community news available.",
                     bg=BG, fg=GREY,
                     font=("Segoe UI", 11)).pack(pady=30)

        for record in news:
            self.news_card(scroll.body, *record)


    def news_card(self, parent, record_id, title, description):

        card = tk.Frame(parent, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        card.pack(fill="x", pady=6)

        tk.Label(card, text=title, bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(
                     anchor="w", padx=20, pady=(15, 5))
        tk.Label(card, text=description, bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9),
                 wraplength=850, justify="left").pack(
                     anchor="w", padx=20, pady=(0, 15))

        if self.current_role == "admin":
            btn_frame = tk.Frame(card, bg=WHITE)
            btn_frame.pack(anchor="e", padx=20, pady=(0, 15))
            self.make_button(btn_frame, "DELETE",
                             lambda rid=record_id: self.delete_news(rid),
                             RED, 12).pack(side="left")


    def add_news(self):

        dialog = tk.Toplevel(self.root)
        dialog.title("Add News")
        dialog.geometry("500x450")
        dialog.configure(bg=BG)

        frame = tk.Frame(dialog, bg=BG)
        frame.pack(fill="both", expand=True, padx=35, pady=30)

        tk.Label(frame, text="ADD NEWS", bg=BG, fg=TEXT,
                 font=("Segoe UI", 20, "bold")).pack(
                     anchor="w", pady=(0, 20))

        tk.Label(frame, text="TITLE", bg=BG, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        title_entry = tk.Entry(frame, font=("Segoe UI", 10))
        title_entry.pack(fill="x", pady=(3, 12))

        tk.Label(frame, text="DESCRIPTION", bg=BG, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        desc_entry = tk.Text(frame, height=5, font=("Segoe UI", 10))
        desc_entry.pack(fill="both", expand=True, pady=(3, 12))

        def save():
            t = title_entry.get().strip()
            d = desc_entry.get("1.0", "end").strip()
            if not t or not d:
                messagebox.showerror("Error",
                                     "Please complete all fields.")
                return
            insert("news", {
                "title": t,
                "description": d,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            dialog.destroy()
            self.show_news()

        self.make_button(frame, "SAVE NEWS",
                         save, GREEN, 20).pack(pady=10)


    def delete_news(self, record_id):
        if messagebox.askyesno(
            "Delete News",
            "Are you sure you want to delete this news entry?"
        ):
            delete("news", record_id)
            self.show_news()


    # ========================================================
    # REPORT A PROBLEM
    # ========================================================

    def show_reports(self):

        self.clear_content()
        self.page_header("REPORT A PROBLEM",
                         "Notify municipal authorities regarding community issues.")

        self.uploaded_doc_path = None

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=35, pady=15)

        form = tk.Frame(scroll.body, bg=WHITE,
                        highlightbackground=BORDER, highlightthickness=1)
        form.pack(fill="x", pady=10)

        inner = tk.Frame(form, bg=WHITE)
        inner.pack(fill="both", expand=True, padx=25, pady=25)

        tk.Label(inner, text="CATEGORY", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")

        categories = [
            "Water & Sanitation", "Roads & Potholes",
            "Electricity & Lighting", "Waste Management",
            "Public Safety", "Other"
        ]
        category_var = tk.StringVar(value=categories[0])
        category_opt = tk.OptionMenu(inner, category_var, *categories)
        category_opt.config(bg=WHITE, fg=TEXT,
                            font=("Segoe UI", 10),
                            bd=1, relief="solid")
        category_opt.pack(fill="x", pady=(3, 15))

        tk.Label(inner, text="LOCATION / ADDRESS", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        location_entry = tk.Entry(inner, font=("Segoe UI", 10))
        location_entry.pack(fill="x", pady=(3, 15))

        tk.Label(inner, text="DESCRIPTION OF ISSUE", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        desc_entry = tk.Text(inner, height=5, font=("Segoe UI", 10))
        desc_entry.pack(fill="both", expand=True, pady=(3, 15))

        tk.Label(inner, text="ATTACHMENT (OPTIONAL)",
                 bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 9, "bold")).pack(
                     anchor="w", pady=(5, 5))

        attach_frame = tk.Frame(inner, bg=WHITE)
        attach_frame.pack(fill="x", pady=(0, 15))

        doc_status = tk.Label(attach_frame, text="Document/Image: None",
                              bg=WHITE, fg=GREY, font=("Segoe UI", 9))

        def upload_document():
            path = filedialog.askopenfilename(
                title="Select Attachment Document/Photo",
                filetypes=[
                    ("All Supported Files",
                     "*.png;*.jpg;*.jpeg;*.pdf;*.docx;*.txt"),
                    ("Images", "*.png;*.jpg;*.jpeg"),
                    ("Documents", "*.pdf;*.docx;*.txt")
                ]
            )
            if path:
                filename = (f"doc_{int(time.time())}_"
                            + os.path.basename(path))
                dest = os.path.join(UPLOADS_DIR, filename)
                shutil.copy(path, dest)
                self.uploaded_doc_path = dest
                doc_status.config(
                    text=f"Document: {os.path.basename(path)}",
                    fg=GREEN
                )

        self.make_button(attach_frame, "UPLOAD ATTACHMENT",
                         upload_document, ORANGE, 20).pack(
                             side="left", padx=(0, 10))
        doc_status.pack(side="left")

        def submit():
            cat = category_var.get()
            loc = location_entry.get().strip()
            desc = desc_entry.get("1.0", "end").strip()

            if not loc or not desc:
                messagebox.showerror(
                    "Error",
                    "Please provide both location and description."
                )
                return

            insert("reports", {
                "category": cat,
                "description": desc,
                "location": loc,
                "status": "Pending",
                "reporter": self.current_user or "Anonymous",
                "document_path": self.uploaded_doc_path,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            })

            messagebox.showinfo(
                "Report Submitted",
                "Your report has been submitted to the municipal management system."
            )
            self.show_reports()

        self.make_button(inner, "SUBMIT REPORT",
                         submit, GREEN, 22).pack(anchor="w", pady=10)

        tk.Label(scroll.body, text="MY SUBMITTED REPORTS",
                 bg=BG, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(
                     anchor="w", pady=(20, 10))

        my_reports = q(
            "SELECT id, category, description, location, status, created "
            "FROM reports WHERE reporter=? ORDER BY id DESC",
            (self.current_user,)
        )

        if not my_reports:
            tk.Label(scroll.body,
                     text="You have not submitted any reports yet.",
                     bg=BG, fg=GREY,
                     font=("Segoe UI", 10)).pack(anchor="w")

        for r in my_reports:
            r_id, r_cat, r_desc, r_loc, r_stat, r_date = r
            r_card = tk.Frame(scroll.body, bg=WHITE,
                              highlightbackground=BORDER,
                              highlightthickness=1)
            r_card.pack(fill="x", pady=4)

            r_inner = tk.Frame(r_card, bg=WHITE)
            r_inner.pack(fill="both", expand=True, padx=15, pady=10)

            status_color = ORANGE if r_stat == "Pending" else GREEN

            tk.Label(r_inner, text=f"{r_cat} - {r_loc}",
                     bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 10, "bold")).pack(anchor="w")
            tk.Label(r_inner,
                     text=f"Status: {r_stat} | Date: {r_date}",
                     bg=WHITE, fg=status_color,
                     font=("Segoe UI", 9, "bold")).pack(
                         anchor="w", pady=(2, 0))


    # ========================================================
    # ADMIN MANAGE REPORTS
    # ========================================================

    def show_manage_reports(self):

        self.clear_content()
        self.page_header("MANAGE REPORTS",
                         "View and manage reported community issues.")

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=35, pady=15)

        reports = q(
            """
            SELECT id, category, description, location,
                   status, reporter, document_path, created
            FROM reports ORDER BY id DESC
            """
        )

        if not reports:
            tk.Label(scroll.body, text="No issues reported yet.",
                     bg=BG, fg=GREY,
                     font=("Segoe UI", 11)).pack(pady=30)

        for report in reports:
            (record_id, category, description, location,
             status, reporter, document_path, created) = report

            card = tk.Frame(scroll.body, bg=WHITE,
                            highlightbackground=BORDER,
                            highlightthickness=1)
            card.pack(fill="x", pady=6)

            inner = tk.Frame(card, bg=WHITE)
            inner.pack(fill="both", expand=True, padx=20, pady=15)

            tk.Label(inner,
                     text=f"[{status.upper()}] {category}",
                     bg=WHITE,
                     fg=(GREEN if status == "Resolved" else ORANGE),
                     font=("Segoe UI", 12, "bold")).pack(anchor="w")

            tk.Label(inner, text=f"LOCATION: {location}",
                     bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 10, "bold")).pack(
                         anchor="w", pady=(2, 0))

            tk.Label(inner,
                     text=f"REPORTER: {reporter} • SUBMITTED: {created}",
                     bg=WHITE, fg=GREY,
                     font=("Segoe UI", 8)).pack(
                         anchor="w", pady=(2, 5))

            tk.Label(inner, text=description,
                     bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 9),
                     wraplength=850, justify="left").pack(
                         anchor="w", pady=(0, 10))

            if document_path and os.path.exists(document_path):
                attach_info = tk.Frame(inner, bg=WHITE)
                attach_info.pack(anchor="w", pady=(0, 10))
                self.make_button(
                    attach_info, "OPEN ATTACHED FILE",
                    lambda dp=document_path:
                        os.startfile(dp) if hasattr(os, 'startfile') else None,
                    ORANGE, 20
                ).pack(side="left")

            controls = tk.Frame(inner, bg=WHITE)
            controls.pack(anchor="e", fill="x")

            def mark_resolved(rid=record_id):
                update_report_status(rid, "Resolved")
                self.show_manage_reports()

            def mark_pending(rid=record_id):
                update_report_status(rid, "Pending")
                self.show_manage_reports()

            if status != "Resolved":
                self.make_button(controls, "MARK RESOLVED",
                                 mark_resolved, GREEN, 16).pack(
                                     side="right", padx=4)
            else:
                self.make_button(controls, "MARK PENDING",
                                 mark_pending, ORANGE, 16).pack(
                                     side="right", padx=4)

            self.make_button(
                controls, "DELETE REPORT",
                lambda rid=record_id: self.delete_report(rid),
                RED, 16
            ).pack(side="right", padx=4)


    def delete_report(self, record_id):
        if messagebox.askyesno(
            "Delete Report",
            "Are you sure you want to delete this report?"
        ):
            delete("reports", record_id)
            self.show_manage_reports()


    # ========================================================
    # EMERGENCY SERVICES
    # ========================================================

    def show_emergency(self):

        self.clear_content()
        self.page_header("EMERGENCY SERVICES",
                         "Direct contact information for local emergency services.")

        scroll = ScrollFrame(self.content, bg=BG)
        scroll.pack(fill="both", expand=True, padx=35, pady=15)

        services = [
            ("SAPS (Police) Umzimkhulu", "039 259 0300 / 10111", RED),
            ("Umzimkhulu Hospital", "039 259 0310", BLUE),
            ("Ambulance Services (EMRS)", "10177 / 112", BLUE),
            ("Fire & Rescue Services", "039 259 0231", ORANGE),
            ("Municipal Disaster Management", "080 011 1238", DARK_GREEN)
        ]

        for name, phone, color in services:
            card = tk.Frame(scroll.body, bg=WHITE,
                            highlightbackground=BORDER,
                            highlightthickness=1)
            card.pack(fill="x", pady=8)

            accent = tk.Frame(card, bg=color, width=6)
            accent.pack(side="left", fill="y")

            inner = tk.Frame(card, bg=WHITE)
            inner.pack(fill="both", expand=True, padx=20, pady=18)

            tk.Label(inner, text=name, bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 14, "bold")).pack(anchor="w")
            tk.Label(inner, text=f"PHONE: {phone}",
                     bg=WHITE, fg=color,
                     font=("Segoe UI", 12, "bold")).pack(
                         anchor="w", pady=(5, 0))


    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self):
        if messagebox.askyesno(
            "Log Out",
            "Are you sure you want to log out?"
        ):
            self.current_user = None
            self.current_role = None
            self.show_welcome()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
