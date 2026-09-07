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


---

# The World You Are Joining

Reference for Ilian. What exists, where it is, and what to do with it all year. September 2026.

## Definitions

Startup. A company built to grow fast, funded by investors who buy a share early.

Venture capital, VC. The investors. A fund is a pool of their money with a portfolio of companies.

Accelerator. A programme that takes a group of startups at once, gives each money and three months of help, and ends with a demo day.

Batch. The group an accelerator takes at one time. Companies are named by their batch.

Fellowship. Money paid to an individual to build or study, with no company required.

Hub. A city where the funds, the companies and the engineers concentrate.

## Accelerators and fellowships

Y Combinator, in San Francisco, is the one that matters most. It has run since 2005, funded Airbnb, Stripe, Dropbox, Coinbase and Reddit, and now takes batches four times a year from anywhere in the world, moves them to San Francisco for three months, and invests half a million dollars in each. A nineteen-year-old in Sofia with a repository that flies can apply. ycombinator.com/apply. Everything YC has learned is free: the Startup School videos at startupschool.org, which you will watch all of this year, one a day, and the YC Library at ycombinator.com/library. Their Requests for Startups page, ycombinator.com/rfs, says what they wish someone would build, and there is always a robotics line in it. The list of every company in every batch is at ycombinator.com/companies, and their open jobs at news.ycombinator.com/jobs. Those jobs are the exact target of this whole document. A YC company that just raised is hiring.

Others in the same family. Speedrun, run by the venture firm a16z, invests up to a million dollars in new companies, many in games and hardware, speedrun.a16z.com. Entrepreneur First, in London and Paris, takes individuals before they have a company or even a co-founder, and pairs them; it is built for a person exactly your age and shape, joinef.com. Antler does the same in thirty cities. Station F in Paris is the largest startup campus in the world, a building with a thousand companies and a dozen programmes inside, stationf.co. The Thiel Fellowship gives 250,000 dollars over two years to people under 23 who want to build instead of sit in a classroom, thielfellowship.org. Z Fellows is one week and ten thousand dollars for young builders who want a fast door into Silicon Valley, zfellows.com. All five take applicants from anywhere. The repository is the application.

The places. San Francisco has the most money and the most companies; hiring there is on what you shipped. London has the biggest scene in Europe, DeepMind, Isomorphic, Entrepreneur First, and most of the European money. Paris has Station F, Mistral and the new biology-AI companies. Munich and Berlin have become the drone and defence cluster: Helsing, Quantum Systems, STARK, TYTAN and Alpine Eagle are all within an hour of each other, and they are hiring students. New York is finance and media and a growing hardware scene. Tallinn built Skype, Bolt and Wise from a country smaller than Bulgaria.

Where Bulgaria fits. It is small and it is real. Four funds worth knowing, Eleven, LAUNCHub, Vitosha and Neo, whose portfolio pages you read every Sunday. Two companies the world takes seriously, Dronamics and EnduroSat, both in Sofia, both in your field, and both in the companies section. INSAIT, an institute built with ETH Zurich and EPFL that publishes at the top conferences and pays undergraduates to do research in the summer. Sofia Tech Park, with drone and robotics labs you can walk into. A defence-technology wave that put more venture money into Bulgarian defence and dual-use companies in 2025 than into any other country in the region. And The Recursive, the news site for startups in this part of Europe, therecursive.com, which you read the way you read the local paper. Build in Bulgaria, publish to the world.

The press. Hacker News, news.ycombinator.com, every day; it is where engineers talk and where you will post your project. TechCrunch, the trade paper for startups worldwide, for the funding announcements. Sifted, sifted.eu, the same for Europe, and the one that will cover the companies on your list. Dealroom for the data behind the news.

The people to listen to. Paul Graham's essays, starting with "How to Do Great Work", "Do Things That Don't Scale" and "How to Get Startup Ideas", one a week. On the Lex Fridman podcast, four long conversations worth every hour: Andrej Karpathy on building Tesla's self-driving, episode 333; Robert Playter, the CEO of Boston Dynamics, on legged robots, episode 374; Jim Keller on how chips and engineers actually work, episode 162; and Sam Altman, episode 419. They are three hours each. Listen while you label images.

