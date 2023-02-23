from itertools import count
import re
import random

def match_inparam(murl, sub_url): 
    
    #match one or more url in query param
    m_inparam = re.compile(r"(\S+?\=https?(?:\:\/\/|%3A%2F%2F))\S*?(\&)")
    
    m_end_inparam = re.compile(r"(\S+?\=https?(?:\:\/\/|%3A%2F%2F))[^\&]+$")

    if m_end_inparam.search(murl):
        d_newurl = m_end_inparam.sub(r"\1"+sub_url, murl)

        if m_inparam.search(d_newurl):
            new_url = m_inparam.sub(r"\1"+sub_url+r"\2", d_newurl, count=70)
            return new_url

    elif m_inparam.search(murl):
        new_url = m_inparam.sub(r"\1"+sub_url+r"\2", murl, count=70)
        return new_url


def check_extension(murl, sub_url):

    test_url = sub_url+"/?aaa"

    match_in_param = re.compile(r"(\S+?\=https?(?:\:\/\/|%3A%2F%2F))[^\&]+?(?:\/|%2F)[^\&]+?(\.[a-z]+\&)")

    matchend_inurl = re.compile(r"(\S+?\=https?(?:\:\/\/|%3A%2F%2F))[^\&]+?(?:\/|%2F)[^\&]+(\.[a-z]+?[^\&]+$)")
    
    if matchend_inurl.search(murl) and match_in_param.search(murl):
        mtch11 = matchend_inurl.sub(r"\1"+test_url+r"\2",murl)

        mtch22 = match_in_param.sub(r"\1"+test_url+r"\2",mtch11)

        return mtch22


    elif match_in_param.search(murl):
        dem_cought = match_in_param.sub(r"\1"+test_url+r"\2", murl)
        return dem_cought

    elif matchend_inurl.search(murl):
        fuk_cought = matchend_inurl.sub(r"\1"+test_url+r"\2", murl)
        return fuk_cought
        
def smell_like_url(murl, sub_url):

    test_url = "https://"+sub_url

    # Match at the end of url
    mtchat_end = re.compile(r"([\w_-]*?(?:url|URL|Url)\=)(?:$|[^&]+$)")

    # Match in btwn params
    mtch_inbtwn = re.compile(r"([\w_-]*?(?:url|URL|Url)\=)\S*?(\&)")

    if mtchat_end.search(murl) and mtch_inbtwn.search(murl):
        smell1b_url = mtchat_end.sub(r"\1"+test_url, murl)

        smellboth_url = mtch_inbtwn.sub(r"\1"+test_url+r"\2", smell1b_url)

        return smellboth_url

    elif mtchat_end.search(murl):
        smellend_url = mtchat_end.sub(r"\1"+test_url,murl)
        return smellend_url

    elif mtch_inbtwn.search(murl):
        smellmid_url = mtch_inbtwn.sub(r"\1"+test_url+r"\2",murl)
        return smellmid_url

def ssrfpoint(flname, sub_url):

    # Regex comp list
    #General match
    m_http_inurl = re.compile(r"^(http\S+?https?(?:\:\/\/|%3A%2F%2F))\S*")

    #General mutch with extension
    m_gen_ext = re.compile(r"^(http\S+?https?(?:\:\/\/|%3A%2F%2F))[^\&]+?(?:\/|%2F)[^\&]+?(\.[a-z]+?\S*)")

    #match all accurence url in query parameters
    m_param_url1 = re.compile(r"^http\S+?\?\S+?\=https?(?:\:\/\/|%3A%2F%2F)\S+?\&\S*")

    #match query params that smell like they contain url
    smellUrl_param = re.compile(r"^http\S+?\?\S*?[\w_-]*?(?:url|URL|Url)\=\S*")




    # Read the urls file
    with open(flname) as urlfile:
        url_list = urlfile.readlines()
    
    # A set to store all maches
    all_found = set()


    # Iterate through a list of urls finding a match
    for murl in url_list:
        murl = murl.strip()


        if m_param_url1.search(murl):

            dnew_rl = match_inparam(murl, sub_url)
            if dnew_rl != None:
                all_found.add(dnew_rl+"\n")

            ext_mtch = check_extension(murl, sub_url)
            if ext_mtch != None:
                all_found.add(ext_mtch+"\n")


        elif m_http_inurl.search(murl):
            match_sub = m_http_inurl.sub(r"\1"+sub_url,murl)
            if match_sub != None:
                all_found.add(match_sub+"\n")

            # Check whether the url has an extension and substitute it
            if m_gen_ext.search(murl):
                mtch_ext = m_gen_ext.sub(r"\1"+sub_url+"/?sss"+r"\2",murl)
                if mtch_ext != None:
                    all_found.add(mtch_ext+"\n")

        elif smellUrl_param.search(murl):
            smelled_url = smell_like_url(murl, sub_url)
            if smelled_url != None:
                all_found.add(smelled_url+"\n")



    # Return all found urls
    return all_found
    