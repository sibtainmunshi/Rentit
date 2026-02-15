# Python-1 Technical Documentation

## 📚 Subject Coverage: Python-1

This document covers all Python programming concepts implemented in the RentIt project.

---

## 🐍 Python Fundamentals

### 1. Python Basics Used

#### Variables & Data Types
```python
# String
app_name = "RentIt"

# Dictionary
mock_listings = {
    "products": [...],
    "services": [...],
    "spaces": [...]
}

# List
items = [item1, item2, item3]

# Boolean
is_ascending = True

# Integer
price = 2500
```

#### Data Structures
- **Lists**: Dynamic arrays for storing listings
- **Dictionaries**: Key-value pairs for structured data
- **Tuples**: Immutable sequences (if needed)
- **Sets**: Unique collections (for future features)

---

## 🌐 Flask Web Framework

### 1. Flask Application Setup

```python
from flask import Flask, render_template, jsonify, request

# Create Flask application instance
app = Flask(__name__)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

#### Key Flask Concepts:

**Application Instance**:
```python
app = Flask(__name__)
```
- `__name__` helps Flask locate resources
- Creates the application object

**Debug Mode**:
```python
app.run(debug=True)
```
- Auto-reloads on code changes
- Shows detailed error messages
- Should be False in production

### 2. Routing & Decorators

#### Route Decorator:
```python
@app.route('/')
def home():
    return render_template('index.html')
```

**Explanation**:
- `@app.route()` is a decorator
- Maps URL path to Python function
- Function name can be anything
- Return value is sent to browser

#### Multiple HTTP Methods:
```python
@app.route('/api/listings', methods=['GET'])
def get_listings():
    # Handle GET request
    return jsonify(data)
```

**HTTP Methods**:
- **GET**: Retrieve data (default)
- **POST**: Send data to server
- **PUT**: Update existing data
- **DELETE**: Remove data

### 3. Request Handling

#### Query Parameters:
```python
category = request.args.get('category', 'products')
sort_order = request.args.get('sort')
```

**Explanation**:
- `request.args` contains URL parameters
- `.get()` method with default value
- Example: `/api/listings?category=products&sort=asc`

#### Request Object:
```python
from flask import request

# Get query parameters
request.args.get('key')

# Get form data (POST)
request.form.get('key')

# Get JSON data
request.json

# Get headers
request.headers.get('Authorization')
```

### 4. Response Handling

#### JSON Response:
```python
from flask import jsonify

@app.route('/api/listings')
def get_listings():
    data = {"products": [...]}
    return jsonify(data)
```

**Why jsonify()?**
- Converts Python dict to JSON
- Sets correct Content-Type header
- Handles serialization automatically

#### Template Rendering:
```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')
```

**Template Engine**: Jinja2
- Looks in `templates/` folder
- Can pass variables to template
- Supports template inheritance

---

## 🔥 Firebase Integration

### 1. Firebase Admin SDK

#### Installation:
```bash
pip install firebase-admin
```

#### Initialization:
```python
import firebase_admin
from firebase_admin import credentials, firestore

# Load service account credentials
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize Firebase app
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
```

### 2. Firestore Operations

#### Create/Add Data:
```python
# Add document with auto-generated ID
db.collection('products').add({
    'title': 'Canon EOS R5',
    'price': '₹2,500',
    'rating': '4.9'
})

# Add document with custom ID
db.collection('products').document('product_1').set({
    'title': 'Canon EOS R5'
})
```

#### Read Data:
```python
# Get all documents in collection
docs = db.collection('products').stream()
for doc in docs:
    print(doc.id, doc.to_dict())

# Get single document
doc = db.collection('products').document('product_1').get()
if doc.exists:
    print(doc.to_dict())
```

#### Update Data:
```python
# Update specific fields
db.collection('products').document('product_1').update({
    'price': '₹3,000'
})
```

#### Delete Data:
```python
# Delete document
db.collection('products').document('product_1').delete()

# Delete all documents in collection
docs = db.collection('products').stream()
for doc in docs:
    doc.reference.delete()
