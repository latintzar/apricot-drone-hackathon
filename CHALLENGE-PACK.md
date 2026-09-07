# The Apricot Drone Hackathon

For Ilian. From Peter, September 2026.

## Why I am writing this

You are nineteen, you can fly a 20 kg drone, you study the thing Stanford calls CS plus robotics, and there is a real drone standing in a garden in the Czech Republic waiting for you. You have three weeks before term. That is a hackathon, and this document is the brief.

The people you have been writing to are the wrong people. A job board is a filter built by someone who wants fewer applicants. The companies that answered you with silence are run by people who are afraid of you. Forget them.

The people who will change your life are building things. Founders, CTOs, the engineers at a company that just raised money. They hire on evidence, and the only evidence that counts is something you built that they can open in a browser and run. A CV tells them what you say about yourself. A repository tells them who you are.

So here is the whole plan. The first half is a hackathon: build one thing, in public, in three weeks. The second half is what you keep doing all year, and the world you are doing it in. Write it up so well that a stranger understands it in a minute and an engineer respects it in five. Then write to thirty people with the link. That is how a nineteen-year-old in Sofia ends up at Anduril, or Oxford Nanopore, or on a Knight-Hennessy scholarship at Stanford, or in NATO's DIANA accelerator with a company of his own. I have watched it happen to people with less than you have.

## The brief

The apricot drone. Your aunt's garden has apricot trees and the neighbour's tree is sick with a fungus. Build the open-source system that flies over the orchard on its own, photographs every tree, and comes back with a map where every tree is outlined and coloured: green is fine, amber is worth a look, red is a risk, and the label says what kind. The map says what it wants to do next, which trees deserve a close look and from which side. You approve, or change it with a tap. The drone flies out again and circles each chosen tree, low, taking close-ups all the way round. Those come back sorted by tree into a gallery of tiles you can tap open and tap shut. When you are sure, you tap spray. The drone goes over the tree, sprays, shows you the progress as it happens, lets you stop it at any second, and says "spraying done".

That is both autonomous and collaborative, and it is the right shape. The drone does the flying, the looking and the spraying. The model does the first reading and the proposing. You do the deciding. Every decision you make teaches the model, because every tap is a label. If the model turns out to see nothing useful from thirty metres up, say so in the log with the pictures that prove it, and the console with a human deciding remains a product your aunt can use. That is an honest result and a good one.

This is a good project for four reasons. It has a real user, your aunt, who will tell you the truth. It has real hardware you already own. It has real unknowns, so the story of solving them is interesting. And it produces things a stranger can look at: a coloured map, a gallery, a video of a circling drone, a table of results.

Spraying drones exist. DJI sells thousands. Papers exist on disease detection from drone images, and the datasets from them are yours to use; the last section of this document lists them. None of that makes the idea less worth doing. Nobody who matters asks whether an idea is new. They ask whether you built it, whether it works, and whether they can read the log.

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

Elena helps if she wants to, on any piece she picks. The console is the natural one, because it is a web app and it is the thing people will see. Or the hub, the small server that receives the drone's packets and stores them. Whatever she builds, her name goes on the repository for that piece, and a pull request with her name on it is worth more than a line in the credits.

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

The repository is for engineers. The project page is for everyone else: the founder who has five minutes, the professor, the scholarship committee, your aunt. It tells the story with pictures, and it links to the repository at the bottom.

Buy a domain. Your own name, ilian-something.dev or .com, about ten euros a year, from Cloudflare or Porkbun. It goes on LinkedIn, in every email and on the repository, and it is yours for the rest of your life. Under it, two things, both free to host.

The project site, at apricot.yourname.dev. One long page: the video at the top, the story, a picture per level, the map, the console GIF, the numbers, the reflections, the link to the code. GitHub Pages serves it straight from the docs folder of the repository, and Vercel does the same with a nicer deploy if you prefer; either takes an hour. It is the page you put in every email.

The live demo, at demo.yourname.dev. This is the part that makes people stop. The console itself, hosted on Vercel, loaded with a recorded flight: the real orthomosaic, the real tree numbers, the real close-ups from your orbits. A founder opens it on a phone, taps tree 12, sees the gallery, taps spray, watches the bar fill against the recorded log. No drone, no login, thirty seconds. Vercel's free plan hosts a static web app on your own account, made with your GitHub login in two minutes, and the console is a static web app once its data is a folder of JSON and images. Build the console so that the same code runs live in the garden and replayed on the web, and this demo costs you nothing extra.

