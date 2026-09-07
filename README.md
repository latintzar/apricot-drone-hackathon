# The Apricot Drone Hackathon

Brief for Ilian. Three weeks, one open-source project, published. September 2026.

## Definitions

Open source. Software whose code is public, under a licence that lets anyone read, use, change and share it. Most of the tools in this brief are open source. This project will be too.

Licence. The file that says what others may do with your code. MIT lets anyone do almost anything with attribution. Apache-2.0 is similar with a patent clause. AGPL, used by OpenDroneMap and Ultralytics, requires that changes are shared under the same terms.

Git. The tool that records every change to a folder of files, with who made it and when. A commit is one recorded change with a one-sentence message. A branch is a parallel line of changes. Git runs on your laptop.

GitHub. The website where git folders are stored and shown publicly. A repository, or repo, is one project on it: the code, the README, the history. Your GitHub profile is the list of your repositories and is what employers open first.

README. The first file a visitor reads, shown on the repository's front page. Written in Markdown, a plain-text format where # makes a heading and - makes a bullet.

Issue. A numbered note on a repository: a bug, a task, a question. This project closes each level with an issue titled "done".

Pull request, or PR. A proposed change to someone else's repository, reviewed before it is merged. A merged pull request to a project like ArduPilot is public proof of your work.

Fork. Your own copy of someone else's repository, where you make changes before proposing them as a pull request.

Star. A bookmark on a repository. Counts of stars are a rough measure of how many people use a project.

Template repository. A repository that GitHub can copy in one click to start a new one with the same files. This hackathon ships one.

CLAUDE.md. A file at the root of a repository that Claude Code reads at the start of every session: what the project is, the rules, where things stand.

Aircraft. The drone you have. Make, model, weight, payload margin, flight time, camera, sprayer.

Flight controller. The board inside the aircraft that keeps it in the air. It runs a flight stack: PX4 or ArduPilot, which are open, or DJI's own, which is closed.

MAVLink. The message protocol PX4 and ArduPilot speak. Your code sends waypoints and reads position, battery and heading over it.

Companion computer. A small computer on the aircraft, a Raspberry Pi or a Jetson, that runs your code and talks MAVLink to the flight controller. On a DJI aircraft, the Android phone in the controller plays this role through DJI's Mobile SDK.

Ground station, or hub. The laptop in the garden. Receives packets from the aircraft, stores them, runs the models, sends the next mission.

Waypoint mission. A list of positions the aircraft flies on its own. A grid survey is one. An orbit is one: a circle around a point at a set radius and height, nose to the centre.

Orthomosaic. One large top-down image of the orchard stitched from hundreds of photos, with real coordinates. OpenDroneMap makes it.

Tree crown. The outline of one tree seen from above. DeepForest finds them.

Detector. A model that draws boxes on images and names what is in them. YOLO is the standard one. You train it on labelled images.

Vision model. A general model that takes an image and a question and answers in text or JSON. Runs locally through Ollama, or through an API.

Console. The web app where a person sees the orchard map, the proposals and the galleries, and taps decisions.

Level. One of the three stages of this project. Each is complete before the next starts.

Log. LOG.md in the repository. One entry per thing shipped, same day.

Field note. One file per flight: conditions, plan, what happened, numbers, what changes.

Replay. A recorded flight anyone can run through the software on a laptop with no drone.

## The brief

### What to build

An open-source system for a drone that:

1. Flies a grid over a small apricot orchard on its own and photographs every tree.
2. Stitches the photos into a map, finds every tree, and colours each one: green for fine, amber for look closer, red for risk, with the type of risk named.
3. Proposes which trees to inspect and from which side. The person approves, removes or adds with a tap.
4. Flies to each approved tree, circles it at six to eight metres, and takes a photo every thirty degrees.
5. Files every photo under the tree it was pointed at, and shows a gallery of tiles per tree. Tap a tile to open it, tap again to close.
6. On a tap and a confirmation, flies above a chosen tree and sprays it, with a progress bar, a stop button that works, and a "spraying done" record with time, amount and a photo.

The person decides at every step. The model reads first and proposes. Every tap is a label the model learns from.

The first orchard is your aunt's garden in the Czech Republic. Your uncle flies it there from a one-page pack you write. The aircraft, camera, sprayer and laptop are the ones you have; this brief describes the function and never the parts. Day one is finding out exactly what you have and writing it down.

### The three levels

Level one, survey and console. Grid flight at fixed height, geotagged photos, orthomosaic, tree crowns found, each tree given a number that stays the same on every flight. Each crown cropped and sent to a vision model with one question: what do you see, how sure are you, which of these diseases could it be. The answers colour the map and label each tree. The console shows the map, the proposals, and the taps. On day one the model is a small open vision model on your laptop through Ollama. Done when: the map is coloured from a real flight and a tap produces a mission file.

Level two, orbit and gallery. Each approved tree gets an orbit mission. PX4 has orbit mode, ArduPilot has circle mode and loiter-turns with a region of interest, DJI's SDK has a point-of-interest mission. Every photo is filed under its tree by logging the tree number when the orbit is commanded and matching by timestamp. The console shows a tile gallery per tree. The model re-reads the close-ups and updates the colour and label. In parallel, a YOLO detector is trained on the crops and close-ups labelled by tapping. Done when: an approved tree produces close-ups in its gallery from a real flight, and a training run has a metrics table and a failure gallery.

Level three, treatment. The spray command executes on the sprayer the aircraft has. On PX4 or ArduPilot the pump is a servo or relay output; ArduPilot has a built-in sprayer function. On a DJI agricultural aircraft it goes through DJI's app and SDK. Spray water while building. A page called LEGAL states what the Czech authorities allow. Done when: a tap sprays a tree, the console shows progress and the stop works, and the record is written. Scheduled for spring, when the blossom shows the fungus.

If the model sees nothing useful from the air, write that in the log with the images that show it. The console with a person deciding remains the product.

### Deliverables

1. The repository, public from day one. README with a story at the top, a true status line, a five-minute replay, the console, the mission code, the model with its training runs and failure gallery, HARDWARE.md with parts and prices, LEGAL.md, field notes, and the one-page pack for your uncle.
2. A two-minute video: takeoff, the console, a tap, the aircraft moving, the close-up appearing.
3. A media folder collected from day one: the aircraft on the grass with the orchard behind it, a ten-second takeoff clip, a screen recording of the console and one of the gallery saved as GIFs, the orthomosaic, a sick tree beside a healthy one, the failure gallery as a nine-image grid, the training curve, the wiring labelled, your uncle holding the pack next to the aircraft, the spray test. Phone in landscape, raw files kept.
4. LOG.md. One entry per shipped thing: date, what shipped, what broke, the number that changed, one photo.
5. Reflections. One per part, on the template in the guidance section.
6. The project page and four Substack posts.

