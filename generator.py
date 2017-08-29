__author__ = 'akeshavan'
from jinja2 import Environment, FileSystemLoader
import os
import simplejson as json

def load_json(filename):
    """Load data from a json file
    Parameters
    ----------
    filename : str
        Filename to load data from.
    Returns
    -------
    data : dict
    """

    with open(filename, 'r') as fp:
        data = json.load(fp)
    return data


files_to_generate = [{"filename": "index.html.tmpl", "location":"./"},
                    {"filename": "css/stylish-portfolio.css.tmpl", "location": "./"}]

env = Environment(loader=FileSystemLoader('./'))
info = load_json("data.json")

for f in files_to_generate:
    template = env.get_template(f["filename"])
    outfile = os.path.join(f["location"], f["filename"].replace(".tmpl",""))
    print("writing", outfile)
    with open(outfile, "w") as q:
        q.write(template.render(**info))