Claude Code sets all of this up in an afternoon: the domain records, the GitHub Pages build, the Vercel deploy from the console folder, and the Substack. Ask it for the plan, buy the domain and open the accounts yourself, and let it do the rest.

The writing goes on Substack. Four posts over the three weeks: "Why I am building a drone that sprays apricot trees" on day one, one post at the end of level one with the console GIF, one at the end of the detector with the failure gallery, and "What I built in three weeks" on day twenty-one with the video. Each post is the log and the reflection for that stretch, rewritten for a reader, eight hundred words, five pictures. Substack gives you an email list, which means the founder who reads post one gets post four without you asking. Post the last one to Hacker News as "Show HN" and to the PX4 and ArduPilot forums, and put the links on LinkedIn with the drone in the photo.

## The Claude Code week

You have Claude Code for a week, and so does Elena. That is the tool for writing the code. Which model reads your trees is a separate choice, made above. Used well, it is a senior engineer sitting next to you. Used badly it writes you a pile of plausible code you cannot explain in an interview.

Use it like this. Start every session by pasting the section of this document you are working on and your last field note. Ask for a plan before code, read the plan, and cut what you do not understand. Let it write the boring parts: the scaffold, the tests for the maths, the field-note template, the replay tool. Make it ask you questions before it assumes anything about the aircraft. Every result comes from you. When it claims something works, run it yourself and paste the real output back. Keep a file called CLAUDE.md at the root of the repository with the aircraft, the SDK, the conventions and the stage you are on. It reads that every session, and so will the next person who opens your repository.

The two prompts at the end of this document are written to be pasted as the first message of a fresh session. They tell it to interview you first.

## The people to write to

These are real companies, checked this week page by page, each with fresh money or fresh work and a founder who reads email. Sixteen names. The full list with sources and open roles is in the companion document, and the Sunday hour below keeps it alive.

In Bulgaria, start with Dronamics. Eleven Ventures backed them first, the EU just committed up to thirty million euros, and Konstantin Rangelov, the CTO, has eleven engineering roles open in Sofia. EnduroSat raised a hundred million dollars last year to build satellites and has a junior harness engineer role open, and their free Space Challenges bootcamp every July is the best month a Bulgarian engineering student can spend. Fadron at Sofia Tech Park design, code and manufacture their own long-range drones and took money from Neo Autonomy in February, which makes them the closest thing in the country to your project as a company. Nomadium Robotics are six people building a long-range VTOL with an AI payload, and six people always need a seventh. Aviosense build radar for drones and have embedded roles open now. D Aerospace build industrial drones on the same open flight stack you will use. ID Robots in Plovdiv run a fleet platform for autonomous drones on ArduPilot and PX4. Bronia put acoustic AI on drones, and their CEO has your degree from your university.

In Europe, start with ABZ Innovation in Budapest, who build thirty-litre spraying drones with their own autonomy and raised seven million euros in January. They are the commercial version of what you are building, and your repository is the whole cover letter. Then the companies that hire students to fly and test: TYTAN in Munich keep a standing opening for a working student in flight testing, STARK have a flight-test intern role, Alpine Eagle want a working student to build drone prototypes, and Origin Robotics in Riga advertise a drone test pilot. Fly4Future in Prague, a spin-out of the university's multi-robot lab, want a test pilot who tunes PX4 and ArduPilot, which is you, an hour from your aunt. Korial in Darmstadt have fourteen student positions in AI and robot software. Flyability in Lausanne have a robotics internship open now, and Switzerland needs no visa from you. Auterion in Zurich are the company behind PX4, and for them a merged pull request is the email.

