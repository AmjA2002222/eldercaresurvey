# ElderCare Survey - Deployment Guide

## Option 1: Deploy to Render (Recommended - Free)

1. **Sign up at Render.com**
   - Go to https://render.com
   - Create a free account

2. **Connect your GitHub repository**
   - Push your code to GitHub
   - Connect your GitHub account to Render

3. **Create a new Web Service**
   - Click "New +" → "Web Service"
   - Connect your repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python app.py`
   - Choose the free plan

4. **Your survey will be available at**: `https://your-app-name.onrender.com`

## Option 2: Deploy to Railway (Free tier available)

1. **Sign up at Railway.app**
   - Go to https://railway.app
   - Create an account

2. **Deploy from GitHub**
   - Connect your GitHub repository
   - Railway will automatically detect it's a Python app
   - Deploy with one click

3. **Your survey will be available at**: `https://your-app-name.railway.app`

## Option 3: Deploy to Heroku (Free tier discontinued, but still popular)

1. **Sign up at Heroku.com**
2. **Install Heroku CLI**
3. **Deploy using CLI**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## Option 4: Use ngrok with a VPS (More control)

1. **Rent a cheap VPS** (DigitalOcean, Linode, Vultr - $5/month)
2. **Upload your code to the VPS**
3. **Run your app on the VPS**
4. **Use ngrok for tunneling**:
   ```bash
   ngrok http 5001
   ```

## Option 5: Use a Domain with ngrok (Professional)

1. **Buy a domain** (Namecheap, GoDaddy, etc.)
2. **Set up ngrok with custom domain**:
   ```bash
   ngrok http 5001 --hostname=yourdomain.com
   ```

## Security Considerations for Production

Before deploying, consider adding these security improvements:

1. **Add environment variables** for sensitive data
2. **Use a production database** (PostgreSQL, MySQL)
3. **Add HTTPS enforcement**
4. **Implement rate limiting**
5. **Add input validation**
6. **Set up monitoring and logging**

## Quick Start with Render (Recommended)

1. Push your code to GitHub
2. Go to https://render.com
3. Create account and connect GitHub
4. Create new Web Service
5. Deploy automatically
6. Share the URL with anyone, anywhere!

Your survey will be accessible 24/7 from anywhere in the world. 