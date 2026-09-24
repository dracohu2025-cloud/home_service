// Cobalt line-art illustration kit shared by every frame (workers inline these SVGs).
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const C = "#1e2bfa";
const INK = "#111111";
const CREAM = "#fdfae7";
const RED = "#dc2626";
const GREEN = "#059669";
const out = join(dirname(fileURLToPath(import.meta.url)), "..", "public", "illustrations");
mkdirSync(out, { recursive: true });

const line = (w = 6) => `stroke="${C}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"`;
const tint = (o) => `fill="${C}" fill-opacity="${o}"`;
const svg = (vb, body) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}">${body}</svg>\n`;
const write = (name, s) => writeFileSync(join(out, name), s);

// ── house cross-section ────────────────────────────────────────────────────────
write(
  "house-cutaway.svg",
  svg(
    "0 0 800 640",
    `
  <g id="soil">
    <rect x="0" y="470" width="800" height="170" ${tint(0.06)}/>
    ${Array.from({ length: 16 }, (_, i) => `<path d="M${20 + i * 50} 612 l18 -18" ${line(3)} opacity="0.25"/>`).join("")}
    <path d="M0 470 H800" ${line(5)}/>
  </g>
  <g id="shell">
    <path d="M90 204 L400 44 L710 204" fill="none" ${line(8)}/>
    <rect x="120" y="200" width="560" height="270" fill="${CREAM}" ${line(7)}/>
    <rect x="120" y="470" width="560" height="130" rx="4" ${tint(0.05)} ${line(6)}/>
    <path d="M120 332 H680" ${line(5)}/>
    <path d="M420 200 V332 M470 332 V470" ${line(4)} opacity="0.35"/>
    <rect x="610" y="100" width="36" height="78" rx="4" fill="${CREAM}" ${line(6)}/>
  </g>
  <g id="windows" opacity="0.55">
    <rect x="170" y="236" width="80" height="60" rx="6" fill="none" ${line(4)}/>
    <path d="M210 236 V296 M170 266 H250" ${line(3)}/>
    <rect x="510" y="236" width="80" height="60" rx="6" fill="none" ${line(4)}/>
    <path d="M550 236 V296 M510 266 H590" ${line(3)}/>
    <rect x="170" y="368" width="80" height="60" rx="6" fill="none" ${line(4)}/>
    <path d="M210 368 V428 M170 398 H250" ${line(3)}/>
  </g>
  <g id="room-labels" font-family="Space Grotesk, sans-serif" font-weight="600" font-size="15" letter-spacing="1.5" fill="${C}" opacity="0.7">
    <text x="300" y="224">BATHROOM</text>
    <text x="500" y="356">KITCHEN</text>
    <text x="140" y="494">BASEMENT</text>
  </g>
  <g id="fixtures">
    <g id="fx-tub"><path d="M300 300 h96 v14 a18 18 0 0 1 -18 18 h-60 a18 18 0 0 1 -18 -18 z" ${tint(0.12)} ${line(5)}/></g>
    <g id="fx-sink"><path d="M540 420 h90 v12 a14 14 0 0 1 -14 14 h-62 a14 14 0 0 1 -14 -14 z" ${tint(0.12)} ${line(5)}/>
      <path d="M585 420 v-26 h18" fill="none" ${line(5)}/></g>
    <g id="fx-heater"><rect x="560" y="492" width="64" height="98" rx="14" ${tint(0.1)} ${line(5)}/>
      <circle cx="592" cy="520" r="10" fill="none" ${line(4)}/></g>
    <g id="fx-breaker"><rect x="138" y="360" width="0" height="0"/></g>
  </g>
  <g id="breaker-panel">
    <rect x="620" y="360" width="44" height="64" rx="6" fill="${CREAM}" ${line(5)}/>
    <path d="M632 376 h20 M632 390 h20 M632 404 h20" ${line(4)}/>
  </g>
  <g id="pipes" fill="none">
    <path id="pipe-main" d="M0 566 H250" ${line(9)}/>
    <path id="pipe-riser" d="M250 566 V316" ${line(7)}/>
    <path id="pipe-upper" d="M250 316 H350" ${line(7)}/>
    <path id="pipe-kitchen" d="M250 446 H585 V420" ${line(6)}/>
    <path id="pipe-heater" d="M250 540 H560" ${line(6)}/>
  </g>
  <g id="meter"><rect x="96" y="548" width="44" height="36" rx="8" fill="${CREAM}" ${line(5)}/>
    <circle cx="118" cy="566" r="8" fill="none" ${line(3)}/></g>
  <g id="valve-main">
    <circle cx="196" cy="566" r="16" fill="${CREAM}" ${line(6)}/>
    <path d="M196 550 V528" ${line(6)}/>
    <g id="valve-main-wheel"><circle cx="196" cy="522" r="18" fill="${CREAM}" ${line(6)}/>
      <path d="M178 522 H214 M196 504 V540" ${line(4)}/></g>
  </g>
  <g id="burst-point" transform="translate(338 316)">
    <path d="M-10 -14 L0 -2 L10 -14 M-12 12 L0 2 L12 12" fill="none" stroke="${RED}" stroke-width="5" stroke-linecap="round"/>
  </g>
  <g id="spray" transform="translate(338 316)" fill="${C}">
    <path d="M0 -8 C -26 -40 -40 -60 -44 -88" fill="none" ${line(5)} opacity="0.8"/>
    <path d="M0 -8 C 20 -44 34 -62 40 -92" fill="none" ${line(5)} opacity="0.8"/>
    <path d="M0 -8 C -4 -46 -2 -70 0 -100" fill="none" ${line(5)} opacity="0.8"/>
    <circle cx="-50" cy="-96" r="5"/><circle cx="46" cy="-100" r="5"/><circle cx="2" cy="-110" r="5"/>
  </g>
  <g id="puddle"><ellipse cx="338" cy="326" rx="70" ry="7" ${tint(0.25)}/></g>`,
  ),
);

