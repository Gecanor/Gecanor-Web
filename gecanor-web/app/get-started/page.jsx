'use client';

import { useState } from 'react';
import PinnedLogo from '@/components/PinnedLogo';
import TopNav from '@/components/TopNav';
import Footer from '@/components/Footer';
import { FORM_SERVICES } from '@/lib/data';

const CONTACT_EMAIL = 'sonia@gecanor.com';

const field = { padding: '13px 14px', background: '#FFFFFF', border: '1px solid #DCDCDA', fontSize: 15 };
const labelText = { fontSize: 14, fontWeight: 500 };
const legendStyle = {
  padding: '0 0 14px', width: '100%', borderBottom: '1px solid #E4E4E2',
  fontFamily: 'ui-monospace,SFMono-Regular,Menlo,monospace', fontSize: 11, letterSpacing: '0.16em', color: '#9A9A9A'
};
const rowStyle = { display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(260px,1fr))', gap: 24, marginTop: 22 };
const step = { padding: '8px 15px', border: '1px solid #E4E4E2', borderRadius: 999, fontSize: 12.5, color: '#4A4A4A' };

function Label({ children, label }) {
  return (
    <label style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
      <span style={labelText}>{label}</span>
      {children}
    </label>
  );
}

export default function GetStartedPage() {
  const [status, setStatus] = useState('idle');
  const [services, setServices] = useState([]);

  const toggleService = (name) => {
    setServices((prev) => (prev.includes(name) ? prev.filter((s) => s !== name) : [...prev, name]));
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    if (status === 'sending') return;
    const form = e.currentTarget;
    const data = { _subject: 'New project enquiry — Gecanor', _template: 'table', _captcha: 'false' };
    form.querySelectorAll('label').forEach((label) => {
      const input = label.querySelector('input, select, textarea');
      if (!input || input.type === 'checkbox') return;
      const name = (label.querySelector('span')?.textContent || '').replace(' *', '').trim();
      if (input.value) data[name] = input.value;
      if (input.type === 'email' && input.value) data._replyto = input.value;
    });
    if (services.length) data['Services needed'] = services.join(', ');
    setStatus('sending');
    try {
      const res = await fetch(`https://formsubmit.co/ajax/${CONTACT_EMAIL}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(data)
      });
      const json = await res.json();
      if (res.ok && String(json.success) === 'true') {
        setStatus('sent');
        setServices([]);
        form.reset();
      } else {
        setStatus('error');
      }
    } catch (err) {
      setStatus('error');
    }
  };

  return (
    <div style={{ width: '100%', overflowX: 'hidden', background: '#FFFFFF' }}>
      <PinnedLogo href="/" />
      <TopNav current="get-started" />

      <section id="top" style={{ maxWidth: 1120, margin: '0 auto', padding: '112px 64px 0' }}>
        <h1 style={{ margin: 0, fontSize: 'clamp(40px,6.4vw,86px)', lineHeight: 0.96, fontWeight: 400, letterSpacing: '-0.045em' }}>Get Started</h1>
        <p style={{ margin: '18px 0 0', fontSize: 'clamp(16px,1.7vw,20px)', lineHeight: 1.5, color: '#3A3A3A' }}>
          Tell us about your project. Our team needs this information to evaluate and respond to your inquiry.
        </p>
        <div style={{ marginTop: 22, fontFamily: 'ui-monospace,SFMono-Regular,Menlo,monospace', fontSize: 11, letterSpacing: '0.12em', color: '#9A9A9A' }}>
          CONFIDENTIAL — WE DO NOT SHARE YOUR INFORMATION
        </div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10, marginTop: 26 }}>
          <span style={step}>1 · Brief received</span>
          <span style={step}>2 · Feasibility review in 48h</span>
          <span style={step}>3 · Scope &amp; quote</span>
        </div>
      </section>

      <form onSubmit={onSubmit} style={{ maxWidth: 1120, margin: '0 auto', padding: '44px 64px 68px', display: 'flex', flexDirection: 'column', gap: 40 }}>
        <fieldset style={{ border: 0, padding: 0, margin: 0 }}>
          <legend style={legendStyle}>PERSONAL</legend>
          <div style={rowStyle}>
            <Label label="Full name *"><input type="text" required placeholder="First and last name" style={field} /></Label>
            <Label label="Job title *"><input type="text" required placeholder="Your position" style={field} /></Label>
            <Label label="Email *"><input type="email" required placeholder="you@email.com" style={field} /></Label>
            <Label label="Phone *"><input type="tel" required placeholder="+1 600 000 000" style={field} /></Label>
          </div>
        </fieldset>

        <fieldset style={{ border: 0, padding: 0, margin: 0 }}>
          <legend style={legendStyle}>COMPANY</legend>
          <div style={rowStyle}>
            <Label label="Company name *"><input type="text" required placeholder="Company Inc." style={field} /></Label>
            <Label label="Website"><input type="url" placeholder="https://yourcompany.com" style={field} /></Label>
          </div>
          <div style={{ marginTop: 24 }}>
            <Label label="Address"><input type="text" placeholder="Company address" style={field} /></Label>
          </div>
          <div style={rowStyle}>
            <Label label="Years in business *">
              <select required defaultValue="" style={field}>
                <option value="">Select</option>
                <option>Pre-launch</option>
                <option>Less than 1 year</option>
                <option>1 – 3 years</option>
                <option>3 – 10 years</option>
                <option>More than 10 years</option>
              </select>
            </Label>
            <Label label="Company type *">
              <select required defaultValue="" style={field}>
                <option value="">Select</option>
                <option>Cosmetic brand</option>
                <option>Supplement brand</option>
                <option>Clinic / aesthetic professional</option>
                <option>Retailer or distributor</option>
                <option>Startup / entrepreneur</option>
                <option>Other</option>
              </select>
            </Label>
          </div>
        </fieldset>

        <fieldset style={{ border: 0, padding: 0, margin: 0 }}>
          <legend style={legendStyle}>PRODUCT / PROJECT</legend>
          <div style={rowStyle}>
            <Label label="Product type *"><input type="text" required placeholder="Serum, cream, supplement..." style={field} /></Label>
            <Label label="Category *">
              <select required defaultValue="" style={field}>
                <option value="">Select</option>
                <option>Skincare</option>
                <option>Body care</option>
                <option>Haircare</option>
                <option>Professional / clinical</option>
                <option>Supplements &amp; nutricosmetics</option>
                <option>Colour cosmetics</option>
              </select>
            </Label>
          </div>
          <div style={{ marginTop: 24 }}>
            <Label label="Regulatory class"><input type="text" placeholder="E.g.: Cosmetic, dietary supplement..." style={field} /></Label>
          </div>
          <div style={{ marginTop: 24 }}>
            <span style={{ display: 'block', ...labelText, marginBottom: 12 }}>Services needed</span>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10 }}>
              {FORM_SERVICES.map((name) => {
                const on = services.includes(name);
                return (
                  <label
                    key={name}
                    data-chip="1"
                    style={{
                      display: 'inline-flex', alignItems: 'center', gap: 9, padding: '9px 16px',
                      border: `1px solid ${on ? '#0A0A0A' : '#DCDCDA'}`, borderRadius: 999, fontSize: 13.5, cursor: 'pointer',
                      background: on ? '#0A0A0A' : '#FFFFFF', color: on ? '#FFFFFF' : '#0A0A0A'
                    }}
                  >
                    <input
                      type="checkbox"
                      checked={on}
                      onChange={() => toggleService(name)}
                      style={{ width: 14, height: 14, accentColor: on ? '#FFFFFF' : '#0A0A0A', margin: 0 }}
                    />
                    {name}
                  </label>
                );
              })}
            </div>
          </div>
        </fieldset>

        <fieldset style={{ border: 0, padding: 0, margin: 0 }}>
          <legend style={legendStyle}>BUDGET &amp; VOLUME</legend>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(200px,1fr))', gap: 24, marginTop: 22 }}>
            <Label label="Project budget (€)"><input type="text" placeholder="20,000" style={field} /></Label>
            <Label label="First order quantity (units)"><input type="text" placeholder="5,000" style={field} /></Label>
            <Label label="Year 1 projection (units)"><input type="text" placeholder="50,000" style={field} /></Label>
          </div>
          <p style={{ margin: '18px 0 0', fontSize: 13, color: '#9A9A9A' }}>Minimum order quantity starts at 2,000 units per reference.</p>
        </fieldset>

        <fieldset style={{ border: 0, padding: 0, margin: 0 }}>
          <legend style={legendStyle}>MORE INFORMATION</legend>
          <div style={{ marginTop: 22 }}>
            <Label label="Tell us more about your project *">
              <textarea
                rows={7}
                required
                placeholder="Tell us about your company, your product idea, and what you need from us..."
                style={{ padding: 14, background: '#FFFFFF', border: '1px solid #DCDCDA', fontSize: 15, lineHeight: 1.55, resize: 'vertical' }}
              />
            </Label>
          </div>
        </fieldset>

        <div style={{ paddingTop: 22, borderTop: '1px solid #E4E4E2', display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: 24, justifyContent: 'space-between' }}>
          <p style={{ margin: 0, fontSize: 13.5, color: '#6E6E6E' }}>Fields marked with * are required. Your information is confidential.</p>
          <button
            type="submit"
            disabled={status === 'sending'}
            style={{
              padding: '15px 42px', background: '#0A0A0A', color: '#FFFFFF', border: 0,
              fontFamily: 'ui-monospace,SFMono-Regular,Menlo,monospace', fontSize: 12, fontWeight: 500,
              letterSpacing: '0.16em', cursor: 'pointer'
            }}
          >
            {status === 'sending' ? 'SENDING…' : status === 'sent' ? 'SENT — WE WILL REPLY WITHIN 48H' : status === 'error' ? 'ERROR — PLEASE TRY AGAIN' : 'SUBMIT'}
          </button>
        </div>
      </form>

      <Footer getStartedHref="#top" />
    </div>
  );
}
