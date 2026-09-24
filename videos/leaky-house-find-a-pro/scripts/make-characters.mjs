import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const INK = "#2D2D2D";
const C = {
  peach: "#FFCBA4",
  coral: "#F8635F",
  butter: "#FDE68A",
  mint: "#A8E6CF",
  lavender: "#D4A5E8",
  sky: "#A8D8F0",
  pink: "#F7C8D4",
  turquoise: "#7ECDC0",
  white: "#FFFFFF",
};
const S = `stroke="${INK}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"`;

const outDir = join(dirname(fileURLToPath(import.meta.url)), "..", "public", "characters");
mkdirSync(outDir, { recursive: true });

const svg = (body, vb = "0 0 300 340") =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}" width="300" height="340">${body}</svg>\n`;

const legs = (fill) => `
  <rect x="96" y="292" width="20" height="30" rx="8" fill="${fill}" ${S}/>
  <rect x="184" y="292" width="20" height="30" rx="8" fill="${fill}" ${S}/>
  <ellipse cx="102" cy="326" rx="22" ry="9" fill="${INK}"/>
  <ellipse cx="198" cy="326" rx="22" ry="9" fill="${INK}"/>`;

const cheeks = `
  <ellipse cx="78" cy="238" rx="17" ry="9" fill="${C.pink}"/>
  <ellipse cx="222" cy="238" rx="17" ry="9" fill="${C.pink}"/>`;

const openEyes = (dx = 0, dy = 0) => `
  <ellipse cx="108" cy="198" rx="24" ry="28" fill="${C.white}" ${S}/>
  <ellipse cx="192" cy="198" rx="24" ry="28" fill="${C.white}" ${S}/>
  <circle cx="${108 + dx}" cy="${202 + dy}" r="12" fill="${INK}"/>
  <circle cx="${192 + dx}" cy="${202 + dy}" r="12" fill="${INK}"/>
  <circle cx="${112 + dx}" cy="${197 + dy}" r="4" fill="${C.white}"/>
  <circle cx="${196 + dx}" cy="${197 + dy}" r="4" fill="${C.white}"/>`;

function house({ bodyFill, roofFill, chimneyFill, face, roof = "tri", extra = "" }) {
  const roofPath =
    roof === "tri"
      ? `<path d="M22 146 L150 30 L278 146 Z" fill="${roofFill}" ${S}/>`
      : `<path d="M28 150 Q28 44 150 40 Q272 44 272 150 Z" fill="${roofFill}" ${S}/>`;
  return svg(`
  <rect x="200" y="52" width="34" height="70" rx="6" fill="${chimneyFill}" ${S}/>
  ${legs(bodyFill)}
  <rect x="44" y="128" width="212" height="172" rx="24" fill="${bodyFill}" ${S}/>
  ${roofPath}
  ${extra}
  ${face}`);
}

const housyBase = { bodyFill: C.peach, roofFill: C.coral, chimneyFill: C.butter };

const faces = {
  neutral: `${openEyes()}${cheeks}
  <path d="M128 244 Q150 262 172 244" fill="none" ${S}/>`,
  sleep: `
  <path d="M86 202 Q108 216 130 202" fill="none" ${S}/>
  <path d="M170 202 Q192 216 214 202" fill="none" ${S}/>${cheeks}
  <ellipse cx="150" cy="250" rx="9" ry="7" fill="${INK}"/>`,
  worried: `${openEyes(0, -6)}${cheeks}
  <path d="M84 160 L126 150" fill="none" ${S}/>
  <path d="M216 160 L174 150" fill="none" ${S}/>
  <path d="M122 254 q7 -10 14 0 t14 0 t14 0 t14 0" fill="none" ${S}/>
  <path d="M244 176 q10 14 0 22 q-10 -8 0 -22 Z" fill="${C.sky}" ${S}/>`,
  confused: `
  <ellipse cx="108" cy="198" rx="24" ry="28" fill="${C.white}" ${S}/>
  <ellipse cx="192" cy="198" rx="24" ry="28" fill="${C.white}" ${S}/>
  <path d="M108 200 m-12 0 a12 12 0 1 1 12 12 a7 7 0 1 1 -7 -7" fill="none" ${S}/>
  <path d="M192 200 m-12 0 a12 12 0 1 1 12 12 a7 7 0 1 1 -7 -7" fill="none" ${S}/>
  ${cheeks}
  <path d="M84 158 L128 162" fill="none" ${S}/>
  <path d="M172 150 L214 142" fill="none" ${S}/>
  <path d="M130 252 L172 244" fill="none" ${S}/>`,
  happy: `
  <path d="M86 206 Q108 180 130 206" fill="none" ${S}/>
  <path d="M170 206 Q192 180 214 206" fill="none" ${S}/>${cheeks}
  <path d="M118 234 Q150 234 182 234 Q178 276 150 276 Q122 276 118 234 Z" fill="${INK}" ${S}/>
  <path d="M132 262 Q150 250 168 262 Q162 274 150 274 Q138 274 132 262 Z" fill="${C.pink}"/>`,
};

