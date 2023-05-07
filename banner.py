import argparse
import requests
import ssl
import platform


def get_whois_info(domain):
    try:
        import whois
        w = whois.whois(domain)

        print("WHOIS Information:")
        print(f"Domain Name: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
    except ImportError:
        print("Please install the 'python-whois' library to retrieve WHOIS information.")


def get_ssl_info(url):
    try:
        cert = ssl.get_server_certificate((url, 443))
        x509 = ssl.load_certificate(ssl.PEM, cert)

        print("SSL Information:")
        print(f"Issuer: {x509.get_issuer()}")
        print(f"Subject: {x509.get_subject()}")
        print(f"Expiration Date: {x509.get_notAfter()}")
    except ssl.SSLError:
        print("SSL Certificate Error")


def detect_os_versions():
    print("Operating System Versions:")
    print(f"Platform: {platform.platform()}")
    print(f"OS Release: {platform.release()}")
    print(f"OS Version: {platform.version()}")


def print_index_html(url):
    response = requests.get(url)
    html_content = response.text

    print("Index.html Content:")
    print(html_content)


def domain_scan(url):
    print(f"Scanning URL: {url}")
    get_whois_info(url)
    get_ssl_info(url)
    detect_os_versions()
    print_index_html(url)


def main():
    parser = argparse.ArgumentParser(description="Website Domain Scan")
    parser.add_argument("url", help="URL of the website to scan")
    parser.add_argument("-w", "--whois", action="store_true", help="Get WHOIS information")
    parser.add_argument("-s", "--ssl", action="store_true", help="Get SSL information")
    parser.add_argument("-o", "--os", action="store_true", help="Detect OS versions")
    parser.add_argument("-i", "--index", action="store_true", help="Analyze index.html content")

    args = parser.parse_args()

    if args.whois or args.ssl or args.os or args.index:
        domain_scan(args.url)
    else:
        parser.print_help()

# main function
if __name__ == "__main__":
    main()
