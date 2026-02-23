# 🚀 Flask Code - Quick Reference Card

## 📝 2 Routes Summary

---

## ROUTE 1: Display Page

```python
@app.route('/complaint')
def complaint():
    return render_template('complaint.html')
```

### Ek Line Mein:
"Jab user `/complaint` pe jaye, to `complaint.html` file dikha do"

### Parts:
- `@app.route('/complaint')` → URL mapping
- `def complaint():` → Function
- `render_template()` → HTML file bhejo

---

## ROUTE 2: Save Data

```python
@app.route('/api/submit-complaint', methods=['POST'])
def submit_complaint():
    data = request.get_json()              # Data receive
    # Validation
    data['timestamp'] = datetime.now()     # Timestamp add
    db.collection('complaints').add(data)  # Firebase save
    return jsonify({"success": True})      # Response
```

### Ek Line Mein:
"POST request se data lo, validate karo, Firebase mein save karo, success bhejo"

### Parts:
- `methods=['POST']` → POST request only
- `request.get_json()` → Data receive
- Validation → Check required fields
- `db.collection().add()` → Firebase save
- `jsonify()` → JSON response

---

## 🎯 Important Functions

| Function | Kya Karta Hai |
|----------|---------------|
| `@app.route()` | URL ko function se connect |
| `render_template()` | HTML file bhejo |
| `request.get_json()` | JSON data receive |
| `jsonify()` | Python dict → JSON |
| `db.collection().add()` | Firebase mein save |

---

## 📊 Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 500 | Server Error |

---

## 🎤 Sir Ko Bolne Ke Liye

**Route 1**:
"Sir, yeh route complaint page ko display karta hai. `render_template()` se HTML file bhejta hai."

**Route 2**:
"Sir, yeh route form data receive karta hai, validate karta hai, Firebase mein save karta hai, aur success response bhejta hai."

---

**Print karke pocket mein rakh lo! 📄**
