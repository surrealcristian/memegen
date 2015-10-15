# memegen

Caption memes from command line, the easy way.


## Requirements

- Python 3
- requests


## Installation

- Install the latest stable release with `pip install kl` or ...

- Install dependencies (`pip install requests`) and download
  [memegen.py](https://raw.githubusercontent.com/surrealcristian/memegen/master/memegen.py)
  (unstable).


## CLI usage

    usage: memegen.py [-h] [-l] [-s {imgflip,memegenerator}] [meme] [top] [bottom]

More help running `./memegen.py -h`.

### Examples:

    $ ./memegen.py -l
    ancient-aliens
    archaic-rap
    bad-luck-brian
    conspiracy-keanu
    courage-wolf
    doge
    ...

    $ ./memegen.py doge 'wow' 'very simple'
    http://i.imgflip.com/skcr1.jpg


## Using `memegen` as a library

`memegen` can also be used as a library.

TODO


## License

MIT