### Rules

1. The repository is public from day one and says nothing flies yet.
2. Something ships every three days. A shipped thing is a commit, a log entry and a picture.
3. Every number in the repository is one you measured. Unfinished work says "works up to step three".
4. The pilot holds the controller and can abort at any moment.
5. The brief describes the function, never the parts. Find out what you have and write it down first.
6. Judged on four things in order: it works; a stranger understands it in a minute; it is honest; someone else could build it from what you wrote.
7. Elena joins on any piece she picks. The console is the natural one. Her name goes on the repository for what she built.

### The three weeks

Days 1 to 3. Identify the aircraft, flight stack, camera path and sprayer. Get camera and GPS into your own code. Repository public, story and status line written. Console sketched on paper: the map, the trees, the three taps.

Days 4 to 9. Grid mission planned in software, flown, photos geotagged, orthomosaic made. Trees found and coloured by the vision model. Proposals and taps working in the console, even before a tap can fly. First field note.

Days 10 to 18. A tap flies: go to the tree, descend, circle, a photo every thirty degrees, return. Photos filed by tree, gallery built. A flight recorded for the replay. First dataset labelled, first detector trained, metrics table and failure gallery. Second field note.

Days 19 to 21. README finished for what exists. Video cut. Reflections written. Project page published. Thirty emails sent.

Term time, weekends: the model re-reading close-ups, the detector improving, the pack in your uncle's hands until his flight succeeds first time. Spring: level three.

Each level closes with an issue on the repository titled "done", stating what works, what does not, and linking the field note. Twenty minutes a week on a screen share with me.

## Resources

### Where the brain lives

The aircraft carries a camera and a radio. The ground station carries the models. The aircraft sends small packets: a 640-pixel JPEG, position, altitude, heading, battery. WiFi covers an orchard; a 4G dongle covers more.

The model that reads the trees is a part you choose. One interface, image in and JSON out, with interchangeable backends: a small open vision model through Ollama on the laptop, free; a hosted API, cents per call, if you have credits; your own trained detector once it exists; a Jetson on the aircraft running the small model in the air. The console never notices a swap.

Diseases on apricot in Central Europe: Monilinia, seen as withered brown blossoms and mummified fruit; shot hole, seen as red spots on leaves that fall out and leave holes. Photograph what your aunt's trees actually have. Labels come from that.

### Get to working condition

Accounts, all free, opened by you: GitHub and the GitHub Student Developer Pack with your university email, which includes a free domain for a year. Vercel with your GitHub login. Substack. Roboflow, Kaggle, Hugging Face. The Dronecode Discord or the ArduPilot forum, whichever your aircraft runs, and the OpenDroneMap forum. A domain in your name, about ten euros, or the free one from the pack.

On the laptop: Python 3.11 or newer, git, uv or pip, Node. Ollama with gemma3 or qwen2.5vl pulled. QGroundControl. The simulator for your flight stack: PX4 with SIH, or ArduPilot SITL. From pip: mavsdk, deepforest, ultralytics, exifread, geopandas, label-studio. OpenDroneMap through Docker, or WebODM. FiftyOne.

On the aircraft side: the manual for the aircraft, flight controller and sprayer, with the SDK or MAVLink pages marked. Spare propellers, two charged batteries, an empty SD card, a tested way to get photos off the aircraft. A laptop with 16 GB of memory for stitching, borrowed if needed.

Working condition is reached when: the aircraft shows in QGroundControl with a GPS fix; your script flies an orbit in the simulator; DeepForest draws boxes on the OpenDroneMap sample dataset; Ollama answers a JSON question about a photo; the repository is public. Write the date in the log as the first entry.

### The reflection template

One file per part, in a folder called reflections, written the day the part ships: the aircraft, the mission code, the console, the model, the field work, the pack, and one for the whole three weeks. Two hundred to four hundred words each, in this order:

1. What I thought this part would be, including how long.
2. What it actually was: what broke, what surprised me, when it worked.
3. The numbers: time, flights, metric, cost.
4. What I would do differently starting tomorrow.
5. One sentence for someone starting this part today.
6. What I still do not understand.
7. One picture with a caption.

### The project page

A domain in your name. Under it, two things, both free to host. The project site on GitHub Pages from the docs folder: video at the top, the story, a picture per level, the map, the console GIF, the numbers, the reflections, the link to the code. The live demo on your own free Vercel account: the console loaded with a recorded flight, so anyone can tap a tree, open the gallery, tap spray and watch the bar fill against the log, with no drone and no login. Build the console so the same code runs live and replayed.

Substack, four posts: day one, end of level one, end of the detector, "What I built in three weeks" with the video. The last one to Hacker News as "Show HN".

### Use Claude Code for these things

You have Claude Code for a week, and so does Elena. It plans, scaffolds, writes the boring parts and reviews. You fly, tap, measure, read the companies, write the cold open, buy the domain, open the accounts, send the emails. The coding tool and the model that reads the trees are separate choices.

Paste this as the first message of a fresh session. It fetches both documents, writes the CLAUDE.md for your repository, and interviews you.

```
You are helping me, Ilian, run a three-week hackathon. Fetch and read the entire brief before you do anything: https://docs.google.com/document/d/1Rqya11yWo3ofDksrC8zOAxPk4b-aKyySU54kC-GBjOY/export?format=md and then the second document, the world around it: https://docs.google.com/document/d/1oEdlMkH0Jt4XT4hXbxiMSBMVuDwneJGdMVBhBUzK_Bk/export?format=md

Rules that never change:
- I do the work. You plan, scaffold, write the boring parts, review, and ask. When something needs running, flying or measuring, tell me what to run and wait for me to paste the real output.
- Interview me before you assume anything about the aircraft, the sprayer, the orchard, or my time. Start with the day-one questions in the brief, one at a time.
- Reading companies, their websites and their people is my job. You tighten what I wrote and keep the sheet.
- When I ask you to mentor me, tell me the truth about my work. Name what is weak, say why, and show what strong looks like.
- Every number in the repository is one I measured. Where you do not know, write "[measure this]".
- Short sentences. Say what a thing is. Sentence-case headings. Commit after every step with a one-sentence message.
- Keep CLAUDE.md at the repository root current: the aircraft, the flight stack, the sprayer, the conventions, the level I am on, and the job we are doing. You read it every session.

First, write CLAUDE.md from the brief and this message. Then state the three levels in three sentences, and ask me the first day-one question.
```

