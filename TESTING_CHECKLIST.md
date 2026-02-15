# 🧪 RentIt - Testing Checklist

## Quick Testing Guide for Professional Booking System

---

## ✅ Pre-Testing Setup

### 1. Start the Application
```bash
python app.py
```
Server should start at: `http://127.0.0.1:5000`

### 2. Firebase Setup (Optional)
- If you have `serviceAccountKey.json`, Firebase will connect automatically
- If not, the app will use mock data (still fully functional)

---

## 🔐 Authentication Testing

### Test 1: Google Sign-In
1. Click "Sign In" button in navbar
2. Click "Continue with Google"
3. **Expected**: Google popup appears (or error if domain not authorized)
4. **Note**: If you see "unauthorized domain" error, follow `FIREBASE_DOMAIN_FIX.md`

### Test 2: Email/Password Signup
1. Click "Sign In" → "Sign Up"
2. Fill in:
   - Name: Test User
   - Email: test@example.com
   - Password: test123
3. Check "I agree to terms"
4. Click "Create Account"
5. **Expected**: Success message, user name appears in navbar

### Test 3: Email/Password Login
1. Click "Sign In"
2. Enter email and password
3. Click "Sign In"
4. **Expected**: Welcome message, user logged in

### Test 4: User Menu
1. After login, click on your name in navbar
2. **Expected**: Dropdown menu with Profile, Bookings, Settings, Logout

### Test 5: Logout
1. Click your name → Logout
2. **Expected**: Redirected to home, "Sign In" button appears

---

## 🎫 Booking Flow Testing

### Test 6: Rent Now (Not Logged In)
1. Browse products
2. Click on any product card
3. Click "Rent Now" button
4. **Expected**: Login modal appears with message "Please login to continue"

### Test 7: Complete Booking Flow
1. **Login first** (use Test 2 or 3)
2. Browse products and click on any item
3. Click "Rent Now"
4. **Expected**: Redirected to `/booking` page

### Test 8: Booking Page
1. On booking page, verify:
   - ✅ Item details shown in right sidebar
   - ✅ Start date picker (min date = today)
   - ✅ End date picker
   - ✅ Contact form (name, email, phone)
   - ✅ Address form (street, city, state, PIN)
   - ✅ Special instructions textarea
   - ✅ Price breakdown visible
   - ✅ Terms checkbox

### Test 9: Price Calculation
1. Select start date: Today
2. Select end date: 3 days from today
3. **Expected**: 
   - Duration shows "3 days"
   - Rental price = base price × 3
   - Total = rental + ₹99 (service) + ₹500 (deposit)

### Test 10: Form Validation
1. Try submitting without filling fields
2. **Expected**: Browser validation errors
3. Try invalid email format
4. **Expected**: Email validation error
5. Try PIN code with letters
6. **Expected**: Only numbers allowed

### Test 11: Complete Booking
1. Fill all required fields:
   - Start date: Today
   - End date: Tomorrow
   - Name: John Doe
   - Email: john@example.com
   - Phone: +91 9876543210
   - Address: 123 Main St
   - City: Mumbai
   - State: Maharashtra
   - PIN: 400001
2. Check "I agree to terms"
3. Click "Confirm & Pay"
4. **Expected**: Redirected to confirmation page

### Test 12: Booking Confirmation
1. On confirmation page, verify:
   - ✅ Success animation (bouncing checkmark)
   - ✅ Booking ID displayed (BK + timestamp)
   - ✅ Status: Confirmed
   - ✅ Item details with image
   - ✅ Rental period dates
   - ✅ Delivery address
   - ✅ Contact phone
   - ✅ Special instructions (if entered)
   - ✅ "Back to Home" button
   - ✅ "Print Receipt" button

### Test 13: Print Receipt
1. Click "Print Receipt"
2. **Expected**: Browser print dialog opens

### Test 14: Booking Storage
1. Open browser DevTools (F12)
2. Go to Application → Local Storage
3. Look for `rentit_bookings`
4. **Expected**: Array with your booking data

---

## 🛒 Cart & Wishlist Testing

### Test 15: Add to Cart
1. Click on any product
2. Click "Add to Cart"
3. **Expected**: Cart sidebar opens, item added, badge shows "1"

### Test 16: Checkout from Cart
1. Add items to cart
2. Click cart icon
3. Click "Checkout"
4. **Expected**: 
   - If not logged in: Login modal
   - If logged in: Redirected to booking page