For Elena, if she wants a list of her own, the same rule applies: companies doing things that are hard, with people who are awake. In Sofia there are three: Checkpoint Cardio, who stream heart signals from wearables to an AI centre and ran a trial across five European hospitals; CoLumbo in Varna, who read spine MRIs with a model the FDA cleared, and have a junior developer role open; and Kelvin Health, who find artery disease with a thermal camera and a model trained on their own patients. In the world: Oxford Nanopore, who sequence DNA on a device the size of a phone. Isomorphic Labs in London, designing drugs with the models that won a Nobel prize. Cradle in Amsterdam and Latent Labs in London, designing proteins. Bioptimus and Owkin in Paris, foundation models for biology and pathology. CMR Surgical in Cambridge, surgical robots. Recursion, running biology experiments with robots. And the wearables and diagnostics companies, which is where a device that sends packets to a hub turns into a career: Oura in Finland, Withings in Paris, Empatica in Milan, whose wristband is cleared to detect seizures, Ultrahuman, Neko Health in Stockholm, who scan a whole body in minutes, Huma in London, and Bloom Diagnostics in Zurich. Read what they publish. A repository with her name on the console or the hub is the letter to any of them.

Two doors are bigger than any company. INSAIT in Sofia runs SURF, a paid summer research fellowship for undergraduates in computer vision and robotics, fifteen hundred euros a month with housing, applications in January. And ArduPilot has forty-seven open issues marked "good first issue" this week, a European developer call on Wednesday mornings, and a fund that gives a developer two hundred dollars for a sensor if he writes the driver. One merged pull request there says more than any email. The PX4 developer summit is in Prague on 7 to 9 October. Go.

## How to write to them

Read what a company builds until you have one real question, the kind only someone who does the work can answer. Then write five sentences: the line that proves you read their work, who you are, the repository with the number that makes it real, the question, and one ask. "I would like to learn how you do this and get involved. Could we talk for twenty minutes?" Under a hundred and fifty words, one link, to a named person. When they say yes, spend the call asking your questions and running the replay on a screen share, agree one next step with a date, and do it on the date. Thank them the same day. That habit alone puts you ahead of almost everyone they meet. Make LinkedIn say what GitHub says, in the same words, with the drone in the photo, and post a field note after each stage.

Then keep the list alive, because the company that raised money last week is the company hiring this week. How, and what else to do all year, is two sections down.

## The world you are joining

Nobody in Sofia will have explained this to you, so here it is in a page. Read it twice.

A startup is a company built to grow fast, usually on software or hardware, usually funded by investors who buy a share of it early. An accelerator is a school for those companies: it takes a group of them at once, gives each some money, three months of help, and a demo day where investors watch them pitch. The group is called a batch. The companies in a batch are named by it forever, the way a university class is named by its year.

Y Combinator, in San Francisco, is the one that matters most. It has run since 2005, funded Airbnb, Stripe, Dropbox, Coinbase and Reddit, and now takes batches four times a year from anywhere in the world, moves them to San Francisco for three months, and invests half a million dollars in each. A nineteen-year-old in Sofia with a repository that flies can apply. ycombinator.com/apply. Everything YC has learned is free: the Startup School videos at startupschool.org, which you will watch all of this year, one a day, and the YC Library at ycombinator.com/library. Their Requests for Startups page, ycombinator.com/rfs, says what they wish someone would build, and there is always a robotics line in it. The list of every company in every batch is at ycombinator.com/companies, and their open jobs at news.ycombinator.com/jobs. Those jobs are the exact target of this whole document. A YC company that just raised is a company hiring a person like you.

Others in the same family. Speedrun, run by the venture firm a16z, invests up to a million dollars in new companies, many in games and hardware, speedrun.a16z.com. Entrepreneur First, in London and Paris, takes individuals before they have a company or even a co-founder, and pairs them; it is built for a person exactly your age and shape, joinef.com. Antler does the same in thirty cities. Station F in Paris is the largest startup campus in the world, a building with a thousand companies and a dozen programmes inside, stationf.co. The Thiel Fellowship gives 250,000 dollars over two years to people under 23 who want to build instead of sit in a classroom, thielfellowship.org. Z Fellows is one week and ten thousand dollars for young builders who want a fast door into Silicon Valley, zfellows.com. Write these five down. Every one of them takes people from anywhere, and the repository is the application.

The places. San Francisco is where the money, the ambition and the hardest engineers are; the culture is that you are judged by what you shipped and nothing else, which is the culture this document is trying to give you a year early. London has the biggest scene in Europe, DeepMind, Isomorphic, Entrepreneur First, and most of the European money. Paris has Station F, Mistral and the new biology-AI companies. Munich and Berlin have become the drone and defence cluster: Helsing, Quantum Systems, STARK, TYTAN and Alpine Eagle are all within an hour of each other, and they are hiring students. New York is finance and media and a growing hardware scene. Tallinn built Skype, Bolt and Wise from a country smaller than Bulgaria, which is the proof that where you start does not decide where you end.

