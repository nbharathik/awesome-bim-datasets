# Awesome BIM Datasets [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of open datasets for Building Information Modeling (BIM) and the built environment.

**[Search all 187 datasets on the website](https://nbharathik.github.io/awesome-bim-datasets/)** · [Suggest a dataset](https://github.com/nbharathik/awesome-bim-datasets/issues/new?template=add-dataset.yml)

## Contents

- [BIM & IFC Models](#bim--ifc-models) (16)
- [Point Clouds & Scan-to-BIM](#point-clouds--scan-to-bim) (25)
- [Urban Point Clouds & Meshes](#urban-point-clouds--meshes) (20)
- [Floorplans](#floorplans) (18)
- [3D City Models & Footprints](#3d-city-models--footprints) (29)
- [Energy & Building Performance](#energy--building-performance) (29)
- [Construction & Inspection](#construction--inspection) (21)
- [Synthetic Indoor Scenes](#synthetic-indoor-scenes) (11)
- [BIM Benchmarks & Machine Learning](#bim-benchmarks--machine-learning) (18)
- [Related lists](#related-lists)

## BIM & IFC Models

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [BIMData IFC Files Collection](https://github.com/bimdata/BIMData-Research-and-Development/blob/master/pages/IFC_FILES.md) | Index of ~100 public IFC files from many sources with direct download links | Varies |  |
| [buildingSMART BCF Test Cases](https://github.com/buildingSMART/BCF-XML/tree/release_3_0/Test%20Cases) | BCF 2.0 to 3.0 issue exchange examples with supporting IFC models | CC BY-ND 4.0 |  |
| [buildingSMART Community Sample Test Files](https://github.com/buildingsmart-community/Community-Sample-Test-Files) | Community IFC, BCF and IDS sample files, including intentionally invalid ones | CC BY 4.0 |  |
| [buildingSMART IDS Test Cases](https://github.com/buildingSMART/IDS/tree/development/Documentation/ImplementersDocumentation/TestCases) | Official IFC and IDS file pairs with expected validation results | CC BY-ND 4.0 |  |
| [buildingSMART IFC 4.3 Sample Models](https://github.com/buildingSMART/IFC4.x-specification-models) | IFC 4.3 specification examples: alignments, linear placement, georeferencing | Not specified |  |
| [buildingSMART IFC5 Examples](https://github.com/buildingSMART/IFC5-development/tree/main/examples) | Preliminary IFC5 (IFCX) example models for buildings and infrastructure | Not specified |  |
| [buildingSMART Sample Test Files](https://github.com/buildingSMART/Certification-datasets) | Official buildingSMART certification sample files for IFC 2x3, IFC 4 and IFC 4.3 | CC BY 4.0 |  |
| [Common BIM Files (Duplex, Office, Clinic)](https://www.wbdg.org/bim/cobie/common-bim-files) | Classic Duplex, Office and Clinic models in IFC and Revit with COBie data | Not specified |  |
| [IFC Infrastructure Unit Tests](https://github.com/bSI-InfraRoom/IFC-infra-unit-test) | IFC infrastructure examples: alignment, terrain, earthworks, drainage | CC BY 4.0 |  |
| [IFC Rail Sample Files](https://github.com/bSI-RailwayRoom/IFC-Rail-Sample-Files) | IFC Rail examples for alignment with cant and linear placement | Not specified |  |
| [IFC Schependomlaan](https://github.com/openBIMstandards/Archive-DataSetSchependomlaan) | Design, as-planned and as-built openBIM data of a Dutch housing project | CC BY 4.0 |  |
| [KIT IFC Examples](https://www.ifcwiki.org/index.php?title=KIT_IFC_Examples) | Small IFC reference models from KIT for testing software and data exchange | Free with attribution |  |
| [Open IFC Model Repository](http://openifcmodel.cs.auckland.ac.nz/) | One of the first public IFC model repositories (~180 files) | Not specified |  |
| [ResBIM](https://github.com/RogerLiang0725/ResBIM) | 1,000+ synthetic residential Revit models with floorplans, plus an IFC version | MIT | [Data](https://huggingface.co/datasets/tsesterh/ResBIM-IFC) · [Paper](https://doi.org/10.1016/j.autcon.2025.106584) |
| [RWTH E3D DigitalHub Models](https://github.com/RWTH-E3D/DigitalHub) | Coordinated architecture and MEP IFC models of a real building, plus CFD variants | MIT |  |
| [TUM GNI Open IFC Models](https://zenodo.org/records/19722012) | 224 anonymized IFC models from TUM BIM coursework | CC BY 4.0 | [Code](https://github.com/ZijianWang-ZW/GNI-BIM-Dataset) |

## Point Clouds & Scan-to-BIM

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [3RScan](https://waldjohannau.github.io/RIO/) | 1,482 RGB-D rescans of 478 indoor scenes for change detection | Custom (non-commercial, terms of use) | [Paper](https://arxiv.org/abs/1908.06109) · [Code](https://github.com/WaldJohannaU/3RScan) |
| [ArCH (Architectural Cultural Heritage)](https://archdataset.polito.it/) | Heritage building point clouds labelled with 10 architectural classes | CC BY-NC-SA 4.0 | [Data](https://archdataset.polito.it/download/) · [Paper](https://doi.org/10.5194/isprs-archives-XLIII-B2-2020-1419-2020) |
| [ARKitScenes](https://github.com/apple/ARKitScenes) | 5,047 iPad LiDAR RGB-D scans of 1,661 indoor venues with 3D boxes | Custom (Apple, non-commercial) | [Paper](https://arxiv.org/abs/2111.08897) |
| [BIMNet](https://thucbims.github.io/bimnet.thucbims.github.io/) | 25 indoor scans paired with ground-truth IFC models for scan-to-BIM evaluation | Custom (Matterport3D terms) | [Paper](https://doi.org/10.1016/j.autcon.2025.106096) |
| [CRASLAB Indoor Point Cloud and BIM](https://zenodo.org/records/7948116) | Labelled scans of university interiors paired with an as-built IFC model | CC BY 4.0 | [Paper](https://doi.org/10.3390/data8060101) |
| [CV4AEC Scan-to-BIM Challenge](https://cv4aec.github.io/) | Laser scans of large buildings paired with floorplans and 3D wall and column models | Custom (research) |  |
| [DeKH (German Hospital Dataset)](https://huggingface.co/datasets/RPTU-FGMB/DeKH) | Hospital scans with semantic labels and handcrafted IFC reference models | CC BY-NC-SA 4.0 | [Data](https://huggingface.co/datasets/RPTU-FGMB/DeKH/tree/main) · [Paper](https://arxiv.org/abs/2604.24311) · [Code](https://github.com/humantecheu/pystruct3d) |
| [Habitat-Matterport 3D (HM3D)](https://aihabitat.org/datasets/hm3d/) | 1,000 3D reconstructions of real homes, offices and public interiors | Custom (academic, non-commercial) | [Data](https://matterport.com/partners/meta) · [Paper](https://arxiv.org/abs/2109.08238) |
| [HePIC](https://github.com/LTTM/Scan-to-BIM) | Point clouds of two large buildings labelled from existing BIM models | CC BY-SA 4.0 | [Paper](https://doi.org/10.1109/ICIP49359.2023.10222064) |
| [HouseLayout3D](https://houselayout3d.github.io/) | 3D vector layouts of multi-floor Matterport3D buildings with doors, windows and stairs | MIT | [Data](https://huggingface.co/datasets/houselayout3d/HouseLayout3D) · [Paper](https://arxiv.org/abs/2512.02450) · [Code](https://github.com/HouseLayout3D/houselayout3d) |
| [ISPRS Benchmark on Indoor Modelling](https://www.isprs.org/resources/datasets/benchmarks/IndoorModeling/dataset.aspx) | Indoor point clouds with reference models for automatic indoor reconstruction | Free for research (attribution) |  |
| [LivingBIM](https://zenodo.org/records/17934615) | As-designed BIM, as-built point clouds and panoramas of an academic building | CC BY 4.0 | [Paper](https://ascelibrary.org/doi/10.1061/9780784485231.080) |
| [Matterport3D](https://niessner.github.io/Matterport/) | RGB-D panoramas of 90 building-scale scenes with meshes and semantic labels | Custom (non-commercial, agreement) | [Paper](https://arxiv.org/abs/1709.06158) · [Code](https://github.com/niessner/Matterport) |
| [MultiScan](https://3dlg-hcvc.github.io/multiscan/) | Mobile RGB-D rescans of indoor scenes with object, part and articulation labels | CC BY-NC 4.0 | [Data](https://huggingface.co/datasets/3dlg-hcvc/MultiScan) · [Paper](https://openreview.net/forum?id=YxUdazpgweG) · [Code](https://github.com/smartscenes/multiscan) |
| [Nothing Stands Still (NSS)](https://www.nothing-stands-still.com/) | Point clouds of buildings under construction captured over time | Custom (non-commercial) | [Paper](https://arxiv.org/abs/2311.09346) · [Code](https://github.com/GradientSpaces/nss-challenge) |
| [PSNet5](https://github.com/PointCloudYC/ResPointNet2#psnet5-dataset) | Industrial laser scans labelled for pipes, pumps, tanks and beams | Not specified |  |
| [Replica](https://github.com/facebookresearch/Replica-Dataset) | 18 photorealistic indoor reconstructions with semantic, glass and mirror labels | Custom (research only) | [Paper](https://arxiv.org/abs/1906.05797) |
| [S3DIS (Stanford 2D-3D-Semantics)](https://github.com/alexsax/2D-3D-Semantics) | Indoor point clouds of 6 office areas (271 rooms) with 13 semantic classes | Custom (research, request form) | [Paper](https://arxiv.org/abs/1702.01105) |
| [ScanNet](https://github.com/ScanNet/ScanNet) | 1,513 RGB-D indoor scans with meshes and instance-level semantic labels | Custom (non-commercial, terms of use) | [Paper](https://arxiv.org/abs/1702.04405) |
| [ScanNet++](https://scannetpp.mlsg.cit.tum.de/scannetpp/) | Laser scans, DSLR images and iPhone RGB-D of 1,006 indoor scenes with dense labels | Custom (non-commercial, terms of use) | [Paper](https://arxiv.org/abs/2308.11417) |
| [ScanNet200](https://rozdavid.github.io/scannet200) | 200-class semantic and instance segmentation benchmark on ScanNet scans | ScanNet terms of use | [Paper](https://arxiv.org/abs/2204.07761) |
| [ScanRefer](https://daveredrum.github.io/ScanRefer/) | Natural-language descriptions of objects in ScanNet scenes for 3D grounding | CC BY-NC-SA 3.0 | [Data](https://github.com/daveredrum/ScanRefer) · [Paper](https://arxiv.org/abs/1912.08830) |
| [SpatialLM Dataset](https://huggingface.co/datasets/manycore-research/SpatialLM-Dataset) | Synthetic point clouds of 12,328 indoor scenes with wall, door and window layouts | CC BY-NC 4.0 | [Paper](https://arxiv.org/abs/2506.07491) · [Code](https://github.com/manycore-research/SpatialLM) |
| [SUM4Re LiDAR and IFC Dataset](https://zenodo.org/records/19678608) | LiDAR scans and target IFC models of buildings in Spain, Norway and the Netherlands | CC BY 4.0 |  |
| [SUN RGB-D](https://rgbd.cs.princeton.edu/) | 10,335 indoor RGB-D images with 3D boxes and room layouts | Not specified |  |

## Urban Point Clouds & Meshes

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [Building-PCC](https://github.com/tudelft3d/Building-PCC-Building-Point-Cloud-Completion-Benchmarks) | Partial airborne LiDAR and complete point clouds of 50k Dutch buildings | GPL-3.0 | [Paper](https://arxiv.org/abs/2404.15644) |
| [Building3D](https://building3d.ucalgary.ca/) | Aerial LiDAR, meshes and roof wireframes for 160,000 Estonian buildings | CC BY-NC-SA 4.0 | [Paper](https://arxiv.org/abs/2307.11914) · [Code](https://github.com/geospatial-lab/Building3D) |
| [BuildingWorld](https://szusic.github.io/BuildingWorld) | ~5M LoD2 building models from 44 cities with real and simulated LiDAR | CC BY-NC-SA 4.0 | [Data](https://huggingface.co/datasets/BuildingWorld/BuildingWorld) · [Paper](https://arxiv.org/abs/2511.06337) |
| [Campus3D](https://github.com/shinke-li/Campus3D) | UAV photogrammetry of the NUS campus with hierarchical semantic labels | CC BY-NC-SA 4.0 | [Paper](https://arxiv.org/abs/2008.04968) |
| [DALES](https://go.udayton.edu/dales3d) | Aerial LiDAR of 10 km² around Surrey, Canada, labelled in 8 classes incl. buildings | Custom (research) | [Paper](https://arxiv.org/abs/2004.11985) |
| [Hessigheim 3D (H3D)](https://ifpwww.ifp.uni-stuttgart.de/benchmark/hessigheim/default.aspx) | UAV LiDAR and textured mesh of a German village over several epochs | Free for research (registration) | [Paper](https://doi.org/10.1016/j.ophoto.2021.100001) |
| [Paris-Lille-3D](https://npm3d.fr/paris-lille-3d) | Mobile laser scans of 2 km of Paris and Lille streets in 50 classes | CC BY-NC-SA 3.0 | [Paper](https://arxiv.org/abs/1712.00032) |
| [RoofN3D](https://roofn3d.gis.tu-berlin.de/) | Airborne LiDAR building point clouds from New York labelled by roof type | Free with citation | [Paper](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-2/1191/2018/) |
| [Semantic3D](https://semantic3d.ethz.ch/) | Terrestrial laser scans of European towns, 4B+ points in 8 classes | CC BY-NC-SA 3.0 | [Paper](https://arxiv.org/abs/1704.03847) |
| [SemanticUrban](https://github.com/YuanFangFF/SemanticUrban) | Dense terrestrial laser scans of Chinese streets in 23 classes | CC BY-NC-SA 4.0 |  |
| [SensatUrban](https://github.com/QingyongHu/SensatUrban) | UAV photogrammetry point clouds of UK cities, ~3B points in 13 classes | Not specified | [Paper](https://arxiv.org/abs/2009.03137) |
| [STPLS3D](https://www.stpls3d.com/data) | Real and synthetic aerial point clouds with building instance labels | CC BY-NC-SA 3.0 | [Paper](https://arxiv.org/abs/2203.09065) |
| [SUM Parts](https://tudelft3d.github.io/SUMParts/) | Urban meshes with roof, facade, window, door and balcony labels | CC BY-NC 4.0 | [Data](https://huggingface.co/datasets/gwxgrxhyz/SUM-Parts) · [Paper](https://arxiv.org/abs/2503.15300) |
| [SUM: Semantic Urban Meshes](https://3d.bk.tudelft.nl/projects/meshannotation/) | Textured Helsinki city meshes with per-face semantic labels | Not specified | [Paper](https://arxiv.org/abs/2103.00355) · [Code](https://github.com/tudelft3d/SUMS-Semantic-Urban-Mesh-Segmentation-public) |
| [Toronto-3D](https://github.com/WeikaiTan/Toronto-3D) | Mobile laser scans of 1 km of Toronto streets in 8 classes | CC BY-NC 4.0 | [Paper](https://arxiv.org/abs/2003.08284) |
| [TUM2TWIN](https://tum2t.win) | Digital twin benchmark of the TUM campus: point clouds, images and 3D models | CC BY 4.0 | [Data](https://gitlab.lrz.de/tum-gis/tum2twin-datasets) · [Paper](https://arxiv.org/abs/2505.07396) |
| [UrbanBIS](https://vcc.tech/UrbanBIS) | Urban photogrammetry with building instance and building-type labels | Custom (non-commercial) | [Paper](https://arxiv.org/abs/2305.02627) |
| [UrbanScene3D](https://vcc.tech/UrbanScene3D) | Real and synthetic city meshes, point clouds and aerial images over 128 km² | Custom (research) | [Paper](https://arxiv.org/abs/2107.04286) |
| [WHU-Urban3D](https://whu3d.com/) | Mobile and airborne LiDAR of Chinese cities with semantic and instance labels | Not specified | [Data](https://whu3d.com/download.html) |
| [ZAHA](https://github.com/OloOcki/zaha) | 601M labelled facade points from Munich mobile laser scans | CC0 | [Paper](https://arxiv.org/abs/2411.04865) |

## Floorplans

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [ArchCAD-400K](https://archiai-lab.github.io/ArchCAD.github.io/) | Architectural CAD drawings with primitive-level labels for symbol spotting | CC BY-NC 4.0 | [Data](https://huggingface.co/datasets/jackluoluo/ArchCAD) · [Paper](https://arxiv.org/abs/2503.22346) · [Code](https://github.com/ArchiAI-LAB/ArchCAD) |
| [CubiCasa5K](https://github.com/CubiCasa/CubiCasa5k) | 5,000 floorplan images with SVG annotations in 80+ categories | CC BY-NC-SA 4.0 | [Data](https://zenodo.org/records/2613548) · [Paper](https://arxiv.org/abs/1904.01920) |
| [CVC-FP](https://dag.cvc.uab.es/dataset/cvc-fp-database-for-structural-floor-plan-analysis/) | 122 scanned floorplans in 4 styles with wall, door and room labels | Free for research |  |
| [FloorPlanCAD](https://floorplancad.github.io/) | 15,663 real CAD floorplans with line-level symbol annotations | CC BY-NC 4.0 | [Paper](https://arxiv.org/abs/2105.07147) |
| [HouseExpo](https://github.com/TeaganLi/HouseExpo) | 35,126 2D house layouts for robot navigation research | MIT | [Paper](https://arxiv.org/abs/1903.09845) |
| [LIFULL HOME'S Dataset](https://www.nii.ac.jp/dsc/idr/en/lifull/) | 5.3M Japanese rental listings with floorplan images | Custom (academic, application) |  |
| [MLSTRUCT-FP](https://github.com/MLSTRUCT/MLStructFP) | 954 multi-unit floor plan images with wall polygon annotations | Not specified | [Paper](https://doi.org/10.1016/j.autcon.2023.105132) · [Code](https://github.com/MLSTRUCT/MLStructFP_benchmarks) |
| [Modified Swiss Dwellings (MSD)](https://caspervanengelenburg.github.io/msd-eccv24-page/) | 5,300+ floorplans of Swiss building complexes with access graphs | CC BY 4.0 | [Data](https://www.kaggle.com/datasets/caspervanengelenburg/modified-swiss-dwellings) · [Paper](https://arxiv.org/abs/2407.10121) · [Code](https://github.com/caspervanengelenburg/msd) |
| [Raster-to-Vector Floorplan Annotations (R2V)](https://github.com/art-programmer/FloorplanTransformation) | Vector annotations of walls, openings and rooms for LIFULL floorplans | Not specified | [Data](https://github.com/art-programmer/FloorplanTransformation/tree/master/data/floorplan_representation) |
| [Rent3D++ (Plan2Scene)](https://3dlg-hcvc.github.io/plan2scene/) | Floorplans with interior photos for creating textured 3D homes | Not specified | [Paper](https://arxiv.org/abs/2106.05375) · [Code](https://github.com/3dlg-hcvc/plan2scene) |
| [ResPlan](https://github.com/m-agour/ResPlan) | 17,000 residential floor plans as vector geometry with room graphs | CC BY 4.0 | [Paper](https://arxiv.org/abs/2508.14006) |
| [ROBIN](https://github.com/gesstalt/ROBIN) | 510 floorplan images in 3 categories for retrieval | Not specified |  |
| [RPLAN](https://ustc-gcl-f.github.io/projects/DeepLayout/index.html) | 80k+ annotated residential floorplans for layout generation | Custom (non-commercial, request form) | [Data](https://docs.google.com/forms/d/e/1FAIpQLSfwteilXzURRKDI5QopWCyOGkeb_CFFbRwtQ0SOPhEg0KGSfw/viewform) · [Paper](https://doi.org/10.1145/3355089.3356556) |
| [SESYD Floorplans](http://mathieu.delalandre.free.fr/projects/sesyd/) | 1,000 synthetic floorplans with symbol-level ground truth | Free for research |  |
| [Swiss Dwellings](https://zenodo.org/records/7788422) | Geometry and simulations for ~45,000 apartments in ~3,100 Swiss buildings | CC BY 4.0 |  |
| [Tell2Design](https://github.com/LengSicong/Tell2Design) | Residential floorplans paired with natural-language design descriptions | CC BY-NC 4.0 | [Paper](https://aclanthology.org/2023.acl-long.820/) |
| [WAFFLE](https://github.com/TAU-VAILab/WAFFLE) | Diverse floorplan images from Wikimedia with building metadata | Varies (Wikimedia) | [Paper](https://arxiv.org/abs/2412.00955) |
| [Zillow Indoor Dataset (ZInD)](https://github.com/zillow/zind) | Panoramas of 1,575 homes with 3D room layouts and floorplans | Custom (non-commercial, agreement) | [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Cruz_Zillow_Indoor_Dataset_Annotated_Floor_Plans_With_360deg_Panoramas_and_CVPR_2021_paper.html) |

## 3D City Models & Footprints

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [3D BAG](https://docs.3dbag.nl/en/) | 3D building models of the whole Netherlands at LoD 1.2, 1.3 and 2.2 | CC BY 4.0 | [Data](https://3dbag.nl/) · [Paper](https://doi.org/10.14358/PERS.21-00032R2) |
| [3D-GloBFP](https://doi.org/10.5281/zenodo.15487037) | Global building footprints with estimated heights for 2020 | CC BY 4.0 | [Paper](https://doi.org/10.5194/essd-16-5357-2024) |
| [Bavaria LoD2 Building Models](https://geodaten.bayern.de/opengeodata/) | CityGML LoD2 models of ~8M buildings in Bavaria | CC BY 4.0 | [Data](https://geodaten.bayern.de/opengeodata/OpenDataDetail.html?pn=lod2) |
| [Berlin 3D City Model](https://www.businesslocationcenter.de/en/economic-atlas/download-portal/) | Textured CityGML LoD2 model of ~550,000 buildings in Berlin | Berlin open data |  |
| [CityJSON Example Datasets](https://www.cityjson.org/datasets/) | Small CityJSON files of Delft, Montréal, New York, Vienna and more | Varies |  |
| [CMAB](https://doi.org/10.6084/m9.figshare.27992417) | 31M buildings in China with height, function, age, structure and quality | CC BY 4.0 | [Paper](https://doi.org/10.1038/s41597-025-04730-5) |
| [CORE3D Public Data and Open Evaluation](https://spacenet.ai/core3d/) | Multiview satellite imagery with reference 3D building labels | Not specified | [Code](https://github.com/pubgeo/core3d-open) |
| [EUBUCCO](https://eubucco.com/) | 322M+ European buildings with footprint, height, floors, use and construction year | ODbL | [Data](https://eubucco.com/data/download) · [Paper](https://doi.org/10.1038/s41597-023-02040-2) · [Code](https://github.com/ai4up/eubucco) |
| [GlobalBuildingAtlas](https://github.com/zhu-xlab/GlobalBuildingAtlas) | ~2.75B building polygons worldwide with heights and LoD1 models | ODbL / CC BY-NC 4.0 | [Paper](https://doi.org/10.5194/essd-17-6647-2025) |
| [Google Open Buildings V3](https://sites.research.google/gr/open-buildings/) | Machine-detected building footprints across the Global South | CC BY 4.0 or ODbL | [Paper](https://arxiv.org/abs/2107.12283) |
| [Helsinki 3D City Models](https://www.hel.fi/en/decision-making/information-on-helsinki/maps-and-geospatial-data/helsinki-3d) | Semantic CityGML model and reality mesh of Helsinki | CC BY 4.0 | [Data](https://hri.fi/data/en_GB/dataset/helsingin-3d-kaupunkimalli) |
| [LEVIR-CD](https://justchenhao.github.io/LEVIR/) | Aerial image pairs with building change masks | Custom (academic only) | [Paper](https://doi.org/10.3390/rs12101662) |
| [LoD2 Building Models NRW](https://www.bezreg-koeln.nrw.de/geobasis-nrw/produkte-und-dienste/3d-gebaeudemodelle) | CityGML LoD2 models of ~10M buildings in North Rhine-Westphalia | DL-DE Zero 2.0 | [Data](https://www.opengeodata.nrw.de/produkte/geobasis/3dg/) |
| [Microsoft Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) | Global machine-generated building footprints, with heights where available | CDLA Permissive 2.0 |  |
| [NYC 3D Building Model](https://www.nyc.gov/site/planning/data-maps/open-data/dwn-nyc-3d-model-download.page) | 3D massing model of every building in New York City | NYC open data |  |
| [Open Buildings 2.5D Temporal](https://sites.research.google/gr/open-buildings/temporal/) | Yearly building presence and height rasters for the Global South | CC BY 4.0 or ODbL | [Paper](https://arxiv.org/abs/2310.11622) |
| [Open City Model](https://github.com/opencitymodel/opencitymodel) | LoD1 CityGML and CityJSON models of ~125M US buildings | ODbL |  |
| [Overture Maps Buildings](https://docs.overturemaps.org/guides/buildings/) | Global building footprints merged from OpenStreetMap and other sources | ODbL |  |
| [PDOK 3D Basisvoorziening](https://www.pdok.nl/introductie/-/article/3d-basisvoorziening-1) | Nationwide 3D topography of the Netherlands in CityJSON | Open data (attribution) |  |
| [Project PLATEAU](https://www.mlit.go.jp/plateau/en/) | Open CityGML 3D city models of 250+ Japanese cities with building use and age | PDL 1.0 (CC BY compatible) | [Data](https://www.geospatial.jp/ckan/dataset/plateau) |
| [SpaceNet 2: Building Detection](https://spacenet.ai/spacenet-buildings-dataset-v2/) | Satellite images with building footprints of Las Vegas, Paris, Shanghai and Khartoum | CC BY-SA 4.0 | [Paper](https://arxiv.org/abs/1807.01232) |
| [SpaceNet 4: Off-Nadir Buildings](https://spacenet.ai/off-nadir-building-detection/) | Off-nadir satellite views of Atlanta with building footprints | CC BY-SA 4.0 |  |
| [SpaceNet 6: Multi-Sensor All-Weather Mapping](https://spacenet.ai/sn6-challenge/) | Optical and SAR imagery of Rotterdam with building footprints | CC BY-SA 4.0 |  |
| [SpaceNet 7: Multi-Temporal Urban Development](https://spacenet.ai/sn7-challenge/) | Monthly satellite mosaics with tracked building footprints for urban growth | CC BY-SA 4.0 | [Paper](https://arxiv.org/abs/2102.04420) |
| [swissBUILDINGS3D](https://www.swisstopo.admin.ch/en/landscape-model-swissbuildings3d-3-0-beta) | 3D building models with roofs for all of Switzerland | Swiss open data (attribution) |  |
| [Urban 3D Challenge](https://spacenet.ai/the-ussocom-urban-3d-competition/) | Orthoimagery, surface models and building footprints of US cities | Custom |  |
| [USA Structures](https://gis-fema.hub.arcgis.com/pages/usa-structures) | Footprints of all US structures over 450 sq ft with occupancy type and height | CC BY 4.0 | [Data](https://disasters.geoplatform.gov/USA_Structures/) |
| [UT-GLOBUS](https://doi.org/10.5281/zenodo.11156602) | Building heights and urban canopy parameters for 1,200+ cities | CC BY 4.0 | [Paper](https://doi.org/10.1038/s41597-024-03719-w) · [Code](https://github.com/texuslabut/UT-GLOBUS) |
| [WHU Building Dataset](https://gpcv.whu.edu.cn/data/building_dataset.html) | Aerial and satellite images with building masks for footprint extraction | Not specified |  |

## Energy & Building Performance

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [AMPds2](https://doi.org/10.7910/DVN/FIE0S4) | Two years of electricity, water and gas data from one Canadian house | Not specified | [Paper](https://www.nature.com/articles/sdata201637) |
| [Appliances Energy Prediction (UCI)](https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction) | Appliance energy and room climate data from a low-energy house | CC BY 4.0 |  |
| [ASHRAE Global Occupant Behavior Database](https://ashraeobdatabase.com/) | 34 field datasets on occupant presence and window, thermostat and light use | CC BY 4.0 | [Data](https://doi.org/10.6084/m9.figshare.16920118) · [Paper](https://doi.org/10.1038/s41597-022-01475-3) |
| [ASHRAE Global Thermal Comfort Database II](https://github.com/CenterForTheBuiltEnvironment/ashrae-db-II) | Indoor climate measurements paired with occupant comfort votes worldwide | ODbL | [Paper](https://www.sciencedirect.com/science/article/pii/S0360132318303652) |
| [ASHRAE Great Energy Predictor III](https://www.kaggle.com/c/ashrae-energy-prediction) | Kaggle competition with hourly meter data from 1,448 buildings | Kaggle rules |  |
| [BOPTEST](https://ibpsa.github.io/project1-boptest/) | Building emulators and scenarios for benchmarking HVAC control | BSD-style | [Data](https://github.com/ibpsa/project1-boptest) · [Paper](https://doi.org/10.1080/19401493.2021.1986574) |
| [Building Data Genome Project 1](https://github.com/buds-lab/the-building-data-genome-project) | Hourly whole-building electricity data, superseded by Building Data Genome 2 | MIT | [Paper](https://doi.org/10.1016/j.egypro.2017.07.400) |
| [Building Data Genome Project 2](https://github.com/buds-lab/building-data-genome-project-2) | Hourly data from 3,053 meters in 1,636 non-residential buildings | CC BY-SA 4.0 | [Paper](https://www.nature.com/articles/s41597-020-00712-x) |
| [Building TimeSeries (BTS)](https://github.com/cruiseresearchgroup/DIEF_BTS) | Three years of BMS time series from three Australian buildings with Brick metadata | CC BY 4.0 | [Data](https://doi.org/10.6084/m9.figshare.28705559) · [Paper](https://arxiv.org/abs/2406.08990) |
| [BuildingsBench (Buildings-900K)](https://data.openei.org/submissions/5859) | 900K simulated US building load profiles plus real buildings for forecasting | CC BY 4.0 | [Paper](https://arxiv.org/abs/2307.00142) · [Code](https://github.com/NREL/BuildingsBench) |
| [CBECS Microdata](https://www.eia.gov/consumption/commercial/) | US commercial building energy survey microdata | Public domain | [Data](https://www.eia.gov/consumption/commercial/data/2018/) |
| [CityLearn](https://www.citylearn.net/) | Multi-building simulation environments for demand response control | MIT | [Code](https://github.com/citylearn-project/CityLearn) |
| [CU-BEMS](https://doi.org/10.6084/m9.figshare.11726517) | Zone-level AC, lighting, plug load and indoor sensor data from a Bangkok office | CC BY 4.0 | [Paper](https://doi.org/10.1038/s41597-020-00582-3) |
| [DOE Commercial Prototype Building Models](https://www.energycodes.gov/prototype-building-models) | EnergyPlus models of 16 commercial building types across US climates | Public domain |  |
| [End-Use Load Profiles (ResStock & ComStock)](https://www.nlr.gov/buildings/end-use-load-profiles) | Calibrated 15-minute end-use load profiles for the US building stock | CC BY 4.0 | [Data](https://data.openei.org/submissions/4520) · [Paper](https://docs.nlr.gov/docs/fy22osti/80889.pdf) |
| [Energy Efficiency (UCI)](https://archive.ics.uci.edu/dataset/242/energy+efficiency) | Simulated heating and cooling loads for 768 residential building variants | CC BY 4.0 |  |
| [EnergyPlus Example Files](https://energyplus.net/) | Hundreds of example IDF energy models shipped with EnergyPlus | BSD-style | [Data](https://github.com/NREL/EnergyPlus) |
| [Google Smart Buildings Dataset](https://www.tensorflow.org/datasets/catalog/smart_buildings) | Six years of HVAC telemetry, setpoints and energy from Google offices | CC BY 4.0 | [Paper](https://arxiv.org/abs/2410.03756) · [Code](https://github.com/google/sbsim) |
| [HOT: HVAC Operations Transfer](https://huggingface.co/datasets/BuildingBench/HOT) | EnergyPlus models and weather for HVAC control transfer across buildings | MIT |  |
| [IDEAL Household Energy Dataset](https://doi.org/10.7488/ds/2836) | Electricity, gas, room climate and survey data from 255 UK homes | CC BY 4.0 | [Paper](https://www.nature.com/articles/s41597-021-00921-y) |
| [LBNL Building 59](https://doi.org/10.7941/D1N33Q) | Three years of office energy, HVAC and occupancy data with a Brick model | CC0 | [Paper](https://doi.org/10.1038/s41597-022-01257-x) · [Code](https://github.com/LBNL-ETA/Data-Cleaning) |
| [LBNL Fault Detection and Diagnostics Datasets](https://fdddata.lbl.gov/) | Labelled HVAC fault data from simulations, labs and field systems | Not specified | [Data](https://fdddata.lbl.gov/data/) |
| [Model America (AutoBEM)](https://doi.org/10.13139/ORNLNCCS/1774134) | OpenStudio and EnergyPlus models for 122.9M US buildings | Not specified |  |
| [NYC Building Energy Benchmarking (LL84)](https://data.cityofnewyork.us/Environment/NYC-Building-Energy-and-Water-Data-Disclosure-for-/5zyy-y8am) | Annual energy and water use of large NYC buildings under Local Law 84 | NYC open data |  |
| [Occupancy Detection (UCI)](https://archive.ics.uci.edu/dataset/357/occupancy+detection) | Office sensor readings labelled as occupied or empty | CC BY 4.0 |  |
| [RECS 2020 Public-Use Microdata](https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata) | US household energy survey microdata | Public domain |  |
| [REFIT Electrical Load Measurements](https://pureportal.strath.ac.uk/en/datasets/refit-electrical-load-measurements/) | Appliance-level electricity data from 20 UK homes | CC BY 4.0 | [Data](https://doi.org/10.15129/31da3ece-f902-4e95-a093-e0a9536983c4) · [Paper](https://doi.org/10.1038/sdata.2016.122) |
| [ROBOD](https://doi.org/10.6084/m9.figshare.19234530) | Room-level occupancy, indoor climate, energy and HVAC data from five rooms | CC BY 4.0 | [Paper](https://doi.org/10.1007/s12273-022-0925-9) · [Code](https://github.com/ideas-lab-nus/robod) |
| [UK-DALE](https://jack-kelly.com/data/) | Whole-home and appliance electricity data from 5 UK homes | CC BY 4.0 | [Data](https://doi.org/10.5286/UKERC.EDC.000004) · [Paper](https://arxiv.org/abs/1404.0284) |

## Construction & Inspection

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [ACID (Alberta Construction Image Dataset)](https://www.acidb.net/) | 10,000 construction machine images with detection, masks and captions | Custom (research only) | [Data](https://www.acidb.net/download) · [Paper](https://doi.org/10.1061/(ASCE)CP.1943-5487.0000945) |
| [AIDCON](https://www.ai2lab.org/aidcon/) | UAV images of construction sites with pixel labels for nine machine classes | CC BY-NC 4.0 | [Paper](https://doi.org/10.3390/rs16173295) |
| [BD3 (Building Defects Detection Dataset)](https://github.com/Praveenkottari/BD3-Dataset) | 3,965 building surface images with six defect types | Not specified | [Paper](https://doi.org/10.1145/3671127.3698789) |
| [CODEBRIM](https://zenodo.org/records/2620293) | Bridge inspection images with multi-label concrete defect annotations | Custom (non-commercial) | [Paper](https://arxiv.org/abs/1904.08486) |
| [Color Helmet and Vest (CHV)](https://github.com/ZijianWang-ZW/PPE_detection) | Site images with workers, vests and four helmet colours | Not specified | [Paper](https://doi.org/10.3390/s21103478) |
| [Concrete Crack Images for Classification](https://data.mendeley.com/datasets/5y9wdsg2zt/2) | 40,000 cracked and intact concrete patches from campus buildings | CC BY 4.0 |  |
| [ConSLAM](https://github.com/mac137/ConSLAM) | Construction-site LiDAR, RGB and IMU sequences with ground-truth scans | Custom (academic) | [Paper](https://doi.org/10.1007/978-3-031-25082-8_21) |
| [Construction Safety Dataset (CSDataset)](https://github.com/zhenhuiou/Construction-Safety-Dataset-CSDataset) | OSHA construction incident, inspection and violation records | Not specified | [Paper](https://arxiv.org/abs/2508.09203) |
| [ConstructionSite 10k](https://huggingface.co/datasets/LouisChen15/ConstructionSite) | 10,013 site images with captions, safety VQA and visual grounding | CC BY-NC 4.0 | [Paper](https://arxiv.org/abs/2508.11011) |
| [CrackStructures](https://github.com/ben-z-original/crackstructures) | Multi-view images and meshes of real structures with crack annotations | Not specified |  |
| [dacl10k](https://github.com/phiyodr/dacl10k-toolkit) | ~10k bridge inspection images with 19 damage and component classes | CC BY-NC 4.0 | [Paper](https://arxiv.org/abs/2309.00460) |
| [dacl1k](https://github.com/phiyodr/building-inspection-toolkit) | Bridge inspection images for multi-label concrete defect classification | Not specified | [Paper](https://doi.org/10.1016/j.engappai.2024.109106) |
| [GYU-DET](https://doi.org/10.57760/sciencedb.19893) | Beam bridge images with boxes for six surface defect classes | Not specified | [Paper](https://www.nature.com/articles/s41597-025-05395-w) · [Code](https://github.com/IamSunday/Multi-defect-type-beam-bridge-dataset-GYU-DET) |
| [Hard Hat Workers Dataset](https://public.roboflow.com/object-detection/hard-hat-workers) | 7,041 images annotated for helmets, heads and people | CC0 |  |
| [Hilti SLAM Challenge Datasets](https://hilti-challenge.com/) | LiDAR, camera and IMU sequences from construction sites with mm-level ground truth | CC BY-NC-SA 4.0 |  |
| [MOCS (Moving Objects in Construction Sites)](http://www.anlab340.com/Archives/IndexArctype/index/t_id/17.html) | 41,668 site images with 13 classes of workers and machinery | Custom (research) | [Paper](https://doi.org/10.1016/j.autcon.2020.103482) |
| [Pictor-v3](https://github.com/ciber-lab/pictor-ppe) | Construction worker images labelled for hard hats and vests | Not specified | [Paper](https://doi.org/10.1016/j.autcon.2020.103085) |
| [SDNET2018](https://digitalcommons.usu.edu/all_datasets/48/) | 56,000+ cracked and intact concrete images from bridges, walls and pavements | CC BY 4.0 | [Paper](https://doi.org/10.1016/j.dib.2018.11.015) |
| [SIP (Sites in Pieces)](https://zenodo.org/records/17667735) | Terrestrial laser scans of construction sites with point-level labels | CC BY-NC 4.0 | [Paper](https://arxiv.org/abs/2512.09062) · [Code](https://github.com/syoi92/SIP_dataset) |
| [SODA (Site Object Detection dAtaset)](https://arxiv.org/abs/2202.09554) | ~20k site images with 286k boxes of workers, materials and machines | Custom (research) | [Paper](https://doi.org/10.1016/j.autcon.2022.104499) |
| [Structural Defects Dataset (S2DS)](https://github.com/ben-z-original/s2ds) | Concrete surface images with pixel labels for cracks, spalling and corrosion | Custom (academic only) |  |

## Synthetic Indoor Scenes

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [3D-FRONT & 3D-FUTURE](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-scene-dataset) | 18,968 furnished rooms and 13,151 textured furniture models | Custom (research, registration) | [Paper](https://arxiv.org/abs/2011.09127) |
| [Aria Synthetic Environments (ASE)](https://www.projectaria.com/datasets/ase/) | 100,000 synthetic indoor scenes with renders and structured floor plans | Custom (non-commercial) | [Paper](https://arxiv.org/abs/2403.13064) |
| [Habitat Synthetic Scenes Dataset (HSSD)](https://3dlg-hcvc.github.io/hssd/) | 211 human-authored 3D indoor scenes for embodied AI | CC BY-NC 4.0 | [Data](https://huggingface.co/datasets/hssd/hssd-hab) · [Paper](https://arxiv.org/abs/2306.11290) |
| [Hypersim](https://github.com/apple/ml-hypersim) | 77,400 photorealistic indoor images with depth and semantic labels | CC BY-SA 3.0 | [Paper](https://arxiv.org/abs/2011.02523) |
| [InteriorNet](https://interiornet.org/) | Photorealistic renders of designed interiors with RGB-D and inertial ground truth | Custom (research) | [Paper](https://arxiv.org/abs/1809.00716) |
| [InteriorVerse](https://interiorverse.github.io/) | Photorealistic interiors with material, geometry and lighting ground truth | Custom (agreement) | [Paper](https://doi.org/10.1145/3550469.3555407) |
| [OpenRooms](https://github.com/ViLab-UCSD/OpenRooms) | Photorealistic indoor scenes with material and lighting ground truth | Not specified | [Paper](https://arxiv.org/abs/2007.12868) |
| [ProcTHOR-10K](https://procthor.allenai.org/) | 10,000 procedurally generated interactive 3D houses | Apache 2.0 | [Data](https://github.com/allenai/procthor-10k) · [Paper](https://arxiv.org/abs/2206.06994) · [Code](https://github.com/allenai/procthor) |
| [ReplicaCAD](https://aihabitat.org/datasets/replica_cad/index.html) | Interactive, artist-built versions of Replica apartment scenes | CC BY 4.0 |  |
| [SceneNet RGB-D](https://robotvault.bitbucket.io/scenenet-rgbd.html) | 5M synthetic RGB-D frames of randomized indoor scenes | Not specified | [Paper](https://arxiv.org/abs/1612.05079) · [Code](https://github.com/jmccormac/pySceneNetRGBD) |
| [Structured3D](https://structured3d-dataset.org/) | 3,500 synthetic house designs with structure annotations and panoramic renders | Custom (non-commercial) | [Paper](https://arxiv.org/abs/1908.00222) · [Code](https://github.com/bertjiazheng/Structured3D) |

## BIM Benchmarks & Machine Learning

| Dataset | Description | License | Links |
| --- | --- | --- | --- |
| [AEC-Bench](https://github.com/nomic-ai/aec-bench) | 196 agentic tasks over real construction drawings, specs and submittals | Apache 2.0 | [Data](https://huggingface.co/datasets/nomic-ai/aec-bench) · [Paper](https://arxiv.org/abs/2603.29199) |
| [AECBench](https://github.com/ArchiAI-LAB/AECBench) | ~4,800 AEC questions across 23 tasks for evaluating LLMs | CC BY-NC 4.0 | [Data](https://huggingface.co/datasets/jackluoluo/AECBench) · [Paper](https://arxiv.org/abs/2509.18776) |
| [AECV-Bench](https://github.com/AECFoundry/AECV-Bench) | Floor plan object counting and drawing QA for multimodal models | Not specified | [Paper](https://arxiv.org/abs/2601.04819) |
| [ArchSIBench](https://huggingface.co/datasets/ArchSIBench/ArchSIBench) | Floor plan and spatial diagram VQA for architectural spatial reasoning | Apache 2.0 | [Paper](https://arxiv.org/abs/2605.20837) |
| [BIM Data Repository with Labels (Purdue)](https://purr.purdue.edu/publications/3259/1) | Five Revit models with expert-labelled architectural and structural elements | CC0 |  |
| [BIM-Edit](https://huggingface.co/datasets/BIM-Edit/BIM-Edit) | Natural-language IFC editing tasks with reference output models | CC BY 4.0 | [Paper](https://arxiv.org/abs/2606.20146) |
| [BIMCompNet](https://bimcompnet-606lab.xaut.edu.cn/) | IFC components as meshes, views, point clouds and graphs for classification | MIT | [Data](https://huggingface.co/datasets/YaMiSo1995/BIMCompNet_100-samplesubset/tree/main) · [Code](https://github.com/Yang-Mingsong/BIMCompNet) |
| [BIMGEOM](https://doi.org/10.7910/DVN/YK86XK) | Component geometry from IFC projects for shape-based classification | Not specified | [Paper](https://doi.org/10.35490/EC3.2021.168) |
| [BuildingNet](https://buildingnet.org/) | 2,000 building meshes with 513k labelled parts in 31 classes | Custom (research, form) | [Paper](https://arxiv.org/abs/2110.04955) · [Code](https://github.com/buildingnet/buildingnet_dataset) |
| [BuiltBench](https://github.com/mehrzadshm/built-bench-paper) | IFC and Uniclass-derived retrieval and clustering tasks for text embeddings | CC BY-NC-ND 4.0 | [Data](https://huggingface.co/datasets/mehrzad-shahin/BuiltBench-clustering-s2s) · [Paper](https://arxiv.org/abs/2411.12056) |
| [CODE-ACCORD](https://github.com/Accord-Project/CODE-ACCORD) | 862 English and Finnish building regulation sentences with entities and relations | CC BY 4.0 | [Data](https://zenodo.org/records/10210022) · [Paper](https://www.nature.com/articles/s41597-024-04320-x) |
| [FloorplanQA](https://huggingface.co/datasets/OldDelorean/FloorplanQA-Layouts) | Spatial reasoning questions over structured room layouts | CC BY 4.0 | [Paper](https://arxiv.org/abs/2507.07644) · [Code](https://github.com/OldDeLorean/FloorplanQA) |
| [GeoBIM Benchmark 2019](https://3d.bk.tudelft.nl/projects/geobim-benchmark/) | IFC and CityGML interoperability benchmark with test models | Varies |  |
| [IFC-Bench](https://huggingface.co/datasets/sylvainHellin/ifc-bench) | Questions and answers over real IFC models for LLM evaluation | CC BY 4.0 | [Paper](https://arxiv.org/abs/2605.01698) |
| [IFCNet](https://ifcnet.e3d.rwth-aachen.de/) | 19,613 single IFC objects for BIM element classification | Not specified | [Paper](https://arxiv.org/abs/2106.09712) · [Code](https://github.com/RWTH-E3D/ifcnet-models) |
| [Ishigaki-IDS-Bench](https://huggingface.co/datasets/ONESTRUCTION/Ishigaki-IDS-Bench) | English and Japanese requirements paired with reference IDS files | CC BY 4.0 | [Paper](https://arxiv.org/abs/2605.22079) · [Code](https://github.com/onestruction/Ishigaki-IDS-Bench) |
| [Logic Clause Representation of Building Codes](https://purr.purdue.edu/publications/3881/1) | IBC 2015 sentences as logic clauses for automated compliance checking | CC BY 4.0 |  |
| [SAGC-A68](https://github.com/A2Amir/SAGC-A68) | Space access graphs from 68 apartment models for space and element classification | CC BY 4.0 | [Data](https://doi.org/10.5281/zenodo.7805872) · [Paper](https://arxiv.org/abs/2307.04515) |

## Related lists

- [Awesome CityGML](https://github.com/OloOcki/awesome-citygml): Open semantic 3D city models by country.
- [OpenConstruction](https://www.openconstruction.org/): Catalog of construction and built-environment datasets.
- [awesome-bim](https://github.com/SikongSphere/awesome-bim): BIM software, libraries and tools.
- [awesome-point-cloud-analysis](https://github.com/Yochengliu/awesome-point-cloud-analysis): Point cloud papers and datasets beyond buildings.

## Contributing

All entries live in [`data/datasets.json`](data/datasets.json). This README is generated from it and the website reads it directly. See [CONTRIBUTING.md](CONTRIBUTING.md).

Licenses are shown as stated by each provider. Check the source before use. This list is released under [CC0](LICENSE).
