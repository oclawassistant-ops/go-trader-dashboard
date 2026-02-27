# Go-Trader Dashboard

**Your personal crypto trading bot monitoring system**

## ✅ What's Running

- **Trading Bot:** Continuously checking BTC & ETH momentum every hour
- **Dashboard:** Live web interface showing all your trading activity
- **Mode:** Paper trading (simulated with fake money, real prices)

## 🌐 Access Your Dashboard

**Local Access (on this server):**
```
http://localhost:8080
```

**Remote Access (from your computer):**
You'll need to set up an SSH tunnel or expose port 8080. For now, use SSH tunnel:

```bash
# Run this on YOUR computer (not the server):
ssh -L 8080:localhost:8080 root@srv1292914

# Then open in your browser:
http://localhost:8080
```

## 📊 What You'll See

### Overview Stats
- **Total Portfolio Value** - Current value of all strategies combined
- **Active Strategies** - How many strategies are currently trading
- **Total Trades** - Number of trades executed + win rate
- **Trading Cycle** - How many times the bot has checked for opportunities

### Live Prices
- Real-time BTC and ETH prices from Binance

### Strategy Details
Each strategy shows:
- **Portfolio Value** - Current total value (cash + positions)
- **P&L** - Profit/Loss in dollars and percentage
- **Trades** - Number of trades executed
- **Cash** - Available cash for trading
- **Drawdown** - Current loss from peak value (risk metric)

## 🔧 System Control

### Check Trading Bot Status
```bash
sudo systemctl status go-trader
```

### Check Dashboard Status
```bash
sudo systemctl status dashboard
```

### Restart Services
```bash
# Restart trading bot
sudo systemctl restart go-trader

# Restart dashboard
sudo systemctl restart dashboard
```

### View Logs
```bash
# Trading bot logs
tail -f /root/.openclaw/workspace/go-trader/logs/scheduler.log

# Dashboard logs
sudo journalctl -u dashboard -f
```

### Stop Everything
```bash
sudo systemctl stop go-trader
sudo systemctl stop dashboard
```

### Start Everything
```bash
sudo systemctl start go-trader
sudo systemctl start dashboard
```

## 📁 File Locations

- **Dashboard:** `/root/.openclaw/workspace/go-trader-dashboard/`
- **Trading Bot:** `/root/.openclaw/workspace/go-trader/`
- **Config:** `/root/.openclaw/workspace/go-trader/scheduler/config.json`
- **Trade History:** `/root/.openclaw/workspace/go-trader/scheduler/state.json`
- **Logs:** `/root/.openclaw/workspace/go-trader/logs/`

## 🎯 Next Steps

1. **Monitor Performance** - Watch the dashboard for 24-48 hours
2. **Analyze Results** - See which strategies are performing well
3. **Add More Strategies** - If paper trading looks good, add more
4. **Go Live** - When ready, switch to real trading with API keys

## ⚠️ Important

- Currently in **PAPER TRADING MODE** (no real money)
- Dashboard auto-refreshes every 30 seconds
- Both services start automatically on server reboot
- All trades are simulated but use real market prices

## 🔐 Security Note

The dashboard is currently only accessible locally (localhost). To access from outside:
- Use SSH tunneling (safest)
- Or set up a reverse proxy with authentication (Nginx + auth)
- Or use a VPN

**DO NOT** expose port 8080 directly to the internet without authentication!
