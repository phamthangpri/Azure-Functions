from azure.storage.filedatalake import DataLakeServiceClient
from azure.storage.filedatalake import DataLakeServiceClient, DataLakeDirectoryClient
import pandas as pd


def initialize_directory_client(conn_str:str,container:str,dir_path:str):
    # Init ADLS service
    service_client = initialize_storage_account(conn_str=conn_str)
    file_system_client = service_client.get_file_system_client(container)
    directory_client = file_system_client.get_directory_client(dir_path)
    return directory_client

def initialize_storage_account(conn_str:str):
    try:  
        return DataLakeServiceClient.from_connection_string(conn_str=conn_str)
    except Exception as err:
        error_message = 'Fail to init SA from connection string.'
        raise Exception(error_message) from err

def download_file_from_directory(directory_client:DataLakeDirectoryClient, file_name:str):
    '''download a file from a given directory
    '''
    try:
        file_client = directory_client.get_file_client(file_name)

        download = file_client.download_file()

        return download.readall()
    except Exception as err:
        error_message = 'Fail to download last_date file content from ADLS'
        raise Exception(error_message) from err


def file_exists(directory_client:DataLakeDirectoryClient, file_name:str):
    try:
        file_client = directory_client.get_file_client(file_name)
        return file_client.exists()
    except Exception as err:
        error_message = 'Fail to check if file exists on ADLS'
        raise Exception(error_message) from err
def upload_file_to_directory(directory_client:DataLakeDirectoryClient, file_name:str, input_df: pd.DataFrame):
    try:
        exists = file_exists(directory_client,file_name)
        if exists:
            pass
        else:
            in_memory_csv = input_df.to_csv(index=False, sep = ';')
            file_client = directory_client.get_file_client(file_name)
            file_client.upload_data(in_memory_csv, overwrite=True)
    except Exception as err:
        error_message = f'Fail to append and upload report ({file_name}) content on ADLS'
        raise Exception(error_message) from err