import re

def check_phishing(url):
    score = 0

    # 1. Check if URL uses HTTPS
    if not url.startswith("https://"):
        score += 1

    # 2. Check for @ symbol (used to hide real URL)
    if "@" in url:
        score += 2

    # 3. Check for IP address instead of domain
    ip_pattern = r"(http[s]?://)?(\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, url):
        score += 2

    # 4. Check URL length
    if len(url) > 75:
        score += 1

    # 5. Check for suspicious words
    suspicious_words = ["login", "verify", "update", "bank", "secure"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    # Final Result
    if score >= 4:
        return "⚠️ Phishing Website Detected"
    elif score >= 2:
        return "⚠️ Suspicious Website"
    else:
        return "✅ Safe Website"


# Take input from user
url = input("Enter URL: ")

# Check result
result = check_phishing(url)
print("Result:", result)
