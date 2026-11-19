'use client';

import PinnedLogo from '@/components/PinnedLogo';
import TopNav from '@/components/TopNav';
import Footer from '@/components/Footer';
import WorkWithUs from '@/components/WorkWithUs';
import { LOGI, MFG, PACK, REG, SERVICES_INDEX, STRATEGY } from '@/lib/data';

const sectionStyle = (padding) => ({ maxWidth: 1560, margin: '0 auto', padding });
const numStyle = { fontSize: 'clamp(24px,3vw,38px)', fontWeight: 400, letterSpacing: '-0.03em', color: '#9A9A9A' };
const titleStyle = { margin: 0, fontSize: 'clamp(22px,3vw,38px)', fontWeight: 400, letterSpacing: '-0.02em', textTransform: 'uppercase' };
const leadStyle = { maxWidth: '92ch', fontSize: 'clamp(17px,1.8vw,24px)', lineHeight: 1.42, letterSpacing: '-0.02em' };
const grey = { color: '#9A9A9A' };
const cellStyle = { background: '#FFFFFF', boxShadow: '0 0 0 1px #E4E4E2', padding: 22, fontSize: 15.5, lineHeight: 1.45 };

function Head({ n, children }) {
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', gap: 22, marginBottom: 20 }}>
      <span style={numStyle}>{n}</span>
      <h2 style={titleStyle}>{children}</h2>
    </div>
  );
}

function Cells({ items, marginTop = 36 }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(260px,1fr))', gap: 1, border: '1px solid #E4E4E2', marginTop }}>
      {items.map((item) => (
        <div key={item} style={cellStyle}>{item}</div>
      ))}
    </div>
  );
}

