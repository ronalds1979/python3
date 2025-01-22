# Double quotes around strings that are used for interpolation or that are natural language messages, and 
# Single quotes for small symbol-like strings, but will break the rules if the strings contain quotes, or if I forget. 
# Triple double quotes for docstrings and raw string literals for regular expressions even if they aren't needed.

# import re regular expression module to be used in the function is_pirate
import re

# Dictionary Definition
# LIGHT_MESSAGES is a dictionary that contains two language-specific messages.
# The keys are the language names ('English' and 'Pirate'), and 
# the values are strings that include a placeholder %(number_of_lights)s. 
# This placeholder will be replaced with an actual number when the string is formatted.
LIGHT_MESSAGES = {
    'English': "There are %(number_of_lights)s lights.",
    'Pirate':  "Arr! Thar be %(number_of_lights)s lights."
}

# Function Definition: lights_message
# Function Purpose: This function takes two parameters: language (a string indicating the desired language) and 
# number_of_lights (an integer representing the count of lights).
#LIGHT_MESSAGES[language]: This retrieves the appropriate message based on the provided language.
# % locals(): This part uses the old-style string formatting in Python. 
# The locals() function returns a dictionary of the current local symbol table, which includes all local variables. Thus, %(number_of_lights)s in the string will be replaced by the value of the number_of_lights variable passed to the function.
def lights_message(language, number_of_lights):
    """Return a language-appropriate string reporting the light count."""
    return LIGHT_MESSAGES[language] % locals()

# Function Definition: is_pirate
#
# Function Purpose: This function checks if a given message contains any words that are commonly associated 
# with pirate speak.
#
# re.search(...): This uses the re (regular expression) module to search for specific patterns in the input 
# message.
# The pattern r"(?i)(arr|avast|yohoho)!" looks for the words "arr", "avast", or "yohoho" in a 
# case-insensitive manner (due to (?i)).
# The function returns True if any of these words are found in the message; otherwise, it returns False.
def is_pirate(message):
    """Return True if the given message sounds piratical."""
    return re.search(r"(?i)(arr|avast|yohoho)!", message) is not None

# Example Usage of lights_message
print(lights_message('English', 5))  # Output: "There are 5 lights."
print(lights_message('Pirate', 3))    # Output: "Arr! Thar be 3 lights."

# Example Usage of is_pirate
print(is_pirate("Arr! We are sailing!"))  # Output: True
print(is_pirate("Hello there!"))           # Output: False