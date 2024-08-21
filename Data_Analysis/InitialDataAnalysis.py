import pandas
class InitialDataAnalysisClass:
    def __init__(self, df:pandas.DataFrame):
        self.dataframe = df

    def printline(self):
        print("\n-----------------------------------------------------------------\n")

    def initialDataAnalysis(self):
      """
      Takes one self argument which is a pandas dataframe
      Outputs:
      1. Dataframe Shape
      2. Dataframe sample: 2% of data is shown. 1 random row is displayed if 2% of rows is 0
      3. Information of columns
      4. Name of columns
      5. Missing Values
      6. Mathematical Description of Data
      7. Duplicate Values
      8. Correlation
      # NOTE: If column contains string datatypes then correlation will return ERROR Statement
      """
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

