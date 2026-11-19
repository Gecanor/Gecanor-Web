'use client';

import Link from 'next/link';

export default function PinnedLogo({ href = '/' }) {
  return (
    <Link
      href={href}
      aria-label="Gecanor home"
      data-pinned-logo="1"
      style={{ position: 'fixed', top: 14, left: 18, zIndex: 200, display: 'block', width: 96, height: 80, mixBlendMode: 'difference' }}
    >
      <span
        data-gr-mark="1"
        style={{
          display: 'block',
          width: '100%',
          height: '100%',
          background: '#FFFFFF',
          WebkitMask: 'url(/assets/gr.svg) center/contain no-repeat',
          mask: 'url(/assets/gr.svg) center/contain no-repeat',
          animation: 'grSpin 7s cubic-bezier(.62,.06,.35,.96) infinite'
        }}
      />
    </Link>
  );
}
