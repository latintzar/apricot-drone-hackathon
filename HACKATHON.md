# The Apricot Drone Hackathon

For Ilian. From Peter, September 2026.

## Why

You are nineteen, you can fly a 20 kg drone, you study computer science and robotics, and there is a real drone standing in a garden in the Czech Republic waiting for you. You have three weeks before term. That is a hackathon, and this is the brief.

The people who will change your life build things and hire on evidence. The only evidence that counts is something you built that they can open in a browser and run. So: build one thing, in public, in three weeks, and write it up so well that a stranger understands it in a minute and an engineer respects it in five. The second document in this folder, the world you are joining, is what you do with it afterwards.

## The brief

The apricot drone. Your aunt's garden has apricot trees and the neighbour's tree is sick with a fungus. Build the open-source system that flies over the orchard on its own, photographs every tree, and comes back with a map where every tree is outlined and coloured: green is fine, amber is worth a look, red is a risk, and the label says what kind. The map says what it wants to do next, which trees deserve a close look and from which side. You approve, or change it with a tap. The drone flies out again and circles each chosen tree, low, taking close-ups all the way round. Those come back sorted by tree into a gallery of tiles you can tap open and tap shut. When you are sure, you tap spray. The drone goes over the tree, sprays, shows you the progress as it happens, lets you stop it at any second, and says "spraying done".

That is both autonomous and collaborative, and it is the right shape. The drone does the flying, the looking and the spraying. The model does the first reading and the proposing. You do the deciding. Every decision you make teaches the model, because every tap is a label. If the model turns out to see nothing useful from thirty metres up, say so in the log with the pictures that prove it, and the console with a human deciding remains a product your aunt can use. That is an honest result and a good one.

Spraying drones exist and papers exist on disease detection from drone images; the datasets from them are yours to use, and the last section lists them. Nobody who matters asks whether an idea is new. They ask whether you built it, whether it works, and whether they can read the log.

## The three levels

Level one, the survey and the risk map. The drone flies a grid over the orchard at a fixed height, takes geotagged photos, lands. Your software stitches them into one picture of the orchard and finds every tree in it; open-source models exist that outline tree crowns from above, and the pointers section names them. Every tree gets a number that stays the same on every flight, because it is a place on the map. Then each crown is cropped and sent to a vision model with one question: what do you see, how sure are you, and which of these diseases could it be. The answers colour the map and label each tree with the type of risk. Under the map, the model's proposals: "look closer at 7, 12 and 19, from the north side, where the brown blossom is." You approve, remove, or add with a tap, and the approved list becomes missions. On day one that model is whatever you can run: a small open vision model on your laptop through Ollama costs nothing and answers in JSON, and a hosted model through an API works the same way if you have credits. Your own trained detector comes later and makes it faster and better on your trees. When level one works, the drone is already useful to your aunt, and the repository already deserves to be read. Make the console beautiful. It is the thing people will screenshot.

Level two, the orbit and the gallery. For each approved tree the drone flies to it, descends to six to eight metres, and circles it once, camera pointed at the trunk, taking a photo every thirty degrees. PX4 and ArduPilot both have an orbit mode built in, and DJI's SDK has a point-of-interest mission; the pointers section links to all three. Every photo is filed under the tree it was pointed at, worked out from where the drone was and where the camera looked, so the gallery groups itself. The console shows one row of tiles per tree; tap a tile to see it full size, tap again to close it. The model reads the close-ups and updates the tree's colour and label with its reason. You decide. Alongside this you start training your own detector on the crops and close-ups you have labelled by tapping, and the day it beats the general model on your orchard, you write that down with the numbers.

