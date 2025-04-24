import pandas as pd
import os 

script_dir = os.path.dirname(__file__)  # Pega o diretório do arquivo atual
file_name = os.path.join(script_dir, '..', '..', 'download', 'grocery_list.csv')
file_name = os.path.abspath(file_name)  # Converte para caminho absoluto

if os.path.exists(file_name):
    # Load the grocery list from the CSV file
    grocery_list_df = pd.read_csv(file_name)

    # Extract the items from the DataFrame and store them in a list
    grocery_list = grocery_list_df['item'].tolist()

    grocery_list.append('Kiwis')
    grocery_list.append('Raspberries')

    grocery_list.remove('Eggs')
    grocery_list.remove('Nao sei')
    # Print the grocery list and inspect the output
    print(grocery_list)
else:
    print(f"Error: The file '{file_name}' was not found in the current directory.")
    print("Please ensure you have followed the instructions on the Coursera site to extract the files from the zip archive.")