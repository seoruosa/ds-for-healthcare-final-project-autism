import numpy as np
import pandas as pd

LIST_NAN_CODES = [90, 95, 96, 99]
HAVE_TO_MAINTAIN_COLUMNS = ["K2Q35B"]
AUTISM_RELATED_TERMS = ['asd', 'autism']

class CleaningData:
    """
    Class to help the process of cleaning the data
    """
    def __init__(self, dataPath:str, columnDescriptionPath:str, index_col_data=None, seed=0):
        self.__dataPath = dataPath
        self.__index_col_data = index_col_data
        self.__columnDescriptionPath = columnDescriptionPath
        np.random.seed(seed)
    
    def convertMissingCodesToNaN(self, df, listNaNCodes=LIST_NAN_CODES) -> pd.DataFrame:
        return df.replace(listNaNCodes, np.nan)

    def filterDescriptionWithElementsToList(self, df:pd.DataFrame, elementsList=AUTISM_RELATED_TERMS, column='description') -> list:
        return (df[df[column].fillna('').str.contains(f"({'|'.join(elementsList)})", case=False)]).index.values.tolist()
    
    def readColumnsDescription(self, header=None) -> pd.DataFrame:
        return pd.read_excel(self.__columnDescriptionPath, header=header, names=["column", "description"], index_col="column")
    
    def saveColumnsdescriptionCSV(self, df, filepath) -> None:
        df.to_csv(filepath)
    
    def selectColumns(self, df, excludeColumnsList:list, haveToMaintainColumns=HAVE_TO_MAINTAIN_COLUMNS):
        return df[[col for col in df.columns.values if col not in excludeColumnsList or col in haveToMaintainColumns]]

    def openData(self) -> pd.DataFrame:
        return pd.read_csv(self.__dataPath, index_col=self.__index_col_data)

    def saveData(self, df:pd.DataFrame, processedFilePath:str) -> None:
        addGZIPtoFilePath = lambda x: x if x.find(".gzip")!=-1 else f"{x}.gzip"
        df.to_csv(addGZIPtoFilePath(processedFilePath), compression='gzip')

    def defaultClean(self, processedFilePath:str, listNaNCodes=LIST_NAN_CODES, headerColumnsDescription=None, 
                     elementsList=AUTISM_RELATED_TERMS):
        df = self.openData()
        df = self.convertMissingCodesToNaN(df, listNaNCodes)
        df_vars = self.readColumnsDescription(headerColumnsDescription)
        columns_to_exclude = self.filterDescriptionWithElementsToList(df_vars, elementsList)
        df = self.selectColumns(df, columns_to_exclude, HAVE_TO_MAINTAIN_COLUMNS)
        self.saveData(df, processedFilePath)


if __name__ == "__main__":
    folderpath = "../data/raw/childhealthdata/2017-2018_NSCH_Topical_CSV_DRC_Jan2020"
    
    filepath = f"{folderpath}/2017-2018 NSCH_Topical_DRC_Dec 2019.csv"
    variablesDescriptionPath = f"{folderpath}/test.xlsx"
    
    saveFilePath = "../data/processed/2017-2018_NSCH_DRC.csv"
    saveColumnsDescriptionFilePath = "../data/processed/2017-2018_description_columns.csv"

    clean = CleaningData(filepath, variablesDescriptionPath)
    clean.defaultClean(saveFilePath)
    # clean.saveColumnsdescriptionCSV(clean.readColumnsDescription(), f"../data/processed/2017-2018_description_columns.csv")