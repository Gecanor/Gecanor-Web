'use client';

import { createContext, useCallback, useContext, useEffect, useState } from 'react';
import { translate } from '@/lib/i18n';

const LangContext = createContext({ lang: 'EN', setLang: () => {} });

export function useLang() {
  return useContext(LangContext);
}

export default function LangProvider({ children }) {
  const [lang, setLangState] = useState('EN');

  useEffect(() => {
    let stored = 'EN';
    try { stored = localStorage.getItem('gecanor-lang') || 'EN'; } catch (e) {}
    setLangState(stored);
  }, []);

  useEffect(() => {
    const ids = [0, 120, 400, 900].map((d) => setTimeout(() => translate(lang), d));
    return () => ids.forEach(clearTimeout);
  }, [lang]);

  const setLang = useCallback((next) => {
    setLangState(next);
    try { localStorage.setItem('gecanor-lang', next); } catch (e) {}
    translate(next);
  }, []);

  return <LangContext.Provider value={{ lang, setLang }}>{children}</LangContext.Provider>;
}