Level three, the treatment. A drone of that size usually already carries a sprayer: a tank, a pump, one or more nozzles, and a valve or a pump speed that something switches on and off. Yours may have all of it. Find out what you have and how it is commanded; on an open flight controller a sprayer is a servo or relay output the mission can switch, and ArduPilot has a built-in sprayer function that does exactly that, while a DJI agricultural aircraft exposes spraying only through its own app and SDK. The pointers section links to both. The function you build is the same whatever the parts: you tap spray on a tree, the console asks you once to confirm, and the drone goes to a known height above the crown and sprays for a computed number of seconds while the console shows a bar filling and a stop button that works. Then "spraying done", with the time, the amount and a photo. Water and marking dye are what you spray while you build, and a page called LEGAL says plainly what the Czech authorities allow you to put in the tank after that. This level is next spring, when the blossom comes and the fungus shows itself.

## Where the brain lives

You asked whether a drone can run a language model. The drone carries a camera and a radio. The brain lives on the ground, and that is better.

On the aircraft: a small computer, a Raspberry Pi 5 or a Jetson if you want detection on board. It reads the camera and the flight controller and sends small packets to the ground: a 640-pixel JPEG, the GPS position, altitude, heading, battery. On a DJI aircraft the small computer is the phone in the controller.

On the ground: a laptop in the garden on WiFi, which covers an orchard, or a 4G dongle if you want more. This is the hub. It stores every observation, builds the map, and asks a vision model the only question that matters: which trees should I look at again, and how. The model is a part you choose, the way the aircraft is. A small open vision model running on your laptop through Ollama does this for free and answers in JSON you can act on. A hosted model through an API does the same for cents a call if you have credits. A detector you trained yourself does it fastest once it exists. A Jetson on the aircraft can run the small one in the air. The interface is the same in every case: an image goes in, a JSON answer comes out, so you can swap the model any day and the console never notices. The hub sends the next waypoints back. You hold the controller and can abort at any moment, because you are the pilot and that is the law.

The first thing you find out, before any code, is what the aircraft is. Make, model, weight, payload margin, what sprayer it already carries, and above all who controls it. A DJI aircraft has a closed flight controller, and your code runs on an Android phone through DJI's Mobile SDK, which can fly waypoints and read the camera. A PX4 or ArduPilot aircraft is open, and a companion computer talks MAVLink and can do anything. Write the answer into the README on day one. Everything else follows from it.

The second thing is the disease. Ask your aunt what the tree has and photograph it. On apricots in Central Europe it is usually Monilinia, which shows as withered brown blossoms and mummified fruit on the branch, or shot-hole, which shows as red spots on leaves that fall out and leave holes. Each looks different from the air. Your labels come from what is actually there.

## What you hand in

A hackathon ends with a demo, and this one ends with six things a stranger can open.

The repository. Public from day one, with a README that starts with a story, tells the truth about what works, and runs a replay in five minutes with no drone, because you recorded a flight and anyone can play it through your pipeline and watch the map appear. Under it: the console, the mission code, the model with its training runs and its failure gallery, the hardware page with parts and prices, the LEGAL page, the field notes, and the pack for your uncle: one printed page, big type, a photo for every cable, one button to start. If your uncle has to phone you, the pack failed, and you fix the pack.

The video. Two minutes. The drone taking off, the console on your screen, a tap, the drone moving, the close-up appearing. Cut it yourself. Put it at the top of the README and on the project page.

The media. Collect it from the first day, into a folder called media, because you cannot go back and film day three. The list: the drone on the grass with the orchard behind it, the hero photo. A ten-second clip of a takeoff. A screen recording of the console, the coloured map, a tap, the drone moving, saved as a GIF. A screen recording of the gallery, tiles opening and closing. The stitched orchard map. One close-up of a sick tree beside one of a healthy tree. The failure gallery as a grid of nine images. The training curve. A photo of the wiring, labelled. A photo of your uncle holding the printed pack, next to the drone. A short clip of the spray test, when it comes. Phone in landscape, always, and the raw files kept.

The log. One entry per thing you ship, same day, in a file called LOG.md. Date, what you shipped, what broke, the number that changed, one photo. This is the source for everything else and it is what I read.

The reflections. One per part, written when the part is done, on the template further down.

The project page, described further down.

## The rules

This brief describes the function, never the parts. Every hackathon assumes people arrive with their own gear, and you have yours: one aircraft, one camera, one sprayer, one laptop, and I know none of their details. Your first job is to find them out and write them down, and then the brief applies to whatever you have.

