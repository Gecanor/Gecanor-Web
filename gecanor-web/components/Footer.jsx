import Link from 'next/link';

export default function Footer({ homeHref = '/', servicesHref = '/services', getStartedHref = '/get-started', topBorder = false }) {
  return (
    <footer style={{ background: '#000000', color: '#FFFFFF', padding: '44px 64px', borderTop: topBorder ? '1px solid #1E1E1E' : undefined }}>
      <div style={{ maxWidth: 1560, margin: '0 auto', display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(240px,1fr))', gap: 40, alignItems: 'start' }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
          <span style={{ fontSize: 16, fontWeight: 500 }}>Let&#39;s collaborate!</span>
          <a href="mailto:social@gecanor.com" style={{ fontSize: 16 }}>social@gecanor.com</a>
        </div>
        <div style={{ display: 'flex', justifyContent: 'center', fontSize: 15, lineHeight: 1.45, color: '#DADADA' }}>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 22, textAlign: 'left' }}>
            <span>C/ Balmes 127, Principal 2ºA<br />08008 Barcelona</span>
            <span>Wanke Jiazhouwan V-Pai, 501<br />610036 Chengdu</span>
          </div>
        </div>
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
          <img src="/assets/gecanor-logo-white.png" alt="gecanor. beauty tech" style={{ width: 'min(240px,60vw)', height: 'auto', display: 'block' }} />
        </div>
      </div>
      <div style={{ maxWidth: 1560, margin: '34px auto 0', paddingTop: 18, borderTop: '1px solid #232323', display: 'flex', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'space-between', gap: 20 }}>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 32, fontSize: 15, color: '#DADADA' }}>
          <Link href={homeHref}>Home</Link>
          <Link href={servicesHref}>Services</Link>
          <Link href={getStartedHref}>Get Started</Link>
        </div>
        <span style={{ fontSize: 13, color: '#8A8A8A' }}>© 2026 Gecanor Beauty Tech</span>
      </div>
    </footer>
  );
}
