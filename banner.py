
import argparse
import requests
from bs4 import BeautifulSoup


def print_index_html(url):
    response = requests.get(url)
    html_content = response.text

    print("Index.html Content:")
    print(html_content)


def print_scripts(url):
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")
    script_tags = soup.find_all("script")

    print("Scripts used in index.html:")
    for script_tag in script_tags:
        if script_tag.has_attr("src"):
            script_url = script_tag["src"]
            print(script_url)


def domain_scan(url):
    print(f"Scanning URL: {url}")
    print_index_html(url)
    print_scripts(url)


def main():
    parser = argparse.ArgumentParser(description="Website Domain Scan")
    parser.add_argument("url", help="URL of the website to scan")
    parser.add_argument("-i", "--index", action="store_true", help="Analyze index.html content")
    parser.add_argument("-s", "--scripts", action="store_true", help="Analyze scripts used on the page")

    args = parser.parse_args()

    if args.index and args.scripts:
        domain_scan(args.url)
    elif args.index:
        print_index_html(args.url)
    elif args.scripts:
        print_scripts(args.url)
    else:
        parser.print_help()

# main function
if __name__ == "__main__":
    main()
