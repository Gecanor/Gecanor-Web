import Link from 'next/link';

export default function WorkWithUs({ wipe = false, marginTop = 0 }) {
  return (
    <section
      data-wipe={wipe ? '1' : undefined}
      style={{
        marginTop, background: '#000000', color: '#FFFFFF', padding: '48px 64px',
        clipPath: wipe ? 'inset(0 100% 0 0)' : undefined,
        transition: wipe ? 'clip-path 1100ms cubic-bezier(.22,.61,.36,1)' : undefined
      }}
    >
      <div style={{ maxWidth: 1432, margin: '0 auto', display: 'flex', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'space-between', gap: 32 }}>
        <div>
          <h2 style={{ margin: '0 0 8px', fontSize: 'clamp(30px,4.4vw,58px)', fontWeight: 400, letterSpacing: '-0.035em' }}>Work with us!</h2>
          <p style={{ margin: 0, fontSize: 'clamp(16px,1.8vw,26px)', fontWeight: 400, color: '#DADADA' }}>Let&#39;s create your next beauty innovation.</p>
        </div>
        <Link
          href="/get-started"
          style={{ padding: '18px 52px', borderRadius: 999, background: '#FFFFFF', color: '#0A0A0A', fontSize: 18, fontWeight: 400, letterSpacing: '-0.01em' }}
        >
          Get Started
        </Link>
      </div>
    </section>
  );
}
