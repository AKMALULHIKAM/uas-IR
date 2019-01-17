from selenium import webdriver
import request
import bs4
import os
import time

kategori = "https://www.tokopedia.com/search?st=product&q=mod+"

# create the selenium brows
browser = webdriver.Chrome('D:\chromedriver')
browser.get("https://www.tokopedia.com/")


# new or top menu
while True:
    print(">>> Menu")
    print(">>> 1 - Cari Vape")
    print(">>> 0 - Exit")
    print()
    choice = int(input(">>> Your choice: "))
    if choice == 0:
        browser.quit()
        break
    print()

    # search for Mod
    if choice == 1:
        name = input("Nama mod: ")
        print()
        "%20".join(name.split(" "))
        browser.get(kategori + name)
        continue

print()
print("Goodbye!")
print()
