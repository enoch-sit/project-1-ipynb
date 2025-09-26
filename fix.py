import json

# Load the notebook JSON with UTF-8 encoding
with open('DataRetrieval.json', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Check and fix metadata.widgets
if 'metadata' in notebook and 'widgets' in notebook['metadata']:
    widgets = notebook['metadata']['widgets']
    for format_name in list(widgets.keys()):  # e.g., 'application/vnd.jupyter.widget-state+json'
        format_dict = widgets[format_name]
        if 'state' not in format_dict:
            # Collect all keys that look like widget IDs (hex strings, not version keys)
            state_keys = {k: v for k, v in format_dict.items() if k not in ['version_major', 'version_minor']}
            # Add empty 'state' if no states, or move existing ones
            format_dict['state'] = state_keys or {}
            # Remove the direct ID keys if they were moved
            for k in state_keys:
                del format_dict[k]
            print(f"Added/restructured 'state' for {format_name}")

# Save the fixed notebook as .ipynb with UTF-8 encoding
with open('fixed_DataRetrieval.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)  # ensure_ascii=False preserves non-ASCII chars

print("Fixed notebook saved as 'fixed_DataRetrieval.ipynb'. Try rendering it now.")