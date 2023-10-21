extensions = ['jpg', 'png', 'jpeg']

extension_in = 'jpg'
extension_out = 'bmp'

extension_in = extension_in.lower()
extension_out = extension_out.lower()
print(f'First ext is {extension_in} and second ext is {extension_out}')

if extension_in in extensions and extension_out in extensions:
    print('Extensions are in the list')

    if extension_in == extension_out:
        print('Extensions are the same')
    else:
        print('Input and output have different extensions')

else:
    print('Extensions are NOT in the list')