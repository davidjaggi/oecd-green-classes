# OECD Green IPC Patent Mapping

The following article explains how the corresponding classes of IPC and CPC can be combined in order to be able to combine them with other datasets later on. 
The aim of this project is to create a dataset that allows for a statistical mapping between the green IPC and CPC classifications based on the OECD green technologies.

The contained classification can be enhanced using the Y02 classes.

## OECD Environmental Technologies
In principle, the method is based on the paper called "Measuring environmental innovation using patent data" by [Hascic and Migotto from 2015](https://ideas.repec.org/p/oec/envaaa/89-en.html). The paper contains a table in the appendix which lists the so-called "Search Strategies for the Identification of Selected Environment-Related Technologies (ENV-TECH)". For the corresponding tables, the corresponding IPC or CPC class is given.

In a first step, I converted the table into an [Excel file](data/env_tech.xlsx) so that I could process it further using Python at a later stage. The Excel table can be found in the GitHub repository with the corresponding code.

Also included is an XML file that allows for a [statistical mapping between the IPC and CPC classifications](https://www.epo.org/searching-for-patents/helpful-resources/first-time-here/classification/cpc/ipccpc.html).
For this first iteration I used all of the available mappings. In a second step, I will try to filter out the mappings that are not relevant for the IPC classification based on a specific level.

The final dataset [env_tech_cpc.pkl](data/env_tech_cpc.pkl) contains the following columns.

| Column Name         | Description                                |
| ------------------- | ------------------------------------------ |
| Level 1             | First level of the patent search strategy  |
| Level 2             | Second level of the patent search strategy |
| Level 3             | Third level of the patent search strategy  |
| Description         | Description of the technology              |
| IPC and CPC Classes | Mixed classification codes                 |
| Extended Classes    | Classes without implicit ranges            |
| Green CPC           | CPC mapped classes                         |

Please open an issue if you have any questions or suggestions.