Where Bulgaria fits. It is small and it is real. Four funds worth knowing, Eleven, LAUNCHub, Vitosha and Neo, whose portfolio pages you read every Sunday. Two companies the world takes seriously, Dronamics and EnduroSat, both in Sofia, both in your field, and both in the companies section. INSAIT, an institute built with ETH Zurich and EPFL that publishes at the top conferences and pays undergraduates to do research in the summer. Sofia Tech Park, with drone and robotics labs you can walk into. A defence-technology wave that put more venture money into Bulgarian defence and dual-use companies in 2025 than into any other country in the region. And The Recursive, the news site for startups in this part of Europe, therecursive.com, which you read the way you read the local paper. Bulgaria is a good place to build a first thing and a bad place to wait for permission. Build here, publish to the world, and let the world come.

The press. Hacker News, news.ycombinator.com, every day; it is where engineers talk and where you will post your project. TechCrunch, the trade paper for startups worldwide, for the funding announcements. Sifted, sifted.eu, the same for Europe, and the one that will cover the companies on your list. Dealroom for the data behind the news.

The people to listen to. Paul Graham's essays, starting with "How to Do Great Work", "Do Things That Don't Scale" and "How to Get Startup Ideas", one a week. On the Lex Fridman podcast, four long conversations worth every hour: Andrej Karpathy on building Tesla's self-driving, episode 333; Robert Playter, the CEO of Boston Dynamics, on legged robots, episode 374; Jim Keller on how chips and engineers actually work, episode 162; and Sam Altman, episode 419. They are three hours each. Listen while you label images.

The top of the world, and how to watch it. Your field has a frontier, and it moves every week. In robotics and drones it is Boston Dynamics, Skydio, whose drones fly themselves through forests with cameras alone, Anduril, the company that made defence a startup category, Figure and 1X, building humanoids, and Physical Intelligence, which is trying to build one model that runs any robot, physicalintelligence.company. In AI it is Google DeepMind, OpenAI, Anthropic and NVIDIA, whose research pages are public and readable, deepmind.google/research, anthropic.com/research, research.nvidia.com. Everything these people publish appears first on arXiv; the robotics list is at arxiv.org/list/cs.RO/recent and Hugging Face's daily papers page, huggingface.co/papers, ranks the ones people are actually reading. Read the abstracts every morning with your coffee, and one full paper a week. Import AI, Jack Clark's weekly newsletter, tells you what mattered, importai.substack.com. The Dwarkesh podcast is where the researchers at those labs explain themselves at length, dwarkesh.com. The State of AI report, once a year, stateof.ai, is the map. Within three months of this habit you will know what the top of the field is doing before most professors in Sofia do, and that knowledge is what makes your emails interesting.

## Getting into the rooms without the money

Your family cannot pay for Stanford. Almost nobody's can, and it turns out that is beside the point. The networks you want are entered by work, and the doors that matter pay you. Here is how a nineteen-year-old in Sofia gets in this year.

The doors that pay you. Every accelerator and fellowship in the previous section gives you money, and asks only what you built. YC invests half a million dollars. Entrepreneur First pays a stipend while you find a co-founder. The Thiel Fellowship is 250,000 dollars. Z Fellows is a paid week in Silicon Valley. Google Summer of Code pays you to write open-source code for three months, from your bedroom, for a project like ArduPilot, and Google's name goes on your CV; organisations are announced each February, so the pull requests have to exist by then, summerofcode.withgoogle.com. INSAIT SURF pays 1,500 euros a month plus housing to do research in Sofia next to people from ETH Zurich. The companies in this document pay their interns, and an internship at Quantum Systems or Auterion or Flyability is the top-company experience you need on the page next to the self-initiative. None of these ask what your parents earn.

The people, reached by work. Open source first: the maintainers of PX4 and ArduPilot work at Auterion and the companies on your list, and a merged pull request puts your name in their history and your face in their weekly call. Conferences second: ICRA and IROS, the two big robotics conferences, take student volunteers, who get in free and eat lunch with the people whose papers they read; ROSCon does the same for a hundred pounds. Professors third: a professor at Stanford, ETH or MIT answers a two-paragraph email from anywhere if it contains one specific question about their paper and one line about what you built. Send one a week. Read their courses first, because the courses are free: Stanford's CS231n on computer vision at cs231n.stanford.edu, and everything at MIT OpenCourseWare, ocw.mit.edu. The lecture is the same one the Stanford student sits in; the difference is the tuition, and you just skipped it.

