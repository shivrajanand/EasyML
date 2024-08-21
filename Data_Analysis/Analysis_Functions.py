from Data_Analysis.InitialDataAnalysis import InitialDataAnalysisClass
import pandas

def AnalyseDataframe(df:pandas.DataFrame):
    """
    uses the Initial Data Analysis Class object to analyse a pandas dataframe
    without the user needing to instantiate an object of the class.
    """ 
    obj = InitialDataAnalysisClass(df)
    obj.initialDataAnalysis()