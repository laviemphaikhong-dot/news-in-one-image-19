# Thursday 19 November 2026 — the whole day on one page

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/laviemphaikhong-dot/news-in-one-image-19/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/laviemphaikhong-dot/news-in-one-image-19/reward.svg)](https://make.fun/bounty/news-image-20261119)

My entry for make.fun's [Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

The image is a single broadsheet page carrying **46 stories from
7 regions — and every story on it belongs to Thursday 19 November
2026**. Down the page you will find a timeline of the day in UTC,
four lead stories with summaries, a twelve-story grid, a dotted world
map dotted with the day's events, thirty further one-line stories, and
a date-check box listing the tempting stories that were verified and
then excluded for belonging to other days.

## The four leads

1. **Shenzhen** — Donald Trump, Xi Jinping and Vladimir Putin sit
   down together for the first trilateral summit in history, held on
   the sidelines of APEC, with a draft joint statement on the table
   and nuclear arms control at the top of Trump's agenda.
2. **GTA VI launch day** — Rockstar's game opens worldwide to a
   Metacritic score of 99; Twitch peaks at 3.29 million simultaneous
   viewers, a platform record.
3. **The Strait of Hormuz** — a tanker is struck off Khasab while
   Iran claims three tankers caught fire on mines and two American
   drones were shot down; CENTCOM answers that all of its personnel
   are accounted for.
4. **The Crimea Bridge** — Ukraine hits the Kerch crossing for the
   third time in a week, hours after a record 1,441-drone night
   across Russia; Moscow replies against Kyiv's bridges and Odesa,
   where three people die.

## Also between the rules

Gold's crash to a 14-month low · thirty leaders in Berlin for Ukraine
talks · Nvidia's record $115.8bn quarter · COP31's fossil-fuel
argument in Antalya · the World Court's Myanmar judgment · Israel's
first big Gaza ground push since the truce · Anthropic's Nasdaq debut
· a $190.4m Van Gogh · Ethiopia–Eritrea clashes · Cyclone Akvan ·
Voyager 1 at one light-day · Hakeem Jeffries and the Speaker's gavel —
plus thirty more in the "Also on Thursday" column.

## Left out on purpose

The date-check box names them: the Qeshm strike and the measles
ruling (both Tuesday 17 November), the Crimea Bridge span collapse
(Wednesday 18 November), Ebola's 11,000-case milestone (figures dated
15 November), the Siberia plane crash (17–18 November) and
Medtronic's Contego acquisition (Monday 16 November). Yesterday's
news, however big, is not Thursday's.

## Running it

```sh
python3 main.py
```

That copies `entry.png` into `$MAKEFUN_OUTPUT_DIR` (or `/output`
when the variable is not set). The file never changes between runs:
one PNG, 1024 × 1024 pixels, below the 1 MiB limit.

## How the page was made

Every story was checked against wire and newspaper reporting dated
19 November 2026 before it earned a place on the page, and the map's
dots sit on the places those stories happened. The page is drawn
programmatically — type, rules, region colours and the dotted world
map are all laid out in code, with no photographs and no stock art.
