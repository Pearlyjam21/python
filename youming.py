import feedparser
import requests
from bs4 import BeautifulSoup
import feedparser
from urllib.parse import urlparse, parse_qs

def extract_real_url(google_url):
    parsed = urlparse(google_url)
    return parse_qs(parsed.query).get('url', [google_url])[0]

# 解析 Google 快訊 RSS feed
feed_url = 'https://www.google.com/alerts/feeds/15616787765566891372/9864151895024129643'
feed = feedparser.parse(feed_url)

print(f"從 feed 中獲取到 {len(feed.entries)} 個條目")

for entry in feed.entries:
    print(f"\n正在處理文章: {entry.title}")
    google_url = entry.link
    url = extract_real_url(google_url)
    print(f"原始 URL: {google_url}")
    print(f"提取後的 URL: {url}")
    
    try:
        # 發送請求獲取網頁內容
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 如果請求不成功則拋出異常
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 嘗試多種常見的文章內容選擇器
        selectors = [
            'div.article-content',
            'div.entry-content',
            'div.post-content',
            'article',
            'main',
            '.content'  # 添加更多可能的選擇器
        ]
        
        content = None
        for selector in selectors:
            content = soup.select_one(selector)
            if content:
                print(f"使用選擇器 '{selector}' 成功找到內容")
                break
        
        if content:
            # 提取純文本並去除多餘的空白字符
            text = ' '.join(content.stripped_strings)
            print(f"提取的內容 (前 200 字符): {text[:200]}...")
        else:
            print("無法找到文章內容")
            print("頁面標題:", soup.title.string if soup.title else "無標題")
            print("頁面內容預覽:", soup.get_text()[:200])
        
    except requests.RequestException as e:
        print(f"請求失敗: {e}")
    except Exception as e:
        print(f"處理過程中出現錯誤: {e}")

print("\n爬取完成")