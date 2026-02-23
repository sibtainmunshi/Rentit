# 🚀 Render Deployment Guide - RentIt App

## Step 1: Push Code to GitHub

```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

## Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub (recommended)

## Step 3: Create New Web Service

1. Click "New +" button on dashboard
2. Select "Web Service"
3. Connect your GitHub repository
4. Select your `rentit` repository

## Step 4: Configure Service

Fill in these settings:

- **Name**: `rentit-app` (or any name you like)
- **Environment**: `Python 3`
- **Region**: Choose closest to India (Singapore recommended)
- **Branch**: `main`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Instance Type**: `Free`

## Step 5: Add Environment Variables

Click "Advanced" → "Add Environment Variable"

### Required Variables:

1. **PYTHON_VERSION**
   - Value: `3.9.0`

2. **FIREBASE_CREDENTIALS** (Important!)
   - Value: Copy the ENTIRE content from your `serviceAccountKey.json` file
   - Make sure it's valid JSON (one line, no extra spaces)
   - Example format:
   ```json
   {"type":"service_account","project_id":"rentit-8404c","private_key_id":"...","private_key":"-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n","client_email":"...","client_id":"...","auth_uri":"...","token_uri":"...","auth_provider_x509_cert_url":"...","client_x509_cert_url":"...","universe_domain":"googleapis.com"}
   ```

## Step 6: Deploy!

1. Click "Create Web Service"
2. Wait 2-5 minutes for deployment
3. Your app will be live at: `https://rentit-app.onrender.com`

## Step 7: Update Firebase Authorized Domains

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Select your project: `rentit-8404c`
3. Go to Authentication → Settings → Authorized domains
4. Add your Render URL: `rentit-app.onrender.com`

## Troubleshooting

### If deployment fails:

1. Check logs in Render dashboard
2. Verify `requirements.txt` has all dependencies
3. Make sure `FIREBASE_CREDENTIALS` is valid JSON

### If Firebase doesn't work:

1. Check environment variable is set correctly
2. Verify Firebase credentials are valid
3. Check Render logs for Firebase connection errors

### Free Tier Limitations:

- App sleeps after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds
- 750 hours/month free (enough for one app)

## Testing Your Deployment

Once deployed, test these URLs:

- Homepage: `https://your-app.onrender.com/`
- API: `https://your-app.onrender.com/api/listings?category=products`
- Health check: Check Render logs for "Firebase Connected Successfully!"

## Updating Your App

After making changes:

```bash
git add .
git commit -m "Update description"
git push origin main
```

Render will automatically redeploy! 🎉

## Custom Domain (Optional)

1. Buy a domain (Namecheap, GoDaddy, etc.)
2. In Render: Settings → Custom Domain
3. Add your domain and follow DNS instructions

---

**Need help?** Check Render docs: https://render.com/docs
