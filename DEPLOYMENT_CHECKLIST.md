# ✅ Render Deployment Checklist

## Before Deployment

- [ ] Code tested locally (`python app.py`)
- [ ] All files committed to Git
- [ ] `.gitignore` includes `serviceAccountKey.json`
- [ ] `requirements.txt` is up to date
- [ ] Firebase working locally

## Render Setup

- [ ] Render account created
- [ ] GitHub repository connected
- [ ] Web Service created
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn app:app`
- [ ] Free tier selected

## Environment Variables

- [ ] `PYTHON_VERSION` = `3.9.0`
- [ ] `FIREBASE_CREDENTIALS` = (entire serviceAccountKey.json content as one line)

## Post-Deployment

- [ ] Deployment successful (check Render logs)
- [ ] App accessible at Render URL
- [ ] Firebase connected (check logs for "✅ Firebase Connected")
- [ ] Test homepage loads
- [ ] Test API endpoints work
- [ ] Firebase authorized domain updated

## Firebase Console Updates

1. Go to: https://console.firebase.google.com
2. Select project: `rentit-8404c`
3. Authentication → Settings → Authorized domains
4. Add: `your-app-name.onrender.com`

## Quick Commands

```bash
# Push to GitHub
git add .
git commit -m "Deploy to Render"
git push origin main

# Check if serviceAccountKey.json is ignored
git status

# View requirements
cat requirements.txt
```

## Your Render URL

After deployment, your app will be at:
`https://[your-app-name].onrender.com`

Replace `[your-app-name]` with the name you chose in Step 4.

## Common Issues

### Issue: "Module not found"
**Fix**: Add missing package to `requirements.txt`

### Issue: "Firebase initialization failed"
**Fix**: Check `FIREBASE_CREDENTIALS` environment variable

### Issue: "Application failed to start"
**Fix**: Check Render logs for specific error

### Issue: "502 Bad Gateway"
**Fix**: App is starting up (wait 30-60 seconds on free tier)

## Support

- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- Firebase Docs: https://firebase.google.com/docs

---

**Ready to deploy?** Follow `RENDER_DEPLOYMENT.md` step by step! 🚀
