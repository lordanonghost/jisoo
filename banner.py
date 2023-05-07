
import argparse
import requests
import whois


def check_website_structure(url):
    response = requests.get(url)
    status_code = response.status_code

    print(f"Website Structure Check for: {url}")
    print(f"Status Code: {status_code}")


def get_whois_info(domain):
    w = whois.whois(domain)

    print("WHOIS Information:")
    print(f"Domain Name: {w.domain_name}")
    print(f"Registrar: {w.registrar}")
    print(f"Creation Date: {w.creation_date}")
    print(f"Expiration Date: {w.expiration_date}")
    print(f"Name Servers: {w.name_servers}")


def domain_scan(url):
    print(f"Scanning URL: {url}")
    check_website_structure(url)
    domain = url.split("//")[-1]
    get_whois_info(domain)


def main():
    parser = argparse.ArgumentParser(description="Website Domain Scan")
    parser.add_argument("url", help="URL of the website to scan")
    parser.add_argument("-s", "--structure", action="store_true", help="Check website structure")
    parser.add_argument("-w", "--whois", action="store_true", help="Get WHOIS information")

    args = parser.parse_args()

    if args.structure and args.whois:
        domain_scan(args.url)
    elif args.structure:
        check_website_structure(args.url)
    elif args.whois:
        domain = args.url.split("//")[-1]
        get_whois_info(domain)
    else:
        parser.print_help()

# main function
if __name__ == "__main__":
    main()
