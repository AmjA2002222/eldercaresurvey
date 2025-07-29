#!/bin/bash

echo "🚀 ElderCare Survey Deployment Helper"
echo "======================================"
echo ""

echo "📋 Choose your deployment option:"
echo "1. Deploy to Render (Recommended - Free, No passcode needed)"
echo "2. Deploy to Railway (Free tier - No passcode needed)"
echo "3. Deploy to Heroku (Paid - No passcode needed)"
echo "4. Use ngrok with custom domain (Professional - No passcode needed)"
echo "5. Continue with localtunnel (Current - Requires passcode)"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🎯 Deploying to Render (Recommended)"
        echo "===================================="
        echo "1. Go to https://render.com"
        echo "2. Sign up for a free account"
        echo "3. Click 'New +' → 'Web Service'"
        echo "4. Connect your GitHub repository"
        echo "5. Set build command: pip install -r requirements.txt"
        echo "6. Set start command: python app.py"
        echo "7. Choose free plan and deploy"
        echo ""
        echo "✅ Your survey will be available at: https://your-app-name.onrender.com"
        echo "🌍 No passcode required - accessible from anywhere!"
        ;;
    2)
        echo ""
        echo "🚂 Deploying to Railway"
        echo "======================="
        echo "1. Go to https://railway.app"
        echo "2. Sign up for an account"
        echo "3. Click 'New Project' → 'Deploy from GitHub repo'"
        echo "4. Select your repository"
        echo "5. Railway will auto-detect and deploy"
        echo ""
        echo "✅ Your survey will be available at: https://your-app-name.railway.app"
        echo "🌍 No passcode required - accessible from anywhere!"
        ;;
    3)
        echo ""
        echo "🦸 Deploying to Heroku"
        echo "======================"
        echo "1. Go to https://heroku.com"
        echo "2. Sign up for an account"
        echo "3. Install Heroku CLI"
        echo "4. Run: heroku create your-app-name"
        echo "5. Run: git push heroku main"
        echo ""
        echo "✅ Your survey will be available at: https://your-app-name.herokuapp.com"
        echo "🌍 No passcode required - accessible from anywhere!"
        ;;
    4)
        echo ""
        echo "🌐 Using ngrok with custom domain"
        echo "================================="
        echo "1. Buy a domain (Namecheap, GoDaddy, etc.)"
        echo "2. Run: ngrok http 5001 --hostname=yourdomain.com"
        echo "3. Configure your domain DNS"
        echo ""
        echo "✅ Your survey will be available at: https://yourdomain.com"
        echo "🌍 No passcode required - accessible from anywhere!"
        ;;
    5)
        echo ""
        echo "🔗 Continue with localtunnel"
        echo "============================"
        echo "Current tunnel password (IP): 216.218.23.14"
        echo "Share this with visitors: https://eldercaresurvey.loca.lt"
        echo "⚠️  Visitors will need to enter the IP address as password"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        ;;
esac

echo ""
echo "📚 For detailed instructions, see DEPLOYMENT.md"
echo "🎯 Recommended: Choose option 1 (Render) for the easiest deployment!" 