import time
import pandas as pd
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.keys import Keys
import datetime
from datetime import datetime as dt
from datetime import timedelta,timezone
import streamlit as st
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

st.set_page_config(page_title="BUYMA 問い合わせ検索ツール")

# JST = timezone(timedelta(hours=+9), 'JST')
st.title("BUYMA Search tool")

st.sidebar.title("BUYMA Search tool")
options = list()
max_list =  int(st.sidebar.number_input("1Pageの検索商品数",value=2))
# for ii in range(1,45):
#     options.append(ii)

# max_page =   int(st.sidebar.select_slider("検索ページ数",options=options,value=))
max_page = st.sidebar.slider('検索ページ数',1, 45, (1, 45))

item = st.sidebar.selectbox("ブランド名",['HERMES','CHANEL','CHRISTIAN DIOR','LUIS VUITTON'])
category = st.sidebar.selectbox("カテゴリ名",['レディースファッション','メンズファッション','ベビー・キッズ','ビューティー','ライフスタイル','スポーツ'])
if category == 'レディースファッション':
    domain = st.sidebar.selectbox("アイテムカテゴリ名",['レディースファッション全て','トップス','ボトムス','ワンピース・オールインワン','アウター','靴・シューズ','ブーツ','バッグ・カバン','財布・小物','アクセサリー','腕時計','アイウェア','帽子','ファッション雑貨・小物','スマホケース・テックアクセサリー','インナー・ルームウェア','水着・ビーチグッズ','ブライダル・パーティー','ヨガ・フィットネス','その他ファッション'])
    if domain == 'トップス':
        url_category = '-C2101'
    elif domain == 'ボトムス':
        url_category = '-C2102'
    elif domain == 'ワンピース・オールインワン':
        url_category = '-C2103'
    elif domain == 'アウター':
        url_category = '-C2104'
    elif domain == '靴・シューズ':
        url_category = '-C2105'
    elif domain == 'ブーツ':
        url_category = '-C2113'
    elif domain == 'バッグ・カバン':
        url_category = '-C2106'
    elif domain == '財布・小物':
        url_category = '-C2114'
    elif domain == 'アクセサリー':
        url_category = '-C2107'
    elif domain == '腕時計':
        url_category = '-C2115'
    elif domain == 'アイウェア':
        url_category = '-C2108'
    elif domain == '帽子':
        url_category = '-C2117'
    elif domain == 'ファッション雑貨・小物':
        url_category = '-C2109'
    elif domain == 'スマホケース・テックアクセサリー':
        url_category = '-C2909'
    elif domain == 'インナー・ルームウェア':
        url_category = '-C2110'
    elif domain == '水着・ビーチグッズ':
        url_category = '-C2111'
    elif domain == 'ブライダル・パーティー':
        url_category = '-C2116'
    elif domain == 'ヨガ・フィットネス':
        url_category = '-C2118'
    elif domain == 'その他ファッション':
        url_category = '-C2112'
    elif domain == 'レディースファッション全て':
        url_category = '-C1001'

elif category == "メンズファッション":
    domain = st.sidebar.selectbox("アイテムカテゴリ名",['メンズファッション全て','トップス','パンツ・ボトムス','アウター・ジャケット','靴・ブーツ・サンダル','バッグ・カバン','アクセサリー','腕時計','財布・雑貨','アイウェア','帽子','ファッション雑貨・小物','スマホケース・テックアクセサリー','インナー・ルームウェア','水着・ビーチグッズ','フィットネス','スーツ','セットアップ','その他ファッション'])
    if domain == 'トップス':
        url_category = '-C2201'
    elif domain == 'パンツ・ボトムス':
        url_category = '-C2202'
    elif domain == 'アウター・ジャケット':
        url_category = '-C2203'
    elif domain == '靴・ブーツ・サンダル':
        url_category = '-C2204'
    elif domain == 'バッグ・カバン':
        url_category = '-C2205'
    elif domain == 'アクセサリー':
        url_category = '-C2206'
    elif domain == '腕時計':
        url_category = '-C2216'
    elif domain == '財布・雑貨':
        url_category = '-C2208'
    elif domain == 'アイウェア':
        url_category = '-C2215'
    elif domain == '帽子':
        url_category = '-C2217'
    elif domain == 'ファッション雑貨・小物':
        url_category = '-C2214'
    elif domain == 'スマホケース・テックアクセサリー':
        url_category = '-C2910'
    elif domain == 'インナー・ルームウェア':
        url_category = '-C2209'
    elif domain == '水着・ビーチグッズ':
        url_category = '-C2210'
    elif domain == 'フィットネス':
        url_category = '-C2218'
    elif domain == 'スーツ':
        url_category = '-C2219'
    elif domain == 'セットアップ':
        url_category = '-C2220'
    elif domain == 'その他ファッション':
        url_category = '-C2213'
    elif domain == 'メンズファッション全て':
        url_category = '-C1002'

