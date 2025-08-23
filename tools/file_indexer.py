import os
from datetime import datetime, timezone

def index_files(path):
  files = []
  for root, _, filenames in os.walk(path):
    for filename in filenames:
      if not filename.endswith("html"):
        files.append(os.path.join(root, filename))
  return files


def create_file_index(dir: str):
    out_file = os.path.join(dir, "index.html")
    template = "<html><head><meta charset='UTF-8'><link rel='stylesheet' href='../styles/glob.css'></head><body><main>{}</main></body></html>"

    out = ""
    files = index_files(dir)
    for file in files:
        rel_path = os.path.relpath(file, dir)
        mod_time = datetime.fromtimestamp(os.path.getmtime(file), tz=timezone.utc).strftime('%Y/%m/%d %H:%M:%S UTC')
        out += f"<a href='{rel_path}'>{os.path.basename(file)}</a> - {mod_time}<br />"

    out = template.format(out)
    with open(out_file, "w") as f:
        f.write(out)

create_file_index("templates")