Building in public, fourth, and it is the one that scales. Post the field notes, the console GIF, the Substack and the Show HN, because the founders in San Francisco read Hacker News and X every morning, and a nineteen-year-old with a drone that sprays apricot trees is exactly the kind of thing they repost. Your aunt's orchard is a better story than a tuition receipt, and it travels further.

If one day you want a degree abroad, that is your decision and not this document's, and you should know the fully funded ones exist and Bulgarians win them: Fulbright for the United States, Chevening for the United Kingdom, Gates Cambridge, Rhodes and Knight-Hennessy, all selecting on exactly the evidence you are about to produce. For now, the order is this hackathon and thirty emails, a merged pull request before February, SURF in January, and an internship at a company that builds.

## The rest of the year

The three weeks end and the habits stay. Every Sunday, one hour: the new funding rounds in drones, robotics and agtech on Dealroom and in Sifted, the portfolio pages of the four Bulgarian funds, the new YC batch when one is announced, and the YC jobs board. Add what you find to the sheet and write to two of them on Monday. Every day, ten minutes on Hacker News and one Startup School video. Every week, one answer in the PX4 or ArduPilot forum and one pull request open somewhere. Every month, a post on Substack about what changed. In January, the INSAIT SURF application. In February, the Google Summer of Code organisations are announced, and your open-source history has to exist by then. Next spring, the treatment level, when the blossom comes. Next summer, an internship at one of the companies you wrote to, or a batch.

## Datasets, pointers and links

Every link here was opened and read this week. The full list, with licences, sizes and the ones that came back empty, is in the companion document.

The apricot thing you remember. There is a Roboflow project by a user called bilal-jan, "Apricot-brown-rot": 135 photos, licence CC BY, classes brown rot and gummosis, with a sister set of 149 healthy apricots. universe.roboflow.com/bilal-jan/apricot-brown-rot. Behind the name are two papers. Jamil Ahmad and Bilal Jan wrote the plum paper in Sensors 2020, brown rot and shot hole photographed on phones in Swat, five thousand images, the method you will copy: transfer learning, ninety-two percent, and heat maps showing the network looked at the lesions. Jamil Ahmad then wrote the apricot drone paper, Expert Systems with Applications 2025, apricot brown rot and shot hole photographed from a DJI Mavic Mini, the exact crop, the exact diseases and the exact camera class. That dataset is unpublished. Write to him on day one and ask for it; one email is worth three days of searching.

The five links for day one. First, the pear rust paper in Agronomy 2024, which is your project already built on pears: two flights at 17 and 8 metres, an orthomosaic, YOLO, symptoms turned into GPS points, and an infection intensity per tree on a five-band colour scale. That is the risk map. mdpi.com/2073-4395/14/11/2643. Second, its dataset, the only drone-altitude tree-disease set in the open: 584 annotated images at 5 to 12 metres, in YOLO format, CC BY. data.mendeley.com/datasets/44kjgc4gkc/1. Train on it in week one and fly your apricots at the same height. Third, DeepForest, which finds every tree crown on an orthomosaic in an afternoon and ships a classifier for dead versus alive crowns, a risk signal on day one. github.com/weecology/DeepForest. Fourth, the MAVSDK orbit example, forty lines of Python that circle a point. github.com/mavlink/MAVSDK-Python/blob/main/examples/do_orbit.py. Fifth, OpenDroneMap, which stitches; 16 GB of RAM handles 250 images and a GPU changes nothing. docs.opendronemap.org/installation.

