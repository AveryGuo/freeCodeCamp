def add_setting(setting_dictionary, kv_tuple):
    key, value = kv_tuple
    key = key.lower()
    value = value.lower()
    if key in setting_dictionary.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting_dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(setting_dictionary, kv_tuple):
    key, value = kv_tuple
    key = key.lower()
    value = value.lower()
    if key in setting_dictionary.keys():
        setting_dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(setting_dictionary, key):
    key = key.lower()
    if key in setting_dictionary.keys():
        del setting_dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"


def view_settings(setting_dictionary):
    if len(setting_dictionary) != 0:
        setting_str = 'Current User Settings:\n'
        for key, value in setting_dictionary.items():
            key = key.capitalize()
            setting_str += f'{key}: ' + f'{value}\n'
        return setting_str
    else:
        return 'No settings available.'        


test_settings  = {
    'theme': 'light'
}

add_setting(test_settings, ('THEME', 'dark'))
add_setting(test_settings, ('volume', 'high'))

update_setting(test_settings, ('theme', 'dark'))
update_setting(test_settings, ('volume', 'high'))

delete_setting(test_settings, 'theme')
delete_setting(test_settings, 'notfound')

view_settings({})
view_settings(test_settings)





