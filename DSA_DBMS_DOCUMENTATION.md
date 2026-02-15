# Data Structures & DBMS Documentation

## 📚 First Year Concepts Integration

This document covers Data Structures and DBMS concepts implemented in RentIt project.

---

## 🧮 DATA STRUCTURES & ALGORITHMS

### 1. Sorting Algorithm - Bubble Sort

#### Implementation:
```python
def sort_listings_by_price(listings, ascending=True):
    n = len(listings)
    sorted_list = listings.copy()
    
    for i in range(n):
        for j in range(0, n-i-1):
            price_a = int(str(sorted_list[j]['price'])
                         .replace('₹', '')
                         .replace(',', '')
                         .replace('k', '000')
                         .split('/')[0])
            price_b = int(str(sorted_list[j+1]['price'])
                         .replace('₹', '')
                         .replace(',', '')
                         .replace('k', '000')
                         .split('/')[0])
            
            if ascending:
                if price_a > price_b:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
            else:
                if price_a < price_b:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    
    return sorted_list
```

#### Algorithm Explanation:

**Bubble Sort** is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they're in wrong order.

**Time Complexity**:
- Best Case: O(n) - when already sorted
- Average Case: O(n²)
- Worst Case: O(n²) - when reverse sorted

**Space Complexity**: O(1) - sorts in place

**Why Bubble Sort?**
- Simple to understand and implement
- Good for small datasets
- Demonstrates DSA concepts clearly
- Shows manual algorithm implementation

#### Step-by-Step Process:
```
Initial: [₹2500, ₹800, ₹1200]

Pass 1:
  Compare 2500 & 800  → Swap → [₹800, ₹2500, ₹1200]
  Compare 2500 & 1200 → Swap → [₹800, ₹1200, ₹2500]

Pass 2:
  Compare 800 & 1200  → No swap → [₹800, ₹1200, ₹2500]
  
Result: [₹800, ₹1200, ₹2500] ✓
```

### 2. Searching Algorithm - Linear Search

#### Implementation:
```python
def search_products_linear(listings, query):
    results = []
    query = query.lower()
    
    for item in listings:
        if query in item['title'].lower() or \
           (item.get('tag') and query in item['tag'].lower()):
            results.append(item)
    
    return results
```

#### Algorithm Explanation:
**Linear Search** checks each element sequentially until finding the target or reaching the end.

**Time Complexity**:
- Best Case: O(1) - found at first position
- Average Case: O(n/2)
- Worst Case: O(n) - found at last position or not found

**Space Complexity**: O(k) - where k is number of matches

**Why Linear Search?**
- Simple and straightforward
- Works on unsorted data
- Good for small datasets
- No preprocessing required

### 3. Array/List Operations

#### Dynamic Arrays (Python Lists):
```python
# Append - O(1) amortized
cart.append(item)

# Remove - O(n)
cart.remove(item)

# Access - O(1)
item = listings[0]

# Search - O(n)
found = item in listings

# Slice - O(k)
first_three = listings[:3]
```

### 4. Hash Tables (Python Dictionaries)

#### Dictionary Operations:
```python
# Insert/Update - O(1) average
mock_listings['products'] = [...]

# Access - O(1) average
products = mock_listings.get('products', [])

# Delete - O(1) average
del mock_listings['products']

# Check existence - O(1) average
if 'products' in mock_listings:
    pass
```

**Why Dictionaries?**
- Fast lookups (O(1))
- Key-value mapping
- Perfect for JSON-like data
- Efficient for category organization

---

## 🗄️ DATABASE MANAGEMENT SYSTEM (DBMS)

### 1. Database Choice - Firebase Firestore

#### NoSQL vs SQL:

| Feature | SQL (MySQL) | NoSQL (Firebase) |
|---------|-------------|------------------|
| Structure | Tables, Rows | Collections, Documents |
| Schema | Fixed | Flexible |
| Scaling | Vertical | Horizontal |
| Queries | Complex SQL | Simple queries |
| Relationships | Foreign Keys | Denormalized |

**Why Firebase Firestore?**
- **Cloud-based**: No server setup needed
- **Real-time**: Live data synchronization
- **Scalable**: Handles growth automatically
- **Free tier**: Good for projects
- **Easy integration**: Simple Python SDK
- **Authentication**: Built-in user management

### 2. Database Schema Design

#### Collections Structure:
```
Firebase Database
├── products/
│   ├── doc_id_1
│   │   ├── title: "Canon EOS R5"
│   │   ├── price: "₹2,500"
│   │   ├── rating: "4.9"
│   │   ├── img: "https://..."
│   │   ├── unit: "/day"
│   │   └── tag: "Hot"
│   └── doc_id_2
│       └── ...
├── services/
│   └── ...
└── spaces/
    └── ...
```

#### Document Structure:
```json
{
  "title": "Canon EOS R5",
  "price": "₹2,500",
  "rating": "4.9",
  "img": "https://images.unsplash.com/...",
  "unit": "/day",
  "tag": "Hot"
}
```

### 3. CRUD Operations

#### CREATE (Insert):
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

#### READ (Select):
```python
# Get all documents
docs = db.collection('products').stream()
for doc in docs:
    print(doc.to_dict())

# Get single document
doc = db.collection('products').document('product_1').get()
if doc.exists:
    data = doc.to_dict()

# Query with filter
docs = db.collection('products').where('price', '>', 1000).stream()
```

#### UPDATE (Modify):
```python
# Update specific fields
db.collection('products').document('product_1').update({
    'price': '₹3,000',
    'rating': '5.0'
})

# Update or create (upsert)
db.collection('products').document('product_1').set({
    'price': '₹3,000'
}, merge=True)
```

