
def url_convert(search_convert):

    result = ""

    for search in search_convert: 

        if search in ENCODING:
            result = result + ENCODING [search] 
        elif search in UNRESERVED:
               result = result + search 
        else:
            result = "Unusable Search"
            return result
        
    return result

UNRESERVED = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789-._~"
)
ENCODING = {
    " ": "%20", 
    "%": "%25", 
    "|": "%7C",
    "&": "%26", 
    "!": "%21"
}


       

def url_space():
    user_search = input("Enter Search: ")
    search = url_convert(user_search)


    print(search)
    
url_space()