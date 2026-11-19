'use client';

import Link from 'next/link';
import { useEffect, useRef } from 'react';
import PinnedLogo from '@/components/PinnedLogo';
import TopNav from '@/components/TopNav';
import Footer from '@/components/Footer';
import WorkWithUs from '@/components/WorkWithUs';
import { BRANDS_BOTTOM, BRANDS_TOP, PROJECTS, STATEMENT_LINES } from '@/lib/data';

const MARQUEE_COPIES = 8;

function BrandRow({ brands }) {
  return (
    <div
      data-brand-row="1"
      style={{ display: 'flex', flexWrap: 'nowrap', alignItems: 'center', justifyContent: 'center', gap: '24px 32px' }}
    >
      {brands.map((b) => (
        <div
          key={b.name}
          data-brand="1"
          style={{ flex: `0 1 ${b.w}px`, display: 'flex', alignItems: 'center', justifyContent: 'center', minWidth: 0, minHeight: 88 }}
        >
          <img
            src={b.logo}
            alt={b.name}
            loading="lazy"
            style={{
              width: '100%',
              height: 'auto',
              display: 'block',
              opacity: 1,
              transition: 'opacity 220ms ease',
              filter: b.mono ? 'grayscale(1) brightness(0.15)' : undefined,
              mixBlendMode: b.name === 'evoxa' ? 'multiply' : undefined
            }}
            onMouseEnter={(e) => { e.currentTarget.style.opacity = '0.35'; }}
            onMouseLeave={(e) => { e.currentTarget.style.opacity = '1'; }}
          />
        </div>
      ))}
    </div>
  );
}

function ProjectCard({ project }) {
  const ctaRef = useRef(null);
  const mediaRef = useRef(null);
  const external = project.href.startsWith('http');

  const enter = () => {
    if (ctaRef.current) ctaRef.current.style.opacity = '1';
    if (mediaRef.current) mediaRef.current.style.filter = 'brightness(0.94)';
  };
  const leave = () => {
    if (ctaRef.current) ctaRef.current.style.opacity = '0';
    if (mediaRef.current) mediaRef.current.style.filter = 'none';
  };

  return (
    <a
      href={project.href}
      data-project="1"
      target={external ? '_blank' : undefined}
      rel={external ? 'noopener noreferrer' : undefined}
      onMouseEnter={enter}
      onMouseLeave={leave}
      style={{ display: 'flex', flexDirection: 'column', gap: 14 }}
    >
      <div
        ref={mediaRef}
        style={{
          position: 'relative',
          aspectRatio: '16/10',
          overflow: 'hidden',
          background: 'repeating-linear-gradient(115deg,#E6E4E1 0 12px,#EFEDEA 12px 24px)'
        }}
      >
        <video
          data-lazy={project.video}
          preload="none"
          muted
          loop
          playsInline
          style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', display: 'block', background: '#EFEDEA' }}
        />
        <span
          ref={ctaRef}
          data-project-cta="1"
          style={{
            position: 'absolute', left: 14, bottom: 14, display: 'inline-flex', alignItems: 'center', gap: 8,
            padding: '8px 14px', borderRadius: 999, background: '#0A0A0A', color: '#FFFFFF', fontSize: 12,
            fontWeight: 500, opacity: 0, transition: 'opacity 260ms ease'
          }}
        >
          ▶ View brand ↗
        </span>
      </div>
      <h3 style={{ margin: 0, fontSize: 'clamp(21px,1.9vw,28px)', fontWeight: 400, letterSpacing: '-0.03em' }}>{project.name}</h3>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10 }}>
        {project.tags.map((tag) => (
          <span
            key={tag}
            style={{
              display: 'inline-flex', alignItems: 'center', whiteSpace: 'nowrap', padding: '7px 15px',
              border: '1px solid #0A0A0A', borderRadius: 999, fontSize: 13, fontWeight: 400, letterSpacing: '-0.005em'
            }}
          >
            {tag}
          </span>
        ))}
      </div>
    </a>
  );
}

