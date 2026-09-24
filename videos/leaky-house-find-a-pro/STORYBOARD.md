---
format: 1440x1080
duration: 60s
message: "在美国请师傅，靠的是口碑和信任，不是最低价"
arc: story-explainer with how-to
audience: 关注美国家居服务 / 出海 Home Service 赛道的中文读者
mode: autonomous
music: none
language: zh
---

## Video direction

**Canvas.** 1440×1080 (4:3). Every frame ground sets `container-type: size`; size everything in `cqw`/`cqh`. Full-bleed grounds ride on their own `class="clip"` background layer, never on `#root`.

**Cast (shared, never redraw).** The characters are pre-drawn SVGs in `public/characters/` — always place them with `<img src="../../public/characters/<file>.svg">` (path relative to `compositions/frames/`), never re-author them:
- `housy-neutral.svg` / `housy-sleep.svg` / `housy-worried.svg` / `housy-confused.svg` / `housy-happy.svg` — **小房子 Housy**, the protagonist (peach body, coral roof, butter chimney). viewBox 300×340. An expression change = stack two `<img>` of the same size at the same spot and hard-swap opacity (`tl.set`), with a tiny squash (scaleY 0.94 → 1) on the swap.
- `neighbor.svg` — the neighbor house (mint body, lavender arched roof, daisy). viewBox 300×340.
- `pro.svg` — the roofer pro (butter cap, sky overalls, coral toolbox, check-mark badge). viewBox 300×360.
Housy's standard size is ~26cqw wide unless a Scene says otherwise; keep his feet on an implied ground line. Props (bucket, drops, tools, phone, receipt, ladder, sun, stars) are drawn inline as SVG in the same style: 3px-equivalent charcoal `#2D2D2D` outlines (use stroke-width ≈ 0.42cqw-equivalent in SVG units), flat pastel fills, rounded joins.

**Palette.** From `frame.md` only: cream ground for data-dense frames; one saturated pastel ground per step frame, rotating butter → mint → sky → lavender → turquoise; white cards with 3px charcoal border + hard 6px offset shadow (no blur); coral only for small markers (step circles, drops of emphasis, the check mark ring). No gradients, no glow, no blur shadows.

**Type.** Chinese display and all Chinese text: `"ZCOOL KuaiLe"` (fallback `"Fredoka One", "Fredoka"`). Latin display + numerals: `"Fredoka"` weight 600 (stack `"Fredoka One", "Fredoka"`). Latin body/meta: `"Quicksand"` 600. Load Fredoka, Quicksand and ZCOOL KuaiLe from Google Fonts via a `<link>` in each frame. Numbers use `font-variant-numeric: tabular-nums`. Floor 1.4cqw for anything load-bearing.

**Shared step chrome (frames 3–7).** Top-left butter **badge-pill** at ~(3cqw, 3cqh): a coral circle-marker with the white step numeral + Fredoka/ZCOOL label, e.g. `STEP 1 · 自己修？`. Same position, same size in every step frame — the consistent stage. The step frame layout is: Housy in the left ~40%, the one white data card in the right ~55%, ornaments at corners.

**Subtitle band (every frame, fixed component — identical in all nine).** No voiceover exists; the bilingual subtitle IS the narration. Bottom band: a white pill centered horizontally, its top edge at 85cqh, max-width 86cqw, padding ~1.4cqw 3cqw, 3px charcoal border, 4px hard offset shadow, radius 50px. Line 1 Chinese in ZCOOL KuaiLe, 3.3cqw, `#2D2D2D`. Line 2 English in Quicksand 600, 1.75cqw, `#6B6B6B`. It enters at +0.25s with a short rise (y 1.2cqh → 0, opacity 0 → 1, power3.out, 0.35s) and then stays. When a frame lists two subtitle lines, the second replaces the first by hard swap at the stated time. All other content plans into the top ~83%.

**Ornaments.** 3–5 hand-drawn SVG ornaments per frame (daisy, star, cloud, sun, sparkle) at corners, cropping past the edge, behind content — per `frame.md`. Fewer (2–3) on the data-dense frames.