Datasets you can download this week, all CC BY unless said. ATZD01, the largest apricot set in existence, 6,055 photos and 20,272 boxes across eleven diseases and pests including 9,023 shot-hole and 480 brown-rot instances, from three orchards in China; the archive is password-locked and the mirror is dead, so open an issue at github.com/meanlang/ATZD01 and email Prof. Zhiyong Tao's group today, because it takes days. Peach Disease on Roboflow by zeerox, 1,081 photos with boxes for brown rot, shot hole and bacterial spot, one click to YOLO format. universe.roboflow.com/zeerox/peach-disease. PlantCity, 10,667 field photos from Pakistan across twelve crops, with 208 apricot shot-hole leaves. data.mendeley.com/datasets/w8kh2xkspx/4. The Turkey plant dataset, the only one that names Monilinia laxa on apricot by species. github.com/mturkoglu23/PlantDiseaseNet. CherryLeaf-KG, 400 clean cherry leaves with shot hole and brown rot, keep it as your test set. data.mendeley.com/datasets/wp3b6pz9gc/3. The plum set with 643 shot-hole images. data.mendeley.com/datasets/w7sdx55m7z/1. And the cherry orchard drone set from Greece, 42 GB, 577 trees photographed from the air and the ground across a whole season with a severity grade per tree by an agronomist: it is your architecture already built once, so copy its structure. zenodo.org/records/7144071. For the fire-blight close-up set, whose "maybe" class is a ready-made bucket for "send a human", data.mendeley.com/datasets/fpmnncmg84/1.

What came back empty, so you can stop looking: there is no public image set for Eutypa, for bacterial canker on stone fruit, or for any apricot orchard photographed from above. The two 875-image "shot hole" sets on Roboflow are grapevines. That gap is the space your repository sits in.

The building blocks. Tree crowns: DeepForest for boxes, then segment-geospatial to turn them into polygons with world coordinates. github.com/opengeos/segment-geospatial. Stitching: ODM, with NodeODM as the API you call from code, and a geo.txt file whose spare column can carry the tree number through the stitch. docs.opendronemap.org/geo. The orbit: PX4 orbit mode, docs.px4.io/main/en/flight_modes_mc/orbit.html, one metre a second by default, nose to the centre, and it will refuse to arm in orbit, so take off in another mode first; on ArduPilot the same thing is CIRCLE mode or a loiter-turns command paired with a region of interest, and the region of interest stays set until you clear it. ardupilot.org/copter/docs/circle-mode.html. Skip DroneKit; it stopped in 2019. Simulation before flying: PX4's SIH simulator runs with nothing installed and is where you build the orbit on your laptop. docs.px4.io/main/en/simulation. Photos to trees: log the tree number and the time when you command each orbit and match photos by their timestamp; the geometry method works too, but the drone's GPS is where the drone was, and on a ten-metre orbit the neighbouring tree wins. Training: Ultralytics for YOLO, Label Studio with its ML backend so your model pre-labels and you only correct, and FiftyOne to look at a tree's photos before you build the gallery. The proposals: TypeFly, github.com/typefly/TypeFly, is an open project where a language model plans a drone's actions from a detector's view of the scene, which is your level one in someone else's code, and DeepDrone, github.com/evangelosmeklis/deepdrone, is a web console with a live map, mission planner, replay and an emergency stop, so lift its interface ideas. The pump: ArduPilot has a sprayer built in, set SPRAY_ENABLE, put the pump on an output with function 22, and a single MAVLink command turns it on and off. ardupilot.org/copter/docs/common-sprayer.html. On PX4 it is one line, set_actuator, on a peripheral output. docs.px4.io/main/en/payloads/generic_actuator_control.html. The console is a web page; the rest is wiring you already understand.

The law, in one sentence you can cite. Article 9 of EU Directive 2009/128 says member states shall ensure that aerial spraying is prohibited, with derogations only for approved products and certified operators. So you spray water, you say so on the page, and your contribution is the targeting with a human approving and a stop button. That is the answer a judge will ask about, and it is a better demo than pretending.

Where the people are. The Dronecode Discord for PX4 and MAVSDK questions, discord.gg/dronecode. The ArduPilot forum, whose sprayer threads are good. The OpenDroneMap forum, where someone will spot your overlap mistake within the hour. The DeepForest issues page, answered by ecologists who like real questions.

How to search for more. On Google Scholar: apricot "brown rot" OR "shot hole" detection UAV deep learning. On GitHub: orchard drone stars:\\5 pushed:\\2025-01-01, and path:\\.py "do_orbit" to find every real orbit implementation. On Roboflow: search class:"apricot leaf", because the class operator searches labels, which is the only way to find the small sets. On Zenodo, use the API: zenodo.org/api/records?q=orthomosaic+AND+orchard&type=dataset. The Czech words that unlock Czech sources: peckoviny for stone fruit, meruňka for apricot, moniliová spála peckovin for blossom blight, suchá skvrnitost listů peckovin for shot hole, and šarka, the plum pox virus, which is what a Czech grower actually worries about. The Czech plant-protection portal is rlportal.ukzuz.cz.