### Test 17: Wishlist
1. Hover over product card
2. Click heart icon
3. **Expected**: Added to wishlist, badge shows count
4. Click wishlist icon in navbar
5. **Expected**: Sidebar shows wishlist items

---

## 🔍 Category & Filter Testing

### Test 18: Category Switching
1. Click "Products" tab
2. **Expected**: Products displayed
3. Click "Services" tab
4. **Expected**: Services displayed
5. Click "Spaces" tab
6. **Expected**: Spaces displayed

### Test 19: Subcategory Filtering
1. In Products, click "Cameras" chip
2. **Expected**: Only camera-related items shown
3. Click "All" chip
4. **Expected**: All products shown

### Test 20: Price Sorting
1. Select "Price: Low to High"
2. **Expected**: Items sorted by ascending price
3. Select "Price: High to Low"
4. **Expected**: Items sorted by descending price

---

## 📱 Responsive Testing

### Test 21: Mobile View
1. Open DevTools (F12)
2. Toggle device toolbar (Ctrl+Shift+M)
3. Select iPhone or Android device
4. **Expected**: 
   - Single column layout
   - Hamburger menu (if implemented)
   - Touch-friendly buttons
   - Sidebars full width

### Test 22: Tablet View
1. Select iPad in device toolbar
2. **Expected**: 2-column grid, proper spacing

### Test 23: Desktop View
1. Maximize browser window
2. **Expected**: 4-column grid, all features visible

---

## 🐛 Error Handling Testing

### Test 24: Network Error
1. Stop Flask server
2. Try switching categories
3. **Expected**: Error toast message

### Test 25: Invalid Booking Data
1. Try booking without authentication
2. **Expected**: Redirected to login

### Test 26: Firebase Errors
1. If Firebase not configured
2. **Expected**: Mock authentication works, toast shows "Mock login"

---

## ✅ Success Criteria

### All Tests Should Pass:
- ✅ Authentication works (Google or Email)
- ✅ User session persists
- ✅ Booking flow requires login
- ✅ Booking page loads with item data
- ✅ Form validation works
- ✅ Price calculation is dynamic
- ✅ Booking confirmation shows all details
- ✅ Data stored in localStorage
- ✅ Cart and wishlist functional
- ✅ Categories and filters work
- ✅ Responsive on all devices
- ✅ Error handling graceful

---

## 🚨 Common Issues & Solutions

### Issue 1: "Unauthorized domain" error
**Solution**: Follow `FIREBASE_DOMAIN_FIX.md` to add 127.0.0.1 to authorized domains

### Issue 2: Booking page shows "Booking not found"
**Solution**: Make sure you clicked "Rent Now" from a product, not direct URL

### Issue 3: User not staying logged in
**Solution**: Check localStorage in DevTools, should have `rentit_user` key

### Issue 4: Firebase not connecting
**Solution**: Check `serviceAccountKey.json` exists, or use mock mode

### Issue 5: Dates not selectable
**Solution**: Make sure browser supports HTML5 date input

---

## 📊 Test Results Template

```
Date: _______________
Tester: _______________

Authentication Tests: ☐ Pass ☐ Fail
Booking Flow Tests: ☐ Pass ☐ Fail
Cart/Wishlist Tests: ☐ Pass ☐ Fail
Category/Filter Tests: ☐ Pass ☐ Fail
Responsive Tests: ☐ Pass ☐ Fail
Error Handling Tests: ☐ Pass ☐ Fail

Notes:
_________________________________
_________________________________
_________________________________
```

---

## 🎯 Demo Preparation

### Before Faculty Demo:
1. ✅ Test all authentication flows
2. ✅ Complete at least one booking
3. ✅ Verify Firebase console shows data
4. ✅ Test on mobile device
5. ✅ Prepare to explain DSA algorithms
6. ✅ Have booking confirmation ready to show
7. ✅ Know your Firebase project ID
8. ✅ Be ready to show code structure

### Demo Flow Suggestion:
1. Show homepage and categories (30 sec)
2. Demonstrate authentication (1 min)
3. Browse and select product (30 sec)
4. Complete booking flow (2 min)
5. Show confirmation page (30 sec)
6. Show Firebase console (1 min)
7. Explain DSA algorithms (1 min)
8. Show code structure (1 min)
9. Answer questions (2 min)

**Total: ~10 minutes**

---

**Last Updated**: February 15, 2026
**Version**: 3.0
**Status**: Ready for Testing ✅
