# lerrigattobot

My twitch bot with some fancy commands, like `!test`
Documentation magically generated with sphinx and available as [pages](https://lerrigatto.github.io/lerrigattobot/)


Based on [TwitchIO](https://github.com/TwitchIO/TwitchIO)

This project uses [poetry](https://python-poetry.org/).
You need a .env with the keys and stuff.
To run it, do `poetry run lerrigattobot`

To build it, do `poetry build`

You can install it with `pip3 install <whatever>.whl` and run it with: `export $(cat .env | xargs) && lerrigattobot`
