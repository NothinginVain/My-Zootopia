import json

def load_html_template(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        return content

html_content = load_html_template('animals_template.html')

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')


def get_animal_info():
    out_put = ''
    for animal in animals_data:
        out_put += f"Name: {animal['name']}\n"
        out_put += f"Diet: {animal['characteristics']['diet']}\n"
        out_put += f"Location: {animal['locations'][0]}\n"
        if animal['characteristics'].get('type'):
            out_put += f"Type: {animal['characteristics']['type'].title()}\n "
        out_put += f"\n"
    return out_put

filtered_animal_info = get_animal_info()


def replace_animals_info(file_path):
    html_with_animal_list = html_content.replace('__REPLACE_ANIMALS_INFO__', filtered_animal_info )
    with open(file_path, "w") as new_file:
        new_file.write(html_with_animal_list)

replace_animals_info("animals.html")