elif category == "ベビー・キッズ":
    domain = st.sidebar.selectbox("アイテムカテゴリ名",['ベビー・キッズ全て','ベビー服・ファッション用品(〜90cm)','子供服・ファッション用品(85cm〜)','ベビーシューズ・靴(〜14cm)','キッズシューズ・子供靴(14.5cm〜)','マタニティウェア・授乳服・グッズ','マザーズバッグ','キッズバッグ・財布','ベビーカー','チャイルドシート(ベビー/ジュニア)','チャイルドシート(ベビー/ジュニア)','抱っこ紐・スリング・ベビーキャリア','食事用グッズ','赤ちゃん用スキンケア','おもちゃ・知育玩具','ベビーベッド・バウンサー','キッズ・ベビー・マタニティその他'])

    if domain == 'ベビー服・ファッション用品(〜90cm)':
        url_category = '-C2501'
    elif domain == '子供服・ファッション用品(85cm〜)':
        url_category = '-C2502'
    elif domain == 'ベビーシューズ・靴(〜14cm)':
        url_category = '-C2505'
    elif domain == 'キッズシューズ・子供靴(14.5cm〜)':
        url_category = '-C2506'
    elif domain == 'マタニティウェア・授乳服・グッズ':
        url_category = '-C2503'
    elif domain == 'マザーズバッグ':
        url_category = '-C3862'
    elif domain == 'キッズバッグ・財布':
        url_category = '-C2507'
    elif domain == 'ベビーカー':
        url_category = '-C3783'
    elif domain == 'チャイルドシート(ベビー/ジュニア)':
        url_category = '-C3789'
    elif domain == '抱っこ紐・スリング・ベビーキャリア':
        url_category = '-C3784'
    elif domain == '食事用グッズ':
        url_category = '-C2508'
    elif domain == '赤ちゃん用スキンケア':
        url_category = '-C3786'
    elif domain == 'おもちゃ・知育玩具':
        url_category = '-C2509'
    elif domain == 'ベビーベッド・バウンサー':
        url_category = '-C2510'
    elif domain == 'キッズ・ベビー・マタニティその他':
        url_category = '-C2504'
    elif domain == 'ベビー・キッズ全て':
        url_category = '-C1005'

elif category == "ビューティー":
    domain = st.sidebar.selectbox("アイテムカテゴリ名",['ビューティー全て','メイクアップ','メイク小物','スキンケア・基礎化粧品','ヘアケア','ボディ・ハンド・フットケア','オーラル・デンタルケア','ネイルグッズ','バスグッズ','香水・フレグランス','美容家電・グッズ','メンズビューティー','サプリメント','ビューティーその他'])

    if domain == 'メイクアップ':
        url_category = '-C2301'
    elif domain == 'メイク小物':
        url_category = '-C2304'
    elif domain == 'スキンケア・基礎化粧品':
        url_category = '-C2402'
    elif domain == 'ヘアケア':
        url_category = '-C2307'
    elif domain == 'ボディ・ハンド・フットケア':
        url_category = '-C2303'
    elif domain == 'オーラル・デンタルケア':
        url_category = '-C2313'
    elif domain == 'ネイルグッズ':
        url_category = '-C2306'
    elif domain == 'バスグッズ':
        url_category = '-C2312'
    elif domain == '香水・フレグランス':
        url_category = '-C2305'
    elif domain == '美容家電・グッズ':
        url_category = '-C2314'
    elif domain == 'メンズビューティー':
        url_category = '-C2315'
    elif domain == 'サプリメント':
        url_category = '-C2316'
    elif domain == 'ビューティーその他':
        url_category = '-C2310'
    elif domain == 'ビューティー全て':
        url_category = '-C1003'

elif category == "ライフスタイル":
    domain = st.sidebar.selectbox("アイテムカテゴリ名",['ライフスタイル全て','キッチン・ダイニング','家具・日用品','インテリア雑貨','デザイン家電','ファブリック','トラベルグッズ','レジャー・アウトドア・キャンプ','ペット用品','ホビー・カルチャー','デザイン文具・ステーショナリ','ワイン','電子タバコ','ライフスタイルその他'])
    if domain == 'キッチン・ダイニング':
        url_category = '-C2401'
    elif domain == '家具・日用品':
        url_category = '-C2416'
    elif domain == 'インテリア雑貨':
        url_category = '-C2402'
    elif domain == 'デザイン家電':
        url_category = '-C2418'
    elif domain == 'ファブリック':
        url_category = '-C2414'
    elif domain == 'トラベルグッズ':
        url_category = '-C2404'
    elif domain == 'レジャー・アウトドア・キャンプ':
        url_category = '-C2417'
    elif domain == 'ペット用品':
        url_category = '-C2405'
    elif domain == 'ホビー・カルチャー':
        url_category = '-C2406'
    elif domain == 'デザイン文具・ステーショナリ':
        url_category = '-C2408'
    elif domain == 'ワイン':
        url_category = '-C2419'
    elif domain == '電子タバコ':
        url_category = '-C2415'
    elif domain == 'ライフスタイルその他':
        url_category = '-C2413'
    elif domain == 'ライフスタイル全て':
        url_category = '-C1004'

