# Image to ASCII Art Generator

This is a Python application that converts an image into ASCII art. It takes an image file as input, resizes it, and outputs the result to a file. The output can be either in grayscale or colorful ASCII characters.

## Installation

1. Clone the repository:
```sh
git clone https://github.com/yourusername/imagetoascii.git
```

2. Navigate to the project directory:
```sh
cd imagetoascii
# I recommend creating an environment for this
python3 -m venv env && source env/bin/activate
```

3. Install the required Python packages:
```sh
pip install -r requirements.txt
```

## Usage

You can run the program with the following command:

```sh
python3 main.py <image_path> <image_size> [--colorful] [output_path]
```

- `image_path`: Path to the image file.
- `image_size`: Size of the image. This is an integer that represents the ratio to resize the image. For example, a value of 10 would resize the image to 1/10 of its original size.
- `--colorful`: Optional flag to enable colorful output.
- `output_path`: Optional path to the output file. If not provided, the output will be saved in the `outputs` directory with the same name as the input file and a `.ascii_art` extension.

## Examples

Convert image with grayscale characters:

```sh
python main.py assets/examples/toothless.png 10
```

Convert image with colorful characters:

```sh
python main.py assets/examples/toothless.png 10 --colorful
```

Specify an output path:

```sh
python main.py assets/examples/toothless.png 10 --colorful my_output.ascii_art
```

## Output

The output is an ASCII representation of the input image. The characters used to represent the image are chosen based on their perceived brightness. Darker characters are used for darker areas of the image, and lighter characters are used for lighter areas.

Here's an example of what the output might look like:

<div style="display: flex; justify-content: space-around;">
    <img src="assets/Screenshot from 2023-12-28 17-34-36.png" width="400"/>
    <img src="assets/Screenshot%20from%202023-12-28%2017-34-51.png" width="400"/>
</div>

For example:

```text
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######*******#:@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##*****+++++****##-@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#****+===----==+***##@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@ #****+===========-=+***%@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%#***+=================***%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@##**+======+=======+=====**#+@@
@@@@@@@@@@@@@@@@@@@@@@@@@#**=-====================+**#@@
@@@@@@@@@@@@@@@@@@@@@@@@#*+============++==========**=@@
@@@@@@@@@@@@@@@@@@@@@@@#*+==========+*******+======+##@@
@@@@@@@@@@@@@@@@@@@@@@#*+=========+***********+====+*%@@
@@@@@@@@@@@@@@@@@@@@@#*+=========+**++++++++***+===+*%@@
@@@@@@@@@@@@@@@@@@@@#**=========+**+++++++++++**===+*%@@
@@@@@@@@@@@@@@@@@@@%#*+========+**++++++++++++**+-=**%@@
@@@@@@@@@@@@@@@@@@-#**========+**++++++++++++++**==**%@@
@@@@@@@@@@@@@@@@@@#**========+**+++++++++++++++**==**%@@
@@@@@@@@@@@@@@@@@%**+========**++++++++++++++++**==*#%@@
@@@@@@@@@@@@@@@@#***========***++++++++++++++++**-+*# @@
@@@@@@@@@@@@@@@@#**========***+++++++++++++++++*+=**%@@@
@@@@@@@@@@@%%###**========+**+++++++++++++++++**+=**@@@@
@@@@@@@@@%#*******========**++++++++++++++++++**==*#@@@@
@@@@@@@@%#*+=::::=**=====***++++++++++++++++++**==**#%@@
@@@@@@@%#*-.  ....-**===+**+++++++++++++++++++*+-++-**@@
@@@@@@@#*=..:=-:...=*+-+**++++++++++++++++++++*==*= -*#%
@@@@@@#**:.=****-..:**=***+++++++++++++++++++++==**=.+*#
@@@@@@%*+.=******:..**+**++++++++++++++++++++*=-+***-:**
@@@@@@%*=.+******-..+***++++++++++++++++++++++==****+.+*
@@@@@@%*-.*******-..+***++++++++++++++++++++++-+*****.=*
@@@@@@#*:.+******...***+++++++++++++++++++++*+=******.=#
@@@@@@@#-.:*****:..-**++++++++++++++++++++++*==*****=.*#
@@@@@@@@=..:+*+:..:***+++++++++++++++++++++**=+****+.=*%
@@@@@@@*#:.......:***++++++++++++++++++++++*+-*=.::.=*#@
@@@@@@@@#*-....:=****++++++++++++++++++++++*+=*- .-+*#@@
@@@@@@ #*++++++**+=*++++++++++++++++++++++**==*+==**#@@@
@@@@@##**+===+=====*+++++++++==+++++++++++**=+*##%%@@@@@
@@@@#****=========+*+++++==---------===+++**=+*%@@@@@@@@
@@@#****+=========*++++=---------------==+*+-+*@@@@@@@@@
@ #***+==========+*++=-------------------=**==*@@@@@@@@@
@#***+===========*++=---------------------=*==+%@@@@@@@@
#***+===========+*+=-----------------------*+-+#@@@@@@@@
**+**++++=======**+------------------------=*==*%@@@@@@@
**++++***+=======**+----------------------:-++=+*%#@@@@@
***+==**===========**=-------------------- .=*==**%@@@@@
@#*****=============+*+-------------------. =**=+*#@@@@@
@@@%#*+====++=========*+=--------------------**==**%@@@@
@@@@%*****##*+=========+*+=------------------+*+-+*%@@@@
@@@@@%%@@@@%**==========+***+=---------------+*+==*%@@@@
@@@@@@@@@@@%**============****+=-------------+*+==*%@@@@
@@@@@@@@@@@@#*=============+*****=---------=+**+==*#@@@@
@@@@@@@@@@@@%*+===============+*****++==++****+===*#@@@@
@@@@@@@@@@@@%*+====+*=============+*********+====+*%@@@@
@@@@@@@@@@@@%*+=====+*+==========================**@@@@@
@@@@@@@@@@@@%*+=======**+=======================**#@@@@@
@@@@@@@@@@@@%*+========***+====================**#%@@@@@
@@@@@@@@@@@@%**=========+****++==============+**#%@@@@@@
@@@@@@@@@@@@%**===========+*******++++====+***#%+@@@@@@@
@@@@@@@@@@@@%**=============+***************#@@@@@@@@@@@
@@@@@@@@@@@@@#*==============+*******#%%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*+===============+*****%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*+==================+**#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*+====================+#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*+====================+*@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*+====================+*%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%*+====================+*%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*+====================+*#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*+====================+**%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%**=====================***%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@%**=====================**+*%@@@@@@@@@@@@@@
@@@@@@@@@@@@@%**=====================**+*#@@@@@@@@@@@@@@
@@@@@@@@@@@@@%**=====================**=**@@@@@@@@@@@@@@
@@@@@@@@@@@@@ #*=====================**+*#@@@@@@@@@@@@@@
```

This can be found in the `assets/` folder.

Enjoy creating ASCII art from your images!

## Disclaimer

This code was created for an experiment, this entire project was developed using mostly *Github Copilot*.


The only human input provided were:
1. Prompts
1. Original Assets
1. Small bug fixes
1. Readme Markdown format

I am really impressed. Total dev time ~2 hours