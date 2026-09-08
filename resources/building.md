# Build resources

Choose tools after identifying the aircraft and laptop. Install one tool, run its smallest example, and record what happened. These links are starting points for the survey; exact hardware support comes from the manufacturer's documentation.

## 1. Start with images

- [OpenDroneMap sample data](https://github.com/OpenDroneMap/odm_data_aukerman): a real image set for practising stitching. Read its data licence and keep the attribution with your copy.
- [OpenDroneMap installation](https://docs.opendronemap.org/installation/): build an orthomosaic from overlapping photographs. Check its current memory and disk requirements against your laptop. A prebuilt orthomosaic lets you start the console while processing is being arranged.
- [NodeODM](https://github.com/OpenDroneMap/NodeODM): an API for running the same processing later, when you want to connect it to your app.

First experiment: display one real image. Next: stitch a small set or open an existing orthomosaic. Write down the source, licence, dimensions and processing time.

## 2. Mark trees and open their images

- [DeepForest](https://github.com/weecology/DeepForest): pretrained tree-crown detection. Compare its boxes with trees you mark yourself. Record missed trees and duplicate detections.
- [Rasterio](https://rasterio.readthedocs.io/): reading geographic images and translating pixels to coordinates.
- [GeoPandas](https://geopandas.org/): handling geographic records. Check coordinate systems and distance units before calculations.
- [ExifRead](https://github.com/ianare/exif-py): reading camera metadata. Match timestamps to the tree targeted during a close-up, then inspect the matches yourself.

Start with a small number of trees and stable IDs. Add automatic detection when the gallery and corrections work. Store the map's coordinate system with its locations.

## 3. Learn from an orchard study

[Development of a Drone-Based Phenotyping System for European Pear Rust](https://www.mdpi.com/2073-4395/14/11/2643) is a worked example of turning aerial observations into a per-tree result. Read its images, method and limitations. It studies pears; use it to understand the process and ask what transfers to apricots.

The associated [pear-rust image dataset](https://data.mendeley.com/datasets/44kjgc4gkc/1) is a candidate for a detection experiment. Check its version, licence, labels and image scale before using it. A result on those images measures performance on that task.

For apricot-specific exploration, inspect [ATZD01](https://github.com/meanlang/ATZD01) and [Apricot-brown-rot on Roboflow](https://universe.roboflow.com/bilal-jan/apricot-brown-rot). Check access and reuse terms, view the images and identify what each label actually describes before downloading or training. Close-up leaf or fruit images answer a different question from an aerial crown image.

A good first comparison: manually mark a small set of real trees; run one existing model; make a gallery of correct and incorrect outputs. Have disease labels checked by someone qualified to assess the condition. A visible concern can still be useful as a prompt for inspection.

## 4. Add a model only where it helps

[Ollama](https://ollama.com/) can run supported local image models; choose a model that fits your laptop and read its model card. A hosted vision API is an alternative if you have agreed credits and data permission. Keep an image-in, observation-out interface so your app can use either.

Record the model name, version, prompt, image and output. Give it a way to return “uncertain”. Keep the human's review in a different field.

Later: [Ultralytics](https://docs.ultralytics.com/) for training a detector and [Label Studio](https://labelstud.io/) for annotation. Read their licences before adding them. Train after you have a clear task and checked labels. Split evaluation by tree or flight so closely related images stay together.

## 5. Connect the aircraft you actually have

- [PX4 simulation](https://docs.px4.io/main/en/simulation/) and [MAVSDK Python](https://github.com/mavlink/MAVSDK-Python): start with the supported simulator and connection example. Simulation still needs the relevant software installed.
- [ArduPilot SITL](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html): test ArduPilot behaviour in software. Use commands documented for the firmware you run.
- [DJI developer site](https://developer.dji.com/): check the exact aircraft, controller and SDK compatibility first. Use a supported photo collection and export workflow where that is the available interface.
- [QGroundControl](https://qgroundcontrol.com/): a ground-control tool for supported aircraft. Follow the aircraft's own supported setup.

Survey first. Then test a single close-up target in simulation. Choose viewpoints from obstacles, camera resolution and measured positioning accuracy; a fixed orbit radius will fit only some sites. Record pilot takeover tests and distinguish simulated from field results.

## 6. Ask the community

[ArduPilot forum](https://discuss.ardupilot.org/), [PX4 community](https://px4.io/community/) and [OpenDroneMap community](https://community.opendronemap.org/) are good places to learn. Search existing discussions. When asking, include the exact version, setup, expected result, actual result and a small reproducible example.

For operating rules, use [EASA](https://www.easa.europa.eu/en/the-agency/faqs/open-category) and the [Czech CAA](https://www.caa.gov.cz/en/). Complete LEGAL.md with the pilot before a field session.

## How to find the next resource

Use a precise question: “tree crown detection orthomosaic”, “apricot brown rot field image dataset”, or your aircraft model plus “SDK waypoint camera”. Prefer the original paper, dataset page and official software documentation. Record the date, licence and what you actually verified.

The earlier broad [dataset research snapshot](https://github.com/latintzar/apricot-drone-hackathon/blob/710f00670089e3bc21d1bfbbeb5cd8a709d550d5/README.md#appendix) remains in repository history for deeper searches. Treat its access, version and performance claims as leads to check against the original source.
