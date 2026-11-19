export const TAGS_FULL = [
  'Full Service',
  'Formula Development',
  'Product Manufacturing',
  'Regulatory Management',
  'Packaging Research',
  'Logistics Management',
  'Brand Strategy & Market Positioning'
];

export const STATEMENT_LINES = [
  '/Full service brand development in cosmetics and supplements',
  '/Formula development with our I+D+I team',
  '/Product manufacturing with top Spanish labs to provide premium cosmetic products',
  '/Regulatory management',
  '/Packaging research',
  '/Logistics management',
  '/Brand strategy & market positioning'
];

export const BRANDS_TOP = [
  { name: 'XSkinlab', logo: '/assets/brand-xskinlab.svg', w: 190 },
  { name: 'KŌEN Japan Beauty', logo: '/assets/brand-koen.png', w: 175 },
  { name: 'cosmefarm.', logo: '/assets/brand-cosmefarm.png', w: 200 },
  { name: 'gloa', logo: '/assets/brand-gloa.png', w: 120 },
  { name: 'FORMULAB+', logo: '/assets/brand-formulab.png', w: 215 }
];

export const BRANDS_BOTTOM = [
  { name: 'BINOMIAL', logo: '/assets/brand-binomial.png', w: 165, mono: true },
  { name: 'OLEVI', logo: '/assets/brand-olevi.png', w: 170 },
  { name: 'Clara Cervera', logo: '/assets/brand-clara.svg', w: 100 },
  { name: 'RÖS\u2019S', logo: '/assets/brand-ross.png', w: 165, mono: true },
  { name: 'evoxa', logo: '/assets/brand-evoxa.png', w: 150 },
  { name: 'antiojeras.com', logo: '/assets/brand-antiojeras.png', w: 205 }
];

export const PROJECTS = [
  { name: 'XSkinlab', href: 'https://xskinlab.com/', video: '/assets/proj-xskinlab.mp4', tags: TAGS_FULL },
  { name: 'Olevi', href: 'https://olevicosmetics.com/', video: '/assets/proj-olevi.mp4', tags: ['Formula Development', 'Product Manufacturing', 'Regulatory Management'] },
  { name: 'Binomial', href: 'https://binomial.skin/', video: '/assets/proj-binomial.mp4', tags: ['Brand Strategy & Market Positioning'] },
  { name: 'Evara haircare', href: '#work', video: '/assets/proj-evara.mp4', tags: TAGS_FULL },
  { name: 'Rös\u2019s', href: 'https://ross.international/', video: '/assets/proj-ross.mp4', tags: ['Packaging Research', 'Brand Strategy & Market Positioning'] },
  { name: 'Koen', href: 'https://www.koenjapan.com/', video: '/assets/proj-koen.mp4', tags: ['Formula Development', 'Product Manufacturing', 'Regulatory Management', 'Brand Strategy & Market Positioning'] },
  { name: 'Clara Cervera Beauty', href: 'https://claracerverabeauty.com/', video: '/assets/proj-clara.mp4', tags: TAGS_FULL },
  { name: 'Cosmefarm', href: '#work', video: '/assets/proj-cosmefarm.mp4', tags: TAGS_FULL },
  { name: 'Evoxa', href: 'https://evoxa.es/', video: '/assets/proj-evoxa.mp4', tags: ['Formula Development', 'Product Manufacturing', 'AEMPS Regulatory Management', 'Packaging Research', 'Market Positioning', 'Portfolio Development'] },
  { name: 'Formulab+', href: 'https://formulabplus.com/', video: '/assets/proj-formulab.mp4', tags: TAGS_FULL },
  { name: 'Gloa Cosmetics', href: 'https://gloacosmetics.com/', video: '/assets/proj-gloa.mp4', tags: TAGS_FULL },
  { name: 'Antiojeras.com', href: 'https://antiojeras.com/', video: '/assets/proj-antiojeras.mp4', tags: TAGS_FULL },
  { name: 'Orae Supplements', href: '#work', video: '/assets/proj-orae.mp4', tags: TAGS_FULL }
];

export const SERVICES_INDEX = [
  { label: '01 / Formula Development', href: '#s01' },
  { label: '02 / Manufacturing', href: '#s02' },
  { label: '03 / Regulatory', href: '#s03' },
  { label: '04 / Packaging', href: '#s04' },
  { label: '05 / Logistics', href: '#s05' },
  { label: '06 / Brand Strategy', href: '#s06' }
];

export const MFG = [
  '• MOQ from 2,000 units per reference',
  '• End-to-end production management',
  '• Raw material sourcing and quality control',
  '• Batch release and quality assurance documentation',
  '• Scalable production for growing brands'
];

export const PACK = [
  '• Primary container sourcing (bottles, tubes, jars, pumps)',
  '• Secondary packaging design coordination',
  '• Sustainability and eco-friendly options',
  '• Supplier negotiation and quality validation',
  '• Compatibility testing with formulas'
];

export const LOGI = [
  '• Warehouse and inventory management',
  '• Domestic and international shipping coordination',
  '• Import/export documentation',
  '• Cold-chain logistics for sensitive formulas',
  '• Customs and compliance support'
];

export const REG = [
  { n: '1', title: 'Stability & Compatibility Studies', body: [
    '• Product Stability Test: To ensure the product maintains its physical, chemical, and microbiological quality under various conditions over time.',
    '• Container Compatibility Test: To verify the compatibility between the product and its final packaging, ensuring no adverse reactions occur.'
  ] },
  { n: '2', title: 'Microbiological Testing', body: [
    'Performed on each production batch to guarantee the product is free from harmful microorganisms and meets the required quality standards.'
  ] },
  { n: '3', title: 'Challenge Test (Preservative Efficacy Test)', body: [
    'This test evaluates the effectiveness of the product\u2019s preservative system against microbial contamination during its shelf-life and consumer use.'
  ] },
  { n: '4', title: 'Patch Test', body: [
    'A skin compatibility test performed on human volunteers to ensure the product does not cause irritation or allergic reactions.'
  ] },
  { n: '5', title: 'Product Information File (PIF)', body: [
    'Compilation of the complete technical dossier for the cosmetic product, containing all data, reports, and information required by the EU regulation.'
  ] },
  { n: '6', title: 'Safety Assessment & CPNP Registration', body: [
    '• Safety Evaluation: A thorough safety assessment of the final product, conducted and signed by a qualified toxicologist or pharmacist.',
    '• CPNP Registration: Notification of the product in the European Cosmetic Products Notification Portal (CPNP), which is mandatory before placing it on the market.'
  ] }
];

export const STRATEGY = [
  { name: 'Brand Identity', desc: 'Naming, visual identity, tone of voice, and brand guidelines tailored to your target audience and market positioning.' },
  { name: 'Market Positioning', desc: 'Competitive analysis, target consumer definition, pricing strategy, and channel selection to maximize market impact.' },
  { name: 'Go-to-Market Strategy', desc: 'Launch planning, digital marketing strategy, influencer and PR approach, and retail/e-commerce channel development.' }
];

export const FORM_SERVICES = [
  'Full Service',
  'Formula Development',
  'Product Manufacturing',
  'Regulatory Management',
  'Packaging Research',
  'Logistics Management',
  'Brand Strategy & Market Positioning'
];
