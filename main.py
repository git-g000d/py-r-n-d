from html_data_extractor import HTMLDataExtractor

html_string = """
<html>
    <body>
        <h1>Welcome to My Website</h1>
        <p class="description">This is a sample website for extracting data.</p>
        <a id="main-link" href="https://example.com">Click Here</a>
    </body>
</html>
"""

data_spec = {
    "title": {"tag": "h1"},
    "description": {"tag": "p", "class": "description"},
    "link": {"tag": "a", "id": "main-link"}
}

extractor = HTMLDataExtractor(html_string)
extracted_data = extractor.extract_data(data_spec)
print(extracted_data)