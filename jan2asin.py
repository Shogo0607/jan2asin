
import time
from numpy import ma
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st
from selenium.webdriver.common.by import By

st.set_page_config(page_title="BUYMA 問い合わせ検索ツール")

st.title("JAN2ASIN")

st.sidebar.title("JAN2ASIN")
jan =  st.sidebar.text_input("JANコード")

if not jan:
    st.warning("JANコードを入力してください")
    st.stop()

if st.sidebar.button("検索開始"):
    st.markdown("1. 検索ツールを立ち上げます。")

    with st.spinner("現在検索ツール立ち上げ中"):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')  
        chrome_options.add_argument('--disable-dev-shm-usage') 
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(3)
    
    st.markdown("2. JANコードを検索。")
    with st.spinner("JANコードを検索中..."):
        driver.get("https://mnsearch.com/search?kwd="+str(jan))
        item_list_xpath = '//*[@id="main_contents"]/section[2]/section[1]/div/a/span'
        item_list_text = driver.find_element(By.XPATH, item_list_xpath).text
        element = driver.find_element(By.XPATH, item_list_xpath)
        driver.execute_script("arguments[0].click();", element)
        asin_xpath = '//*[@id="__main_content"]/section[3]/section[3]/section[2]/section/div[1]/span'
        asin_text = driver.find_element(By.XPATH, asin_xpath).text
        st.write("商品名：",item_list_text)
        st.write("ASIN：",asin_text)
        driver.close()