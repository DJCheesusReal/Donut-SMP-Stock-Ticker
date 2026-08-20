# Donut SMP Stock Ticker

> a little ESP32 desk display thing for showing Donut SMP info

<p align="center">
  <img src="https://img.shields.io/badge/status-early%20dev-orange?style=flat-square" alt="Project status: early development" />
  <img src="https://img.shields.io/badge/hardware-ESP32--S3-00979D?style=flat-square&logo=espressif&logoColor=white" alt="ESP32-S3" />
  <img src="https://img.shields.io/badge/PlatformIO-used-F5822A?style=flat-square&logo=platformio&logoColor=white" alt="Built with PlatformIO" />
  <img src="https://img.shields.io/badge/Donut%20SMP-unofficial-8B5CF6?style=flat-square" alt="Unofficial Donut SMP project" />
  <img src="https://img.shields.io/badge/licence-PolyForm%20Noncommercial-blueviolet?style=flat-square" alt="PolyForm Noncommercial License 1.0.0" />
</p>

**this is just a fan project and is not affiliated with or endorsed by Donut SMP.**

## what is this

basically i got annoyed having to keep checking the auction house when i was trying to flip items. i also like esp32s, desk accessories, and littyc tech so i thought it would be sick to make a thing that just sits on my desk and shows all the stuff i care about.

it is called a stock ticker because it's inspired by the nasdaq ones and can show item prices/graphs, but it is not *just* that. the idea is that it has a bunch of little pages and it cycles through them like a carousel.

right now the focus is only Donut SMP. maybe in the future it could work with other servers too but i am not even close to worrying about that yet.

## pages i wanna make

| page | what it would show |
| --- | --- |
| **item stock ticker** | current price, price change, and a little 24-hour graph for one item |
| **balance leaderboard** | baltop, probably the top 3 players |
| **player stats** | a player’s balance, kills, shards, deaths, playtime |
| **other leaderboards** | shard leaderboards and whatever other stats would be cool |

instead of one massive watchlist page, the plan is just to have loads of separate item pages. you pick the ones you care about and put them in the carousel.

later on i wanna have a local setup website hosted by the ESP32 so you can set all this up over Wi-Fi, then the device just saves it and runs by itself. if that turns out to be too much for the ESP32 then there might be some USB-to-PC setup thing instead, idk yet.

## future / bigger idea

donut smp is still the main thing rn and i wanna actually finish that properly first. but if this turns out tuff, i do not want it to just be a Donut-only thing forever. the bigger idea is basically a desk ticker for whatever live game/internet stuff you care about.

| future pack / thing | what it could show |
| --- | --- |
| **MCSR Ranked** | your player head, current rank + ELO, last match change, and a little 30-match ELO graph |
| **Twitch** | people you follow who are live, |
| **Spotify now playing** | the current song, artist, little album icon, playback progress bar, and maybe time left |
| **other Minecraft servers** | their own item prices, player stats, leaderboards, or whatever their API makes possible |
| **other game / internet stuff** | other live things that would be cool to have on a desk screen |

so the eventual setup website could have a little **page packs** bit where you install stuff like `Donut SMP`, `MCSR Ranked`, `Twitch`, or `Spotify`, choose the pages you want, then add them to your carousel. the layouts, text, graphs, and animations would be drawn by the actual firmware; packs are mainly settings + data for page types the device already knows how to draw. if a pack needs actual new code then it would need a normal firmware update.

### stuff i wanna get to eventually

- [ ] finish the actual Donut SMP ticker and make it work on real hardware first

- [ ] make the page engine/carousel so it can render loads of different kinds of pages

- [ ] make the local Wi-Fi setup website

- [ ] add a proper page-pack system in the setup site

- [ ] make an MCSR Ranked pack with player rank, ELO, and recent-match graph pages

- [ ] make a Twitch pack that shows people you follow who are live

- [ ] make a Spotify now-playing page because that would be tuff on a desk display

- [ ] see what other Minecraft servers / game / live internet APIs would be sick to support

- [ ] make the finished thing good enough that people can just buy a prebuilt one if they do not wanna wire anything

