import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import http.client
import json
import Seq1


HTML_FOLDER = "./html/"
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'

GENES = {"FRAT1": "ENSG00000165879",
             "ADA": "ENSG00000196839",
             "FXN": "ENSG00000165060",
             "RNU6_269P": "ENSG00000212379",
             "MIR633": "ENSG00000207552",
             "TTTY4C": "ENSG00000228296",
             "RBMY2YP": "ENSG00000227633",
             "FGFR3": "ENSG00000068078",
             "KDR": "ENSG00000128052",
             "ANK2": "ENSG00000145362"}

names = GENES.keys()
NAMES_LIST = []
for n in names:
    NAMES_LIST.append(n)


def read_html_file(filename):

    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents


def make_ensembl_request(url,params):

    conn = http.client.HTTPConnection(SERVER)
    parameters = '?content-type=application/json'

    try:
       conn.request("GET", url + parameters + params)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()


    print(f"Response received!: {r1.status} {r1.reason} \n")

    data1 = r1.read().decode('utf-8')


    our_dict = json.loads(data1)
    return our_dict



PORT = 8080


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)

        if self.path == "/":
            contents = read_html_file(HTML_FOLDER + "index.html")\
                .render(context={"n_names": NAMES_LIST})

#BASIC LEVEL:

        elif path == "/list_species":
            dict_answer = make_ensembl_request("/info/species", "")
            species_all = dict_answer["species"]
            selected_species = []

            try:
                try:
                    try:
                        limit = int(arguments["limit"][0])
                        for i in range(0, limit):
                            selected_species.append(species_all[i]["common_name"])

                        if "json" in arguments:
                            contents = {
                                "species": selected_species,
                                "n_species": len(species_all),
                                "limit": limit}

                        else:
                            contents = read_html_file(HTML_FOLDER + path[1:] + ".html") \
                                .render(context={
                                "species": selected_species,
                                "n_species": len(species_all),
                                "limit": limit
                                })
                    except ValueError:
                        contents = read_html_file(HTML_FOLDER + "error.html") \
                            .render()

                except KeyError:
                    for i in range(0, len(species_all)):
                        selected_species.append(species_all[i]["common_name"])

                    contents = read_html_file(HTML_FOLDER + path[1:] + ".html") \
                        .render(context={
                        "species": selected_species})

            except IndexError:
                contents = read_html_file(HTML_FOLDER + "error.html") \
                    .render()

        elif path == "/karyotype":
            try:
                specie = str(arguments['specie'][0].strip())
                dict_answer = make_ensembl_request("/info/assembly/" + specie, "")

                info_all = dict_answer["karyotype"]

                if "json" in arguments:
                    contents = {"karyotype": info_all}

                else:
                    contents = read_html_file(HTML_FOLDER + path[1:] + ".html") \
                        .render(context={
                        "karyotype": info_all})

            except KeyError:
                contents = read_html_file(HTML_FOLDER + "error.html") \
                    .render()

        elif path == "/chromosomeLength":
            try:

                specie = str(arguments['specie'][0].strip())
                dict_answer = make_ensembl_request("/info/assembly/" + specie, "")
                try:
                    length_chromo = int(arguments['length'][0].strip())
                    dict_all = dict_answer["top_level_region"]
                    names_chromo = []
                    for i in range(0,len(dict_all)):
                        names_chromo.append(dict_all[i]["name"])

                    if length_chromo >= 0:

                        l_chromo = []
                        for i in range(0,len(dict_all)):
                            l_chromo.append(dict_all[i]["length"])
                        largest_length = max(l_chromo)

                        if length_chromo <= largest_length:

                            wanted_dict = dict(zip(l_chromo, names_chromo))
                            wanted_lengths = []

                            for l in l_chromo:
                                if l >= length_chromo:
                                    wanted_lengths.append(l)

                            list_chromosomes = []
                            for c in wanted_lengths:
                                list_chromosomes.append(wanted_dict[c])

                            print(list_chromosomes)

                            if "json" in arguments:
                                contents = {"l": length}
                            else:
                                contents = read_html_file(HTML_FOLDER + path[1:] + ".html") \
                                    .render(context={
                                    "list_c": list_chromosomes})

                        else:
                            contents = read_html_file(HTML_FOLDER + "error.html") \
                                .render()

                    else:
                        contents = read_html_file(HTML_FOLDER + "error.html") \
                            .render()

                except ValueError:
                    contents = read_html_file(HTML_FOLDER + "error.html") \
                        .render()

            except KeyError:
                contents = read_html_file(HTML_FOLDER + "error.html") \
                    .render()