```

### 3. Database Seeding Script

```python
def seed_data():
    # Check if credentials file exists
    if not os.path.exists("serviceAccountKey.json"):
        print("❌ Error: serviceAccountKey.json not found!")
        return

    # Initialize Firebase
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    
    print("✅ Firebase Connected! Uploading data...")

    # Loop through categories
    for category, items in data_to_upload.items():
        print(f"📂 Uploading category: {category}...")
        col_ref = db.collection(category)
        
        # Clear existing data
        docs = col_ref.stream()
        for doc in docs:
            doc.reference.delete()
            
        # Add new data
        for item in items:
            col_ref.add(item)
            print(f"   -> Added: {item['title']}")
    
    print("\n🎉 Success! All data uploaded to Firebase.")
```

---

## 🔄 Python Modules & Imports

### 1. Import Statements

```python
# Standard library imports
import os

# Third-party imports
from flask import Flask, render_template, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore

# Local imports
from utils.dsa_logic import sort_listings_by_price, search_products_linear
```

### 2. Module Organization

**Why separate files?**
- **Modularity**: Easier to maintain
- **Reusability**: Use functions in multiple places
- **Organization**: Clean project structure
- **Testing**: Test individual modules

**Project Modules**:
- `app.py`: Main application
- `seed_database.py`: Database setup
- `utils/dsa_logic.py`: Custom algorithms

---

## 🧮 Data Processing

### 1. List Operations

```python
# List comprehension
prices = [item['price'] for item in listings]

# Filtering
expensive_items = [item for item in listings if item['price'] > 1000]

# Mapping
titles = list(map(lambda x: x['title'], listings))

# Sorting
sorted_items = sorted(listings, key=lambda x: x['price'])
```

### 2. Dictionary Operations

```python
# Access value
price = product['price']

# Get with default
rating = product.get('rating', '0.0')

# Check key existence
if 'tag' in product:
    print(product['tag'])

# Iterate over items
for key, value in product.items():
    print(f"{key}: {value}")
```

### 3. String Manipulation

```python
# String formatting
message = f"Product: {title}, Price: {price}"

# String methods
price_str = "₹2,500"
price_int = int(price_str.replace('₹', '').replace(',', ''))

# String splitting
price, unit = "₹2,500/day".split('/')
```

---

## 🔧 Functions & Control Flow

### 1. Function Definition

```python
def sort_listings_by_price(listings, ascending=True):
    """
    Sorts listings by price using Bubble Sort.
    
    Args:
        listings (list): List of product dictionaries
        ascending (bool): Sort order (default: True)
    
    Returns:
        list: Sorted list of products
    """
    n = len(listings)
    sorted_list = listings.copy()
    
    # Bubble sort implementation
    for i in range(n):
        for j in range(0, n-i-1):
            # Comparison logic
            if ascending:
                if sorted_list[j]['price'] > sorted_list[j+1]['price']:
                    # Swap
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    
    return sorted_list
```

**Function Components**:
- **Docstring**: Function documentation
- **Parameters**: Input values
- **Default Arguments**: `ascending=True`
- **Return Statement**: Output value

### 2. Control Flow

#### If-Else Statements:
```python
if sort_order:
    is_asc = True if sort_order == 'asc' else False
    data = sort_listings_by_price(data, ascending=is_asc)
```

#### For Loops:
```python
for category, items in data_to_upload.items():
    for item in items:
        col_ref.add(item)
```

#### While Loops:
```python
i = 0
while i < len(listings):
    print(listings[i])
    i += 1
```

### 3. Error Handling

```python
try:
    # Initialize Firebase
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
except FileNotFoundError:
    print("❌ Error: Credentials file not found!")
except Exception as e:
    print(f"❌ Error: {str(e)}")