The repository is public from day one, with nothing flying yet, and it says so.

Something ships every three days. A shipped thing is a commit plus a log entry plus a picture.

Every number in the repository is one you measured. Where something is unfinished, the README says "works up to step three".

The pilot holds the controller and can abort at any moment. That is the law and it is also good engineering.

You are judged on four things, in this order. Does it work. Can a stranger understand it in a minute. Is it honest. Could someone else build it from what you wrote.

Elena helps if she wants to, on any piece she picks; the console is the natural one. Her name goes on the repository for what she built.

## Get to working condition

Every hackathon starts with a page like this: make these accounts, install these things, and you are ready when the following runs. Do it on day one, before the story, before the code. Claude Code can do most of the installs for you; the accounts you open yourself, because they are yours.

Accounts, all free:

- GitHub, if you do not already have it, and then the GitHub Student Developer Pack at education.github.com/pack with your university email. It includes a free domain for a year and a long list of credits.
- Vercel, with your GitHub login. The Hobby plan is free and hosts the live demo.
- Substack, for the four posts.
- Roboflow and Kaggle, for the datasets. Hugging Face, for the models and to host your own dataset later.
- The Dronecode Discord and the ArduPilot forum, whichever flight stack your aircraft runs. The OpenDroneMap forum.
- A domain in your name, about ten euros, from Cloudflare or Porkbun, or the free one from the student pack.

On your laptop:

- Python 3.11 or newer, git, and uv or pip. Node, for the console.
- Ollama, and one vision model pulled: gemma3 or qwen2.5vl. Ask it to describe a photo of a tree and answer in JSON. That is your first model, free.
- QGroundControl. Connect the aircraft to it and see the map, the battery and the GPS. If that works, your code can talk to the aircraft.
- The flight stack's simulator: PX4 with SIH, which needs nothing but the PX4 source, or ArduPilot SITL. Fly a circle in the simulator before you fly one in the garden.
- MAVSDK for Python, DeepForest, Ultralytics, ExifRead and geopandas, all from pip. OpenDroneMap through Docker, or WebODM.
- Label Studio, from pip, for labelling. FiftyOne, for looking at what you labelled.

On the aircraft side:

- The manual for your exact aircraft, its flight controller and its sprayer, read once, with the pages on the SDK or the MAVLink port marked.
- Spare propellers, two charged batteries, an SD card that is empty, and a way to get photos off the aircraft that you have tested.
- A laptop with 16 GB of memory if you can borrow one. Stitching 250 photos needs it.

You are in working condition when all five of these are true. The aircraft shows up in QGroundControl with a GPS fix. A script of yours flies an orbit in the simulator. DeepForest draws boxes on the OpenDroneMap sample dataset on your laptop. Ollama answers a JSON question about a photo. The repository is public with a README that says none of this flies yet. Write the date you got there in the log. That is your first entry.

## The three weeks

Days one to three. Find out what the aircraft is and get its camera and GPS into your own code. Write the story and the status line. Put the repository up. Sketch the console on paper: the orchard, the trees, the three taps.

Days four to nine. Plan a grid in software, fly it, geotag the photos, stitch the map. Find the trees on the map, colour them with the vision model's first reading, and put the proposals and the taps in the console, even if the drone cannot fly a tap yet. First field note. First log entries.

Days ten to eighteen. Make a tap fly: go to the tree, descend, circle it, a photo every thirty degrees, back. File the photos by tree and build the gallery. Record a flight for the replay. Label what you have, train a first detector, make the table and the failure gallery. Let the model propose and you confirm. Second field note.

Days nineteen to twenty-one. Finish the README for what exists. Cut the video. Write the reflections. Publish the project page. Thirty emails. Everything after this is weekends, and the spring is for the nozzle.

## The reflection template

Write one when a part is done, in a folder called reflections, one file per part: the aircraft, the mission code, the console, the model, the reasoning step, the field work, the pack for your uncle, and one for the whole three weeks. Two hundred to four hundred words each, first person, written the day the part ships, before you forget what was hard. Use these seven questions and answer them in order.

