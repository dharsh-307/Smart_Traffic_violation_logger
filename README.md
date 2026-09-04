# Smart_Traffic_violation_logger
A Flask-based traffic violation management system that allows police officers to record violations, manage fines, track payment status, and generate QR-enabled digital challans.
# 🚦 Smart Traffic Violation Logger

A web-based traffic violation management system developed using **Python Flask** to help traffic police record, manage, and monitor traffic violations digitally.

## 📌 Project Overview

The **Smart Traffic Violation Logger** is designed to simplify the process of recording traffic violations and managing digital challans.

The system allows authorized users to enter vehicle details, violation information, location, date, and fine amount. It also provides features to view violation history, update payment status, and generate QR codes for accessing challan details.

This project demonstrates how **Web Development, Database Management, and QR Code Technology** can be combined to create a practical solution for traffic management.

## 🎯 Objectives

* Digitize the process of recording traffic violations.
* Reduce manual paperwork and data entry errors.
* Maintain a centralized database of violations.
* Track unpaid and paid fines.
* Generate digital challans with QR codes.
* Improve accessibility of violation records.

## ✨ Features

* 🚗 Record vehicle number and violation details.
* 📍 Store violation location and date.
* 💰 Record fine amount.
* 📋 View complete violation history.
* 🔄 Update payment status.
* 📱 Generate QR codes for challan details.
* 🔍 Access public violation status through QR code.
* 💾 Store data using SQLite database.

## 🛠️ Technologies Used

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Programming language   |
| Flask      | Web framework          |
| SQLite     | Database               |
| HTML       | Page structure         |
| CSS        | Styling                |
| Jinja2     | Dynamic templates      |
| QR Code    | Digital challan access |

## 📂 Project Structure

```text id="stl1042"
smart-traffic-violation-logger/
│
├── app.py
├── traffic.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── add_violation.html
│   ├── history.html
│   ├── edit_violation.html
│   └── public_status.html
│
└── static/
    └── style.css
```

> Update the structure according to your actual project files.

## 🧠 How the System Works

The system follows a simple workflow:

```text id="stl2026"
Enter Violation Details
          ↓
Save Data in SQLite
          ↓
View Violation History
          ↓
Update Payment Status
          ↓
Generate QR Code
          ↓
Access Public Challan Status
```

## 📊 Database Details

The application uses **SQLite** to store traffic violation records.

### Example Fields

| Field          | Description                    |
| -------------- | ------------------------------ |
| Vehicle Number | Registered vehicle number      |
| Violation Type | Type of traffic violation      |
| Location       | Place where violation occurred |
| Date           | Date of violation              |
| Fine Amount    | Amount of fine                 |
| Status         | Paid / Unpaid                  |

## 🚀 How to Run

### 1. Clone the Repository

```bash id="stlclone"
git clone https://github.com/your-username/smart-traffic-violation-logger.git
```

### 2. Navigate to the Project

```bash id="stlcd"
cd smart-traffic-violation-logger
```

### 3. Create a Virtual Environment

```bash id="stlvenv"
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash id="stlactivate"
venv\Scripts\activate
```

### 5. Install Dependencies

```bash id="stlpip"
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install Flask and QR Code support:

```bash id="stlinstall"
pip install flask qrcode[pil]
```

### 6. Run the Application

```bash id="stlrun"
python app.py
```

### 7. Open in Browser

Visit:

```text id="stlurl"
http://127.0.0.1:5000
```

## 📱 QR Code Feature

The system generates a QR code for each challan.

When the QR code is scanned, it opens the **public status page**, allowing users to view the violation details and payment status.

```text id="stlqr"
Digital Challan
      ↓
QR Code
      ↓
Public Status Page
      ↓
Violation Details
```

## 📈 Benefits

* Saves time in recording violations.
* Reduces paperwork.
* Provides organized digital records.
* Makes fine tracking easier.
* Improves transparency.
* Supports quick access to challan information.

## 🔮 Future Enhancements

* Add police officer login and authentication.
* Integrate online fine payment.
* Add SMS or email notifications.
* Generate downloadable PDF challans.
* Add dashboard with violation statistics.
* Integrate vehicle number plate recognition.
* Deploy the application online.

## 👩‍💻 Author

**Dharshani.D**

BCA Student | Web Development & AI Enthusiast

## 📄 License

This project is created for educational purposes.
