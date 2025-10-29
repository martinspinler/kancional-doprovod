import os
import json

for i in ["ly", "log_ly", "musicxml", "pdf", "pdf_crop", "pdf_tmp", "song_data", "tex"]:
    try:
        os.mkdir(f"../{i}")
    except:
        pass

with open("selection_candidate.json", "r") as f:
    songs = json.load(f)

for i in songs:
    url = "https://www.karlin.mff.cuni.cz/~slavika/kanc_render/"

    datafn = f"{i}.json"
    if not os.path.isfile(f"../song_data/{datafn}"):
        os.system(f"wget {url}song_data/{datafn} -O ../song_data/{datafn}")

    with open(f"../song_data/{datafn}", "r", encoding="utf-8") as f:
        jf = json.load(f)
        stanzas = jf["stanzas"]
        stanza_lengths = jf["stanza_lengths"]

    for s in stanza_lengths:
        xmlfn = f"{i}-{s}.xml"
        if not os.path.isfile(f"../musicxml/{xmlfn}"):
            os.system(f"wget {url}musicxml/{xmlfn} -O ../musicxml/{xmlfn}")

with open("../ly_templates/pocty_systemu.tsv", "w") as f:
    #for s in songs:
    #    f.write(f"{s}   1")
    f.close()
