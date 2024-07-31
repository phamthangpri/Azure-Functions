# Azure Data Lake Storage Utilities

## Overview

This repository contains Python scripts to interact with Azure Data Lake Storage (ADLS) using the `azure-storage-file-datalake` library. The utilities provided include initializing connections, downloading files, checking for file existence, and uploading files to a specified directory within ADLS.

## Features

- Initialize directory and storage account clients.
- Download files from a specified directory in ADLS.
- Check if a file exists in ADLS.
- Upload files (as Pandas DataFrames) to a specified directory in ADLS.

## Prerequisites

- Python 3.x
- Azure storage account connection string
- Required Python libraries: `azure-storage-file-datalake`, `pandas`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/phamthangpri/azure_datalake_utilities.git
    ```
2. Install the required Python libraries:
    ```sh
    pip install azure-storage-file-datalake pandas
    ```

## Usage

### Initialize Directory Client

```python
from azure.storage.filedatalake import DataLakeDirectoryClient

directory_client = initialize_directory_client(conn_str='your_connection_string', container='your_container', dir_path='your_directory_path')
```
###  Download File from Directory
```
file_content = download_file_from_directory(directory_client, file_name='your_file_name.csv')
```

###  Check File Existence
```
exists = file_exists(directory_client, file_name='your_file_name.csv')
```
###  Upload File to Directory
```
import pandas as pd

data = {'column1': [1, 2], 'column2': [3, 4]}
df = pd.DataFrame(data)
upload_file_to_directory(directory_client, file_name='your_file_name.csv', input_df=df)

```

### Overall 
```
import pandas as pd
from azure_functions import *

file_name ='YOUR_FILENAME.xlsx'

def read_file(file_name:str):
    container = 'YOUR_AZURE_CONTAINER'
    dir_path = 'YOUR_FILE_PATH'
    dir_path_output = 'YOUR_OUTPUT_FILE_PATH'
    conn_str = 'YOUR_CONN_STR'
    
    directory_client = initialize_directory_client(conn_str,container,dir_path)
    try:
        print(f'reading {file_name}')
        # download a file from the container
        df_data = download_file_from_directory(directory_client,file_name) 
        
        # upload a file to the container
        directory_client_output = initialize_directory_client(conn_str,container,dir_path_output)
        upload_file_to_directory(directory_client_output,file_name,df_data)
    except Exception as err:
        error_message = f'Fail to read file {file_name}'
        raise Exception(error_message) from err
```
