class CreateTable:
    def __init__(self, row_headers, col_headers):
        self.row_headers = row_headers
        self.col_headers = col_headers

    def add_values(self, data):
        if len(self.col_headers) > 1:
            return {
                row: dict(zip(self.col_headers, values))
                for row, values in zip(self.row_headers, data)
            }
        else:
            return {row: values[0] for row, values in zip(self.row_headers, data)}


# Example usage
def Example1():
    row_headers = ["Row1", "Row2", "Row3"]
    col_headers = ["Col1", "Col2", "Col3"]
    values = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    table = CreateTable(row_headers, col_headers).add_values(values)
    print(table)

def Example2():
    row_headers = ["Row1", "Row2", "Row3"]
    col_headers = ["Col1", "Col2", "Col3"]
    table = CreateTable(row_headers, col_headers)
    table_dict = dict()
    
    values = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    table_dict["page1"] = table.add_values(values)

    values = [
        [10, 20, 30],
        [20, 40, 60],
        [30, 60, 90]
    ]
    table_dict["page2"] = table.add_values(values) 
    
    print(table_dict)

def filter_parameters(param_dict, class_ref):
    """Filter required parameters from a dictionary based on the class's __init__ method."""
    return {k: param_dict[k] for k in param_dict if k in class_ref.__init__.__code__.co_varnames}