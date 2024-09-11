# Sample input text
text_data = """
department is : Department of Biochemistry
Name is : Prof. Pawan Kumar Maurya
Designation is : Professor
Department is : Department of Biochemistry
Contact number is : 9560869477
Official email is : hodbiochem@cuh.ac.in
---------
department is : Department of Biotechnology
Name is : Dr. Rupesh Deshmukh
Designation is : Associate Professor
Department is : Department of Biotechnology
Contact number is : 9650792638
Official email is : hodbiotechnology@cuh.ac.in
"""

# Split the text into individual entries
entries = text_data.strip().split("---------")
file = open("output.txt", "a")

def process_entry(entry):
    lines = entry.strip().split("\n")
    data = {}
    for line in lines:
        if "is :" in line:
            key, value = line.split("is :")
            data[key.strip()] = value.strip()
    return data

# Define the header and footer for the format
header = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>You are an AI assistant that provides information about academic departments.<|eot_id|><|start_header_id|>user<|end_header_id|>Can you present the department information in a table format?<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
footer = "<|eot_id|><|end_of_text|>"

# Construct the table for each entry
tables = []
for entry in entries:
    data = process_entry(entry)
    table_header = "| Field | Information |\n|-------|-------------|"
    table_rows = "\n".join([
        f"| Department | {data['department']} |",
        f"| Name | {data['Name']} |",
        f"| Designation | {data['Designation']} |",
        f"| Contact number | {data['Contact number']} |",
        f"| Official email | {data['Official email']} |"
    ])
    tables.append(f"{table_header}\n{table_rows}")

# Combine everything into the final output
output = f"{header}\n\n" + "\n\n".join(tables) + f"\n\n{footer}"

# Print the output to the console
print(output)

# Optionally, write the output to a file
with open("department_info_output.txt", "w") as file:
    file.write(output)

print("Formatted data saved to department_info_output.txt")
