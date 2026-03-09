# BioPAX to SIF abstraction in SPARQL

This repository contains SPARQL queries for abstraction BioPAX (Biological Pathway Exchange) data to SIF (Simple Interaction Format).

We identified three meanings of description of SIF abstraction rules: 
- Meaning 1: SIF rules diagrams and associated textual descriptions from PathwayCommons (https://www.pathwaycommons.org/pc2/formats)
- Meaning 2: Textual descriptions associated to SIF Paxtools patterns
- Meaning 3: Paxtools patterns codes

For each meaning of description, we implemented a SPARQL query for each one of the 14 SIF rules.
These queries can be found in the following folders: 
- `Scripts/Meaning1-SIFAbstraction/Meaning1-SPARQLQueries`
- `Scripts/Meaning2-SIFAbstraction/Meaning2-SPARQLQueries`
- `Scripts/Meaning3-SIFAbstraction/Meaning3-SPARQLQueries`

In the `Scripts` folder, we also provide Jupyter notebboks that execute the SPARQL queries on the BioPAX exports of Reactome (version 95, December 2025) and PathBank (PathwayCommons, last updated 2019) for the three meanings of description:

### References

- E. Demir et al., “Using Biological Pathway Data with Paxtools,” PLoS Comput Biol, vol. 9, no. 9, p. e1003194, Sep. 2013, doi: 10.1371/journal.pcbi.1003194.
- E. G. Cerami et al., “Pathway Commons, a web resource for biological pathway data,” Nucleic Acids Res, vol. 39, no. Database issue, pp. D685-690, Jan. 2011, doi: 10.1093/nar/gkq1039.
- B. Jassal et al., “The reactome pathway knowledgebase,” Nucleic Acids Res, vol. 48, no. D1, pp. D498–D503, Jan. 2020, doi: 10.1093/nar/gkz1031.
- D. S. Wishart et al., “PathBank: a comprehensive pathway database for model organisms,” Nucleic Acids Res, vol. 48, no. D1, pp. D470–D478, Jan. 2020, doi: 10.1093/nar/gkz861.