Day-one questions it will ask:

1. The exact aircraft: make, model, take-off weight, payload margin, flight time, camera, sprayer.
2. The flight controller: DJI with its Mobile SDK, or PX4 or ArduPilot with MAVLink and a companion computer.
3. How the live camera feed and GPS reach your own code.
4. The ground station: laptop on WiFi, or 4G dongle on the aircraft.
5. The diseases seen, and whether photos exist.
6. Number of trees, plot size, surroundings.
7. Days available, and whether a GPU is available.

Jobs, one sentence at the start of a session:

- Do my GitHub. "Read my three repositories and write READMEs that are true." One sentence on what each does, one image, how to run it, what you learned, "works up to step three" where unfinished.
- Working condition. "Get me to working condition." It checks installs, lists the accounts to open, and stops when the five conditions hold.
- Build. "Level one, day four. Plan the grid mission module and its tests, then wait." It plans, you cut what you do not understand, it writes, you run.
- Write. "Turn today's log entry into the reflection for the console." Seven questions, your numbers, blanks where it has none.
- Publish. "Set up the project site and the live demo." GitHub Pages, the Vercel deploy from the console folder with a recorded flight, DNS, a Substack template.
- Judge. "Judge the repository as a stranger." The four questions, then a list to fix.
- Mentor. "Be my mentor today." A call tomorrow, a paper half understood, what to learn next, a mock interview, the truth about a post. Ends with one thing to do before next time.

### Datasets, pointers and links

Every link was opened this week. The full list with licences and sizes is the appendix at the end.

The apricot set. Roboflow user bilal-jan publishes "Apricot-brown-rot": 135 photos, CC BY, classes brown rot and gummosis, plus 149 healthy apricots. universe.roboflow.com/bilal-jan/apricot-brown-rot. Related papers: Jamil Ahmad and Bilal Jan, plum brown rot and shot hole on phone photos, Sensors 2020, the method template. Jamil Ahmad, apricot brown rot and shot hole from a DJI Mavic Mini, Expert Systems with Applications 2025, dataset unpublished. Email him on day one and ask for it.

Day one, five links. The pear rust paper, Agronomy 2024, this project on pears with a five-band per-tree colour map: mdpi.com/2073-4395/14/11/2643. Its dataset, the only drone-altitude tree-disease set in the open, 584 annotated images at 5 to 12 metres, YOLO format, CC BY: data.mendeley.com/datasets/44kjgc4gkc/1. DeepForest for tree crowns, with a dead-versus-alive crown classifier: github.com/weecology/DeepForest. The MAVSDK orbit example: github.com/mavlink/MAVSDK-Python/blob/main/examples/do_orbit.py. OpenDroneMap install, 16 GB RAM for 250 images, GPU irrelevant: docs.opendronemap.org/installation.

Datasets to download this week, CC BY unless stated. ATZD01, 6,055 apricot photos, 20,272 boxes, 11 classes including 9,023 shot-hole and 480 brown-rot instances; password-gated, request access on day one at github.com/meanlang/ATZD01. Peach Disease by zeerox on Roboflow, 1,081 photos with boxes for brown rot, shot hole, bacterial spot: universe.roboflow.com/zeerox/peach-disease. PlantCity, 10,667 field photos including 208 apricot shot-hole leaves: data.mendeley.com/datasets/w8kh2xkspx/4. Turkey plant dataset, names Monilinia laxa on apricot: github.com/mturkoglu23/PlantDiseaseNet. CherryLeaf-KG, 400 cherry leaves with shot hole and brown rot, use as the test set: data.mendeley.com/datasets/wp3b6pz9gc/3. Plum set with 643 shot-hole images: data.mendeley.com/datasets/w7sdx55m7z/1. Cherry orchard drone set, 42 GB, 577 trees from the air and the ground across a season with a severity grade each; copy its structure: zenodo.org/records/7144071. Fire-blight close-ups whose "maybe" class is a ready "send a human" bucket: data.mendeley.com/datasets/fpmnncmg84/1.

Searched and empty: Eutypa images, bacterial canker on stone fruit, any apricot orchard from above. The two 875-image "shot hole" sets on Roboflow are grapevines.

Building blocks. Crowns: DeepForest for boxes, segment-geospatial for polygons with coordinates, github.com/opengeos/segment-geospatial. Stitching: ODM, NodeODM as the API, a geo.txt whose spare column carries the tree number: docs.opendronemap.org/geo. Orbit: PX4 orbit mode, docs.px4.io/main/en/flight_modes_mc/orbit.html, one metre a second, nose to centre, cannot arm in orbit so take off in another mode; ArduPilot circle mode or loiter-turns with region of interest, which persists until cleared: ardupilot.org/copter/docs/circle-mode.html. DroneKit is unmaintained since 2019; use MAVSDK. Simulation: PX4 SIH, nothing to install: docs.px4.io/main/en/simulation. Photos to trees: log the tree number and time at each orbit command, match by timestamp. Training: Ultralytics for YOLO, Label Studio with its ML backend for pre-labelling, FiftyOne to inspect. Proposals: TypeFly, github.com/typefly/TypeFly, a language model planning drone actions from a detector's view; DeepDrone, github.com/evangelosmeklis/deepdrone, a web console with live map, planner, replay and emergency stop. Pump: ArduPilot sprayer, SPRAY_ENABLE and an output with function 22, one MAVLink command on and off: ardupilot.org/copter/docs/common-sprayer.html. PX4: set_actuator on a peripheral output: docs.px4.io/main/en/payloads/generic_actuator_control.html.

Law. Article 9 of EU Directive 2009/128 requires member states to prohibit aerial spraying, with derogations only for approved products and certified operators. Spray water. State it on the page. The contribution is the targeting with a person approving and a stop button.

Search. Google Scholar: apricot "brown rot" OR "shot hole" detection UAV deep learning. GitHub: orchard drone stars:>5 pushed:>2025-01-01; path:*.py "do_orbit". Roboflow: class:"apricot leaf". Zenodo API: zenodo.org/api/records?q=orthomosaic+AND+orchard&type=dataset. Czech terms: peckoviny, meruňka, moniliová spála peckovin, suchá skvrnitost listů peckovin, šarka. Portal: rlportal.ukzuz.cz.

Two things that eat time: installing Detectron2, so use DeepForest boxes unless they fail; adopting ROS 2, which MAVSDK makes unnecessary. Two things that save time: the SIH simulator; logging the tree number at the orbit command.

## Appendix

### Datasets, papers and open-source pointers, full list

Every link fetched on 2026-09-07 and returned real content (Opus agent, max effort). "Not found" is a real search that came back empty.

