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


def serialize_animal(animal_obj):
    out_put = ''
    out_put += '<li class="cards__item">'
    out_put += f'<div class="card__title">{animal_obj["name"]}</div>'
    out_put += '<p class="card__text">'
    out_put += f'<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n'
    out_put += f'<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n'
    if animal_obj['characteristics'].get('type'):
        out_put += f'<strong>Type:</strong> {animal_obj['characteristics']['type'].title()}<br/>\n'
        out_put += '</p>'
    out_put += '</li>'

    return out_put


def get_animal_info():
    out_put = ''
    for animal in animals_data:
        out_put += serialize_animal(animal)
    return out_put

filtered_animal_info = get_animal_info()


def replace_animals_info(file_path):
    html_with_animal_list = html_content.replace('__REPLACE_ANIMALS_INFO__', filtered_animal_info )
    with open(file_path, "w") as new_file:
        new_file.write(html_with_animal_list)

replace_animals_info("animals.html")