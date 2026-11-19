'use client';

import Link from 'next/link';
import { useLang } from './LangProvider';

const LANGS = ['EN', 'ES', 'CAT'];

export default function TopNav({ current }) {
  const { lang, setLang } = useLang();

  return (
    <nav
      data-topnav="1"
      style={{
        position: 'fixed', top: 30, right: 18, zIndex: 200, display: 'flex', flexDirection: 'column',
        alignItems: 'flex-end', gap: 10, mixBlendMode: 'difference', color: '#FFFFFF',
        fontSize: 14, fontWeight: 500, letterSpacing: '-0.01em'
      }}
    >
      <span data-langs="1" style={{ order: 2, display: 'flex', alignItems: 'center', gap: 5, fontSize: 12, fontWeight: 400 }}>
        {LANGS.map((code, i) => (
          <span key={code} style={{ display: 'flex', alignItems: 'center', gap: 5 }}>
            {i > 0 ? <span style={{ opacity: 0.4 }}>/</span> : null}
            <button
              type="button"
              onClick={() => setLang(code)}
              aria-pressed={lang === code}
              style={{
                background: 'none', border: 0, padding: 0, cursor: 'pointer', font: 'inherit', color: 'inherit',
                fontSize: 12, letterSpacing: 0,
                fontWeight: lang === code ? 600 : 400,
                opacity: lang === code ? 1 : 0.5
              }}
            >
              {code}
            </button>
          </span>
        ))}
      </span>
      <Link href="/get-started" style={{ fontWeight: 600, opacity: current === 'get-started' ? 0.55 : 1 }}>Get Started</Link>
    </nav>
  );
}
