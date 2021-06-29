import urllib.request as urlreq
import sys

args = sys.argv
if ".py" or ".exe" in args[0]:
    del args[0]
search_name = ' '.join(args)

URL = "https://pypi.org/search/?q="

print("""
##############################
# PyPi Library Search System #
#         @AiueoABC          #
##############################
""")


def search(name):
    query_name = ""
    name_list = name.split()
    for q in name_list:
        query_name = query_name + '+' + q
    try:
        fp = urlreq.urlopen(URL + query_name)
        ret = fp.read().decode("utf8")
        fp.close()
        print(f'Search Result For "{name}":')
        for line in ret.splitlines():
            if "package-snippet__name" in line:
                print(line.replace('<span class="package-snippet__name">', '').replace('</span>', ''))
    except Exception as e:
        print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    search(search_name)
