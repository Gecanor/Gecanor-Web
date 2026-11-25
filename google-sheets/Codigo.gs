// Gecanor — guarda cada envío del formulario Get Started en esta hoja.
// Instrucciones en LEEME-Google-Sheets.txt
const HEADERS = ['Fecha','Idioma','Página','Full name','Job title','Email','Phone','Company name','Website','Years in business','Company type','Product type','Category','Services needed','Project budget (€)','First order quantity (units)','Year 1 projection (units)','Tell us more about your project','Estado'];
const KEYS = { 'Idioma': 'Language', 'Página': 'Page' };

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getSheetByName('Peticiones') || ss.insertSheet('Peticiones');
  if (sh.getLastRow() === 0) {
    sh.appendRow(HEADERS);
    sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold').setBackground('#0B0B0B').setFontColor('#FFFFFF');
    sh.setFrozenRows(1);
  }
  return sh;
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    const sh = sheet_();
    sh.appendRow(HEADERS.map(function (h) {
      if (h === 'Fecha') return new Date();
      if (h === 'Estado') return 'Nueva';
      return String(d[KEYS[h] || h] || '').slice(0, 5000);
    }));
    return ContentService.createTextOutput(JSON.stringify({ ok: true })).setMimeType(ContentService.MimeType.JSON);
  } finally { lock.releaseLock(); }
}

function doGet() { return ContentService.createTextOutput('Gecanor form endpoint OK'); }
