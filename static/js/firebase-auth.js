// Firebase Authentication Configuration
// Your Firebase project config

const firebaseConfig = {
    apiKey: "AIzaSyBm0Mp-nfrsmmBD1pG5DA9A72bmmhZCADA",
    authDomain: "rentit-8404c.firebaseapp.com",
    projectId: "rentit-8404c",
    storageBucket: "rentit-8404c.firebasestorage.app",
    messagingSenderId: "1048387184334",
    appId: "1:1048387184334:web:af76777e9dcabfbfde129f",
    measurementId: "G-BCCXKHC6F2"
};

// Initialize Firebase (only if not already initialized)
let auth;
try {
    if (!firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
    }
    auth = firebase.auth();
    console.log('✅ Firebase Auth initialized');
} catch (error) {
    console.warn('⚠️ Firebase not configured. Using mock authentication.');
    auth = null;
}

// Current user state
let currentUser = null;

// Auth state observer
if (auth) {
    auth.onAuthStateChanged((user) => {
        if (user) {
            currentUser = {
                uid: user.uid,
                email: user.email,
                name: user.displayName || user.email.split('@')[0],
                photoURL: user.photoURL,
                emailVerified: user.emailVerified,
                loggedIn: true  // Add this flag for consistency
            };
            
            // Store in localStorage for quick access
            localStorage.setItem('rentit_user', JSON.stringify(currentUser));
            updateUserUI(currentUser);
            
            console.log('✅ User logged in:', currentUser.email);
        } else {
            currentUser = null;
            localStorage.removeItem('rentit_user');
            console.log('👋 User logged out');
        }
    });
}

// Google Sign-In
async function handleGoogleLogin() {
    if (!auth) {
        showToast('Firebase not configured. Using mock login.');
        mockLogin('google@example.com', 'Google User');
        return;
    }

    try {
        const provider = new firebase.auth.GoogleAuthProvider();
        const result = await auth.signInWithPopup(provider);
        
        closeAuthModal();
        showToast(`Welcome ${result.user.displayName}! 👋`);
        
    } catch (error) {
        console.error('Google login error:', error);
        
        if (error.code === 'auth/popup-closed-by-user') {
            showToast('Sign-in cancelled');
        } else if (error.code === 'auth/popup-blocked') {
            showToast('Please allow popups for this site');
        } else {
            showToast('Login failed. Please try again.');
        }
    }
}

// Email/Password Login
async function handleEmailLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    
    if (!auth) {
        showToast('Firebase not configured. Using mock login.');
        mockLogin(email, email.split('@')[0]);
        return;
    }

    try {
        const result = await auth.signInWithEmailAndPassword(email, password);
        
        closeAuthModal();
        showToast('Welcome back! 👋');
        
    } catch (error) {
        console.error('Login error:', error);
        
        if (error.code === 'auth/user-not-found') {
            showToast('No account found with this email');
        } else if (error.code === 'auth/wrong-password') {
            showToast('Incorrect password');
        } else if (error.code === 'auth/invalid-email') {
            showToast('Invalid email address');
        } else if (error.code === 'auth/too-many-requests') {
            showToast('Too many attempts. Please try later.');
        } else {
            showToast('Login failed. Please try again.');
        }
    }
}

// Email/Password Signup
async function handleEmailSignup(event) {
    event.preventDefault();
    
    const name = document.getElementById('signup-name').value;
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;
    
    if (!auth) {
        showToast('Firebase not configured. Using mock signup.');
        mockLogin(email, name);
        return;
    }

    try {
        const result = await auth.createUserWithEmailAndPassword(email, password);
        
        // Update profile with name
        await result.user.updateProfile({
            displayName: name
        });
        
        closeAuthModal();
        showToast('Account created successfully! 🎉');
        
        // Optional: Send verification email
        // await result.user.sendEmailVerification();
        // showToast('Verification email sent!');
        
    } catch (error) {
        console.error('Signup error:', error);
        
        if (error.code === 'auth/email-already-in-use') {
            showToast('Email already registered. Please login.');
        } else if (error.code === 'auth/invalid-email') {
            showToast('Invalid email address');
        } else if (error.code === 'auth/weak-password') {
            showToast('Password should be at least 6 characters');
        } else {
            showToast('Signup failed. Please try again.');
        }
    }
}

