import { Inter } from 'next/font/google';
import './globals.css';
import LangProvider from '@/components/LangProvider';

const inter = Inter({ subsets: ['latin'], weight: ['400', '500', '600', '700'], variable: '--font-inter', display: 'swap' });

export const metadata = {
  title: 'Gecanor — Beauty Tech',
  description: 'Integral development of cosmetic and supplement brands. Formulation, manufacturing, regulatory, packaging, logistics and brand strategy.',
  openGraph: {
    title: 'Gecanor — Beauty Tech',
    description: 'Integral development of cosmetic and supplement brands.',
    type: 'website'
  }
};

export const viewport = { width: 'device-width', initialScale: 1 };

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={inter.variable}>
      <body>
        <LangProvider>{children}</LangProvider>
      </body>
    </html>
  );
}
