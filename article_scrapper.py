import argparse
import requests
from urllib.parse import urlparse

parser = argparse.ArgumentParser()

def validate_url(url):
    try:
        res_url = urlparse(url)
        if all([res_url.scheme, res_url.netloc]):
            if not res_url.scheme in ['http', 'https']:
                raise ValueError("URL must start with http:// or https://")
            return url
        else:
            raise ValueError("Invalid URL format")
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid URL {e}")

def fetchContent(url):
    r = requests.get(url)
    return r.text

def parseContent():
    return -1


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="News Article Web Scraper")
    
    # Add URL argument with validation
    parser.add_argument(
        '-u',
        '--url',  # This is the name of the argument
        type=validate_url,  # Use the custom validation function
        help="URL of the news article to scrape"
    )
    
    # Parse arguments
    args = parser.parse_args()

    # print(args)
    
    # Now you can access the validated URL
    print(f"Scraping article from: {args.url}")
    # Add your scraping logic here
    fetchContent(args.url)

if __name__ == "__main__":
    main()

