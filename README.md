# 🌍 **Umzimkhulu Connect**

[![View Project](https://img.shields.io/badge/View%20Project-GitHub-black?logo=github)](https://github.com/Second021/Umzimkhulu-Connect)

A desktop community information and reporting system developed for the Umzimkhulu community.
# 🌍 **Umzimkhulu Connect**

## 📖 **Overview**

**Umzimkhulu Connect** is a desktop community information and reporting system developed for the **Umzimkhulu community in KwaZulu-Natal, South Africa**.

The application is built with **Python and Tkinter** and uses **SQLite** to store users, businesses, jobs, events, community news, reports and settings.

The system is designed to make it easier for residents to:

* 🏪 Find local businesses and services
* 💼 Find jobs and opportunities
* 📅 View community events
* 📰 Read community news
* 🚨 Report community problems
* 📞 Access important services
* ⚙️ Manage application settings

---

## ✨ **Main Features**

### 👤 **Resident Features**

Residents can:

* 📝 Create an account and sign in.
* ⚙️ Manage their account settings.
* 🔎 Search for local businesses and services.
* 💼 View available jobs and opportunities.
* 📋 View job requirements.
* 📅 View community events.
* 📰 Read community news and updates.
* 🚨 Report community problems.
* 📎 Attach a document or image to a report.
* 📊 View the status of submitted reports.
* 📂 Open report attachments.
* 🚑 Access emergency and important service information.
* 🌙 Change between light and dark mode.
* 🔠 Change text size.
* 🔔 Enable or disable selected notifications.

---

## 👨‍💼 **Admin Features**

Administrators have access to additional management functions.

The admin can:

* ➕ Add local businesses.
* ✏️ Edit local businesses.
* 🗑️ Delete local businesses.
* ➕ Add jobs and opportunities.
* ✏️ Edit jobs and opportunities.
* 🗑️ Delete jobs and opportunities.
* ➕ Add community events.
* ✏️ Edit community events.
* 🗑️ Delete community events.
* ➕ Add community news.
* 🗑️ Delete community news.
* 👀 View all submitted reports.
* 🔄 Mark reports as **In Progress**.
* ✅ Mark reports as **Resolved**.
* 📂 Open report attachments.

The **Manage Reports** section is only shown when the current user is logged in as an administrator.

---

## 🚨 **Report a Problem**

The reporting system allows residents to report issues affecting the community.

### 📋 **Report Categories**

The application includes the following categories:

* 💧 Water & Sanitation
* 🛣️ Roads & Potholes
* 💡 Electricity & Lighting
* 🗑️ Waste Management
* 🛡️ Public Safety
* 📌 Other

A resident provides:

* 🏷️ Problem category
* 📝 Description
* 📍 Location

The resident can also attach:

* 📄 PDF/document
* 🖼️ Image

The selected file is copied to the application's `uploads` folder and its path is saved with the report.

New reports are created with the status:

**🟡 Pending**

Administrators can later change the status to:

**🔵 In Progress**

or

**🟢 Resolved**

---

## 🏠 **Dashboard**

After signing in residents and administrators can access the dashboard.

The dashboard provides quick access to:

* 🏪 Local Businesses
* 💼 Jobs & Opportunities
* 📅 Community Events
* 📰 Community News
* 🚨 Report a Problem
* 🚑 Emergency Services
* ⚙️ Settings

The dashboard also displays report statistics and system information.

---

## 🏪 **Local Businesses**

The **Local Businesses** section allows users to find useful businesses and services in the Umzimkhulu area.

The project includes default business data such as:

* 🛋️ Furniture stores
* 👕 Clothing stores
* 🛒 Supermarkets
* 🍴 Restaurants
* 🏦 Banks and financial services
* 🔨 Hardware stores
* 🚚 Transport and plant hire
* 🏛️ Municipal services
* 🏥 Health services
* 📱 Mobile network services
* 💇 Beauty services
* 🏪 Other local businesses

Administrators can:

* ➕ Add businesses
* ✏️ Update businesses
* 🗑️ Delete businesses

---

## 💼 **Jobs & Opportunities**

The **Jobs & Opportunities** section allows residents to view available opportunities.

Example job categories in the project include:

* 💻 IT Support Assistant
* 📑 Administrative Assistant
* 🛍️ Retail Sales Assistant
* 💾 Data Capturer
* 🤝 Community Outreach Assistant
* 🌐 Junior Web Developer
* 📊 Bookkeeping Assistant
* 📞 Customer Service Representative
* 👷 General Worker
* 📱 Social Media Assistant

The system can also display requirements for the selected position.

Administrators can:

* ➕ Add job opportunities
* ✏️ Update job opportunities
* 🗑️ Delete job opportunities

---

## 📅 **Community Events**

Residents can view community events stored in the system.

Administrators can:

* ➕ Add events
* ✏️ Update events
* 🗑️ Delete events

---

## 📰 **Community News**

The **Community News** section provides local announcements and updates.

Administrators can:

* ➕ Add news
* 🗑️ Delete news

Residents can read the available community news from the application.

---

## 🚑 **Emergency Services**

The **Emergency Services** section provides important service information and contact details for residents.

This section is designed to provide quick access to important community and emergency-related services.

---

## ⚙️ **Account and Settings**

The **Settings** section allows users to manage application preferences.

### 🎨 **Appearance**

Users can choose:

* ☀️ Light Mode
* 🌙 Dark Mode
* 🔠 Text Size

### 🔔 **Notifications**

Users can enable or disable notifications for:

* 🚨 Reports
* 💼 Jobs
* 📅 Events
* 📰 News

### 👤 **Account**

Users can manage their:

* 👤 Display name
* 🔑 Password

---

## 👥 **User Roles**

The application supports two main roles.

### 👤 **Resident**

Residents can access normal community services such as:

* 🏪 Businesses
* 💼 Jobs
* 📅 Events
* 📰 News
* 🚨 Reports
* 🚑 Emergency Services
* ⚙️ Settings

### 👨‍💼 **Admin**

Administrators have access to all resident features plus administration tools for managing system content and community reports.

---

## 🛠️ **Technologies Used**

### 🐍 **Programming Language**

* Python 3.9+

### 🖥️ **GUI**

* Tkinter

### 🗄️ **Database**

* SQLite

### 🖼️ **Image Processing**

* Pillow

### 📦 **Additional Python Modules**

The project also uses standard Python libraries including:

* `hashlib`
* `os`
* `re`
* `sqlite3`
* `shutil`
* `time`
* `math`
* `datetime`
* `tkinter`

Most of these modules are included with Python.

---

## 🔐 **Security**

Resident passwords are not stored as plain text.

The application uses:

* 🔐 PBKDF2-HMAC
* 🔒 SHA-256
* 🧂 Random password salts
* 🔁 Multiple hashing iterations

This helps protect resident passwords stored in the SQLite database.

---

## 📁 **Project Structure**

A typical project folder contains:

```text
Umzimkhulu Connect/
│
├── 🐍 Umzimkhulu_Connect.py
├── 🖼️ umzimkhulu_CoA.png.png
├── 🖼️ umzimkhulu_logo.png
├── 📖 README.md
├── 🗄️ umzimkhulu_connect.db
└── 📂 uploads/
```

### 🐍 **Main Files**

#### `Umzimkhulu_Connect.py`

This is the main Python application.

It contains:

* 🖥️ GUI screens
* 🔐 Login and registration
* 🗄️ Database operations
* 🏠 Dashboard
* 🏪 Businesses
* 💼 Jobs
* 📅 Events
* 📰 News
* 🚨 Reports
* 👨‍💼 Admin functions
* 🚑 Emergency services
* ⚙️ Settings
* 🎨 Theme management

#### `umzimkhulu_CoA.png.png`

Used by the application for the Umzimkhulu visual/login background.

#### `umzimkhulu_logo.png`

Used as the application logo.

#### `umzimkhulu_connect.db`

SQLite database created and used by the application.

#### `uploads/`

Stores files attached to community reports.

---

## 🗄️ **Database**

The application automatically creates and uses a SQLite database named:

```text
umzimkhulu_connect.db
```

The database stores information for areas such as:

* 👥 Users
* ⚙️ Settings
* 🏪 Businesses
* 💼 Jobs
* 📅 Events
* 📰 News
* 🚨 Reports

The database file is created automatically when the application is run.

---

## 📋 **Requirements**

Make sure **Python 3.9 or newer** is installed.

Install Pillow with:

```bash
pip install Pillow
```

Tkinter and SQLite are normally included with standard Python installations.

---

## 📥 **Installation**

### **1️⃣ Download or Clone the Project**

Download the project files or clone the repository.

### **2️⃣ Keep the Image Files in the Project Folder**

Make sure these files are available:

```text
umzimkhulu_CoA.png.png
umzimkhulu_logo.png
```

### **3️⃣ Install Pillow**

Run:

```bash
pip install Pillow
```

### **4️⃣ Run the Application**

Open a terminal in the project folder and run:

```bash
python Umzimkhulu_Connect.py
```

On the first run the application creates the SQLite database and the `uploads` directory automatically.

---

## 🔑 **Admin Login**

The current source code contains demo administrator credentials:

```text
Email: Admin02@gmail.com
Password: Admin123
```

These credentials are intended for the demonstration version of the application.

⚠️ **Important:** Change or remove the fixed admin credentials before using the project as a real production system.

---

## 📝 **Important Notes**

* 🖥️ This project is a desktop application.
* 🗄️ SQLite is used as the database.
* 📂 Report attachments are stored locally in the `uploads` folder.
* 📎 The application opens attachments using the operating system's default application.
* 🖼️ The current report system supports document and image attachments.
* 🎙️ The current source code does **not** include voice recording.
* 🎓 The project is intended mainly for learning demonstration and community-system development.

---

## 🎨 **Application Design**

The application uses a modern green-based interface inspired by the Umzimkhulu community environment.

The project includes:

* 📌 Sidebar navigation
* 📊 Dashboard cards
* 📈 Report statistics
* ☀️ Light mode
* 🌙 Dark mode
* 📜 Scrollable content
* 🔎 Search functionality
* 📝 Forms and management dialogs
* 🏷️ Status indicators
* 🌍 Community-focused navigation

---

## 🔄 **Example User Flow**

```text
🚀 Start Application
       │
       ▼
👋 Welcome Screen
       │
       ├── 👤 Resident Sign In
       │       │
       │       ▼
       │    🏠 Dashboard
       │       │
       │       ├── 🏪 Local Businesses
       │       ├── 💼 Jobs & Opportunities
       │       ├── 📅 Community Events
       │       ├── 📰 Community News
       │       ├── 🚨 Report a Problem
       │       ├── 🚑 Emergency Services
       │       └── ⚙️ Settings
       │
       └── 👨‍💼 Admin Sign In
               │
               ▼
            🏠 Dashboard
               │
               ├── 🏪 Manage Businesses
               ├── 💼 Manage Jobs
               ├── 📅 Manage Events
               ├── 📰 Manage News
               └── 🚨 Manage Reports
```

---

## 📊 **Report Status Flow**

```text
👤 Resident submits report
          │
          ▼
      🟡 Pending
          │
          ▼
    🔵 In Progress
          │
          ▼
      🟢 Resolved
```

---

## 🚀 **Future Improvements**

Possible future improvements include:

* 🎙️ Voice recording for problem reports.
* 🔎 More advanced search and filtering.
* 🏛️ Online municipal integration.
* 📧 Email or SMS notifications.
* ⚡ Real-time service updates.
* 🔐 Stronger administrator authentication.
* ☁️ Cloud database support.
* 📱 Mobile application support.
* 👤 Improved user verification.
* 📊 More detailed reporting and analytics.

---

## 🎯 **Project Purpose**

The main purpose of **Umzimkhulu Connect** is to provide a central platform where community members can access local information and communicate problems that affect their area.

The system demonstrates how a Python desktop application can combine:

* 🔐 User authentication
* 🗄️ Database management
* 🖥️ GUI development
* 📂 File handling
* 🌍 Community information
* 🚨 Reporting functionality
* 👨‍💼 Administrative management

---

## 👨‍💻 **Author**

**Tshangase Sinentlantla**

🎓 Final-Year BSc Information Technology Student
🏫 North-West University (NWU)

---

## 📜 **License**

This project is intended for educational and demonstration purposes.

Please update this section with your preferred license before publishing the project as an open-source application.

---

## ❤️ **Umzimkhulu Connect**

**Connecting the community with information opportunities and services. 🌍🤝**
