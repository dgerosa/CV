import numpy as np
import sys,os

import json

papers = {}
submitted = True
published = True
proceedings = True
others = True

talks  = {}
conferences= True
seminars = True
lectures = True
posters = True
outreach = True

if submitted:

    papers['submitted'] = {}
    papers['submitted']['label'] = 'Submitted papers'
    papers['submitted']['data'] = []

    papers['submitted']['data'].append({
        "title":    "Sampling the full hierarchical population posterior distribution in gravitational-wave astronomy",
        "author":   "M. Mancarella, D. Gerosa",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2502.12156 [gr-qc]",
        "ads":      "2025arXiv250212156M",
        "inspire":  "Mancarella:2025uat",
        "more":     ""
        })

    papers['submitted']['data'].append({
        "title":    "SFTs: a scalable data-analysis framework for long-duration gravitational-wave signals",
        "author":   "R. Tenorio, D. Gerosa",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2502.11823 [gr-qc]",
        "ads":      "2025arXiv250211823T",
        "inspire":  "Tenorio:2025yca",
        "more":     ""
        })

    papers['submitted']['data'].append({
        "title":    "Non-adiabatic dynamics of eccentric black-hole binaries in post-Newtonian theory",
        "author":   "G. Fumagalli, N. Loutrel, D. Gerosa, M. Boschini",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2502.06952 [gr-qc]",
        "ads":      "2025arXiv250206952F",
        "inspire":  "Fumagalli:2025rhc",
        "more":     ""
        })

    papers['submitted']['data'].append({
        "title":    "A confirmed recoiling supermassive black hole in a powerful quasar",
        "author":   "M. Chiaberge, T. Morishita, M. Boschini, S. Bianchi, A. Capetti, G. Castignani, D. Gerosa, M. Konishi, S. Koyama, K. Kushibiki, E. Lambrides, E. T. Meyer, K. Motohara, M. Stiavelli, H. Takahashi, G. R. Tremblay, C. Norman",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2501.18730 [astro-ph.GA]",
        "ads":      "2025arXiv250118730C",
        "inspire":  "Chiaberge:2025ouh",
        "more":     ""
        })

    papers['submitted']['data'].append({
        "title":    "Reconstructing parametric gravitational-wave population fits from non-parametric results without refitting the data.",
        "author":   "C. M. Fabbri, D. Gerosa, A. Santini, M. Mould, A. Toubiana, J. Gair",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2501.17233 [astro-ph.HE]",
        "ads":      "2025arXiv250117233F",
        "inspire":  "Fabbri:2025faf",
        "more":     ""
        })

    papers['submitted']['data'].append({
        "title":    "A test for LISA foreground Gaussianity and stationarity. I. Galactic white-dwarf binaries.",
        "author":   "R. Buscicchio, A. Klein, V. Korol, F. Di Renzo, C. J. Moore, D. Gerosa, A. Carzaniga",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2410.08263 [astro-ph.HE]",
        "ads":      "2024arXiv241008263B",
        "inspire":  "Buscicchio:2024wwm",
        "more":     ""
        })

    papers['submitted']['data'].append({
        "title":    "The last three years: multiband gravitational-wave observations of stellar-mass binary black holes",
        "author":   "A. Klein, G. Pratten, R. Buscicchio, P. Schmidt, C. J. Moore, E. Finch, A. Bonino, L. M. Thomas, N. Williams, D. Gerosa, S. McGee, M. Nicholl, A. Vecchio",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2204.03423 [gr-qc]",
        "ads":      "2022arXiv220403423K",
        "inspire":  "Klein:2022rbf",
        "more":     ""
        })