export default function ServicesPage() {
  return (
    <div style={{ width: '100%', overflowX: 'hidden', background: '#FFFFFF' }}>
      <PinnedLogo href="/" />
      <TopNav current="services" />

      <section id="top" style={sectionStyle('112px 64px 32px')}>
        <h1 style={{ margin: 0, fontSize: 'clamp(48px,8vw,112px)', lineHeight: 0.94, fontWeight: 400, letterSpacing: '-0.045em' }}>Services</h1>
        <p style={{ margin: '20px 0 0', maxWidth: '92ch', fontSize: 'clamp(16px,1.6vw,21px)', lineHeight: 1.5, color: '#4A4A4A' }}>
          Six disciplines under one roof. Pick the ones you need or hand us the whole path from brief to shelf.
        </p>
      </section>

      <nav
        data-sticky-nav="1"
        style={{
          position: 'sticky', top: 0, zIndex: 150, background: 'rgba(255,255,255,0.94)', backdropFilter: 'blur(10px)',
          borderBottom: '1px solid #E4E4E2', padding: '14px 64px 14px 130px'
        }}
      >
        <div style={{ maxWidth: 1560, margin: '0 auto', display: 'flex', flexWrap: 'wrap', gap: 10 }}>
          {SERVICES_INDEX.map((i) => (
            <a
              key={i.href}
              href={i.href}
              style={{
                display: 'inline-flex', alignItems: 'center', whiteSpace: 'nowrap', padding: '7px 14px',
                border: '1px solid #D8D8D6', borderRadius: 999, fontSize: 12.5, fontWeight: 500, color: '#4A4A4A'
              }}
            >
              {i.label}
            </a>
          ))}
        </div>
      </nav>

      <section id="s01" style={sectionStyle('60px 64px 0')}>
        <Head n="01/">Formula Development &amp; Innovation</Head>
        <p style={{ margin: '0 0 12px', ...leadStyle }}>
          We develop exclusive and innovative formulas for <span style={grey}>cosmetic and nutricosmetic</span> products, tailored to the specific needs of your brand.
        </p>
        <p style={{ margin: 0, ...leadStyle }}>
          Our R&amp;D&amp;I team focuses on creating <span style={grey}>high-performance</span> products with <span style={grey}>scientifically-backed ingredients</span>.
        </p>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(240px,1fr))', gap: 28, marginTop: 40, paddingTop: 20, borderTop: '1px solid #E4E4E2' }}>
          <div>
            <div style={{ fontSize: 13, color: '#9A9A9A', marginBottom: 14 }}>Service</div>
            <div style={{ fontSize: 16, fontWeight: 500 }}>Custom Formula Development</div>
          </div>
          <div>
            <div style={{ fontSize: 13, color: '#9A9A9A', marginBottom: 14 }}>Description</div>
            <p style={{ margin: 0, fontSize: 16, lineHeight: 1.55 }}>
              Creation of a unique formula based on your brand&#39;s requirements, target audience, and desired product characteristics. Includes ingredient sourcing, lab-scale sample creation, and iterative revisions.
            </p>
          </div>
          <div>
            <div style={{ fontSize: 13, color: '#9A9A9A', marginBottom: 14 }}>Deliverables</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 6, fontSize: 16, lineHeight: 1.5 }}>
              <span>• Final Product Formula</span>
              <span>• Lab-scale Samples</span>
              <span>• Ingredient Dossier</span>
              <span>• Intellectual Property ownership</span>
            </div>
          </div>
        </div>
      </section>

      <section id="s02" style={sectionStyle('72px 64px 0')}>
        <Head n="02/">Manufacturing &amp; Production</Head>
        <p style={{ margin: 0, ...leadStyle }}>
          We manage the production process to ensure the <span style={grey}>highest quality standards</span> are met, from <span style={grey}>raw material sourcing</span> to the <span style={grey}>final packaged product</span>. We work with <span style={grey}>top Spanish laboratories</span> to provide premium cosmetic products at scale.
        </p>
        <Cells items={MFG} />
      </section>

      <section id="s03" style={sectionStyle('72px 64px 0')}>
        <Head n="03/">Regulatory &amp; Compliance Services</Head>
        <p style={{ margin: '0 0 40px', ...leadStyle }}>
          We ensure that your products comply with all the rigorous requirements of the <span style={grey}>European Union&#39;s cosmetic regulations (EC) No 1223/2009</span>. Our comprehensive regulatory package covers all necessary testing, documentation, and registration to legally place your product on the market.
        </p>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          {REG.map((r) => (
            <div
              key={r.n}
              data-reg-row="1"
              style={{ display: 'grid', gridTemplateColumns: '64px minmax(180px,1fr) minmax(280px,2fr)', gap: 24, padding: '20px 0', borderTop: '1px solid #E4E4E2' }}
            >
              <span style={{ fontSize: 26, fontWeight: 400, color: '#9A9A9A', lineHeight: 1 }}>{r.n}</span>
              <span style={{ fontSize: 16, fontWeight: 500, lineHeight: 1.4 }}>{r.title}</span>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 14, fontSize: 15.5, lineHeight: 1.55, color: '#2A2A2A' }}>
                {r.body.map((b) => <span key={b}>{b}</span>)}
              </div>
            </div>
          ))}
        </div>
      </section>

      <section id="s04" style={sectionStyle('72px 64px 0')}>
        <Head n="04/">Packaging Research &amp; Sourcing</Head>
        <p style={{ margin: 0, ...leadStyle }}>
          We identify and source the most suitable <span style={grey}>primary and secondary packaging</span> for your product, balancing aesthetics, functionality, sustainability, and cost-efficiency. Our network of suppliers ensures access to premium packaging solutions aligned with your brand identity.
        </p>
        <Cells items={PACK} />
      </section>

      <section id="s05" style={sectionStyle('72px 64px 0')}>
        <Head n="05/">Logistics Management</Head>
        <p style={{ margin: 0, ...leadStyle }}>
          We coordinate the full logistics chain <span style={grey}>from production to final delivery</span>, ensuring your products reach their destination on time and in perfect condition. Our logistics expertise covers both domestic and international markets.
        </p>
        <Cells items={LOGI} />
      </section>

      <section id="s06" style={sectionStyle('72px 64px 68px')}>
        <Head n="06/">Brand Strategy &amp; Market Positioning</Head>
        <p style={{ margin: 0, ...leadStyle }}>
          We help cosmetic and supplement brands define their identity, positioning, and go-to-market strategy. From <span style={grey}>naming and visual identity</span> to <span style={grey}>digital presence and retail strategy</span>, we provide the strategic framework to connect your brand with its target consumer.
        </p>
        <div style={{ marginTop: 40, paddingTop: 20, borderTop: '1px solid #E4E4E2', display: 'flex', flexDirection: 'column', gap: 0 }}>
          <div data-strategy-head="1" style={{ display: 'grid', gridTemplateColumns: 'minmax(180px,1fr) minmax(280px,2fr)', gap: 24, paddingBottom: 14, fontSize: 13, color: '#9A9A9A' }}>
            <span>Service</span><span>Description</span>
          </div>
          {STRATEGY.map((s) => (
            <div
              key={s.name}
              data-strategy-row="1"
              style={{ display: 'grid', gridTemplateColumns: 'minmax(180px,1fr) minmax(280px,2fr)', gap: 24, padding: '18px 0', borderTop: '1px solid #E4E4E2' }}
            >
              <span style={{ fontSize: 16, fontWeight: 500 }}>{s.name}</span>
              <span style={{ fontSize: 15.5, lineHeight: 1.55, color: '#2A2A2A' }}>{s.desc}</span>
            </div>
          ))}
        </div>
      </section>

      <WorkWithUs />
      <Footer servicesHref="#top" topBorder />
    </div>
  );
}