**Motion grammar.** One paused GSAP timeline per frame. Entrances are `fromTo`, smooth long-tail `power3.out`; this is a playful cartoon, so character and sticker pops may use a gentle `back.out(1.4)` — the only sanctioned overshoot, never on text or cards. Reveal each piece on its subtitle cue; never front-load. During holds, only a subtle low-amplitude jitter on Housy (≤0.4cqw, finite) or live SVG internals (drips, ringing lines). No breathing loops, no slow back-half pans, no `repeat:-1`, no `Math.random`.

**Rhythm.** Frame 1 is fast and comic; frame 2 is the one number-heavy stakes beat; frames 3–7 are the five-step run, one push-slide LEFT between each so they read as one journey; frame 8 is the calm breather (held, sunrise); frame 9 lands the thesis and holds to the end with the only real exit (a short fade of the whole frame in the last 0.4s).

**Negative list.** No stock photo look, no purple-blue AI gradients, no bokeh, no square corners, no blurred shadows, no fake browser/app chrome, no invented numbers (every figure below traces to HIRI and to `capture/extracted/visible-text.txt`), no slideshow (front-load then freeze), no screensaver (everything floating).

**Audio.** `music: none` here because HeyGen is signed out and local MusicGen is missing; the orchestrator synthesizes BGM + SFX procedurally and mounts them at the root after assembly. Workers never add `<audio>`. The `sfx:` lines below are the cue sheet for that synthesis.

## Frame 1 — 滴、滴、滴

- scene: night; Housy asleep; three drops fall from the ceiling onto his roof; he wakes up worried
- voiceover: ""
- subtitle: "半夜，屋顶开始漏水…… / Midnight. The roof starts to leak…"
- duration: 5s
- poster: 4s
- transition_in: cut
- status: animated
- src: compositions/frames/01-hook-leak.html
- type: hook
- persuasion: Imagine / scenario + visceral onomatopoeia
- beat: curiosity + comic tension
- blueprint: compose
- focal: Housy waking up under the drops
- roles: lavender night ground with butter moon + 3 stars = background · Housy = foreground subject · drops + "滴!" labels = supporting · "Zzz" = supporting
- sfx: drip at 1.3s, 2.0s, 2.7s; boing-gasp at 3.1s

narrativeRole: Opens the curiosity gap with a relatable household emergency before any data appears.
keyMessage: A leak just happened — what does an American homeowner do next?