The top of the world, and how to watch it. Your field has a frontier, and it moves every week. In robotics and drones it is Boston Dynamics, Skydio, whose drones fly themselves through forests with cameras alone, Anduril, the company that made defence a startup category, Figure and 1X, building humanoids, and Physical Intelligence, which is trying to build one model that runs any robot, physicalintelligence.company. In AI it is Google DeepMind, OpenAI, Anthropic and NVIDIA, whose research pages are public and readable, deepmind.google/research, anthropic.com/research, research.nvidia.com. Everything these people publish appears first on arXiv; the robotics list is at arxiv.org/list/cs.RO/recent and Hugging Face's daily papers page, huggingface.co/papers, ranks the ones people are actually reading. Read the abstracts every morning with your coffee, and one full paper a week. Import AI, Jack Clark's weekly newsletter, tells you what mattered, importai.substack.com. The Dwarkesh podcast is where the researchers at those labs explain themselves at length, dwarkesh.com. The State of AI report, once a year, stateof.ai, is the map. Three months of this habit is enough to know what the field is doing.

## Getting into the rooms

Entry is by work. The doors below pay the person entering.

The doors that pay you. Every accelerator and fellowship in the previous section gives you money, and asks only what you built. YC invests half a million dollars. Entrepreneur First pays a stipend while you find a co-founder. The Thiel Fellowship is 250,000 dollars. Z Fellows is a paid week in Silicon Valley. Google Summer of Code pays you to write open-source code for three months, from your bedroom, for a project like ArduPilot, and Google's name goes on your CV; organisations are announced each February, so the pull requests have to exist by then, summerofcode.withgoogle.com. INSAIT SURF pays 1,500 euros a month plus housing to do research in Sofia next to people from ETH Zurich. The companies in this document pay their interns, and an internship at Quantum Systems or Auterion or Flyability is the top-company experience you need on the page next to the self-initiative. 

The people, reached by work. Open source first: the maintainers of PX4 and ArduPilot work at Auterion and the companies on your list, and a merged pull request puts your name in their history and your face in their weekly call. Conferences second: ICRA and IROS, the two big robotics conferences, take student volunteers, who get in free and eat lunch with the people whose papers they read; ROSCon does the same for a hundred pounds. Professors third: a professor at Stanford, ETH or MIT answers a two-paragraph email from anywhere if it contains one specific question about their paper and one line about what you built. Send one a week. Read their courses first, because the courses are free: Stanford's CS231n on computer vision at cs231n.stanford.edu, and everything at MIT OpenCourseWare, ocw.mit.edu. 

Building in public, fourth. Post the field notes, the console GIF, the Substack and the Show HN. Founders read Hacker News and X daily.

The order, then: the hackathon and thirty emails, a merged pull request before February, SURF in January, and an internship at a company that builds.

## The people to write to

These are real companies, checked this week page by page, each with fresh money or fresh work and a founder who reads email. Sixteen names. The full list with sources and open roles is in the companion research document, and the Sunday hour at the end keeps it alive.

In Bulgaria, start with Dronamics. Eleven Ventures backed them first, the EU just committed up to thirty million euros, and Konstantin Rangelov, the CTO, has eleven engineering roles open in Sofia. EnduroSat raised a hundred million dollars last year to build satellites and has a junior harness engineer role open, and their free Space Challenges bootcamp every July is the best month a Bulgarian engineering student can spend. Fadron at Sofia Tech Park design, code and manufacture their own long-range drones and took money from Neo Autonomy in February, which makes them the closest thing in the country to your project as a company. Nomadium Robotics are six people building a long-range VTOL with an AI payload, and six people always need a seventh. Aviosense build radar for drones and have embedded roles open now. D Aerospace build industrial drones on the same open flight stack you will use. ID Robots in Plovdiv run a fleet platform for autonomous drones on ArduPilot and PX4. Bronia put acoustic AI on drones, and their CEO has your degree from your university.

