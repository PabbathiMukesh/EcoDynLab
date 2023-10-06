import csv
import re
# Define the list of publications
publications = [
    "S. Lantin, K. McCourt, E. Larkin, N. Butcher, V. Puri, E. McLamore, M. Corrrell, A. Singh (2023) Scanning Plant IoT (SPOT) Facility for High-Throughput Plant Phenotyping, HardwareX (in press).",
    "J.B. Carter, R. Huffaker, A. Singh, E.Z. Bean (2023) HUM: A review of hydrochemical analysis using ultraviolet-visible absorption spectroscopy and machine learning, Science of The Total Environment. https://doi.org/10.1016/j.scitotenv.2023.165826",
    "F. Tishome, G. Hoogenboom, B. Schaffer, A. Singh, Y. Amaptzidis, H. Bayabil (2023) Unmanned Aerial Vehicle (UAV) Imaging and Machine Learning Applications for Plant Phenotyping. Computers and Electronics in Agriculture. https://doi.org/10.1016/j.compag.2023.108064",
    "F. Tishome, H. Bayabil, B. Schaffer, Y. Amaptzidis, G. Hoogenboom, A. Singh (2023) Exploring deficit irrigation as a water conservation strategy: Insights from field experiments and model simulation. Agricultural Water Management. https://doi.org/10.1016/j.agwat.2023.108490",
    "J.B. Carter, A. Sarkees, A. Singh, E.Z. Bean (2023) Evaluation of Low-Cost UV-Vis Spectroscopy for Measuring Nitrate using Synthetic Water Samples. Journal of the American Society of Agricultural and Biological Engineering. doi: 10.13031/ja.15502",
    "S. Shin, Y. Her, R. Muñoz-Carpena, X. Yu, C. Martinez, A. Singh (2023) Climate change impacts on water quantity and quality of a watershed-lake system using a spatially integrated modeling framework in the Kissimmee River – Lake Okeechobee system. Journal of Hydrology. https://doi.org/10.1016/j.ejrh.2023.101408",
    "B.G. Weinstein, S. Marconi, S.J. Graves, A. Zare, A. Singh, S.A. Bohlman, L. Magee, D.J. Johnson, P.A. Townsend, E.P. White (2023) Capturing long-tailed individual tree diversity using an airborne multi-temporal hierarchical model. Remote Sensing in Ecology and Conservation. https://doi.org/10.1002/rse2.335.",
    "A. Singh, P. Townsend (2022) Influence of foliar traits, watershed physiography, and nutrient subsidies on stream water quality in the Upper Midwestern United States. Frontiers in Environmental Science-Environmental Informatics and Remote Sensing. https://doi.org/10.3389/fenvs.2022.974206",
    "E. Morton, S.K. Robinson, F. Mulindahabi, M. Masozera, A. Singh, M.K. Oli (2022) Spatiotemporal patterns in an Afrotropical montane forest bird community. Global Ecology and Conservation. https://doi.org/10.1016/j.gecco.2022.e02333",
    "S. Marconi, B.G. Weinstein, S. Zou, S.A. Bohlman, A. Zare, A. Singh, D. Stewart, I. Harmon, A. Steinkraus, E.P. White (2022) Continental-scale hyperspectral tree species classification in the United States National Ecological Observatory Network. Remote Sensing of Environment. https://doi.org/10.1016/j.rse.2022.113264",
    "B. Bessell, A. Singh (2022) A low-cost open-source handheld LiDAR-based automated understory timber stand surveying device. HardwareX. https://doi.org/10.1016/j.ohx.2022.e00339.",
    "J. Peeling, A. Singh, J. Judge (2022) A structural equation modeling approach to disentangling regional-scale landscape dynamics in Ghana. Frontiers in Environmental Science. https://doi.org/10.3389/fenvs.2021.729266.",
    "I. Harmon, S. Marconi, B. Weinstein, S. Graves, D.Z. Wang, A. Zare, S. Bohlman, A. Singh, E. White (2022) Injecting Domain Knowledge Into Deep Neural Networks for Tree Crown Delineation. IEEE Transactions on Geoscience and Remote Sensing. DOI: 10.1109/TGRS.2022.3216622",
    "A. Biswas, M.H.M.L. Andrade, J.P. Acharya, C.L. De Souza, Y.Lopez, G. De Assis, S. Shirbhate, A. Singh, P.R. Munoz, E. Rios (2021) Phenomics-Assisted Selection for Herbage Accumulation in Alfalfa (Medicago sativa L.) Frontiers in Plant Science. DOI: https://doi.org/10.3389/fpls.2021.756768",
    "D. Stewart, A. Zare, S. Marconi, B.G. Weinstein, E.P. White, S.J. Graves, S.A. Bohlman, A. Singh (2021) RandCrowns: A Quantitative Metric for Imprecisely Labeled Tree Crown Delineation. IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing (14) pp 11229-11239 DOI: 10.1109/JSTARS.2021.3122345",
    "M. Arasumani, A. Singh, M. Bunyan, V.V. Robin (2021) Testing the efficacy of hyperspectral (AVIRIS-NG), multispectral (Sentinel-2) and radar (Sentinel-1) remote sensing images to detect native and invasive non-native trees. Biological Invasions. DOI: 10.1007/s10530-021-02543-2",
    "B. Weinstein, S.J. Graves, S. Marconi, A. Singh, A. Zare, D. Stewart, S. A. Bohlman, E.P. White (2021) A benchmark dataset for canopy crown detection and delineation in co-registered airborne RGB, LiDAR and hyperspectral imagery from the National Ecological Observation Network, PLOS Computational Biology. https://doi.org/10.1371/journal.pcbi.1009180",
    "P.A. Townsend, J.D. Clare, N. Liu, J.L. Stenglein, C. Anhalt-Depies, T.R. Van Deelen, N.A. Gilbert, A. Singh, K.J. Martin, B. Zuckerberg (2021) Snapshot Wisconsin: networking community scientists and remote sensing to improve ecological monitoring and management, Ecological Applications. https://doi.org/10.1002/eap.2436",
    "N. Liu, M. Garcia, A. Singh, J.D.J. Clare, J.L. Stenglein, B. Zuckerberg, E.L. Kruger, P.A. Townsend (2021) Trail camera networks provide insights into satellite-derived phenology for ecological studies, International Journal of Applied Earth Observation and Geoinformation. DOI: 10.1016/j.jag.2020.102291",
    "B. Weinstein, S. Marconi, S.A. Bohlman, A. Zare, A. Singh, S.J. Graves, E.P. White (2021) A remote sensing derived data set of 100 million individual tree crowns for the National Ecological Observatory Network, eLife. DOI: 10.7554/eLife.62922.",
    "I. Ahmad, A. Singh, M. Fahad, M.M. Waqas (2020) Remote sensing-based framework to predict and assess the interannual variability of maize yields in Pakistan using Landsat imagery. Computers and Electronics in Agriculture. DOI: 10.1016/j.compag.2020.105732",
    "Z. Wang, A. Chlus, R. Geygan, Z. Ye, T. Zheng, A. Singh, J.J. Couture, J. Cavender-Bares, E.L. Kruger, P.A. Townsend (2020) Foliar functional traits from imaging spectroscopy across biomes in eastern North America. New Phytologist. DOI: 10.1111/nph.16711",
    "J.E. Meireles, J. Cavender-Bares, P.A. Townsend, S.Ustin, J.A. Gamon, A.K. Schweiger, M.E. Schaepman, G.P. Asner, R.E. Martin, A. Singh, F. Schrodt, A. Chlus Brian C. O'Meara (2020) Leaf reflectance spectra capture the evolutionary history of seed plants, New Phytologist, DOI: 10.1111/nph.16771.",
    "A.N. Chaurasia,M.G. Dave, R.M. Parmar, B. Bhattacharya, P.R. Marpu, A. Singh, N.S.R. Krishnayya (2020) Inferring Species Diversity and Variability over Climatic Gradient with Spectral Diversity Metrics. Remote Sensing. 12 2130.",
    "M. Lien, R. Barker; Z. Ye, M. Westphall, R. Gao, A. Singh, S. Gilroy, P. Townsend (2019) A Low-cost and Open-Source Platform for Automated Imaging. Plant Methods 15 (6). DOI: 10.1186/s13007-019-0392-1",
    "J. Clare, P. Townsend, C. Anhalt-Depies, C. Locke, J. Stenglein, S. Frett, K. Martin, A. Singh, T. Van Deelen, B. Zuckerberg (2019) Making inference with messy (citizen science) data: when are data accurate enough and how can they be improved? Ecological Applications. DOI: 10.1002/eap.1849",
    "Z. Wang, P. A. Townsend, A. K. Schweiger, J.J. Couture, A.Singh, S.E. Hobbie, J.Cavender-Bares (2019) Mapping foliar functional traits and their uncertainties across three years in a grassland experiment. Remote Sensing of Environment. (221) 405-416. DOI: 10.1016/j.rse.2018.11.016",
    "A. Sharma, K.K. Bohn, J. McKeithen, A. Singh (2019) Effects of conversion harvests on light regimes in a southern pine ecosystem in transition from intensively managed plantations to uneven-aged stands. Forest Ecology and Management. (432) 140-149. DOI: 10.1016/j.foreco.2018.09.019",
    "S. Dubois, A. Desai, A. Singh, S.P. Serbin, M. Goulden, D. Baldocchi, S. Ma, W. Oechel, S. Wharton, E.L. Kruger, P.A. Townsend (2018) Using imaging spectroscopy to detect variation in terrestrial ecosystem productivity across a water-stressed landscape. Ecological Applications. 28(5) 1313-1324. DOI: 10.1002/eap.1733",
    "J.J. Couture, A. Singh, A.O. Charkowski, R.L. Groves, S.M. Gray, P.C. Bethke, P.A. Townsend (2018) Integrating spectroscopy with potato disease management. Plant Disease. DOI: 10.1094/PDIS-01-18-0054-RE",
    "I. Herrmann, S.K. Vosberg, P. Ravindran, A. Singh, H. Chang, M.I. Chilvers, S.P. Conley, P. Townsend (2018) Leaf and Canopy Level Detection of Fusarium Virguliforme (Sudden Death Syndrome) in Soybean. Remote Sensing. 10(3) 426. DOI:10.3390/rs10030426",
    "R. Kolka, B.R. Sturtevant, J.R. Miesel, P. Wolter, S. Fraver, T.D. DeSutter, A. Singh, P.T. Wolter, S. Fraver, T.M. DeSutter, P.A. Townsend (2017) Emissions of Forest Floor and Mineral Soil Carbon, Nitrogen and Mercury Pools and Relationships with Fire Severity for the Pagami Creek Fire in the Boreal Forest of Northern Minnesota. International Journal of Wildland Fire. 26(4) 296-305. DOI:10.1071/WF16128",
    "F. Lacasella, S. Marta, A. Singh, K. S. Whitney, K. Hamilton, P. Townsend, C.J. Kucharik, T.D. Meehan and C. Gratton (2017) From pest data to abundance-based risk maps combining eco-physiological knowledge, weather and habitat variability. Ecological Applications. 27(2) 575-588 DOI: 10.1002/eap.1467",
    "J. J. Couture,  A. Singh, K.F. Rubert-Nason, S.P. Serbin, R.L. Lindroth, P.A. Townsend (2016) Spectroscopic determination of ecologically relevant plant secondary metabolites. Methods in Ecology and Evolution. (7) 1402-1412. DOI: 10.1111/2041-210X.12596",
    "S.C. Zipper, J. Schatz, A. Singh, C.J. Kucharik, P.A. Townsend, S.P. Loheide II (2016) Urban heat island impacts on plant phenology: intra-urban variability and response to land cover. Environmental Research Letters. 11 (5).",
    "C.J. Kucharik, A.C. Mork, T.D. Meehan, S.P. Serbin, A. Singh, P.A. Townsend, K.S. Whitney, C. Gratton (2016) Evidence for Compensatory Photosynthetic and Yield Response of Soybeans to Aphid Herbivory. Journal of Economic Entomology. DOI: 10.1093/jee/tow066",
    "J. Cavender-Bares, J.E. Meireles, J.J. Couture, M.A. Kaproth, C.C. Kingdon, A. Singh, S.P. Serbin, A. Center, E. Zuniga, G. Pilz, P.A. Townsend (2016) Associations of Leaf Spectra with Genetic and Phylogenetic Variation in Oaks: Prospects for Remote Detection of Biodiversity. Remote Sensing. DOI: 10.3390/rs8030221",
    " S.P. Serbin, A. Singh, B.E. McNeil, C.C. Kingdon, P.A. Townsend (2015) Remotely estimating photosynthetic capacity, and its response to temperature, in vegetation canopies using imaging spectroscopy. Remote Sensing of Environment. DOI:10.1016/j.rse.2015.05.024",
    "H. Gu, A. Singh, P.A. Townsend (2015). Detection of gradients of forest composition in an urban area using imaging spectroscopy. Remote Sensing of Environment. DOI:10.1016/j.rse.2015.06.010",
    "A. Singh, B.E. McNeil, P.A. Townsend (2015) Imaging spectroscopy algorithms for mapping canopy foliar chemical and morphological traits and their uncertainties. Ecological Applications. DOI: 10.1890/14-2098.1",
    "A.C. Perillo, C.J. Kucharik, T.D. Meehan, S.P. Serbin, A. Singh, P.A. Townsend, K.S. Whitney, C. Gratton (2015) Use of insect exclusion cages in soybean creates an altered microclimate and differential crop response. Agricultural and Forest Meteorology 208 50-61. DOI: 10.1016/j.agrformet.2015.04.014",
    "M.E. Fagan, R.S. DeFries, S.E. Sesnie, J.P. Arroyo-Mora, C. Soto, A. Singh, P.A. Townsend, R.L. Chazdon (2015) Mapping species composition of forests and tree plantations in northeastern Costa Rica with an integration of hyperspectral and multitemporal Landsat imagery. Remote Sensing. 7(5), 5660-5696; doi:10.3390/rs70505660",
    "M. Bunyan, S. Bardhan, A. Singh, S. Jose (2015) Effect of topography on the distribution of tropical montane forest fragments: a predictive modelling approach. Journal of Tropical Forest Science. 27(1) 30-38.",
    "S.P. Serbin, A. Singh, A.R. Desai, S.G. Dubois, A.D. Jablonski, C.C. Kingdon, E.L. Kruger, P.A. Townsend (2014) Spectroscopic determination of leaf morphological and biochemical traits for northern temperate and boreal tree species. Ecological Applications. DOI: 10.1890/13-2110.1",
    "M.D. Madritch; C.C. Kingdon; A. Singh; K.E. Mock, R.L. Lindroth, P.A. Townsend (2014) Imaging spectroscopy links aspen genotype with below-ground processes at landscape scales. Philosophical transactions of the Royal Society of London. Series B, Biological sciences 369: 20130194.",
    "L. Brottem, M.D. Turner, B. Butt, A. Singh (2014) Biophysical variability and pastoral rights to resources: West African transhumance revisited. Human Ecology, DOI:/10.1007/s10745-014-9640-1",
    "M.D. Turner, B. Butt, A. Singh, L. Brottem, A. Ayantunde, B. Gerard (2014) Variation in Vegetation Cover and Livestock Mobility Needs in Sahelian West Africa. Journal of Land Use Science. DOI: 10.1080/1747423X.2014.965280",
    "A. Singh, A.R. Jakubowski, I. Chidister, P. A. Townsend (2013) A MODIS approach to predicting stream water quality in Wisconsin. Remote Sensing of the Environment 128:74-86.",
    "P.G. Shankar, A. Singh, S. R. Ganesh, R. Whitaker (2013) Factors influencing human hostility to King Cobras (Ophiophagus hannah) in the Western Ghats of India. Hamadryad 36:91-100.",
    "M. Z. Islam, A. Singh, M. P. Basheer, J. Judas and A. Boug (2012) Differences in space use and habitat selection between captive-bred and wild-born Houbara bustards in Saudi Arabia: results from a long-term reintroduction program. Journal of Zoology 289:251-261.",
    "P.T. Wolter, E.A. Berkley, S.D. Peckham, A. Singh, and P.A. Townsend (2012). Exploiting tree shadows on snow for estimating forest basal area using Landsat data. Remote Sensing of the Environment 121:69-79.",
    "P. A Townsend, A. Singh, J. R. Foster, N. J. Rehberg, C. C. Kingdon, K. N. Eshleman, S. W. Seagle (2012) A general Landsat model to predict canopy defoliation in broadleaf deciduous forests, Remote Sensing of the Environment 119:255-265.",
    "L. N. Deel, B. E. McNeil, P. G. Curtis, S. P. Serbin, A. Singh, K. N. Eshleman, P. A. Townsend (2012) Relationship of a Landsat cumulative disturbance index to canopy nitrogen and forest structure across eastern US forests. International Journal of Remote Sensing 33:5084-5098.",
    "S. Dubois, A. Desai, E. Euskirchen, S. Vargas, A. Verma, A. Singh, S. Ustin, W. Oechel (2011) Ecosystem function and stability of an Alaskan tussock tundra in response to climate change and variation in bedrock geology. Global Change Biology 17:2562-2574.",
    "P.T. Wolter, S.D. Peckham, E.A. Berkley, S.P. Serbin, A. Singh, M.B. Baker, P.A. Townsend (2011) Improved monitoring and modelling of snow cover using MODIS, Remote Sensing of the Environment, 115, 1017-1032.",
    "D. H. T. Shah, A. Singh, S. S. Talmale, R. A. Khan, M. Z. Islam (2010) Social organisation, mating system and cooperative breeding in Indian Desert Gerbil, Meriones hurrianae. Journal of Arid Environments 74(12):1625-1630.",
    "S. J. K. Frey, S. P. Serbin, A. Singh, D. S. Amanda, S. A. Wingfield, M. L. Hofmann, M. S. Davis (2010) Land use change, water balance, and ecosystem services in the Prairie Pothole Region of the Dakotas, Ecological Modelling, 221(22): 2765-2779.",
    "J. M. Pisciotta, E. H. Merrill, A. Singh, J. L. Wilkening, A. D. Afton (2010) Influence of bison and prescribed fire on vegetation and breeding birds in tallgrass prairie, Biological Conservation, 143(2): 406-416.",
    "P. T. Wolter, S. D. Peckham, E. A. Berkley, S. P. Serbin, A. Singh, M. B. Baker, P. A. Townsend (2009) An integrated high resolution land surface model and MODIS leaf area index data for quantifying the impact of forest disturbance on carbon and water cycling, Environmental Modelling and Software, 24(2): 142-158.",
    "D. R. Jensen, M. A. Ramsey, A. Singh, D. E. Wildt, A. M. Ellis-Felege, G. F. Birchard (2008) Microencapsulated spermatozoa for artificial insemination and the study of avian reproduction. Journal of the International Journal of Poultry Science, 7(2): 161-165."
]

# Define the CSV file name
csv_filename = "publications.csv"

data = []

for publication in publications:
    # Split each publication into its components using regular expressions
    match = re.match(r"^(.*?)\((\d{4})\) (.*?), (.*?)(?:\. |, in press\.|$)(https?://[^\s]+)?$", publication)

    if match:
        authors = match.group(1).strip()
        year = match.group(2)
        title = match.group(3).strip()
        journal = match.group(4).strip()
        doi = match.group(5).strip() if match.group(5) else None

        # Format the DOI as a URL if it's in the DOI format
        if doi and not doi.startswith("https://"):
            doi = f"https://doi.org/{doi}"

        # Create a dictionary for each publication
        publication_data = {
            "authors": authors,
            "year": year,
            "title": title,
            "journal": journal,
            "DOI": doi,
        }

        data.append(publication_data)

# Write the data to a CSV file
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["authors", "year", "title", "journal", "DOI"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write header row
    writer.writeheader()

    # Write publication data
    writer.writerows(data)

print(f"CSV file '{csv_filename}' has been created successfully.")