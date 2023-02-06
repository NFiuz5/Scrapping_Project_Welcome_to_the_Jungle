import json
import pandas as pd
import os
from pathlib import Path

class DataProcessor:

    index = ['Sheet 0', 'Sheet 1', 'Sheet 2','Sheet 3', 'Sheet 4']
    data = ['Liste des résultats mise en forme','Retrait des valeurs manquantes', 
            'Retrait des doublons', 'Retrait de tous les contrats différents de CDI',
            'Nettoyage des noms de job']

    df_info = pd.DataFrame(data=data, index=index)

    def __init__(self, job: list, data_file: str, save_file: str= None, contract_type: str='CDI' ) -> None:
        
        self.data_file = data_file
        self.job = job
        self.contract_type = contract_type

        self.df = pd.DataFrame()
        self.df_list = []
        
        if save_file != None:
            self.save_file = save_file
        
        else :
            self.save_file = f'{self.job[0]}.xlsx'
    
    def read_json(self):
        #open and read json file containing raw data
    
        if os.path.exists(self.data_file):
            
            with open(self.data_file, "r") as f:
                json_list = list(json.load(f))
                
                return json_list
    
    def is_job(self):
        #tests if the job given corresponds to the job wanted 

        df_bis = self.df
        self.job = [j.lower() for j in self.job]
        
        
        for jobs_index in range(len(df_bis['job'].values)):
            df_job = df_bis['job'].iloc[jobs_index].lower()
            
            if (df_job.lower() not in self.job):
                df_bis['job'].iloc[jobs_index] = None
                
        
        return df_bis.dropna()
    
    def sheet_writer(self):
        #write step of the process in an excel file
    
        with pd.ExcelWriter(self.save_file) as writer:
            for df_index in range(len(self.df_list)):
                self.df_list[df_index].to_excel(writer, sheet_name=f'Sheet {df_index}')
            self.df_info.to_excel(writer, sheet_name='Info sheet')
    
    def df_0(self):
        #turn a json file into a pandas DataFrame
        self.df = pd.DataFrame(self.read_json())
        return self.df

    
    def df_1(self):
        #supress rows with missing values
        self.df = self.df.dropna()
        return self.df
    
    def df_2(self):
        #supress duplicates
        self.df = self.df.drop_duplicates(keep='first') 
        return self.df
    
    def df_3(self):
        #check contract type
        self.df = self.df[self.df['contract_type']==self.contract_type]
        return self.df
    
    def df_4(self):
        #check job description 
        self.df = self.is_job().dropna().reset_index(drop=True)
        return self.df
    
    def run(self):
        #running all revious functions in order to have all data in a single excel file, describing every step of the process

        df = self.df_0()       
        df1 = self.df_1()  
        df2 = self.df_2()
        df3 = self.df_3()
        df4 = self.df_4()

        self.df_list = [df,df1,df2,df3,df4]
        
        self.sheet_writer()

if __name__ == "__main__":
    
    #For tests
    
    #path to the json file containing the scraper's results
    data_file_name = input("Data file name in Data directory : \n")
    data_file = Path(__file__).parent / f"Data/{data_file_name}.json"
    
    #path to the excel file in which you want to save your processed results
    results_file_name = input("Results file name : \n")
    save_file = Path(__file__).parent / f"Results/{results_file_name}.xlsx"
    
    #list of different ways to write the name of the job offer ex : ["it manager", "manager it", "it"]
    new_job = 'y'
    job = [] 
    while new_job == 'y':
        
        job.append(input('Job description : \n'))
        new_job = input("Do you want to add another job description [y/n] : \n")
    
    #type of contract ex : "CDI"
    parse_contract = input("Do you want to specify a contract type [y/n] : \n")
    if parse_contract == 'y':
        contract_type = input("Contract type : \n")
    else :
        contract_type = "CDI" 

    DataProcessor(job=job, data_file=data_file, save_file=save_file, contract_type=contract_type).run()
    