#### Read this first — the five links for day one

**1** (https://www.mdpi.com/2073-4395/14/11/2643 — \*Development of a Drone-Based Phenotyping System for European Pear Rust\* (Agronomy 2024)). Why: This project, already built and published, on pears. Two DJI P4P nadir flights at 17 m and 8 m, orthomosaic, YOLOv5lu at mAP@50 81.25%, symptom boxes → GPS → QGIS, divided by canopy area = infestation intensity in symptoms/m² on a 5-band scale. That is the colour-coded risk map.

**2** (https://data.mendeley.com/datasets/44kjgc4gkc/1 — GYMNSA pear rust UAV dataset, CC BY 4.0). Why: The only drone-altitude tree-disease detection dataset in the open. 584 annotated + 162 background images, 768×768, 16,251 annotations, 5–12 m AGL, pre-split in YOLO format.

**3** (https://github.com/weecology/DeepForest — MIT, 771 stars, pushed 2026-08-30). Why: `pip install deepforest`, pretrained crown model on the orthomosaic → per-tree boxes in an afternoon. Ships an alive/dead crown classifier (ResNet-50, 6,342 crops, 95.8%) = a risk signal on day one. Docs: https://deepforest.readthedocs.io/en/latest/

**4** (https://github.com/mavlink/MAVSDK-Python/blob/main/examples/do_orbit.py). Why: Orbit-a-tree in ~40 lines.

**5** (https://docs.opendronemap.org/installation/ + https://github.com/OpenDroneMap/odm_data_aukerman (CC0, 77 images, 543 MB)). Why: Stitching. 16 GB RAM handles ~250 images; "a GPU currently has no impact on performance". Aukerman is the 5-minute smoke test.

#### 1. The apricot paper

**No paper or dataset called "Apricot" with an author Belal Jan / Bilal Yan exists** (Crossref, Semantic Scholar, Mendeley Data, Kaggle, Zenodo, Roboflow Universe, Data in Brief all searched). **Bilal Jan is real** (Semantic Scholar 36029268, FATA University / Islamia College Peshawar, 33 papers); his one plant-disease paper is on plum. His co-author **Jamil Ahmad** is first author of the apricot UAV paper. **Wentao Yan** is on the Apnet apricot paper. The memory blends these.

**Candidate 1 — the apricot + drone paper (most likely what was remembered).** \*Leveraging model explainability and fine-grained cutmix augmentation for robust detection of apricot diseases in UAV images\*, Jamil Ahmad (UAE University, corresponding), Gueaieb, El Saddik, De Masi, Karray. Expert Systems with Applications 296, 128946, online 2025-07-17. DOI 10.1016/j.eswa.2025.128946. Apricot fruit and leaf images with boxes, Khyber Pakhtunkhwa, **DJI Mavic Mini**, 12 MP, ~1,500 images, classes **brown rot** and **shot hole**. **Dataset not public** (Unpaywall: closed). **Email Jamil Ahmad and ask** — exact crop, exact diseases, exact camera class.

**Candidate 2 — Apnet / ATZD01, the largest public apricot dataset.** \*Apnet: Lightweight network for apricot tree disease and pest detection in real-world complex backgrounds\*, Minglang Li, Zhiyong Tao, **Wentao Yan**, Sen Lin, Kaihao Feng (Liaoning Technical University). Plant Methods 21:4 (2025), open access, DOI 10.1186/s13007-025-01324-5. Dataset **ATZD01**: https://github.com/meanlang/ATZD01 — **6,055 images, 20,272 instances, 15.4 GB**, YOLO format, 11 classes incl. **Bacterial Shot Hole (9,023)**, **Brown Rot (480)**, Gummosis, Scabbed Disease, Anthracnose, mites and pests. Ground-level close-ups in three orchards over 5 months. **The OneDrive mirror is dead; Baidu Pan needs an account, password \`0wm3\`, and a decompression password by application; no licence declared.** Open a GitHub issue and email Prof. Zhiyong Tao's group on day one — it takes days.

**Candidate 3 — the plum paper Bilal Jan actually wrote.** \*Disease Detection in Plum Using Convolutional Neural Network under True Field Conditions\*, Jamil Ahmad, **Bilal Jan**, Haleem Farman, Wakeel Ahmad, Atta Ullah. Sensors 2020, 20(19), 5569, CC BY, DOI 10.3390/s20195569. 5,000 originals → 100,000 augmented, phones, Swat district, 5 classes: healthy, brown rot, shot hole (fruit), shot hole (leaf), nutrient deficiency. **Dataset not published.** Plum is \*Prunus\* like apricot and the two diseases are exactly the ones that matter; the paper is the method template (Inception-v3 transfer learning, 92%+).

Not it: \*APRICOT: A Dataset of Physical Adversarial Attacks on Object Detection\* (ECCV 2020) — adversarial patches, skip.

#### 2. Every other dataset

\#### (a) Stone-fruit leaf and fruit disease sets

**Plantae_K (has apricot)** (https://data.mendeley.com/datasets/t6j2h22jpx/1). Licence: CC BY 4.0 · Size: 2,157 (1,223 healthy / 934 diseased) · Classes: 16 = 8 species × healthy/diseased incl. Apricot, Cherry, Peach · Type: Leaf, DSLR · Use: Fine-tune and evaluate

**PlantCity (has apricot)** (https://data.mendeley.com/datasets/w8kh2xkspx/4 · paper 10.1016/j.dib.2025.112130). Licence: CC BY 4.0 · Size: 10,667 → 52,219 augmented · Classes: 52 across 12 crops incl. Apricot · Type: Leaf, smartphone, field · Use: Biggest apricot-bearing leaf set

**Apricot slice of PlantCity** (https://www.kaggle.com/datasets/codewithsk/apricot-leaf-diseases-on-plantcity-2025). Licence: ODbL · Size: 405 MB · Classes: 3 · Type: Leaf · Use: Drop-in apricot leaf classifier

**PlantVillage (peach)** (https://github.com/spMohanty/PlantVillage-Dataset · HF https://huggingface.co/datasets/mohanty/PlantVillage (cc-by-sa-3.0) · Kaggle https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset (CC BY-NC-SA)). Licence: mirrors differ — cite one · Size: Peach bacterial spot 1,000, peach healthy 360 · Classes: 38 · Type: Leaf, studio · Use: Baseline

**Plum leaf + fruit (DiB 2025)** (https://data.mendeley.com/datasets/w7sdx55m7z/1 · paper 10.1016/j.dib.2025.111625). Licence: CC BY 4.0 · Size: 3,554 + 18,000 aug · Classes: 6 incl. Shot Hole, Bacterial Spot · Type: Leaf + fruit · Use: Only public labelled shot-hole images; "plum" here is jujube — symptom morphology only

**Roboflow apricot projects** (https://universe.roboflow.com/fyp-1/apricot-disease-dataset-1tino (431, 5 cls) · https://universe.roboflow.com/fyp-1/apricot-disease-datasetv04 (137; Brown-rot, Powdery-mildew) · https://universe.roboflow.com/kayisi/apricot (150; apricot / tree(side) / tree(up)) · https://universe.roboflow.com/wad-i799x/apricot-healthy-leaf (68) · https://universe.roboflow.com/abdullah-kqdi3/apricot-icg0y (104)). Licence: CC BY 4.0 · Size: tiny · Classes: see left · Type: mostly close-up; `kayisi` is whole-tree · Use: YOLO format, one click; bootstrap the pipeline on day two

**Peach / cherry augmented** (https://www.kaggle.com/datasets/shuvokumarbasak2030/peach-leaf-diseases-plant-village-augmented-data · …/cherry-leaf-diseases-plant-village-augmented-data). Licence: MIT · Size: ~1 GB / 736 MB · Classes: PlantVillage classes · Type: Leaf · Use: More data

Almond: not found.

\#### (b) Specific pathogens — mostly not found

- Monilinia / brown rot: no dedicated public set (Roboflow \*Apricot-brown-rot\*, 135 images, listing only). Kaggle `monilinia` = 0. Zenodo sweep = wood-decay fungi only.
- Shot hole: only the plum DiB class and ATZD01's 9,023 instances.
- Bacterial canker: not found; proxies PlantVillage peach bacterial spot, plum Bacterial Spot.
- Eutypa: not found.

\#### (c) UAV / orchard datasets

**Cherry Tree Disease Detection** (https://zenodo.org/records/7144071). Licence: CC BY 4.0 (Zenodo copy) · Size: 42.14 GB · Type: UAV RGB + multispectral + NDVI + ground RGB of the same 577 cherry trees, full season, 4 severity stages by an agronomist · Use: Closest analogue to the whole project — per-tree graded severity, aerial + ground

**Pistachio orchard nadir + oblique** (https://zenodo.org/records/7271542 · https://www.mdpi.com/2306-5729/7/11/157). Licence: CC BY 4.0 · Size: 22.28 GB, 248 images · Type: UAV −90° and −60°, 55 m, with GCPs, point cloud, DEM, orthomosaic · Use: Photogrammetry sandbox with correct outputs

**NeonTreeEvaluation** (https://github.com/weecology/NeonTreeEvaluation · https://zenodo.org/records/5914554). Licence: CC BY 4.0 · Size: 8.35 GB, 30,975 annotations · Type: Airborne RGB + LiDAR + hyperspectral · Use: Crown detection train/eval (forest)

**MillionTrees** (https://milliontrees.idtrees.org/ · https://github.com/weecology/MillionTrees). Licence: GPL-3.0 code · Size: 292 GB · Type: airborne RGB · Use: Too big — cherry-pick one source

**detectree2 sample** (https://github.com/PatBall1/detectree2 · DOI 10.5281/zenodo.8136161). Licence: CC BY 4.0 · Size: 10.92 GB · Type: Orthomosaic + crown polygons · Use: Crown segmentation worked example

**ODM samples** (https://www.opendronemap.org/odm/datasets/ — seneca (CC0, 168 farm images), aukerman (CC0, 77), brighton_beach (BSD-2, 19 + ortho + .laz), rv_nir (CC0, 566 NIR)). Type: UAV nadir · Use: Stitching sandbox

**Agriculture-Vision** (https://www.agriculture-vision.com/agriculture-vision-2021/dataset-2021 · https://registry.opendata.aws/intelinair_agriculture_vision/). Licence: in bucket · Size: 94,986 images · Type: UAV RGB+NIR, 9 anomaly classes · Use: Aerial anomaly segmentation reference

**WeedMap** (https://projects.asl.ethz.ch/datasets/weedmap-2018/). Licence: not stated · Size: 18,746 images, 5.36 GB · Type: orthomosaics + tiles, RGB/CIR/NDVI · Use: orthomosaic → tiles → pixel labels → map pipeline

**UAV LiDAR fruit orchards (Poland)** (https://zenodo.org/records/15831891). Licence: CC BY 4.0 · Size: 0.71 GB · Type: LiDAR, 476 apple / 705 cherry / 607 peach trees · Use: Per-tree canopy geometry on stone fruit

**Apple MOTS** (https://zenodo.org/records/5939726). Licence: CC BY 4.0 · Size: 5.66 GB · Type: 86,000 apple instances, 1,700 frames · Use: Keep identity across a moving camera = the orbit problem

**Campaneta orange orchard** (https://zenodo.org/records/17866344). Licence: CC BY 4.0 · Size: 20.9 GB · Type: DJI Mavic 3 Multispectral at 14 m, 5 bands, 301,232 fruit instances · Use: The exact flight profile

**Embrapa ADD 256** (https://github.com/thsant/add256). Licence: CC BY-NC 4.0 · Size: 2,400 images, 256×256 · Type: UAV low-res apples · Use: Does your model survive a cheap camera

**Haly.ID pear orchard** (https://zenodo.org/records/20431348). Licence: CC BY 4.0 · Size: 41 GB · Type: UAV + canopy cams + microclimate, 2021–23 · Use: Risk over a season

**FlexiGroBots blueberry** (https://zenodo.org/records/7775448). Licence: CC BY 4.0 · Size: 12.9 GB · Type: raw UAV + orthomosaics · Use: Validate your stitch

**AgML (Hugging Face)** (https://huggingface.co/Project-AgML · https://github.com/Project-AgML/AgML). Licence: per dataset · Size: 100+ · Type: `apple_detection_drone_brazil`, `olive_tree_crown_detection` (CC BY 4.0), `almond_bloom_2023`, `peachpear_flower_segmentation`, `plum_leaf_fruit_disease_classification` · Use: Standard loaders

**digital-agriculture-datasets index** (https://github.com/ricber/digital-agriculture-datasets). Licence: GPL-3.0 · Use: Twenty minutes well spent; no stone-fruit UAV disease entry exists = the gap

\#### (d) Aerial disease detection for fruit trees

**GYMNSA pear rust UAV** (https://data.mendeley.com/datasets/44kjgc4gkc/1 · paper https://pmc.ncbi.nlm.nih.gov/articles/PMC11783052/). Licence: CC BY 4.0 · Size: 584 + 162 bg, 768×768, 16,251 ann · Classes: 1 (GYMNSA) · Type: UAV nadir + oblique, 5–12 m, GSD 0.17 cm/px, Phantom 4 Pro V2 + M300 RTK · Use: Train YOLO as-is; fly apricots at 5–12 m; demo the transfer honestly

**ERWIAM fire blight** (https://data.mendeley.com/datasets/fpmnncmg84/1 · paper https://pmc.ncbi.nlm.nih.gov/articles/PMC11385024/). Licence: CC BY 4.0 · Size: 1,698 images, 1280×1280, 15,761 ann · Classes: MAYBE\_, FLOWER, LEAF\_\_, SHOOT\_ · Type: close-range handheld · Use: The inspect half; `MAYBE\_` = the "send a human" bucket, already labelled

**Olive Verticillium wilt UAV** (https://zenodo.org/records/8144164 · https://www.mdpi.com/1999-4893/16/7/343). Licence: CC BY 4.0 · Size: 4.45 GB, 160 tiles, 3,038 trees · Classes: damaged / healthy · Type: orthomosaic tiles, whole crowns · Use: Exactly the per-tree label shape

**AppleScabFDs** (https://zenodo.org/records/13353948). Licence: CC BY-NC-ND 4.0 · Size: 0.76 GB · Classes: Healthy / Scab · Type: field close-ups · Use: demo-only (no derivatives)

#### 3. Building blocks

\#### 3.1 Tree detection

- **DeepForest** https://github.com/weecology/DeepForest (MIT). Docs https://deepforest.readthedocs.io/en/latest/ (v2.1.0; v1 pages still indexed, different API). Prebuilt: https://deepforest.readthedocs.io/en/latest/user_guide/02_prebuilt.html — `from deepforest import main; m = main.deepforest(); m.load_model(model_name="weecology/deepforest-tree")`; alive/dead crown classifier; `CropModel` for a secondary per-crown classifier. Python ≥3.10.
- **segment-geospatial (samgeo)** https://github.com/opengeos/segment-geospatial · https://samgeo.gishub.org/ — SAM on georeferenced rasters → GeoJSON polygons. The glue.
- SAM 2 https://github.com/facebookresearch/sam2 (Apache-2.0); SAM 3 https://github.com/facebookresearch/sam3 (check licence). SAM 1 frozen.
- detectree2 https://github.com/PatBall1/detectree2 (MIT) — polygons via Detectron2; **installation is the risk; no weights checked in.**
- Others: https://github.com/open-forest-observatory/tree-detection-framework (fresh), https://github.com/AWF-GAUG/TreeCrownDelineation. pycrown archived — skip.
- **Spine:** DeepForest boxes → samgeo/SAM 2 polygons → DeepForest alive/dead as first risk signal.

\#### 3.2 Stitching

- ODM https://github.com/OpenDroneMap/ODM (AGPL-3.0); WebODM https://github.com/OpenDroneMap/WebODM (canonical now WebODM/WebODM). Requirements https://docs.opendronemap.org/installation/ — 4 GB RAM minimum (100–200 images), 16 GB recommended (250), GPU irrelevant.
- **NodeODM** https://github.com/OpenDroneMap/NodeODM — REST: `POST /task/new`, `/task/new/init` → `/upload/{uuid}` → `/commit/{uuid}`, `GET /task/{uuid}/info`, `/download/{asset}`, `POST /task/cancel`. Your programmatic hook.
- `geo.txt` https://docs.opendronemap.org/geo/ — `image_name geo_x geo_y \[z\] \[yaw\] \[pitch\] \[roll\] \[hacc\] \[vacc\] \[extras\]`; the extras column can carry `tree_id`.

\#### 3.3 Orbit / point of interest

- **PX4 Orbit mode** https://docs.px4.io/main/en/flight_modes_mc/orbit.html — 1 m/s clockwise default; radius 1 m … `MC_ORBIT_RAD_MAX`; yaw front-to-centre; **cannot arm in orbit — take off in another mode**; QGC or a MAVLink API required to enable. MAVLink `MAV_CMD_DO_ORBIT` (34) → `ORBIT_EXECUTION_STATUS` (360); limits are silently clamped, so verify against the status message. https://mavlink.io/en/messages/common.html
- **MAVSDK-Python** https://github.com/mavlink/MAVSDK-Python (BSD-3, PyPI `mavsdk` 3.17.2, server bundled). `do_orbit(radius_m, velocity_ms, yaw_behavior, latitude_deg, longitude_deg, absolute_altitude_m)`; example https://github.com/mavlink/MAVSDK-Python/blob/main/examples/do_orbit.py (connect `udpin://0.0.0.0:14540`; wait for global + home position). API reference: http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/plugins/action.html (the mavsdk.mavlink.io python api_reference path 404s). armv6 Pi: apt `python3-grpcio`.
- **ArduPilot** CIRCLE mode https://ardupilot.org/copter/docs/circle-mode.html (radius units: metres, trust the Note); `MAV_CMD_DO_SET_ROI` + `MAV_CMD_NAV_LOITER_TURNS` https://ardupilot.org/copter/docs/common-mavlink-mission-command-messages-mav_cmd.html — ROI persists until cleared; negative radius = CCW; **no DO_ORBIT on ArduPilot.**
- **DroneKit-Python: do not use** (last commit 2024-05, PyPI 2019, "maintainers needed").
- **Simulation:** PX4 https://docs.px4.io/main/en/simulation/ — jMAVSim gone; **SIH** = headless, zero-install, start here; Gazebo https://docs.px4.io/main/en/sim_gazebo_gz/ only for simulated cameras. ArduPilot SITL https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html. QGroundControl https://qgroundcontrol.com/.
- **DJI:** MSDK V5 https://github.com/dji-sdk/Mobile-SDK-Android-V5 (branch `dev-sdk-main`, v5.18.0, enterprise airframes, App Key gated). developer.dji.com blocks non-browser traffic (405) — open it logged in. Android-only, proprietary.

\#### 3.4 Per-tree image grouping

- ExifTool https://exiftool.org/ (13.49); **ExifRead** https://pypi.org/project/ExifRead/ (3.5.1, read-only, healthiest); piexif (frozen 2019, read/write); pyexiv2 (GPL-3, native dep). geopandas + `sjoin_nearest` https://geopandas.org/en/stable/docs/reference/api/geopandas.sjoin_nearest.html
- Recipe: crowns (pixel) → georeference (`rasterio.transform.xy` or samgeo GeoJSON) → GeoDataFrame with `tree_id` → photo GPS points → **reproject both to UTM** → `sjoin_nearest(max_distance=15)` → group by `tree_id`.
- Traps: degrees give nonsense distances; **the photo's GPS is the drone, not the tree** (on a 10 m orbit the neighbour wins) — project forward along `GPSImgDirection`/gimbal yaw or widen max_distance; **the shortcut: log \`tree_id\` + timestamp when you issue \`do_orbit\` and match photos by EXIF time window.** Exact, and the right call for three weeks.

\#### 3.5 Companion computer

- PX4 https://docs.px4.io/main/en/companion_computer/ · Pixhawk wiring https://docs.px4.io/main/en/companion_computer/pixhawk_companion.html · Raspberry Pi https://docs.px4.io/main/en/companion_computer/pixhawk_rpi.html · ArduPilot https://ardupilot.org/dev/docs/companion-computers.html
- **mavlink-router** https://github.com/mavlink-router/mavlink-router (Apache-2.0) on the drone; MAVProxy https://ardupilot.org/mavproxy/ for debugging. ROS 2 https://docs.px4.io/main/en/ros2/user_guide.html — **not needed**; Offboard's 2 Hz setpoint rule bites.

\#### 3.6 Training and annotation

- Ultralytics train https://docs.ultralytics.com/modes/train/ (models index lists YOLO26, 12, 11…); **AGPL-3.0** https://github.com/ultralytics/ultralytics — fine for an open project; decide in week one.
- Roboflow https://universe.roboflow.com/ · https://docs.roboflow.com/; Label Studio https://github.com/HumanSignal/label-studio · https://labelstud.io/guide/; **Label Studio ML backend** https://github.com/HumanSignal/label-studio-ml-backend (pre-label with your model, correct only the wrong ones — 100 → 1,000 labels in a weekend); CVAT https://github.com/cvat-ai/cvat; FiftyOne https://github.com/voxel51/fiftyone (look at per-tree groups before building UI).

\#### 3.7 Vision-LLM reasoning

- Claude API vision https://docs.claude.com/en/docs/build-with-claude/vision · structured outputs https://docs.claude.com/en/docs/build-with-claude/structured-outputs · tool use https://docs.claude.com/en/docs/build-with-claude/tool-use/overview (optional backend).
- **TypeFly** https://github.com/typefly/TypeFly · https://arxiv.org/abs/2312.14950 (Apache-2.0) — NL → LLM plan over robot skills, YOLO as the eyes. Best reference for "propose which trees to inspect".
- **DeepDrone** https://github.com/evangelosmeklis/deepdrone — web chat console + live telemetry map + mission planner + replay + emergency stop/RTH; supports Anthropic and others. **A working reference for the console UI**; its flight layer is DroneKit — lift the UI, not the flight code.
- PromptCraft-Robotics https://github.com/microsoft/PromptCraft-Robotics; EchoPilot https://github.com/Bilalileri/EchoPilot---Ollama---PX4---MCP (Ollama → PX4 wiring).

\#### 3.8 Payload — the pump on and off

- **ArduPilot Copter Sprayer** https://ardupilot.org/copter/docs/common-sprayer.html (old `sprayer.html` URL is 404). `SPRAY_ENABLE=1`; pump on a PWM output with `SERVOn_FUNCTION=22` (spinner =23); `RCx_OPTION=15` pilot switch; `SPRAY_PUMP_RATE` (% at 1 m/s), `SPRAY_PUMP_MIN`, `SPRAY_SPEED_MIN` (cm/s), `SPRAY_SPINNER`. MAVLink `MAV_CMD_DO_SPRAYER` (216), param1 0/1 https://mavlink.io/en/messages/ardupilotmega.html
- **PX4 generic actuator** https://docs.px4.io/main/en/payloads/generic_actuator_control.html — `MAV_CMD_DO_SET_ACTUATOR`, "Peripheral via Actuator Set 1–6"; MAVSDK `set_actuator(index, value)` (index from 1, value −1…1). Generic: `MAV_CMD_DO_SET_SERVO` (183), `DO_REPEAT_SERVO` (184). https://docs.px4.io/main/en/payloads/
- Open hardware: agrodrone https://github.com/annesteenbeek/agrodrone (12 stars, PWM pumps on Odroid/Pi); farmware.v1 https://github.com/Harka-io/farmware.v1 (0 stars). DJI Agras https://ag.dji.com/ closed. Practical build: 12 V diaphragm pump, nozzle, MOSFET/relay off an AUX output.
- ArduPilot Discourse sprayer threads: `t/setting-up-crop-sprayer/67023`, `t/do-set-servo-in-spray-function-parameters-pump/56048`.

\#### 3.9 Safety and the legal framing

- **EU Directive 2009/128/EC Art. 9** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32009L0128 — "Member States shall ensure that aerial spraying is prohibited"; derogation needs an approved product, a certified operator and a specific assessment. So: **spray water**, cite Article 9, and the contribution is the targeting with a human approving and a stop button. EASA Open category https://www.easa.europa.eu/en/domains/civil-drones-rpas/open-category-civil-drones

\#### 3.10 Similar projects — a gap No substantial open-source orchard-scouting console exists. Long tail: `COS301-SE-2022/Chopper-Charlie` (4★, 2022), `4darsh-Dev/OrchardEyes` (1★), `werner291/Multigoal-Orchard-Drone-Planning-Library` (route planning), `AntonBock/OrchardDrone`, `vivek10-ppt/Autonomous-Drone-for-precision-agriculture` (Pixhawk + Pi via pymavlink, 2026). Assemble from components; the result will be more complete than anything public.

\#### 3.11 Communities PX4/Dronecode Discord https://discord.gg/dronecode · ArduPilot Discourse https://discuss.ardupilot.org/ · OpenDroneMap https://community.opendronemap.org/ · Ultralytics Discord https://ultralytics.com/discord · DeepForest GitHub Discussions · Roboflow forum via https://docs.roboflow.com/ · r/diydrones.

#### 4. Search recipes

1.  Google Scholar: `apricot ("brown rot" OR "shot hole") detection UAV deep learning`
2.  Google Scholar: `"Data in Brief" orchard UAV annotated image dataset disease YOLO`
3.  Google Scholar: `orthomosaic "per-tree" disease severity "symptoms per m2" drone phenotyping`
4.  GitHub: `orchard drone stars:\>5 pushed:\>2025-01-01` (swap `orthomosaic`, `tree crown`, `sprayer`)
5.  GitHub: `path:\*.py "do_orbit" MAVSDK`
6.  Roboflow: `https://universe.roboflow.com/search?q=class%3A%22apricot+leaf%22` (searches label names)
7.  Kaggle: `apricot OR "stone fruit" leaf disease`, sort Most Votes, check licence
8.  Hugging Face API: `https://huggingface.co/api/datasets?search=orchard`, `?author=Project-AgML`
9.  Zenodo API: `https://zenodo.org/api/records?q=orthomosaic+AND+orchard&type=dataset`
10. Papers: `https://huggingface.co/papers?q=tree+crown+detection` (paperswithcode.com now redirects there)

Bonus: Crossref `https://api.crossref.org/works?query.bibliographic=\`; Unpaywall `https://api.unpaywall.org/v2/\?email=you@example.com`.

\#### Pathologist keywords — English / Czech / German \***Monilinia laxa**\* (brown rot blossom blight, twig blight). Czech: moniliová spála peckovin (monilióza) · German: Monilia-Spitzendürre

\***Monilinia fructigena/fructicola**\* (brown rot fruit rot). Czech: moniliová hniloba plodů · German: Monilia-Fruchtfäule

\***Wilsonomyces/Stigmina carpophila**\* (shot hole, coryneum blight). Czech: suchá skvrnitost listů peckovin (dírkovitost listů) · German: Schrotschusskrankheit

\***Pseudomonas syringae**\* (bacterial canker, gummosis). Czech: bakteriální odumírání peckovin (klejotok) · German: Pseudomonas-Bakterienbrand

**Plum pox / decline** (sharka, apricot apoplexy, ESFY). Czech: šarka švestky, mrtvice meruněk, evropská žloutenka peckovin · German: Scharka, Apoplexie, ESFY

Genus word: **peckoviny**; apricot: **meruňka**. Czech sources: https://rlportal.ukzuz.cz/ (browser only), https://www.zahradaweb.cz/. German: https://www.hortipendium.de/, https://www.lfl.bayern.de/ips/, https://www.julius-kuehn.de/. English: https://ipm.ucanr.edu/agriculture/apricot/shot-hole-disease/

#### Two closing notes

Most likely to sink the three weeks: installing Detectron2 (avoid detectree2 unless DeepForest boxes fail) and adopting ROS 2 (MAVSDK-Python covers the spec). Most time saved: PX4 SIH for zero-install simulation, and logging `tree_id` when you issue `do_orbit`.

#### Addendum — pathogen sets verified by a second pass (2026-09-07)

**The "Apricot … Bilal Jan" memory resolves here:** a Roboflow Universe user named **bilal-jan** publishes **Apricot-brown-rot** — https://universe.roboflow.com/bilal-jan/apricot-brown-rot — 135 images, CC BY 4.0, classes **brown rot** and **gumosis and galls**, updated ~July 2026; and **apricot-healthy** (149 images) as the negative class. Small, on-target, one click.

**Turkey-PlantDataset (TPPD)** (https://raw.githubusercontent.com/mturkoglu23/PlantDiseaseNet/master/README.md → Google Drive `Turkey_PlantDataset.rar`; classes verified at https://www.nature.com/articles/s41598-025-90487-1). licence: not stated · size: 4,447 images, Nikon D7200, 4000×6000 · classes: 15 incl. Apricot Coryneum beijerinckii (shot hole), Apricot Monilia laxa, Peach Monilia laxa · type: field photos: leaves, fruit, trees · use: The only set naming \*Monilinia laxa\* on apricot

**PlantCity (figshare copy)** (https://figshare.com/articles/dataset/PlantCity_A_comprehensive_image_based_on_multi_crop_leaves_in_Pakistan/33040562). licence: CC BY 4.0 · size: 10,667 → 52,273; 6.76 GB · classes: apricot: shot hole 208 orig / 1,040 aug, blight 90/402, normal 163/815 · type: smartphone leaf · use: Biggest clean apricot shot-hole class

**Peach Disease (Roboflow, zeerox)** (https://universe.roboflow.com/zeerox/peach-disease). licence: CC BY 4.0 · size: 1,081 images · classes: `bacterial_spot`, `brown_rot`, `healthy_peach`, `shot_hole`, `shot_hole_leaf` · type: fruit + leaf boxes · use: Both target pathogens with boxes, YOLO in one click

**CherryLeaf-KG** (https://data.mendeley.com/datasets/wp3b6pz9gc/3). licence: CC BY 4.0 · size: 400 (100/class), 224×224 · classes: Teshik = shot hole, Chirish = brown rot, chlorosis, healthy · type: leaf, iPhone, Kyrgyz farm · use: Clean held-out eval set

**Plum leaf & fruit (counted from the zip)** (https://data.mendeley.com/datasets/w7sdx55m7z/1). licence: CC BY 4.0 · size: 3,554 orig · classes: Shot Hole 643, Bacterial Spot 592, Healthy Leaf 735, Wilted 548, Healthy Fruit 560, Unhealthy Fruit 476 · type: leaf + fruit · use: Second-largest shot-hole class

**LeafScans-Orchard** (https://zenodo.org/records/20187966). licence: CC BY 4.0 · size: 9,708 scans, ~37 GB · classes: 7 crops incl. apricot, 67 cultivars, no disease labels · type: flatbed scans · use: Healthy negatives, leaf-shape prior

**Seen on search, not opened (proxy died): \`bilal-jan/apricot-healthy\` (149); \`jhon-alan-fernandez-maturano-wawws/peach-diseases\` (213, incl. Moniliosis, segmentation); \`usfx-xqsnn/peach-diseasesusfx-cy77o\` (4.02k, Public Domain)**.

**Traps:** the 875-image Roboflow "shot hole" projects (`tonoya-ruku/shot-hole`, `shahnewaz-ahmed/shot-hole-tbg2n`) are **grape**; "Spanish cherry leaves diseases" (Mendeley c9k638ctgm) is \*Muntingia\*, not \*Prunus\*; the Monilinia peach paper https://www.mdpi.com/2624-7402/8/9/368 has data "on request" only; Zenodo 19355833 is a PDF review, no images. Plum "Bacterial Spot" is \*Xanthomonas\*, not Pseudomonas — label accordingly.

**Not found anywhere:** Eutypa images; bacterial canker (\*Pseudomonas\*) on stone fruit; Monilinia at species level beyond TPPD; \*Wilsonomyces/Stigmina\* by name; any UAV/orthomosaic apricot set. The cherry orchard set (Zenodo 7144071) is the only stone-fruit UAV disease dataset.

**Pull order:** ATZD01 (start the authorization email today), Roboflow zeerox/peach-disease + PlantCity apricot (immediate, CC BY, both pathogens), bilal-jan/apricot-brown-rot + apricot-healthy, CherryLeaf-KG as eval, Zenodo 7144071 as the blueprint.
