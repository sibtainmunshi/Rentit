# 🏠 RentIt - The Rental Marketplace

> A professional full-stack rental marketplace with Firebase authentication and dedicated booking system

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Firebase](https://img.shields.io/badge/Firebase-Firestore-orange.svg)](https://firebase.google.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)](https://tailwindcss.com/)
[![Status](https://img.shields.io/badge/Status-Demo%20Ready-success.svg)]()

**Version**: 3.0 | **Last Updated**: February 15, 2026

---

## 📖 About The Project

**RentIt** is a modern, professional rental marketplace platform featuring:
- 🔐 **Firebase Authentication**: Google Sign-In & Email/Password
- 🎫 **Professional Booking System**: Dedicated pages (Airbnb-style)
- 🎥 **Rent Products**: Cameras, bikes, electronics, furniture, books, camping gear
- 👨‍💻 **Hire Services**: Developers, cleaners, trainers, tutors, designers, movers
- 🏢 **Book Spaces**: Villas, apartments, offices, studios, event halls, gardens

### 🎯 Project Type: Case 3
This project combines concepts from:
- **FSD-1** (Full Stack Development) - Multi-page application with professional UI
- **Python-1** (Python Programming) - Flask backend with Firebase integration
- **DSA** (Data Structures & Algorithms) - Bubble Sort & Linear Search
- **DBMS** (Database Management Systems) - Firebase Firestore with CRUD operations

**Extra Marks**: 20% total (10% in FSD-1 + 10% in Python-1)

---

## ✨ Key Features

### 🔐 Authentication System
- Firebase Authentication integration
- Google Sign-In with OAuth
- Email/Password login and signup
- User session management
- Protected routes
- Profile display in navbar

### 🎫 Professional Booking System
- Dedicated booking page (not popup)
- Authentication guard
- Rental period selection
- Contact & delivery forms
- Dynamic price calculation
- Booking confirmation page
- Unique booking ID generation
- Print receipt functionality

### 🛍️ Shopping Experience
- 54 listings across 3 categories
- Smart filtering (27 subcategories)
- Price sorting (custom Bubble Sort)
- Product detail pages
- Cart & wishlist functionality
- Responsive design

### 🔧 Technical Features
- RESTful API (8 endpoints)
- Firebase Firestore integration
- Custom DSA algorithms
- Real-time data synchronization
- Fallback to mock data
- Error handling
- Loading states

---

## 🚀 Tech Stack

### Frontend
- HTML5
- Tailwind CSS (CDN)
- JavaScript ES6+ (Vanilla)
- FontAwesome Icons
- Google Fonts (Plus Jakarta Sans)

### Backend
- Python 3.8+
- Flask Framework
- Firebase Admin SDK
- Firebase Authentication SDK
- Custom DSA Algorithms

### Database
- Firebase Firestore (NoSQL)
- Collections: products, services, spaces
- LocalStorage (for bookings)

---

## 📂 Project Structure

```
RentIt/
├── app.py                          # Main Flask application
├── seed_database.py                # Database seeding script
├── requirements.txt                # Python dependencies
├── serviceAccountKey.json          # Firebase credentials (PRIVATE)
├── templates/
│   └── index.html                 # Main frontend page
├── static/
│   ├── css/                       # Custom CSS
│   ├── js/                        # Custom JavaScript
│   └── images/                    # Static images
├── utils/
│   └── dsa_logic.py               # Custom algorithms
└── docs/
    ├── FSD_DOCUMENTATION.md       # FSD concepts
    ├── PYTHON_DOCUMENTATION.md    # Python concepts
    ├── DSA_DBMS_DOCUMENTATION.md  # DSA & DBMS concepts
    ├── PROJECT_OVERVIEW.md        # Complete overview
    └── VIVA_PREPARATION_GUIDE.md  # Viva Q&A
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Firebase account
- Internet connection

### Step 1: Clone Repository
```bash
git clone <your-repo-url>
cd RentIt
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Firebase Setup
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create new project
3. Go to Project Settings → Service Accounts
4. Generate new private key
5. Save as `serviceAccountKey.json` in project root

### Step 4: Seed Database
```bash
python seed_database.py
```

### Step 5: Run Application
```bash
python app.py
```

### Step 6: Open Browser
Navigate to: `http://localhost:5000`

---

## 🎨 Features

### ✅ Implemented
- [x] Multi-category marketplace (Products, Services, Spaces)
- [x] Responsive design (mobile, tablet, desktop)
- [x] Product detail pages
- [x] Shopping cart functionality
- [x] Price sorting (custom Bubble Sort algorithm)
- [x] Product search (custom Linear Search)
- [x] Firebase database integration
- [x] RESTful API endpoints
- [x] Modern UI with animations
- [x] Toast notifications
- [x] Modal dialogs

### 🚧 Future Enhancements
- [ ] User authentication (Google Sign-In)
- [ ] Payment integration (Razorpay/Stripe)
- [ ] Real-time chat
- [ ] Booking calendar
- [ ] Image upload
- [ ] Reviews and ratings
- [ ] Admin dashboard
- [ ] Email notifications

---

## 📚 Documentation

Comprehensive documentation available in the following files:

1. **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** - Complete project overview
2. **[FSD_DOCUMENTATION.md](FSD_DOCUMENTATION.md)** - Full Stack Development concepts
3. **[PYTHON_DOCUMENTATION.md](PYTHON_DOCUMENTATION.md)** - Python programming concepts
4. **[DSA_DBMS_DOCUMENTATION.md](DSA_DBMS_DOCUMENTATION.md)** - DSA & DBMS concepts
5. **[VIVA_PREPARATION_GUIDE.md](VIVA_PREPARATION_GUIDE.md)** - Viva questions & answers

---

## 🎯 Key Concepts Demonstrated

### Full Stack Development (FSD-1)
- HTML5 semantic elements
- CSS3 styling and animations
- Responsive web design
- JavaScript ES6+ features
- DOM manipulation
- AJAX/Fetch API
- RESTful API design
- Flask framework

### Python Programming (Python-1)
- Flask web framework
- Firebase Admin SDK
- Functions and modules
- Error handling
- Data processing
- JSON handling
- Request/Response handling

### Data Structures & Algorithms (DSA)
- **Bubble Sort**: O(n²) time complexity
- **Linear Search**: O(n) time complexity
- Arrays/Lists operations
- Hash Tables/Dictionaries
- Time & Space complexity analysis

### Database Management (DBMS)
- NoSQL database design
- CRUD operations
- Collections and documents
- Data modeling
- Query operations
- Cloud database integration

---

## 🎤 API Endpoints

### GET /
Returns the main HTML page

### GET /api/listings
Fetch listings with optional filtering and sorting

**Query Parameters**:
- `category` (optional): products | services | spaces
- `sort` (optional): asc | desc

**Example**:
```
GET /api/listings?category=products&sort=asc
```

**Response**:
```json
[
  {
    "title": "Canon EOS R5",
    "price": "₹2,500",
    "rating": "4.9",
    "img": "https://...",
    "unit": "/day",
    "tag": "Hot"
  }
]
```

---

## 🔐 Security Notes

⚠️ **IMPORTANT**: Never commit `serviceAccountKey.json` to version control!

Add to `.gitignore`:
```
serviceAccountKey.json
__pycache__/
*.pyc
.env
```

---

## 🎓 Academic Information

**Subject**: FSD-1 & Python-1 (Semester 3)
**Project Type**: Case 3 (Combined Project)
**Marks**: 50% + 10% bonus (each subject)
**Total Bonus**: 20% (10% FSD + 10% Python)

---

## 👥 Team Members

- [Your Name] - [Roll Number]
- [Team Member 2] - [Roll Number]
- [Team Member 3] - [Roll Number]

---

## 📝 License

This project is created for academic purposes as part of Semester 3 coursework.

---

## 🙏 Acknowledgments

- Faculty members for guidance
- Firebase for cloud database
- Unsplash for images
- Tailwind CSS for UI framework
- Flask community for documentation

---

## 📞 Contact

For any queries regarding this project:
- Email: [your-email@example.com]
- GitHub: [your-github-username]

---

**Made with ❤️ for Semester 3 Project**

*Last Updated: February 2026*