What I thought this part would be. One paragraph, honest, including how long I thought it would take.

What it actually was. What broke, what surprised me, the moment it worked.

The numbers. Time it took, flights it needed, the metric, the cost.

What I would do differently, starting again tomorrow.

What I would tell someone starting this part today. One sentence they could pin above their desk.

What I still do not understand.

One picture, and the caption that explains it.

The last file, the whole three weeks, answers the same questions about the hackathon itself, and ends with the sentence you would say to a founder who asked "so what did you build this summer".

## The project page

The repository is for engineers. The project page is for everyone else: the founder who has five minutes, the professor, your aunt. It tells the story with pictures and links to the code at the bottom.

Buy a domain in your name, about ten euros a year, or take the free one from the GitHub Student Pack. Under it, two things, both free to host. The project site, one long page: the video at the top, the story, a picture per level, the map, the console GIF, the numbers, the reflections, the link to the code. GitHub Pages serves it from the docs folder of the repository. And the live demo: the console itself on your own free Vercel account, loaded with a recorded flight, so a founder opens it on a phone, taps tree 12, sees the gallery, taps spray, and watches the bar fill against the log. No drone, no login, thirty seconds. Build the console so the same code runs live in the garden and replayed on the web, and this costs nothing extra.

The writing goes on Substack: four posts over the three weeks, day one, end of level one, end of the detector, and "What I built in three weeks" with the video. Each post is the log and the reflection for that stretch, rewritten for a reader. Post the last one to Hacker News as "Show HN".

## Use Claude Code for these things

You have Claude Code for a week, and so does Elena. Used well, it is a senior engineer sitting next to you. Used badly it writes you a pile of plausible code you cannot explain in an interview. The coding tool and the model that reads your trees are separate choices.

Paste this as the first message of a fresh session. It fetches this whole brief from the folder, writes the CLAUDE.md for your repository, and interviews you.

```
You are helping me, Ilian, run a three-week hackathon. Fetch and read the entire brief before you do anything: https://drive.google.com/uc?export=download&id=1oLiD1jfimaN2GgULBM8jM0-1eote1sdn

Rules that never change:
- I do the work. You plan, scaffold, write the boring parts, review, and ask. When something needs running, flying or measuring, tell me what to run and wait for me to paste the real output.
- Interview me before you assume anything about the aircraft, the sprayer, the orchard, or my time. Start with the day-one questions in the brief, one at a time.
- Reading companies, their websites and their people is my job. You tighten what I wrote and keep the sheet.
- When I ask you to mentor me, tell me the truth about my work. Flattery wastes my time.
- Every number in the repository is one I measured. Where you do not know, write "[measure this]".
- Short sentences. Say what a thing is. Sentence-case headings. Commit after every step with a one-sentence message.
- Keep CLAUDE.md at the repository root current: the aircraft, the flight stack, the sprayer, the conventions, the level I am on, and the job we are doing. You read it every session.

First, write CLAUDE.md from the brief and this message. Then tell me in three sentences what the three levels are, and ask me the first day-one question.
```

The day-one questions it will ask you, so have the answers ready:

1. The exact aircraft: make, model, take-off weight, payload margin, flight time, camera, and what sprayer it already carries.
2. The flight controller: DJI, with its Mobile SDK on Android, or PX4 or ArduPilot, with MAVLink and a companion computer.
3. How you get the live camera feed and GPS into your own code on that aircraft.
4. The ground station: a laptop on WiFi in the garden, or a 4G dongle on the aircraft.
5. The diseases your aunt has seen, and whether you have photos.
6. How many trees, how big the plot is, and what is around it.
7. How many days you have, and whether you have a GPU.

After that, every session starts with one plain sentence that names the job:

