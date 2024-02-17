from datasets import load_dataset
import json
import matplotlib.pyplot as plt
import os


datasets = load_dataset("Norod78/RickAndMorty-HorizontalMirror-blip-captions")

print(datasets['train'])

my_dataset = datasets["train"]

# Define the output JSON file path
output_json_path = 'output.json'

# Create a list to store the formatted data
json_data = []

# Iterate through the dataset and format the data
for i in range(len(my_dataset)):
    image_file = f"{i}.png"
    text = my_dataset['text'][i]

    data_point = {
        'image_file': image_file,
        'text': text
    }

    json_data.append(data_point)

# Write the formatted data to a JSON file
with open(output_json_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON file created successfully at {output_json_path}")

output_dir = 'dataset'
os.makedirs(output_dir, exist_ok=True) # create output directory if it doesn't exist

for i in range(0,529):
# Construct the full filename with path
  filename = os.path.join(output_dir, f'{i}.png')

  # Save the image to disk
  datasets['train'][i]['image'].save(filename)
  print(f"Saved image to {filename}")