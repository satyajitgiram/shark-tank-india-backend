founders = "Malvica Saxena, , , , ,  "

# Split the string by commas
founders_list = founders.split(",")

# Remove empty elements from the list
founders_list = [founder.strip() for founder in founders_list if founder.strip()]

# Join the list elements back into a string
cleaned_founders = ", ".join(founders_list)

print(cleaned_founders)