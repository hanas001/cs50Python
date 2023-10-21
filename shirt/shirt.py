import sys
from PIL import Image

try:
    arg = sys.argv[1:]
except IndexError:
    sys.exit('Too few command-line arguments')

extensions = ['jpg', 'png', 'jpeg']


if len(arg) < 2:
    sys.exit('Too few command-line arguments')
elif len(arg) > 2:
    sys.exit('Too many command-line arguments')
elif len(arg) == 2:
    full_name_in = str( arg[0 ] )
    full_name_out = str(arg[-1])
    try:
        file_name_in, extension_in = full_name_in.split( '.' )
        file_name_out , extension_out = full_name_out.split ( '.' )
        # print(f'First ext is {extension_in} and second ext is {extension_out}')
        extension_in = extension_in.lower()
        extension_out = extension_out.lower()
        # print(f'First ext is {extension_in} and second ext is {extension_out}')
        # print(extensions)

        if extension_in in extensions and extension_out in extensions:
            # print('Extensions are in the list')

            if extension_in == extension_out:
                # print('Extensions are the same')

                #image open and check if it exists
                try:
                    shirt = Image.open('shirt.png')
                    size_shirt = shirt.size
                    # print(f'size of an image "shirt.png" is {size_shirt}')

                    overlayd_image = Image.open(full_name_in)
                    overlayed_image_size = overlayd_image.size
                    # print(f'size of an image {full_name_in} is {overlayed_image_size}')

                    width, height = overlayed_image_size
                    # Calculate the coordinates of the square region to be cropped.
                    square_size = min(width, height)
                    x_offset = (width - square_size) // 2
                    y_offset = (height - square_size) // 2

                    # Crop the image.
                    overlayd_image = overlayd_image.crop((x_offset, y_offset, x_offset + square_size, y_offset + square_size))

                    # Resize the image
                    overlayd_image = overlayd_image.resize((size_shirt[0], size_shirt[-1]))

                    # shirt = shirt.resize((square_size, square_size))
                    # size_shirt = shirt.size
                    # print(f'New size of an image "shirt.png" is {size_shirt}')

                    overlayd_image.paste(shirt, shirt)
                    # overlayd_image = overlayd_image.resize((size_shirt[0], size_shirt[-1]))
                    overlayd_image.save(full_name_out)
                    # print(f'Write of an image{full_name_out} successful!')

                except FileNotFoundError:
                    sys.exit('Input does not exist')


            else:
                sys.exit('Input and output have different extensions')


            # except FileNotFoundError:
            #     sys.exit(f'Could not read {full_name_in} or {full_name_out}')
        else:
            sys.exit('Invalid output')
    except ValueError:
        sys.exit('Not a valid file')