Two things most likely to eat your three weeks: installing Detectron2, so use DeepForest boxes unless they visibly fail, and adopting ROS 2, which MAVSDK makes unnecessary. Two things that save the most: the SIH simulator, and logging the tree number at the moment you command the orbit.

## For agents

You will use Claude Code for most of this, and the fastest way to give it everything is one paragraph. Paste this as the first message of a fresh session; it fetches this whole document from the Drive folder, writes the CLAUDE.md file for your repository, and then interviews you. The rules inside it are the ones that keep you doing the work.

```
You are helping me, Ilian, run a three-week hackathon and then keep it going all year. Fetch and read the entire brief before you do anything: https://drive.google.com/uc?export=download&id=1oLiD1jfimaN2GgULBM8jM0-1eote1sdn

Rules that never change:
- I do the work. You plan, scaffold, write the boring parts, review, and ask. When something needs running, flying or measuring, tell me what to run and wait for me to paste the real output.
- Interview me before you assume anything about the aircraft, the sprayer, the orchard, or my time.
- Reading companies, their websites and their people is my job. I browse, I pick the person, I write the question. You tighten what I wrote and keep the sheet.
- When I ask you to mentor me, tell me the truth about my work. Flattery wastes my time. Name what is weak, say why, and show me what strong looks like.
- Every number in the repository is one I measured. Where you do not know, write "[measure this]".
- Short sentences. Say what a thing is. Sentence-case headings. Commit after every step with a one-sentence message.
- Keep CLAUDE.md at the repository root current: the aircraft, the flight stack, the sprayer, the conventions, the level I am on, and the job we are doing. You read it every session.

First, write CLAUDE.md from the brief and this message. Then tell me in three sentences what the three levels are, and ask me the first question from Prompt B.
```

After that, every session starts with one plain sentence that names the job. Seven are about the hackathon. The eighth, Mentor, is about you, and it is the one you will use all year.

- Build. "We are on level one, day four. Plan the grid mission module and its tests, then wait." It plans, you cut what you do not understand, it writes, you run.
- Working condition. "Get me to working condition." It checks the installs, tells you which accounts to open, and stops when the five things are true.
- Publish. "Set up the project site and the live demo." It does GitHub Pages, the Vercel deploy from the console folder with a recorded flight, the DNS records, and a Substack template. You buy the domain and open the accounts.
- Write. "Turn today's log entry into the reflection for the console." It uses the seven questions, in your voice, from your log and your numbers, and leaves blanks where it has none.
- Outreach. You read the company's site yourself, pick the person, and write the question and a first draft. Then: "I read Fadron. Vasil Petrov, CTO. Here is my question and my draft. Tighten it to five sentences and add the row." It tightens and files. You send.
- Sunday. You do the hour yourself: Dealroom, Sifted, the fund portfolios, the YC directory. Then: "Here is what I found this Sunday. Add the rows and tell me which two to write to first." It files and ranks.
- Mentor. "Be my mentor today." Then say what is on your mind: a founder answered and you have a call tomorrow; you do not understand what a term sheet is; you want to know what to learn next; you read a paper and half of it went past you; you want a mock interview for an internship; you wrote a Substack post and want the truth about it. It explains like a senior engineer who has been where you want to go, reviews your work without flattery, points you at the exact YC video, essay or paper for the thing you are doing that week, and ends every session with one thing to do before the next one.
- Judge. "Judge the repository as a stranger." It answers the four questions: does it work, can a stranger understand it in a minute, is it honest, could someone else build it. Then it lists what to fix, and you fix it.

The file START-HERE in the folder has the same list. What only you can do: fly, tap, measure, read the companies, pick the person, write the question, buy the domain, open the accounts, send the emails, write the cold open, take the photos.

The two prompts below are the long form for the first two sessions. They are written for the machine, so they are lists.

### Prompt A, the portfolio (Ilian, day one)

See prompts/A-portfolio.md

### Prompt B, the apricot drone (Ilian, and Elena on the console if she joins)

See prompts/B-apricot-drone.md
