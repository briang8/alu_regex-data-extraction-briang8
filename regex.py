import re 
def validate_data(data, pattern):
    return re.match(pattern, data)


data_samples = {
    "email": "user@example.com",
    "url": "https://www.example.com",
    "phone": "(123) 456-7890",
    "hashtag": "#example"
}


patterns = {
    "email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "url": r"^(https?:\/\/)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(\/[a-zA-Z0-9\-._~:/?#[\]@!$&'()*+,;=]*)?$",
    "phone": r"^(\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$",
    "hashtag": r"#([a-zA-Z0-9_]+)"
}


results = {}
for data_type, sample_data in data_samples.items():
    pattern = patterns[data_type]
    match = validate_data(sample_data, pattern)
    results[data_type] = "valid" if match else "invalid"

for data_type, result in results.items():
    print(f"{data_type.capitalize()} validation: {result}")
    