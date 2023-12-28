import argparse
from dataclasses import dataclass


@dataclass(frozen=True, repr=True, eq=True)
class Args:
    image_path: str
    image_size: int
    output_path_inner: str | None
    colorful: bool = False

    def __str__(self) -> str:
        return str(
            {
                'image_path': self.image_path,
                'image_size': self.image_size,
                'output_path': self.output_path,
                'colorful': self.colorful,
            },
        )

    def get_modified_image_path(self) -> str:
        # Modify the image_path to have a different output name with .ascii_art extension
        output_name = self.image_path.split(
            "/")[-1].rsplit(".", 1)[0] + ".ascii_art"
        return self.image_path.replace(self.image_path.split("/")[-1], output_name)

    @property
    def output_path(self) -> str:
        if self.output_path_inner:
            return self.output_path_inner
        
        name = self.get_modified_image_path()

        if self.colorful:
            name = "colorful_" + name

        return name

    def parseArgs():
        parser = argparse.ArgumentParser(
            prog='Image ASCII Art Generator',
            description='This program takes an image file, resizes it using the Pillow library, and outputs the result to a file.',
        )

        parser.add_argument(
            'image_path',
            help='Path to the image file',
            type=str,
            metavar='IMAGE_PATH',
        )
        parser.add_argument(
            'image_size',
            help='Size of the image',
            type=int,
            metavar='IMAGE_SIZE',
            default=1,
        )
        parser.add_argument(
            'output_path_inner',
            help='Path to the output file',
            type=str,
            metavar='OUTPUT_PATH',
            nargs='?',
        )
        parser.add_argument(
            '--colorful',
            dest='colorful',
            help='Flag to enable colorful output',
            action='store_true',
        )

        args = parser.parse_args()

        return Args(**args.__dict__)


if __name__ == '__main__':
    args = Args.parseArgs()
    print(args)
    print(args.output_path)
