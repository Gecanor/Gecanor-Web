# -*- coding: utf-8 -*-
"""Artículos de la sección Recursos.

Cada artículo: el texto va en <slug>.<idioma>.md y aquí sus datos.
Un artículo se publica (página, listado, sitemap) cuando su fecha `date` es hoy o anterior
y existe su .md en ese idioma. Para publicar: python3 source/build.py y subir a GitHub.
`cat` debe ser una de las categorías de la página de Recursos:
Formulation, Regulatory, Manufacturing, Packaging, Brand & market.
"""

AUTHOR = {'name': 'David Castillo', 'role': {'es': 'CEO de Gecanor Beauty Tech', 'ca': 'CEO de Gecanor Beauty Tech', 'en': 'CEO, Gecanor Beauty Tech'}}

from translations import TR  # textos en inglés y catalán

ARTICLES = [
    {
        'slug': 'crear-marca-cosmetica-propia',
        'date': '2026-11-24',
        'cat': 'Brand & market',
        'time': '7 min',
        'es': {
            'title': 'Cómo crear tu propia marca de cosmética en España',
            'seo_title': 'Cómo crear tu propia marca de cosmética en España (guía 2026)',
            'description': 'Pasos para lanzar tu marca de cosmética: marca blanca o fórmula a medida, laboratorio, normativa UE, packaging, pedido mínimo y costes. Guía práctica.',
            'excerpt': 'Las siete decisiones para lanzar tu línea: marca blanca o fórmula a medida, laboratorio, normativa, packaging, pedido mínimo y plazos.',
            'keywords': ['crear marca de cosmética propia', 'fabricar cosméticos con mi marca', 'cosmética marca blanca', 'laboratorio cosmético para marcas', 'pedido mínimo cosméticos'],
            'faq': [
                ('¿Cuál es el pedido mínimo para fabricar cosméticos con mi marca?',
                 'Depende del laboratorio y del envase. En Gecanor parte de 500 unidades por referencia, lo que permite lanzar sin grandes volúmenes.'),
                ('¿Necesito ser laboratorio o tener instalaciones para tener una marca de cosmética?',
                 'No. Puedes encargar la fabricación a un laboratorio autorizado. Lo que sí necesitas es una persona responsable que garantice el cumplimiento del Reglamento 1223/2009.'),
                ('¿La fórmula será mía?',
                 'En marca blanca, no: es del laboratorio. En una fórmula a medida puede serlo si queda pactado; en Gecanor la propiedad intelectual de las fórmulas a medida es de tu marca.'),
                ('¿Tengo que registrar el cosmético en Sanidad?',
                 'No hay una autorización previa por producto: se notifica en el portal europeo CPNP antes de venderlo y se mantiene el PIF a disposición de las autoridades.'),
                ('¿Puedo vender en toda la UE con la misma notificación?',
                 'Sí. La notificación CPNP es única para toda la Unión Europea, aunque la etiqueta debe estar en la lengua de cada país donde vendas.'),
            ],
            'cta': 'Si estás pensando en tu propia línea, cuéntanos el proyecto. Te respondemos con un primer estudio de viabilidad en 48 horas.',
        },
        'sources': [
            ('Reglamento (CE) n.º 1223/2009 sobre los productos cosméticos', 'https://eur-lex.europa.eu/eli/reg/2009/1223/oj/spa'),
            ('AEMPS · Declaración responsable de fabricación e importación de cosméticos', 'https://www.aemps.gob.es/preguntas-y-respuestas-mas-frecuentes-sobre-la-declaracion-responsable-de-actividades-de-fabricacion-y-o-importacion-de-productos-cosmeticos/'),
            ('AEMPS · Garantías sanitarias de los productos cosméticos', 'https://www.aemps.gob.es/informa/notasinformativas/cosmeticos-cuidado-personal/2016/cos_2-2016-garantias-sanitarias/'),
        ],
    },
    {
        'slug': 'fabricar-marca-de-cosmetica',
        'date': '2026-11-26',
        'cat': 'Formulation',
        'time': '6 min',
        'es': {
            'title': 'Fabricar tu marca de cosmética: fases, plazos y con cuántas unidades empezar',
            'seo_title': 'Fabricar tu marca de cosmética: plazos y pocas unidades',
            'description': 'Cómo y cuánto se tarda en fabricar tu marca de cosmética: marca blanca o a medida, laboratorio a terceros, pedido mínimo desde 500 unidades, ensayos y plazos.',
            'excerpt': 'Las seis fases para fabricar tu marca de cosmética, con cuántas unidades se puede empezar y cómo lanzar antes con marca blanca.',
            'keywords': ['fabricación marca de cosmética', 'laboratorio para fabricar marca de cosmética pocas unidades', 'fabricar marca blanca cosméticos', 'creación marca de cosmética', 'fabricar cosméticos con mi marca', 'fabricación de cosméticos a terceros', 'cuánto se tarda en fabricar un cosmético', 'pedido mínimo cosméticos'],
            'faq': [
                ('¿Cuánto se tarda en fabricar mi marca de cosmética?',
                 'Como orientación, unas 7 semanas con una fórmula de marca blanca y un envase de catálogo, de 2 a 4 meses si el envase es personalizado y unos 3 meses con una fórmula a medida, que necesita formulación y ensayos de estabilidad, compatibilidad y conservación.'),
                ('¿Qué es lo que más alarga el desarrollo de un cosmético?',
                 'Los ensayos de validación y el packaging personalizado. El challenge test, por ejemplo, dura como mínimo 28 días según el método ISO 11930.'),
                ('¿Es más rápido fabricar cosméticos de marca blanca?',
                 'Sí. La fórmula ya está desarrollada y tiene sus estudios hechos, así que te saltas la formulación y la mayoría de ensayos.'),
                ('¿Puedo cambiar el envase cuando la fórmula ya está aprobada?',
                 'Sí, pero hay que repetir el ensayo de compatibilidad entre fórmula y envase, lo que retrasa el lanzamiento.'),
                ('¿Dónde puedo fabricar mi marca de cosmética con pocas unidades?',
                 'En un laboratorio de fabricación a terceros que acepte tiradas cortas. En Gecanor coordinamos la fabricación con laboratorios españoles desde 500 unidades por referencia.'),
            ],
            'cta': 'Si tienes una idea de producto y quieres saber qué plazo realista tendría, cuéntanosla. Te respondemos con un primer estudio de viabilidad en 48 horas.',
        },
        'sources': [
            ('Reglamento (CE) n.º 1223/2009 sobre los productos cosméticos', 'https://eur-lex.europa.eu/eli/reg/2009/1223/oj/spa'),
            ('Cosmetics Europe · Guidelines on stability testing of cosmetic products', 'https://www.cosmeticseurope.eu/files/5914/6407/8121/Guidelines_on_Stability_Testing_of_Cosmetics_CE-CTFA_-_2004.pdf'),
            ('ISO 11930:2019 · Evaluación de la protección antimicrobiana de un producto cosmético', 'https://www.iso.org/standard/75058.html'),
            ('ISO/TR 18811:2018 · Directrices sobre ensayos de estabilidad de cosméticos', 'https://www.iso.org/standard/63465.html'),
        ],
    },
    {
        'slug': 'lanzar-marca-complementos-alimenticios',
        'date': '2026-11-26',
        'cat': 'Regulatory',
        'time': '6 min',
        'es': {
            'title': 'Cómo lanzar una marca de complementos alimenticios en España',
            'seo_title': 'Cómo lanzar una marca de complementos alimenticios en España',
            'description': 'Registro sanitario, notificación de puesta en el mercado, composición, etiqueta y alegaciones de salud: lo que necesitas para vender suplementos en España.',
            'excerpt': 'Registro sanitario, notificación, ingredientes permitidos, etiqueta y alegaciones de salud: lo que necesitas para vender suplementos con tu marca.',
            'keywords': ['crear marca de complementos alimenticios', 'comercializar suplementos en España', 'notificación complementos alimenticios', 'registro sanitario RGSEAA', 'etiquetado complementos alimenticios', 'alegaciones de salud suplementos'],
            'faq': [
                ('¿Necesito registro sanitario para vender suplementos con mi marca?',
                 'Sí. La empresa que los comercializa debe estar inscrita en el RGSEAA, aunque no fabrique.'),
                ('¿Dónde se notifica un complemento alimenticio?',
                 'Ante la autoridad sanitaria de la comunidad autónoma donde tiene el domicilio social la empresa responsable de la primera puesta en el mercado; en Cataluña, la Agència de Salut Pública de Catalunya.'),
                ('¿Hay que esperar a la respuesta para empezar a vender?',
                 'No: la notificación es previa o simultánea a la primera comercialización. Aun así, la autoridad puede pedir cambios después.'),
                ('¿Puedo decir que mi suplemento mejora la piel?',
                 'Solo con declaraciones autorizadas en la lista europea y con sus condiciones exactas. Frases libres o que aluden a curar o prevenir enfermedades están prohibidas.'),
                ('¿Se aplica la misma normativa que a los cosméticos?',
                 'No. Los complementos son alimentos y siguen la normativa alimentaria (RD 1487/2009, Reglamentos 1169/2011 y 1924/2006); los cosméticos siguen el Reglamento 1223/2009.'),
            ],
            'cta': 'En Gecanor desarrollamos complementos alimenticios y nutricosmética y coordinamos el registro y la notificación. Si quieres añadir una línea de suplementos a tu marca, cuéntanos tu idea.',
        },
        'sources': [
            ('AESAN · Complementos alimenticios', 'https://www.aesan.gob.es/en/seguridad-alimentaria/alimentos-especificos/complementos-alimenticios'),
            ('Junta de Castilla y León · Procedimiento para comercializar un complemento alimenticio en España', 'https://www.saludcastillayleon.es/profesionales/es/seguridad-alimentaria/comercializacion-complementos-alimenticios/procedimiento-comercializar-complemento-alimenticio-espana'),
            ('Comunidad de Madrid · Notificación de puesta en el mercado de complementos alimenticios', 'https://sede.comunidad.madrid/comunicaciones-declaraciones/notificapuesta-mercado-complealimentic'),
            ('Govern de les Illes Balears · Los complementos alimentarios', 'https://www.caib.es/sites/seguretatalimentaria/es/complementos_alimenticios/'),
            ('Reglamento (UE) 432/2012 · Declaraciones de propiedades saludables autorizadas', 'https://eur-lex.europa.eu/eli/reg/2012/432/oj/spa'),
        ],
    },
    {
        'slug': 'requisitos-legales-cosmeticos-ue',
        'date': '2026-12-01',
        'cat': 'Regulatory',
        'time': '7 min',
        'es': {
            'title': 'Requisitos legales para vender cosméticos en la UE: persona responsable, PIF y CPNP',
            'seo_title': 'Requisitos para vender cosméticos en la UE: PIF, CPNP y más',
            'description': 'Qué exige el Reglamento 1223/2009 antes de vender un cosmético: persona responsable, evaluación de seguridad, PIF, notificación CPNP y etiquetado.',
            'excerpt': 'Persona responsable, evaluación de seguridad, PIF, notificación CPNP y etiqueta: los cinco requisitos antes de la primera venta.',
            'keywords': ['requisitos para vender cosméticos', 'notificación CPNP', 'qué es el PIF cosmético', 'persona responsable cosméticos', 'registro de cosméticos en España', 'declaración responsable AEMPS'],
            'faq': [
                ('¿Hay que registrar un cosmético en Sanidad para venderlo?',
                 'No hay autorización previa por producto. Se notifica en el CPNP antes de venderlo y el PIF queda a disposición de las autoridades.'),
                ('¿Quién hace la evaluación de seguridad?',
                 'Un evaluador con la cualificación que exige el artículo 10 del Reglamento 1223/2009, normalmente un farmacéutico, toxicólogo o titulado equivalente.'),
                ('¿Cuánto tiempo hay que guardar el PIF?',
                 'Diez años desde que se comercializa el último lote del producto.'),
                ('¿Sirve la notificación CPNP para vender en otros países de la UE?',
                 'Sí, es única para toda la UE. Lo que cambia es el idioma de la etiqueta.'),
                ('¿Necesito declaración responsable ante la AEMPS si solo tengo la marca?',
                 'No, si no fabricas ni importas de fuera de la UE: la necesita el laboratorio que fabrica, envasa o etiqueta. Sí la necesitas si importas.'),
            ],
            'cta': 'En Gecanor coordinamos los ensayos, el PIF, la evaluación de seguridad y la notificación CPNP de cada producto que desarrollamos. Si tienes un producto a punto de lanzar, cuéntanos en qué punto estás.',
        },
        'sources': [
            ('Reglamento (CE) n.º 1223/2009 sobre los productos cosméticos', 'https://eur-lex.europa.eu/eli/reg/2009/1223/oj/spa'),
            ('Real Decreto 85/2018 por el que se regulan los productos cosméticos', 'https://www.boe.es/eli/es/rd/2018/02/23/85'),
            ('AEMPS · Preguntas frecuentes sobre el Reglamento 1223/2009', 'https://www.aemps.gob.es/cosmeticos-y-cuidado-personal/cosmeticoshigiene_cosmeticos/faqs-reglamento-ce-1223-2009/'),
            ('AEMPS · Declaración responsable de fabricación e importación de cosméticos', 'https://www.aemps.gob.es/preguntas-y-respuestas-mas-frecuentes-sobre-la-declaracion-responsable-de-actividades-de-fabricacion-y-o-importacion-de-productos-cosmeticos/'),
            ('Comisión Europea · Guía del portal CPNP', 'https://ec.europa.eu/docsroom/documents/29563/attachments/1/translations/es/renditions/pdf'),
            ('Decisión 2013/674/UE · Directrices del anexo I (informe de seguridad)', 'https://eur-lex.europa.eu/eli/dec_impl/2013/674/oj'),
        ],
    },
]

for _a in ARTICLES:
    _a.update(TR.get(_a['slug'], {}))
