These functions in Python allow you to connect to a container in Azure storage and then download or upload a file.
To use these functions :

def read_file(file_name:str):
    '''read and upload a file in the directory
    '''
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