for (const [name, face] of Object.entries(faces)) {
  writeFileSync(join(outDir, `housy-${name}.svg`), house({ ...housyBase, face }));
}

writeFileSync(
  join(outDir, "neighbor.svg"),
  house({
    bodyFill: C.mint,
    roofFill: C.lavender,
    chimneyFill: C.sky,
    roof: "arch",
    extra: `
  <circle cx="150" cy="88" r="14" fill="${C.butter}" ${S}/>
  <circle cx="150" cy="60" r="12" fill="${C.white}" ${S}/>
  <circle cx="176" cy="88" r="12" fill="${C.white}" ${S}/>
  <circle cx="124" cy="88" r="12" fill="${C.white}" ${S}/>
  <circle cx="150" cy="116" r="12" fill="${C.white}" ${S}/>
  <circle cx="150" cy="88" r="14" fill="${C.butter}" ${S}/>`,
    face: `
  <path d="M86 204 Q108 188 130 204" fill="none" ${S}/>
  <path d="M170 204 Q192 188 214 204" fill="none" ${S}/>${cheeks}
  <path d="M120 238 Q150 268 180 238" fill="none" ${S}/>`,
  }),
);

writeFileSync(
  join(outDir, "pro.svg"),
  svg(
    `
  <rect x="112" y="300" width="26" height="46" rx="10" fill="${C.sky}" ${S}/>
  <rect x="162" y="300" width="26" height="46" rx="10" fill="${C.sky}" ${S}/>
  <ellipse cx="122" cy="350" rx="24" ry="9" fill="${INK}"/>
  <ellipse cx="178" cy="350" rx="24" ry="9" fill="${INK}"/>
  <path d="M86 196 Q60 250 72 290" fill="none" stroke="${INK}" stroke-width="20" stroke-linecap="round"/>
  <path d="M86 196 Q60 250 72 290" fill="none" stroke="${C.peach}" stroke-width="10" stroke-linecap="round"/>
  <rect x="84" y="176" width="132" height="140" rx="30" fill="${C.sky}" ${S}/>
  <rect x="110" y="204" width="80" height="54" rx="12" fill="${C.white}" ${S}/>
  <path d="M136 222 l10 10 l20 -20" fill="none" stroke="${C.turquoise}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="150" cy="118" r="54" fill="${C.peach}" ${S}/>
  <path d="M94 104 Q98 52 150 50 Q202 52 206 104 Z" fill="${C.butter}" ${S}/>
  <path d="M188 104 L240 104 Q244 116 232 118 L188 118 Z" fill="${C.butter}" ${S}/>
  <circle cx="130" cy="126" r="7" fill="${INK}"/>
  <circle cx="170" cy="126" r="7" fill="${INK}"/>
  <ellipse cx="112" cy="146" rx="11" ry="6" fill="${C.pink}"/>
  <ellipse cx="188" cy="146" rx="11" ry="6" fill="${C.pink}"/>
  <path d="M134 148 Q150 162 166 148" fill="none" ${S}/>
  <path d="M214 196 Q246 236 236 262" fill="none" stroke="${INK}" stroke-width="20" stroke-linecap="round"/>
  <path d="M214 196 Q246 236 236 262" fill="none" stroke="${C.peach}" stroke-width="10" stroke-linecap="round"/>
  <path d="M212 262 Q212 242 236 242 Q260 242 260 262" fill="none" ${S}/>
  <rect x="196" y="258" width="82" height="56" rx="10" fill="${C.coral}" ${S}/>
  <path d="M196 280 L278 280" ${S}/>`,
    "0 0 300 360",
  ),
);

console.log("characters written to", outDir);
