def replace_special_chars(text):
    return text.replace(" ", ":").replace(",", ":").replace(".", ":")

input_text = "Hello, kak dela. Normalno,a u tebya."
output_text = replace_special_chars(input_text)
print(output_text)