// ── valves ─────────────────────────────────────────────────────────────────────
write(
  "valve-gate.svg",
  svg(
    "0 0 240 240",
    `
  <path d="M10 178 H230" ${line(20)} stroke-opacity="0.14"/>
  <path d="M10 170 H80 M160 170 H230 M10 186 H80 M160 186 H230" ${line(5)}/>
  <path d="M80 150 H160 L172 178 L160 206 H80 L68 178 Z" ${tint(0.1)} ${line(6)}/>
  <path d="M120 150 V92" ${line(7)}/>
  <g id="wheel">
    <circle cx="120" cy="70" r="52" fill="${CREAM}" ${line(7)}/>
    <circle cx="120" cy="70" r="10" fill="${C}"/>
    <path d="M120 22 V118 M72 70 H168 M86 36 L154 104 M154 36 L86 104" ${line(5)}/>
  </g>`,
  ),
);

write(
  "valve-ball.svg",
  svg(
    "0 0 240 240",
    `
  <path d="M10 150 H230" ${line(20)} stroke-opacity="0.14"/>
  <path d="M10 142 H84 M156 142 H230 M10 158 H84 M156 158 H230" ${line(5)}/>
  <rect x="84" y="118" width="72" height="64" rx="16" ${tint(0.1)} ${line(6)}/>
  <path d="M120 118 V98" ${line(7)}/>
  <g id="lever">
    <rect x="112" y="84" width="112" height="22" rx="11" fill="${C}"/>
    <circle cx="120" cy="95" r="14" fill="${CREAM}" ${line(6)}/>
  </g>`,
  ),
);

// ── icons ──────────────────────────────────────────────────────────────────────
write(
  "breaker-panel.svg",
  svg(
    "0 0 200 240",
    `
  <rect x="20" y="10" width="160" height="220" rx="18" fill="${CREAM}" ${line(6)}/>
  <rect x="40" y="30" width="120" height="180" rx="10" ${tint(0.06)} ${line(4)}/>
  ${[0, 1, 2, 3, 4]
    .map(
      (r) => `<rect x="52" y="${44 + r * 32}" width="40" height="20" rx="5" fill="${CREAM}" ${line(4)}/><rect x="56" y="${48 + r * 32}" width="14" height="12" rx="3" fill="${C}"/>
  <rect x="108" y="${44 + r * 32}" width="40" height="20" rx="5" fill="${CREAM}" ${line(4)}/><rect x="112" y="${48 + r * 32}" width="14" height="12" rx="3" fill="${C}"/>`,
    )
    .join("")}
  <g id="switch-target"><rect x="104" y="104" width="48" height="28" rx="7" fill="none" stroke="${RED}" stroke-width="4"/>
    <rect id="switch-toggle" x="112" y="112" width="14" height="12" rx="3" fill="${RED}"/></g>`,
  ),
);

write(
  "faucet.svg",
  svg(
    "0 0 240 240",
    `
  <path d="M30 214 H210" ${line(6)}/>
  <rect x="76" y="196" width="88" height="18" rx="9" ${tint(0.12)} ${line(6)}/>
  <path d="M120 196 V104 C120 44 196 44 196 104 V118" fill="none" ${line(12)}/>
  <g id="handle-hot"><path d="M100 150 H64" stroke="${RED}" stroke-width="12" stroke-linecap="round"/>
    <circle cx="104" cy="150" r="9" fill="${CREAM}" stroke="${RED}" stroke-width="6"/></g>
  <g id="handle-cold"><path d="M140 150 H176" ${line(12)}/>
    <circle cx="136" cy="150" r="9" fill="${CREAM}" ${line(6)}/></g>
  <path id="stream" d="M196 128 V192" ${line(8)} stroke-opacity="0.55" stroke-dasharray="10 12"/>`,
  ),
);

