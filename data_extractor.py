from websites.resources.data import WEBSITES


class DataExtractor:
    """
    Use to extract, cleanse and amend incorrect website data collection.
    """
    def __init__(self):
        self.data = WEBSITES

    def find_items(self, value=4):
        """
        Find and return a new list of items where key "value" is greater than or equal to parameter value. Default = 4.
        :return: list(dict), list of dictionaries matching the above filtering rule.
        """
        return [item for item in self.data if item.get('value') and item.get('value') >= value]

    def amend_domain_values(self, prefix='www.'):
        """
        Fixes missing parts of the domain names.
        :param prefix: str, prefix to add to the domain name. Default = 'www'.
        :return: amended: list(dict), amended list of web records.
        """
        amended = []
        for item in self.data:
            if item.get('domain') and not item.get('domain').startswith(prefix):
                item['domain'] = f"{prefix}{item['domain']}"
            amended.append(item)
        return amended


data_extractor = DataExtractor()
# print(data_extractor.amend_domain_values())
print(data_extractor.find_items(4))
print(len(data_extractor.find_items(4)))
