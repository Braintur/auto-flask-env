import os

def create_structure():
    # Define the folders and files to create
    folders = ['templates', 'static', 'static/img', 'static/styles', 'static/fonts']
    files = ['static/styles/style.css', 'templates/index.html']

    html_code="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
    rel="stylesheet"
    href="{{ url_for('static', filename='styles/style.css') }}"
    />
    <title>Document</title>
</head>
<body></body>
</html>
    """
    css_code="""
body{
    background-color: black;
}
    """

    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create files
    for file in files:
        with open(file, 'w') as f:
            f.write('')  # Create an empty file
        print(f"Created file: {file}")
    with open('templates/index.html', 'w') as html_file:
        html_file.write(html_code)
        
    with open('static/styles/style.css', 'w') as css_file:
        css_file.write(css_code)
        
        

if __name__ == "__main__":
    create_structure()