#### DELETE (Remove):
```python
# Delete document
db.collection('products').document('product_1').delete()

# Delete all documents in collection
docs = db.collection('products').stream()
for doc in docs:
    doc.reference.delete()
```

### 4. Database Normalization

#### Current Design (Denormalized):
```
products/
  - All product data in one document
  - No separate user table
  - No separate category table
```

**Why Denormalized?**
- Faster reads (no joins needed)
- Simpler queries
- Better for NoSQL databases
- Suitable for read-heavy applications

#### Future Normalized Design:
```
users/
  - user_id, name, email, phone

listings/
  - listing_id, user_id, category_id, title, price

categories/
  - category_id, name, description

bookings/
  - booking_id, listing_id, user_id, dates
```

### 5. Data Integrity

#### Constraints (Future Implementation):
- **Primary Key**: Unique document IDs
- **Foreign Key**: User ID references
- **Not Null**: Required fields validation
- **Check**: Price > 0, Rating 0-5
- **Unique**: Email addresses

#### Validation:
```python
def validate_listing(data):
    if not data.get('title'):
        raise ValueError("Title is required")
    
    if not data.get('price'):
        raise ValueError("Price is required")
    
    price = int(data['price'].replace('₹', '').replace(',', ''))
    if price <= 0:
        raise ValueError("Price must be positive")
    
    return True
```

### 6. Database Transactions

#### Atomic Operations:
```python
# Transaction example (future)
transaction = db.transaction()

@firestore.transactional
def update_booking(transaction, listing_ref, user_ref):
    # Read
    listing = listing_ref.get(transaction=transaction)
    
    # Validate
    if not listing.get('available'):
        raise Exception("Not available")
    
    # Write
    transaction.update(listing_ref, {'available': False})
    transaction.set(user_ref, {'booking': listing.id})
```

### 7. Indexing

**Firebase Auto-Indexing**:
- Automatically indexes all fields
- Fast queries on any field
- No manual index creation needed

**Composite Indexes** (for complex queries):
```python
# Query requiring composite index
db.collection('products') \
  .where('category', '==', 'electronics') \
  .where('price', '<', 5000) \
  .order_by('rating', 'desc')
```

---

## 🎯 DSA & DBMS Integration

### How They Work Together:

```
User Request: "Sort products by price"
        ↓
Backend receives request
        ↓
Fetch data from Firebase (DBMS)
        ↓
Apply Bubble Sort (DSA)
        ↓
Return sorted data
        ↓
Display to user
```

### Example Flow:
```python
@app.route('/api/listings', methods=['GET'])
def get_listings():
    # DBMS: Fetch from database
    data = fetch_from_firebase('products')
    
    # DSA: Apply sorting algorithm
    if request.args.get('sort'):
        data = sort_listings_by_price(data)
    
    # Return processed data
    return jsonify(data)
```

---

## 🎤 Viva Questions & Answers

### DSA Questions:

**Q1: Why did you use Bubble Sort instead of built-in sort()?**
A: To demonstrate DSA concepts from first year. Shows understanding of algorithm implementation, not just using library functions.

**Q2: What is the time complexity of your sorting algorithm?**
A: O(n²) in worst and average case, O(n) in best case when already sorted.

**Q3: Can you explain how Linear Search works?**
A: It checks each element sequentially. Starts from first element, compares with target, continues until found or end reached.

**Q4: What other sorting algorithms could you use?**
A: Quick Sort (O(n log n)), Merge Sort (O(n log n)), Insertion Sort (O(n²)), Selection Sort (O(n²)).

**Q5: What is the difference between array and linked list?**
A: Array has contiguous memory, O(1) access. Linked list has scattered memory, O(n) access but O(1) insertion/deletion.

### DBMS Questions:

**Q1: Why Firebase instead of MySQL?**
A: Firebase is cloud-based, no server setup, real-time sync, easy integration, free tier, and perfect for modern web apps.

**Q2: What is the difference between SQL and NoSQL?**
A: SQL has fixed schema, tables, complex queries. NoSQL has flexible schema, documents/collections, simple queries, better scalability.

**Q3: Explain CRUD operations.**
A: Create (INSERT), Read (SELECT), Update (MODIFY), Delete (REMOVE) - basic database operations.

**Q4: What is database normalization?**
A: Process of organizing data to reduce redundancy. Divides large tables into smaller ones with relationships.

**Q5: What are Firebase collections and documents?**
A: Collections are like tables, documents are like rows. Each document is a JSON object with key-value pairs.

**Q6: How do you ensure data integrity?**
A: Validation, constraints, transactions, error handling, and Firebase security rules.

**Q7: What is indexing and why is it important?**
A: Indexing creates data structure for fast lookups. Like book index - find information quickly without reading everything.

---

## 📊 Concepts Checklist

### ✅ Data Structures:
- [x] Arrays/Lists
- [x] Dictionaries/Hash Tables
- [x] Sorting (Bubble Sort)
- [x] Searching (Linear Search)
- [x] Time Complexity Analysis
- [x] Space Complexity Analysis

### ✅ DBMS:
- [x] Database design
- [x] Collections/Tables
- [x] CRUD operations
- [x] NoSQL concepts
- [x] Data modeling
- [x] Query operations
- [x] Data integrity
- [x] Cloud database

---

**Last Updated**: February 2026
**Subjects**: Data Structures & DBMS (First Year)
**Integration**: Case 3 Bonus Marks
