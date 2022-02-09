# emock

Emock (*emote block*) is a Python package for generating mosaic from raster images.

## Example

### Original image (scaled from 8x4)

![Original image, scaled](docs/scaled.png)

### Result

#### Text

```text
:blue_square::blue_square::blue_square::blue_square::red_square::red_square::red_square::blue_square:
:blue_square::blue_square::blue_square::yellow_square::red_square::yellow_square::blue_square::blue_square:
:purple_square::yellow_square::yellow_square::yellow_square::green_square::yellow_square::yellow_square::blue_square:
:purple_square::purple_square::purple_square::green_square::green_square::green_square::yellow_square::blue_square:
```

#### Emotes (Discord)

![Emotes mosaic](docs/emotes.png)

## Usage

### Install Emock with Git

```shell
$ git clone https://github.com/dreamscached/emock.git
$ cd emock
$ pip install -r requirements.txt
```

### Run script

```shell
$ python -m emock image
```