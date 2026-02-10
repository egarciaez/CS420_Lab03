class uabcs_parser:
    def __init__(self):
        """Creates a new parser instance"""
        pass
    
    def parse_file(self, filename):
        """
        Parses a .uabcs file and returns list of record dictionaries.
        Raises ValueError for invalid file format or extension.
        Raises FileNotFoundError if file doesn't exist.
        """
        pass
    
    def get_column_names(self):
        """Returns list of column names from the parsed file"""
        pass
    
    def get_records_by_field(self, field_name, value):
        """Returns all records where specified field equals value"""
        pass