import pywikibot

def edit_page(page_title2, new_content, summary):
    
    site = pywikibot.Site('mediawiki:en')

    page = pywikibot.Page(site, page_title2)

    if not page.exists():
        print(f"The page '{page_title2}' does not exist.")
        return

    page_text = page.text
    



    if page_text != new_content:
        
        page.text += new_content

        page.save(summary=summary)
        print(f"Page '{page_title2}' successfully edited.")
    else:
        print(f"Page '{page_title2}' content is already up to date.")

# def read_page(page_title):

    

#     page = pywikibot.Page(site, page_title)

#     if not page.exists():
#         print(f"The page '{page_title}' does not exist.")
#         return

#     page_text = page.text
#     words = page_text.split()
#     return words


if __name__ == "__main__":
    site = pywikibot.Site("en", "mediawiki") 
    username = "Bot"  # Replace with your Wikipedia username.

# Fetch your contributions.
    contribs = site.usercontribs(user=username)
    pagelist = []
# Iterate over your contributions and print page titles.
    for contrib in contribs:
        page_title = contrib["title"]
        
        if page_title not in pagelist:
             pagelist.append(page_title)
             
        
            
        
    
    for pages in pagelist:
        page_title2 = "Word list"
        new_content = pages
        new_content += "http://192.168.137.88/mediawiki/index.php/" + pages +"\n"
        summary = "Updating page content."
        edit_page(page_title2, new_content, summary)
        print(pages)

    #page_title2 = "User:Mohitahmed/page3"
    #r = read_page(page_title)
    #new_content = page_title
    #new_content += "https://test.wikipedia.org/wiki/User:" + page_title
    #summary = "Updating page content."
    
    #edit_page(page_title2, new_content, summary)
    