- Do my GitHub. "Read my three repositories and write READMEs that are true." Day one, two hours. One sentence saying what each does, one image, how to run it, what you learned, and "works up to step three" where it is unfinished.
- Working condition. "Get me to working condition." It checks the installs, tells you which accounts to open, and stops when the five things are true.
- Build. "We are on level one, day four. Plan the grid mission module and its tests, then wait." It plans, you cut what you do not understand, it writes, you run.
- Write. "Turn today's log entry into the reflection for the console." Seven questions, your voice, your numbers, blanks where it has none.
- Publish. "Set up the project site and the live demo." GitHub Pages, the Vercel deploy from the console folder with a recorded flight, the DNS records, a Substack template. You buy the domain and open the accounts.
- Judge. "Judge the repository as a stranger." Does it work, can a stranger understand it in a minute, is it honest, could someone else build it. Then you fix what it lists.
- Mentor. "Be my mentor today." A call tomorrow, a paper you half understood, what to learn next, a mock interview, the truth about a post. It explains like someone who has been where you want to go, and ends with one thing to do before next time.

What only you can do: fly, tap, measure, read the companies, pick the person, write the question, buy the domain, open the accounts, send the emails, write the cold open, take the photos.

## Datasets, pointers and links

Every link here was opened and read this week. The full list, with licences and sizes, is in the companion research document in the folder.

The apricot thing you remember. There is a Roboflow project by a user called bilal-jan, "Apricot-brown-rot": 135 photos, licence CC BY, classes brown rot and gummosis, with a sister set of 149 healthy apricots. universe.roboflow.com/bilal-jan/apricot-brown-rot. Behind the name are two papers. Jamil Ahmad and Bilal Jan wrote the plum paper in Sensors 2020, brown rot and shot hole photographed on phones in Swat, five thousand images, the method you will copy: transfer learning, ninety-two percent, and heat maps showing the network looked at the lesions. Jamil Ahmad then wrote the apricot drone paper, Expert Systems with Applications 2025, apricot brown rot and shot hole photographed from a DJI Mavic Mini, the exact crop, the exact diseases and the exact camera class. That dataset is unpublished. Write to him on day one and ask for it; one email is worth three days of searching.

The five links for day one. First, the pear rust paper in Agronomy 2024, which is your project already built on pears: two flights at 17 and 8 metres, an orthomosaic, YOLO, symptoms turned into GPS points, and an infection intensity per tree on a five-band colour scale. That is the risk map. mdpi.com/2073-4395/14/11/2643. Second, its dataset, the only drone-altitude tree-disease set in the open: 584 annotated images at 5 to 12 metres, in YOLO format, CC BY. data.mendeley.com/datasets/44kjgc4gkc/1. Train on it in week one and fly your apricots at the same height. Third, DeepForest, which finds every tree crown on an orthomosaic in an afternoon and ships a classifier for dead versus alive crowns, a risk signal on day one. github.com/weecology/DeepForest. Fourth, the MAVSDK orbit example, forty lines of Python that circle a point. github.com/mavlink/MAVSDK-Python/blob/main/examples/do_orbit.py. Fifth, OpenDroneMap, which stitches; 16 GB of RAM handles 250 images and a GPU changes nothing. docs.opendronemap.org/installation.

Datasets you can download this week, all CC BY unless said. ATZD01, the largest apricot set in existence, 6,055 photos and 20,272 boxes across eleven diseases and pests including 9,023 shot-hole and 480 brown-rot instances, from three orchards in China; the archive is password-locked and the mirror is dead, so open an issue at github.com/meanlang/ATZD01 and email Prof. Zhiyong Tao's group today, because it takes days. Peach Disease on Roboflow by zeerox, 1,081 photos with boxes for brown rot, shot hole and bacterial spot, one click to YOLO format. universe.roboflow.com/zeerox/peach-disease. PlantCity, 10,667 field photos from Pakistan across twelve crops, with 208 apricot shot-hole leaves. data.mendeley.com/datasets/w8kh2xkspx/4. The Turkey plant dataset, the only one that names Monilinia laxa on apricot by species. github.com/mturkoglu23/PlantDiseaseNet. CherryLeaf-KG, 400 clean cherry leaves with shot hole and brown rot, keep it as your test set. data.mendeley.com/datasets/wp3b6pz9gc/3. The plum set with 643 shot-hole images. data.mendeley.com/datasets/w7sdx55m7z/1. And the cherry orchard drone set from Greece, 42 GB, 577 trees photographed from the air and the ground across a whole season with a severity grade per tree by an agronomist: it is your architecture already built once, so copy its structure. zenodo.org/records/7144071. For the fire-blight close-up set, whose "maybe" class is a ready-made bucket for "send a human", data.mendeley.com/datasets/fpmnncmg84/1.

