from argparse import ArgumentParser
import sakkoulas_parser as sak
import requests
import pdfkit


def print_banner():
    banner = """
           _    _               _
          | |  | |             | |
 ___  __ _| | _| | _____  _   _| | __ _ ___
/ __|/ _` | |/ / |/ / _ \| | | | |/ _` / __|
\__ \ (_| |   <|   < (_) | |_| | | (_| \__ \\
|___/\__,_|_|\_\_|\_\___/ \__,_|_|\__,_|___/
        __  __ _ _
       / _|/ _| (_)
  ___ | |_| |_| |_ _ __   ___
 / _ \|  _|  _| | | '_ \ / _ \\
| (_) | | | | | | | | | |  __/
 \___/|_| |_| |_|_|_| |_|\___|
  """
    print(banner)


def parse_args():
    parser = ArgumentParser(
        description="Download content from sakkoulas-online.gr for offline use!",
        epilog="Sharing files downloaded with this tool could be illegal in some use cases, be cautious!"
    )

    parser.add_argument(
        "url",
        help="The url of the book you want to download")

    cookie_access = parser.add_argument_group("cookie access")
    cookie_access.add_argument(
        "-c",
        "--cookie",
        action="store",
        help="The JSESSIONID of a valid login session. This option will keep you logged in."
    )

    pass_access = parser.add_argument_group("password access")
    pass_access.add_argument("-u", "--username", action="store")
    pass_access.add_argument("-p", "--password", action="store")

    parser.add_argument(
        "-w",
        "--wkhtmltopdf-path",
        help="Path to a wkhtmltopdf executable")

    args = parser.parse_args()
    if args.cookie and (args.username or args.password):
        parser.error("Provide either either a cookie or a user/pass combo. NOT both!")
    elif (args.username and not args.password) or (args.password and not args.username):
        parser.error("Provide both a username and a password")
    elif not (args.cookie or args.username or args.password):
        parser.error("Provide login credentials using -c | -u & -p")

    return args


def check_cookie(cookie):
    print("Validating cookie...")
    cookies = {
        'JSESSIONID': f'{cookie}',
    }

    response = requests.get('https://www.sakkoulas-online.gr', cookies=cookies)
    return "Shopping" in response.text


def login(username, password):
    print("Logging in...")
    data = {
        'username': f'{username}',
        'password': f'{password}'
    }

    response = requests.post('https://www.sakkoulas-online.gr/j_spring_security_check', data=data)
    for cookie in response.cookies:
        if cookie.name == "JSESSIONID":
            return cookie.value


def logout(cookie):
    print("Logging out.")
    cookies = {
        'JSESSIONID': f'{cookie}',
    }

    response = requests.get('https://www.sakkoulas-online.gr/access/logout/', cookies=cookies)


def main():
    print_banner()

    args = parse_args()

    cookie = args.cookie if args.cookie else login(args.username, args.password)

    try:
        config = pdfkit.configuration() if not args.wkhtmltopdf_path else pdfkit.configuration(
            wkhtmltopdf=args.wkhtmltopdf_path)
        pdfkit.from_string('', '', configuration=config)
    except OSError:
        raise SystemExit(
            "wkhtmltopdf is not present in your $PATH. Install it or use -w [path] and point to a portable executable")

    try:
        if not check_cookie(cookie):
            if args.cookie:
                raise SystemExit("Cookie provided was not valid")
            else:
                raise SystemExit("Credentials provided were not valid")
        else:
            print("Login successful!")

        sak.make_pdf(args.url, cookie, config)
    finally:
        if args.username:
            logout(cookie)


if __name__ == "__main__":
    main()