if published:
    papers['published'] = {}
    papers['published']['label'] = 'Papers in major peer-reviewed journals'
    papers['published']['data'] = []
    
    papers['published']['data'].append({
        "title":    "Which is which? Identification of the two compact objects in gravitational-wave binaries",
        "author":   "D. Gerosa, V. De Renzis, F. Tettoni, M. Mould, A. Vecchio, C. Pacilio.",
        "journal":  "\prl 134 (2025) 121402",
        "link":     "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.134.121402",
        "arxiv":    "arXiv:2409.07519 [astro-ph.HE]",
        "ads":      "2024arXiv240907519G",
        "inspire":  "Gerosa:2024ojv",
        "more":     "PRL Editors' Suggestion. Covered by press release"
        })

    papers['published']['data'].append({
        "title":    "Forecasting the population properties of merging black holes",
        "author":   "V. De Renzis, F. Iacovelli, D. Gerosa, M. Mancarella, C. Pacilio",
        "journal":  "\prd 111 (2025) 044048.",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.044048",
        "arxiv":    "arXiv:2410.17325 [astro-ph.HE]",
        "ads":      "2025PhRvD.111d4048D",
        "inspire":  "DeRenzis:2024dvx",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Orbital eccentricity in general relativity from catastrophe theory",
        "author":   "M. Boschini, N. Loutrel, D. Gerosa, G. Fumagalli",
        "journal":  "\prd 111 (2025) 024008",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.024008",
        "arxiv":    "arXiv:2411.00098 [gr-qc]",
        "ads":      "2025PhRvD.111b4008B",
        "inspire":  "Boschini:2024scu",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Stars or gas? Constraining the hardening processes of massive black-hole binaries with LISA",
        "author":   "A. Spadaro, R. Buscicchio, D. Izquierdo-Villalba, D. Gerosa, A. Klein, G. Pratten",
        "journal":  "\prd 111 (2025) 023004 ",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.023004",
        "arxiv":    "arXiv:2409.13011 [astro-ph.HE]",
        "ads":      "2025PhRvD.111b3004S",
        "inspire":  "Spadaro:2024tve",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Probing AGN jet precession with LISA",
        "author":   "N. Steinle, D. Gerosa, M. G. H. Krause",
        "journal":  "\prd 110 (2024) 123034",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.110.123034",
        "arxiv":    "arXiv:2403.00066 [astro-ph.HE]",
        "ads":      "2024PhRvD.110l3034S",
        "inspire":  "Steinle:2024kea",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Minimum gas mass accreted by spinning intermediate-mass black holes in stellar clusters",
        "author":   "K. Kritos, L. Reali, D. Gerosa, E. Berti",
        "journal":  "\prd 110 (2024) 123017",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.110.123017",
        "arxiv":    "arXiv:2409.15439 [astro-ph.HE]",
        "ads":      "2024PhRvD.110l3017K",
        "inspire":  "Kritos:2024kpn",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Flexible mapping of ringdown amplitudes for nonprecessing binary black holes",
        "author":   "C. Pacilio, S. Bhagwat, F. Nobili, D. Gerosa",
        "journal":  "\prd 110 (2024) 103037",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.110.103037",
        "arxiv":    "arXiv:2408.05276 [gr-qc]",
        "ads":      "2024PhRvD.110j3037P",
        "inspire":  "Pacilio:2024tdl",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "Classifying binary black holes from Population III stars with the Einstein Telescope: a machine-learning approach",
        "author":   "F. Santoliquido, U. Dupletsa, J. Tissino, M. Branchesi, F. Iacovelli, G. Iorio, M. Mapelli, D. Gerosa, J. Harms, M. Pasquato",
        "journal":  "\\aap 690 (2024) A362",
        "link":     "https://doi.org/10.1051/0004-6361/202450381",
        "arxiv":    "arXiv:2404.10048 [astro-ph.HE]",
        "ads":      "2024A&A...690A.362S",
        "inspire":  "Santoliquido:2024oqs",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Residual eccentricity as a systematic uncertainty on the formation channels of binary black holes",
        "author":   "G. Fumagalli, I. Romero-Shaw, D. Gerosa, V. De Renzis, K. Kritos, A. Olejak",
        "journal":  "\prd 110 (2024) 063012",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.110.063012",
        "arxiv":    "arXiv:2405.14945 [astro-ph.HE]",
        "ads":      "2024PhRvD.110f3012F",
        "inspire":  "Fumagalli:2024gko",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Astrophysical and relativistic modeling of the recoiling black-hole candidate in quasar 3C 186",
        "author":   "M. Boschini, D. Gerosa, O. S. Salafia, M. Dotti",
        "journal":  "\\aap 686 (2024) A245",
        "link":     "https://doi.org/10.1051/0004-6361/202449596",
        "arxiv":    "arXiv:2402.08740 [astro-ph.GA]",
        "ads":      "2024A&A...686A.245B",
        "inspire":  "Boschini:2024tls",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "Quick recipes for gravitational-wave selection effects",
        "author":   "D. Gerosa, M. Bellotti",
        "journal":  "\cqg 41 (2024) 125002",
        "link":     "https://iopscience.iop.org/article/10.1088/1361-6382/ad4509",
        "arxiv":    "arXiv:2404.16930 [astro-ph.HE]",
        "ads":      "2024CQGra..41l5002G",
        "inspire":  "Gerosa:2024isl",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "pAGN: the one-stop solution for AGN disc modeling",
        "author":   "D. Gangardt, A. A. Trani, C. Bonnerot, D. Gerosa",
        "journal":  "\mnras 530 (2024) 3986–3997",
        "link":     "https://doi.org/10.1093/mnras/stae1117",
        "arxiv":    "arXiv:2403.00060 [astro-ph.HE]",
        "ads":      "2024MNRAS.530.3689G",
        "inspire":  "Gangardt:2024bic",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "Catalog variance of testing general relativity with gravitational-wave data",
        "author":   "C. Pacilio, D. Gerosa, S. Bhagwat",
        "journal":  "\prdl 109 (2024) L081302",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.109.L081302",
        "arxiv":    "arXiv:2310.03811 [gr-qc]",
        "ads":      "2024PhRvD.109h1302P",
        "inspire":  "Pacilio:2023uef",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Calibrating signal-to-noise ratio detection thresholds using gravitational-wave catalogs",
        "author":   "M. Mould, C. J. Moore, D. Gerosa",
        "journal":  "\prd 109 (2024) 063013",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.109.063013",
        "arxiv":    "arXiv:2311.12117 [gr-qc]",
        "ads":      "2024PhRvD.109f3013M",
        "inspire":  "Mould:2023eca",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "Spin-eccentricity interplay in merging binary black holes",
        "author":   "G. Fumagalli, D. Gerosa",
        "journal":  "\prd 108 (2023) 124055",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.124055",
        "arxiv":    "arXiv:2310.16893 [gr-qc]",
        "ads":      "2023PhRvD.108l4055F",
        "inspire":  "Fumagalli:2023hde",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Glitch systematics on the observation of massive black-hole binaries with LISA",
        "author":   "A. Spadaro, R. Buscicchio, D. Vetrugno, A. Klein, D. Gerosa, S. Vitale, R. Dolesi, W. J. Weber, M. Colpi",
        "journal":  "\prd 108 (2023) 123029",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.123029",
        "arxiv":    "arXiv:2306.03923 [gr-qc]",
        "ads":      "2023PhRvD.108l3029S",
        "inspire":  "Spadaro:2023muy",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Black-hole mergers in disk-like environments could explain the observed $q-\chi_\mathrm{eff}$ correlation",
        "author":   "A. Santini, D. Gerosa, R. Cotesta, E. Berti",
        "journal":  "\prd 108 (2023) 083033",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.083033",
        "arxiv":    "arXiv:2308.12998 [astro-ph.HE]",
        "ads":      "2023PhRvD.108h3033S",
        "inspire":  "Santini:2023ukl",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Extending black-hole remnant surrogate models to extreme mass ratios",
        "author":   "M. Boschini, D. Gerosa, V. Varma, C. Armaza, M. Boyle, M. S. Bonilla, A. Ceja, Y. Chen, N. Deppe, M. Giesler, L. E. Kidder, G. Lara, O. Long, S. Ma, K. Mitman, P. J. Nee, H. P. Pfeiffer, A. Ramos-Buades, M. A. Scheel, N. L. Vu, J. Yoo",
        "journal":  "\prd 108 (2023) 084015",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.084015",
        "arxiv":    "arXiv:2307.03435 [gr-qc]",
        "ads":      "2023PhRvD.108h4015B",
        "inspire":  "Boschini:2023ryi",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "One to many: comparing single gravitational-wave events to astrophysical populations",
        "author":   "M. Mould, D. Gerosa, M. Dall'Amico, M. Mapelli",
        "journal":  "\mnras 525 (2023) 3986–3997",
        "link":     "https://doi.org/10.1093/mnras/stad2502",
        "arxiv":    "arXiv:2305.18539 [astro-ph.HE]",
        "ads":      "2023MNRAS.525.3986M",
        "inspire":  "Mould:2023ift",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Efficient multi-timescale dynamics of precessing black-hole binaries",
        "author":   "D. Gerosa, G. Fumagalli, M. Mould, G. Cavallotto, D. Padilla Monroy, D. Gangardt, V. De Renzis",
        "journal":  "\prd 108 (2023) 024042",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.024042",
        "arxiv":    "arXiv:2304.04801 [gr-qc]",
        "ads":      "2023PhRvD.108b4042G",
        "inspire":  "Gerosa:2023xsx",
        "more":     "Open source code"
        })

    papers['published']['data'].append({
        "title":    "Parameter estimation of binary black holes in the endpoint of the up-down instability",
        "author":   "V. De Renzis, D. Gerosa, M. Mould, R. Buscicchio, L. Zanga",
        "journal":  "\prd 108 (2023) 024024",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.024024",
        "arxiv":    "arXiv:2304.13063 [gr-qc]",
        "ads":      "2023PhRvD.108b4024D",
        "inspire":  "DeRenzis:2023lwa",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Inferring, not just detecting: metrics for high-redshift sources observed with third-generation gravitational-wave detectors",
        "author":   "M. Mancarella, F. Iacovelli, D. Gerosa",
        "journal":  "\prdl 107 (2023) L101302",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.L101302",
        "arxiv":    "arXiv:2303.16323 [gr-qc]",
        "ads":      "2023PhRvD.107j1302M",
        "inspire":  "Mancarella:2023ehn",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Eccentricity or spin precession? Distinguishing subdominant effects in gravitational-wave data",
        "author":   "I. Romero-Shaw, D. Gerosa, N. Loutrel",
        "journal":  "\mnras 519 (2023) 5352–5357",
        "link":     "https://doi.org/10.1093/mnras/stad031",
        "arxiv":    "arXiv:2211.07528 [astro-ph.HE]",
        "ads":      "2023MNRAS.519.5352R",
        "inspire":  "Romero-Shaw:2022fbf",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "The Bardeen-Petterson effect, disk breaking, and the spin orientations of supermassive black-hole binaries",
        "author":   "N. Steinle, D. Gerosa",
        "journal":  "\mnras 519 (2023) 5031–5042",
        "link":     "https://doi.org/10.1093/mnras/stac3821",
        "arxiv":    "arXiv:2211.00044 [astro-ph.HE]",
        "ads":      "2023MNRAS.519.5031S",
        "inspire":  "Steinle:2022jmc",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Deep learning and Bayesian inference of gravitational-wave populations: hierarchical black-hole mergers",
        "author":   "M. Mould, D. Gerosa, S. R. Taylor",
        "journal":  "\prd 106 (2022) 103013",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.106.103013",
        "arxiv":    "arXiv:2203.03651 [astro-ph.HE]",
        "ads":      "2022PhRvD.106j3013M",
        "inspire":  "Mould:2022ccw",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Characterization of merging black holes with two precessing spins",
        "author":   "V. De Renzis, D. Gerosa, G. Pratten, P. Schmidt, M. Mould",
        "journal":  "\prd 106 (2022) 084040",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.106.084040",
        "arxiv":    "arXiv:2207.00030 [gr-qc]",
        "ads":      "2022PhRvD.106h4040D",
        "inspire":  "DeRenzis:2022vsj",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Which black hole formed first? Mass-ratio reversal in massive binary stars from gravitational-wave data",
        "author":   "M. Mould, D. Gerosa, F. S. Broekgaarden, N. Steinle",
        "journal":  "\mnras 517 (2022) 2738–2745",
        "link":     "https://doi.org/10.1093/mnras/stac2859",
        "arxiv":    "arXiv:2205.12329 [astro-ph.HE]",
        "ads":      "2022MNRAS.517.2738M",
        "inspire":  "Mould:2022xeu",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "The irreducible mass and the horizon area of LIGO's black holes",
        "author":   "D. Gerosa, C. M. Fabbri, U. Sperhake",
        "journal":  "\cqg 39 (2022) 175008",
        "link":     "https://iopscience.iop.org/article/10.1088/1361-6382/ac8332",
        "arxiv":    "arXiv:2202.08848 [gr-qc]",
        "ads":      "2022CQGra..39q5008G",
        "inspire":  "Gerosa:2022fbk",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Constraining black-hole binary spin precession and nutation with sequential prior conditioning",
        "author":   "D. Gangardt, D. Gerosa, M. Kesden, V. De Renzis, N. Steinle",
        "journal":  "\prd 106 (2022) 024019",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.106.024019",
        "erratum":  "107 (2023) 109901",
        "errlink":  "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.109901",
        "arxiv":    "arXiv:2204.00026 [gr-qc]",
        "ads":      "2022PhRvD.106b4019G",
        "inspire":  "Gangardt:2022ltd",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Inferring the properties of a population of compact binaries in presence of selection effects",
        "author":   "S. Vitale, D. Gerosa, W. M. Farr, S. R. Taylor",
        "journal":  "Chapter in: Handbook of Gravitational Wave Astronomy, Springer, Singapore",
        "link":     "https://doi.org/10.1007/978-981-15-4702-7_45-1",
        "arxiv":    "arXiv:2007.05579 [astro-ph.IM]",
        "ads":      "2022hgwa.bookE..45V",
        "inspire":  "Vitale:2020aaz",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Gravitational-wave population inference at past time infinity",
        "author":   "M. Mould, D. Gerosa",
        "journal":  "\prd 105 (2022) 024076",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.105.024076",
        "arxiv":    "arXiv:2110.05507 [astro-ph.HE]",
        "ads":      "2022PhRvD.105b4076M",
        "inspire":  "Mould:2021xst",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "The Bardeen-Petterson effect in accreting supermassive black-hole binaries: disc breaking and critical obliquity",
        "author":   "R. Nealon, E. Ragusa, D. Gerosa, G. Rosotti, R. Barbieri",
        "journal":  "\mnras 509 (2022) 5608–5621",
        "link":     "https://doi.org/10.1093/mnras/stab3328",
        "arxiv":    "arXiv:2111.08065 [astro-ph.HE]",
        "ads":      "2022MNRAS.509.5608N",
        "inspire":  "Nealon:2021akj",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Population-informed priors in gravitational-wave astronomy",
        "author":   "C. J. Moore, D. Gerosa",
        "journal":  "\prd 104 (2021) 083008",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.104.083008",
        "arxiv":    "arXiv:2108.02462 [gr-qc]",
        "ads":      "2021PhRvD.104h3008M",
        "inspire":  "Moore:2021xhn",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Looking for the parents of LIGO's black holes",
        "author":   "V. Baibhav, E. Berti, D. Gerosa, M. Mould, K. W. K. Wong",
        "journal":  "\prd 104 (2021) 084002",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.104.084002",
        "arxiv":    "arXiv:2105.12140 [gr-qc]",
        "ads":      "2021PhRvD.104h4002B",
        "inspire":  "Baibhav:2021qzw",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Modeling the outcome of supernova explosions in binary population synthesis using the stellar compactness",
        "author":   "M. Dabrowny, N. Giacobbo, D. Gerosa",
        "journal":  "Rendiconti Lincei. Scienze Fisiche e Naturali 32 (2021) 665–673",
        "link":     "https://link.springer.com/article/10.1007/s12210-021-01019-8",
        "arxiv":    "arXiv:2106.12541 [astro-ph.HE]",
        "ads":      "2021RLSFN..32..665D",
        "inspire":  "Dabrowny:2021yag",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Bayesian parameter estimation of stellar-mass black-hole binaries with LISA",
        "author":   "R. Buscicchio, A. Klein, E. Roebber, C. J. Moore, D. Gerosa, E. Finch, A. Vecchio",
        "journal":  "\prd 104 (2021) 044065",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.104.044065",
        "arxiv":    "arXiv:2106.05259 [astro-ph.HE]",
        "ads":      "2021PhRvD.104d4065B",
        "inspire":  "Buscicchio:2021dph",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Hierarchical mergers of stellar-mass black holes and their gravitational-wave signatures",
        "author":   "D. Gerosa, M. Fishbach",
        "journal":  "\\natastro 5 (2021) 749-760",
        "link":     "https://www.nature.com/articles/s41550-021-01398-w",
        "arxiv":    "arXiv:2105.03439 [gr-qc]",
        "ads":      "2021NatAs...5..749G",
        "inspire":  "Gerosa:2021mno",
        "more":     "Review article. Covered by press release.",
        })

    papers['published']['data'].append({
        "title":    "High mass but low spin: an exclusion region to rule out hierarchical black-hole mergers as a mechanism to populate the pair-instability mass gap",
        "author":   "D. Gerosa, N. Giacobbo, A. Vecchio",
        "journal":  "\\apj 915 (2021) 56",
        "link":     "https://iopscience.iop.org/article/10.3847/1538-4357/ac00bb",
        "arxiv":    "arXiv:2104.11247   [astro-ph.HE]",
        "ads":      "2021ApJ...915...56G",
        "inspire":  "Gerosa:2021hsc",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Testing general relativity with gravitational-wave catalogs: the insidious nature of waveform systematics",
        "author":   "C. J. Moore, E. Finch, R. Buscicchio, D. Gerosa",
        "journal":  "iScience 24 (2021) 102577",
        "link":     "https://www.sciencedirect.com/science/article/pii/S2589004221005459",
        "arxiv":    "arXiv:2103.16486   [gr-qc]",
        "ads":      "2021iSci...24j2577M",
        "inspire":  "Moore:2021eok",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "A taxonomy of black-hole binary spin precession and nutation",
        "author":   "D. Gangardt, N. Steinle, M. Kesden, D. Gerosa, E. Stoikos",
        "journal":  "\prd 103 (2021) 124026",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.124026",
        "arxiv":    "arXiv:2103.03894 [gr-qc]",
        "ads":      "2021PhRvD.103l4026G",
        "inspire":  "Gangardt:2021lic",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "A generalized precession parameter $\chi_\mathrm{p}$ to interpret gravitational-wave data",
        "author":   "D. Gerosa, M. Mould, D. Gangardt, P. Schmidt, G. Pratten, L. M. Thomas",
        "journal":  "\prd 103 (2021) 064067",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.064067",
        "arxiv":    "arXiv:2011.11948 [gr-qc]",
        "ads":      "2021PhRvD.103f4067G",
        "inspire":  "Gerosa:2020aiw",
        "more":     "Open source code"
        })

    papers['published']['data'].append({
        "title":    "Eccentric binary black hole surrogate models for the gravitational waveform and remnant properties: comparable mass, nonspinning case",
        "author":   "T. Islam, V. Varma, J. Lodman, S. E. Field, G. Khanna, M. A. Scheel, H. P. Pfeiffer,  D. Gerosa, L. E. Kidder",
        "journal":  "\prd 103 (2021) 064022",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.064022",
        "arxiv":    "arXiv:2101.11798 [gr-qc]",
        "ads":      "2021PhRvD.103f4022I",
        "inspire":  "Islam:2021mha",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Up-down instability of binary black holes in numerical relativity",
        "author":   "V. Varma, M. Mould, D. Gerosa, M. A. Scheel, L. E. Kidder, H. P. Pfeiffer",
        "journal":  "\prd 103 (2021) 064003",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.064003",
        "arxiv":    "arXiv:2012.07147 [gr-qc]",
        "ads":      "2021PhRvD.103f4003V",
        "inspire":  "Varma:2020bon",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Massive black hole binary inspiral and spin evolution in a cosmological framework",
        "author":   "M. Sayeb, L. Blecha, L. Z. Kelley, D. Gerosa, M. Kesden, J. Thomas",
        "journal":  "\mnras 501 (2021) 2531-2546",
        "link":     "https://doi.org/10.1093/mnras/staa3826",
        "arxiv":    "arXiv:2006.06647 [astro-ph.GA]",
        "ads":      "2021MNRAS.501.2531S",
        "inspire":  "Sayeb:2020ryl",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Gravitational-wave selection effects using neural-network classifiers",
        "author":   "D. Gerosa, G. Pratten, A. Vecchio",
        "journal":  "\prd 102 (2020) 103020",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.102.103020",
        "arxiv":    "arXiv:2007.06585 [astro-ph.HE]",
        "ads":      "2020PhRvD.102j3020G",
        "inspire":  "Gerosa:2020pgy",
        "more":     "Open source code"
        })

    papers['published']['data'].append({
        "title":    "Mapping the asymptotic inspiral of precessing binary black holes to their merger remnants",
        "author":   "L. Reali, M. Mould, D. Gerosa, V. Varma",
        "journal":  "\cqg 37 (2020) 225005",
        "link":     "https://iopscience.iop.org/article/10.1088/1361-6382/abb639/meta",
        "arxiv":    "arXiv:2005.01747 [gr-qc]",
        "ads":      "2020CQGra..37v5005R",
        "inspire":  "Reali:2020vkf",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Astrophysical implications of GW190412 as a remnant of a previous black-hole merger",
        "author":   "D. Gerosa, S. Vitale, E. Berti",
        "journal":  "\prl 125 (2020) 101103",
        "link":     "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.125.101103",
        "arxiv":    "arXiv:2005.04243 [astro-ph.HE]",
        "ads":      "2020PhRvL.125j1103G",
        "inspire":  "Gerosa:2020bjb",
        "more":     "Covered by press release"
        })

    papers['published']['data'].append({
        "title":    "Structure of neutron stars in massive scalar-tensor gravity",
        "author":   "R. Rosca-Mead, C. J. Moore, U. Sperhake, M. Agathos, D. Gerosa",
        "journal":  "Symmetry 12 (2020) 1384",
        "link":     "https://www.mdpi.com/2073-8994/12/9/1384",
        "arxiv":    "arXiv:2007.14429 [gr-qc]",
        "ads":      "2020Symm...12.1384R",
        "inspire":  "Rosca-Mead:2020bzt",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Core collapse in massive scalar-tensor gravity",
        "author":   "R. Rosca-Mead, U. Sperhake, C. J. Moore, M. Agathos, D. Gerosa, C. D. Ott",
        "journal":  "\prd 102 (2020) 044010",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.102.044010",
        "arxiv":    "arXiv:2005.09728 [gr-qc]",
        "ads":      "2020PhRvD.102d4010R",
        "inspire":  "Rosca-Mead:2020ehn",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "The mass gap, the spin gap, and the origin of merging binary black holes",
        "author":   "V. Baibhav, D. Gerosa, E. Berti, K. W. K. Wong, T. Helfer, M. Mould",
        "journal":  "\prd 102 (2020) 043002",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.102.043002",
        "arxiv":    "arXiv:2004.00650 [gr-qc]",
        "ads":      "2020PhRvD.102d3002B",
        "inspire":  "Baibhav:2020xdf",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "The Bardeen-Petterson effect in accreting supermassive black-hole binaries: a systematic approach",
        "author":   "D. Gerosa, G. Rosotti, R. Barbieri",
        "journal":  "\mnras 496 (2020) 3060-3075",
        "link":     "https://doi.org/10.1093/mnras/staa1693",
        "arxiv":    "arXiv:2004.02894 [astro-ph.GA]",
        "ads":      "2020MNRAS.496.3060G",
        "inspire":  "Gerosa:2020xly",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Populations of double white dwarfs in Milky Way satellites and their detectability with LISA",
        "author":   "V. Korol, S. Toonen, A. Klein, V. Belokurov, F. Vincenzo, R. Buscicchio, D. Gerosa, C. J. Moore, E. Roebber, E. M. Rossi, A. Vecchio",
        "journal":  "\\aap 638 (2020) A153",
        "link":     "https://www.aanda.org/articles/aa/abs/2020/06/aa37764-20/aa37764-20.html",
        "arxiv":    "arXiv:2002.10462 [astro-ph.GA]",
        "ads":      "2020A&A...638A.153K",
        "inspire":  "Korol:2020lpq",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Endpoint of the up-down instability in precessing binary black holes",
        "author":   "M. Mould, D. Gerosa",
        "journal":  "\prd 101 (2020) 124037",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.101.124037",
        "arxiv":    "arXiv:2003.02281 [gr-qc]",
        "ads":      "2020PhRvD.101l4037M",
        "inspire":  "Mould:2020cgc",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Black holes in the low mass gap: Implications for gravitational wave observations",
        "author":   "A. Gupta, D. Gerosa, K. G. Arun, E. Berti, W. Farr, B. S. Sathyaprakash",
        "journal":  "\prd 101 (2020) 103036",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.101.103036",
        "arxiv":    "arXiv:1909.05804 [gr-qc]",
        "ads":      "2020PhRvD.101j3036G",
        "inspire":  "Gupta:2019nwj",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Milky Way satellites shining bright in gravitational waves",
        "author":   "E. Roebber, R. Buscicchio, A. Vecchio, C. J. Moore, A. Klein, V. Korol, S. Toonen, D. Gerosa, J. Goldstein, S. M. Gaebel, T. E. Woods",
        "journal":  "\\apjl 894 (2020) L15",
        "link":     "https://iopscience.iop.org/article/10.3847/2041-8213/ab8ac9",
        "arxiv":    "arXiv:2002.10465 [astro-ph.GA]",
        "ads":      "2020ApJ...894L..15R",
        "inspire":  "Roebber:2020hso",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Evolutionary roads leading to low effective spins, high black hole masses, and O1/O2 rates for LIGO/Virgo binary black holes",
        "author":   "K. Belczynski, J. Klencki, C. E. Fields, A. Olejak, E. Berti, G. Meynet, C. L. Fryer, D. E. Holz, R. O'Shaughnessy, D. A. Brown, T. Bulik, S. C. Leung,  K. Nomoto, P. Madau, R, Hirschi, E. Kaiser, S. Jones, S. Mondal, M. Chruslinska, P. Drozda, D. Gerosa, Z. Doctor, M. Giersz, S. Ekstr\:om, C. Georgy, A. Askar, V. Baibhav, D. Wysocki, T. Natan, W. M. Farr, G. Wiktorowicz, M. C. Miller, B. Farr, J.-P. Lasota",
        "journal":  "\\aap 636 (2020) A104",
        "link":     "https://www.aanda.org/articles/aa/full_html/2020/04/aa36528-19/aa36528-19.html",
        "arxiv":    "arXiv:1706.07053 [astro-ph.HE]",
        "ads":      "2020A&A...636A.104B",
        "inspire":  "Belczynski:2017gds",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Amplification of superkicks in black-hole binaries through orbital eccentricity",
        "author":   "U. Sperhake, R. Rosca-Mead, D. Gerosa, E. Berti",
        "journal":  "\prd 101 (2020) 024044",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.101.024044",
        "arxiv":    "arXiv:1910.01598 [gr-qc]",
        "ads":      "2020PhRvD.101b4044S",
        "inspire":  "Sperhake:2019wwo",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Constraining the fraction of binary black holes formed in isolation and young star clusters with gravitational-wave data",
        "author":   "Y. Bouffanais, M. Mapelli, D. Gerosa, U. N. Di Carlo, N. Giacobbo, E. Berti, V. Baibhav",
        "journal":  "\\apj 886 (2019) 25",
        "link":     "https://iopscience.iop.org/article/10.3847/1538-4357/ab4a79",
        "arxiv":    "arXiv:1905.11054 [astro-ph.HE]",
        "ads":      "2019ApJ...886...25B",
        "inspire":  "Bouffanais:2019nrw",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Machine-learning interpolation of population-synthesis simulations to interpret gravitational-wave observations: a case study.",
        "author":   "K. W. K. Wong, D. Gerosa",
        "journal":  "\prd 100 (2019) 083015",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.100.083015",
        "arxiv":    "arXiv:1909.06373 [astro-ph.HE]",
        "ads":      "2019PhRvD.100h3015W",
        "inspire":  "Wong:2019uni",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Surrogate models for precessing binary black hole simulations with unequal masses",
        "author":   "V. Varma, S. E. Field, M. A. Scheel, J. Blackman, D. Gerosa, L. C. Stein, L. E. Kidder, H. P. Pfeiffer",
        "journal":  "\prr 1 (2019) 033015",
        "link":     "",
        "arxiv":    "arXiv:1905.09300 [gr-qc]",
        "ads":      "2019PhRvR...1c3015V",
        "inspire":  "Varma:2019csw",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Gravitational-wave detection rates for compact binaries formed in isolation: LIGO/Virgo O3 and beyond",
        "author":   "V. Baibhav, E. Berti, D. Gerosa, M. Mapelli, N. Giacobbo, Y. Bouffanais, U. N. Di Carlo",
        "journal":  "\prd 100 (2019) 064060",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.100.064060",
        "arxiv":    "arXiv:1906.04197 [gr-qc]",
        "ads":      "2019PhRvD.100f4060B",
        "inspire":  "Baibhav:2019gxm",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Escape speed of stellar clusters from multiple-generation black-hole mergers in the upper mass gap",
        "author":   "D. Gerosa, E. Berti",
        "journal":  "\prdrc 100 (2019) 041301R",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.100.041301",
        "arxiv":    "arXiv:1906.05295 [astro-ph.HE]",
        "ads":      "2019PhRvD.100d1301G",
        "inspire":  "Gerosa:2019zmo",
        "more":     "Covered by press release"
        })

    papers['published']['data'].append({
        "title":    "Are stellar-mass black-hole binaries too quiet for LISA?",
        "author":   "C. J. Moore, D. Gerosa, A. Klein",
        "journal":  "\mnrasl 488 (2019) L94-L98",
        "link":     "https://doi.org/10.1093/mnrasl/slz104",
        "arxiv":    "arXiv:1905.11998 [astro-ph.HE]",
        "ads":      "2019MNRAS.488L..94M",
        "inspire":  "Moore:2019pke",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Optimizing LIGO with LISA forewarnings to improve black-hole spectroscopy",
        "author":   "R. Tso, D. Gerosa, Y. Chen",
        "journal":  "\prd 99 (2019) 124043",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.99.124043",
        "arxiv":    "arXiv:1807.00075 [gr-qc]",
        "ads":      "2019PhRvD..99l4043T",
        "inspire":  "Tso:2018pdv",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Multiband gravitational-wave event rates and stellar physics",
        "author":   "D. Gerosa, S. Ma, K. W. K. Wong, E. Berti, R. O'Shaughnessy, Y. Chen, K. Belczynski",
        "journal":  "\prd 99 (2019) 103004",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.99.103004",
        "arxiv":    "arXiv:1902.00021 [astro-ph.HE]",
        "ads":      "2019PhRvD..99j3004G",
        "inspire":  "Gerosa:2019dbe",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Wide nutation: binary black-hole spins repeatedly oscillating from full alignment to full anti-alignment",
        "author":   "D. Gerosa, A. Lima, E. Berti, U. Sperhake, M. Kesden, R. O'Shaughnessy",
        "journal":  "\cqg 36 (2019) 105003",
        "link":     "https://iopscience.iop.org/article/10.1088/1361-6382/ab14ae/meta",
        "arxiv":    "arXiv:1811.05979 [gr-qc]",
        "ads":      "2019CQGra..36j5003G",
        "inspire":  "Gerosa:2018mwg",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "The binary black hole explorer: on-the-fly visualizations of precessing binary black holes",
        "author":   "V. Varma, L. C. Stein, D. Gerosa",
        "journal":  "\cqg 36 (2019) 095007",
        "link":     "https://iopscience.iop.org/article/10.1088/1361-6382/ab0ee9/meta",
        "arxiv":    "arXiv:1811.06552 [astro-ph.HE]",
        "ads":      "2019CQGra..36i5007V",
        "inspire":  "Varma:2018rcg",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Frequency-domain waveform approximants capturing Doppler shifts",
        "author":   "K. Chamberlain, C. J. Moore, D. Gerosa, N. Yunes",
        "journal":  "\prd 99 (2019) 024025",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.99.024025",
        "arxiv":    "arXiv:1809.04799 [gr-qc]",
        "ads":      "2019PhRvD..99b4025C",
        "inspire":  "Chamberlain:2018snj",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "High-accuracy mass, spin, and recoil predictions of generic black-hole merger remnants",
        "author":   "V. Varma, D. Gerosa, L. C. Stein, F. H\'ebert, H. Zhang",
        "journal":  "\prl 122 (2019) 011101",
        "link":     "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.122.011101",
        "arxiv":    "arXiv:1809.091259 [gr-qc]",
        "ads":      "2019PhRvL.122a1101V",
        "inspire":  "Varma:2018aht",
        "more":     "Covered by press release"
        })

    papers['published']['data'].append({
        "title":    "Spin orientations of merging black holes formed from the evolution of stellar binaries",
        "author":   "D. Gerosa, E. Berti, R. O'Shaughnessy, K. Belczynski, M. Kesden, D. Wysocki, W. Gladysz",
        "journal":  "\prd 98 (2018) 084036",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.98.084036",
        "arxiv":    "arXiv:1808.02491 [astro-ph.HE]",
        "ads":      "2018PhRvD..98h4036G",
        "inspire":  "Gerosa:2018wbw",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Mining gravitational-wave catalogs to understand binary stellar evolution: a new hierarchical bayesian framework",
        "author":   "S. R. Taylor, D. Gerosa",
        "journal":  "\prd 98 (2018) 083017",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.98.083017",
        "arxiv":    "arXiv:1806.08365 [astro-ph.HE]",
        "ads":      "2018PhRvD..98h3017T",
        "inspire":  "Taylor:2018iat",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Gravitational-wave astrophysics with effective-spin measurements: asymmetries and selection biases",
        "author":   "K. K. Y. Ng, S. Vitale, A. Zimmerman, K. Chatziioannou, D. Gerosa, C.-J. Haster",
        "journal":  "\prd 98 (2018) 083007",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.98.083007",
        "arxiv":    "arXiv:1805.03046 [gr-qc]",
        "ads":      "2018PhRvD..98h3007N",
        "inspire":  "Ng:2018neg",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Black-hole kicks from numerical-relativity surrogate models",
        "author":   "D. Gerosa, F. H\'ebert, L. C. Stein",
        "journal":  "\prd 97 (2018) 104049",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.97.104049",
        "arxiv":    "arXiv:1802.04276 [gr-qc]",
        "ads":      "2018PhRvD..97j4049G",
        "inspire":  "Gerosa:2018qay",
        "more":     "Open source code"
        })

    papers['published']['data'].append({
        "title":    "Explaining LIGO's observations via isolated binary evolution with natal kicks",
        "author":   "D. Wysocki, D. Gerosa, R. O'Shaughnessy, K. Belczynski, W. Gladysz, E. Berti, M. Kesden, D. Holz",
        "journal":  "\prd 97 (2018) 043014",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.97.043014",
        "arxiv":    "arXiv:1709.01943 [astro-ph.HE]",
        "ads":      "2018PhRvD..97d3014W",
        "inspire":  "Wysocki:2017isg",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Impact of Bayesian priors on the characterization of binary black hole coalescences",
        "author":   "S. Vitale, D. Gerosa, C.-J. Haster, K. Chatziioannou, A. Zimmerman",
        "journal":  "\prl 119 (2017) 251103",
        "link":     "http://dx.doi.org/10.1103/PhysRevLett.119.251103",
        "arxiv":    "arXiv:1707.04637 [gr-qc]",
        "ads":      "2017PhRvL.119y1103V",
        "inspire":  "Vitale:2017cfs",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Long-lived inverse chirp signals from core collapse in massive scalar-tensor gravity",
        "author":   "U. Sperhake, C. J. Moore, R. Rosca, M. Agathos, D. Gerosa, C. D. Ott",
        "journal":  "\prl 119 (2017) 201103",
        "link":     "http://dx.doi.org/10.1103/PhysRevLett.119.201103",
        "arxiv":    "arXiv:1708.03651 [gr-qc]",
        "ads":      "2017PhRvL.119t1103S",
        "inspire":  "Sperhake:2017itk",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Nutational resonances, transitional precession, and precession-averaged evolution in binary black-hole systems",
        "author":   "X. Zhao, M. Kesden, D. Gerosa",
        "journal":  "\prd 96 (2017) 024007",
        "link":     "http://dx.doi.org/10.1103/PhysRevD.96.024007",
        "arxiv":    "arXiv:1705.02369 [gr-qc]",
        "ads":      "2017PhRvD..96b4007Z",
        "inspire":  "Zhao:2017tro",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Inferences about supernova physics from gravitational-wave measurements: GW151226 spin misalignment as an indicator of strong black-hole natal kicks",
        "author":   "R. O'Shaughnessy, D. Gerosa, D. Wysocki",
        "journal":  "\prl 119 (2017) 011101",
        "link":     "http://dx.doi.org/10.1103/PhysRevLett.119.011101",
        "arxiv":    "arXiv:1704.03879 [gr-qc]",
        "ads":      "2017PhRvL.119a1101O",
        "inspire":  "OShaughnessy:2017eks",
        "more":     "APS Editor's choice (physics.aps.org). Covered by press release"
        })

    papers['published']['data'].append({
        "title":    "Are merging black holes born from stellar collapse or previous mergers?",
        "author":   "D. Gerosa, E. Berti",
        "journal":  "\prd 95 (2017) 124046",
        "link":     "http://dx.doi.org/10.1103/PhysRevD.95.124046",
        "arxiv":    "arXiv:1703.06223 [gr-qc]",
        "ads":      "2017PhRvD..95l4046G",
        "inspire":  "Gerosa:2017kvu",
        "more":     "PRD Editors' Suggestion"
        })

    papers['published']['data'].append({
        "title":    "On the equal-mass limit of precessing black-hole binaries.",
        "author":   "D. Gerosa, U. Sperhake, J. Vo\\v{s}mera",
        "journal":  "\cqg 34 (2017) 064004",
        "link":     "http://dx.doi.org/10.1088/1361-6382/aa5e58",
        "arxiv":    "arXiv:1612.05263 [gr-qc]",
        "ads":      "2017CQGra..34f4004G",
        "inspire":  "Gerosa:2016aus",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Black-hole kicks as new gravitational-wave observables.",
        "author":   "D. Gerosa, C. J. Moore",
        "journal":  "\prl 117 (2016) 011101",
        "link":     "http://dx.doi.org/10.1103/PhysRevLett.117.011101",
        "arxiv":    "arXiv:1606.04226 [gr-qc]",
        "ads":      "2016PhRvL.117a1101G",
        "inspire":  "Gerosa:2016vip",
        "more":     "PRL Editors' Suggestion. Covered by press release"
        })

    papers['published']['data'].append({
        "title":    "PRECESSION: Dynamics of spinning black-hole binaries with python",
        "author":   "D. Gerosa, M. Kesden",
        "journal":  "\prd 93 (2016) 124066",
        "link":     "http://dx.doi.org/10.1103/PhysRevD.93.124066",
        "arxiv":    "arXiv:1605.01067 [astro-ph.HE]",
        "ads":      "2016PhRvD..93l4066G",
        "inspire":  "Gerosa:2016sys",
        "more":     "Open source code"
        })

    papers['published']['data'].append({
        "title":    "Numerical simulations of stellar collapse in scalar-tensor theories of gravity",
        "author":   "D. Gerosa, U. Sperhake, C. D. Ott",
        "journal":  "\cqg 33 (2016) 135002",
        "link":     "http://dx.doi.org/10.1088/0264-9381/33/13/135002",
        "arxiv":    "arXiv:1602.06952 [gr-qc]",
        "ads":      "2016CQGra..33m5002G",
        "inspire":  "Gerosa:2016fri",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Distinguishing black-hole spin-orbit resonances by their gravitational wave signatures. II: Full parameter estimation",
        "author":   "D. Trifir\`o, R. O'Shaughnessy, D. Gerosa, E. Berti, M. Kesden, T. Littenberg, U. Sperhake",
        "journal":  "\prd 93 (2016) 044071",
        "link":     "http://dx.doi.org/10.1103/PhysRevD.93.044071",
        "arxiv":    "arXiv:1507.05587 [gr-qc]",
        "ads":      "2016PhRvD..93d4071T",
        "inspire":  "Trifiro:2015zda",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Precessional instability in binary black holes with aligned spins",
        "author":   "D. Gerosa, M. Kesden, R. O'Shaughnessy, A. Klein, E. Berti, U. Sperhake, D. Trifir\`o",
        "journal":  "\prl 115 (2015) 141102",
        "link":     "http://dx.doi.org/10.1103/PhysRevLett.115.141102",
        "arxiv":    "arXiv:1506.09116 [gr-qc]",
        "ads":      "2015PhRvL.115n1102G",
        "inspire":  "Gerosa:2015hba",
        "more":     "PRL Editors' Suggestion"
        })

    papers['published']['data'].append({
        "title":    "Tensor-multi-scalar theories: relativistic stars and 3+1 decomposition",
        "author":   "M. Horbatsch, H. O. Silva, D. Gerosa, P. Pani,  E. Berti, L. Gualtieri, U. Sperhake",
        "journal":  "\cqg 32 (2015) 204001",
        "link":     "http://dx.doi.org/10.1088/0264-9381/32/20/204001",
        "arxiv":    "arXiv:1505.07462 [gr-qc]",
        "ads":      "2015CQGra..32t4001H",
        "inspire":  "Horbatsch:2015bua",
        "more":     "IoP Editor's choice (CQG+, IOPselect)"
        })

    papers['published']['data'].append({
        "title":    "Multi-timescale analysis of phase transitions in precessing black-hole binaries",
        "author":   "D. Gerosa, M. Kesden, U. Sperhake, E. Berti, R. O'Shaughnessy",
        "journal":  "\prd 92 (2015) 064016",
        "link":     "http://dx.doi.org/10.1103/PhysRevD.92.064016",
        "arxiv":    "arXiv:1506.03492 [gr-qc]",
        "ads":      "2015PhRvD..92f4016G",
        "inspire":  "Gerosa:2015tea",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Spin alignment and differential accretion in merging black hole binaries",
        "author":   "D. Gerosa, B. Veronesi, G. Lodato, G. Rosotti",
        "journal":  "\mnras 451 (2015) 3941-3954",
        "link":     "http://dx.doi.org/10.1093/mnras/stv1214",
        "arxiv":    "arXiv:1503.06807 [astro-ph.GA]",
        "ads":      "2015MNRAS.451.3941G",
        "inspire":  "Gerosa:2015xya",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Effective potentials and morphological transitions for binary black-hole spin precession",
        "author":   "M. Kesden, D. Gerosa, R. O'Shaughnessy, E. Berti, U. Sperhake",
        "journal":  "\prl 114 (2015) 081103",
        "link":     "http://dx.doi.org/10.1103/PhysRevLett.114.081103",
        "arxiv":    "arXiv:1411.0674 [gr-qc]",
        "ads":      "2015PhRvL.114h1103K",
        "inspire":  "Kesden:2014sla",
        "more":     "Covered by press release"
        })

    papers['published']['data'].append({
        "title":    "Missing black holes in brightest cluster galaxies as evidence for the occurrence of superkicks in nature",
        "author":   "D. Gerosa, A. Sesana",
        "journal":  "\mnras 446 (2015) 38-55",
        "link":     "http://dx.doi.org/10.1093/mnras/stu2049",
        "arxiv":    "arXiv:1405.2072 [astro-ph.GA]",
        "ads":      "2015MNRAS.446...38G",
        "inspire":  "Gerosa:2014gja",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Distinguishing black-hole spin-orbit resonances by their gravitational-wave signatures",
        "author":   "D. Gerosa, R. O'Shaughnessy, M. Kesden, E. Berti, U. Sperhake",
        "journal":  "\prd 89 (2014) 124025.",
        "link":     "http://dx.doi.org/10.1103/PhysRevD.89.124025",
        "arxiv":    "arXiv:1403.7147 [gr-qc]",
        "ads":      "2014PhRvD..89l4025G",
        "inspire":  "Gerosa:2014kta",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Resonant-plane locking and spin alignment in stellar-mass black-hole binaries: a diagnostic of compact-binary formation",
        "author":   "D. Gerosa, M. Kesden, E. Berti, R. O'Shaughnessy, U. Sperhake",
        "journal":  "\prd 87 (2013) 10, 104028",
        "link":     "http://dx.doi.org/10.1103/PhysRevD.87.104028",
        "arxiv":    "arXiv:1302.4442 [gr-qc]",
        "ads":      "2013PhRvD..87j4028G",
        "inspire":  "Gerosa:2013laa",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Black hole mergers: do gas discs lead to spin alignment?",
        "author":   "G. Lodato, D. Gerosa",
        "journal":  "\mnrasl 429 (2013) L30-L34",
        "link":     "http://dx.doi.org/10.1093/mnrasl/sls018",
        "arxiv":    "arXiv:1211.0284 [astro-ph.CO]",
        "ads":      "2013MNRAS.429L..30L",
        "inspire":  "Lodato:2012yr",
        "more":     ""
        })


