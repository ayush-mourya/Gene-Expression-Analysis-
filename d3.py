import os
import GEOparse
import csv


# NORMAL
accession_numbers = ['GSM706036', 'GSM706037', 'GSM706038', 'GSM706039']


output_folder = "NORMAL"


# Create the output folders if they don't exist
os.makedirs(output_folder, exist_ok=True)


for accession_number in accession_numbers:
    try:
        # Load the dataset from GEO
        gse = GEOparse.get_GEO(geo=accession_number, destdir=output_folder)
        
      
        
        # Save the data to a tab-separated file
        filename = f"{accession_number}.txt"    
       
      
        

        
    except Exception as e:
        print(f"failed to download {accession_number}: {str(e)}")


import os
import csv

input_folder = "NORMAL"
output_folder1 = "NORMAL_CSV"

# Create the output folder if it doesn't exist
os.makedirs(output_folder1, exist_ok=True)

# Get a list of all text files in the input folder
text_files = [file for file in os.listdir(input_folder) if file.endswith('.txt')]

for file_name in text_files:
    try:
        # Read the contents of the text file, skip first 48 lines
        with open(os.path.join(input_folder, file_name), 'r') as file:
            lines = file.readlines()[46:-1]

        # Write the modified data to a new CSV file in the output folder
        with open(os.path.join(output_folder1, file_name[:-4] + '.csv'), 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            for line in lines:
                writer.writerow(line.strip().split('\t'))

        print(f"Processing completed for {file_name}. Output saved to '{output_folder1}/{file_name[:-4]}.csv'")
    except Exception as e:
        print(f"Failed to process {file_name}: {str(e)}")



# CANCER
accession_numbers = [
    
     "GSM705467", "GSM705468", "GSM705469", "GSM705470", "GSM705471",
     "GSM705472", "GSM705473", "GSM705475", "GSM705482", "GSM705483",
     "GSM705484", "GSM705485", "GSM705486", "GSM705487", "GSM705488",
     "GSM705648", "GSM705649", "GSM705650", "GSM705651", "GSM705652",
     "GSM705653", "GSM705655", "GSM705657", "GSM705658", "GSM705659",
     "GSM705660", "GSM705661", "GSM705664", "GSM705665", "GSM705673",
     "GSM705712", "GSM705715", "GSM705717", "GSM705787", "GSM705789",
     "GSM705818", "GSM705820", "GSM705821", "GSM705824", "GSM705825",
     "GSM705831", "GSM705832", "GSM705833", "GSM705834", "GSM705835",
     "GSM705836", "GSM705837", "GSM705838", "GSM705839", "GSM705841",
     "GSM705842", "GSM705756", "GSM705759", "GSM705761", "GSM705845",
     "GSM705846", "GSM705848",'GSM705626', 'GSM705654', 'GSM705663', 'GSM705721', 'GSM705722',
     'GSM705741', 'GSM705762', 'GSM705765', 'GSM705776', 'GSM705777',
     'GSM705778', 'GSM705779', 'GSM705844', 'GSM705849', 'GSM705850',
     'GSM705851', 'GSM705852',
     
    'GSM705689', 'GSM705690', 'GSM705691', 'GSM705692', 'GSM705698', 
   'GSM705699', 'GSM705700','GSM705686', 'GSM705688', 'GSM705693', 'GSM705701', 'GSM705702',
     'GSM705703', 'GSM705704', 'GSM705706', 'GSM705707',
     
     'GSM705853', 'GSM705854', 'GSM705855', 'GSM705856', 'GSM705857',
     'GSM705858', 'GSM705859', 'GSM705860', 'GSM705861', 'GSM705862',
     'GSM705863', 'GSM705864', 'GSM705865', 'GSM705866', 'GSM705867',
     'GSM705873', 'GSM705874', 'GSM705875', 'GSM705876', 'GSM705877',
     'GSM705879', 'GSM705880', 'GSM705881', 'GSM705882', 'GSM705883',    
     'GSM705884', 'GSM705885', 'GSM705886', 'GSM705887', 'GSM705888',
     'GSM705891', 'GSM705893', 'GSM705896', 'GSM705897', 'GSM705898',
     'GSM705899', 'GSM705900', 'GSM705901', 'GSM705902', 'GSM705903',
     'GSM705904', 'GSM705905', 'GSM705906', 'GSM705931', 'GSM705933',
     'GSM705934',
       'GSM705476', 'GSM705656', 'GSM705666', 'GSM705675', 'GSM705676', 
     'GSM705677', 'GSM705678', 'GSM705679', 'GSM705680', 'GSM705682', 
     'GSM705683', 'GSM705695', 'GSM705714', 'GSM705718', 'GSM705763', 
     'GSM705764', 'GSM705766', 'GSM705819', 'GSM705823', 'GSM705981',
     
      'GSM705498', 'GSM705499', 'GSM705500', 'GSM705501', 'GSM705502', 
     'GSM705503', 'GSM705504', 'GSM705505', 'GSM705506', 'GSM705507', 
     'GSM705508', 'GSM705510', 'GSM705511', 'GSM705512', 'GSM705513', 
     'GSM705514', 'GSM705515', 'GSM705516', 'GSM705517', 'GSM705518', 
     'GSM705519', 'GSM705520',
      "GSM705536", "GSM705537", "GSM705538", "GSM705539", "GSM705540",
     "GSM705541", "GSM705542", "GSM705543", "GSM705544", "GSM705545",
     "GSM705546", "GSM705547", "GSM705548", "GSM705549", "GSM705550",
     "GSM705551", "GSM705552", "GSM705553", "GSM705554", "GSM705564",
     "GSM705573", "GSM705582", "GSM705593", "GSM705600", "GSM705601",
     "GSM705606", "GSM705614", "GSM705616", "GSM705617", "GSM705619",
     "GSM705622", "GSM705623", "GSM705624", "GSM705625",
     "GSM705627", "GSM705629", "GSM705630", "GSM705631", "GSM705632",
     "GSM705633", "GSM705634", "GSM705635", "GSM705637", "GSM705639",
     "GSM705640", "GSM705641", "GSM705642", "GSM705643", "GSM705644",
     "GSM705645", "GSM705646",
     
     
     
     "GSM705937", "GSM705938", "GSM705939", "GSM705940", "GSM705941",
     "GSM705942", "GSM705943", "GSM705944", "GSM705945", "GSM705946",
     "GSM705947", "GSM705948", "GSM705949", "GSM705950", "GSM705951",
     "GSM705952", "GSM705953", "GSM705954", "GSM705955", "GSM705956",
     "GSM705957", "GSM705961", "GSM705964", "GSM705965", "GSM705966",
     "GSM705967", "GSM705968", "GSM705973", "GSM705974", "GSM705975",
     "GSM705976", "GSM705977", "GSM705978", "GSM705979", "GSM705980",
     "GSM705981", "GSM705982", "GSM705986", "GSM705987", "GSM705990",
     "GSM705991", "GSM705992", "GSM705993", "GSM705994", "GSM705995",
     "GSM705996", "GSM705997", "GSM705998", "GSM705999", "GSM706000",
     "GSM706001", "GSM706002", "GSM706003", "GSM706004", "GSM706005",
     "GSM706007"
]




output_folder = "CANCER"


# Create the output folders if they don't exist
os.makedirs(output_folder, exist_ok=True)


for accession_number in accession_numbers:
    try:
        # Load the dataset from GEO
        gse = GEOparse.get_GEO(geo=accession_number, destdir=output_folder)
        
      
        
        # Save the data to a tab-separated file
        filename = f"{accession_number}.txt"    
       
      
        

        
    except Exception as e:
        print(f"failed to download {accession_number}: {str(e)}")


import os
import csv

input_folder = "CANCER"
output_folder1 = "CANCER_CSV"

# Create the output folder if it doesn't exist
os.makedirs(output_folder1, exist_ok=True)

# Get a list of all text files in the input folder
text_files = [file for file in os.listdir(input_folder) if file.endswith('.txt')]

for file_name in text_files:
    try:
        # Read the contents of the text file, skip first 48 lines
        with open(os.path.join(input_folder, file_name), 'r') as file:
            lines = file.readlines()[48:-1]

        # Write the modified data to a new CSV file in the output folder
        with open(os.path.join(output_folder1, file_name[:-4] + '.csv'), 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            for line in lines:
                writer.writerow(line.strip().split('\t'))

        print(f"Processing completed for {file_name}. Output saved to '{output_folder1}/{file_name[:-4]}.csv'")
    except Exception as e:
        print(f"Failed to process {file_name}: {str(e)}")