#MEDIUM LEVEL:

        elif path == "/geneSeq":
            gene = str(arguments['seq'][0].strip())
            key = GENES[gene]
            dict_answer = make_ensembl_request("/sequence/id/" + str(key), "")
            sequence = dict_answer["seq"]
            if "json" in arguments:
                contents = {
                    "g": sequence,
                    "n": NAMES_LIST
                }
            else:
                contents = read_html_file(HTML_FOLDER + path[1:] + ".html") \
                    .render(context={
                    "g": sequence,
                    "n": NAMES_LIST
                })

        elif path == "/geneInfo":
            gene = str(arguments['info'][0].strip())
            key = GENES[gene]
            dict_answer = make_ensembl_request("/sequence/id/" + str(key), "")
            description = dict_answer["desc"].split(":")
            length = int(description[4]) - int(description[3])
            if "json" in arguments:
                contents = {
                    "start": description[3],
                    "end": description[4],
                    "chromosome_n": description[2],
                    "n": gene,
                    "id": key,
                    "l": length
                }

            else:

                contents = read_html_file(HTML_FOLDER + path[1:] + ".html") \
                    .render(context={
                    "start": description[3],
                    "end": description[4],
                    "chromosome_n": description[2],
                    "n": gene,
                    "id": key,
                    "l": length
                })

        elif path == "/geneCalc":
            gene = str(arguments['calc'][0].strip())
            key = GENES[gene]

            dict_answer = make_ensembl_request("/sequence/id/" + str(key) , "")

            sequence = dict_answer["seq"]

            s = Seq1.Seq(sequence)

            if "json" in arguments:
                contents = {
                    "length": s.len(),
                    "p": s.info()
                }

            else:

                contents = read_html_file(HTML_FOLDER + path[1:] + ".html") \
                    .render(context={
                    "length": s.len(),
                    "p": s.info()
                })


        elif path == "/geneList":

            try:

                specie = str(arguments['specie'][0].strip())
                name = str(arguments['name_chromo'][0].strip())
                s = str(arguments['start'][0].strip())
                e = str(arguments['end'][0].strip())
                desc = name + ":" + s + "-" + e
                dict_answer = make_ensembl_request("/phenotype/region/" + specie + "/" + desc, "")

                if len(dict_answer) > 0:

                    gene_result = []
                    for i in range(0,len(dict_answer)):
                        for c in dict_answer[i]["phenotype_associations"]:
                            if "attributes" in c:
                                if "associated_gene" in c["attributes"]:
                                    gene_result.append(c["attributes"]["associated_gene"])
                    if "json" in arguments:
                        contents ={
                            "n_g": gene_result
                        }
                    else:
                        contents = read_html_file(HTML_FOLDER + path[1:] + ".html") \
                            .render(context={
                            "n_g": gene_result
                        })

                elif len(dict_answer) == 0:

                    contents = read_html_file(HTML_FOLDER + "error.html") \
                        .render()

            except KeyError:
                contents = read_html_file(HTML_FOLDER + "error.html") \
                    .render()


        else:
            contents = "I am the happy server! :-)"



        self.send_response(200)


        if not "json" in arguments:
            self.send_header('Content-Type', 'text/html')
        elif "json" in arguments:
            print(contents)
            contents = json.dumps(contents)
            self.send_header('Content-Type', 'application/json')


        self.send_header('Content-Length', len(contents.encode()))


        self.end_headers()


        self.wfile.write(contents.encode())

        return



Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)


    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

