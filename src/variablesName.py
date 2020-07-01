import pandas as pd
try:
    import pathconfig as pathcfg
except ImportError:
    import src.pathconfig as pathcfg

class VariablesName():
    __descriptionColumnName = "description"
    def __init__(self):
        self.__dictColumnsDescriptions = self.__listFromCSV()

    def allColumns(self):
        return [a for a in self.__dictColumnsDescriptions]
    
    def allDescriptions(self):
        return [self.__dictColumnsDescriptions[a] for a in self.__dictColumnsDescriptions]

    def descriptionOfColumn(self, column:str) -> str:
        return self.__dictColumnsDescriptions.get(column)

    def __listFromCSV(self):
        df = pd.read_csv(pathcfg.columnDescriptionPath, index_col="column")
        columnsName = df.index.tolist()
        columnsDescription = df[self.__descriptionColumnName].fillna("").values
        return {i:j for i,j in zip(columnsName, columnsDescription)}

if __name__ == "__main__":
    a = VariableName()
    a.allColumns()