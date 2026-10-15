#! /usr/bin/env python3

import kgExplorer # retrieve from https://gitlab.com/odameron/kgExplorer

explorer = kgExplorer.KgExplorer("http://localhost:3030/chebi")
explorer.addPrefix("CHEBI", "http://purl.obolibrary.org/obo/CHEBI_")

moleculeBlackList = ["CHEBI:15377", "CHEBI:24636", "CHEBI:15378", "CHEBI:15379", "CHEBI:57783", "CHEBI:13392", "CHEBI:16474", "CHEBI:58349","CHEBI:18009", "CHEBI:13390", "CHEBI:25523", "CHEBI:25524", "CHEBI:30616", "CHEBI:15422", "CHEBI:16761", "CHEBI:456216", "CHEBI:57945", "CHEBI:16908","CHEBI:57540", "CHEBI:15846", "CHEBI:16526", "CHEBI:29888", "CHEBI:35782", "CHEBI:68836", "CHEBI:18361", "CHEBI:43474", "CHEBI:35780", "CHEBI:18367", "CHEBI:26078", "CHEBI:77740", "CHEBI:28931", "CHEBI:58307", "CHEBI:17877", "CHEBI:17552", "CHEBI:58189", "CHEBI:37565", "CHEBI:15996"]

print("Nb moecules in blacklist: {}".format(len(moleculeBlackList)))

g = None
for molecule in moleculeBlackList:
    g = explorer.addAncestorsHierarchyToGraph(molecule, graph=g, transitive=True, labelRelationList=["rdfs:label"], highlightClassURI=True, highlightColorBorder="#ff0000", highlightColorFill="#ffbbbb")
    g = explorer.addDescendantsHierarchyToGraph(molecule, graph=g, transitive=True, labelRelationList=["rdfs:label"], highlightClassURI=True, highlightColorBorder="#ff0000", highlightColorFill="#ffbbbb")

g.draw(path="chebi-blacklist-SIFrules.svg", format="svg", prog="dot")
g.write(path="chebi-blacklist-SIFrules.dot")