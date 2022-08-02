# wikispeedia-bot
A Twitter bot that plays [Wikispeedia](https://dlab.epfl.ch/wikispeedia/play/) 

## Usage
The front-end for this project is [@wikispeedia_bot](https://twitter.com/wikispeedia_bot/with_replies). It's currently turned off—I still need
to migrate it to an always-on service—but when it works, you can tweet at it in the form "@wikispeedia_bot {topic1} --> {topic2}", and it'll tweet back at you with
a path between the two topics. There are still some examples on Twitter, even though the bot is currently inactive.

## Examples
| Input  | Output |
|--------|--------|
| `King Solomon --> xenobiology` | `Solomon --> Hiram I --> Pharmacy --> Xenobiology` |
|`Old navy --> war crimes`| `Old Navy --> California --> Korean War --> War crime` |

## Search Algorithm
The most interesting part of this project is the algorithm that finds the path between articles. It's a  BFS based on a bidirectional implementation of
[Lee's Alogorithm](https://en.wikipedia.org/wiki/Lee_algorithm)—i.e., it starts at either end and flood-fills until there's some overlap.

I wrote it in a recursive way, basically taking advantage of the fact that
$BFS(P_0, P_n) \rightarrow P_0 + BFS(P_{1}, P_{n - 1}) + P_n$, which lends itself nicely to decomposing the search into smaller self-similar problems.

This approach has the added benefite of being very easy to write and not requiring any sophisticated data structures, but it is almost certainly slower
than it has to be. 

## TODO
- Host it somewhere so that it can be always-on
- Optimize the search algorithm
- Only search through links from main page—not in the images, sources, notes, etc
- Improve the aesthetic (the whole `-->` thing is a bit unsightly)