elif category == "スポーツ":
    domain = st.sidebar.selectbox("アイテムカテゴリ名",['スポーツ全て','ゴルフ','ランニング','テニス','フットボール・サッカー','ウィンタースポーツ','サーフィン','スポーツその他'])
    if domain == 'スポーツ全て':
        url_category = '-C1006'
    elif domain == 'ゴルフ':
        url_category = '-C2601'
    elif domain == 'ランニング':
        url_category = '-C2603'
    elif domain == 'テニス':
        url_category = '-C2611'
    elif domain == 'フットボール・サッカー':
        url_category = '-C2612'
    elif domain == 'ウィンタースポーツ':
        url_category = '-C2605'
    elif domain == 'サーフィン':
        url_category = '-C2607'
    elif domain == 'スポーツその他':
        url_category = '-C2610'

now = dt.now() + datetime.timedelta(hours = 9)
past_day = now - datetime.timedelta(days = 1)
max_day =  int(st.sidebar.number_input("本日から過去遡って検索する日数",value=1))

if item == "HERMES":
    url = 'https://www.buyma.com/r/_HERMES-%E3%82%A8%E3%83%AB%E3%83%A1%E3%82%B9'
elif item == 'CHANEL':
    url = 'https://www.buyma.com/r/_CHANEL-%E3%82%B7%E3%83%A3%E3%83%8D%E3%83%AB'
elif item == 'CHRISTIAN DIOR':
    url = 'https://www.buyma.com/r/_CHRISTIAN-DIOR-%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%81%E3%83%A3%E3%83%B3%E3%83%87%E3%82%A3%E3%82%AA%E3%83%BC%E3%83%AB'
elif item == 'LUIS VUITTON':
    url = 'https://www.buyma.com/r/_LOUIS-VUITTON-%E3%83%AB%E3%82%A4%E3%83%B4%E3%82%A3%E3%83%88%E3%83%B3'



bar = st.progress(0)
if st.sidebar.button("検索開始"):
    
    st.markdown("1. 検索ツールを立ち上げます。")

    with st.spinner("現在検索ツール立ち上げ中"):
        now = dt.now() + datetime.timedelta(hours=9)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')  
        chrome_options.add_argument('--disable-dev-shm-usage') 
        # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        print('>処理開始')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(5)

        item_list = list()
        item_url_list = list()
        inq_url_list = list()
        item_price_list = list()
        item_list_question_time = list()
        item_list_question_questioner = list()
        item_list_question_question = list()
        item_list_answer_time = list()
        item_list_answer_answerer = list()
        item_list_answer_answer = list()
        item_number_list = list()
        # st.success("検索ツール立ち上げ完了")
    
    all_page = int(max_page[1])-int(max_page[0])+1
    count = 0
    st.markdown("2. 問い合わせページを検索します。")
    with st.spinner("問い合わせページを検索中..."):
        for page in range(int(max_page[0]),int(max_page[1])+1):  #商品のページ数
            for shop_id in range(1,max_list+1):  #1ページの最大掲載数
                
                count += 1

                progress = int((count) /( all_page * max_list)*100)

                if page ==1:
                    driver.get(url + '/' + url_category + '/')
                else:
                    driver.get(url + '/' + url_category +'_'+str(page)+'/')

    driver.close()
    st.success("正常に終了しました。")

else:
    st.warning("検索開始ボタンを押すと、検索を開始します。")
# import time
# from numpy import ma
# import pandas as pd
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import streamlit as st
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome import service as fs
# from selenium.webdriver.common.keys import Keys
# st.set_page_config(page_title="JAN2ASIN")

# st.title("JAN2ASIN")

# st.sidebar.title("JAN2ASIN")
# jan =  st.sidebar.text_input("JANコード")

# def driver_set():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')  
#     chrome_options.add_argument('--disable-dev-shm-usage') 
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     return driver


# if not jan:
#     st.warning("JANコードを入力してください")
#     st.stop()

# if st.sidebar.button("検索開始"):
#     st.markdown("1. 検索ツールを立ち上げます。")

#     with st.spinner("現在検索ツール立ち上げ中"):
#         driver = driver_set()
    
#     st.markdown("2. JANコードを検索。")
#     with st.spinner("JANコードを検索中..."):
#         driver.get("https://mnsearch.com/search?kwd="+str(jan))
#         item_list_xpath = '//*[@id="main_contents"]/section[2]/section[1]/div/a/span'
#         item_list_text = driver.find_element(By.XPATH, item_list_xpath).text
#         element = driver.find_element(By.XPATH, item_list_xpath)
#         driver.execute_script("arguments[0].click();", element)
#         asin_xpath = '//*[@id="__main_content"]/section[3]/section[3]/section[2]/section/div[1]/span'
#         asin_text = driver.find_element(By.XPATH, asin_xpath).text
#         st.write("商品名：",item_list_text)
#         st.write("ASIN：",asin_text)
#         driver.close()