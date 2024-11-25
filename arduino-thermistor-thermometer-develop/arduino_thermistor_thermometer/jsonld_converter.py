# reading JSON-LD
import json

def jsonld2json(jsonld_dict: dict):
    # Remove the @context key if it exists
    jsonld_dict.pop("@context", None)
    jsonld_dict.pop("comments", None)
    
    # Map JSON-LD "@type" to a "type" field expected by Pydantic
    if "@type" in jsonld_dict:
        jsonld_dict["type"] = jsonld_dict.pop("@type")

    return jsonld_dict


def read_jsonld(file_path: str):
    with open(file_path, 'r') as f:
        jsonld_data = json.load(f)
        return jsonld2json(jsonld_data)