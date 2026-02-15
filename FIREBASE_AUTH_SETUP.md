# 🔥 Firebase Authentication Setup Guide

## Prerequisites
- Firebase project created (RentIt)
- Firebase Console access

---

## Step-by-Step Setup

### 1️⃣ Enable Authentication in Firebase Console

1. Go to https://console.firebase.google.com/
2. Select your **RentIt** project
3. Click **"Authentication"** in left sidebar
4. Click **"Get Started"** button

### 2️⃣ Enable Sign-in Methods

#### Email/Password:
1. Go to **"Sign-in method"** tab
2. Click on **"Email/Password"**
3. **Enable** the toggle
4. Click **"Save"**

#### Google Sign-In:
1. Click on **"Google"** in providers list
2. **Enable** the toggle
3. Select your **support email** from dropdown
4. Click **"Save"**

### 3️⃣ Get Firebase Configuration

1. Click **⚙️ (Settings icon)** → **Project Settings**
2. Scroll to **"Your apps"** section
3. If no web app:
   - Click **"Add app"** → **Web** (</> icon)
   - Nickname: **"RentIt Web"**
   - Check **"Also set up Firebase Hosting"** (optional)
   - Click **"Register app"**
4. Copy the **firebaseConfig** object

Example config:
```javascript
const firebaseConfig = {
  apiKey: "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "rentit-xxxxx.firebaseapp.com",
  projectId: "rentit-xxxxx",
  storageBucket: "rentit-xxxxx.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:xxxxxxxxxxxxx"
};
```

### 4️⃣ Update Your Code

Open `static/js/firebase-auth.js` and replace:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

With your actual Firebase config.

### 5️⃣ Test Authentication

1. Restart your Flask server:
   ```bash
   python app.py
   ```

2. Open browser: http://localhost:5000

3. Click **"Sign In"** button

4. Try:
   - **Google Sign-In** (popup will open)
   - **Email/Password Signup** (create new account)
   - **Email/Password Login** (login with created account)

---

## 🎯 Features Enabled

### ✅ What Works Now:

1. **Google Sign-In**
   - One-click authentication
   - Auto-fills user name and photo
   - Secure OAuth flow

2. **Email/Password Signup**
   - Create new accounts
   - Password validation (min 6 chars)
   - Display name support

3. **Email/Password Login**
   - Secure authentication
   - Remember me option
   - Error handling

4. **User Session**
   - Persistent login
   - Auto-login on page refresh
   - User info in navbar

5. **Logout**
   - Secure sign out
   - Clear session data

### 🔒 Security Features:

- Firebase handles all security
- Passwords encrypted
- Secure token-based auth
- HTTPS required in production
- Rate limiting built-in

---

## 🚨 Common Issues & Solutions

### Issue 1: "Firebase not configured"
**Solution**: Update firebaseConfig in `static/js/firebase-auth.js`

### Issue 2: Google Sign-In popup blocked
**Solution**: Allow popups in browser settings

### Issue 3: "auth/popup-closed-by-user"
**Solution**: User closed popup, try again

### Issue 4: "auth/email-already-in-use"
**Solution**: Email already registered, use login instead

### Issue 5: "auth/weak-password"
**Solution**: Use password with at least 6 characters

---

## 🎨 Mock Authentication (Fallback)

If Firebase is not configured, the app automatically uses **mock authentication**:

- Stores user in localStorage
- Works offline
- Perfect for development/demo
- No Firebase required

To use mock auth:
- Just don't configure Firebase
- Or set `auth = null` in firebase-auth.js

---

## 📱 Testing Checklist

- [ ] Firebase Authentication enabled in console
- [ ] Email/Password provider enabled
- [ ] Google provider enabled
- [ ] Firebase config updated in code
- [ ] Server restarted
- [ ] Google Sign-In works
- [ ] Email Signup works
- [ ] Email Login works
- [ ] User name shows in navbar
- [ ] Logout works
- [ ] Session persists on refresh

---

## 🔜 Optional Enhancements

### Email Verification:
```javascript
await user.sendEmailVerification();
```

### Password Reset:
```javascript
await auth.sendPasswordResetEmail(email);
```

### Phone Authentication:
Enable in Firebase Console → Add phone provider

### Social Logins:
- Facebook
- Twitter
- GitHub
- Apple

---

## 📚 Resources

- [Firebase Auth Docs](https://firebase.google.com/docs/auth)
- [Firebase Console](https://console.firebase.google.com/)
- [Firebase Auth Web Guide](https://firebase.google.com/docs/auth/web/start)

---

**Last Updated**: February 2026
**Status**: Ready for Setup ✅
