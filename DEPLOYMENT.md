# Deployment Guide for Go-Trader Dashboard

## 🚀 Vercel Deployment

This dashboard is configured to deploy to Vercel with a serverless API proxy.

### Prerequisites

1. **Expose Trading Bot API** - Your trading bot needs to be accessible from the internet
2. **Vercel Account** - Free tier works fine

### Option A: Automatic Deployment

The easiest way is to connect this GitHub repo to Vercel:

1. Go to [vercel.com](https://vercel.com)
2. Click "Import Project"
3. Connect GitHub and select `oclawassistant-ops/go-trader-dashboard`
4. Configure environment variable:
   - Name: `TRADER_API_URL`
   - Value: `http://YOUR_SERVER_IP:8099/status` (or use a tunnel URL)
5. Click "Deploy"

### Option B: CLI Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
cd /root/.openclaw/workspace/go-trader-dashboard
vercel --prod
```

### ⚠️ Important: API Accessibility

The dashboard needs to connect to your trading bot API at `http://srv1292914.hstgr.cloud:8099/status`

**Options to make it accessible:**

#### 1. **SSH Tunnel (Easiest for testing)**
```bash
# On your local machine
ssh -R 8099:localhost:8099 root@srv1292914
```

#### 2. **Cloudflare Tunnel (Recommended for production)**
```bash
# On your server
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
chmod +x cloudflared
./cloudflared tunnel --url http://localhost:8099
```

This gives you a public URL like `https://random-words.trycloudflare.com` that you can use in Vercel.

#### 3. **Nginx Reverse Proxy (For advanced users)**
Set up Nginx with SSL to proxy requests to port 8099.

#### 4. **Direct Port Exposure (NOT RECOMMENDED)**
Open port 8099 in your firewall - only do this with authentication!

### Environment Variables

Set in Vercel dashboard under Settings > Environment Variables:

| Variable | Value | Description |
|----------|-------|-------------|
| `TRADER_API_URL` | `https://your-tunnel-url/status` | Your trading bot API endpoint |

### Testing After Deployment

1. Visit your Vercel URL (e.g., `https://go-trader-dashboard.vercel.app`)
2. Check browser console for errors
3. Verify API connection is working

### Troubleshooting

**"Cannot connect to trading bot"**
- Check that your API is accessible from the internet
- Verify the `TRADER_API_URL` environment variable is correct
- Test the API directly: `curl https://your-tunnel-url/status`

**CORS errors**
- The serverless function should handle CORS automatically
- If issues persist, check the API endpoint allows external requests

**Dashboard loads but shows "Loading..." forever**
- API might be unreachable
- Check browser console for detailed error messages
- Verify serverless function is working: visit `/api/status` directly

---

## 🔒 Security Considerations

### Current Setup (Development)
- No authentication on API
- Anyone with the URL can view your trades
- Fine for paper trading with fake money

### Production Setup (When using real money)
1. Add API authentication (Bearer token)
2. Use environment variables for secrets
3. Implement rate limiting
4. Use HTTPS only (Cloudflare Tunnel handles this)
5. Consider IP whitelisting

### Recommended Security Stack:
```
Browser → Vercel Dashboard → Cloudflare Tunnel → Your Server:8099
         (HTTPS)              (Encrypted)         (Localhost)
```

---

## 📊 What Gets Deployed

- `index.html` - Main dashboard interface
- `api/status.js` - Serverless function to proxy API requests
- `vercel.json` - Vercel configuration

**NOT deployed:**
- `server.py` - Only needed for local development
- `dashboard.service` - Only needed for systemd on server
- `README.md` - Documentation only

---

## 🔄 Updating the Dashboard

```bash
# Make changes to index.html or api/status.js
cd /root/.openclaw/workspace/go-trader-dashboard

# Commit and push
git add -A
git commit -m "Update dashboard"
git push origin master

# Vercel auto-deploys from GitHub (if connected)
# Or manually: vercel --prod
```

---

## 💡 Alternative: Static Dashboard (No Serverless Function)

If you want a completely static dashboard that connects directly to your API:

1. Remove `api/` folder
2. Update `index.html` to use your public API URL directly
3. Ensure your API has CORS headers enabled
4. Deploy as a simple static site

This is simpler but requires your API to be publicly accessible with CORS enabled.
