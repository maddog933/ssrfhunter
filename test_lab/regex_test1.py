import re

# Regexp that matches any url in the main_url query
in_query_url_regexp = re.compile(r"(\S+?\=https?(?:\:\/\/|%3A%2F%2F))\S*?(\&|$)")

# Regexp that matches any url in the main_url query that contain extension
in_query_url_regexp_with_ext = re.compile(r"(\S+?\=https?(?:\:\/\/|%3A%2F%2F))[^\&]+?(?:\/|%2F)[^\&]+?(\.\w+?(?:\&|$))")

# Regexp that matches any url in the main url path
in_path_url_regexp = re.compile(r"(^https?\:\/\/[^\?]+https?(?:\:\/\/|%3A%2F%2F))\S*")

# Regexp that matches any url parameters that seems to be vulnerable

likely_vuln_params_regexp = re.compile(r"((?:\?|\&)[a-zA-Z0-9_-]*?(?:url|location|path|site)\=)[^\&]*?(\&|$)", re.IGNORECASE)

#

# Read the test urls from the test url file
with open('testurls4.txt') as test_urls_file:
    de_test_urls = test_urls_file.readlines()

# Iterate through all the urls and find http links in query string. Replace those http links with identaty string and save the results in a file
new_urls = []

for dde_url in de_test_urls:


    ##transformed_url = in_query_url_regexp.sub(r"\1"+"www.example.com"+r"\2", dde_url)

    ##transformed_url = in_query_url_regexp_with_ext.sub(r"\1"+"www.example.com/?aa"+r"\2",dde_url)

    ##transformed_url = in_path_url_regexp.sub(r"\1"+"www.example.com", dde_url)

    ##transformed_url = likely_vuln_params_regexp.sub(r"\1"+"https%3A%2F%2Fwww.example.net"+r"\2", dde_url)

    transformed_url = ""

    new_urls.append(transformed_url)


# Write the new urls in a file
with open("result_urls4.txt", "w") as result_urls_file:
    result_urls_file.writelines(new_urls)