// Logout
async function logout() {
    if (!auth) {
        localStorage.removeItem('rentit_user');
        location.reload();
        return;
    }

    try {
        await auth.signOut();
        showToast('Logged out successfully');
        location.reload();
    } catch (error) {
        console.error('Logout error:', error);
        showToast('Logout failed');
    }
}

// Password Reset
async function resetPassword(email) {
    if (!auth) {
        showToast('Firebase not configured');
        return;
    }

    try {
        await auth.sendPasswordResetEmail(email);
        showToast('Password reset email sent! Check your inbox.');
    } catch (error) {
        console.error('Password reset error:', error);
        
        if (error.code === 'auth/user-not-found') {
            showToast('No account found with this email');
        } else {
            showToast('Failed to send reset email');
        }
    }
}

// Mock login (fallback when Firebase not configured)
function mockLogin(email, name) {
    const user = {
        email: email,
        name: name,
        loggedIn: true,
        loginTime: new Date().toISOString(),
        mock: true
    };
    
    localStorage.setItem('rentit_user', JSON.stringify(user));
    closeAuthModal();
    updateUserUI(user);
    showToast('Welcome! (Mock login) 👋');
}

// Update UI based on user state
function updateUserUI(user) {
    console.log('🔄 Updating UI for user:', user);
    
    const signInBtn = document.querySelector('button[onclick="openLoginModal()"]');
    if (signInBtn && user) {
        signInBtn.innerHTML = `
            <div class="flex items-center gap-2">
                ${user.photoURL ? 
                    `<img src="${user.photoURL}" class="w-6 h-6 rounded-full" alt="${user.name}">` : 
                    `<i class="fa-solid fa-user-circle"></i>`
                }
                <span class="hidden sm:inline">${user.name}</span>
            </div>
        `;
        signInBtn.onclick = () => showUserMenu();
        
        console.log('✅ UI updated successfully');
    }
}

// User menu dropdown
function showUserMenu() {
    // Create dropdown menu
    const menu = document.createElement('div');
    menu.id = 'user-menu';
    menu.className = 'absolute top-16 right-4 bg-white rounded-xl shadow-2xl border border-gray-100 py-2 w-48 z-50 animate-fade-in';
    menu.innerHTML = `
        <div class="px-4 py-3 border-b border-gray-100">
            <p class="text-sm font-bold text-slate-900">${currentUser?.name || 'User'}</p>
            <p class="text-xs text-gray-500">${currentUser?.email || ''}</p>
        </div>
        <a href="/profile" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 transition">
            <i class="fa-solid fa-user mr-2"></i> My Profile
        </a>
        <a href="/my-listings" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 transition">
            <i class="fa-solid fa-list mr-2"></i> My Listings
        </a>
        <a href="/my-bookings" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 transition">
            <i class="fa-solid fa-box mr-2"></i> My Bookings
        </a>
        <a href="/settings" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50 transition">
            <i class="fa-solid fa-gear mr-2"></i> Settings
        </a>
        <div class="border-t border-gray-100 mt-2 pt-2">
            <button onclick="logout()" class="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 transition">
                <i class="fa-solid fa-right-from-bracket mr-2"></i> Logout
            </button>
        </div>
    `;
    
    // Remove existing menu if any
    const existingMenu = document.getElementById('user-menu');
    if (existingMenu) {
        existingMenu.remove();
        return;
    }
    
    document.body.appendChild(menu);
    
    // Close menu when clicking outside
    setTimeout(() => {
        document.addEventListener('click', function closeMenu(e) {
            if (!menu.contains(e.target)) {
                menu.remove();
                document.removeEventListener('click', closeMenu);
            }
        });
    }, 100);
}

// Check for existing session on page load
window.addEventListener('load', function() {
    const storedUser = JSON.parse(localStorage.getItem('rentit_user') || 'null');
    if (storedUser && storedUser.loggedIn && !auth) {
        // Mock user from localStorage
        currentUser = storedUser;
        updateUserUI(storedUser);
    }
});
