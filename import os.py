import os
from github import Github

# Your GitHub Personal Access Token
GITHUB_TOKEN = GIT_HUB_REPO_KEY
REPO_NAME = "ofeksoffer/trading_view_charts"  # Replace with your repository name
HTML_FILE_NAME = "chart.html"

# TradingView widget HTML template
TRADINGVIEW_HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  </head>
  <body>
    <div id="tradingview_widget"></div>
    <script type="text/javascript">
      new TradingView.widget({
        "symbol": "NASDAQ:AAPL",  // Replace with your stock symbol
        "interval": "D",         // Timeframe
        "theme": "light",        // Theme: light or dark
        "container_id": "tradingview_widget"
      });
    </script>
  </body>
</html>
"""

# Save HTML file locally
with open(HTML_FILE_NAME, "w") as file:
    file.write(TRADINGVIEW_HTML_TEMPLATE)

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Push the file to GitHub
with open(HTML_FILE_NAME, "r") as file:
    content = file.read()
repo.create_file(
    path=HTML_FILE_NAME,
    message="Add TradingView chart",
    content=content,
    branch="main",
)

print(f"File uploaded to https://{REPO_NAME}.github.io/{HTML_FILE_NAME}")
