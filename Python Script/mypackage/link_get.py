def link_inp():
    link = input("Enter Youtube Video link : ")
    global link_str
    try:
        link_str = str(link)
    except:
        TypeError
        print("Invalid Link")
        
    if "https://www.youtube.com" in link_str:
            print("valid Link")
            return link_str
    else:
            print("Please Enter a 'https://www.youtube.com' link.")


link_inp()