```

---

## 📦 Python Packages & Dependencies

### requirements.txt
```
flask
firebase-admin
```

### Installation:
```bash
pip install -r requirements.txt
```

### Package Purposes:
- **flask**: Web framework for backend
- **firebase-admin**: Firebase SDK for database operations

---

## 🎯 Python Best Practices Used

### 1. Code Organization
- Modular structure with separate files
- Clear function names
- Proper imports

### 2. Naming Conventions
- **snake_case** for functions and variables
- **UPPER_CASE** for constants
- Descriptive names

### 3. Documentation
- Docstrings for functions
- Comments for complex logic
- README files

### 4. Error Handling
- Try-except blocks
- Meaningful error messages
- Graceful failures

---

## 🎤 Viva Questions & Answers

### Q1: What is Flask and why did you use it?
**A**: Flask is a lightweight Python web framework. I used it because it's simple, flexible, and perfect for building RESTful APIs. It has minimal boilerplate code compared to Django.

### Q2: Explain the difference between @app.route and app.run().
**A**: `@app.route()` is a decorator that maps URLs to functions. `app.run()` starts the development server and makes the application accessible.

### Q3: What is the purpose of jsonify()?
**A**: `jsonify()` converts Python dictionaries to JSON format and sets the correct Content-Type header (application/json) for API responses.

### Q4: How does Firebase Admin SDK work?
**A**: It's a Python library that connects to Firebase services. We initialize it with service account credentials, then use it to perform database operations like add, read, update, delete.

### Q5: What is the difference between .get() and direct dictionary access?
**A**: `.get()` returns None (or default value) if key doesn't exist. Direct access `dict['key']` raises KeyError if key is missing.

### Q6: Explain list comprehension with an example.
**A**: List comprehension is a concise way to create lists. Example: `[x*2 for x in range(5)]` creates `[0, 2, 4, 6, 8]`.

### Q7: What is the purpose of if __name__ == '__main__'?
**A**: It ensures code only runs when the file is executed directly, not when imported as a module. Useful for testing and running scripts.

### Q8: How do you handle errors in Python?
**A**: Using try-except blocks. Code that might fail goes in `try`, error handling goes in `except`. Can catch specific exceptions or general Exception.

### Q9: What is the difference between list and tuple?
**A**: Lists are mutable (can be changed), tuples are immutable (cannot be changed). Lists use `[]`, tuples use `()`.

### Q10: Explain the seed_database.py script.
**A**: It's a utility script that populates Firebase with initial data. It connects to Firebase, clears old data, and uploads new product/service/space listings.

---

## 📊 Python Concepts Checklist

### ✅ Covered Topics:

- [x] Variables and data types
- [x] Lists, dictionaries, tuples
- [x] Functions and parameters
- [x] Control flow (if-else, loops)
- [x] String manipulation
- [x] List comprehension
- [x] Error handling (try-except)
- [x] Modules and imports
- [x] Flask web framework
- [x] Routing and decorators
- [x] Request/Response handling
- [x] JSON processing
- [x] Firebase integration
- [x] Database operations (CRUD)
- [x] File operations
- [x] Lambda functions
- [x] Default arguments
- [x] Docstrings

---

## 🔍 Code Examples

### Example 1: Flask Route with Query Parameters
```python
@app.route('/api/listings', methods=['GET'])
def get_listings():
    # Get query parameters
    category = request.args.get('category', 'products')
    sort_order = request.args.get('sort')
    
    # Get data for category
    data = mock_listings.get(category, [])
    
    # Apply sorting if requested
    if sort_order:
        is_asc = True if sort_order == 'asc' else False
        data = sort_listings_by_price(data, ascending=is_asc)
    
    # Return JSON response
    return jsonify(data)
```

### Example 2: Firebase Data Upload
```python
def upload_to_firebase(category, items):
    db = firestore.client()
    col_ref = db.collection(category)
    
    for item in items:
        col_ref.add(item)
        print(f"Added: {item['title']}")
```

### Example 3: Custom Sorting Function
```python
def sort_listings_by_price(listings, ascending=True):
    n = len(listings)
    sorted_list = listings.copy()
    
    for i in range(n):
        for j in range(0, n-i-1):
            price_a = extract_price(sorted_list[j]['price'])
            price_b = extract_price(sorted_list[j+1]['price'])
            
            if ascending:
                if price_a > price_b:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
            else:
                if price_a < price_b:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    
    return sorted_list
```

---

**Last Updated**: February 2026
**Subject**: Python-1
**Marks Weightage**: 50% + 10% (Case 3 bonus)
