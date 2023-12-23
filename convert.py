import json
import csv

'''
                      =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                      
                   ...=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#...                   
                  :@@@#--------------------------------------------*@@@=                  
               :::-%%%*--------------------------------------------+%%%+:::               
               @@@%----------------------------------------------------%@@@:              
           :---###*----------------------------------------------------*###+---           
           #@@@=----------------------------MBO-----------------------------@@@@           
       :===*###------------------https://x.com/burakhoc-------------------*###+==-       
     =@@@+---------------------https://x.com/injectigos-------------------------=@@@#       
   .*******=------------------------------------------------------------------=*******-   
   :@@@#--------------------------------------------------------------------------*@@@+   
###*+++=-----------------------------=***********###*-----------------------------=+++####
@@@%---------------------------------+###########%%%#---------------------------------%@@@
@@@%-----------------------------=***###################+-----------------------------%@@@
@@@%-----------------------------=###################%%%*-----------------------------%@@@
@@@%--------------------------#######*-------###########%%%%=-------------------------%@@@
@@@%--------------------------#######*-------###########%%%%+======-------------------%@@@
@@@%--------------------------##############################%%%%%%%#------------------%@@@
@@@%--------------------------####*******####***********####%%%%%%%*------------------%@@@
@@@%--------------------------@@@%:::::::#@@@    :::::::#@@@+-------------------------%@@@
@@@%--------------------------@@@%:::::::+###   .:::::::#@@@+-------------------------%@@@
@@@%--------------------------@@@%::::::::::::::::::::::#@@@+-------------------------%@@@
@@@%--------------------------@@@%:::::::=+++***+:::::::#@@@+-------------------------%@@@
@@@%--------------------------@@@%:::::::#@@@@@@%:::::::#@@@+-------------------------%@@@
@@@%--------------------------****###+:::=++++++=:::=####***=-------------------------%@@@
@@@%-----------------------------=@@@*::::::::::::::*@@@*-----------------------------%@@@
@@@%-----------------------------=@@@%%%%+::::::-%%%@@@@@%%%%%%%----------------------%@@@
@@@%-----------------------------=@@@@@@@*::::::=@@@@@@@@@@@@@@@----------------------%@@@
@@@%--------------------------%%%%@@@@@@@*::::::=@@@@@@@@@@@@@@@@@@#------------------%@@@
@@@%--------------------------@@@@@@@@@@@*::::::=@@@@@@@@@@@@@@@@@@%------------------%@@@
@@@%----------------------#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*--------------%@@@
@@@%------------------====#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#===-----------%@@@
@@@%------------------*@@@@@@@.  :@@@@@@@*===+++*@@@@@@@+   @@@@@@@@@@@@@@@+----------%@@@
%%%%+++=----------=+++*#######   :%%%@@@@*===****@@@@%%%=   %%%%@@@@@@@@@@@*+++---=+++#%%%
   :@@@#----------+@@@+              :+++****%%%#===-          :@@@@@@@@@@@@@@@---*@@@+   
   .###*+++=---+******-              :+++****####===-          :###%@@@@@@@@@@@*++####-   
       =@@@+---@@@#                  :===*###****+++=              =@@@@@@@@@@@@@@#       
       :*******+++=       -+++       .:::+***++++---========+++=   =@@@@@@@@@@@***=       
           #@@@           #@@@           =+++====   =@@@@@@@@@@%   =@@@@@@@@@@@           
           -+++*++=       #@@@           ::::::::   :=======@@@%   =@@@@@@@*+++           
               @@@#       #@@@                              @@@%   =@@@@@@@:              
               ---=#######@@@@           +###               @@@@###%@@@*---               
                  :@@@@@@@@@@@           #@@@               @@@@@@@@@@@=                  
                   :::*@@@@@@@%%%%%%%%%%%@@@@%%%%%%%%%%%%%%%@@@@@@@%:::.                  
                      =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                      

'''

def extract_number_from_name(name):
    # '#' işaretli sayıları alarak '.png' ekler
    return ''.join(c for c in name if c.isdigit())


def convert_json_to_csv(json_file_path, csv_file_path):
    # CSV dosyasını oluştur ve başlık satırını yaz
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        header = ["Filename", "Title", "Description", "NbCopies", "NbSelf", "Background", "Bear", "Body", "Bot", "Bunny",
                  "Cape", "Chick", "Clothes", "Devil", "Facial Hair", "Hair", "Head", "Heart", "Hoodie",
                  "Lord Cape", "Ninja", "Tags"]

        writer.writerow(header)

    # JSON dosyasını aç ve her bir veriyi CSV'ye yaz
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

        for data in json_data:
            with open(csv_file_path, mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)

                row_data = [
                    "{}.png".format(extract_number_from_name(
                        data.get('name', 'None'))),
                    data.get("name", "None"),
                    data.get("description", "None"),
                    1,  # NbCopies
                    0,  # NbSelf
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Background"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Bear"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Body"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Bot"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Bunny"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Cape"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Chick"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Clothes"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Devil"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Facial Hair"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Hair"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Head"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Heart"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Hoodie"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Lord Cape"), "None"),
                    next((attr["value"] for attr in data["attributes"]
                         if attr["trait_type"] == "Ninja"), "None"),
                    data.get("Tags", "injectigos/InjectigosNft/injectiveNFT"),
                ]

                writer.writerow(row_data)

    print(f"CSV dosyası oluşturuldu: {csv_file_path}")


# Kullanım örneği
json_file_path = '/your-path/injectigos-metadata/metadata.json'
csv_file_path = '/your-path/injectigos-metadata/injectigos_metadata.csv'

convert_json_to_csv(json_file_path, csv_file_path)