Scene 1 (0.0–1.2s): lavender ground, butter crescent moon upper-right, three small stars; Housy (housy-sleep) centered at y≈45%, ~30cqw wide; three Fredoka "Z" letters drift up from his chimney one after another (finite, index-staggered). Centered, layered depth (sky / moon / Housy).
Scene 2 (1.2–3.0s): a teardrop (sky fill, charcoal outline) falls from the top edge and splats on Housy's roof at 1.3s, a second at 2.0s, a third at 2.7s; each splat pops a coral Chinese "滴!" sticker label beside the roof, scale-pop then settle, the three labels landing at slightly different angles (index-derived). The Z letters fade on the first splat.
Scene 3 (3.0–5.0s): hard swap housy-sleep → housy-worried at 3.1s with a squash; a white butter-bordered badge-pill "漏水了！ LEAK!" springs in above his roof at 3.3s; hold with subtle jitter on Housy (he's trembling). Subtitle is up from 0.25s.

## Frame 2 — 最烧钱的保养

- scene: Housy holds a bucket under the drip; a card counts up the yearly roof & gutter spend
- voiceover: ""
- subtitle: "屋顶和天沟，是美国家庭最烧钱的保养。 / Roofs & gutters: the priciest upkeep in a US home."
- duration: 6s
- poster: 5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-stakes-cost.html
- type: social_proof
- persuasion: Statistical proof + anchoring on a familiar referent (the bucket)
- beat: concern + surprise
- blueprint: dataviz-countup (Adapt)
- focal: the count-up "$1,390"
- roles: cream ground = background · Housy (worried) holding an inline-drawn sky bucket, drops still falling into it = foreground left · framed-header card = foreground right (hero) · 2 ornaments = supporting
- sfx: drip at 0.4s and 1.1s; coin-ding at 3.6s

narrativeRole: Grounds the stakes in money — a roof leak is the most expensive kind of home upkeep in HIRI's data.
keyMessage: Roof & gutter upkeep averages about $1,390 a year, and ~$1,200 of it goes to the contractor.

Adapt: keep the count-up hero-number signature; no camera push-through — the number lives inside one framed-header card beside the character.
Scene 1 (0.0–1.5s): cream ground; Housy (housy-worried) in the left 40%, holding a sky bucket under his roof edge; two drops fall into the bucket (0.4s, 1.1s) with a tiny splash. Asymmetric 40/60.
Scene 2 (1.5–3.6s): a white framed-header card slides in from the right (power3.out): coral cap strip reading "屋顶 + 天沟 Roof & Gutter", white body. Inside, the Fredoka hero number counts up from $0 to "$1,390" with a small "/ 年 per year" label, value-scaled counter (`counting-dynamic-scale`), landing at 3.6s.
Scene 3 (3.6–6.0s): at 3.8s a Quicksand/ZCOOL line reveals under the number: "美国家庭年均保养花费最高的一项"; at 4.6s a mint chip reveals: "其中约 $1,200 付给承包商 · ~$1,200 to the pro". A tiny meta source line "HIRI Home Services Study 2024" sits at the card's bottom edge from 4.6s. Hold.

## Frame 3 — STEP 1 · 自己修？

- scene: Housy tries to fix it himself with a toolbox; tools tumble; he's confused; two reason chips reveal
- voiceover: ""
- subtitle: "自己修？不会，也没工具。 / DIY? No skills, no tools."
- duration: 7s
- poster: 6.5s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-step1-diy.html
- type: feature_showcase
- persuasion: Signposting (step 1 of 5) + causal chain (can't → hire)
- beat: recognition + comic failure
- blueprint: compose
- focal: the tumbling toolbox and the two reason chips
- roles: butter ground = background · step badge = chrome · Housy = foreground left · inline coral toolbox + wrench + hammer = supporting · white card with 2 rows = foreground right
- sfx: whoosh at 0.3s; clatter at 2.3s; boing at 3.0s; pop at 4.4s and 5.6s

narrativeRole: First step of the journey — explains WHY Americans hire a pro at all.
keyMessage: HIRI's top two reasons to hire a licensed pro are lack of skills and lack of tools.

Scene 1 (0.0–1.6s): butter ground; the shared step badge "STEP 1 · 自己修？" slides in top-left (0.2s); Housy (housy-neutral) enters from the left and stops in the left 40%, a coral toolbox drops beside his feet.
Scene 2 (1.6–3.6s): a wrench and hammer pop out of the toolbox, spin in the air above Housy, and clatter down at 2.3s (deterministic arcs); hard swap to housy-confused at 3.0s with squash; a small "?" sticker pops above his roof.
Scene 3 (3.6–7.0s): a white card fades up in the right 55% with a ZCOOL title "请人的前两大原因"; row ① "缺技能 No skills" pops in at 4.4s with a coral circle-marker "1"; row ② "缺工具 No tools" at 5.6s with a mint marker "2"; meta "HIRI 2024" at the card foot. Hold with subtle Housy jitter.

## Frame 4 — STEP 2 · 问邻居

- scene: the neighbor house pops up over a fence with a speech bubble; a bar chart shows referrals ≈ 2× online search
- voiceover: ""
- subtitle: "先问邻居——熟人推荐是网上搜索的 2 倍。 / Ask the neighbors — referrals beat search 2 to 1."
- duration: 7s
- poster: 6.5s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/04-step2-neighbor.html
- type: feature_showcase
- persuasion: Comparison of two options + statistical proof
- beat: delight + "aha"
- blueprint: compose
- focal: the 2× bar comparison
- roles: mint ground = background · step badge = chrome · Housy (neutral) left + neighbor peeking from behind a white picket fence = foreground left · speech bubble = supporting · white card with 2 horizontal bars = foreground right
- sfx: pop at 1.6s; whoosh at 3.3s; ding at 4.8s; pop at 5.8s

narrativeRole: Second step — how Americans find a pro: people, not search engines.
keyMessage: Personal referrals are about twice as likely as online search to be how a homeowner finds a pro; social media helps only 16%.

Scene 1 (0.0–1.4s): mint ground; step badge "STEP 2 · 问邻居" (0.2s); Housy (housy-neutral) stands left-of-center; a white picket fence (inline SVG) along the lower-left third.
Scene 2 (1.4–3.2s): the neighbor house (neighbor.svg, ~22cqw) pops up from behind the fence at 1.6s (gentle back.out); a white speech bubble with charcoal outline springs from the neighbor at 2.0s: "我认识个靠谱师傅！" and below in Quicksand "I know a guy!".
Scene 3 (3.2–7.0s): white card in the right 55% titled "怎么找到师傅"; bar 1 "熟人推荐 Referral" (coral) grows to full length at 3.3–4.3s; bar 2 "网上搜索 Search" (sky) grows to half length at 3.8–4.6s; a butter sticker "×2" stamps at the end of bar 1 at 4.8s; at 5.8s a small lavender chip "社交媒体只对 16% 有用 · social media: 16%". Meta "HIRI 2024". Hold.

## Frame 5 — STEP 3 · 打电话

- scene: a big retro phone rings; Housy picks up; a ring fills to about two-thirds; web / text / app chips get crossed out
- voiceover: ""
- subtitle: "约师傅，美国人还是爱打电话。 / Most still book by phone — not an app."
- duration: 6s
- poster: 5.5s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-step3-phone.html
- type: feature_showcase
- persuasion: Counterintuitive claim (digital age, yet phone wins) + statistical proof
- beat: surprise + recognition
- blueprint: dataviz-countup (Adapt)
- focal: the 2/3 progress ring
- roles: sky ground = background · step badge = chrome · Housy + coral rotary phone (inline SVG) = foreground left · white card with ring + chips = foreground right
- sfx: phone ring at 0.4s–1.6s; pickup click at 1.7s; tick during ring fill 2.0–3.4s; scribble at 4.0s, 4.5s, 5.0s

narrativeRole: Third step — how the booking actually happens.
keyMessage: Nearly two-thirds of homeowners prefer to book by phone or in person, not via website, text, or app.

Adapt: keep the count-up ring signature (`stat-bars-and-fills` ring + a "≈ 2/3" readout); no camera push.
Scene 1 (0.0–1.7s): sky ground; step badge "STEP 3 · 打电话"; a coral retro phone sits beside Housy (housy-worried) and shakes with ringing lines (live SVG internals, finite) 0.4–1.6s; at 1.7s the handset lifts to Housy's side and he hard-swaps to housy-neutral.
Scene 2 (1.7–3.6s): white card in the right 55%: a coral progress ring draws from 12 o'clock to 66% (2.0–3.4s) while the center readout ticks to "≈ 2/3"; ZCOOL caption under the ring "更愿意电话或当面预约".
Scene 3 (3.6–6.0s): a row of three pastel chips "网站 Web" · "短信 Text" · "App" reveals under the ring, then each gets a hand-drawn charcoal strike-through (`css-marker-patterns` sketch) at 4.0 / 4.5 / 5.0s. Meta "HIRI 2024". Hold.

## Frame 6 — STEP 4 · 看报价

- scene: a long receipt unrolls full of question marks; Housy is confused; a stamp says over a quarter find pricing unclear
- voiceover: ""
- subtitle: "报价单一长串，根本看不懂。 / The quote? Long and totally unclear."
- duration: 7s
- poster: 6.5s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/06-step4-quote.html
- type: pain_point
- persuasion: Concretization (opaque pricing → a receipt of question marks) + statistical proof
- beat: puzzlement + unease
- blueprint: compose
- focal: the unrolling receipt and the "1/4+" stamp
- roles: lavender ground = background · step badge = chrome · Housy (confused) = foreground left · white receipt with zigzag edge = foreground center-right (hero) · coral stamp = supporting
- sfx: paper-unroll 1.4–3.4s; pop at 2.2s, 2.6s, 3.0s; boing at 3.9s; stamp thud at 5.4s

narrativeRole: Fourth step — the friction point: price transparency.
keyMessage: More than a quarter of homeowners found service pricing hard to understand in the past year.

Scene 1 (0.0–1.4s): lavender ground; step badge "STEP 4 · 看报价"; Housy (housy-neutral) left 35%, looking right.
Scene 2 (1.4–3.8s): a tall white receipt (zigzag bottom edge, charcoal outline, hard shadow) unrolls downward in the right 55% (mask-reveal from the top, transform-only); lines print as it unrolls: "人工 Labor …… $ ???", "材料 Materials …… $ ???", "上门费 Trip fee …… $ ???", "其他 Misc …… $ ???"; three coral "?" stickers pop around it at 2.2 / 2.6 / 3.0s.
Scene 3 (3.8–7.0s): hard swap to housy-confused at 3.9s with squash; at 5.4s a round coral-outlined stamp slams onto the receipt, slightly rotated: big Fredoka "1/4+" and ZCOOL "觉得价格不透明"; meta "HIRI 2024" under the receipt. Hold with subtle jitter on Housy.

## Frame 7 — STEP 5 · 挑师傅

- scene: three pro cards deal in; Housy picks the well-reviewed licensed one, not the cheapest; a ranking strip puts price last
- voiceover: ""
- subtitle: "最后挑的是口碑，不是最低价。 / They pick reputation — not the lowest price."
- duration: 8s
- poster: 7.5s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-step5-choose.html
- type: feature_showcase
- persuasion: Common-belief vs reality (cheapest wins? no) + rule of three
- beat: conviction + "aha"
- blueprint: grid-card-assemble (Adapt)
- focal: the chosen middle card with the pro
- roles: turquoise ground = background · step badge = chrome · three white pro cards (triptych) = foreground · pro.svg on the middle card = foreground subject · ranking strip = supporting · small Housy (happy) bottom-left pointing = supporting
- sfx: card whoosh at 1.4s, 1.7s, 2.0s; ding at 3.6s; pop at 5.2s, 5.8s, 6.4s, 7.0s

narrativeRole: Fifth step — the decision rule, and the video's key insight.
keyMessage: Work quality, reputation, and being licensed & insured all beat price; ~96% say work quality matters.

Adapt: keep the staggered self-assembling card cascade signature; three cards only, then one gets chosen, then a one-line ranking strip accumulates beneath.
Scene 1 (0.0–1.3s): turquoise ground; step badge "STEP 5 · 挑师傅"; small Housy (housy-neutral, ~16cqw) at lower-left, looking at the cards.
Scene 2 (1.3–3.4s): three white cards deal in left→right (1.4 / 1.7 / 2.0s), triptych across the upper-middle: card A "最便宜 Cheapest" with a big "$" and empty grey stars; card B (middle) "口碑好 Top reviews" with five butter stars and a mint badge "持证 + 保险 Licensed & insured"; card C "没评价 No reviews" with "?".
Scene 3 (3.4–5.0s): card B lifts and scales up slightly, gets a coral check-mark circle at 3.6s; pro.svg pops up from behind card B; cards A and C dim to ~45% opacity; Housy hard-swaps to housy-happy and points.
Scene 4 (5.0–8.0s): a white ranking strip along the lower band above the subtitle builds item by item: "施工质量 Quality 96%" (5.2s) › "口碑 Reputation" (5.8s) › "持证保险 Licensed" (6.4s) › then, set apart and smaller in grey, "价格 Price" (7.0s) with a small "排在后面 comes later" tag. Meta "HIRI 2024" at the strip end. Hold.

## Frame 8 — 修好啦

- scene: sunrise; the pro patches the roof; drops stop; Housy beams
- voiceover: ""
- subtitle: "天亮了，屋顶也修好了。 / Morning. Roof fixed."
- duration: 6s
- poster: 5.5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-fixed-sunrise.html
- type: benefit_highlight
- persuasion: Callback (frame 1's leak resolved) + before/after
- beat: relief + delight
- blueprint: compose
- focal: Housy (happy) with the patched roof
- roles: sky ground with a rising butter sun = background · Housy large center = foreground subject · pro standing on/next to the roof with a hammer = foreground supporting · a butter roof patch sticker = supporting · sparkles = supporting
- sfx: hammer tap at 1.2s, 1.6s, 2.0s; sparkle at 3.4s; soft chime at 4.2s

narrativeRole: The breather and payoff of the story — the right pro solves it.
keyMessage: Pick the trusted pro, and the problem gets solved.

Scene 1 (0.0–2.2s): sky ground; a butter sun rises from behind the lower horizon (a pale mint ground strip), slow and smooth; Housy (housy-worried) center, ~34cqw; pro.svg (~20cqw) stands on a small ladder to Housy's right, hammer arm; three hammer taps at 1.2 / 1.6 / 2.0s each emit a tiny star burst at the roof.
Scene 2 (2.2–4.0s): a butter patch sticker (rounded rectangle with two stitch lines) appears on Housy's roof at 2.3s; at 3.4s hard swap to housy-happy with squash; 4–5 sparkles pop around him (index-staggered).
Scene 3 (4.0–6.0s): a butter badge-pill "修好啦！ Fixed!" springs in above; hold still (the held breather). Subtitle as specified.

## Frame 9 — 靠的是信任

- scene: a recap row of the five steps builds; the thesis headline lands; the cast waves; source line
- voiceover: ""
- subtitle: "记住：口碑 > 低价。 / Remember: trust beats cheap."
- duration: 8s
- poster: 7s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-thesis-trust.html
- type: branding
- persuasion: Distillation + recap (numbered enumeration → one line)
- beat: clarity + satisfaction
- blueprint: kinetic-type-beats (Adapt)
- focal: the headline "在美国请师傅，靠的是信任。"
- roles: soft-pink ground = background · 5 circle-marker recap icons + arrows = supporting (upper band) · Fredoka/ZCOOL display headline white with charcoal text-shadow = foreground hero · Housy (happy), neighbor, pro small along the bottom above the subtitle = supporting · source chip = chrome · ornament wreath (5) = supporting
- sfx: pop at 0.4s, 0.8s, 1.2s, 1.6s, 2.0s; whoosh-slam at 3.0s; soft chime at 5.6s

narrativeRole: Lands the thesis and generalizes the five steps into one principle.
keyMessage: In the US, home service runs on trust — referrals, phone calls, and reputation beat the lowest bid.

Adapt: keep the statement build onto a payoff (beat-by-beat) signature; the "beats" are the five recap markers, the payoff is the headline.
Scene 1 (0.0–2.4s): soft-pink ground with an ornament wreath; five step circle-markers pop in left→right across the upper third (0.4 / 0.8 / 1.2 / 1.6 / 2.0s), each with a tiny inline icon and ZCOOL label: 缺技能 · 问邻居 · 打电话 · 看报价 · 挑口碑, linked by Fredoka "→" arrows. Full-width strip.
Scene 2 (2.4–5.4s): the headline slams in at 3.0s, centered at y≈45%: ZCOOL display, white with 3px charcoal text-shadow, two lines "在美国请师傅，" / "靠的是信任。"; at 3.8s the Latin line under it in Fredoka "In the US, home service runs on trust." (white, soft text-shadow).
Scene 3 (5.4–8.0s): Housy (housy-happy), the neighbor and the pro pop in small along the bottom above the subtitle band (5.4 / 5.6 / 5.8s); a white source chip "数据：HIRI Home Services Study 2024" at 5.8s; hold; the whole frame fades out over the last 0.4s (the video's only real exit).