In Europe, start with ABZ Innovation in Budapest, who build thirty-litre spraying drones with their own autonomy and raised seven million euros in January. They are the commercial version of what you are building, and your repository is the whole cover letter. Then the companies that hire students to fly and test: TYTAN in Munich keep a standing opening for a working student in flight testing, STARK have a flight-test intern role, Alpine Eagle want a working student to build drone prototypes, and Origin Robotics in Riga advertise a drone test pilot. Fly4Future in Prague, a spin-out of the university's multi-robot lab, want a test pilot who tunes PX4 and ArduPilot, which is you, an hour from your aunt. Korial in Darmstadt have fourteen student positions in AI and robot software. Flyability in Lausanne have a robotics internship open now, and Switzerland needs no visa from you. Auterion in Zurich are the company behind PX4, and for them a merged pull request is the email.

For Elena, if she wants a list of her own, the same rule applies: companies doing things that are hard, with people who are awake. In Sofia there are three: Checkpoint Cardio, who stream heart signals from wearables to an AI centre and ran a trial across five European hospitals; CoLumbo in Varna, who read spine MRIs with a model the FDA cleared, and have a junior developer role open; and Kelvin Health, who find artery disease with a thermal camera and a model trained on their own patients. In the world: Oxford Nanopore, who sequence DNA on a device the size of a phone. Isomorphic Labs in London, designing drugs with the models that won a Nobel prize. Cradle in Amsterdam and Latent Labs in London, designing proteins. Bioptimus and Owkin in Paris, foundation models for biology and pathology. CMR Surgical in Cambridge, surgical robots. Recursion, running biology experiments with robots. And the wearables and diagnostics companies, which is where a device that sends packets to a hub turns into a career: Oura in Finland, Withings in Paris, Empatica in Milan, whose wristband is cleared to detect seizures, Ultrahuman, Neko Health in Stockholm, who scan a whole body in minutes, Huma in London, and Bloom Diagnostics in Zurich. Read what they publish. A repository with her name on the console or the hub is the letter to any of them.

Two doors are bigger than any company. INSAIT in Sofia runs SURF, a paid summer research fellowship for undergraduates in computer vision and robotics, fifteen hundred euros a month with housing, applications in January. And ArduPilot has forty-seven open issues marked "good first issue" this week, a European developer call on Wednesday mornings, and a fund that gives a developer two hundred dollars for a sensor if he writes the driver. One merged pull request there says more than any email. The PX4 developer summit is in Prague on 7 to 9 October. Go.

## How to write to them

Read what a company builds until you have one real question, the kind only someone who does the work can answer. Then write five sentences: the line that proves you read their work, who you are, the repository with the number that makes it real, the question, and one ask. "I would like to learn how you do this and get involved. Could we talk for twenty minutes?" Under a hundred and fifty words, one link, to a named person. When they say yes, spend the call asking your questions and running the replay on a screen share, agree one next step with a date, and do it on the date. Thank them the same day. Make LinkedIn say what GitHub says, in the same words, with the drone in the photo, and post a field note after each stage.

Then keep the list alive, because the company that raised money last week is the company hiring this week. How is at the end.

## The rest of the year

The three weeks end and the habits stay. Every Sunday, one hour: the new funding rounds in drones, robotics and agtech on Dealroom and in Sifted, the portfolio pages of the four Bulgarian funds, the new YC batch when one is announced, and the YC jobs board. Add what you find to the sheet and write to two of them on Monday. Every day, ten minutes on Hacker News and one Startup School video. Every week, one answer in the PX4 or ArduPilot forum and one pull request open somewhere. Every month, a post on Substack about what changed. In January, the INSAIT SURF application. In February, the Google Summer of Code organisations are announced, and your open-source history has to exist by then. Next spring, the treatment level, when the blossom comes. Next summer, an internship at one of the companies you wrote to, or a batch.