## what actually works rn

this is still early asf. i have not even got the physical hardware yet, i am waiting for Stardance funding so i can buy it. so the cool screen stuff is still a design/plan and not something i am saying is finished.

| thing | status |
| --- | --- |
| made the page designs | ✅ done |
| ESP32 connects to Wi-Fi | ✅ works |
| ESP32 gets one item price from the auction API | ✅ works |
| JSON parsing + printing the price to Serial | ✅ works |
| Python item search thing | ✅ works |
| Python price-history graph | ✅ works |
| K/M/B number formatting | 🛠️ kinda works, needs fixing |
| got an ESP32, panel, and adapter | ⏳ nope not yet |
| actually rendering the UI on the LED panel | ⏳ not yet |
| carousel system | 💭 planned |
| Wi-Fi setup portal | 💭 planned |

## hardware plan

the current plan is a **128×64 HUB75 LED matrix**, an **ESP32-S3 DevKitC-1**, and an ESP32 HUB75 adapter. the panel will have its own power because it is gonna need it.

my current parts research is in [Bill Of Materials.md](./Bill%20Of%20Materials.md). it is not a proper shopping list/build guide yet, it is just what i am looking at. when i actually have the parts and know it works i will make a real one with wiring and everything.

also want to make a 3D-printed desk stand and maybe a wall-mount version later.

## whats in this repo

| file/folder | what it is |
| --- | --- |
| `Donut SMP Stock Ticker ESP32 Project/` | the PlatformIO C++ test firmware. it connects to Wi-Fi, asks for one item price, then prints it to Serial. |
| `api_items.py` | my Python thing for searching items, checking prices, and making price graphs. |
| `donut_items.csv` | a list of Minecraft items, IDs, and stack sizes that i put together from Minecraft Wiki data. |
| `ideas.md` | random thoughts about pages, APIs, hardware and stuff. |
| `Bill Of Materials.md` | current parts research. |

im using **PlatformIO** and **ArduinoJson** for the ESP32 test code. the ESP32 project expects a `secrets.h` file with Wi-Fi stuff in it, which is ignored by Git. obviously do not commit your Wi-Fi password.

> there are no full build instructions yet. i will put them here once i have the real hardware and it actually works instead of making people buy stuff based on a project that is still half in my head.

## todo

- [x] make the page designs

- [x] look at the auction, leaderboard, and stats APIs

- [x] make Python tests for item searching, prices, and graphs

- [x] make the ESP32 get and parse a single auction price

- [ ] get the ESP32, HUB75 adapter, panel, and power supply

- [ ] get text/graphics on the actual LED matrix

- [ ] fix the K/M/B number thing because Donut SMP numbers get dumbly massive

- [ ] turn the item-price test into actual ticker pages with graphs

- [ ] add baltop, player stats, shards, and more leaderboards

- [ ] make the page carousel

- [ ] make a Wi-Fi setup/config portal and save settings on the device

- [ ] make a 3D-printed desk stand and wall mount

- [ ] write a proper parts list, wiring diagram, and build guide

## devlog

im putting my progress and random experiments on my [Stardance devlog](https://stardance.hackclub.com/projects/46566) if you wanna see what im doing with it.

## feedback

im not really looking for contributors rn but if you play Donut SMP and have a page idea, find a bug, or think something would be sick, open a [GitHub Issue](https://github.com/DJCheesusReal/Donut-SMP-Stock-Ticker/issues). no promises but i do wanna know what people would actually want to see on it.

## licence

the code in this repo is licensed under the [PolyForm Noncommercial License 1.0.0](./LICENSE).

you can use, build, modify, and share this project for personal, non-commercial use. **do not sell kits, prebuilts, copies, or commercial versions without asking first.**

if you want to sell one or work out a commercial licence, open an issue first.

## credits

- made by [@DJCheesusReal](https://github.com/DJCheesusReal)

- currently using the Donut Auction API for price tests

- item names and IDs in `donut_items.csv` came from Minecraft Wiki data

---

if you are a Donut SMP player and you would put this on your desk then yea that is exactly why im making it