if proceedings:
    papers['proceedings'] = {}
    papers['proceedings']['label'] = 'White papers, long-authorlist reviews, g proceedings, software papers, etc.'
    papers['proceedings']['data'] = []

    papers['proceedings']['data'].append({
        "title":    "Waveform modelling for the Laser Interferometer Space Antenna",
        "author":   "N. Afshordi, et al. (105 authors incl. D. Gerosa)",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2311.01300 [gr-qc]",
        "ads":      "2023arXiv231101300L",
        "inspire":  "LISAConsortiumWaveformWorkingGroup:2023arg",
        "more":     ""
        })


    papers['proceedings']['data'].append({
        "title":    "QLUSTER: quick clusters of merging binary black holes",
        "author":   "D. Gerosa, M. Mould",
        "journal":  "Proceedings of the 57th Rencontres de Moriond",
        "link":     "https://doi.org/10.58027/bsnq-2422",
        "arxiv":    "arXiv:2305.04987 [astro-ph.HE]",
        "ads":      "2023arXiv230504987G",
        "inspire":  "",
        "more":     "Open source code"
        })

    papers['proceedings']['data'].append({
        "title":    "Astrophysics with the Laser Interferometer Space Antenna",
        "author":   "P. Amaro-Seoane, et al. (155 authors incl. D. Gerosa)",
        "journal":  "\lrr 26 (2022) 2",
        "link":     "https://link.springer.com/article/10.1007/s41114-022-00041-y",
        "arxiv":    "arXiv:2203.06016 [gr-qc]",
        "ads":      "2023LRR....26....2A",
        "inspire":  "Amaro-Seoane:2022rxf",
        "more":     ""
        })

    papers['proceedings']['data'].append({
        "title":    "New horizons for fundamental physics with LISA",
        "author":   "K. G. Arun, et al. (141 authors incl. D. Gerosa)",
        "journal":  "\lrr 25 (2022) 4",
        "link":     "https://doi.org/10.1007/s41114-022-00036-9",
        "arxiv":    "arXiv:2205.01597 [gr-qc]",
        "ads":      "2022LRR....25....4A",
        "inspire":  "Arun:2022vqj",
        "more":     ""
        })

    papers['proceedings']['data'].append({
        "title":    "Prospects for fundamental physics with LISA",
        "author":   "E. Barausse, et al. (320 authors incl. D. Gerosa)",
        "journal":  "\grg 52 (2020) 8, 81",
        "link":     "https://doi.org/10.1007/s10714-020-02691-1",
        "arxiv":    "arXiv:2001.09793 [gr-qc]",
        "ads":      "2020GReGr..52...81B",
        "inspire":  "Barausse:2020rsu",
        "more":     ""
        })

    papers['proceedings']['data'].append({
        "title":    "Black holes, gravitational waves and fundamental physics: a roadmap",
        "author":   "L. Barack, et al. (199 authors incl. D. Gerosa).",
        "journal":  "\cqg 36 (2019) 143001",
        "link":     "https://iopscience.iop.org/article/10.1088/1361-6382/ab0587",
        "arxiv":    "arXiv:1806.05195 [gr-qc]",
        "ads":      "2019CQGra..36n3001B",
        "inspire":  "Barack:2018yly",
        "more":     ""
        })

    papers['proceedings']['data'].append({
        "title":    "Reanalysis of LIGO black-hole coalescences with alternative prior assumptions",
        "author":   "D. Gerosa, S. Vitale, C.-J. Haster, K. Chatziioannou, A. Zimmerman",
        "journal":  "Proceedings of the International Astronomical Union 338 (2018) 22-28",
        "link":     "https://doi.org/10.1017/S1743921318003587",
        "arxiv":    "arXiv:1712.06635 [astro-ph.HE]",
        "ads":      "2018IAUS..338...22G",
        "inspire":  "Gerosa:2017mwk",
        "more":     ""
        })

    papers['proceedings']['data'].append({
        "title":    "Surprises from the spins: astrophysics and relativity with detections of spinning black-hole mergers",
        "author":   "D. Gerosa",
        "journal":  "Journal of Physics: Conference Series 957 (2018) 1, 012014",
        "link":     "http://dx.doi.org/10.1088/1742-6596/957/1/012014",
        "arxiv":    "arXiv:1711.10038 [astro-ph.HE]",
        "ads":      "2018JPhCS.957a2014G",
        "inspire":  "Gerosa:2017xik",
        "more":     ""
        })

    papers['proceedings']['data'].append({
        "title":    "filltex: Automatic queries to ADS and INSPIRE databases to fill LaTex bibliography",
        "author":   "D. Gerosa, M. Vallisneri",
        "journal":  "Journal of Open Source Software 2 (2017) 13",
        "link":     "http://dx.doi.org/10.21105/joss.00222",
        "arxiv":    "",
        "ads":      "2017JOSS....2..222G",
        "inspire":  "Gerosa:2017xrm",
        "more":     "Open source code"
        })

    papers['proceedings']['data'].append({
        "title":    "Testing general relativity with present and future astrophysical observations",
        "author":   "E. Berti, et al. (53 authors incl. D. Gerosa).",
        "journal":  "\cqg 32 (2015) 243001. Topical Review",
        "link":     "http://dx.doi.org/10.1088/0264-9381/32/24/243001",
        "arxiv":    "arXiv:1501.07274 [gr-qc]",
        "ads":      "2015CQGra..32x3001B",
        "inspire":  "Berti:2015itd",
        "more":     ""
        })

    papers['proceedings']['data'].append({
        "title":    "Rival families: waveforms from resonant black-hole binaries as probes of their astrophysical formation history",
        "author":   "D. Gerosa",
        "journal":  "Astrophysics and Space Science Proceedings 40 (2015) 137-145",
        "link":     "http://dx.doi.org/10.1007/978-3-319-10488-1_12",
        "arxiv":    "",
        "ads":      "2015ASSP...40..137G",
        "inspire":  "Gerosa:2015nmy",
        "more":     ""
        })

    papers['proceedings']['data'].append({
        "title":    "Spin alignment effects in black hole binaries",
        "author":   "D. Gerosa",
        "journal":  "Caltech Undergraduate Research Journal (CURJ) 15:1 (2014) 17-26",
        "link":     "https://caltechcampuspubs.library.caltech.edu/2800/",
        "arxiv":    "",
        "ads":      "2015CURJ...15...17G",
        "inspire":  "",
        "more":     ""
        })


