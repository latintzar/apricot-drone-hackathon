# The Apricot Drone Hackathon

Build an orchard survey that ends with a clear bird's-eye map, close-ups for each tree, and a proposed route through trees a person selects for treatment planning.

**Two weeks · Your own hardware · One participant or a pair · A working example and a two-minute demonstration**

Start with [The World You Are Joining](WORLD.md): the short course, your GitHub and LinkedIn, and people to learn from. This README is the build brief. [Resources](resources/building.md) gives you a small set of tools and datasets. [Glossary](resources/glossary.md) explains the technical words.

## Start here: your first hour

1. Create your own GitHub account. Press **Use this template → Create a new repository** above and name it `apricot-drone`. Choose Public when you are ready to share the starter.
2. Open your copy in GitHub. Use **Code → Download ZIP** and extract it, or clone it with Git. The starter files are at the repository root.
3. Install Python 3.11 or newer from [python.org](https://www.python.org/downloads/). In a terminal opened in the project folder, run `python3 replay.py`. On Windows, use `py replay.py`.
4. Open the generated `output/review.html` in your browser. It shows three labelled practice records and exports a reviewed selection and a route drawing. The example uses invented coordinates and text observations so you can learn the flow.
5. Change one decision in the page, download the plan, and look at the JSON file. JSON is a text format programs use to exchange structured data. Compare the saved decision with the page.
6. Call your aunt or uncle. Fill in [HARDWARE.md](HARDWARE.md), especially the exact model, camera, access dates and control interface. An interface is the way your software communicates with another system.
7. Add a first entry to [LOG.md](LOG.md). Save your change as a commit through GitHub or Git. Use a message such as “Record the aircraft model and first experiment”.

The practice example is a small learning exercise. Your job is to replace it with real images, mapping and inspection. It stays offline and exports a planning file. Flight integration comes from your own tested aircraft-specific code.

## The challenge

Your aunt's orchard near Brno is the first place to try the system. Your uncle may help collect images and test your instructions. Arrange who will fly and when on day one. Elena can join on a part she enjoys; record who built each part.

The full survey has six steps:

1. **Survey:** a supervised aircraft follows a planned route and takes overlapping images.
2. **Map:** stitch a bird's-eye image, called an orthomosaic. Give each tree a stable ID and location. Start by marking crowns by hand, then try a tree detector.
3. **Suggest:** a model records visible observations and proposes closer inspections. Show its evidence and uncertainty beside each suggestion.
4. **Look closer:** the person approves trees to inspect. Collect closer images from suitable viewpoints and group them under each tree. A gallery lets the person open each image at full size. Use the camera's zoom or a checked flight path as appropriate for the hardware and space.
5. **Review:** the person records “reviewed”, “inspect again” or “treatment review”. A qualified assessment can then support a separate selection for treatment planning. Keep that decision, its author, evidence and time.
6. **Plan:** export the bird's-eye image with tree IDs, reviewed selections and a proposed route through selected trees. Export the decisions and coordinates as JSON or CSV too.

The final screen should answer: Which tree is this? What did we see? What did the person decide? Which trees appear in the proposed plan?

## Finish line and extensions

### Core submission: a complete software flow

- A real image set becomes a map with numbered trees and a gallery per tree.
- The person can save observations and inspection decisions, then separately select trees for treatment planning.
- The map and proposed route export with the underlying decisions and data source.
- A recorded example runs on another laptop, with clear setup steps.
- The repo includes a two-minute video, a field note and a short reflection.

Use your orchard's images where available. A licensed public image set is an accepted fallback; record its source and the field work still to do. Describe manual, simulated and automated steps separately.

### Full survey challenge: the two-week aim

Add a documented automated survey and approved close-up flights. Show that images from each selected tree arrive in the correct gallery. Confirm feasibility on day one: aircraft support, pilot availability, permitted location, camera control and access dates.

Each core milestone is useful on its own. At the day-seven check-in, use the evidence to decide which remaining flight work fits the fortnight. Keep the completed map and review flow ready to demonstrate.

### Next project: treatment

After the survey, scope actual spraying as its own project. Its work includes operating permission, a qualified treatment decision, payload integration, bench tests, measured flow and coverage, pilot override, and a record of the action. Water tests also need an appropriate operating basis when flown.

## Your two weeks

| Days | Work | Something to show |
|---|---|---|
| 1–2 | First three videos; publish an existing project; run the starter; identify aircraft and access; agree the demo | Hardware facts, starter output, first real image |
| 3–5 | Obtain images; stitch the map; mark and number trees; try a detector if useful | Bird's-eye map and first field note |
| 6–9 | Galleries, model observations and human review; test a close-up mission in simulation; collect field close-ups when ready | Saved decisions and images grouped by tree |
| 10–12 | Proposed route, map export, recorded replay; let your uncle try the instructions | Complete flow and a change based on feedback |
| 13–14 | README, two-minute video, reflection, LinkedIn; choose three people to contact | One link ready to share |

Arrange short check-ins with Peter around days 3, 7 and 14. Show the latest result, the main difficulty and the next experiment. The final demonstration is the recorded flow plus the field evidence you collected.

## Day-one questions

Fill the answers in [HARDWARE.md](HARDWARE.md) and [LEGAL.md](LEGAL.md).

- What are the exact aircraft model, camera, controller, firmware and take-off mass? What is fitted?
- What qualification does the pilot hold, and who will operate the aircraft in the Czech Republic?
- Which commands and photo exports does this exact model support? Find the official manual and compatibility list.
- Where are the aircraft and orchard? When can the pilot collect images? What permissions and flight-area checks apply?
- How many trees are there? What obstacles, people, neighbouring properties and access limits surround them?
- What problem has your aunt actually seen? What photos and any expert assessment already exist?
- What computer, operating system, memory and time do you have? What spending, if any, is agreed?

Choose a path from these answers: supported automated survey; pilot-collected images; or public data while you arrange the field session. Use the same map and review flow for each path.

## Engineering guidance

### Keep observations and decisions separate

A crown is the top of a tree. A detector can suggest where crowns are. A vision model can describe an image. A disease label needs evidence and a person qualified to assess it. Use an explicit “uncertain” state when the image is too distant or unclear.

Store the model's observation separately from the person's inspection decision and treatment selection. An approval tap records a workflow choice. For model training, use a separate label with its source and reviewer.

Start with human review and a pretrained model, if useful. Training your own detector is an extension after the flow works. Compare predictions against checked labels on different trees or a later flight. Keep neighbouring frames and augmented copies together when splitting training and test sets; otherwise the test can look better than performance on new trees.

### Match every image to a tree

Keep the original photo, timestamp, mission ID and tree ID. For a close-up mission, record which tree the camera targets and check a few matches by hand. The camera's GPS location describes the aircraft; a tree's location comes from the map or a measured reference. Record coordinate systems and units.

### Plot a proposed route

Start with a visible ordered line through selected tree centres. Label it “Proposed treatment route”. Keep it separate from recorded flight tracks. Save tree IDs, selection evidence, coordinates, coordinate system and the route order. Let the person review the order.

A field-ready mission needs additional planning for obstacles, positioning error, clearance, take-off and landing, reserve battery, travel between trees and pilot control. Distances and spray coverage need measured hardware and field data. Treat a route drawing as a planning output.

### Check the operating basis before each field session

Use the [EASA open-category requirements](https://www.easa.europa.eu/en/the-agency/faqs/open-category) and the [Czech Civil Aviation Authority](https://www.caa.gov.cz/en/). Record the applicable category, pilot credentials, operator registration, location restrictions, land access and insurance requirements. A qualification's weight limit is one fact among these.

EASA's open category requires operations that retain all carried material. A spraying operation therefore needs a separately established operating basis, including for water. Plant-protection products have additional rules under [Article 9 of Directive 2009/128/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32009L0128). Record the authority's guidance in LEGAL.md.

The pilot supervises the flight and retains a tested way to take control. Test new commands in the matching simulator first. Choose close-up distance and viewpoints from measured clearance and camera needs.

## What to submit

**README:** the family problem, one real image, current status, setup, results, credits and links to the notes. Example status format: “Map: [tested result]. Review: [tested result]. Survey flight: [manual / simulated / field-tested]. Close-ups: [status].”

**Recorded example:** source data or a small shareable subset, licence, setup and commands. Time a clean run on another machine. Large raw data can live in a linked download with checksums and access instructions.

**Two-minute video:** show the map, choose a tree, open close-ups, record a decision and export the proposed plan. Include the real aircraft when field work is part of the result. Label recorded and simulated footage.

**Field note:** aircraft and conditions, what you intended, what happened, measured results, an image and the next change. Use [the template](docs/field-notes/TEMPLATE.md).

**Reflection:** 150–300 words about expectations, evidence, learning and the next experiment. Use [the template](reflections/TEMPLATE.md).

**Media:** the aircraft, the map, a gallery, one useful failure and the final route. Collect these while building. Publish images with permission and remove home coordinates from public copies. Keep private originals for measurement.

**Instructions for your uncle:** one page explaining preparation, the approved collection steps, how to transfer files, and what result to report. Observe him using it and improve one confusing step.

A project page and a learning journal are optional ways to share the same work. [The guide](WORLD.md#4-put-your-work-where-people-can-see-it) explains each medium and gives examples.

## How the work is reviewed

| Question | Weight | Evidence |
|---|---|---|
| Does the submitted flow work? | 40% | Someone repeats the example; the map, galleries, decisions and export agree |
| Can a visitor understand it? | 20% | A clear README, real images and a short demonstration |
| Do the claims match the evidence? | 20% | Sources, measured results, uncertainty and failures |
| Can another person build on it? | 20% | Setup, data licence, hardware facts and useful instructions |

## Use an agent

Copy this into your coding agent. Claude Code is one option; use the tool you have access to. The agent that helps write code and the image model in your project are separate tools.

```text
I am Ilian, a student building the Apricot Drone Hackathon.
Read https://raw.githubusercontent.com/latintzar/apricot-drone-hackathon/main/WORLD.md
and https://raw.githubusercontent.com/latintzar/apricot-drone-hackathon/main/README.md.
Read this repository's CLAUDE.md or AGENTS.md and inspect the files.

Help me learn while I build. Use short, clear English. Define new terms
with an example. Ask the day-one questions one at a time and record
my actual answers in HARDWARE.md and LEGAL.md.

Our two-week goal is the survey, per-tree inspection, human review and
an exported proposed treatment route. Actual spraying is a later project.
Use the documented aircraft capabilities to agree which flight steps fit.
Start with the runnable offline exercise, then one real image.

Plan small steps. Explain the code, let me run it and inspect the result.
Ask me to explain an important change back to you. Base claims on actual
outputs. Mark sample data, estimates and measurements separately.
Keep model observations, checked labels and human decisions separate.
Treat flight commands as a separate, explicitly reviewed integration.
Help me write from my own notes and credit the tools and people involved.

First: tell me the next three small steps, then ask the first hardware question.
```

## Files in your copy

- `replay.py` and `sample/`: the small offline learning exercise.
- `HARDWARE.md`, `LEGAL.md`, `LOG.md`: facts and work record.
- `docs/field-notes/`, `reflections/`, `media/`: evidence and explanations.
- `aircraft/`, `perception/`, `console/`: space for your implementation.
- `resources/`: tool links, datasets, glossary and company directory.
- `WORLD.md`: the course and the wider guide.

As your project grows, rewrite this README around your own work. Keep a link to the original brief. The root MIT licence covers the starter code; check and record the separate licences of any libraries, models and datasets you add.
