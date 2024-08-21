from Data_Analysis.InitialDataAnalysis import InitialDataAnalysisClass
import pandas

def AnalyseDataframe(df:pandas.DataFrame):
    obj = InitialDataAnalysisClass(df)
    obj.initialDataAnalysis()