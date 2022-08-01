# wikispeedia-bot
A Twitter bot that plays Wikispeedia

## Usage
The front-end for this project is [@wikispeedia_bot](https://twitter.com/wikispeedia_bot/with_replies). Tweeting at it currently doesn't actually do anything—although
there are still some examples of its work on Twitter—since I haven't migrated it to some always-on cloud service. [*Quick, quick, add that to the to-do list*]

## [Wikispeedia](https://dlab.epfl.ch/wikispeedia/play/) 
Perhaps the single greatest way to pass time in 10th grade personal finanace, try to find your way from one Wikipedia page to another through internal links—thereby providing 
data for some research project. (Of course, making a bot to do it for you both defeats the point of the research *and* sucks the joy out of the game.)

## Examples
| Input  | Output |
|--------|--------|
| `King Solomon --> xenobiology` | `Solomon --> Hiram I --> Pharmacy --> Xenobiology` |
|`Old navy --> war crimes`| `Old Navy --> California --> Korean War --> War crime` |

## Search Algorithm
I named it `twoWayCloudSearch`—I suppose my mental image of it is two clouds expanding until they intersect? Anyway, it's just a BFS based on a bidirectional implementation of
[Lee's Alogorithm](https://en.wikipedia.org/wiki/Lee_algorithm). It's also recursive, because that made it very easy to write, but definitely shouldn't be because that leads to
significant recomputations.

## TODO
- Host it somewhere so that it can be always-on
- Optimize the search algorithm
- Only search through links from main page—not in the images, sources, notes, etc
- Improve the aesthetic (the whole `-->` thing is a bit unsightly)


