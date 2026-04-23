import json

def load_html_template(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        return content


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal2(animal_obj):
    out_put = ''
    out_put += '<li class="cards__item">'
    out_put += f'<div class="card__title">{animal_obj["name"]}</div>'
    out_put += '<p class="card__text">'
    out_put += f'<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n'
    out_put += f'<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n'
    out_put += f'<strong>Type:</strong> {animal_obj['characteristics']['temperament'].title()}<br/>\n'
    if animal_obj['characteristics'].get('type'):
        out_put += f'<strong>Type:</strong> {animal_obj['characteristics']['type'].title()}<br/>\n'
        out_put += '</p>'
    out_put += '</li>'

    return out_put

def serialize_animal(animal_obj):
    diet = animal_obj['characteristics'].get('diet', 'NA.')
    location = animal_obj['locations'][0]
    temperament = animal_obj['characteristics'].get('temperament', 'NA.').title()
    type_ = animal_obj['characteristics'].get('type', 'NA.').title()
    color = animal_obj['characteristics'].get('color','NA.').title()
    habitat = animal_obj['characteristics'].get('habitat','NA.').title()
    name = animal_obj["name"]

    animal_charact = { 'Diet': diet,
                       'Location': location,
                       'Temperament': temperament,
                       'Type': type_,
                       'Color': color,
                       'Habitat': habitat
                       }

    update_animal_char = [ f'<li class="animal-item"><strong>{key}: </strong>{value}</li>'
                           for key, value in animal_charact.items() if value != 'Na.']
    animals_char_to_html = '\n'.join(update_animal_char)

    out_put = (f'<li class="cards__item">\n<div class="card__title">'
               f'{name}</div>\n<div class ="card__text">\n '
               f'<ul class="animal-list">\n'
               f'{animals_char_to_html}\n'
               f'</ul>\n'
               f'</div>\n'
               f'</li>\n')

    return out_put


def get_animal_info(animals_data):
    out_put = ''
    for animal in animals_data:
        out_put += serialize_animal(animal)
    return out_put


def replace_animals_info(file_path,html_content, filtered_animal_info):
    html_with_animal_list = html_content.replace('__REPLACE_ANIMALS_INFO__', filtered_animal_info )
    with open(file_path, "w") as new_file:
        new_file.write(html_with_animal_list)


def skin_type_filter(animals_data):
    skin_type_set = set()
    for animal in animals_data:
        if animal['characteristics'].get('skin_type') != None:
            skin_type_set.add(animal['characteristics']['skin_type'])
    return skin_type_set

def skin_type_print(animals_data,user_input):
    skin_type_select = [ animal  for animal in animals_data if animal['characteristics'].get('skin_type') == user_input ]
    return skin_type_select

def main():
    html_content = load_html_template('animals_template.html')
    animals_data = load_data('animals_data.json')

    skin_type_list = (skin_type_filter(animals_data))
    print(list(skin_type_list))
    user_input = input('Type one of the skin type from the list or "all": ').title()

    if user_input == 'All':
        filtered_animal_info = get_animal_info(animals_data)
        replace_animals_info("animals.html", html_content, filtered_animal_info)
    elif user_input in skin_type_list:
        selected_animals = skin_type_print(animals_data,user_input)
        filtered_animals_skin = get_animal_info(selected_animals)
        replace_animals_info("selected_animals.html",html_content, filtered_animals_skin )
    else:
        print('Typing was not correct, By by!')

if __name__ == "__main__":
    main()