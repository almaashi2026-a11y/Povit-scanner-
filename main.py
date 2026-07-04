import time
import random
import config
import finnhub
from concurrent.futures import ThreadPoolExecutor

# إعداد العميل
finnhub_client = finnhub.Client(api_key=config.FINNHUB_API_KEY)

def get_market_stocks():
    # جلب قائمة أسهم ناسداك (كمثال)
    return finnhub_client.stock_symbols(exchange='US')

def scan_single_stock(symbol):
    try:
        # هنا ستضع منطق التحليل الخاص بك (القاع الصاعد)
        # quote = finnhub_client.quote(symbol['symbol'])
        # if condition_met:
        #     return f"🚀 {symbol['symbol']}"
        pass
    except Exception:
        return None

def main():
    print("--- البوت بدأ العمل (نظام 50 سهم) ---")
    stocks = get_market_stocks() # جلب القائمة كاملة
    
    while True:
        # اختيار 50 سهم عشوائي
        sample_stocks = random.sample(stocks, 50)
        
        print(f"--- فحص جديد لـ 50 سهم... ---")
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(scan_single_stock, sample_stocks))
        
        # طباعة النتائج التي تم العثور عليها
        found = [r for r in results if r]
        print(f"تم الانتهاء! الفرص المكتشفة: {found}")
        
        print("انتظار 5 دقائق للدورة التالية...")
        time.sleep(300)

if __name__ == "__main__":
    main()
