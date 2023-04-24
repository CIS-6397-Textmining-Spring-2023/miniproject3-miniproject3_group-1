import os
import re
corpus_path = "Articles"

article_list = []

# iterate over files in corpus folder
for filename in os.listdir(corpus_path):
    # read in file content
    with open(os.path.join(corpus_path, filename), "r", encoding="utf-8") as file:
        content = file.read()
        
    # split content into articles
    articles = content.split("\n\n\n")  # assuming articles are separated by two newlines
    
    # create article objects
    for article in articles:
        article_obj = {"content": article}  # create dictionary object with "content" key
        if(len(article)!=1):
            article_list.append(article_obj)  # add article object to list
    break
    

# print number of articles and first article content
print(f"Number of articles: {len(article_list)}")

metadata_pattern = r'^([^:\n]+):\s*(.*)$'
metadata = {}
text=article_list[len(article_list)-1]['content']

end_of_metadata_index = text.find("All Rights Reserved.")

# Add the length of "All Rights Reserved." to get the index of the character after it
end_of_metadata_index += len("All Rights Reserved.")

# Use slicing to separate the text into metadata and content
metadata = text[:end_of_metadata_index]
content = text[end_of_metadata_index:-36]

document = text[-36:]
metadata = metadata + '\n' +document



print("Content:")
print(content)
print()
print("Metadata:")
print(metadata)

metadata_dict = {}
lines = metadata.split('\n')
metadata_dict['SpecialSections'] = lines[1].split(';')[0].strip()
metadata_dict['SECTF'] = lines[1].split(';')[1].strip()
metadata_dict['Reporter\'s Note'] = lines[2].strip()
metadata_dict['Author'] = lines[3].split('By')[1].strip()
metadata_dict['Words'] = int(lines[3].split('By')[0].split()[-2])
metadata_dict['Date'] = lines[4].strip()
metadata_dict['Newspaper'] = lines[5].strip()
metadata_dict['NYTF'] = lines[6].strip()
metadata_dict['Edition'] = lines[7].strip()
metadata_dict['Page'] = int(lines[8].strip())
metadata_dict['Language'] = lines[9].strip()
metadata_dict['Copyright'] = lines[10].strip()
metadata_dict['Document'] = lines[11].strip()

print(metadata_dict)