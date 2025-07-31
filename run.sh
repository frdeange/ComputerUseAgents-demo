#!/bin/bash

# Computer Use Agents v2.0 - Quick Start Script
# =============================================

echo "🤖 Computer Use Agents v2.0"
echo "============================"
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found. Creating one from template..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "✅ Created .env file from template"
        echo "🔧 Please edit .env with your Azure OpenAI credentials before running"
        echo ""
    else
        echo "❌ .env.example not found"
        exit 1
    fi
fi

# Show usage options
echo "Choose how to run the application:"
echo ""
echo "1) 🌐 Web Interface (Recommended)"
echo "   python3 app_browser.py"
echo "   Then open: http://localhost:5000"
echo ""
echo "2) ⚡ Command Line Interface"
echo "   python3 app_cli.py"
echo "   Or: python3 app_cli.py \"Your task here\""
echo ""
echo "3) 🖥️  Browser Console Only"
echo "   Open: http://localhost:6080"
echo ""

read -p "Select option (1-3) or press Enter to show this help: " choice

case $choice in
    1)
        echo "🚀 Starting web interface..."
        python3 app_browser.py
        ;;
    2)
        echo "🚀 Starting CLI interface..."
        python3 app_cli.py
        ;;
    3)
        echo "🚀 Opening browser console..."
        if command -v xdg-open > /dev/null; then
            xdg-open "http://localhost:6080" &
        elif command -v open > /dev/null; then
            open "http://localhost:6080" &
        else
            echo "Please open http://localhost:6080 in your browser"
        fi
        ;;
    "")
        echo "📖 For more information, see README.md"
        ;;
    *)
        echo "❌ Invalid option. Starting web interface by default..."
        python3 app_browser.py
        ;;
esac
