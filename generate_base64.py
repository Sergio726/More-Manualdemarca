import base64
import os

files = ['logo_more_light.png', 'logo_more_dark.png']

for file in files:
    if os.path.exists(file):
        with open(file, 'rb') as f:
            encoded_string = base64.b64encode(f.read()).decode('utf-8')
            with open(file + '.base64', 'w') as out:
                out.write(encoded_string)
            print(f"Generated {file}.base64")
    else:
        print(f"File {file} not found")