write(
  "toilet.svg",
  svg(
    "0 0 240 240",
    `
  <rect x="130" y="30" width="80" height="80" rx="12" ${tint(0.08)} ${line(6)}/>
  <path d="M150 50 h30" ${line(6)}/>
  <path d="M40 110 H210 a0 0 0 0 1 0 0 c0 40 -30 64 -80 64 h-30 c-40 0 -60 -30 -60 -64 z" fill="${CREAM}" ${line(6)}/>
  <path d="M100 174 l-8 40 h70 l-8 -40" fill="${CREAM}" ${line(6)}/>`,
  ),
);

write(
  "water-heater.svg",
  svg(
    "0 0 200 260",
    `
  <rect x="40" y="30" width="120" height="200" rx="30" ${tint(0.08)} ${line(6)}/>
  <path d="M80 30 V10 M120 30 V10" ${line(6)}/>
  <circle cx="100" cy="86" r="22" fill="${CREAM}" ${line(5)}/>
  <path id="dial-needle" d="M100 86 L112 72" ${line(5)}/>
  <rect x="70" y="170" width="60" height="34" rx="8" fill="${CREAM}" ${line(5)}/>
  <path id="flame" d="M100 198 c-10 -8 -8 -18 0 -24 c8 6 10 16 0 24 z" fill="${RED}"/>`,
  ),
);

write(
  "phone-camera.svg",
  svg(
    "0 0 200 260",
    `
  <rect x="40" y="10" width="120" height="240" rx="22" fill="${CREAM}" ${line(6)}/>
  <rect x="54" y="36" width="92" height="170" rx="10" ${tint(0.08)}/>
  <path d="M86 24 h28" ${line(5)}/>
  <circle cx="100" cy="228" r="10" fill="none" ${line(5)}/>
  <g id="viewfinder" ${line(4)} fill="none">
    <path d="M66 60 v-12 h12 M134 60 v-12 h-12 M66 182 v12 h12 M134 182 v12 h-12"/>
  </g>
  <circle cx="100" cy="121" r="26" fill="none" ${line(5)}/>
  <circle cx="100" cy="121" r="10" fill="${C}"/>`,
  ),
);

write(
  "wrench.svg",
  svg(
    "0 0 200 200",
    `
  <path d="M136 30 a38 38 0 0 0 -46 50 l-60 60 a14 14 0 0 0 20 20 l60 -60 a38 38 0 0 0 50 -46 l-22 22 l-20 -4 l-4 -20 z" ${tint(0.12)} ${line(6)}/>`,
  ),
);

write(
  "shield-check.svg",
  svg(
    "0 0 200 220",
    `
  <path d="M100 14 L170 40 V104 C170 150 140 184 100 204 C60 184 30 150 30 104 V40 Z" ${tint(0.1)} ${line(6)}/>
  <path id="check" d="M68 110 L92 134 L136 86" fill="none" stroke="${GREEN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>`,
  ),
);

write(
  "tape-no.svg",
  svg(
    "0 0 220 220",
    `
  <circle cx="100" cy="110" r="64" ${tint(0.1)} ${line(6)}/>
  <circle cx="100" cy="110" r="28" fill="${CREAM}" ${line(6)}/>
  <path d="M100 174 H196 V148" fill="none" ${line(6)}/>
  <circle cx="160" cy="54" r="34" fill="${CREAM}" stroke="${RED}" stroke-width="7"/>
  <path d="M146 40 L174 68 M174 40 L146 68" stroke="${RED}" stroke-width="7" stroke-linecap="round"/>`,
  ),
);

write(
  "valve-tag.svg",
  svg(
    "0 0 300 160",
    `
  <path d="M60 20 H270 a14 14 0 0 1 14 14 V126 a14 14 0 0 1 -14 14 H60 L16 80 Z" fill="${C}"/>
  <circle cx="52" cy="80" r="10" fill="${CREAM}"/>
  <text x="170" y="74" text-anchor="middle" font-family="Space Grotesk, sans-serif" font-weight="700" font-size="28" letter-spacing="2" fill="${CREAM}">MAIN</text>
  <text x="170" y="108" text-anchor="middle" font-family="Space Grotesk, sans-serif" font-weight="700" font-size="28" letter-spacing="2" fill="${CREAM}">SHUT-OFF</text>`,
  ),
);

write(
  "clock.svg",
  svg(
    "0 0 220 220",
    `
  <circle cx="110" cy="110" r="92" fill="${CREAM}" ${line(7)}/>
  ${Array.from({ length: 12 }, (_, i) => {
    const a = (i * Math.PI) / 6;
    const x1 = 110 + Math.sin(a) * 76, y1 = 110 - Math.cos(a) * 76;
    const x2 = 110 + Math.sin(a) * 84, y2 = 110 - Math.cos(a) * 84;
    return `<path d="M${x1.toFixed(1)} ${y1.toFixed(1)} L${x2.toFixed(1)} ${y2.toFixed(1)}" ${line(5)}/>`;
  }).join("")}
  <path id="hand-hour" d="M110 110 L152 86" ${line(9)}/>
  <path id="hand-minute" d="M110 110 L110 44" ${line(6)}/>
  <circle cx="110" cy="110" r="8" fill="${C}"/>`,
  ),
);

console.log("illustrations →", out);
