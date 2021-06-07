import csv
import importlib
import inspect


class TableData(object):
    """Returns loadable data objects for VBR Table Classes
    
    Data can be defined as dict-mapped JSON in the DATA 
    property or can be provided in a csv file with the 
    same root name as the table data clss module file 
    (i.e. FileFormatData is defined in file_format.py 
    and records can be provided in file_format.csv)
    """
    CLASSNAME = None
    DATA = []

    def __init__(self):
        self.objects = []
        m = importlib.import_module('vbr.tableclasses')
        if self.CLASSNAME is not None:
            cn = self.CLASSNAME
        else:
            cn = self.__class__.__name__
            if cn.endswith('Data'):
                cn = cn[:len(cn) - 4]

        cl = getattr(m, cn)
        self.__classname__ = cn
        self.__classref__ = cl

    @property
    def csv_path(self):
        mod_path = inspect.getfile(self.__class__)
        mod_path = mod_path.replace('.py', '.csv')
        return mod_path

    def load_csv(self):
        records = []
        try:
            with open(self.csv_path, 'r') as data:
                for record in csv.DictReader(data):
                    records.append(record)
        except FileNotFoundError:
            pass
        return records

    @property
    def records(self):
        cl = self.__classref__
        if len(self.DATA) == 0:
            self.DATA = self.load_csv()
        for d in self.DATA:
            self.objects.append(cl(**d))
        return self.objects
