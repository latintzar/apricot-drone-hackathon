# The Apricot Drone Hackathon

Brief for Ilian. Three weeks, one open-source project, published. September 2026.

## Definitions

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

## Guidance

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

Paste this as the first message of a fresh session. It fetches this brief from the folder, writes the CLAUDE.md for your repository, and interviews you.

```
You are helping me, Ilian, run a three-week hackathon. Fetch and read the entire brief before you do anything: https://drive.google.com/uc?export=download&id=1oLiD1jfimaN2GgULBM8jM0-1eote1sdn

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

Every link was opened this week. Full list with licences and sizes in the companion research document.

The apricot set. Roboflow user bilal-jan publishes "Apricot-brown-rot": 135 photos, CC BY, classes brown rot and gummosis, plus 149 healthy apricots. universe.roboflow.com/bilal-jan/apricot-brown-rot. Related papers: Jamil Ahmad and Bilal Jan, plum brown rot and shot hole on phone photos, Sensors 2020, the method template. Jamil Ahmad, apricot brown rot and shot hole from a DJI Mavic Mini, Expert Systems with Applications 2025, dataset unpublished. Email him on day one and ask for it.

Day one, five links. The pear rust paper, Agronomy 2024, this project on pears with a five-band per-tree colour map: mdpi.com/2073-4395/14/11/2643. Its dataset, the only drone-altitude tree-disease set in the open, 584 annotated images at 5 to 12 metres, YOLO format, CC BY: data.mendeley.com/datasets/44kjgc4gkc/1. DeepForest for tree crowns, with a dead-versus-alive crown classifier: github.com/weecology/DeepForest. The MAVSDK orbit example: github.com/mavlink/MAVSDK-Python/blob/main/examples/do_orbit.py. OpenDroneMap install, 16 GB RAM for 250 images, GPU irrelevant: docs.opendronemap.org/installation.

Datasets to download this week, CC BY unless stated. ATZD01, 6,055 apricot photos, 20,272 boxes, 11 classes including 9,023 shot-hole and 480 brown-rot instances; password-gated, request access on day one at github.com/meanlang/ATZD01. Peach Disease by zeerox on Roboflow, 1,081 photos with boxes for brown rot, shot hole, bacterial spot: universe.roboflow.com/zeerox/peach-disease. PlantCity, 10,667 field photos including 208 apricot shot-hole leaves: data.mendeley.com/datasets/w8kh2xkspx/4. Turkey plant dataset, names Monilinia laxa on apricot: github.com/mturkoglu23/PlantDiseaseNet. CherryLeaf-KG, 400 cherry leaves with shot hole and brown rot, use as the test set: data.mendeley.com/datasets/wp3b6pz9gc/3. Plum set with 643 shot-hole images: data.mendeley.com/datasets/w7sdx55m7z/1. Cherry orchard drone set, 42 GB, 577 trees from the air and the ground across a season with a severity grade each; copy its structure: zenodo.org/records/7144071. Fire-blight close-ups whose "maybe" class is a ready "send a human" bucket: data.mendeley.com/datasets/fpmnncmg84/1.

Searched and empty: Eutypa images, bacterial canker on stone fruit, any apricot orchard from above. The two 875-image "shot hole" sets on Roboflow are grapevines.

Building blocks. Crowns: DeepForest for boxes, segment-geospatial for polygons with coordinates, github.com/opengeos/segment-geospatial. Stitching: ODM, NodeODM as the API, a geo.txt whose spare column carries the tree number: docs.opendronemap.org/geo. Orbit: PX4 orbit mode, docs.px4.io/main/en/flight_modes_mc/orbit.html, one metre a second, nose to centre, cannot arm in orbit so take off in another mode; ArduPilot circle mode or loiter-turns with region of interest, which persists until cleared: ardupilot.org/copter/docs/circle-mode.html. DroneKit is unmaintained since 2019; use MAVSDK. Simulation: PX4 SIH, nothing to install: docs.px4.io/main/en/simulation. Photos to trees: log the tree number and time at each orbit command, match by timestamp. Training: Ultralytics for YOLO, Label Studio with its ML backend for pre-labelling, FiftyOne to inspect. Proposals: TypeFly, github.com/typefly/TypeFly, a language model planning drone actions from a detector's view; DeepDrone, github.com/evangelosmeklis/deepdrone, a web console with live map, planner, replay and emergency stop. Pump: ArduPilot sprayer, SPRAY_ENABLE and an output with function 22, one MAVLink command on and off: ardupilot.org/copter/docs/common-sprayer.html. PX4: set_actuator on a peripheral output: docs.px4.io/main/en/payloads/generic_actuator_control.html.

Law. Article 9 of EU Directive 2009/128 requires member states to prohibit aerial spraying, with derogations only for approved products and certified operators. Spray water. State it on the page. The contribution is the targeting with a person approving and a stop button.

Search. Google Scholar: apricot "brown rot" OR "shot hole" detection UAV deep learning. GitHub: orchard drone stars:>5 pushed:>2025-01-01; path:*.py "do_orbit". Roboflow: class:"apricot leaf". Zenodo API: zenodo.org/api/records?q=orthomosaic+AND+orchard&type=dataset. Czech terms: peckoviny, meruňka, moniliová spála peckovin, suchá skvrnitost listů peckovin, šarka. Portal: rlportal.ukzuz.cz.

Two things that eat time: installing Detectron2, so use DeepForest boxes unless they fail; adopting ROS 2, which MAVSDK makes unnecessary. Two things that save time: the SIH simulator; logging the tree number at the orbit command.
