from bs4 import BeautifulSoup

class HTMLDataExtractor:
    def __init__(self, html_string):
        self.html_string = html_string
        self.soup = BeautifulSoup(html_string, "html.parser")

    def extract_data(self, data_spec):
        extracted_data = {}
        
        for key, spec in data_spec.items():
            tag = spec.get("tag")
            tag_class = spec.get("class")
            tag_id = spec.get("id")
            
            if tag:
                if tag_class:
                    element = self.soup.find(tag, class_=tag_class)
                elif tag_id:
                    element = self.soup.find(tag, id=tag_id)
                else:
                    element = self.soup.find(tag)
                
                extracted_data[key] = element.get_text(strip=True) if element else None
        
        return extracted_data
