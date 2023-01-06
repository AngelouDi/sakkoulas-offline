



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">sakkoulas-offline</h3>

  <p align="center">
    Downloading content from sakkoulas-online for personal offline use.
  </p>
</div>





<!-- ABOUT THE PROJECT -->
## sakkoulas-offline

This tool helps you keep download documents from sakkoulas-online.gr in pdf format for later offline use.

Keep in mind that on sakkoulas-online is copyrighted, and distribution of files downloaded from there without the permission of the authors and owners of the website is most probably illegal in your area.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You will need to have [python](https://www.python.org/) installed on your computer.
[wkhtmltopdf](https://wkhtmltopdf.org/) is also needed. You can either:
1. Install it and add it to your $PATH
2. Download just the portable executable

The first time you should run
  ```sh
  pip install -r requirements.txt
  ```

## Usage

Running
  ```sh
            _    _               _
           | |  | |             | |
 ___  __ _| | _| | _____  _   _| | __ _ ___
/ __|/ _` | |/ / |/ / _ \| | | | |/ _` / __|
\__ \ (_| |   <|   < (_) | |_| | | (_| \__ \
|___/\__,_|_|\_\_|\_\___/ \__,_|_|\__,_|___/
        __  __ _ _
       / _|/ _| (_)
  ___ | |_| |_| |_ _ __   ___
 / _ \|  _|  _| | | '_ \ / _ \
| (_) | | | | | | | | | |  __/
 \___/|_| |_| |_|_|_| |_|\___|
  
usage: sakkoulas_offline.py [-h] [-c COOKIE] [-u USERNAME] [-p PASSWORD] [-w WKHTMLTOPDF_PATH] url

Download content from sakkoulas-online.gr for offline use!

positional arguments:
  url                   The url of the book you want to download

options:
  -h, --help            show this help message and exit
  -w WKHTMLTOPDF_PATH, --wkhtmltopdf-path WKHTMLTOPDF_PATH
                        Path to a wkhtmltopdf executable

cookie access:
  -c COOKIE, --cookie COOKIE
                        The JSESSIONID of a valid login session. This option will keep you logged in.

password access:
  -u USERNAME, --username USERNAME
  -p PASSWORD, --password PASSWORD

Sharing files downloaded with this tool could be illegal in some use cases, be cautious!
```
If you are using the portable executable or haven't configured your $PATH you should also use the `-w [path to wkhtmltopdf]` argument and point to your executable.

You can either supply your username and password as 
```sh
python sakkoulas_offline.py -u username -p password [url]
``` 
to download using your credentials OR by using your JSESSIONID cookie from a valid session:
```sh
python sakkoulas_offline.py -c COOKIE [url]
```

## TODO

- [ ] Add logout option for cookie
- [ ] Add multithreaded download capabilities


See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

