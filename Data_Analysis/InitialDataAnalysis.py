import pandas
class InitialDataAnalysisClass:
    def __init__(self, df:pandas.DataFrame):
        self.dataframe = df

    def printline(self):
        print("\n-----------------------------------------------------------------\n")

    def initialDataAnalysis(self):
      print("1. Size of data: \n")
      print(self.dataframe.shape)
      self.printline()
      Two_percent = int(self.dataframe.shape[0] * 0.02)+1
      print(f"2. Data Sample: Random {Two_percent} Rows")
      print(self.dataframe.sample(Two_percent))
      self.printline()
      print("3. Data Types of Columns:\n")
      print(self.dataframe.info())
      self.printline()
      print("4. Column Names: ")
      print(self.dataframe.columns)
      self.printline()
      print("5. Missing Values: \n")
      print(self.dataframe.isnull().sum())
      self.printline()
      print("6. Mathematical Description of Data: \n")
      print(self.dataframe.describe())
      self.printline()
      print("7. Duplicate Values: \n")
      print(self.dataframe.duplicated().sum())
      self.printline()
      print("8. Correlation: \n")
      try:
        print(self.dataframe.corr())
      except Exception as e:
          print("ERROR: ", e)




# if __name__ == "__main__":
#     df = pandas.read_csv('test.csv')
#     AnalyseDataframe(df)