What came back empty, so you can stop looking: there is no public image set for Eutypa, for bacterial canker on stone fruit, or for any apricot orchard photographed from above. The two 875-image "shot hole" sets on Roboflow are grapevines. That gap is the space your repository sits in.

The building blocks. Tree crowns: DeepForest for boxes, then segment-geospatial to turn them into polygons with world coordinates. github.com/opengeos/segment-geospatial. Stitching: ODM, with NodeODM as the API you call from code, and a geo.txt file whose spare column can carry the tree number through the stitch. docs.opendronemap.org/geo. The orbit: PX4 orbit mode, docs.px4.io/main/en/flight_modes_mc/orbit.html, one metre a second by default, nose to the centre, and it will refuse to arm in orbit, so take off in another mode first; on ArduPilot the same thing is CIRCLE mode or a loiter-turns command paired with a region of interest, and the region of interest stays set until you clear it. ardupilot.org/copter/docs/circle-mode.html. Skip DroneKit; it stopped in 2019. Simulation before flying: PX4's SIH simulator runs with nothing installed and is where you build the orbit on your laptop. docs.px4.io/main/en/simulation. Photos to trees: log the tree number and the time when you command each orbit and match photos by their timestamp; the geometry method works too, but the drone's GPS is where the drone was, and on a ten-metre orbit the neighbouring tree wins. Training: Ultralytics for YOLO, Label Studio with its ML backend so your model pre-labels and you only correct, and FiftyOne to look at a tree's photos before you build the gallery. The proposals: TypeFly, github.com/typefly/TypeFly, is an open project where a language model plans a drone's actions from a detector's view of the scene, which is your level one in someone else's code, and DeepDrone, github.com/evangelosmeklis/deepdrone, is a web console with a live map, mission planner, replay and an emergency stop, so lift its interface ideas. The pump: ArduPilot has a sprayer built in, set SPRAY_ENABLE, put the pump on an output with function 22, and a single MAVLink command turns it on and off. ardupilot.org/copter/docs/common-sprayer.html. On PX4 it is one line, set_actuator, on a peripheral output. docs.px4.io/main/en/payloads/generic_actuator_control.html. The console is a web page; the rest is wiring you already understand.

The law, in one sentence you can cite. Article 9 of EU Directive 2009/128 says member states shall ensure that aerial spraying is prohibited, with derogations only for approved products and certified operators. So you spray water, you say so on the page, and your contribution is the targeting with a human approving and a stop button. That is the answer a judge will ask about, and it is a better demo than pretending.

How to search for more. On Google Scholar: apricot "brown rot" OR "shot hole" detection UAV deep learning. On GitHub: orchard drone stars:\\5 pushed:\\2025-01-01, and path:\\.py "do_orbit" to find every real orbit implementation. On Roboflow: search class:"apricot leaf", because the class operator searches labels, which is the only way to find the small sets. On Zenodo, use the API: zenodo.org/api/records?q=orthomosaic+AND+orchard&type=dataset. The Czech words that unlock Czech sources: peckoviny for stone fruit, meruňka for apricot, moniliová spála peckovin for blossom blight, suchá skvrnitost listů peckovin for shot hole, and šarka, the plum pox virus, which is what a Czech grower actually worries about. The Czech plant-protection portal is rlportal.ukzuz.cz.

Two things most likely to eat your three weeks: installing Detectron2, so use DeepForest boxes unless they visibly fail, and adopting ROS 2, which MAVSDK makes unnecessary. Two things that save the most: the SIH simulator, and logging the tree number at the moment you command the orbit.