if others:
    papers['others'] = {}
    papers['others']['label'] = ''
    papers['others']['data'] = []

    papers['others']['data'].append({
        "title":    "Source modelling at the dawn of gravitational-wave astronomy",
        "author":   "D. Gerosa",
        "journal":  "PhD thesis",
        "link":     "https://www.repository.cam.ac.uk/handle/1810/261557",
        "arxiv":    "",
        "ads":      "2016PhDT.......177G",
        "inspire":  "Gerosa:2016joa",
        "more":     ""
        })

if conferences:
    talks['conferences'] = {}
    talks['conferences']['label'] = 'Talks at conferences'
    talks['conferences']['data'] = []

    talks['conferences']['data'].append({
        "title":    "Spin the black circle.",
        "where":    "Stellar black hole formation and detection, Kyoto, Japan",
        "when":     "Mar 2025",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "It’s not at all trivial to say which is BH1 and which is BH2.",
        "where":    "Gravitational-wave snowballs, populations, and models, Sexten, Italy",
        "when":     "Jan 2025",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "36 186: the kick strikes back",
        "where":    "6th Milan Christmas Workshop, Milan, Italy",
        "when":     "Dec 2024",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({  
        "title":    "Merge many times",
        "where":    "Spanish and Portuguese Relativity Meeting (EREP 2024), Coimbra, Portugal",
        "when":     "Jul 2024",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({    
        "title":    "One population fit to rule them all",
        "where":    "Emerging methods in gravitational-wave population inference, Trieste, Italy",
        "when":     "Jun 2024",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Gravitational-wave selection effects, the easy way",
        "where":    "Linking Advances in our Understanding of Theoretical Astrophysics and Relativity to Observations (LAUTARO), Milan, Italy",
        "when":     "Apr 2024",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Quasar 3C186 as a recoiling massive black hole: still possible but unlikely",
        "where":    "April APS Meeting, Sacramento CA, USA",
        "when":     "Apr 2024",
        "invited":  False,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "Black-hole generations in AGN disks",
        "where":    "TEONGRAV meeting, Naples, Italy",
        "when":     "Dec 2023",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Correlated black holes from AGN disks",
        "where":    "5th Milan Christmas Workshop, Milan, Italy",
        "when":     "Dec 2023",
        "invited":  True,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "The masses and spins of LIGO's black holes are correlated… here is a disk explanation",
        "where":    "RESCEU-NBIA workshop on gravitational-wave sources, Tokyo, Japan",
        "when":     "Dec 2023",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Gravitational waves: figuring out what’s missing",
        "where":    "6th World Laureates Forum, Shanghai, China",
        "when":     "Nov 2023",
        "invited":  True,
        "more":     ""
        })


    talks['conferences']['data'].append({
        "title":    "A lonely gravitational wave",
        "where":    "LISA Astrophysics Working Group Meeting, Milan, Italy",
        "when":     "Sep 2023",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Eccentricity, spin precession, and gravitational-wave signals that are too short",
        "where":    "15th Edoardo Amaldi Conference, (online)",
        "when":     "Jul 2023",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "When orbital eccentricity and spin precession are kind of the same",
        "where":    "April APS Meeting, Minneapolis MN, USA",
        "when":     "Apr 2023",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "The black-hole binary formation-channel problem in gravitational-wave astronomy",
        "where":    "57th Rencontres de Moriond - Gravitation, La Thuile, Italy",
        "when":     "Mar 2023",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "You’ll never merge alone",
        "where":    "Unsolved problems in astrophysics and cosmology, Jerusalem, Israel",
        "when":     "Dec 2022",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Characterization of LIGO/Virgo selection effects with neural networks",
        "where":    "Machine learning in GW search: g2net next challenges, Pisa, Italy",
        "when":     "Sep 2022",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Machine learning and the origin of LIGO's black holes",
        "where":    "31th Texas Symposium on Relativistic Astrophysics, Prague, Czechia",
        "when":     "Sep 2022",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Gravitational-wave populations with a pinch of deep learning",
        "where":    "23nd International Conference on General Relativity and Gravitation (GR23), Beijing, China, (online)",
        "when":     "Jul 2022",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Accretion disks around supermassive black-hole binaries can break",
        "where":    "EuCAPT workshop: Gravitational-wave probes of black hole environments, Rome, Italy",
        "when":     "Jun 2022",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Black-hole binary spin precession: new theoretical predictions and current observational evidence",
        "where":    "9th KAGRA international workshop, Beijing, China, (online)",
        "when":     "Jun 2022",
        "invited":  True,
        "more":     ""
        })


    talks['conferences']['data'].append({
        "title":    "A deep-learning solution to the gravitational-wave population problem",
        "where":    "NBIA Workshop on black-hole dynamics: from gaseous environments to empty space, Copenhagen, Denmark",
        "when":     "Jun 2022",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Gravitational-wave populations and black-hole spin time travel",
        "where":    "April APS Meeting, New York NY, USA",
        "when":     "Apr 2022",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "I've seen a deviation from General Relativity: do you believe me?",
        "where":    "4th Milan Christmas Workshop, Milan, Italy",
        "when":     "Dec 2021",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Filling the gap with hierarchical black-hole mergers",
        "where":    "4th World Laureates Forum, Shanghai, China, (online)",
        "when":     "Nov 2021",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Inspiral, merge, repeat: hierarchical black-hole mergers and their gravitational-wave signatures",
        "where":    "XXIV SIGRAV Conference 2021, Urbino, Italy",
        "when":     "Sep 2021",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Two precessing spins and how to find them",
        "where":    "14th Edoardo Amaldi Conference, Melbourne, Australia, (online)",
        "when":     "Jul 2021",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Waveform systematics and gravitational-wave catalogs",
        "where":    "2nd European Physical Society Conference on Gravitation: measuring gravity, London, UK, (online)",
        "when":     "Jul 2021",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Probing warped accretion disks with gravitational-wave observations of supermassive black-hole mergers",
        "where":    "European Astronomical Society Annual Meeting (EAS2021), Leiden, The Netherlands, (online)",
        "when":     "Jun 2021",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Hierarchical black-hole mergers in the LIGO/Virgo band",
        "where":    "Gravitational Wave Astrophysics Conference 2021, Hefei, China, (online)",
        "when":     "Jun 2021",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Testing GR? Keep calm and mind the waveform.",
        "where":    "24rd Capra Meeting on Radiation Reaction in General Relativity, Waterloo, Canada, (online)",
        "when":     "Jun 2021",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Warped accretion disks with LISA",
        "where":    "Distorted astrophysical discs: new insights and future directions, Cambridge, UK (online)",
        "when":     "May 2021",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Detectability of gravitational-wave signals with neural-network classifiers",
        "where":    "RAS Specialist Meeting -- Machine learning and artificial intelligence applied to astronomy 2, (online)",
        "when":     "May 2021",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Transitioning to research independence in gravitational-wave astronomy (my own view on postdoc and grant applications)",
        "where":    "Gravitational Wave Astrophysics for Early Career Scientists, Leiden, The Netherlands, (online)",
        "when":     "May 2021",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Can a computer learn if LIGO and Virgo will observe gravitational waves?",
        "where":    "April APS Meeting, (online)",
        "when":     "Apr 2021",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "A self-consistent treatment of warped accretion disks surrounding spinning supermassive black holes",
        "where":    "Science at the Horizon: the Next-Generation EHT, (online)",
        "when":     "Feb 2021",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Astrophysical black-hole binaries: the elephant in the room",
        "where":    "Primordial black holes confront gravitational-wave data, Rome, Italy, (online)",
        "when":     "Feb 2021",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Black holes, gravitational waves, and the BEARs",
        "where":    "10th Birmingham Environment for Academic Research (BEAR) Conference, Birmingham, UK, (online)",
        "when":     "Sep 2020",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Warped accretion discs, black-hole spins, and LISA",
        "where":    "13th LISA Symposium, (online)",
        "when":     "Sep 2020",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Multi-timescale post-Newtonian dynamics of spinning black-hole binaries: a status update",
        "where":    "23rd Capra Meeting on Radiation Reaction in General Relativity, Austin TX, USA, (online)",
        "when":     "Jun 2020",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "An attempt to navigate the astro job market",
        "where":    "LISA Early Career Scientists (LECS) training workshop (online)",
        "when":     "Jun 2020",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Second-generation black holes, the pair-instability mass gap, and the escape speed of stellar clusters",
        "where":    "30th Texas Symposium on Relativistic Astrophysics, Portsmouth, UK",
        "when":     "Dec 2019",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Testing the no-hair theorem with multiband black-hole binaries",
        "where":    "30th Texas Symposium on Relativistic Astrophysics, Portsmouth, UK",
        "when":     "Dec 2019",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Multiband gravitational-wave (astro)physics",
        "where":    "Gravitational-wave Excellence through Alliance Training (GrEAT) PhD school, Birmingham, UK",
        "when":     "Nov 2019",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Pick the right one: Bayesian model selection on catalogs of gravitational-wave events",
        "where":    "22nd International Conference on General Relativity and Gravitation (GR22) and 13th Edoardo Amaldi Conference, Valencia, Spain",
        "when":     "Jul 2019",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Space-ground multiband detections. How many?",
        "where":    "22nd International Conference on General Relativity and Gravitation (GR22) and 13th Edoardo Amaldi Conference, Valencia, Spain",
        "when":     "Jul 2019",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Black-hole kicks: how and where",
        "where":    "Taipei Gravitational Wave Group (TGWG) Conference, Taipei, Taiwan",
        "when":     "Oct 2018",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Forming binary black holes out of stars",
        "where":    "Taipei Gravitational Wave Group (TGWG) Conference, Taipei, Taiwan",
        "when":     "Oct 2018",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Getting ready: exploit LISA to improve LIGO's tests of General Relativity",
        "where":    "Einstein Fellows Symposium 2018, Cambridge MA, USA",
        "when":     "Oct 2018",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Runaways: recoiling black holes and their gravitational-wave signatures",
        "where":    "COSPAR 2018 42nd assembly, Pasadena CA, USA",
        "when":     "Jul 2018",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "An unprecedented opportunity: black-hole spectroscopy with LISA forewarnings and LIGO optimizations",
        "where":    "12th LISA Symposium, Chicago IL, USA",
        "when":     "Jul 2018",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "What do LIGO's black holes remember?",
        "where":    "April APS Meeting, Columbus OH, USA",
        "when":     "Apr 2018",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Modeling black hole kicks with waveform approximants",
        "where":    "34rd Pacific Coast Gravity Meeting, Pasadena CA, USA",
        "when":     "Mar 2018",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Black holes from other black holes?",
        "where":    "Gravity@Malta2018, Valletta, Malta",
        "when":     "Jan 2018",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "The gravitational-wave astronomy revolution",
        "where":    "2nd Milan Christmas Workshop, Milan, Italy",
        "when":     "Dec 2017",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Reanalysis of LIGO black-hole coalescences with alternative prior assumptions",
        "where":    "IAU Symposium 338, Baton Rouge LA, USA",
        "when":     "Oct 2017",
        "invited":  False,
        "more":     "Proceedings published by Cambridge University Press (2018)"
        })

    talks['conferences']['data'].append({
        "title":    "Careful with the priors: a reanalysis of LIGO black-hole coalescences",
        "where":    "Einstein Fellows Symposium 2017, Cambridge MA, USA",
        "when":     "Oct 2017",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Empty galaxies to constrain black-hole superkicks",
        "where":    "3rd Swinburne-Caltech Galaxy Workshop, Pasadena CA, USA",
        "when":     "Sept 2017",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Surprises from the spins: astrophysics and relativity with detections of spinning black-hole mergers",
        "where":    "12th Edoardo Amaldi Conference, Pasadena CA, USA, (plenary talk)",
        "when":     "Jul 2017",
        "invited":  True,
        "more":     "Proceedings published by IoP (2018)"
        })

    talks['conferences']['data'].append({
        "title":    "Core collapse and compact-object formation to test General Relativity",
        "where":    "LIGO Core Collapse Supernova Workshop, Pasadena CA, USA",
        "when":     "Mar 2017",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "The curious and simple limit of equal-mass precessing black-hole binaries",
        "where":    "33rd Pacific Coast Gravity Meeting, Santa Barbara CA, USA",
        "when":     "Mar 2017",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Spins remember: spin signatures of astrophysical black hole formation mechanisms",
        "where":    "Strong Gravity and Binary Dynamics with Gravitational Wave Observations, Oxford MS, USA",
        "when":     "Feb 2017",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "The kick is in the waveform: detection of black-hole recoils",
        "where":    "The Dawning Era of Gravitational-Wave Astrophysics, Aspen CO, USA",
        "when":     "Feb 2017",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Kicked waveforms: prospects for direct detection of black hole recoils",
        "where":    "``April'' APS Meeting, Washington DC, USA",
        "when":     "Jan 2017",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Getting the most out of gravitational-wave observations: kicks and spin precession",
        "where":    "Einstein Fellow Symposium 2016, Cambridge MA, USA",
        "when":     "Oct 2016",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Averaging the average: multi-timescale analysis of precessing black-hole binaries",
        "where":    "21st International Conference on General Relativity and Gravitation (GR21), New York NY, USA",
        "when":     "Jul 2016",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Differential accretion means differential alignment",
        "where":    "BritGrav 16, Nottingham, UK",
        "when":     "Apr 2016",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "A new instability to black-hole spin precession",
        "where":    "28th Texas Symposium on Relativistic Astrophysics, Geneva, Switzerland",
        "when":     "Dec 2015",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Binary black-hole spin precession: a tale of three timescales",
        "where":    "One Hundred Years of Strong Gravity, Lisbon, Portugal",
        "when":     "Jun 2015",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Giant and empty: black-hole occupation fraction in brightest cluster galaxies",
        "where":    "BritGrav 15, Birmingham, UK",
        "when":     "Apr 2015",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Not so fast: gas-driven spin alignment in merging black-hole binaries",
        "where":    "Milan Christmas Workshop, Milan, Italy",
        "when":     "Dec 2014",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Missing black holes in brightest cluster galaxies as evidence for the occurrence of superkicks",
        "where":    "99 years of Black Holes, Potsdam, Germany",
        "when":     "May 2014",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Rival families: waveforms from resonant black-hole binaries as probes of their astrophysical formation history",
        "where":    "3rd Session of the Sant Cugat Forum on Astrophysics, Sant Cugat, Spain",
        "when":     "Apr 2014",
        "invited":  False,
        "more":     "Proceedings published by Springer (2015)"
        })

    talks['conferences']['data'].append({
        "title":    "Gravitational-wave signals from stellar-mass black-hole binaries in resonant configurations",
        "where":    "BritGrav 14, Cambridge, UK",
        "when":     "Mar 2014",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Spin alignment effects in stellar mass black hole binaries",
        "where":    "22nd Midwest Relativity Meeting, Chicago IL, USA",
        "when":     "Sep 2012",
        "invited":  False,
        "more":     ""
        })

if seminars:
    talks['seminars'] = {}
    talks['seminars']['label'] = 'Talks at department seminars'
    talks['seminars']['data'] = []

    talks['seminars']['data'].append({
        "title":    "The case of quasar 3C 186 as kicked black hole",
        "where":    "Astronomy seminars, Cardiff University, Cardiff, UK",
        "when":     "Jul 2024",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Black-hole binaries, formation channels, and repeated mergers",
        "where":    "Gravitational-wave seminars, Università di Pisa, Pisa, Italy",
        "when":     "May 2024",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Deep learning and Bayesian stats to uncover the origin of merging black holes",
        "where":    "INAF/OAPD seminars, Università degli Studi di Padova, Padua, Italy",
        "when":     "Apr 2023",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Deep-learning emulators for gravitational-wave population fits",
        "where":    "Theoretical Astrophysics seminars, University of Zurich, Zurich, Switzerland",
        "when":     "Feb 2023",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Comparing gravitational-wave data and stellar-physics predictions with deep learning",
        "where":    "Theoretical Physics colloquium, University of Cambridge, Cambridge, UK",
        "when":     "Feb 2023",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Gravitational-wave data exploitation with deep learning",
        "where":    "Astrophysics seminars, Universit\`{a}  degli Studi di Milano, Milan, Italy",
        "when":     "Jan 2023",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Some of the LIGO events might have merged a few times already",
        "where":    "Gr@v seminars, Universidade de Aveiro, Aveiro, Portugal (online)",
        "when":     "Nov 2021",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Entering the data-driven regime of gravitational-wave astronomy",
        "where":    "Physics Department colloquium, Universit\`{a}  degli Studi di Milano-Bicocca, Milan, Italy (online)",
        "when":     "Oct 2020",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Waiting for the next black-hole surprise, from the upper mass gap to GW190412",
        "where":    "Gravity seminars, University of Mississippi, Oxford MS, USA (online)",
        "when":     "Jun 2020",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Keep the black holes merging: cluster escape speed and the curious case of GW190412",
        "where":    "Astronomy seminars, Cardiff University, Cardiff, UK (online)",
        "when":     "Jul 2020",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Growing up: the next generation of black holes moves out of the cluster",
        "where":    "Black Hole Initiative Colloquium, Harvard University, Cambridge MA, USA (online)",
        "when":     "Mar 2020",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Multiple generations of black-hole mergers to pinpoint their astrophysical origin",
        "where":    "Gravity seminars, University of Southampton, Southampton, UK",
        "when":     "Feb 2020",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Assembling multiple generations of black-hole mergers in the LIGO/Virgo band",
        "where":    "Theoretical Astrophysics seminars, University of Leicester, Leicester, UK",
        "when":     "Feb 2020",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Predicting LIGO's black holes with LISA",
        "where":    "AstroParticle seminars, Institute for Fundamental Physics of the Universe, Trieste, Italy",
        "when":     "Nov 2019",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Multiband gravitational waves: event rates, detectability, and tests of gravity",
        "where":    "Particle Cosmology seminars, University of Nottingham, Nottingham, UK",
        "when":     "Nov 2019",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Understanding birth and growth of binary black holes with gravitational waves",
        "where":    "Physics Colloquium, California State University Los Angeles, Los Angeles CA, USA",
        "when":     "Feb 2019",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "The (astro)physics of black-hole mergers and their gravitational-wave emission",
        "where":    "Physics and Astronomy Colloquium, California State University Northridge, Los Angeles CA, USA",
        "when":     "Jan 2019",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Model selection for large catalogs of gravitational-wave events",
        "where":    "Cosmology seminars, Johns Hopkins University, Baltimore MD, USA",
        "when":     "Nov 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "How to kick black holes out of their galaxies",
        "where":    "Strong Gravity Seminars, Perimeter Institute for Theoretical Physics, Waterloo, Canada",
        "when":     "Sep 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "(Astro)physical consequences of black-hole recoils",
        "where":    "CITA Seminars, Canadian Institute for Theoretical Astrophysics, Toronto, Canada",
        "when":     "Sep 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Black-hole spins and the astrophysics of LIGO's sources",
        "where":    "AEI seminars, Albert Einstein Institute, Hannover, Germany",
        "when":     "Apr 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Dynamics of spinning black-hole binaries as a tool to uncover their formation pathway",
        "where":    "AEI seminars, Albert Einstein Institute, Potsdam, Germany",
        "when":     "Mar 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Runaways: phenomenology and detectability of black-hole recoils",
        "where":    "Theoretical Astrophysics seminars, University of Florida, Gainsville FL, USA",
        "when":     "Mar 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Testing relativity with past and future supernova explosions",
        "where":    "Physics colloquia, Montana State University, Bozeman MT, USA",
        "when":     "Feb 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "More astrophysics out of the first gravitational wave detections",
        "where":    "GSSI seminars, Gran Sasso Science Institute, L'Aquila, Italy",
        "when":     "Jan 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Where do binary black holes come from? How do we find out?",
        "where":    "Theory seminars, Sapienza Universit\`a di Roma, Rome, Italy",
        "when":     "Jan 2018",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Monopole radiation, hyper scalarization and inverse chirps: the promise of testing gravity with stellar collapse",
        "where":    "Steward Observatory lunch seminars, University of Arizona, Tucson AZ, USA",
        "when":     "Nov 2017",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Black-hole binary spin precession: from relativity to astronomy",
        "where":    "GRITTS seminars, Massachusetts Institute of Technology LIGO Lab, Cambridge MA, USA",
        "when":     "Oct 2017",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Constraining the astrophysics behind the first LIGO detections",
        "where":    "Physics colloquia, University of Texas at Dallas, Richardson TX, USA",
        "when":     "Sep 2017",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Binary black hole astrophysics with the first gravitational-wave events",
        "where":    "Theory group seminars, Universitat de Barcelona, Barcelona, Spain",
        "when":     "May 2017",
        "invited":  True,
        "more":     ""
        })


    talks['seminars']['data'].append({
        "title":    "Astrophysics with the first gravitational-wave events: from supernova asymmetries to multiple black-hole generations",
        "where":    "GR seminars, Department of Applied Mathematics and Theoretical Physics, Cambridge, UK",
        "when":     "May 2017",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Black-hole binaries on the road to merger",
        "where":    "Oskar Klein Center colloquia, Stockholms Universitet, Stockholm, Sweden",
        "when":     "Jan 2017",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "A tale of astronomy and relativity: formation and evolution of black-hole binaries",
        "where":    "Department seminars, Universit\`{a}  degli Studi di Milano, Milan, Italy",
        "when":     "Apr 2016",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "A new paradigm for black-hole spin precession",
        "where":    "Astrophysics seminars, University of Birmingham, Birmingham, UK",
        "when":     "Feb 2016",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "New insights on binary black-hole spin precession",
        "where":    "Relativity division seminars, Albert Einstein Institute, Potsdam, Germany",
        "when":     "Feb 2016",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Spontaneous scalarization: a promising avenue for gravitational-wave astronomy",
        "where":    "GReCO seminars, Institut d'Astrophysique de Paris, Paris, France",
        "when":     "Jan 2016",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Innovative multi-timescale approach to binary black holes",
        "where":    "Theoretical Astrophysics seminars, Universit\`{a}  degli Studi di Milano, Milan, Italy",
        "when":     "Dec 2015",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Stellar collapse in scalar-tensor theories of gravity: prospects for gravitational-wave astronomy",
        "where":    "Gravity and Particles seminar, University of Nottingham, Nottingham, UK",
        "when":     "Dec 2015",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Core collapse and relativistic stars in scalar-tensor theories of gravity",
        "where":    "Gravity seminars, STAG Research Center, Southampton, UK",
        "when":     "Oct 2015",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Binary black-hole spin alignment: gas-driven and relativistic inspiral",
        "where":    "Wednesday seminars, Institute of Astronomy, Cambridge, UK",
        "when":     "Jun 2015",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Spin-orbit resonances: unveiling black-hole binary dynamics on both stellar-mass and supermassive scale",
        "where":    "Gravitational Physics seminars, Cardiff University, Cardiff, UK",
        "when":     "May 2014",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Spin-orbit resonances: unveiling black-hole binary dynamics on both stellar-mass and supermassive scale",
        "where":    "GR seminars, Department Applied Mathematics and Theoretical Physics, Cambridge, UK",
        "when":     " May 2014",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "Spin alignment and resonant plane in stellar mass black hole binaries",
        "where":    "Lunch talks, Leiden Observatory, Leiden, The Netherlands",
        "when":     "Jan 2012",
        "invited":  True,
        "more":     ""
        })

if lectures:
    talks['lectures'] = {}
    talks['lectures']['label'] = 'Lectures at PhD schools'
    talks['lectures']['data'] = []

    talks['lectures']['data'].append({
        "title":    "Tips on academic job applications for early career scientists",
        "where":    "Gravitational-wave early-career scientists (GWECS) online talks, (online)",
        "when":     "Nov 2024",
        "invited":  True,
        "more":     ""
        })

    talks['lectures']['data'].append({
        "title":    "My thoughts on the academic job market",
        "where":    "IPTA Student Week 2024, Milan, Italy",
        "when":     "Jun 2024",
        "invited":  True,
        "more":     ""
        })

    talks['lectures']['data'].append({
        "title":    "Stellar-mass black-hole binary formation channels",
        "where":    "Kavli-Villum Summer School on Gravitational Wave, Corfu, Greece",
        "when":     "Sep 2023",
        "invited":  True,
        "more":     ""
        })

    talks['lectures']['data'].append({
        "title":    "Gravitational waves: principles of emission",
        "where":    "Kavli-Villum Summer School on Gravitational Wave, Corfu, Greece",
        "when":     "Sep 2023",
        "invited":  True,
        "more":     ""
        })

    talks['lectures']['data'].append({
        "title":    "Introduction to gravitational waves (theory background)",
        "where":    "VIPER summer school on PTA GW astrophysics, Nashville TN, USA (online)",
        "when":     "Jul 2022",
        "invited":  True,
        "more":     ""
        })

if posters:
    talks['posters'] = {}
    talks['posters']['label'] = 'Posters at conferences'
    talks['posters']['data'] = []

    talks['posters']['data'].append({
        "title":    "Exploitation of gravitational-wave data",
        "where":    "Milano-Bicocca Physics Department 25th anniversary, Milan, Italy",
        "when":     "Sep 2024",
        "invited":  True,
        "more":     ""
        })

    talks['posters']['data'].append({
        "title":    "PRECESSION: efficient black-hole binary evolution with python",
        "where":    "Mathematics and Big Data showcase, Cambridge, UK",
        "when":     "Apr 2016",
        "invited":  False,
        "more":     ""
        })

    talks['posters']['data'].append({
        "title":    "Numerical relativity group at University of Cambridge",
        "where":    "Einstein's Legacy: celebrating 100 years of general relativity, London, UK",
        "when":     "Nov 2015",
        "invited":  True,
        "more":     ""
        })

    talks['posters']['data'].append({
        "title":    "Formation and evolution of compact objects in relativity and modified gravity",
        "where":    "5th DiRAC Science Day, Cambridge, UK",
        "when":     "Sep 2015",
        "invited":  True,
        "more":     ""
        })

    talks['posters']['data'].append({
        "title":    "New analytic solutions to binary black-hole dynamics: from spin precession to inspiral",
        "where":    "Eurostrings 2015, Cambridge, UK",
        "when":     "Mar 2015",
        "invited":  False,
        "more":     ""
        })

    talks['posters']['data'].append({
        "title":    "Analytic solutions to binary black-hole spin precession: recalling Kepler's two-body problem",
        "where":    "Compact objects as astrophysical and gravitational probes, Leiden, The Netherlands",
        "when":    "Jan 2015",
        "invited":  True,
        "more":     "\\textbf{Best  presentation award}"
        })

    talks['posters']['data'].append({
        "title":    "Efficient precession-averaged evolution of spinning black-hole binaries",
        "where":    "RAS Specialist Meeting -- Towards gravitational-wave astronomy: data analysis techniques and challenges, London, UK",
        "when":     "Dec 2014",
        "invited":  False,
        "more":     ""
        })

    talks['posters']['data'].append({
        "title":    "Morphologies and binary transfer: a new approach to the post-newtonian dynamics of precessing black-holes binaries",
        "where":    "DPG Physics School ``General Relativity @99'', Bad Honnef, Germany",
        "when":     "Sep 2014",
        "invited":  False,
        "more":     ""
        })


if outreach:
    talks['outreach'] = {}
    talks['outreach']['label'] = 'Outreach talks'
    talks['outreach']['data'] = []

    talks['outreach']['data'].append({
        "title":    "Buchi neri ed onde gravitazionali (aka: ``Cosa racconto alla vostra prof. dopo una giornata di lavoro'')",
        "where":    "Collegio San Carlo, Milan, Italy",
        "when":     "Jun 2024",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Al confine fra astronomia e relativit\`a",
        "where":    "Finals of the Italian Physics Olympiad, Senigallia, Italy",
        "when":     "Apr 2024",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Black holes on the way to merger",
        "where":    "Cambridge University Astronomical Society, Cambridge, UK",
        "when":     "Feb 2024",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Gravity with some data science in the blender",
        "where":    "Datrix Tech Dissemination, Milan, Italy, (online)",
        "when":     "Oct 2023",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Hands-on astrophysics. Il ruolo del ricercatore",
        "where":    "Italian Association of Physics Students (AISF), Milan, Italy",
        "when":     "May 2023",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Gravity explorers",
        "where":    "Istituto Svizzero, Milan, Italy",
        "when":     "Mar 2023",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Onde gravitazionali, buchi neri e dove trovarli",
        "where":    "Fondazione Sacro Cuore, Milan, Italy",
        "when":     "Sep 2022",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Quando la gravit\`a viaggia",
        "where":    "Astronomiamo Association, Italy, (online)",
        "when":     "Mar 2022",
        "invited":  True,
        "more":     ""
        })


    talks['outreach']['data'].append({
        "title":    "Hearing the Universe with gravitational waves",
        "where":    "Bromsgrove Astronomical Society, Bromsgrove, UK, (online)",
        "when":     "Jun 2021",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Esplorare l'Universo con le onde gravitazionali",
        "where":    "Settimana dell'Astronomia, Fondazione Lombardia per l'Ambiente, Italy, (online)",
        "when":     "Apr 2021",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Can black-hole binaries really make it?",
        "where":    "University of Birmingham Astronomical Student Society,  Birmingham, UK, (online)",
        "when":     "Mar 2021",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "The (gravitational) sound of the Universe",
        "where":    "Institute of Physics (IoP) Lecture Series, UK, (online)",
        "when":     "Dec 2020",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Looking at the Universe with gravity",
        "where":    "Marling School visit, Birmingham, UK",
        "when":     "Feb 2020",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Somewhere in between astronomy and relativity",
        "where":    "Astronomy in the City, Birmingham, UK",
        "when":     "Jan 2020",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Gravitational waves: somewhere between astronomy and relativity",
        "where":    "Malvern Physics Olympics, Great Malvern, UK",
        "when":     "Oct 2019",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Ride the wave (with gravity)",
        "where":    "Physics Day Experience, Birmingham, UK",
        "when":     "Jun 2019",
        "invited":  True,
        "more":     ""
        })

    talks['outreach']['data'].append({
        "title":    "Onde gravitazionali: ascoltare l'Universo (anzich\\'e solo vederlo?)",
        "where":    "Liceo Candia and Liceo Frassati, Seregno, Italy",
        "when":     "Jan 2018",
        "invited":  True,
        "more":     ""
        })


#######################################
