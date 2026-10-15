#! /usr/bin/env python3

import kgExplorer # retrieve from https://gitlab.com/odameron/kgExplorer

# https://github.com/BioPAX/Paxtools/blob/master/pattern/src/main/resources/org/biopax/paxtools/pattern/miner/blacklist-names.txt
moleculeFromBlacklistNames = set(["CHEBI:15377", "CHEBI:24636", "CHEBI:15378", "CHEBI:15379", "CHEBI:57783", "CHEBI:13392", "CHEBI:16474", "CHEBI:58349","CHEBI:18009", "CHEBI:13390", "CHEBI:25523", "CHEBI:25524", "CHEBI:30616", "CHEBI:15422", "CHEBI:16761", "CHEBI:456216", "CHEBI:57945", "CHEBI:16908","CHEBI:57540", "CHEBI:15846", "CHEBI:16526", "CHEBI:29888", "CHEBI:35782", "CHEBI:68836", "CHEBI:18361", "CHEBI:43474", "CHEBI:35780", "CHEBI:18367", "CHEBI:26078", "CHEBI:77740", "CHEBI:28931", "CHEBI:58307", "CHEBI:17877", "CHEBI:17552", "CHEBI:58189", "CHEBI:37565", "CHEBI:15996"])

# https://github.com/BioPAX/Paxtools/blob/master/pattern/src/test/resources/org/biopax/paxtools/pattern/blacklist.txt
moleculeFromBlacklist = set([ "CHEBI:13389", "CHEBI:13390", "CHEBI:13392", "CHEBI:15346", "CHEBI:15351", "CHEBI:15356", "CHEBI:15361", "CHEBI:15377", "CHEBI:15378", "CHEBI:15379", "CHEBI:15414", "CHEBI:15422", "CHEBI:15428", "CHEBI:15846", "CHEBI:15996", "CHEBI:16015", "CHEBI:16027", "CHEBI:16134", "CHEBI:16238", "CHEBI:16240", "CHEBI:16467", "CHEBI:16474", "CHEBI:16526", "CHEBI:16680", "CHEBI:16761", "CHEBI:16810", "CHEBI:16856", "CHEBI:16908", "CHEBI:17200", "CHEBI:17361", "CHEBI:17552", "CHEBI:17561", "CHEBI:17659", "CHEBI:17925", "CHEBI:17980", "CHEBI:17985", "CHEBI:18009", "CHEBI:18367", "CHEBI:25524", "CHEBI:29016", "CHEBI:29888", "CHEBI:29985", "CHEBI:30031", "CHEBI:30616", "CHEBI:30915", "CHEBI:32551", "CHEBI:32682", "CHEBI:32863", "CHEBI:35235", "CHEBI:35780", "CHEBI:37565", "CHEBI:4208", "CHEBI:45212", "CHEBI:456215", "CHEBI:456216", "CHEBI:46911", "CHEBI:51381", "CHEBI:57287", "CHEBI:57288", "CHEBI:57540", "CHEBI:57783", "CHEBI:57856", "CHEBI:57925", "CHEBI:57945", "CHEBI:58052", "CHEBI:58189", "CHEBI:58223", "CHEBI:58339", "CHEBI:58343", "CHEBI:58349", "CHEBI:59789", "CHEBI:60377", "CHEBI:68836" ])

print("Nb ChEBI molecules in blacklist.txt: {}".format(len(moleculeFromBlacklist)))
print("Nb ChEBI molecules in blacklist-names.txt: {}".format(len(moleculeFromBlacklistNames)))

print()
print("Nb ChEBI molecules in union: {}".format(len(moleculeFromBlacklist.union(moleculeFromBlacklistNames))))
print("Nb ChEBI molecules in intersection: {}".format(len(moleculeFromBlacklist.intersection(moleculeFromBlacklistNames))))
print("Nb ChEBI molecules in blacklist.txt but NOT in blacklist-names.txt: {}".format(len(moleculeFromBlacklist.difference(moleculeFromBlacklistNames))))
print("Nb ChEBI molecules in blacklist-names.txt but NOT in blacklist.txt: {}".format(len(moleculeFromBlacklistNames.difference(moleculeFromBlacklist))))

print()
print("blacklist.txt")
print("\"{}\"".format("\", \"".join(list(moleculeFromBlacklist))))
print()
print("blacklist-names.txt")
print("\"{}\"".format("\", \"".join(list(moleculeFromBlacklistNames))))
print()
print("union")
print("\"{}\"".format("\", \"".join(list(moleculeFromBlacklist.union(moleculeFromBlacklistNames)))))



explorer = kgExplorer.KgExplorer("http://localhost:3030/chebi")
explorer.addPrefix("CHEBI", "http://purl.obolibrary.org/obo/CHEBI_")
g = None
for molecule in moleculeFromBlacklist.difference(moleculeFromBlacklistNames):
    g = explorer.addAncestorsHierarchyToGraph(molecule, graph=g, transitive=True, labelRelationList=["rdfs:label"], highlightClassURI=True, highlightColorBorder="#ff0000", highlightColorFill="#ffbbbb")
    g = explorer.addDescendantsHierarchyToGraph(molecule, graph=g, transitive=True, labelRelationList=["rdfs:label"], highlightClassURI=True, highlightColorBorder="#ff0000", highlightColorFill="#ffbbbb")

for molecule in moleculeFromBlacklistNames.difference(moleculeFromBlacklist):
    g = explorer.addAncestorsHierarchyToGraph(molecule, graph=g, transitive=True, labelRelationList=["rdfs:label"], highlightClassURI=True, highlightColorBorder="#0000ff", highlightColorFill="#bbbbff")
    g = explorer.addDescendantsHierarchyToGraph(molecule, graph=g, transitive=True, labelRelationList=["rdfs:label"], highlightClassURI=True, highlightColorBorder="#0000ff", highlightColorFill="#bbbbff")

for molecule in moleculeFromBlacklist.intersection(moleculeFromBlacklistNames):
    g = explorer.addAncestorsHierarchyToGraph(molecule, graph=g, transitive=True, labelRelationList=["rdfs:label"], highlightClassURI=True, highlightColorBorder="#ff00ff", highlightColorFill="#ffbbff")
    g = explorer.addDescendantsHierarchyToGraph(molecule, graph=g, transitive=True, labelRelationList=["rdfs:label"], highlightClassURI=True, highlightColorBorder="#ff00ff", highlightColorFill="#ffbbff")

g.draw(path="chebi-blacklist-paxtools.svg", format="svg", prog="dot")
g.write(path="chebi-blacklist-paxtools.dot")
