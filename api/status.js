// Vercel serverless function to proxy trading bot API
// This allows the frontend to fetch data without CORS issues

export default async function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    // Fetch from your trading bot API
    // You'll need to expose port 8099 or use a tunnel/proxy
    const API_URL = process.env.TRADER_API_URL || 'http://srv1292914.hstgr.cloud:8099/status';
    
    const response = await fetch(API_URL);
    
    if (!response.ok) {
      throw new Error(`API responded with status ${response.status}`);
    }
    
    const data = await response.json();
    
    return res.status(200).json(data);
  } catch (error) {
    console.error('Error fetching trading data:', error);
    return res.status(500).json({ 
      error: 'Failed to fetch trading data',
      message: error.message,
      note: 'Make sure your trading bot API is accessible at the configured URL'
    });
  }
}
