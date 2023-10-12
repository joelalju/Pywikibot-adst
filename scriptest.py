import pywikibot

def edit_page(page_title2, new_content, summary):
    
    site = pywikibot.Site('wikipedia:test')

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
    site = pywikibot.Site("test", "wikipedia") 
    username = "Mohitahmed"  # Replace with your Wikipedia username.

# Fetch your contributions.
    contribs = site.usercontribs(user=username)
    pagelist = []
# Iterate over your contributions and print page titles.
    for contrib in contribs:
        page_title = contrib["title"]
        
        if page_title not in pagelist:
             pagelist.append(page_title)
             
        
    page_title2 = "User:Mohitahmed/page3"        
        
    summary = "Updating page content."
    result = ""
    
    for pages in pagelist:
        
        new_content = "\n" + pages + "\n"
        new_content += " https://test.wikipedia.org/wiki/User:" + pages  + "\n"
        result += new_content
        
    edit_page(page_title2, result, summary)    

    #page_title2 = "User:Mohitahmed/page3"
    #r = read_page(page_title)
    #new_content = page_title
    #new_content += "https://test.wikipedia.org/wiki/User:" + page_title
    #summary = "Updating page content."
    
    #edit_page(page_title2, new_content, summary)
    


