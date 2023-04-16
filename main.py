import requests
from bs4 import BeautifulSoup


print("1. Site and Text search!")
print("2. Filetype and Text Search!")
choice = input("Enter which one you would like to select: ")


if choice == "1":
    site = input("Input the domain of the top level domain: ")
    textsearch = input("Input what text you're looking for: ")

    r = requests.get(f"https://www.google.com/search?q=site%3A.{site}+%22{textsearch}%22")

    if "Try different keywords" in r.text:
        print("Searches have not been found for this, try some different keywords or a differnt TLD")
    elif "Try different keywords" not in r.text:
        print(f"Searches have been found, here is the link: {r.url}")
elif choice == "2":
    ft = input("Input the filetype: ")
    textsearch = input("Input what text you are searching for: ")

    r = requests.get(f"https://www.google.com/search?q=filetype%3A{ft}+%22{textsearch}%22")

    if "Try different keywords" in r.text:
        print("Nothing has been found for this search, try a different filetype or different text: ")
    elif "Try different keywords" not in r.text:
        print(f"Search results have been located for your search, here is the link {r.url}")