export default function HomePage() {
  useEffect(() => {
    const fadeLines = Array.from(document.querySelectorAll('[data-fade-line]'));

    const onScroll = () => {
      const h = window.innerHeight;
      fadeLines.forEach((n) => {
        const r = n.getBoundingClientRect();
        let t = (h * 0.82 - r.top) / (h * 0.3);
        t = Math.max(0, Math.min(1, t));
        const v = Math.round(201 - 191 * t);
        n.style.color = `rgb(${v},${v},${v})`;
      });
    };

    const checkVideos = () => {
      const h = window.innerHeight;
      document.querySelectorAll('video[data-lazy]').forEach((v) => {
        const r = v.getBoundingClientRect();
        const near = r.top < h * 1.4 && r.bottom > -h * 0.4;
        const visible = r.top < h && r.bottom > 0;
        if (near && !v.src) { v.src = v.dataset.lazy; v.load(); }
        if (!v.src) return;
        if (visible && v.paused) { const p = v.play(); if (p && p.catch) p.catch(() => {}); }
        else if (!visible && !v.paused) { v.pause(); }
      });
    };

    const checkWipes = () => {
      const h = window.innerHeight;
      document.querySelectorAll('[data-wipe]').forEach((n) => {
        if (n.dataset.wiped) return;
        const r = n.getBoundingClientRect();
        if (r.top < h * 0.88 && r.bottom > 0) {
          n.dataset.wiped = '1';
          n.style.clipPath = 'inset(0 0 0 0)';
        }
      });
    };

    const handlers = [onScroll, checkVideos, checkWipes];
    handlers.forEach((fn) => {
      window.addEventListener('scroll', fn, { passive: true });
      window.addEventListener('resize', fn);
    });

    onScroll();
    const tWipes = setTimeout(checkWipes, 60);
    const tVideos = setTimeout(checkVideos, 400);

    return () => {
      handlers.forEach((fn) => {
        window.removeEventListener('scroll', fn);
        window.removeEventListener('resize', fn);
      });
      clearTimeout(tWipes);
      clearTimeout(tVideos);
    };
  }, []);

  return (
    <div style={{ width: '100%', overflowX: 'hidden', background: '#FFFFFF' }}>
      <PinnedLogo href="#top" />
      <TopNav current="home" />

      <section id="top" style={{ position: 'relative', height: '100vh', minHeight: 560, width: '100%', overflow: 'hidden', background: '#D9D7D4' }}>
        <video
          src="/assets/hero.mp4"
          autoPlay
          muted
          loop
          playsInline
          style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover', display: 'block' }}
        />
        <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '0 20px' }}>
          <img src="/assets/gecanor-logo.png" alt="gecanor. beauty tech" style={{ width: 'min(62vw,900px)', height: 'auto', display: 'block' }} />
        </div>
        <a
          href="#statement"
          data-scroll-cue="1"
          style={{
            position: 'absolute', left: 64, bottom: 26, fontFamily: 'ui-monospace,SFMono-Regular,Menlo,monospace',
            fontSize: 11, letterSpacing: '0.14em', color: '#0A0A0A', animation: 'grCue 2.4s ease-in-out infinite'
          }}
        >
          SCROLL ↓
        </a>
        <a href="mailto:social@gecanor.com" style={{ position: 'absolute', right: 64, bottom: 26, fontSize: 15, fontWeight: 500, color: '#0A0A0A' }}>
          social@gecanor.com
        </a>
      </section>

      <section id="statement" style={{ maxWidth: 1560, margin: '0 auto', padding: '84px 64px 64px' }}>
        <h1 style={{ margin: 0, fontSize: 'clamp(30px,4.6vw,70px)', lineHeight: 1.04, fontWeight: 400, letterSpacing: '-0.035em', textWrap: 'pretty' }}>
          We are fully dedicated to create within the cosmetic and supplements space.
        </h1>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6, margin: '56px 0 32px' }}>
          {STATEMENT_LINES.map((line) => (
            <div
              key={line}
              data-fade-line="1"
              style={{ fontSize: 'clamp(17px,2.05vw,32px)', lineHeight: 1.3, fontWeight: 400, letterSpacing: '-0.025em', whiteSpace: 'nowrap', color: '#C9C9C9' }}
            >
              {line}
            </div>
          ))}
        </div>
        <Link
          href="/services"
          style={{
            display: 'inline-flex', alignItems: 'center', gap: 12, fontSize: 'clamp(17px,1.9vw,26px)',
            fontWeight: 500, letterSpacing: '-0.02em', borderBottom: '1px solid #0A0A0A', paddingBottom: 4
          }}
        >
          More information <span style={{ fontSize: '0.9em' }}>↗</span>
        </Link>
      </section>

      <section
        data-wipe="1"
        style={{ background: '#000000', color: '#FFFFFF', padding: '20px 64px', clipPath: 'inset(0 100% 0 0)', transition: 'clip-path 1100ms cubic-bezier(.22,.61,.36,1)' }}
      >
        <h2 style={{ margin: 0, textAlign: 'center', fontSize: 'clamp(22px,3.4vw,50px)', fontWeight: 400, letterSpacing: '-0.032em' }}>
          Some of our work. Different brands. Same goal.
        </h2>
      </section>

      <section id="work" style={{ padding: '40px 0 0' }}>
        <div style={{ overflow: 'hidden', whiteSpace: 'nowrap', padding: '8px 0 40px' }}>
          <div style={{ display: 'inline-flex', gap: 120, animation: 'grMarquee 26s linear infinite', fontSize: 'clamp(14px,1.5vw,22px)', fontWeight: 600, letterSpacing: '0.02em' }}>
            {Array.from({ length: MARQUEE_COPIES }).map((_, i) => (
              <span key={i}>ONE VERTICAL SPECIALISTS</span>
            ))}
          </div>
        </div>
        <div
          style={{
            maxWidth: 1560, margin: '0 auto', padding: '0 64px', display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit,minmax(min(100%,520px),1fr))', gap: '52px 40px'
          }}
        >
          {PROJECTS.map((project) => (
            <ProjectCard key={project.name} project={project} />
          ))}
        </div>
      </section>

      <WorkWithUs wipe marginTop={76} />

      <section style={{ background: '#F4F4F3', padding: '68px 64px' }}>
        <div style={{ maxWidth: 1432, margin: '0 auto', display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(320px,1fr))', gap: 40, alignItems: 'end' }}>
          <div>
            <h2 style={{ margin: '0 0 26px', fontSize: 'clamp(30px,4vw,54px)', fontWeight: 400, letterSpacing: '-0.035em', color: '#0A0A0A' }}>Find us here</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 0, maxWidth: 520 }}>
              <div style={{ display: 'flex', gap: 28, padding: '16px 0', borderBottom: '1px solid #C8C8C6' }}>
                <span style={{ minWidth: 96, fontSize: 'clamp(19px,2vw,26px)', fontWeight: 500, letterSpacing: '-0.02em' }}>Spain</span>
                <span style={{ fontSize: 15, lineHeight: 1.45 }}>C/ Balmes 127, Principal 2ºA<br />08008 Barcelona</span>
              </div>
              <div style={{ display: 'flex', gap: 28, padding: '16px 0', borderBottom: '1px solid #C8C8C6' }}>
                <span style={{ minWidth: 96, fontSize: 'clamp(19px,2vw,26px)', fontWeight: 500, letterSpacing: '-0.02em' }}>China</span>
                <span style={{ fontSize: 15, lineHeight: 1.45 }}>Wanke Jiazhouwan V-Pai, 501<br />610036 Chengdu</span>
              </div>
            </div>
          </div>
          <div style={{ aspectRatio: '4/3', overflow: 'hidden', background: '#E2E0DD' }}>
            <img
              src="/assets/oficina.png"
              alt="Gecanor office, Barcelona"
              loading="lazy"
              style={{ width: '100%', height: '100%', objectFit: 'cover', objectPosition: '50% 35%', display: 'block' }}
            />
          </div>
        </div>
      </section>

      <section data-gr-section="1" style={{ padding: '30px 64px 40px', textAlign: 'center' }}>
        <span
          data-gr-mark="1"
          style={{
            display: 'block', width: 'min(42vw,440px)', aspectRatio: '99.19/82.86', margin: '0 auto', background: '#0A0A0A',
            WebkitMask: 'url(/assets/gr.svg) center/contain no-repeat',
            mask: 'url(/assets/gr.svg) center/contain no-repeat',
            animation: 'grSpin 9s cubic-bezier(.62,.06,.35,.96) infinite'
          }}
        />
        <p
          style={{
            margin: '26px auto 0', maxWidth: 'min(48ch,94vw)', fontSize: 'clamp(19px,2.9vw,44px)',
            lineHeight: 1.18, fontWeight: 400, letterSpacing: '-0.032em', textWrap: 'pretty'
          }}
        >
          Gecanor transforms ideas into beauty experiences. We craft brands that matter by blending Strategic Thinking, Creative Innovation and Cutting-edge Technology into every step — from formulation to market launch.
        </p>
        <div style={{ maxWidth: 1400, margin: '60px auto 0', display: 'flex', flexDirection: 'column', gap: 20 }}>
          <BrandRow brands={BRANDS_TOP} />
          <BrandRow brands={BRANDS_BOTTOM} />
        </div>
      </section>

      <Footer homeHref="#top" />
    </div>
  );
}
